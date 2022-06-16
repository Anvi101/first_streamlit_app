
import streamlit
import pandas
import requests

streamlit.header('My Mom\'s New Healthy Diner')
streamlit.text('BREAKFAST MENU')
streamlit.text('🥣 OMEGA3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinace & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Range Eggs')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so that they can select the fruits they like

fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice\'s fruit advice')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalize)
