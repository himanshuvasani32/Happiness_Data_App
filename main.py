import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search of Happiness")
x_axis = st.selectbox("Select the data for X-axis",
                      ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for Y-axis",
                      ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

match x_axis:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

match y_axis:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{x_axis} and {y_axis}")

plot = px.scatter(x=x_array, y=y_array,
                  labels={"x": x_axis, "y": y_axis})

st.plotly_chart(plot)