import streamlit as st
from forms.conatct import contact_form
# st.title("About Me")

@st.dialog("Contact Me")
def show_contact_form():
    # st.text_input("First Name")
    contact_form()

col1,col2=st.columns(2,gap="small",vertical_alignment="center")

with col1:
    st.image("./assets/Gautham.jpg",width=230)
with col2:
    st.title("Gautham",anchor=False)
    st.write("Freelance Web Developer")
    if st.button("📧 Contact Me"):
        show_contact_form()

# Experience and Qualifiction
st.write("\n")
st.subheader("Experience & Qualifications",anchor=False)
st.write(
    """
    - 3 Years experience extracting actionable insight from data
    - Strong hands on experience and knowledge in Python and Java
    - Good understanding of Web Development principles and design philosophy
    """
)

# Skills
st.write("\n")
st.subheader("Skills",anchor=False)
st.write(
    """
    - Programming : Python, Java, C
    - Web : HTML, CSS, JS, React
    - Database : MySQL, MongoDB, Firebase
    - Frameworks and Libraries : Flutter, React
    
    """
)