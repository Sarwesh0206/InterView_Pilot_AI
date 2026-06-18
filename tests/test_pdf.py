import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.pdf_generator import create_career_report_pdf

create_career_report_pdf(
    "career_report.pdf",
    {"CGPA": 8.5},
    82,
    "This is a sample career report."
)

print("PDF Created")