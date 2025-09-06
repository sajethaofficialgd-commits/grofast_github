import streamlit as st

st.title("say hello to everyone")

name = st.text_input("Enter your name")
if st.button("how was your day"):
    if name:
        st.success(f"hello{name} , Welcome to our new trail")
    else:
        st.warning("please enter your name")    