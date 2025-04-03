import streamlit as st

st.title("Cloud-Edge-Fog Load Balancing")
st.write("This is a simple visualization of energy consumption.")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/energy_consumption.csv")  

st.bar_chart(df.set_index("Node"))
