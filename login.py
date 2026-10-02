import streamlit as st
import json
def login():
    name=st.text_input("enter the name: ")
    password=st.text_input("enter the password: ")
    if st.button("LOGIN"):
        try:
            file=open("users.json",'r')
            users=json.load(file)
            file.close()
        except FileNotFoundError:
            st.error("user not exist")
            return False
        for user in users:
            if user["name"]==name and user["password"]==password:
                return True
        st.error("Invalid Username or Password")    
    return False