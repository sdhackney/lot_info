import streamlit as st 
import pandas as pd
import plotly.express as px 

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Vehicle Data Analysis')
st.dataframe(df)

#histogram of the price distribution

st.subheader("Price Distribution")
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

#scatterplot of the price vs odometer reading

st.subheader("Price vs Odometer Reading")
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer Reading')
st.plotly_chart(fig_scatter)

#barchart of the average vehicle price by paint color

filtered_data = df.dropna(subset=['price', 'paint_color'])
color_price_group = filtered_data.groupby('paint_color')['price'].mean().reset_index()
fig = px.bar(color_price_group, x='paint_color', y='price', title='Average Vehicle Price by Paint Color')
st.plotly_chart(fig)


#A checkbox of displaying unique paint colors

unique_colors = df['paint_color'].dropna().unique()
selected_colors = st.multiselect('Select Paint Colors', unique_colors)

if selected_colors:
    filtered_data = df[df['paint_color'].isin(selected_colors)]
    bar_fig = px.bar(filtered_data, x='paint_color', y='price', title='Average Vehicle Price by Selected Paint Colors')
    st.plotly_chart(bar_fig)
else:
    st.write("Please select at least one color to display the prices.")


