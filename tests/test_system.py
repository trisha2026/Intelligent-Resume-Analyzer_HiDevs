import unittest

from src.parser import parse_resume
from src.matcher import calculate_match
from src.report import generate_report


class TestResumeParser(unittest.TestCase):

    def test_complete_resume(self):
        resume = """Name: John Doe
Email: john@example.com
Skills: Python, SQL, Git
3 years of experience"""

        result = parse_resume(resume)

        self.assertEqual(result["name"], "John Doe")
        self.assertEqual(result["email"], "john@example.com")
        self.assertEqual(result["skills"], ["Python", "SQL", "Git"])
        self.assertEqual(result["experience"], 3.0)

    def test_missing_email(self):
        resume = """Name: Jane Smith
Skills: Java, Docker
5 years of experience"""

        result = parse_resume(resume)

        self.assertEqual(result["name"], "Jane Smith")
        self.assertIsNone(result["email"])

    def test_empty_resume(self):
        with self.assertRaises(ValueError):
            parse_resume("")

    def test_missing_skills(self):
        resume = """Name: Jane Smith
Email: jane@example.com
5 years of experience"""

        result = parse_resume(resume)

        self.assertEqual(result["name"], "Jane Smith")
        self.assertEqual(result["skills"], [])

    def test_case_insensitive_email(self):
        resume = """Name: JOHN DOE
Email: JOHN@EXAMPLE.COM
Skills: Python
3 years of experience"""

        result = parse_resume(resume)

        self.assertEqual(result["name"], "John Doe")
        self.assertEqual(result["email"], "john@example.com")

    def test_missing_name(self):
        resume = """Email: test@example.com
Skills: Python
2 years of experience"""

        result = parse_resume(resume)

        self.assertIsNone(result["name"])

    def test_empty_skills(self):
        resume = """Name: John Doe
Email: john@example.com
2 years of experience"""

        result = parse_resume(resume)

        self.assertEqual(result["skills"], [])


class TestMatcher(unittest.TestCase):

    def test_skill_matching(self):
        resume = {
            "skills": ["Python", "SQL", "Java"]
        }

        job = {
            "skills": ["Python", "SQL", "Git"]
        }

        result = calculate_match(resume, job)

        self.assertEqual(
            result["matched_skills"],
            ["Python", "SQL"]
        )

        self.assertAlmostEqual(
            result["skill_score"],
            66.67,
            places=2
        )

    def test_no_matching_skills(self):
        resume = {
            "skills": ["Java", "C++"]
        }

        job = {
            "skills": ["Python", "SQL"]
        }

        result = calculate_match(resume, job)

        self.assertEqual(result["matched_skills"], [])
        self.assertEqual(result["skill_score"], 0.0)

    def test_case_insensitive_skill_matching(self):
        resume = {
            "skills": ["python", "SQL"]
        }

        job = {
            "skills": ["Python", "sql"]
        }

        result = calculate_match(resume, job)

        self.assertEqual(
            result["matched_skills"],
            ["python", "SQL"]
        )

        self.assertEqual(
            result["skill_score"],
            100.0
        )

    def test_empty_job_skills(self):
        resume = {
            "skills": ["Python", "SQL"],
            "experience": 3
        }

        job = {
            "skills": []
        }

        result = calculate_match(resume, job)

        self.assertEqual(result["matched_skills"], [])
        self.assertEqual(result["skill_score"], 0.0)

    def test_zero_experience(self):
        resume = {
            "skills": ["Python"],
            "experience": 0
        }

        job = {
            "skills": ["Python"],
            "experience": 2
        }

        result = calculate_match(resume, job)

        self.assertEqual(result["experience_score"], 0.0)


class TestReport(unittest.TestCase):

    def test_report_generation(self):
        resume = {
            "name": "John Doe",
            "email": "john@example.com",
            "experience": 3
        }

        match = {
            "matched_skills": ["Python", "SQL"],
            "skill_score": 66.67
        }

        result = generate_report(resume, match)

        self.assertEqual(result["candidate"], "John Doe")
        self.assertEqual(result["email"], "john@example.com")
        self.assertEqual(result["experience_years"], 3)
        self.assertEqual(
            result["matched_skills"],
            ["Python", "SQL"]
        )
        self.assertEqual(result["match_score"], 66.67)


if __name__ == "__main__":
    unittest.main()