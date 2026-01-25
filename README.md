# Cora Citation Network - Node Classification

This project implements a baseline classification model for the **Cora Dataset**. The approach uses a Random Forest Classifier to predict the category of scientific papers based on their word content.

![alt text](image.png)
## 📊 Dataset Statistics
The dataset was processed using the `Planetoid` library with the following graph properties:

* **Undirected:** True
* **Self-loops:** False
* **Isolated Nodes:** False
* **Total Training Nodes:** 640 
* **Training Label Rate:** 0.236
* **Total Testing Nodes:** 1,000
* **Testing Label Rate:** 0.369

## 🏷️ Category Mapping
The dataset classifies papers into 7 distinct scientific fields:

| Index | Category Name       |
| :--- | :---               |
| 0    | Theory             |
| 1    | Reinforcement Learning |
| 2    | Genetic Algorithms |
| 3    | Neural Networks    |
| 4    | Probabilistic Methods |
| 5    | Case Based         |
| 6    | Rule Learning      |

----

## Class Distribution 
![alt text](image-1.png)
![alt text](image-2.png)

## Dataset Distribution

| Index | Category Name       | Training Set |            | Testing Set |            |
| :--- | :---               | :---: | :---: | :---: | :---: |
|       |                    | **Count** | **%** | **Count** | **%** |
| 0    | Theory             | 81    | 12.66% | 130   | 13.0% |
| 1    | Reinforcement Learning | 56  | 8.75%  | 91    | 9.1%  |
| 2    | Genetic Algorithms | 98    | 15.31% | 144   | 14.4% |
| 3    | Neural Networks    | 178   | 27.81% | 319   | 31.9% |
| 4    | Probabilistic Methods | 101 | 15.78% | 149   | 14.9% |
| 5    | Case Based         | 77    | 12.03% | 103   | 10.3% |
| 6    | Rule Learning      | 49    | 7.66%  | 64    | 6.4%  |
| **Total** | | **640** | **100%** | **1000** | **100%** |

## 📋 User Submission Rules
## 🚀 Quick Start Guide

    Fork this Repository

- Click the "Fork" button at the top right of this page

- You'll be redirected to https://github.com/YOUR_USERNAME/gnn-challenge

    Clone Your Fork
- bash

- git clone https://github.com/YOUR_USERNAME/gnn-challenge.git
- cd gnn-challenge

    Install Dependencies
- bash

- pip install -r starter_code/requirements.txt

    Train Your Model & Generate Submission

- Modify starter_code/baseline.py or create your own model

- CRITICAL: Your output file MUST be named: github_<YOUR_USERNAME>.csv
        

## 📁 Submission File Requirements

Your CSV file MUST follow this exact format:
File Name:

- submissions/github_<your_github_username>.csv

Examples:

- submissions/github_emre123.csv

File Format:
- csv

| prediction | 
|----|
| 3  | 
| 3  | 
| 2  | 
| ... |

Requirements:

- Single column named prediction (exact spelling)

- No index column (no row numbers)

- Same number of rows as the test set

- Predictions must be integers (0, 1, 2, etc.)

- No header row except the column name

- CSV format (not Excel, not TSV)

🔄 Commit & Push Process
bash

# Add ONLY your submission file
git add submissions/github_<YOUR_USERNAME>.csv

# Commit with clear message
git commit -m "Submission by <YOUR_USERNAME>"

# Push to your fork
git push origin main

📤 Create Pull Request


⏳ What Happens Next?
Automatically (2-3 minutes):

- ✅ Scoring runs automatically on your PR

- ✅ Score appears as a comment on your PR

- ✅ Minimum per-class F1 score is calculated

- ✅ Validation checks ensure correct format

After PR is merged:

- ✅ Leaderboard updates automatically

- ✅ Your ranking appears in leaderboard.md

- ✅ Score is preserved even if you submit again later

⚠️ Common Errors & Solutions
Error	Cause	Solution
"No CSV files found"	File not in submissions/ folder	Move file to correct location
"Submission must have 'prediction' column"	Wrong column name	Rename column to prediction
"Wrong number of rows"	Different row count	Check your test set size
"File not found"	Wrong filename	Use github_<username>.csv format
Score = 0.0	Format/validation error	Check all requirements above
🎯 Scoring Details

Your submission is evaluated using:

- Metric: Minimum per-class F1 score

- Goal: Maximize the worst-performing class F1 score

- Range: 0.0 (worst) to 1.0 (perfect)

- Fairness: Ensures no class is neglected

Example scores:

- Perfect predictions: 1.0000

- Good balanced predictions: 0.8500+

- Poor on one class: 0.0000 (if any class has zero F1)

## 📊 Leaderboard Rules

    Highest score wins (Minimum per-class F1)

    Tie-breaking: First submission timestamp

    Multiple submissions allowed: Only your highest score is kept

    Updates automatically: After PR merge

    View leaderboard: Check leaderboard.md in main repo


## 📁 Data Structure

The processed dataset is provided in CSV format and organized as follows:

- **`data/train.csv`**  
  Contains features and labels for **640 training nodes**. The last column has labels.

- **`data/test.csv`**  
  Contains features for **1,000 test nodes**.  
  ⚠️ Labels are intentionally removed for blind evaluation.

- **`submissions/github_<username>.csv`**  
  The final prediction file generated by your model.

### 📄 Submission Format

Your submission file must follow the exact format below:

**Example Submission Format (`submissions/github_username.csv`):**



## 📏 Evaluation Metrics

Submissions are evaluated on `Minimum per-class F1-score`.

- The evaluation metric measures the performance of the worst-performing class in the model.


## Baseline Approach

We provide a simple baseline using Multi-output Random Forest:

# Train baseline
python starter_code/baseline.py


Baseline Performance (validation set):

    Macro F1: ~0.6

Your goal: Beat the baseline! 🎯

## 🛠️ Requirements
To run this project, you need the following Python libraries:

- pandas
- numpy
- scikit-learn
- torch
- torch-geometric
- matplotlib
- networkx

## 📤 Submission Rules
- Submit exactly **one CSV file**
- File must be named: `<github_username>.csv`
- CSV must contain a column named `label`
- Number of rows must match the test set (1000 rows)

## References
- Data: [Planetoid-Cora](https://pytorch-geometric.readthedocs.io/en/2.5.0/generated/torch_geometric.datasets.Planetoid.html)

😈Your worst class performance defines your score.

## 🤓 Have a nice works!