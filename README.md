📺 Content Monetization Modeler

Content Monetization Modeler is an end-to-end Machine Learning web application that predicts **YouTube ad revenue** based on video performance and contextual features. The project demonstrates the complete ML workflow from data analysis to cloud deployment using Streamlit.

---

## 🚀 Project Overview

As content creators and media companies rely heavily on ad revenue, accurately estimating monetization potential is essential. This project uses regression models to predict ad revenue for YouTube videos based on engagement, reach, and contextual information.

The final model is deployed as an **interactive Streamlit web application**, allowing users to input video metrics and instantly receive revenue predictions.

---

## 🧠 Machine Learning Workflow

- Exploratory Data Analysis (EDA)
- Data Cleaning and Preprocessing
- Feature Engineering (Engagement Rate, Temporal Features)
- Categorical Encoding
- Model Training and Evaluation
- Model Selection (Ridge Regression)
- Model Serialization
- Streamlit App Deployment

---

## 🏆 Model Details

- Algorithms tested:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Random Forest Regressor
  - Gradient Boosting Regressor

- **Final Model:** Ridge Regression  
- **Evaluation Metrics:** R² Score, RMSE, MAE

---

## 🎨 Streamlit Web Application

The Streamlit app allows users to:
- Enter video performance details
- Select category, device, and country
- Instantly predict estimated ad revenue
- View results in a clean and colorful UI

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Git & GitHub
- Streamlit Cloud

---

## 📁 Project Structure

content-monetization-modeler/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
├── README.md
│
├── notebooks/
│ └── EDA_and_Modeling.ipynb
│
└── data/
└── youtube_ad_revenue_dataset.csv

yaml
Copy code

---

## ▶️ How to Run the App Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/content-monetization-modeler.git
   cd content-monetization-modeler
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run Streamlit app:

bash
Copy code
streamlit run app.py
🌍 Deployment
The application is deployed using Streamlit Cloud, providing a publicly accessible web interface for real-time predictions.

🎯 Use Cases
Content creators estimating monetization potential

Media companies forecasting ad revenue

Educational demonstration of ML deployment