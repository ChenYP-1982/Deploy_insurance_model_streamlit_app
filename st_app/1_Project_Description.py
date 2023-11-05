import streamlit as st

#This script is used to create a simple web app using Streamlit with side bars 
#and multipages

st.set_page_config(
    page_title="Insurance Prediction",
    page_icon= "../img/stethoscope.png"  # Change the title of your app here
)
#App header
st.sidebar.header('''Project Description \nMedical insurance prediction is crucial in healthcare as it predicts medical costs and helps healthcare organizations prepare for expenses.
    By analyzing factors like demographics, medical history, and lifestyle, insurance companies can set accurate premium rates
    and allocate resources effectively. This also helps high-risk individuals receive necessary resources and support.
    Overall, medical insurance prediction is a valuable tool for both patients and providers in a sustainable healthcare system.''')


st.write ("# :blue[_Welcome to the Insurance Prediction App_] 🩺")

st.write("\n\n")




st.image("img/health_insurance_img.jpg")



st.markdown(
'''
The venerable insurance industry is no stranger to data driven decision making. Yet in today's rapidly transforming digital landscape, Insurance is struggling to adapt and benefit from new technologies compared to other industries,
even within the BFSI sphere (compared to the Banking sector for example.) 
Extremely complex underwriting rule-sets that are radically different in different product lines, 
many non-KYC environments with a lack of centralized customer information base, 
complex relationship with consumers in traditional risk underwriting where sometimes customer centricity runs reverse to business profit, 
inertia of regulatory compliance - are some of the unique challenges faced by Insurance Business.

Despite this, emergent technologies like AI and Block Chain have brought a radical change in Insurance, 
and Data Analytics sits at the core of this transformation. 
We can identify 4 key factors behind the emergence of Analytics as a crucial part of InsurTech:

This App aims to predict the insurance cost using the following features:
* Age
* BMI( Body Mass Index )
* Number of children
* Smoker status
   '''
)

st.success("Please **go to next pages** to get the predictions ")



