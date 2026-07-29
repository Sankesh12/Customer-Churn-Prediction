# 📊 Customer Churn Prediction

An End-to-End Machine Learning Project from raw customer data to a live Streamlit web application.

**Python • Scikit-Learn • Pandas • NumPy • Matplotlib • Seaborn • Streamlit • Joblib**

---

## 🔗 Live Demo

**Coming Soon**

---

# 📌 About the Project

This project predicts whether a telecom customer is likely to **stay** or **leave** based on customer demographics, subscription details, and service usage.

It is more than just a machine learning notebook. The project demonstrates a complete ML workflow including data exploration, preprocessing, model training, evaluation, feature importance analysis, model deployment, and an interactive Streamlit application.

The goal is to understand how machine learning models can help businesses identify high-risk customers and improve customer retention strategies.

---

# ✨ Features

* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data Cleaning and Missing Value Handling
* 🔄 One-Hot Encoding for Categorical Features
* 🤖 Trained Multiple Machine Learning Models
* 📈 Model Performance Comparison
* 🌳 Feature Importance Analysis
* 🎯 Customer Churn Prediction
* 💻 Interactive Streamlit Web Application
* 💾 Model Serialization using Joblib
* 🚀 Easy Deployment Ready

---

# 🧪 Model Performance

Two machine learning models were trained and compared before selecting the final model.

| Model                     | Accuracy | Precision |   Recall | F1 Score |
| ------------------------- | -------: | --------: | -------: | -------: |
| **Logistic Regression** ✅ |  **82%** |  **0.86** | **0.90** | **0.88** |
|  Decision Tree              |      70% |      0.80 |     0.80 |     0.80 |

### ✅ Final Model

**Logistic Regression**

It achieved the highest overall accuracy and better generalization on unseen customer data.

---

# 🛠️ Tech Stack

| Layer                | Technology                         |
| -------------------- | ---------------------------------- |
| Programming Language | Python                             |
| Data Analysis        | Pandas, NumPy                      |
| Data Visualization   | Matplotlib, Seaborn                |
| Machine Learning     | Scikit-Learn                       |
| Models               | Logistic Regression, Decision Tree |
| Web Application      | Streamlit                          |
| Model Serialization  | Joblib                             |

---

# 📂 Project Structure

```text
Customer_Churn_Prediction/

│── model.pkl
│── columns.pkl
│── app.py
│── WA_Fn-UseC_-Telco-Customer-Churn.csv
│── requirements.txt
│── README.md
```

---

# ⚙️ How It Works

1. Load the Telco Customer Churn dataset.
2. Perform data cleaning and preprocessing.
3. Convert categorical variables using One-Hot Encoding.
4. Split the dataset into training and testing sets.
5. Train Logistic Regression and Decision Tree models.
6. Compare model performance using evaluation metrics.
7. Save the trained model using Joblib.
8. Load the model inside a Streamlit application.
9. User enters customer information.
10. The model predicts whether the customer is likely to **Stay** or **Leave** along with prediction probabilities.

---

# 🚀 Run Locally

Clone the repository

```bash
git clone https://github.com/Sankesh12/Customer_Churn_Prediction.git

cd Customer_Churn_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📊 Streamlit Inputs

The application predicts customer churn using the following customer information:

* Gender
* Senior Citizen
* Tenure (Months)
* Internet Service
* Online Security
* Contract Type
* Payment Method
* Monthly Charges
* Total Charges

---

# 📈 Prediction Output

The application displays

* ✅ Customer likely to Stay
* ⚠️ Customer likely to Leave

It also shows prediction probabilities for both classes.

Example

```text
Stay Probability  : 86.72%

Leave Probability : 13.28%
```

---

# 📊 Exploratory Data Analysis

The project includes

* Dataset Overview
* Statistical Summary
* Missing Value Analysis
* Duplicate Record Check
* Correlation Heatmap
* Customer Churn Distribution
* Contract vs Churn Analysis
* Monthly Charges Box Plot

---

# 🌳 Feature Importance

Feature importance analysis was performed using the Decision Tree model to identify the most influential factors affecting customer churn.

Important factors include:

* Contract Type
* Monthly Charges
* Tenure
* Total Charges
* Internet Service

---

# ⚖️ Class Imbalance

The dataset is slightly imbalanced because there are more customers who stay than customers who churn.

Although the imbalance is not severe, future improvements may include:

* SMOTE
* Class Weighting
* Advanced Ensemble Models

---

# 💼 Business Insights

The analysis provides several valuable business insights:

* Customers with Month-to-Month contracts are more likely to churn.
* Customers with higher monthly charges have a greater risk of leaving.
* Customers with longer tenure tend to remain loyal.
* Feature importance highlights the key drivers of customer churn.
* These insights can help telecom companies improve customer retention through personalized offers, loyalty programs, and proactive customer support.

---

# 🧠 What I Learned

* Performing Exploratory Data Analysis (EDA)
* Data Cleaning and Preprocessing
* Handling Missing Values
* Feature Engineering using One-Hot Encoding
* Training and Comparing Machine Learning Models
* Evaluating Classification Models
* Saving and Loading Machine Learning Models
* Building Interactive Streamlit Applications
* Deploying Machine Learning Projects

---

# 🔮 Future Improvements

* Hyperparameter Tuning
* Cross Validation
* Pipeline Implementation
* Feature Selection
* SMOTE for Class Imbalance
* Cloud Deployment
* User Authentication
* Model Monitoring

---

# ⚠️ Disclaimer

This project is developed for educational and learning purposes. The predictions are based on historical customer data and should be used as decision-support insights rather than absolute business decisions.

---

# 📬 Connect With Me

If you found this project helpful, feel free to connect with me or provide your feedback.

## 📬 Connect With Me

<p align="left">

<a href="https://www.linkedin.com/in/sankeshlal/" target="_blank">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="https://github.com/Sankesh12" target="_blank">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="mailto:sankesh.lal12@gmail.com">
<img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

</p>
