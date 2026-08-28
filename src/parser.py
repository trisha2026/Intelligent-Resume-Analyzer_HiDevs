import re


def extract_name(resume_text):
    """Extract candidate name from resume text."""

    # Try explicit "Name:" format first.
    match = re.search(
        r"(?im)^name\s*:\s*(.+)$",
        resume_text
    )

    if match:
        return match.group(1).strip().title()

    lines = [
        line.strip()
        for line in resume_text.splitlines()
        if line.strip()
    ]

    section_words = [
        "professional",
        "summary",
        "skills",
        "experience",
        "education",
        "projects",
        "certifications",
        "achievements",
        "work experience",
    ]

    # Look for a name immediately before an email/contact line.
    for i, line in enumerate(lines):
        if "@" in line:
            if i > 0:
                possible_name = lines[i - 1].strip()

                if (
                    len(possible_name.split()) >= 2
                    and ":" not in possible_name
                    and not any(
                        word in possible_name.lower()
                        for word in section_words
                    )
                    and not any(char.isdigit() for char in possible_name)
                ):
                    return possible_name.title()

    # Fallback: look for a reasonable standalone name.
    for line in lines:
        if (
            len(line.split()) >= 2
            and ":" not in line
            and "@" not in line
            and not any(char.isdigit() for char in line)
            and not any(
                word in line.lower()
                for word in section_words
            )
        ):
            return line.title()

    return None


def extract_email(resume_text):
    """Extract and normalize email address."""

    match = re.search(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        resume_text
    )

    if match:
        return match.group(0).lower()

    return None


def extract_skills(resume_text):
    """Extract skills from simple and structured resume formats."""

    skills = []

    # ---------------------------------------------------------
    # Format 1:
    # Skills: Python, SQL, Git
    # ---------------------------------------------------------
    skills_match = re.search(
        r"(?im)^skills\s*:\s*(.+)$",
        resume_text
    )

    if skills_match:
        skills_text = skills_match.group(1)

        for skill in skills_text.split(","):
            skill = skill.strip()

            if skill:
                skills.append(skill)

        return skills

    # ---------------------------------------------------------
    # Format 2:
    #
    # SKILLS
    # Technical: Python, SQL, Git, Docker
    # Frameworks: Flask, FastAPI
    # Other: Data Processing, Unit Testing, JSON
    # ---------------------------------------------------------
    lines = resume_text.splitlines()

    in_skills_section = False

    section_headers = {
        "professional experience",
        "experience",
        "education",
        "projects",
        "certifications",
        "achievements",
        "work experience",
    }

    for line in lines:
        stripped = line.strip()

        if not stripped:
            continue

        lower = stripped.lower()

        if lower == "skills":
            in_skills_section = True
            continue

        if in_skills_section and lower in section_headers:
            break

        if in_skills_section:
            # Remove labels such as:
            # Technical:
            # Frameworks:
            # Other:
            line_without_label = re.sub(
                r"^[A-Za-z ]+\s*:\s*",
                "",
                stripped
            )

            parts = line_without_label.split(",")

            for skill in parts:
                skill = skill.strip()

                if skill:
                    skills.append(skill)

    return skills


def extract_experience(resume_text):
    """Extract years of professional experience."""

    # Example:
    # 3 years of experience
    # 4 years of experience
    match = re.search(
        r"(\d+(?:\.\d+)?)\s*\+?\s*years?\s+of\s+experience",
        resume_text,
        re.IGNORECASE
    )

    if match:
        return float(match.group(1))

    # Example:
    # Experience: 3 years
    # Experience: 3
    match = re.search(
        r"(?im)^experience\s*:\s*(\d+(?:\.\d+)?)",
        resume_text
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