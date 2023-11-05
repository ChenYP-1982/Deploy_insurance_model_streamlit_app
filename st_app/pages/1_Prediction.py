import pandas as pd
import pickle 
import streamlit as st


# page config
st.set_page_config(page_title="Insurance Prediction", 
                   page_icon="../img/stethoscope.png"
                   )

st.sidebar.header(''':blue[**What if Prediction**] \n 
Please insert your prediction variables 
* Age
* BMI
* Children
* Smoker''')

st.write("# :blue[_Insurance Prediction_]")

         
#----Parameters----#


age=st.number_input(label="Age", 
                    value=18,
                    min_value=18,
                    max_value=120)
st.write(f"Sua idade é  { age}")

bmi=st.number_input ( label= "BMI",
                     min_value=12.0,
                    max_value=50.0)
st.write(f"Seu indice de massa corporal  é  { bmi:.2f}")

children=st.slider(label="Children", 
                         min_value=0,
                         max_value=10)
st.write(f"Voce tem  { children} filhos")

smoker=st.selectbox(label="Smoker", options=["no", "yes"])

with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def prediction():
    df_input=pd.DataFrame([{
       "age":age,
       "bmi":bmi,
       "children":children,
       "smoker":smoker
}])
    prediction=model.predict(df_input)[0]
    return prediction


if st.button("Predict"):
    try:
        insurance_cost=prediction() 
        st.success(f"Your insurance cost will be {insurance_cost:.2f}")
    except Exception as error:
        st.error(f"Error in predicting the cost of insurance.{error}")

