import streamlit as st

from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contacts"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contacts":
    st.title(f"you have selected {selected}")
