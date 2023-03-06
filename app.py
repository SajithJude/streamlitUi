import streamlit as st
import hydralit_components as hc
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
# from streamlit_card import card
import openai
import os

openai.api_key =  os.getenv("APIKEY")
st.set_page_config(page_title="My App", page_icon=":rocket:", layout="wide",initial_sidebar_state="expanded"  )


# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover;
#         background-position: 20% center;
        
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('image.jpg')   
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

    
def openai(description):
    reply = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=inpt,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
    explan= reply.choices[0].text.strip()
    st.stop()
    return explan

 
    
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

        with st.form(key="form"):
            st.subheader('Write for me')
            des=st.text_input(label='Description') 
    with col2:

        # para=st.text_input(label='Parameter') 
        submitted = st.form_submit_button('Submit')
        if submitted:
            x = openai(des)
            st.code(x)
                
    

#     elif choose == "Idea Generator":
#         with st.form(key="form2"):
#             st.subheader('Idea Generator')
#             des2=st.text_input(label='Description') 
#             para2=st.text_input(label='Parameter') 
#             submitted = st.form_submit_button('Submit')
#             if submitted:
#                 x = openai(des2)
#                 # if "x" not in st.session_state:
#                 st.session_state['x_result'] = x



#     elif choose == "Promotion Ideas":
#         with st.form(key="form2"):
#             st.subheader('Promotion Ideas')
#             des3=st.text_input(label='Description') 
#             # para2=st.text_input(label='Parameter') 
#             submitted = st.form_submit_button('Submit')
#             if submitted:
#                 x = openai(des2)
#                 # if "x" not in st.session_state:
#                 st.session_state['x_result'] = x



# with col2:
#     with st.container():
#         # if x is not None:
#         st.code(st.session_state['x'])