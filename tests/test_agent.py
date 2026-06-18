import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.agent_graph import agent_graph

result = agent_graph.invoke(
    {
        "query":
        "How can I improve my placement chances?"
    }
)

print(result["response"])