# importing required libraries
import streamlit as st  #used for building web apps with python
import numpy as np  #fast numerical operations
import pandas as pd  #data manipulation
import  json #used for storing and sending data

st.set_page_config(layout="wide")

#dataframe, table, metric, json
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns = ["cols" +str(i) for i in range(20)])
# st.dataframe(df, width = 800, height = 1000)

#Another way to print the dataframe rather than a long version
#st.dataframe(np.random.randn(50, 20))

#creating a table in streamlit
#st.table(df)

#creating metric in streamlit
#st.metric("TCS STOCK", value ="3220.70" , delta = "19.10")

#how to handle json file
f = open(r"C:\Users\Zione\Desktop\Streamlit practice\intents.json")
dt = json.load(f)
st.json(dt, expanded = True)  #this displays the json data