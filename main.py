import streamlit as st
import plotly.express as px
import backend as bd

# create title, input box,slider,selectbox
st.title('Weather Forecast For The Next Days')
place = st.text_input('place:')
days = st.slider('Forescast Days:',
                 min_value=1, max_value=5,
                 help='Select the number of forecasted days.')
option = st.selectbox('Select the data to view:', ('temperature', 'sky'))
if days == 1:
    st.subheader(f"{option} for the next day in {place}:")
else:
    st.subheader(f"{option} for the next {days} days in {place}:")
# get temperature/sky data
if place:
    try:
        filtered_data = bd.get_data(place, days)
        if option == 'temperature':
            # filtered data
            temperature = [dict['main']['temp'] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            fig = px.line(x=dates, y=temperature, labels={'x': 'dates', 'y': 'temperature (C)'})
            st.plotly_chart(fig)
        if option == 'sky':
            # filtered data
            # empt = st.empty()
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png'
                , 'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths,width=120)
    #         with empt:
    #             for i in image_paths:
    #                 dates = [dict['dt_txt'] for dict in filtered_data]
    #                 st.write(dates)
    #                 st.image(image_paths, width=115)
    except KeyError:
        st.info('Please enter a place that exists.')
