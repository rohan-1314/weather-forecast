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
            col1, col2, col3, col4, col5 = st.columns(5)
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png'
                , 'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            image_paths = [images[condition] for condition in sky_conditions]
            print(image_paths)
            print(enumerate(image_paths))
            # st.image(image_paths, width=120)
            with col1:
                dates = [dict['dt_txt'] for dict in filtered_data]
                for index, path in enumerate(image_paths):
                    if index in [0, 1, 2, 3]:
                        st.image(image_paths[index])
                        st.write(dates[index])
                    if index in [4, 5, 6, 7]:
                        st.image(image_paths[index])
                        st.write(dates[index])
            with col2:
                dates = [dict['dt_txt'] for dict in filtered_data]
                for index, path in enumerate(image_paths):
                    if index in [8, 9, 10, 11]:
                        st.image(image_paths[index])
                        st.write(dates[index])
                    if index in [12, 13, 14, 15]:
                        st.image(image_paths[index])
                        st.write(dates[index])
            with col3:
                dates = [dict['dt_txt'] for dict in filtered_data]
                for index, path in enumerate(image_paths):
                    if index in [16, 17, 18, 19]:
                        st.image(image_paths[index])
                        st.write(dates[index])
                    if index in [20, 21, 22, 23]:
                        st.image(image_paths[index])
                        st.write(dates[index])
            with col4:
                dates = [dict['dt_txt'] for dict in filtered_data]
                for index, path in enumerate(image_paths):
                    if index in [24, 25, 26, 27]:
                        st.image(image_paths[index])
                        st.write(dates[index])
                    if index in [28, 29, 30, 31]:
                        st.image(image_paths[index])
                        st.write(dates[index])
            with col5:
                dates = [dict['dt_txt'] for dict in filtered_data]
                for index, path in enumerate(image_paths):
                    if index in [32, 33, 34, 35]:
                        st.image(image_paths[index])
                        st.write(dates[index])
                    if index in [36, 37, 38, 39]:
                        st.image(image_paths[index])
                        st.write(dates[index])

    except KeyError:
        st.info('Please enter a place that exists.')
