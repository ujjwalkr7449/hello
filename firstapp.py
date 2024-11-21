import streamlit as st
from streamlit import divider
import pandas as pd
import numpy as np


st.title("my chatbot")
with st.sidebar:
    st.header(" about app")
    st.write("hello")

st.text("hello")
st.form("")
st.header("hello", divider="rainbow")
st.markdown("hello")
x=st.slider("chose x ",1,10)
st.write("the value : blue[***x***] is",x)
st.write("the value of : blue[***x***] is",x)
col1,col2 ,col3= st.columns(3)
with col1:
    x=st.slider("chose x", 1,100)
with col2 :
    st.write("the value x ",x)
"""with col3:
    st.write("helllo")"""
"""chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)"""
