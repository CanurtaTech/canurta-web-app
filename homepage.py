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
from bokeh.models.widgets import Div
import json
import requests
import sqlite3
conn = sqlite3.connect("personal_data.db", check_same_thread=False)
cur = conn.cursor()



st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#STYLE

hide_menu= """
<style>
#MainMenu{
     visiibity:hidden;
}
<style>
"""
side_bar="""
<style>
div.st-bz.st-cd.st-ce.st-ae.st-af.st-ag.st-ah.st-ai.st-aj{
     font-family: Helvetica, Arial, sans-serif;
     list-style: none
}
<style>
"""
# Data
#df= pd.read_csv('https://raw.githubusercontent.com/goga0001/canurta/main/Untitled%20spreadsheet%20-%20Sheet1.csv')

#load assets=add empty space
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")



with st.sidebar:
    choose = option_menu("", ["Home", "Data", "Profile"],
                            
                         styles={
        "container": {"padding": "5!important", "background-color": "#023334"},
        "nav-link": {"padding":"12px 0px;", "min-height":"30px", "min-width": "150px","font-size": "20px","font-size": "16px","border-radius":"0px","border":"5px","border-color":"#054747", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color":"white","font-family":"wf_282b04cad22942a295c9c48f5 - 400"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    

if choose == "Home":
 
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'wf_282b04cad22942a295c9c48f5 - 400'; color: #FF9633; float:left;margin: auto -90px;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Home</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image("images/canurta.png", width=130 )
    
    
    a1, a2, a3, a4= st.columns(4)
    a1.metric("Dose Recomendation: ", "2 pills")
    a2.metric("Avg Inflammation \n Score","20%")
    a3.metric("Avg Pain Score", "8%")
    a4.metric("Avg mood score", "11%")
    space(1)
    st.subheader("Product Recomendations")
    space(1)
    space(1)
    b1, b2= st.columns(2)
    with b1:
       st.image("images/canurta1.png", use_column_width=True)
       button=st.button("Get your product here")
       
      
    with b2:
       st.image("images/product.png", use_column_width=True)
       
elif choose == "Profile":
#Add a file uploader to allow users to upload their project plan file
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'wf_282b04cad22942a295c9c48f5 - 400'; color: #FF9633; float:left;margin: auto -90px;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Your Profile</p>', unsafe_allow_html=True)
    personal_info = st.container()
    share_results = st.container()
    with personal_info:
        st.subheader("Personal Info")
        def form():
            with st.form(key="Information Form"):
                name = st.text_input("Full Name: ")
                age = st.text_input("Age: ")
                height = st.text_input("Height: ")
                weight = st.text_input("Weight: ")
                submission = st.form_submit_button(label="Submit")
                if submission == True:
                    addData(name,age,height,weight)
        def addData(a,b,c,d):
            cur.execute("""CREATE TABLE IF NOT EXISTS personal_form(NAME TEXT(50), AGE TEXT(50), HEIGHT TEXT(50), WEIGHT TEXT(50));""")
            cur.execute("INSERT INTO personal_form VALUES (?,?,?,?)", (a,b,c,d))
            conn.commit()
            conn.close()
            st.success("Successfully submitted!")
        form()
    with share_results: 
        st.subheader("My Physician")
        #st.button("Send Report to My Doctor")
        def physician_form():
            with st.form(key="Physician Form"):
                doctor_name = st.text_input("Doctor's Name: ")
                doctor_email = st.text_input("Email: ")
                submission = st.form_submit_button(label="Invite")
                if submission == True:
                   st.success("Successfully submitted!") 
        physician_form()
        #st.write("[Connect with my doctor >](https://mail.yahoo.com/)")
        st.write("[Connect to Fullscript >](https://fullscript.com/)")

elif choose == "Data":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'wf_282b04cad22942a295c9c48f5 - 400'; color: #FF9633; float:left;margin: auto -90px;} 
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
    st.text("A close look into the data")
     

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


