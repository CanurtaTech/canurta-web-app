from email.policy import default
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

import json
import requests

st.set_page_config(
    page_title="App",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="auto"
)
with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Data
#df= pd.read_csv('https://raw.githubusercontent.com/goga0001/canurta/main/Untitled%20spreadsheet%20-%20Sheet1.csv')

#load assets=add empty space
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")



with st.sidebar:
    image1 = st.image("images/canurta_logo.png")
    a1, a2 = st.columns(2)
    a1.image("images/profile_1.png", width=60)
    a2.text("Jim, 24")
    
    choose = option_menu("", ["Home", "Data", "Profile"],
                            
                         styles={
        "container": {"default_index":"0","padding": "5!important","position":"relative","top":"50%","height":"200px","width": "320","min-width":"320px", "background-color": "#023334","border-radius":"0px", "width": "320px","margin": "auto"},
        "icon": {"visibility":"hidden"},
        "nav-link active": {"padding":"15px 40px;", "min-height":"50px", "min-width": "150px","font-size": "16px","border-radius":"0px","border":"5px","border-color":"#054747", "text-align": "left", "margin":"-20px", "--hover-color": "#eee", "color":"white","font-family":"wf_282b04cad22942a295c9c48f5 - 400"},
        "nav-link": {"padding":"18px 40px;", "min-height":"50px", "min-width": "150px","font-size": "16px","border-radius":"0px","border":"5px","border-color":"#054747", "text-align": "left", "margin":"-0px", "--hover-color": "#eee", "color":"white","font-family":"wf_282b04cad22942a295c9c48f5 - 400"},
        "nav-link-selected": {"background-color": "#02292A","color":"ffffff"},
    }
    )
    mood = st.sidebar.slider('Daily Pain Tracker', 0, 10, 7)
    pain = st.sidebar.slider('Daliy Mood Tracker', 0, 10, 2)


if choose == "Home":
 
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:45px ;font-style:bold; font-family: font-family: "Source Sans Pro", sans-serif;
    font-weight: 600; color: black; float:left;margin: auto -90px;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Home</p>', unsafe_allow_html=True)    
      
    with col2:               # To display brand log
        st.write("")
    space(1)
    space(1)
    space(1)
    space(1)
    space(1)
  
    
    a1, a2, a3, a4= st.columns(4)
    a1.metric("Dose Recomendation: ", "\n2 pills")
    a2.metric("Avg Inflammation\nScore","9 mpg", "-8%")
    a3.metric("Avg Pain\nScore", "32 mpg", "+2%")
    a4.metric("Avg mood score", "11 mpg", "-7%")
    space(1)
    space(1)
    space(1)
    space(1)
    space(1)
    st.image("images/graph.png")
    st.subheader("Product Recomendations")
    space(1)
    space(1)

    b1, b2= st.columns(2)
    with b1:
       st.image("images/canurta1.png")
       button=st.button("Get your product here")
       
      
    with b2:
       st.image("images/product.png", use_column_width=True)
       
elif choose == "Profile":
#Add a file uploader to allow users to upload their project plan file
    st.markdown(""" <style> .font {
    font-size:45px ; font-family: 'wf_282b04cad22942a295c9c48f5 - 400'; color: black; float:left;margin: auto -90px;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">My Profile</p>', unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Personal Info", "Share Results", "Subsctiption"],
        icons=["book","share","file-earmark-medical"],
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "20px"}, 
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )

    if selected == "Personal Info":
        st.subheader("Personal Info")
        def form():
            with st.form(key="Information Form"):
                name = st.text_input("Full Name: ")
                age = st.text_input("Age: ")
                height = st.text_input("Height: ")
                weight = st.text_input("Weight: ")
                submission = st.form_submit_button(label="Submit")
                if submission == True:
                    st.success("Successfully submitted!") 
        form()
        space(1)
        space(1)
        space(1)
        col1, col2, col3 = st.columns(3) #putting an image in centre
        col2.image("images/profile_page_pic2.png") 
    

    if selected == "Share Results": 
        st.subheader("My Physician")
        
        def physician_form():
            with st.form(key="Physician Form"):
                doctor_name = st.text_input("Doctor's Name: ")
                doctor_email = st.text_input("Email: ")
                submission = st.form_submit_button(label="Invite")
                if submission == True:
                   st.success("Successfully submitted!") 
        physician_form()
        st.markdown(
            """<a style='display: block; text-align: center;' href="https://fullscript.com/">Connect to Fullscript</a>
            """, 
            unsafe_allow_html=True
            )
        space(1)
        space(1)
        space(1)
        col1, col2, col3 = st.columns((15,10,5)) #putting an image in centre
        col2.image("images/profile_page_pic3.png")
    if selected == "Subsctiption":
        col1, col2, col3 = st.columns(3) #putting an image in centre
        with col1:
         st.markdown(
            """<a style='display: block; padding: 30px 20px; position:relative;
    border-radius: 0px;
    border: solid;
    border-width: thick;
    color: #023334;
    text-align: center;
    left: 200px;' href="https://www.canurta.com/">Subscription Details</a>
            """, 
            unsafe_allow_html=True
            )
        with col2:
            st.write("")
        with col3:
         st.write("")

elif choose == "Data":
    st.markdown(""" <style> .font {
    font-size:45px ; font-family: 'wf_282b04cad22942a295c9c48f5 - 400'; color: black; float:left;margin: auto -90px;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Data</p>', unsafe_allow_html=True)
    def import_json(json_file):
        df = pd.read_json(json_file)
        df =df.T
        df.iloc[:, 1:8] = df.iloc[:, 1:8].astype('float')
        df.iloc[:, 8:10] = df.iloc[:, 8:10].astype('int')
        df['skin_temp'] = df['skin_temp'].astype('float')
        df.iloc[:, 12:15] = df.iloc[:, 12:15].astype('int')
        df['date'] = df['date'].astype('datetime64')

        return df
    df = import_json('canurta_dashboard.json')
    df_biomarkers = df[df['user_id'] == 227722].iloc[:,0:8]
    marker_list = df_biomarkers.columns[1:8].tolist()
    choice = marker_list
    groupby_column2 = st.multiselect(
        'What would you like to analyse?',
        ('trail', 'crp', 'il6', "tgfb",	"tgfa",	"il8","ip10")
    )
    data=df_biomarkers[choice]
    st.text("")
     

    fig2 = px.line(
        data,
        x=df_biomarkers['date'],
        y=groupby_column2)
    fig2.update_xaxes(title_text='Date')

    st.plotly_chart(fig2,use_container_width=True)
    #####SECOND GRAPH#######         FINISHED
    lang = pd.read_excel('Book1.xlsx')
    st.text("A close look into the data")
    list= lang.columns[8:15].tolist()
    choice1= list
    data1=lang[choice1]
    groupby_column = st.selectbox(
        'What would you like to analyse?',
        ("rhr","calories","skin_temp", "sleep")
    )

    fig1 = px.bar(
        data1,
        x=lang['date'],
        y=groupby_column,
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        title=f'<b>Physiological Analysis by {groupby_column}</b>'
        )
    fig1.update_xaxes(title_text='Date')
    st.plotly_chart(fig1,use_container_width=True)


