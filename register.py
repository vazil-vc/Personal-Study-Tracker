import streamlit as st
import json
def registration():
    name=st.text_input("enter the name: ")
    email=st.text_input("enter the email: ")
    password=st.text_input("enter the password:",type='password')
    confirm_password=st.text_input("enter the confirm password: ",type='password')
    if st.button("REGISTER"):
        if name.strip()=="":
            st.warning("name can't empty")
            return None
        if email.strip()=="":
            st.warning("email can't empty")
            return None
        if password.strip()=="":
            st.warning("email can't empty")
            return None
        if password !=confirm_password:
            st.warning("password not matched")
            return None
        user={"name":name,"email":email,"password":password}
        try:
            file=open("users.json",'r')
            users=json.load(file)
            file.close()
        except FileNotFoundError:
            users=[]
        users.append(user)
        file=open("users.json",'w')
        json.dump(users,file)
        file.close()
        return users
    return None