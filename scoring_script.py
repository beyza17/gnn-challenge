import sys
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

# -----------------------------
# 1. Read submission path
# -----------------------------
if len(sys.argv) != 2:
    print("Usage: python scoring_script.py <github_beyza17.csv>")
    sys.exit(1)

submission_file = sys.argv[1]

# -----------------------------
# 2. Load files
# -----------------------------
submission = pd.read_csv(submission_file)
truth = pd.read_csv("data/test_labels.csv")

# -----------------------------
# 3. Validation
# -----------------------------
if "label" not in submission.columns:
    raise ValueError("Submission must contain a 'label' column")

if len(submission) != len(truth):
    raise ValueError("Submission length does not match test labels")

# -----------------------------
# 4. Compute score
# -----------------------------
# score = f1_score(
#     truth["label"],
#     submission["label"],
#     average="macro"
# )

report = classification_report(
    truth["label"],
    submission["label"],
    output_dict=True,
    zero_division=0
)
score = min(
    cls["f1-score"]
    for cls in report.values()
    if isinstance(cls, dict) and "f1-score" in cls
)

# -----------------------------
# 5. Output
# -----------------------------
print("--- Submission Evaluation ---")
print(f"Macro F1 Score: {score:.4f}")

with open("score.txt", "w") as f:
    f.write(str(score))
