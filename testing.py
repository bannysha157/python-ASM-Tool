import streamlit as st
from PIL import Image
image1=Image.open("thundersoft.png")
col1, col2, col3 = st.columns([2,2,2])

with col3:
    st.write("")

with col1:
    st.image(image1)

with col2:
    st.write("")
st.markdown('\n **Choose One**.')
Emp_det,Assert=st.columns([2,2])
with Emp_det:
    Emp_details=st.selectbox("enter your choose",
            ("Mail","Emp_name","Emp_id"))
    if Emp_details=="Mail":
        Email=st.text_input("Enter your mailid")
        st.write(Email)
    elif Emp_details=="Emp_name":
        Emp_name=st.text_input("Enter your name")
        st.write(Emp_name)
    else:
        Emp_id=st.text_input("Enter your id")
        st.write(Emp_id)
with Assert:
    st.write("")


#st.radio("Select one",("Name","Id"))