import streamlit as st
from cProfile import label
from curses import keyname
from email.mime import image
from tarfile import PAX_FIELDS
from turtle import color, width
import requests
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from matplotlib import pyplot as plt
import plost
import seaborn as sns
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io 
from bokeh.models.widgets import Div
import json


st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Main Page")
with st.sidebar:
    choose = option_menu("Dashboard", ["Home", "Data", "Profile"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == "Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image("images/canurta.png", width=130 )
    
    st.write("Sharone Li is a data science practitioner, enthusiast, and blogger. She writes data science articles and tutorials about Python, data visualization, Streamlit, etc. She is also an amateur violinist who loves classical music.\n\nTo read Sharone's data science posts, please visit her Medium blog at: https://medium.com/@insightsbees")    
   
