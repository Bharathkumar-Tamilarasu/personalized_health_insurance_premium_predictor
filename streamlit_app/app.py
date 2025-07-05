import streamlit as st
from predict_page import predictor
from about_page import show_about_page
from streamlit_option_menu import option_menu

if __name__ == "__main__":
    
    print("\nStarting the Streamlit App....\nHere you goooo...")

    st.title("Personalized Health Insurance Premium Predictor 🏥💳")

    selected_option = option_menu(
        menu_title=None,
        options=["Prediction", "About",],
        icons=["graph-up", "info-circle"],
        menu_icon=["list"],
        default_index=0,
        orientation="horizontal",
    )

    if selected_option == "About":
        show_about_page()
    elif selected_option == "Prediction":
        predictor()