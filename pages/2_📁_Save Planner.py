"""



TITLE: FITFLEX APP
AUTHOR: BRANDEN ADEMS ANAK KIETHSON



"""
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is to import library
import streamlit as st
from datetime import date


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is to set the page title and icon
st.set_page_config(
    page_title="Save Planner",
    page_icon="📁",
)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is for the background picture
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://i.pinimg.com/originals/67/18/22/671822c2f63dd5f65d8fd15c9710420b.jpg");

}
</style>

<style>
[data-testid="stHeader"] {
background-image: url("https://i.pinimg.com/originals/67/18/22/671822c2f63dd5f65d8fd15c9710420b.jpg");

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This section is for the sidebar transparency
sidebar_style = """

<style>
.css-1cypcdb {
background-color: rgba(255, 255, 255, 0.2);
}
</style>


"""
st.markdown(sidebar_style, unsafe_allow_html=True)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This section is for the text color background
text_color = """

<style>
.css-q8sbsg {

background-color: black;

}
</style>

"""

st.markdown(text_color, unsafe_allow_html=True)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This Section is for the download button, the user input, the calendar and the main title
def main():
    st.title("Save Planner")

    # Display a calendar and retrieve the selected date
    selected_date = st.date_input("Select a date", date.today())

    # Display the selected date
    st.write("Selected date:", selected_date)


    # User input
    user_input = st.text_area("Paste the planner that you copy from FitFlex to save it:", "")

    st.download_button("Download", data= user_input, file_name= f"{selected_date}_Fitness_Planner.txt", mime="text/plain")


if __name__ == "__main__":
    main()