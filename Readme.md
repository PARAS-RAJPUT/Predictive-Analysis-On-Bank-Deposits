# Predictive Analysis of Population Group-wise Bank Deposits
## Project Overview

This project implements regression models to predict deposit amounts based on banking infrastructure and account data for different population groups. It allows comparison between multiple regression models to identify the best-performing model.

## Key Features:

Predict deposit amounts using no_of_offices and no_of_accounts.

Compare multiple regression models: Linear Regression, Decision Tree, Random Forest, SVR, KNN.

Modular code to run models individually to avoid heavy computation.

Includes correlation heatmaps, scatter plots, and R² comparison charts.

Hyperparameter tuning using GridSearchCV.

Scalable SVR implementation with StandardScaler.

## Dataset

### File: populationgroup-wise-deposits.csv

### Columns:

no_of_offices – Number of bank offices in the population group.

no_of_accounts – Number of accounts in the population group.

deposit_amount – Total deposits in the population group.

### Requirements

Python 3.x

### Packages: pandas, numpy, matplotlib, seaborn, scikit-learn

## Install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn
regression-deposits-project/
├── 📄 populationgroup-wise-deposits.csv   # Dataset containing banking data
├── 🐍 regression_project.py               # Main Python script with model code
├── 📁 regression_graphs/                  # Folder to save generated plots and charts
│   ├── correlation_heatmap_seaborn.png
│   ├── Linear_Regression.png
│   ├── Random_Forest.png
│   ├── SVR.png
│   └── final_comparison_r2.png
├── 📄 final_model_comparison.csv          # CSV file storing metrics (R², MAE, MSE) for all models
└── 📄 README.md                           # Project documentation



## Methodology

Data Loading and Preprocessing

Load dataset using pandas.

Handle missing values and select numeric features.

Split dataset into training (80%) and testing (20%) sets.

## Exploratory Data Analysis (EDA)

Generate correlation heatmap using seaborn.

Identify strongest predictors for deposit amounts.

## Model Selection

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Support Vector Regressor (SVR)

K-Nearest Neighbors (KNN) Regressor

## Model Training

Each model trained individually.

Hyperparameter tuning with GridSearchCV.

SVR scaled with StandardScaler for faster and accurate predictions.

## Evaluation Metrics

R² Score

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Cross-Validation R²

## Visualization

Correlation heatmap.

Actual vs Predicted scatter plots for each model.

Bar chart comparing R² scores across models.

## How to Run

### Clone the repository:

git clone <https://github.com/PARAS-RAJPUT/Predictive-Analysis-On-Bank-Deposits>


### Navigate to the project folder:

cd < Predictive-Analysis-On-Bank-Deposits>


### Run the main Python script:

python regression_project.py


Generated plots and results will be saved in the regression_graphs folder.

## Model Outputs

![linear](https://github.com/user-attachments/assets/d8581d67-1dd8-4130-aff2-6938b642d2f3)


![Random ](https://github.com/user-attachments/assets/29ede652-5171-42ff-8aee-1805159cc622)


![decision](https://github.com/user-attachments/assets/c1bbfdbb-92f2-4a33-8921-2071cb163ceb)


![regressor](https://github.com/user-attachments/assets/d2ec5974-a928-42d9-9bf3-c8021c8c1578)


![model beat](https://github.com/user-attachments/assets/03666949-88a7-4f6c-b254-e1c40504bd08)







## Conclusion

Random Forest Regressor performed best in predicting deposit amounts.

Modular design allows running models separately for efficiency.

Visualizations provide insights into feature importance and model performance.

### Contact : parasrajput987045@gmail.com
