# 🚀 InterviewPilot AI

An AI-powered Career Guidance, Placement Readiness Assessment, and Interview Preparation Platform built using Machine Learning, LangGraph, LangChain, Groq LLM, ChromaDB, and Streamlit.

InterviewPilot AI helps students understand their placement readiness, identify skill gaps, receive personalized career guidance, prepare for interviews, and generate professional career development reports.

---

# 🎯 Project Vision

Many students struggle with:

* Understanding their placement readiness
* Identifying missing skills
* Preparing for company-specific interviews
* Creating a structured learning roadmap
* Receiving personalized career guidance

InterviewPilot AI addresses these challenges by combining Machine Learning, Retrieval-Augmented Generation (RAG), and Multi-Agent AI systems into a single intelligent platform.

---

# ✨ Key Features

## 📊 Placement Readiness Predictor

Analyze a student's academic and professional profile to estimate placement readiness.

Evaluates:

* CGPA
* Internships
* Projects
* Certifications
* Aptitude Skills
* Soft Skills
* Extracurricular Activities
* Placement Training
* SSC Marks
* HSC Marks

Provides:

* Placement Readiness Score
* Readiness Insights
* Improvement Suggestions

---

## 🧠 AI Career Coach

A personalized AI career mentor that provides:

* Career readiness evaluation
* Skill gap analysis
* Role-specific guidance
* Company-specific preparation strategies
* Learning roadmaps
* Resume improvement suggestions
* LinkedIn optimization recommendations

Supported roles include:

* Data Analyst
* Data Scientist
* Machine Learning Engineer
* Software Developer
* Business Analyst
* And more

---

## 🎤 AI Interview Assistant

A Retrieval-Augmented Generation (RAG) powered assistant designed for placement preparation.

Supports:

### Technical Domains

* Python
* SQL
* Machine Learning
* Data Analytics
* Statistics

### Interview Categories

* Technical Interviews
* HR Interviews
* Aptitude Preparation
* Company-Specific Questions

### Companies Covered

* TCS
* Infosys
* Wipro
* Accenture
* Cognizant
* Common Placement Questions

Provides:

* Detailed explanations
* Interview tips
* Common mistakes
* Real-world examples
* Practical use cases

---

## 🤖 Multi-Agent AI Architecture

The platform utilizes LangGraph to orchestrate multiple specialized AI agents.

### Router Agent

Analyzes user queries and determines the most appropriate agent.

### Placement Agent

Handles placement readiness assessment and prediction workflows.

### Career Coach Agent

Generates personalized career guidance and improvement plans.

### Interview Assistant Agent

Retrieves knowledge from the RAG knowledge base and generates interview-focused responses.

### Report Agent

Creates professional and structured outputs for users.

This architecture enables intelligent task delegation and scalable AI workflows.

---

## 📄 Professional Career Report Generation

Generate downloadable PDF reports containing:

* Placement Readiness Analysis
* Profile Evaluation
* Skill Gap Analysis
* Technical Learning Roadmap
* Project Recommendations
* Interview Preparation Strategy
* Resume Suggestions
* LinkedIn Recommendations
* Company-Specific Preparation Plan
* 30-Day Placement Roadmap

---

# 🏗️ System Architecture

Student Input

⬇️

LangGraph Router Agent

⬇️

Placement Agent / Career Coach Agent / Interview Assistant Agent

⬇️

Machine Learning + RAG + LLM Processing

⬇️

Personalized Recommendations

⬇️

PDF Career Report Generation

---

# 🛠️ Technology Stack

## Frontend

* Streamlit

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

## Large Language Models

* Groq
* Llama 3.3 70B Versatile

## AI Frameworks

* LangChain
* LangGraph

## Retrieval-Augmented Generation (RAG)

* ChromaDB
* HuggingFace Embeddings
* Sentence Transformers

## Report Generation

* ReportLab

## Deployment

* Streamlit Community Cloud

---

# 📂 Project Structure

```text
InterView_Pilot_AI/

├── app/
│   └── app.py

├── src/
│   ├── predictor.py
│   ├── ml_agent.py
│   ├── rag_engine.py
│   ├── career_coach.py
│   ├── pdf_generator.py
│   └── agent_graph.py

├── data/
│   └── rag_data/

├── models/
│   └── placement_readiness_model.pkl

├── vector_db/

├── tests/

├── requirements.txt

└── README.md
```

---

# 📚 Knowledge Base

The RAG system uses custom knowledge sources covering:

* Python
* SQL
* Machine Learning
* Aptitude
* HR Interviews
* Placement Preparation
* Company-Specific Questions
* Interview Tips

This enables context-aware and domain-specific responses.

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Sarwesh0206/InterView_Pilot_AI.git
```

Navigate to the project directory:

```bash
cd InterView_Pilot_AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/app.py
```

---

# 🌐 Live Demo

Deployment Link:

https://interviewpilotai.streamlit.app/

---

# 🔮 Future Enhancements

Planned improvements:

* ATS Resume Analyzer
* Resume Scoring System
* Mock Interview Simulator
* Voice-Based Interview Practice
* Company-Wise Assessment Tests
* AI Resume Builder
* Job Recommendation Engine
* Personalized Learning Tracker
* Interview Performance Analytics

---

# 💡 Learning Outcomes

Through this project, I gained practical experience in:

* Machine Learning Deployment
* Retrieval-Augmented Generation (RAG)
* LangChain Workflows
* LangGraph Multi-Agent Systems
* Vector Databases
* LLM Integration
* Streamlit Application Development
* AI-Powered Career Guidance Systems

---

# 👨‍💻 Author

### Sarweshwaran

Electronics & Instrumentation Engineering

Puducherry Technological University

Passionate about Machine Learning, Data Analytics, AI Applications, and Intelligent Systems.

---

## ⭐ If you found this project useful, consider giving the repository a star.
