import streamlit as st
import pandas as pd
import pickle
#-------Setting side bar infos-------#

st.set_page_config(page_title="File Prediction",
                   page_icon="../img/stethoscope.png")

st.sidebar.header(''':blue[**Insert your file for prediction**]
File format:
* CSV
''')
st.write ("# :blue[_Insurance prediction_]")

#-------Model-------#

with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

#---File uplpader---#
data=st.file_uploader("Please upload your file")
if data:
    df_input=pd.read_csv(data)
    insurance_prediction=model.predict(df_input)
    df_output=df_input.assign(prediction=insurance_prediction.round(2))

st.markdown("Insurance output \n\n")
try:
    st.write(df_output)
except:
    #preventing showing error at streamlit app
    st.error("Please make sure that already upload your file")
    st.stop()

st.download_button(label= "Download file CSV", data=df_output.to_csv(index=False).encode("utf-8"),
                   mime="text/csv", file_name="predicted_insurance_cost.csv" )

