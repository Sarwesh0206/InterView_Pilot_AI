
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# =====================================================
# LLM
# =====================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_tokens=3000
)


# =====================================================
# CAREER COACH
# =====================================================

def generate_career_plan(
    profile,
    readiness_score,
    skills,
    target_role,
    target_company
):

    prompt = f"""
You are a senior placement trainer, recruiter, career mentor, industry expert and interview coach.

Generate a highly detailed and personalized career report.

=====================================================
STUDENT PROFILE
=====================================================

Placement Readiness Score:
{readiness_score}%

Current Skills:
{skills}

Target Role:
{target_role}

Target Company:
{target_company}

=====================================================
ACADEMIC DETAILS
=====================================================

CGPA:
{profile.get("CGPA", "Not Available")}

Projects Completed:
{profile.get("Projects", "Not Available")}

Internships Completed:
{profile.get("Internships", "Not Available")}

Aptitude Score:
{profile.get("Aptitude", "Not Available")}

Soft Skills Rating:
{profile.get("SoftSkills", "Not Available")}

Workshops/Certifications:
{profile.get("Workshops", "Not Available")}

Placement Training:
{profile.get("PlacementTraining", "Not Available")}

SSC Marks:
{profile.get("SSC_Marks", "Not Available")}

HSC Marks:
{profile.get("HSC_Marks", "Not Available")}

=====================================================
REPORT REQUIREMENTS
=====================================================

Generate a professional report with the following sections:

# Career Readiness Analysis

Analyze the student's current placement readiness level.

Mention strengths and weaknesses.

# Profile Evaluation

Evaluate:

- CGPA
- Internships
- Projects
- Aptitude
- Communication Skills
- Academic Performance

# Skill Gap Analysis

Compare current skills with the skills required for the target role.

Identify missing skills.

# Technical Skills Roadmap

Recommend technologies, frameworks, tools and concepts to learn.

# Project Recommendations

Suggest 5 strong resume-worthy projects.

Explain why each project is useful.

# Interview Preparation Strategy

Provide preparation guidance for:

- Technical Interview
- HR Interview
- Aptitude Round
- Coding Round (if applicable)

# Resume Improvement Suggestions

Provide detailed resume recommendations.

# Certifications

Recommend useful certifications.

# LinkedIn Profile Suggestions

Provide LinkedIn improvement recommendations.

# 30-Day Placement Preparation Plan

Provide a detailed week-by-week roadmap.

Week 1:
Week 2:
Week 3:
Week 4:

# Company Specific Preparation

Explain how to prepare specifically for:

{target_company}

Include:

- Recruitment Process
- Important Topics
- Expected Interview Questions
- Aptitude Focus Areas

# Final Career Mentor Advice

Provide detailed practical guidance and motivation.

=====================================================
IMPORTANT
=====================================================

1. Be highly personalized.
2. Use the student profile data.
3. Give actionable recommendations.
4. Write at least 1000 words.
5. Use markdown headings and bullet points.
6. Make the report professional and detailed.
7. DO NOT use placeholders such as [Student Name], [Name], [Candidate Name].
8. DO NOT generate any student name.
9. Start directly with "# Career Readiness Analysis".

Use proper markdown formatting.

Use headings with # symbols.

Use bullet points.

Leave blank lines between sections.

Make the output PDF-friendly.
"""
    response = llm.invoke(prompt)

    report = response.content

    report = report.replace(
        "Career Report for [Student Name]",
        ""
    )

    report = report.replace(
        "[Student Name]",
        ""
    )

    report = report.replace(
        "[Name]",
        ""
    )

    return report
