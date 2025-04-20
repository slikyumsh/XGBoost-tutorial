
# 🔍 XGBoost Workflow Example: Classification, Visualization & Optimization

This project is a **comprehensive walkthrough of using XGBoost** for binary classification.  
It covers everything from preprocessing to evaluation, visualization, and hyperparameter optimization.

While it compares different boosters (`gbtree`, `dart`, `gblinear`), the main goal is to **showcase best practices and tools around XGBoost**.

---

## 📚 What You'll Learn

- How to:
  - Load and preprocess real-world data
  - Train XGBoost models with different boosters
  - Monitor performance with early stopping
  - Visualize learning curves and feature importance
  - Track resource usage (time & memory)
  - Tune hyperparameters using **Optuna**

---

## 🧪 Dataset

The script uses the classic `breast_cancer` dataset from `sklearn.datasets`.

---

---

## 🚀 Quick Start

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Run the main notebook**

XGBoost_overview.ipynb

All visual outputs will be saved in the `plots/` directory.

---

## 📊 What's Included

### ✅ Booster Evaluation

Three XGBoost boosters are trained and compared:

- `gbtree`: Standard gradient boosting with decision trees
- `dart`: Dropout-based boosting (randomly drops trees)
- `gblinear`: Linear booster without trees

For each model, the script records:

- Accuracy
- Log loss
- Training time
- Memory consumption

### ✅ Learning Curve Visualization

- `Log Loss` and `Classification Error` vs. iteration
- Separate plots for training and validation sets

### ✅ Feature Importance

Top-N features plotted by importance (Gain or Weight depending on booster)

### ✅ Hyperparameter Tuning (Optuna)

- Optimizes `gbtree` parameters: learning rate, depth, regularization, etc.
- Uses early stopping to prevent overfitting
- Clean logging, silent mode available

---

## 📦 Dependencies

```txt
xgboost>=1.7
scikit-learn>=1.2
pandas>=1.3
matplotlib>=3.4
optuna>=3.0
memory-profiler>=0.60
```

---

## 🧠 Memory Usage Notes

Different boosters behave differently in memory:

### `gbtree`
- Builds and stores all trees
- Accumulates memory as more trees are added

### `dart`
- Randomly drops some trees during training
- Reduces peak memory by using only a subset of trees at a time

### `gblinear`
- No trees used
- Uses matrix operations; memory depends on feature dimensionality

---

## 📈 Example Output

| Booster   | Accuracy | LogLoss | Time (sec) | Memory (MB) |
|-----------|----------|---------|------------|-------------|
| gbtree    | 0.9561   | 0.1294  | 0.56       | 9.3         |
| dart      | 0.9649   | 0.1182  | 0.67       | 7.1         |
| gblinear  | 0.9298   | 0.2321  | 0.12       | 8.4         |

---

## 📌 Summary

This project is not just a benchmark — it's a **practical guide to working with XGBoost in Python**:

- Fits real models ✅  
- Visualizes training progress ✅  
- Tunes hyperparameters effectively ✅  
- Measures resource efficiency ✅  

Whether you're new to XGBoost or want to deepen your workflow, this is a solid reference example.

---

## 🧪 License

MIT – use and modify freely.
