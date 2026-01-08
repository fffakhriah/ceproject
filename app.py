import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from aco import AntColonyOptimization

st.set_page_config(page_title="Cinema Ticket Pricing Optimization", layout="centered")

st.title("🎬 Cinema Ticket Price Optimization using ACO")

# Load dataset
data = pd.read_csv("cinema_ticket_pricing_clean.csv")
st.subheader("Dataset Preview")
st.dataframe(data)

# Parameters
st.sidebar.header("ACO Parameters")
num_ants = st.sidebar.slider("Number of Ants", 5, 50, 20)
num_iterations = st.sidebar.slider("Number of Iterations", 10, 200, 50)
evaporation_rate = st.sidebar.slider("Evaporation Rate", 0.1, 0.9, 0.5)

if st.button("Run Optimization"):
    aco = AntColonyOptimization(
        data,
        num_ants=num_ants,
        num_iterations=num_iterations,
        evaporation_rate=evaporation_rate
    )

    best_price, best_revenue, convergence = aco.run()

    st.success(f"Optimal Ticket Price: RM {best_price}")
    st.success(f"Maximum Revenue: RM {best_revenue}")

    # Plot convergence
    st.subheader("ACO Convergence Curve")
    fig = plt.figure()
    plt.plot(convergence)
    plt.xlabel("Iteration")
    plt.ylabel("Best Revenue")
    plt.title("ACO Convergence Curve")
    st.pyplot(fig)
