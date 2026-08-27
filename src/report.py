def generate_report(resume, match_result):
    score = match_result["skill_score"]

    if score >= 80:
        recommendation = "Strongly Recommended"
    elif score >= 60:
        recommendation = "Recommended"
    elif score >= 40:
        recommendation = "Consider"
    else:
        recommendation = "Not Recommended"

    return {
        "candidate": resume.get("name"),
        "email": resume.get("email"),
        "experience_years": resume.get("experience"),
        "matched_skills": match_result["matched_skills"],
        "match_score": score,
        "recommendation": recommendation
    }

import json


def save_report(report, filename="data/resume_report.json"):
    """Save the report to a JSON file."""
    with open(filename, "w") as file:
        json.dump(report, file, indent=2)


def load_report(filename="data/resume_report.json"):
    """Load a report from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)