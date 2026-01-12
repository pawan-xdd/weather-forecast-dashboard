import streamlit as st
import plotly.express as px
from backend import get_data
import datetime

st.title("Weather Forecast for the next the days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days:",min_value=1, max_value=5,
                 help="Select the number of days to forecast")

option = st.selectbox("Select data to view:",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.title()}")

try:
    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]- 273.15 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates,y=temperatures,labels={"x": "Date", "y": "Temperatures (in °C)."})
            st.plotly_chart(figure)

        if option == "Sky":
            # images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
            #           "Rain": "images/rain.png", "Snow": "images/snow.png"}
            # sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # image_path = [images[sky_condition] for sky_condition in sky_conditions]

            api_data = get_data(place, days)
            dates = [date["dt_txt"] for date in api_data]
            sky_condition = [f"images/{data['weather'][0]['main']}.png" for data in api_data]
            display_dates = [i.split('-') for i in dates]
            out = []
            for i in range(len(dates)):
                out.append(datetime.datetime(int(display_dates[i][0]), int(display_dates[i][1]),
                                             int(display_dates[i][2][:2]), int(display_dates[i][2][3:5]), 0))
            final = [x.strftime("%a, %b %d %H:%M") for x in out]
            st.image(sky_condition, width=175, caption=final)

            # st.image(image_path, width=115)

except KeyError:
    st.warning("No such place!", icon="⚠️")

