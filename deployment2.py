#Base Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

#UI Library
 
import streamlit as st
 
##################Dashboard##############

st.subheader(":green[DataAnalytics]")
st.divider()
st.write(":blue[Data Taken for Analysis..]")
df = pd.read_csv("validateddataset1.csv")
st.dataframe(df.head())
st.divider()
st.subheader(":red[Uni-Variate Analytics(Single Column Data Study):]")
st.divider()

cola, colb , colc = st.columns(3)
with colb:
    colname = st.selectbox("Select Column:", df.columns)

if df[colname].dtype==object:
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{colname} Stats:")
        st.divider()
        st.write(df[colname].value_counts())
    with col2:
        st.write(f"{colname} Bar Chart:")
        st.divider()
        st.bar_chart(df[colname].value_counts())
elif df[colname].dtype=='float64':
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{colname} Stats:")
        st.divider()
        st.write(df[colname].value_counts())
    with col2:
        st.write(f"{colname} Line Chart:")
        st.divider()
        st.line_chart(df[colname].value_counts())

st.subheader(":red[Bi-Variate Analytics(Two Columns Data Study):]")


cold, cole , colf = st.columns(3)
with cold:
    colname1 = st.selectbox("Select Column1:", df.columns)
with colf:
    colname2 = st.selectbox("Select Column2:",df.columns)

if df[colname1].dtype == object and df[colname2].dtype==object:
    st.subheader(":green[Pure Categorical:]")
    st.divider()
    fig = px.bar(df, x=colname1, y=colname2, title="Bar Chart")
    st.plotly_chart(fig)
elif df[colname1].dtype == 'float64' and df[colname2].dtype=='float64':
    st.subheader(":green[Pure Numerical:]")
    st.divider()
    fig = px.scatter(df, x=colname1, y=colname2, title="Scatter plot")
    st.plotly_chart(fig)
elif df[colname1].dtype == 'float64' and df[colname2].dtype==object:
    st.subheader(":green[Categorical & Numerical:]")
    st.divider()
    fig = px.box(df, x=colname1, y=colname2, title="Box Plot")
    st.plotly_chart(fig)
elif df[colname1].dtype == object and df[colname2].dtype=='float64':
    st.subheader(":green[Categorical & Numerical:]")
    st.divider()
    fig = px.box(df, x=colname1, y=colname2, title="Box plot")
    st.plotly_chart(fig)

st.subheader(":red[Multi-Variate Analytics(More than Two Columns Data Study):]")
colg, colh , coli = st.columns(3)
with colg:
    colname3 = st.selectbox("Select Columns1:", df.columns)
with colh:
    colname4 = st.selectbox("Select Columns2:",df.columns)
with coli:
    colname5 = st.selectbox("Select Columns3:", df.columns)


# Checking if selected columns are numeric for 2D scatter plot
if np.issubdtype(df[colname3].dtype, np.number) and np.issubdtype(df[colname4].dtype, np.number):
    st.write(f"2D Scatter Plot: {colname3} vs {colname4} with {colname5} as color")
    fig = px.scatter(df, x=colname3, y=colname4, color=colname5, 
                     title=f"2D Scatter Plot: {colname3} vs {colname4} colored by {colname5}")
    st.plotly_chart(fig)

# Checking for categorical-numeric combination for catplot
elif df[colname3].dtype == object and np.issubdtype(df[colname4].dtype, np.number):
    st.write(f"Categorical vs Numerical Catplot: {colname3} vs {colname4} with {colname5} as color")
    fig = px.strip(df, x=colname3, y=colname4, color=colname5, 
                   title=f"Catplot: {colname3} vs {colname4} colored by {colname5}")
    st.plotly_chart(fig)

elif df[colname4].dtype == object and np.issubdtype(df[colname3].dtype, np.number):
    st.write(f"Categorical vs Numerical Catplot: {colname4} vs {colname3} with {colname5} as color")
    fig = px.strip(df, x=colname4, y=colname3, color=colname5, 
                   title=f"Catplot: {colname4} vs {colname3} colored by {colname5}")
    st.plotly_chart(fig)
elif df[colname3].dtype == object and df[colname4].dtype == object:
    st.write(f"Bar Plot: {colname3} vs {colname4} with {colname5} as color")
    fig = px.bar(df, x=colname3, y=colname4, color=colname5, 
                 title=f"Bar Plot: {colname3} vs {colname4} colored by {colname5}", barmode='group')
    st.plotly_chart(fig)
