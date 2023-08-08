import streamlit as st
import FitFlex

def run_app():
    st.set_page_config(
        page_title="FitFlex",
        page_icon="🏋️‍♂️",
    )
    
    FitFlex.main()


if __name__ == "__main__":
    run_app()

