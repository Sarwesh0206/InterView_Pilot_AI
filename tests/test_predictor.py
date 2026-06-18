import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.predictor import predict_readiness

prediction, score = predict_readiness(
    8.5,
    2,
    3,
    4,
    80,
    8,
    "Yes",
    "Yes",
    85,
    88
)

print("Prediction:", prediction)
print("Readiness Score:", score)