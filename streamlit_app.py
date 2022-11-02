import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.text('Today\'s Menu')
streamlit.text('Bacon & Eggs')
streamlit.text('Biscuits & Gravy')
streamlit.text('Omelette')
streamlit.title(':strawberry: Build Your Own Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
