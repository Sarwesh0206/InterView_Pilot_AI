import joblib
import pandas as pd

# Load model once
model = joblib.load(
    "models/placement_readiness_model.pkl"
)

def predict_readiness(
    cgpa,
    internships,
    projects,
    workshops,
    aptitude,
    softskills,
    extracurricular,
    placement_training,
    ssc_marks,
    hsc_marks
):

    input_df = pd.DataFrame([{
        "CGPA": cgpa,
        "Internships": internships,
        "Projects": projects,
        "Workshops/Certifications": workshops,
        "AptitudeTestScore": aptitude,
        "SoftSkillsRating": softskills,
        "ExtracurricularActivities": extracurricular,
        "PlacementTraining": placement_training,
        "SSC_Marks": ssc_marks,
        "HSC_Marks": hsc_marks
    }])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    return prediction, round(probability * 100, 2)