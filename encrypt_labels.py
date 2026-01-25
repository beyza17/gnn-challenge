# encrypt_labels.py (run locally once)
import pandas as pd
from cryptography.fernet import Fernet
import base64
import json

# Load your test labels
true_labels = pd.read_csv(r"D:\uni\phd\GNN\project\data\test_labels.csv")

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt the labels
labels_dict = true_labels.to_dict(orient='list')
labels_json = json.dumps(labels_dict)
encrypted = cipher.encrypt(labels_json.encode())

# Save encrypted file
with open("encrypted_labels.bin", "wb") as f:
    f.write(encrypted)

# Save the key (will be added as GitHub Secret)
print("KEY (add to GitHub Secrets as DECRYPTION_KEY):")
print(key.decode())