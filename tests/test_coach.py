import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.career_coach import generate_career_plan

print(
    generate_career_plan(
        profile={"CGPA": 8.5},
        readiness_score=82,
        skills="Python, SQL, Power BI",
        target_role="Data Analyst",
        target_company="TCS"
    )
)