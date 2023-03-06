import streamlit as st
# import hydralit_components as hc
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
# from streamlit_card import card
import openai
import os

openai.api_key =  os.getenv("APIKEY")
st.set_page_config(page_title="My App", page_icon=":rocket:", layout="wide",initial_sidebar_state="expanded"  )

   
with st.sidebar:
    choose = option_menu("App Gallery", ["Write For Me", "Idea Generator", "Promotion Ideas", "Account", "Log Out"],
                         icons=['cpu', 'lightbulb fill', 'bar-chart fill', 'book','person dash'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important","background": "rgba(255, 255, 255, 0.2)","border-radius": "16px","box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)","backdrop-filter": "blur(5px)","-webkit-backdrop-filter": "blur(5px)","border": "1px solid rgba(255, 255, 255, 0.3)"},
        "icon": {"font-color":"Grey", "font-size": "25px", "border-radius":"50%"}, 
        "nav-link": {"font-size": "16px","font-weight":"700", "border-radius":"10px", "font-color":"Grey", "text-align": "left", "margin":"10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
    }
    )

    with st.container():
        box=option_menu("Trial Pack", ["Click to subscribe"],
                         icons=['currency-exchange'],
                         menu_icon="activity", default_index=0,
                        styles={
        "container": {"padding": "5!important","background": "rgba(255, 255, 255, 0.2)","border-radius": "16px","box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)","backdrop-filter": "blur(5px)","-webkit-backdrop-filter": "blur(5px)","border": "1px solid rgba(255, 255, 255, 0.3)"},
        "icon": {"font-color":"Grey", "font-size": "25px", "border-radius":"50%"}, 
        "nav-link": {"font-size": "16px","font-weight":"700", "border-radius":"10px", "font-color":"Grey", "text-align": "left", "margin":"10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
    }
    )

    
# def openai(description):
#     reply = openai.Completion.create(
#                                         engine="text-davinci-003",
#                                         prompt=inpt,
#                                         max_tokens=3600,
#                                         n=1,
#                                         stop=None,
#                                         temperature=0.5,
#                                         )
#     explan= reply.choices[0].text.strip()
#     st.stop()
#     return explan

 
    
st.markdown(""" <style> 
    .form {
   
background: rgba(255, 255, 255, 0.2);
border-radius: 16px;
box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
backdrop-filter: blur(5px);
-webkit-backdrop-filter: blur(5px);
border: 1px solid rgba(255, 255, 255, 0.3);

     } 
    </style> """, unsafe_allow_html=True)

col1, col2,= st.columns(2)

if choose == "Write For Me":
    with col1:
        st.subheader('Write for me')
        des=st.text_area(label='Description',label_visibility='collapsed' )
        if st.button('Submit'):
            reply = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=des,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
            explan= reply.choices[0].text.strip()
            # st.code(explan)
    with col2:
        st.subheader('Generated OutPuts')

        try:
            explan= reply.choices[0].text.strip()
            st.code(explan)
        except:
            st.code("Input something and click submit")
        # st.code(explan)
            # st.stop()
                
elif choose == "Idea Generator":
    with col1:

        st.subheader('Idea Generator')
        src = st.text_input("source Link")
        des=st.text_area(label='Description',label_visibility='collapsed' )
        if st.button('Submit'):
            prompt = str(des) + " " + " Response should be based from this source :" + str(src)
            reply = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=des,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
            idea= reply.choices[0].text.strip()
            # st.code(explan)
    with col2:
        st.subheader('Generated OutPuts')

        try:
            idea= reply.choices[0].text.strip()
            st.code(idea)
        except:
            st.code("Input something and click submit")
        # st.code(explan)
# st.stop()


elif choose == "Promotion Ideas":
    with col1:
        st.subheader('Promotion Ideas')
        string_list = ['OnlyFans mass Message', 'Caption For Instagram Post', 'Reply for a Tweet or Message']
        selected_option = st.selectbox('Select an option', string_list, label_visibility ='collapsed')
# Define the options for the select box
        options = [' That Would arrouse and turn on the guy who is reading it and make him ask for nudes ', ' that Would grab the attention of the person who is reads it and well suits the caption ', ' a sarcastic response']
        des=st.text_area(label='Description',label_visibility='collapsed' ,placeholder='Specify under which context')
        promp = "Generate a " + selected_option + ' ' + options[string_list.index(selected_option)] + ' Under the following context' + des
        if st.button('Submit'):
            reply = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=str(promp),
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
            explan= reply.choices[0].text.strip()
            # st.code(explan)
    with col2:
        st.subheader('Generated OutPuts')

        try:
            explan= reply.choices[0].text.strip()
            st.code(explan)
        except:
            st.code("Input something and click submit")
