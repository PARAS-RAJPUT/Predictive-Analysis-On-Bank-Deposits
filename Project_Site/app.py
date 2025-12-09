import json
import os
from datetime import datetime
from random import random

from flask import Flask, jsonify, render_template, request, make_response

app = Flask(__name__)

# Sample data to populate pages and APIs
MODEL_SUMMARIES = [
    {"name": "Linear Regression", "type": "Baseline", "r2": 0.82, "rmse": 1.8, "mae": 1.2, "cv_mean": 0.80},
    {"name": "Polynomial Regression", "type": "Feature expansion", "r2": 0.84, "rmse": 1.6, "mae": 1.1, "cv_mean": 0.82},
    {"name": "Random Forest Regressor", "type": "Ensemble", "r2": 0.91, "rmse": 1.2, "mae": 0.9, "cv_mean": 0.88},
    {"name": "Gradient Boosting Regressor", "type": "Ensemble", "r2": 0.93, "rmse": 1.1, "mae": 0.8, "cv_mean": 0.89},
    {"name": "KNN Regression", "type": "Instance-based", "r2": 0.84, "rmse": 1.7, "mae": 1.3, "cv_mean": 0.81},
    {"name": "Support Vector Regressor", "type": "Kernel", "r2": 0.85, "rmse": 1.6, "mae": 1.1, "cv_mean": 0.83},
    {"name": "CNN Regression", "type": "Temporal CNN", "r2": 0.88, "rmse": 1.4, "mae": 1.0, "cv_mean": 0.85},
]

CV_RESULTS = [
    {"model": "Linear Regression", "cv_mean": 0.80},
    {"model": "Random Forest", "cv_mean": 0.88},
    {"model": "Gradient Boosting", "cv_mean": 0.89},
    {"model": "Support Vector Regressor", "cv_mean": 0.83},
    {"model": "CNN Regressor", "cv_mean": 0.85},
]

CLUSTERS = [
    {"id": 1, "name": "High Value Urban", "description": "Urban customers with high balances and digital adoption."},
    {"id": 2, "name": "Steady Retail", "description": "Stable deposits, mid-income, branch-first interactions."},
    {"id": 3, "name": "Growth Potential", "description": "Younger demographics with rising balances."},
]


def load_model():
    """Placeholder for loading serialized model; returns None if missing."""
    model_path = os.path.join("models", "model.pkl")
    if os.path.exists(model_path):
        return "loaded-model-placeholder"
    return None


@app.route("/")
def home():
    return render_template("index.html", title="Home", active="home")


@app.route("/predict_page")
def predict_page():
    return render_template("predict.html", title="Predict Deposit", active="predict")


@app.route("/results")
def results_page():
    return render_template("results.html", title="Model Results", active="results", models=MODEL_SUMMARIES, cv_results=CV_RESULTS)


@app.route("/clusters")
def clusters_page():
    return render_template("clusters.html", title="Clustering", active="clusters", clusters=CLUSTERS)


@app.route("/insights")
def insights_page():
    return render_template("insights.html", title="Data Insights", active="insights")


@app.route("/about")
def about_page():
    return render_template("about.html", title="About Project", active="about")


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json() or {}
    model = load_model()
    # This is a stub prediction using a deterministic value for demo purposes.
    base_value = (hash(json.dumps(payload, sort_keys=True)) % 5000) / 10
    noise = random() * 50
    prediction = round(base_value + noise + 500, 2)
    response = {
        "predicted_deposit": prediction,
        "confidence": 0.89,
        "model_name": "Gradient Boosting Regressor" if model else "Demo Gradient Boosting Regressor",
        "interpretation": "Deposit expected to be strong; focus retention campaigns on this cohort."
    }
    return jsonify(response)


@app.route("/get_model_results")
def get_model_results():
    return jsonify({
        "models": MODEL_SUMMARIES,
        "cross_validation": CV_RESULTS,
        "generated_at": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/get_clusters")
def get_clusters():
    return jsonify({
        "clusters": CLUSTERS,
        "elbow_plot": "/static/images/elbow.png",
        "scatter_plot": "/static/images/clusters.png"
    })


@app.route("/download/model-report")
def download_model_report():
    content = "Model, R2, RMSE, MAE, CV Mean\n"
    content += "\n".join([f"{m['name']},{m['r2']},{m['rmse']},{m['mae']},{m['cv_mean']}" for m in MODEL_SUMMARIES])
    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=model_comparison.csv"
    response.headers["Content-Type"] = "text/csv"
    return response


@app.route("/download/cluster-report")
def download_cluster_report():
    content = "Cluster,Description\n"
    content += "\n".join([f"{c['name']},{c['description']}" for c in CLUSTERS])
    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=cluster_report.csv"
    response.headers["Content-Type"] = "text/csv"
    return response


if __name__ == "__main__":
    app.run(debug=True)

