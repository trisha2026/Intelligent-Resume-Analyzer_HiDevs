import json

from src.parser import parse_resume
from src.matcher import calculate_match
from src.report import generate_report, save_report, load_report


def main():
    print("Enter resume text.")
    print("Type END on a new line when finished:")

    resume_lines = []

    while True:
        line = input()
        if line.strip() == "END":
            break
        resume_lines.append(line)

    resume_text = "\n".join(resume_lines)

    print("Enter required skills (comma-separated):")
    required_skills = input().split(",")

    job_requirements = {
        "skills": [skill.strip() for skill in required_skills]
    }

    try:
        resume = parse_resume(resume_text)
        match_result = calculate_match(resume, job_requirements)
        report = generate_report(resume, match_result)

        # Save report to JSON
        save_report(report)

        # Load report back from JSON
        loaded_report = load_report()

        print("\nResume Analysis")
        print(json.dumps(loaded_report, indent=2))

        print("\nReport saved and loaded successfully.")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()