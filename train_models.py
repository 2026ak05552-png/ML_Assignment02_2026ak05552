import pandas as pd
import numpy as np
import joblib
import os
import warnings

warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    matthews_corrcoef,
)

os.makedirs("model", exist_ok=True)

# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------
df = pd.read_csv("data/bank-additional-full.csv", sep=";")

# Exclude duration (target leakage: only known after the call)
if "duration" in df.columns:
    df = df.drop(columns=["duration"])

# Encode target
df["y"] = df["y"].map({"yes": 1, "no": 0})

X = df.drop(columns=["y"])
y = df["y"]

# ------------------------------------------------------------
# 2. Identify column types
# ------------------------------------------------------------
numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()

print("Rows:", X.shape[0])
print("Features:", X.shape[1])
print("Numeric columns:", len(numeric_cols))
print("Categorical columns:", len(categorical_cols))
print("Target distribution:\n", y.value_counts())

# ------------------------------------------------------------
# 3. Preprocessing: OneHot for categorical, StandardScaler for numeric
# ------------------------------------------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_cols),
    ]
)

# ------------------------------------------------------------
# 4. Train/test split (stratified)
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------------------------------------
# 5. Define models inside pipelines (preprocessing bundled with each model)
# ------------------------------------------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Naive Bayes": GaussianNB(),
    "Support Vector Machine": LinearSVC(random_state=42, max_iter=2000),
}

results = []

# ------------------------------------------------------------
# 6. Train, evaluate, save pipelines
# ------------------------------------------------------------
for name, model in models.items():
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", model)])
    pipeline.fit(X_train, y_train)

    # Save complete pipeline
    filename = name.lower().replace(" ", "_") + ".joblib"
    joblib.dump(pipeline, os.path.join("model", filename))

    y_pred = pipeline.predict(X_test)

    if hasattr(pipeline, "predict_proba"):
        y_prob = pipeline.predict_proba(X_test)[:, 1]
    else:
        y_prob = pipeline.decision_function(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    try:
        auc = roc_auc_score(y_test, y_prob)
    except Exception:
        auc = float("nan")
    mcc = matthews_corrcoef(y_test, y_pred)

    results.append(
        {
            "ML Model Name": name,
            "Accuracy": round(acc, 4),
            "AUC": round(auc, 4) if not np.isnan(auc) else "N/A",
            "Precision": round(prec, 4),
            "Recall": round(rec, 4),
            "F1": round(f1, 4),
            "MCC": round(mcc, 4),
        }
    )

    print(
        f"{name:25s} | Acc={acc:.4f} AUC={auc:.4f} Prec={prec:.4f} "
        f"Rec={rec:.4f} F1={f1:.4f} MCC={mcc:.4f}"
    )

# ------------------------------------------------------------
# 7. Save comparison table
# ------------------------------------------------------------
results_df = pd.DataFrame(results)
results_df.to_csv(os.path.join("model", "metrics_comparison.csv"), index=False)

print("\n=== MODEL COMPARISON TABLE ===")
print(results_df.to_string(index=False))

winner = results_df.loc[results_df["MCC"].astype(float).idxmax(), "ML Model Name"]
print("\nOverall Winner (by MCC):", winner)

# ------------------------------------------------------------
# 8. Generate correctly aligned test_data.csv
# ------------------------------------------------------------
test_data = X_test.reset_index(drop=True).copy()
test_data["y"] = y_test.reset_index(drop=True).values
test_data.to_csv("test_data.csv", index=False)

print("\nSaved: model/ (5 pipelines + metrics_comparison.csv)")
print("Saved: test_data.csv")
