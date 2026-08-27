def calculate_match(resume, job_requirements):
    """Calculate how well a resume matches job requirements."""

    resume_skills = resume.get("skills", [])
    required_skills = job_requirements.get("skills", [])

    # Normalize skills for comparison
    resume_skills_normalized = {
        skill.strip().lower() for skill in resume_skills
    }

    required_skills_normalized = {
        skill.strip().lower() for skill in required_skills
    }

    # Find matching skills
    matched_normalized = (
        resume_skills_normalized & required_skills_normalized
    )

    # Keep original skill names from the resume
    matched_skills = [
        skill for skill in resume_skills
        if skill.strip().lower() in matched_normalized
    ]

    # Calculate skill score
    if required_skills_normalized:
        skill_score = (
            len(matched_normalized)
            / len(required_skills_normalized)
        ) * 100
    else:
        skill_score = 0.0

    # Calculate experience score
    resume_experience = resume.get("experience", 0)
    required_experience = job_requirements.get("experience", 0)

    if required_experience <= 0:
        experience_score = 100.0
    else:
        experience_score = min(
            resume_experience / required_experience * 100,
            100.0
        )

    # Weighted final score
    match_score = (
        skill_score * 0.70 +
        experience_score * 0.30
    )

    # Recommendation
    if match_score >= 70:
        recommendation = "Recommended"
    elif match_score >= 50:
        recommendation = "Consider"
    else:
        recommendation = "Not Recommended"

    return {
        "matched_skills": matched_skills,
        "skill_score": round(skill_score, 2),
        "experience_score": round(experience_score, 2),
        "match_score": round(match_score, 2),
        "recommendation": recommendation
    }