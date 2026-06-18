
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def create_career_report_pdf(
    filename,
    profile,
    readiness_score,
    report
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    # ------------------------------------------------
    # TITLE
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "InterviewPilot AI Career Report",
            title_style
        )
    )

    elements.append(Spacer(1, 12))

    # ------------------------------------------------
    # SUMMARY
    # ------------------------------------------------

    elements.append(
        Paragraph(
            f"<b>Placement Readiness Score:</b> {readiness_score}%",
            heading_style
        )
    )

    elements.append(Spacer(1, 12))

    # ------------------------------------------------
    # PROFILE SUMMARY
    # ------------------------------------------------

    profile_text = f"""
    <b>CGPA:</b> {profile.get('CGPA','N/A')}<br/>
    <b>Projects:</b> {profile.get('Projects','N/A')}<br/>
    <b>Internships:</b> {profile.get('Internships','N/A')}<br/>
    <b>Aptitude Score:</b> {profile.get('Aptitude','N/A')}<br/>
    <b>Soft Skills:</b> {profile.get('SoftSkills','N/A')}<br/>
    """

    elements.append(
        Paragraph(
            profile_text,
            body_style
        )
    )

    elements.append(Spacer(1, 15))

    # ------------------------------------------------
    # REPORT CONTENT
    # ------------------------------------------------

    for line in report.split("\n"):

        line = line.strip()

        if not line:
            continue

        # Markdown heading
        if line.startswith("#"):

            clean_heading = line.replace("#", "").strip()

            elements.append(
                Paragraph(
                    clean_heading,
                    heading_style
                )
            )

            elements.append(
                Spacer(1, 8)
            )

        else:

            elements.append(
                Paragraph(
                    line,
                    body_style
                )
            )

            elements.append(
                Spacer(1, 4)
            )

    doc.build(elements)

    return filename

