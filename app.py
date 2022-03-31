import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff



header = st.container()
dataset = st.container()
features = st.container()


with header:
	st.title('Welcome! :wave:')
	st.text('In this project I analyze the correlation of students final scores in relation\nto the number of minutes they studied.')


with dataset:
	st.header('Data Set')
	st.text('I retrieved this data in this url:\nhttps://digitalcommons.odu.edu/cgi/viewcontent.cgi?article=1292&context=ots_masters_projects')
	
	df = pd.read_csv('Data3.csv')
	df = df.drop(df.columns.difference(['Student Number', 'Minutes of Study', 'Final Score(%)']), axis=1).dropna()
	df
	st.subheader('Line Chart')
	st.line_chart(data=df, width=0, height=0, use_container_width=True)
	st.subheader('Bar Chart')
	st.bar_chart(data=df.head(20), width=0, height=0, use_container_width=True)

	

