import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Content Monetization Modeler",
    page_icon="📺",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    h1, h2, h3 {
        color: #38bdf8;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(90deg, #22c55e, #16a34a);
        color: white;
        font-size: 18px;
        padding: 0.6em 1.4em;
        border-radius: 12px;
        border: none;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #16a34a, #15803d);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL FILES ----------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("ℹ️ About This App")
    st.write(
        "This application predicts **YouTube Ad Revenue** using a "
        "**Ridge Regression ML model** trained on video performance data."
    )
    st.markdown("### 📊 Key Factors")
    st.markdown("""
    - Views  
    - Watch Time  
    - Engagement  
    - Subscribers  
    - Category  
    - Device  
    - Country  
    """)
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit & Scikit-learn")

# ---------------- TITLE ----------------
st.markdown("## 📺 Content Monetization Modeler")
st.markdown(
    "<p style='text-align:center;color:#cbd5f5;'>"
    "Predict YouTube Ad Revenue using AI & Machine Learning"
    "</p>",
    unsafe_allow_html=True
)
st.divider()

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    views = st.number_input("👀 Views", min_value=0, step=1000)
    likes = st.number_input("👍 Likes", min_value=0, step=100)
    comments = st.number_input("💬 Comments", min_value=0, step=10)
    watch_time = st.number_input("⏱ Watch Time (minutes)", min_value=0.0)

with col2:
    video_length = st.number_input("🎬 Video Length (minutes)", min_value=0.0)
    subscribers = st.number_input("📈 Subscribers", min_value=0, step=1000)
    category = st.selectbox("📂 Category", ["Education", "Entertainment", "Gaming", "Technology"])
    device = st.selectbox("📱 Device", ["Mobile", "Desktop"])
    country = st.selectbox("🌍 Country", ["India", "USA", "UK"])

# ---------------- FEATURE ENGINEERING ----------------
engagement_rate = (likes + comments) / views if views > 0 else 0

# Create full feature dictionary
input_dict = dict.fromkeys(features, 0)

# Numeric features
input_dict["views"] = views
input_dict["likes"] = likes
input_dict["comments"] = comments
input_dict["watch_time_minutes"] = watch_time
input_dict["video_length_minutes"] = video_length
input_dict["subscribers"] = subscribers
input_dict["engagement_rate"] = engagement_rate
input_dict["day"] = 1
input_dict["month"] = 1

# One-hot encoded features
cat_col = f"category_{category}"
dev_col = f"device_{device}"
country_col = f"country_{country}"

if cat_col in input_dict:
    input_dict[cat_col] = 1
if dev_col in input_dict:
    input_dict[dev_col] = 1
if country_col in input_dict:
    input_dict[country_col] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Scale input
input_scaled = scaler.transform(input_df)

# ---------------- PREDICTION ----------------
st.divider()

if st.button("🚀 Predict Revenue"):
    prediction = model.predict(input_scaled)

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #22c55e, #4ade80);
        padding: 22px;
        border-radius: 16px;
        text-align: center;
        font-size: 22px;
        color: black;
        margin-top: 20px;
        ">
        💰 <b>Estimated Ad Revenue</b><br>
        <span style="font-size:34px;">${prediction[0]:.2f}</span>
    </div>
    """, unsafe_allow_html=True)
