import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score



df_train_loaded = pd.read_csv('../data/train.csv') # Planetoid open dataset was used.
X = df_train_loaded.drop(columns=['label']).values
y = df_train_loaded['label'].values

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"After splitting train.csv (80/20):")
print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"X_val shape: {X_val.shape}, y_val shape: {y_val.shape}")


# Train a baseline model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_val)
score = f1_score(y_val, y_pred, average='macro')
print(f"--- Validation Set Results ---")
print(f"Validation Accuracy: {score:.4f}")
print(f'Validation F1 Score: {score:.4f}')


# --- FIXED TEST EVALUATION ---

# 1. Load the test set
test = pd.read_csv('../data/test.csv')

# 2. Extract features exactly like you did for training
# Do NOT drop the first column by index; drop the 'label' column
test_features = test.drop(columns=[0], errors='ignore').values

# 4. Predict
test_preds = clf.predict(test_features)
print(f"Test features shape: {test_features.shape}")
# 5. Save using a generic ID (since Cora nodes don't have natural IDs in the CSV)
pd.DataFrame({
    'id': range(len(test_preds)), 
    'label': test_preds
}).to_csv('../submissions/github_beyza17.csv', index=False)

print("Submission saved successfully!")
