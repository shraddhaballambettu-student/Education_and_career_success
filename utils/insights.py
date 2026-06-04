def generate_recommendations(
    gpa,
    internships,
    projects,
    certifications,
    networking,
    soft_skills
):

    recommendations = []

    if gpa < 3.2:
        recommendations.append(
            "Improve GPA through advanced courses."
        )

    if internships < 2:
        recommendations.append(
            "Gain additional internship experience."
        )

    if projects < 5:
        recommendations.append(
            "Build more real-world projects."
        )

    if certifications < 3:
        recommendations.append(
            "Earn industry certifications."
        )

    if networking < 7:
        recommendations.append(
            "Increase professional networking."
        )

    if soft_skills < 7:
        recommendations.append(
            "Develop leadership and communication skills."
        )

    return recommendations
