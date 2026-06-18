from src.predictor import predict_readiness


def ml_agent(profile):


    score = predict_readiness(
    profile.get("CGPA", 0),
    profile.get("Internships", 0),
    profile.get("Projects", 0),
    profile.get("Workshops", 0),
    profile.get("Aptitude", 0),
    profile.get("SoftSkills", 0),
    profile.get("Extracurricular", 0),
    profile.get("PlacementTraining", 0),
    profile.get("SSC_Marks", 0),
    profile.get("HSC_Marks", 0)
)

    return {
        "readiness_score": score
    }