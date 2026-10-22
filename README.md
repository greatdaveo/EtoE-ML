# Student Performance Prediction

An end-to-end machine learning learning project that explores student exam data and builds a regression model to predict a student’s math score from demographic information, test preparation, and reading and writing scores.

The project includes exploratory data analysis, data ingestion, preprocessing, comparison of regression models, and saving the selected model and preprocessing pipeline.

## Project status

**Implemented:** exploratory data analysis, training data preparation, preprocessing, model comparison, and saving the selected model.

**Not implemented in this repository:** a prediction/inference pipeline or application deployment. The course also covers topics such as hyperparameter tuning and deployment, but those are not currently part of this project.

## Dataset

The project uses the Student Performance in Exams dataset. The data file is included at `notebook/data/stud.csv`.

The original dataset source is [Students Performance in Exams on Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).

The model uses students’ reading and writing scores and categorical features such as gender, race/ethnicity, parental education, lunch, and test-preparation course to predict `math_score`.

## Project workflow

1. **Explore the data** in Jupyter notebooks.
2. **Ingest the data:** save a raw copy and split the data into training and test sets.
3. **Transform the data:** impute missing values, scale numerical features, and encode categorical features.
4. **Train and compare regression models** using the training data and evaluate them using the test data.
5. **Save artifacts:** store the selected model and fitted preprocessor for later use.

The candidate models currently include Random Forest, Decision Tree, Gradient Boosting, K-Neighbors, XGBoost, CatBoost, and AdaBoost regressors.

## Setup

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

## Run the training workflow

From the repository root, run:

```bash
python -m src.components.data_ingestion
```

The workflow reads `notebook/data/stud.csv` and writes its generated files under `artifacts/`, including the data splits, preprocessor, and selected model. Run it from the repository root so the relative data and output paths resolve correctly.
