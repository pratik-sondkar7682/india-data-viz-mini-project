import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India ka Data vizualization')
selected_state = st.sidebar.selectbox('Select the state', list_of_states)
primary_parameter = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary_parameter = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')
st.text('Size represents primary parameter')
st.text('Color represents secondary parameter')
if plot:
    if selected_state=='Overall India':
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude",
                    color_continuous_scale=px.colors.cyclical.IceFire, size = primary_parameter, color= secondary_parameter, zoom=3,
                    map_style="carto-positron",width = 1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State']==selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude",
                    color_continuous_scale=px.colors.cyclical.IceFire, size = primary_parameter, color= secondary_parameter, zoom=3,
                    map_style="carto-positron",width = 1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)