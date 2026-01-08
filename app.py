import streamlit as st
import matplotlib.pyplot as plt
from aco import ACO

st.title("🎬 Cinema Ticket Pricing Optimization (ACO)")

st.sidebar.header("ACO Parameters")
ants = st.sidebar.slider("Number of Ants", 10, 50, 20)
iterations = st.sidebar.slider("Iterations", 20, 100, 50)
evap = st.sidebar.slider("Evaporation Rate", 0.1, 0.9, 0.5)

aco = ACO(n_ants=ants, n_iterations=iterations, evaporation=evap)

if st.button("Run Optimization"):
    price, revenue, history = aco.run()

    st.success(f"Optimal Ticket Price: RM{price}")
    st.info(f"Maximum Revenue: RM{revenue:.2f}")

    fig, ax = plt.subplots()
    ax.plot(history)
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Revenue")
    ax.set_title("Convergence Curve")

    st.pyplot(fig)

