import pandas as pd

def calculate_success_score(
    gpa,
    internships,
    projects,
    certifications,
    networking,
    soft_skills
):
    score = (
        gpa * 20
        + internships * 4
        + projects * 2
        + certifications * 3
        + networking * 5
        + soft_skills * 5
    )

    return min(round(score), 100)


def calculate_promotion_score(
    projects,
    certifications,
    networking,
    soft_skills
):
    score = (
        projects * 5
        + certifications * 5
        + networking * 10
        + soft_skills * 10
    )

    return min(round(score), 100)


def career_level(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "High"

    elif score >= 50:
        return "Moderate"

    return "Needs Improvement"
