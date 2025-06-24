
import matplotlib.pyplot as plt
import streamlit as st

def visualize_frequency(predictions):
    flat = predictions.values.flatten()
    counts = {n: list(flat).count(n) for n in range(1, 46)}
    sorted_counts = dict(sorted(counts.items()))
    fig, ax = plt.subplots()
    ax.bar(sorted_counts.keys(), sorted_counts.values())
    ax.set_title("Number Frequency in Predictions")
    ax.set_xlabel("Number")
    ax.set_ylabel("Count")
    st.pyplot(fig)
