
import streamlit as st
import pandas as pd
import joblib
from ozlotpro_predictor import generate_predictions
from utils import visualize_frequency
from config import DEBUG_MODE, MODEL_THRESHOLD

st.set_page_config(page_title="OzLotPro", layout="wide")
st.title("OzLotPro - Advanced Oz Lotto Predictor")

try:
    model = joblib.load("ozlotpro_model.pkl")
except Exception as e:
    st.error(f"⚠️ Failed to load model: {e}")
    model = None

uploaded = st.file_uploader("Upload latest winning numbers CSV", type=["csv"])
if uploaded:
    new_draws = pd.read_csv(uploaded)
    st.write("Latest Draw Uploaded:")
    st.dataframe(new_draws)

if st.button("Generate Predictions"):
    predictions = generate_predictions(n_sets=200)
    st.write("Generated Predictions:")
    st.dataframe(predictions)
    visualize_frequency(predictions)
    if DEBUG_MODE:
        st.info("Debug Mode is ON")
