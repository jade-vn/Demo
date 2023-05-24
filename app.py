import streamlit as st
st.title('My App')
a=st.number_input("Enter a number")
b=st.number_input("Enter another number")
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
if operation == "Add":
    st.write(a+b)
elif operation == "Subtract":
    st.write(a-b)
elif operation == "Multiply":
    st.write(a*b)
else:
    st.write(a/b)