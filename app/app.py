import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import sys
import os
from dotenv import load_dotenv

# Try importing standard Groq/OpenAI/LangChain common exceptions for fallback
try:
    from groq import GroqError, RateLimitError, APIStatusError
except ImportError:
    # Fallback to general exceptions if the groq package isn't fully compiled in venv yet
    GroqError = Exception
    RateLimitError = Exception
    APIStatusError = Exception

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.rag_engine import ask_interview_assistant
from src.career_coach import generate_career_plan
from src.pdf_generator import create_career_report_pdf
from src.agent_graph import agent_graph

# PAGE CONFIG
st.set_page_config(
    page_title="InterviewPilot AI",
    page_icon="🚀",
    layout="wide"
)

if "readiness_score" not in st.session_state:
    st.session_state["readiness_score"] = None

if "student_profile" not in st.session_state:
    st.session_state["student_profile"] = None

if "career_report" not in st.session_state:
    st.session_state["career_report"] = None

# LOAD CSS
css_path = Path(__file__).parent.parent / "assets" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# HELPER FUNCTION FOR GROQ ERROR UI HANDLING
def handle_groq_exception(e):
    """Displays user-friendly error messages based on the Groq exception type."""
    error_msg = str(e)
    if "rate_limit_exceeded" in error_msg.lower() or "429" in error_msg:
        st.error("⏳ **Groq API Rate Limit Hit:** You have exceeded the allowed requests per minute. Please wait a moment before trying again.")
    elif "api_key" in error_msg.lower() or "401" in error_msg:
        st.error("🔑 **Authentication Error:** Invalid or missing Groq API Key. Please check your `.env` configuration file.")
    elif "service_unavailable" in error_msg.lower() or "503" in error_msg:
        st.error("🖥️ **Groq Service Down:** The LLM service is temporarily unavailable. Please try again shortly.")
    else:
        st.error(f"❌ **Groq API Error:** {error_msg}")

# LOAD MODEL
try:
    model = joblib.load("models/placement_readiness_model.pkl")
except Exception:
    model = None

# SIDEBAR
st.sidebar.title("🚀 InterviewPilot AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Readiness Predictor",
        "Interview Assistant",
        "Career Coach",
        "AI Career Agent"
    ]
)

# DASHBOARD
if page == "Dashboard":
    st.title("🚀 InterviewPilot AI")
    st.subheader("Multi-Agent Career Guidance System")
    st.caption("Prepare Smarter • Interview Better • Get Hired Faster")
    st.divider()

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: st.metric("📊 ML Predictor", "Ready" if model else "Missing Model")
    with c2: st.metric("🎯 RAG Assistant", "Ready")
    with c3: st.metric("🧠 Career Coach", "Ready")
    with c4: st.metric("🤖 LangGraph Agent", "Ready")
    with c5: st.metric("🚀 Overall Status", "All Systems Go" if model else "Action Required")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.info("""
                ### 📊 Placement Readiness Predictor
                Predict placement readiness using a Machine Learning model based on student profile features.
                """)
        with st.container(border=True):
            st.success("""
                ### 🎯 Interview Assistant (RAG)
                Ask specialized core technical interview questions powered by document retrieval.
                """)
    with col2:
        with st.container(border=True):
            st.warning("""
                ### 🧠 AI Career Coach
                Generate comprehensive career roadmaps, skill analyses, and personalized action steps.
                """)
        with st.container(border=True):
            st.error("""
                ### 🤖 AI Career Agent (LangGraph)
                Multi-Agent Routing System dynamically processing complex user intents using specialized nodes.
                """)

# READINESS PREDICTOR
elif page == "Readiness Predictor":
    st.title("📊 Placement Readiness Predictor")
    col1, col2 = st.columns(2)
    
    with col1:
        cgpa = st.number_input("CGPA", 0.0, 10.0, 8.0)
        internships = st.number_input("Internships", 0, 10, 1)
        projects = st.number_input("Projects", 0, 20, 2)
        workshops = st.number_input("Workshops/Certifications", 0, 20, 2)
        aptitude = st.number_input("Aptitude Test Score", 0, 100, 75)
    with col2:
        softskills = st.number_input("Soft Skills Rating", 0, 10, 5)
        extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])
        placement_training = st.selectbox("Placement Training", ["No", "Yes"])
        ssc_marks = st.number_input("SSC Marks", 0, 100, 85)
        hsc_marks = st.number_input("HSC Marks", 0, 100, 85)

    st.write("### Prediction Result")
    if st.button("🚀 Predict Readiness"):
        if model is None:
            st.error("Machine learning model file could not be loaded. Please ensure `models/placement_readiness_model.pkl` exists.")
        else:
            try:
                input_df = pd.DataFrame({
                    "CGPA": [cgpa],
                    "Internships": [internships],
                    "Projects": [projects],
                    "Workshops/Certifications": [workshops],
                    "AptitudeTestScore": [aptitude],
                    "SoftSkillsRating": [softskills],
                    "ExtracurricularActivities": [extracurricular],
                    "PlacementTraining": [placement_training],
                    "SSC_Marks": [ssc_marks],
                    "HSC_Marks": [hsc_marks]
                })

                probability = model.predict_proba(input_df)[0][1]
                score = round(probability * 100, 2)
                st.session_state["readiness_score"] = score
                st.session_state["student_profile"] = {
                    "CGPA": cgpa, "Internships": internships, "Projects": projects,
                    "Workshops": workshops, "Aptitude": aptitude, "SoftSkills": softskills,
                    "Extracurricular": extracurricular, "PlacementTraining": placement_training,
                    "SSC_Marks": ssc_marks, "HSC_Marks": hsc_marks
                }
                
                st.success(f"🎯 Placement Probability: {score}%")
                if score >= 80:
                    st.success("Excellent placement readiness!")
                elif score >= 60:
                    st.info("Good profile. Keep improving projects and aptitude.")
                else:
                    st.warning("Focus on skills, certifications and placement preparation.")
            except Exception as e:
                st.error(f"Error executing prediction logic: {e}")

# INTERVIEW ASSISTANT
elif page == "Interview Assistant":
    st.title("🎯 AI Interview Assistant")
    st.write("Ask questions about Python, SQL, OOP, DBMS, Aptitude, TCS Interviews and more.")

    question = st.text_area("Enter your question:", height=120)
    if st.button("🚀 Ask AI"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Quizzing RAG Engine..."):
                try:
                    answer = ask_interview_assistant(question)
                    st.success("Answer Generated Successfully")
                    st.markdown(answer)
                except (GroqError, RateLimitError, APIStatusError) as ge:
                    handle_groq_exception(ge)
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")

# CAREER COACH
elif page == "Career Coach":
    st.title("🧠 AI Career Coach")
    profile = st.session_state.get("student_profile")
    readiness_score = st.session_state.get("readiness_score")

    if profile is None:
        st.warning("Please run the Placement Readiness Predictor tab first to establish your baseline profile attributes.")
    else:
        st.success(f"Current Baseline Readiness Score: {readiness_score}%")
        skills = st.text_area("Current Technical Skills", placeholder="Python, SQL, Power BI...")
        target_role = st.text_input("Target Role", placeholder="Data Analyst")
        target_company = st.text_input("Target Company", placeholder="TCS")

        if st.button("🚀 Generate Career Plan"):
            if not skills or not target_role or not target_company:
                st.warning("Please fill out all missing technical inputs.")
            else:
                with st.spinner("Analyzing profile requirements against live benchmarks..."):
                    try:
                        report = generate_career_plan(
                            profile=profile,
                            readiness_score=readiness_score,
                            skills=skills,
                            target_role=target_role,
                            target_company=target_company
                        )
                        st.markdown("---")
                        st.session_state["career_report"] = report
                        st.markdown(report)
                        
                        pdf_file = create_career_report_pdf(
                            "career_report.pdf",
                            profile,
                            readiness_score,
                            report
                        )

                        with open(pdf_file, "rb") as file:
                            st.download_button(
                                label="📄 Download Career Report",
                                data=file,
                                file_name="InterviewPilot_Career_Report.pdf",
                                mime="application/pdf"
                            )
                    except (GroqError, RateLimitError, APIStatusError) as ge:
                        handle_groq_exception(ge)
                    except Exception as e:
                        st.error(f"An unexpected error occurred while compiling your report: {e}")

# AI CAREER AGENT
elif page == "AI Career Agent":
    st.title("🤖 AI Career Agent")
    query = st.text_area("Ask Anything (Multi-Agent Routing System)")

    if st.button("🚀 Ask Agent"):
        if query.strip() == "":
            st.warning("Please ask a contextual question.")
        else:
            with st.spinner("Routing query through LangGraph agents..."):
                try:
                    result = agent_graph.invoke({
                        "query": query,
                        "profile": st.session_state.get("student_profile"),
                        "readiness_score": st.session_state.get("readiness_score")
                    })
                    st.markdown(result.get("response", "No response object received from backend graph agents."))
                except (GroqError, RateLimitError, APIStatusError) as ge:
                    handle_groq_exception(ge)
                except Exception as e:
                    st.error(f"LangGraph Orchestration Interruption: {e}")

st.divider()
st.caption("InterviewPilot AI • ML + RAG + LangGraph Multi-Agent Career Guidance System")