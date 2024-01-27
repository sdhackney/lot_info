import streamlit as st 
import pandas as pd
import plotly.express as px 

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Vehicle Data Analysis')
st.dataframe(df)

if st.checkbox('Show Price Distribution Histogram'):
    
    fig_hist = px.histogram(df, x='price', title='Price Distribution')
    st.plotly_chart(fig_hist)

st.subheader("Price vs Odometer Reading")
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer Reading')
st.plotly_chart(fig_scatter)


filtered_data = df.dropna(subset=['price', 'paint_color'])

color_price_group = filtered_data.groupby('paint_color')['price'].mean().reset_index()

fig = px.bar(color_price_group, x='paint_color', y='price', title='Average Vehicle Price by Paint Color')
st.plotly_chart(fig)


