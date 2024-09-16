import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import base64

st.set_page_config(page_title="Tharik", page_icon=":tada:", layout="wide")

#function to define lottie animation 
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



#assets
lottie_coding=load_lottieurl("https://lottie.host/28785e1d-98c4-4616-8b78-e0da2c9afe6c/m79m8uNtFp.json")
lottie_code=load_lottieurl("https://lottie.host/39c705ef-04a4-4d2a-ad08-7e9221028e72/NZ43eclJnH.json")
image1=Image.open("web/pro 3.GIF")
img2=Image.open("web/pro2.JPG")
img3=Image.open("web/pro1.JPG")

st.write("##")
st.subheader("Hey Guys!:wave:")
st.title("My Portfolio Website")
st.subheader("I am Mohamed Tharik")
st.write(" I am  passionate about finding ways to use python to effective in modern world")
st.write("[Know more>>](dm.wa.link/e4r2ws)")

with st.container():
    selected=option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )


if selected=='About':
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.write("##")
            st.title("I am Mohamed Tharik:wave:")
            st.subheader("Profile Summary")
            st.write(""" 
                     Dynamic knowledge in Python and Basics in Django, Streamlit and RDBMS. Fresh 
                     Graduate with an aptitude for aptitude and passion for Continuous Learning.
                     Eager to contribute to collaborative and impactful Software development projects and drive innovation in field""")
            st.subheader("Resume")
            file_path = "web/Mohamed Tharik.PDF"
            with open(file_path, "rb") as file:
                st.download_button(
                    label="Download File",
                    data=file,
                    file_name="Mohamed Tharik.PDF",
                    #mime="text/plain"  # Adjust MIME type based on your file
                )

        with col2:
            st_lottie(lottie_coding, height=300)
    st.write("---")

    with st.container():
        col3,col4=st.columns(2)
        with col3:
            st.header("Education-College")
            
            st.subheader("Post Graduate")
            st.write("M.Sc - Computer Science")
            st.write ("2022 - 2024")
            st.write("GTN arts and science college") 
            st.write("CGPA – 7")

            st.subheader("Under Graduate")
            st.write("B.Sc - Computer Science") 
            st.write("2019 - 2022")
            st.write("Parvathis arts and science college") 
            st.write("CGPA – 6.7")
        with col4:
            st.header("Education-School")
            st.subheader("Higher Secondary")
            st.write("CSMA Higher Secondary School(2019)")
            st.write("Percentage = 47%")

            st.subheader("SSLC")
            st.write("TPKN Matric Higher Secondary School(2017)")
            st.write("Percentage = 97%")


if selected=='Projects':
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5,col6=st.columns((1,2))
        with col5:
            st.subheader("Plant Disease Identification")
            st.image(image1)
            st.write("---")
            st.write("###")
        with col6:
            st.subheader("The development of plant disease detection, to recognize the disease and suggesting a remedy to it")
            st.write("""
                 The project entitled “Plant Disease Identification” is crucial for ensuring plant quality and food security.
                 Recent advances in computer vision and machine learning techniques have made it possible 
                 to accurately detect, classify, and monitor plant diseases based on images of leaves.""")
            st.markdown("[Contact me...](dm.wa.link/e4r2ws)")
            st.write("######")
            st.write("---")
            st.write("###")
        with col5:
            st.subheader("Online Grocery Store")
            st.image(img2)
            st.write("---")
            st.write("###")
        with col6:
            st.subheader("The development of an online grocery, to track offer and availability of an item in the market")
            st.write(""" 
                 Shop Management System is a software application to be developed to manage most of the activities or tasks running in a grocery shop.
                 This system divided in to three main categories: cashier/stock management, supplier information management/generating report, staff management00.
                 This application will provide the basic features such as cashier to handle sales transaction, stock management to control.""")
            st.markdown("[Contact me...](dm.wa.link/e4r2ws)")
            st.write("######")
            st.write("---")
            st.write("###")


        with col5:
            st.subheader("Eye Bank Management")
            st.image(img3)
            st.write("---")
            st.write("#####")

        with col6:
            st.subheader("The development of Eye Bank system,to track camp and donor details")
            st.write("""  
                  This application is built such a way that it should suits for all type of Eye Banks in future. 
                  So every effort is taken to implement this project in this Eye Bank, on successful implementation in this Eye Bank, 
                  we can target other Eye Banks in the city""")
            st.markdown("[Contact me...](dm.wa.link/e4r2ws)")
            st.write("##")
            st.write("---")

if selected=='Contact':
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

# HTML form from FormSubmit
    contact_form = """
        <form action="https://formsubmit.co/mhmdtharik017@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; margin: 4px 0; border: 1px solid #ccc; border-radius: 4px;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; margin: 4px 0; border: 1px solid #ccc; border-radius: 4px;">
        <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 8px; margin: 4px 0; border: 1px solid #ccc; border-radius: 4px;"></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
    </form>
"""

# Create columns layout
    left_column, right_column = st.columns(2)

# Display form in the left column
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:

        st_lottie(lottie_code, height=300)
