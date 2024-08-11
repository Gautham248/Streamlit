import streamlit as st

# st.title("Gautham")

# Page Setup

about_me=st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page=st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

project_2_page=st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

# Navigation Menu

# pg=st.navigation(pages=[about_me,project_1_page,project_2_page])
# use python dictionaries to create navigation bar with sub menus

pg=st.navigation(
    {
        'Info':[about_me],
        'Projects':[project_1_page,project_2_page]
    }
)

# Run Navigation
pg.run()

# Anything that is displayed on the main page will be displayed on all pages
# st.logo("assets/Gautham.jpg")
st.sidebar.text("Made with ❤️ by Gautham")