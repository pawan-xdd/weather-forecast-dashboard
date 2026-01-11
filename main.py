import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next the days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days:",min_value=1, max_value=5,
                 help="Select the number of days to forecast")

option = st.selectbox("Select data to view:",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.title()}")


def get_data(days):
    _dates = ["2026-01-11","2026-01-12","2026-01-13","2026-01-14"]
    _temperatures = [10, 11, 34, 40]
    _temperatures = [days * i for i in _temperatures]
    return _dates, _temperatures

dates, temperatures = get_data(days)

figure = px.line(x=dates,y=temperatures,labels={"x": "Date", "y": "Temperatures (in °C)."})
st.plotly_chart(figure)


