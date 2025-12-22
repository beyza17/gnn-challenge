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

---

## Class Distribution
![alt text](image-1.png)

| Label | Category Name       | Count | Percentage (%) |
| :--- | :---               | :---: | :---: |
| 0    | Theory             | 81    | 12.66% |
| 1    | Reinforcement Learning | 56  | 8.75%  |
| 2    | Genetic Algorithms | 98    | 15.31% |
| 3    | Neural Networks    | 178   | 27.81% |
| 4    | Probabilistic Methods | 101 | 15.78% |
| 5    | Case Based         | 77    | 12.03% |
| 6    | Rule Learning      | 49    | 7.66%  |

**Total Instances:** 640




## 📁 Data Structure
The processed data is exported into the following CSV files:
- **train.csv**: Features and labels for the 640 training nodes.
- **test.csv**: Features for the 1,000 test nodes (labels removed for blind testing).
- **submission.csv**: The final model output in `id, label` format.

The ground truth wasn't shared here. It will be used for evaluation.



## 🛠️ Requirements
To run this project, you need the following Python libraries:
```text
pandas
numpy
scikit-learn
torch
torch-geometric
matplotlib
networkx


