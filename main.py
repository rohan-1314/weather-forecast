import streamlit as st
import plotly.express as px

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
# fig = px.line(x=dates, y=temp, labels={'x': 'dates', 'y': 'temperature (c)'})
# st.plotly_chart()
