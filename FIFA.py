import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly_express as px

st.subheader('Raw data')

x = st.slider('x')
st.write(x, 'squared is', x * x)

df = st.cache(pd.read_csv)('data.csv')

is_check = st.checkbox('Display Data')
if is_check: st.write(df)

teams = st.sidebar.multiselect('Enter clubs', df['Club'].unique())
st.write('Your input clubs', teams)

variables = st.sidebar.multiselect('Enter the variables', df.columns)
st.write('You selected these variables', variables)

selected_club_data = df[(df['Club'].isin(teams))]
two_clubs_data = selected_club_data[variables]

club_data_is_check = st.checkbox('Display the data of selected clubs')
if club_data_is_check: st.write(two_clubs_data)

selected_players = st.sidebar.multiselect('Select players to compare', two_clubs_data.Name.unique())
st.write('The players are', selected_players)

plot_data = two_clubs_data[(two_clubs_data['Name']).isin(selected_players)]
st.write(plot_data)
st.bar_chart(plot_data.Name)

n = 2
values = plot_data.values
value1 = values[0][1:]
value2 = values[1][1:]
index = np.arange(2)
width = 0.3
p1 = plt.bar(index, value1, width)
p2 = plt.bar(index+width, value2, width)
plt.xlabel('Variables')
plt.ylabel('Value')
plt.xticks(index, ('Potential', 'Age'))
plt.legend(values[:,0])
st.pyplot()
