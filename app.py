import streamlit as st
from register import registration
from login import login
from subject import Subject
from study import Study
st.set_page_config(
    page_title="Personal Study Tracker",
    page_icon="📚"
)

st.sidebar.title("Menu")

menu = st.sidebar.selectbox(
    "Choose",
    [
        "Register",
        "Login",
        "Subjects",
        "Study Tracker"
    ]
)

if menu=="Register":
    st.header ("REGISTER")
    users=registration()

    if users:
        st.success("Registered Successfully")

if menu=="Login":
    st.header("LOGIN")

    user=login()

    if user:
        st.success("logined")

if menu=="Subjects":
    sub=Subject()
    st.header("Subject")
    choice=st.selectbox("operations",
        ["add","view","update","delete"]
    )
    if choice=="add":
        subject=st.text_input("subject name")
        if st.button("add"):
            if subject.strip() == "":
                st.warning("Subject can't be empty")
            else:
                sub.add_subject(subject)
                st.success("subject added successfully")
    elif choice=="view": 
        subjects=sub.get_subject()
        st.write("Subjects")
        for s in subjects:
            st.write(s)
    elif choice=="update":
        ps=st.text_input("enter the previous subject name: ")
        ns=st.text_input("enter the new subject name: ")
        if st.button("update"):
            if ps.strip() == "" or ns.strip() == "":
                st.warning("Subject names can't be empty")  
            elif sub.update_subject(ps,ns):
                st.success("subject updated successfully")
            else:
                st.warning("subject not found")
    elif choice=="delete":
        subject=st.text_input("enter the subject name: ")
        if st.button("delete"):
            if subject.strip() == "":
                st.warning("Subject can't be empty")        
            elif sub.delete_subject(subject):
                st.success("subject deleted successfully")
            else:
                st.warning("subject not found")
if menu == "Study Tracker":
    tr=Study()

    st.header("Study Tracker")

    choice=st.selectbox("operations",
        ["add","view","update","delete"])

    if choice=="add":
        sbj=st.text_input("Subject")
        hr=st.number_input("Hours")
        date = st.text_input("Date")
        if st.button("Save"):
            if sbj.strip() == "" or hr <= 0 or date.strip() == "":
                st.warning("Please fill in all fields correctly")
            else:
                tr.add_tracker(sbj, hr, date)
                st.success("Saved")
    elif choice=="view":
        records=tr.get_tracker()
        st.title("Study Records")
        for r in records:
            st.write("**Subject:**", r["subject"])
            st.write("**Hours:**", r["hours"])
            st.write("**Date:**", r["date"])
            st.divider()
    elif choice=="update":
        ps=st.text_input("enter the previous subject name: ")
        ns=st.text_input("enter the new subject name: ")
        if st.button("update"):
            if ps.strip() == "" or ns.strip() == "":
                st.warning("Subject names can't be empty")  
            elif tr.update(ps,ns):
                st.success("subject updated successfully")
            else:
                st.warning("subject not found")
    elif choice=="delete":
        subject=st.text_input("enter the subject name: ")
        if st.button("delete"):
            if subject.strip() == "":
                st.warning("Subject can't be empty")        
            elif tr.delete(subject):
                st.success("subject deleted successfully")
            else:
                st.warning("subject not found") 
