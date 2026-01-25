import sys
import pandas as pd
from sklearn.metrics import f1_score, precision_recall_fscore_support
import json
from cryptography.fernet import Fernet
import os
import numpy as np

def load_true_labels():
    """Load true labels from encrypted file using GitHub secret"""
    with open("encrypted_labels.bin", "rb") as f:
        encrypted = f.read()
    
    key = os.environ.get('DECRYPTION_KEY')
    if not key:
        raise ValueError("DECRYPTION_KEY not found in environment")
    
    cipher = Fernet(key.encode())
    decrypted = cipher.decrypt(encrypted)
    labels_dict = json.loads(decrypted.decode())
    
    return pd.DataFrame(labels_dict)

def calculate_min_per_class_f1(y_true, y_pred):
    """
    Calculate minimum per-class F1 score.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
    
    Returns:
        Minimum F1 score across all classes
    """
    # Get per-class precision, recall, f1, support
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, average=None, zero_division=0
    )
    
    # Get unique classes (handle cases where some classes might be missing)
    classes = np.unique(np.concatenate([y_true, y_pred]))
    
    print(f"Classes found: {classes}")
    print(f"Per-class F1 scores: {f1}")
    
    # Return minimum F1 score
    min_f1 = np.min(f1) if len(f1) > 0 else 0.0
    print(f"Minimum per-class F1: {min_f1:.4f}")
    
    return min_f1

def main():
    if len(sys.argv) < 2:
        print("Usage: python scoring_script.py <csv_file>")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    
    try:
        # Load submission
        df = pd.read_csv(csv_path)
        
        # Load true labels from encrypted file
        true_labels = load_true_labels()
        
        # Validate submission format
        if 'prediction' not in df.columns:
            raise ValueError("Submission must have 'prediction' column")
        
        if len(df) != len(true_labels):
            raise ValueError(f"Submission has {len(df)} rows, expected {len(true_labels)}")
        
        # Get true and predicted labels
        y_true = true_labels['label'].values
        y_pred = df['prediction'].values
        
        # Validate label range
        unique_true = np.unique(y_true)
        unique_pred = np.unique(y_pred)
        print(f"Unique true labels: {unique_true}")
        print(f"Unique predicted labels: {unique_pred}")
        
        # Calculate minimum per-class F1 score
        score = calculate_min_per_class_f1(y_true, y_pred)
        
        # Also calculate macro F1 for comparison
        macro_f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)
        print(f"Macro F1 (for comparison): {macro_f1:.4f}")
        
        # Save score
        with open("score.txt", "w") as f:
            f.write(str(score))
        
        print(f"\nFinal Score (Minimum per-class F1): {score:.4f}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        with open("score.txt", "w") as f:
            f.write("0.0")
        sys.exit(1)

if __name__ == "__main__":
    main()