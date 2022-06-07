
import streamlit
import pandas

streamlit.header('My Mom\'s New Healthy Diner')
streamlit.text('BREAKFAST MENU')
streamlit.text('🥣 OMEGA3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinace & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Range Eggs')
streamlit.text('🥑🍞 Avocado Toast')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

