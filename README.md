# Advanced Data Science Internship - Developers Hub Corporation

This repository contains my solutions for the Advanced Data Science Internship. The projects demonstrate expertise in unsupervised learning, time series forecasting, predictive classification, and interactive business intelligence.

---

## 📁 Project Structure

```text
├── Task_02_Customer_Segmentation/
│   └── task_02             # K-Means Clustering & t-SNE Analysis
├── Task_03_Energy_Forecasting/
│   └── task_03         # Time Series (ARIMA, Prophet, XGBoost)
├── Task_04_Loan Default Risk/
│   └── task_04     # CatBoost Classification Model
├── Task_05_Business_Dashboard/
│   ├── app.py                      # Streamlit Application
│   └──task_05     # EDA and Data Preprocessing
└── README.md

```

---

## 🚀 Task 02: Customer Segmentation

**Objective:** Cluster customers based on spending habits to design tailored marketing strategies.

* **Approach:** * Performed EDA and data scaling on the **Mall Customers Dataset**.
* Applied **K-Means Clustering** (Optimal clusters found via Elbow Method).
* Visualized segments using **t-SNE** for high-dimensional clarity.


* **Key Findings:** Identified 5 distinct segments, including "High-Income/High-Spenders" (Premium targets) and "Low-Income/High-Spenders" (Budget-bundle targets).

---

## 📈 Task 03: Energy Consumption Forecasting

**Objective:** Forecast short-term household energy usage using historical data.

* **Approach:** * Processed the **Household Power Consumption Dataset** to an hourly frequency.
* Evaluated **ARIMA**, **Facebook Prophet**, and **XGBoost**.


* **Results:** **XGBoost** outperformed other models with a superior **RMSE of 0.607**, effectively capturing non-linear consumption patterns.

---

## 🛡️ Task 04: Credit Risk Classification

**Objective:** Predict loan default probability to minimize financial risk.

* **Approach:** * Extensive feature engineering and handling of missing data on the **Home Credit** dataset.
* Utilized **CatBoost Classifier** for its high efficiency with categorical data.


* **Evaluation:** Optimized for **ROC-AUC Score** to ensure a high true-positive rate for identifying potential defaulters.

---

## 📊 Task 05: Interactive Business Dashboard

**Objective:** Create a real-time BI tool for the **Global Superstore** dataset.

* **Features:**
* Built with **Streamlit** for a web-based interactive experience.
* Dynamic sidebar filters for Region, Category, and Sub-Category.
* Live KPI tracking for **Total Sales**, **Profit**, and **Quantity**.
* Data visualizations identifying Top 5 Customers and Sales by Sub-Category.


* **Usage:** Navigate to the `Task_05_Business_Dashboard` folder and run `streamlit run app.py`.

---

## 🛠️ Skills & Tools

* **Languages:** Python
* **Machine Learning:** Scikit-Learn, XGBoost, CatBoost, K-Means
* **Time Series:** Statsmodels (ARIMA), Prophet
* **Web/BI:** Streamlit, Pandas
* **Visualization:** Matplotlib, Seaborn, t-SNE

---

**Submission Date:** March 11, 2026

**Intern:** WANIYA ASIM
