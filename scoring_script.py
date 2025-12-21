import pandas as pd
from sklearn.metrics import f1_score

# 1. Path to your recently saved submission
submission_file = '../submissions/submission.csv'

# 2. Load your submission and the ground truth
submission = pd.read_csv(submission_file)
truth = pd.read_csv('../data/test_labels.csv')

print(f"Test labels shape: {truth.shape}")
# 4. Compute F1 score
# We compare the 'target' column from both dataframes
score = f1_score(truth['label'], submission['label'], average='macro')

print(f'--- Submission Evaluation ---')
print(f"Test Accuracy: {score:.4f}")
print(f"Test F1 Score (Macro): {score:.4f}")