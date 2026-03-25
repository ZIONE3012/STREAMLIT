


# Streamlit practice
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#For creating the title
st.title("Zion is learning Streamlit")
st.header("Header")
st.subheader("Subheader")

#to text in streamlit program..this is for simple plain text
st.text("This is Zion's practice world.")

#to write in streamlit program, this is for complex words too
st.write("This is **just** a **_theme_** ")

#In adding a csv file, importing pandas package firstly
df = pd.read_csv("supermarket_sales.csv")
st.dataframe(df) #This is to display the csv file
fig , ax = plt.subplots()
ax.scatter(np.arange(5), np.arange(5) ** 2)


#writing code in streamlit
code = '''def func():
      print (np.arange(10))'''
st.code(code, language = "python")

