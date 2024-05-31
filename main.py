import streamlit as st

from streamlit_option_menu import option_menu

import home, about, contacts, info

st.set_page_config(
    page_title="Menu", 
)

class MultiApp:

    def __init__(self):
        
        self.apps = []

    def add_app (self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title = 'Menu',
                options= ['Home', 'About', 'Contacts' , 'Info'],
                icons= ['house-fill', 'android2', 'info',''],
                menu_icon= 'chat-text-fill',
                default_index= 1,
                styles= {
                    "container": {"padding": "5!important", "background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
    
        if app == 'Home':
            home.app()
        if app == 'About':
            about.app()
        if app == 'Contacts':
            contacts.app()    
        if app == 'Info':
            info.app()   

    run()







        