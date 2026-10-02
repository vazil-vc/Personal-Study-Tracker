from subject import Subject
from study import Study
import streamlit as st
sd=Study()
sub=Subject()

def menu():
    while True: 
        try:
            choice=int(input("1.add\n2.view\n3.update\n4.delete\n5.tracker\n6.exit\nenter your choice: "))
        except ValueError:
            print("enter a number")
            continue
        if choice==1:
            sn=st.text_input("enter the subject name: ")
            sub.add_subject(sn)
        elif choice==2:
            subjects=sub.get_subject()
            for i,s in enumerate(subjects,start=1):
                print(i,".",s)
        elif choice==3:
            pn=st.text_input("enter the subject name: ")
            nm=st.text_iinput("enter the new subject name: ")
            if sub.update_subject(pn,nm):
                print("updated")
            else:
                print("not found")
        elif choice==4:
            n=st.text_input("enter the subject name: ")
            if sub.delete_subject(n):
                print("deleted")
            else:
                print("not found")
        elif choice==5:
            t_choice=int(input("1.add\n2.view\n3.update\n4.delete\n5.exit\nenter the option:"))
            if t_choice==1:
                subject=st.text_input("enter the subject name :")
                hr=int(st.text_input("enter hour: "))
                date=st.text_input("enter the date: ")
                subjects=sub.get_subject()
                if subject in subjects:
                    sd.add_tracker(subject,hr,date)
                else:
                    print("not exsting")
            elif t_choice==2:
                print(sd.get_tracker())    
            elif t_choice==3:
                new_subject=st.text_input("enter the update subject: ")
                p_subject=st.text_input("enter the previous subject: ")
                if sd.update(p_subject,new_subject):
                    print("update")
                else:
                    print("not exist")
            elif t_choice==4:
                new_subject=st.text_input("enter the subject: ")
                sd.delete(new_subject)
            elif t_choice==5:
                print("go to main menu")
                break
            else:
                print("invalid choice")
        elif choice==6:
            print("go to main menu")
            break
        else:
            print("invalid choice")

