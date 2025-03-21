import streamlit as st
st.title("HELLO WORLD")
st.write("This is a simple streamlit app.")

if st.button("say hello"):
	st.text("Hello, Streamlit")
	
name=st.text_input("Please enter your name: ")
if name:
	st.write(f'hello , {name}!')
	
if st.file_uploader()
