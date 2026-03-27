#Importing required libraries
import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#dataframe of random numbers
df = pd.DataFrame(np.random.randn(10, 2), columns = ["prices" , "diff"])

#printing the table
#st.write(df)
#st.dataframe(df)

#plotting a linechart
#st.line_chart(df)

#printing only a column, pass a variable to it 
#st.line_chart(df, y = ["prices"])

#plotting an areachart
#st.area_chart(df)

#plotting a barchart
#st.bar_chart(df)

#Matplotlib_in_streamlit(scatterplot)
#fig, ax = plt.subplots()
#ax.scatter(np.arange(10), np.arange(10) ** 2)
#ax.hist(np.random.randn(150), bins=10)
#st.pyplot(fig)                                   #to display on the streamlit

#checking out an area through the map, firstly creating a dataframe to present it
#map for Victoria Island, Lagos
places = pd.DataFrame({
        "lat" : [6.4281 , 6.4273, 6.4285] ,
        "lon" : [3.4219 , 3.4303, 3.4210]
     })
st.title("Victoria Island Map")
st.map(places)



