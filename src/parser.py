import re


def extract_name(resume_text):
    """Extract candidate name from resume text."""
    match = re.search(
        r"(?im)^name\s*:\s*(.+)$",
        resume_text
    )

    if match:
        return match.group(1).strip().title()

    return None


def extract_email(resume_text):
    """Extract email address from resume text."""
    match = re.search(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        resume_text
    )

    if match:
        return match.group(0).lower()

    return None


def extract_skills(resume_text):
    """Extract skills from a Skills section."""
    match = re.search(
        r"(?im)^skills\s*:\s*(.+)$",
        resume_text
    )

    if not match:
        return []

    skills = match.group(1).split(",")

    return [skill.strip() for skill in skills if skill.strip()]


def extract_experience(resume_text):
    """Extract years of experience from resume text."""
    match = re.search(
        r"(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)\s+(?:of\s+)?experience",
        resume_text,
        re.IGNORECASE
    )

    if match:
        return float(match.group(1))

    return 0.0


def parse_resume(resume_text):
    """Parse a resume and return structured information."""
    if not resume_text or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    return {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "skills": extract_skills(resume_text),
        "experience": extract_experience(resume_text)
    }