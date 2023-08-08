import streamlit as st
import FitFlex

# Creating a page logo
st.set_page_config(
    page_title="FitFlex",
    page_icon="🏋️‍♂️",
    )

def run_app():

    FitFlex.main()


if __name__ == "__main__":
    run_app()

