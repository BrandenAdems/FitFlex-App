"""



TITLE: FITFLEX APP
AUTHOR: BRANDEN ADEMS ANAK KIETHSON



"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is to import library
import streamlit as st

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is to set the page title, page icon and main title
st.set_page_config(
    page_title="About",
    page_icon="📖",
)


st.title("About")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is for the background picture
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://i2.wp.com/wallpapercave.com/wp/wp7377856.jpg");
background-size: cover
}
</style>

<style>
[data-testid="stHeader"] {
background-image: url("https://i2.wp.com/wallpapercave.com/wp/wp7377856.jpg");
background-size: cover
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
#This is the about section

st.header("The Purpose of this web app")

st.write("""

This app is designed to assist users to layout a plan on exercising. It is friendly for beginners
and also to those who wanted to maintained fit and would like to try different exercises.
With the app supported by ChatGPT AI model GPT-3.5-Turbo, it is able to plan out
an exercise plan and a diet plan. Without a diet plan, seeing a results would be much more slower.

""")

st.header("From Developer")

st.write("""

I am pleased to announce the release of this free app that assist those who planned
on a journey to lose weight and stay fit.
         
I would like to used this opportunity to express my gratitude to the open-source community
and my AI Instructor for showing me the ropes on how to start my very own AI App and publish 
it into streamlit. Your contributions have enabled me to make this tool available to everyone.
         
I hope this app will give significant impact on people's lives, and I am glad for the chance
to return something to the community.
         
Thank you!

Best Regard,

Branden Adems

(AI Trainee)
""")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------