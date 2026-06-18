import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.rag_engine import ask_interview_assistant

print(
    ask_interview_assistant(
        "What is polymorphism in Python?"
    )
)