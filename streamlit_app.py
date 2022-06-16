
import streamlit
import pandas
import requests
import snowflake.connector

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

fruit_choice =streamlit.text_input('What fruit you would like information about?','Kiwi')
streamlit.write('User entered choice: ',fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalize)



add_my_fruit =streamlit.text_input('What fruit would you like to add?','Kiwi')
#fruityvice_response_add = requests.put("https://fruityvice.com/api/fruit/"+add_my_fruit)
streamlit.write('Thanks for adding: ',add_my_fruit)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlit')")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select * from fruit_load_list")
my_data_rows=my_cur.fetchall()

streamlit.header("The fruitload list contains: ")
streamlit.dataframe(my_data_rows)

