import streamlit as st
import joblib 
import pandas as pd
model = joblib.load("heartmodel.pkl")
st.title("😊😊😊HEART💘 DISEASE PREDICTION😀💙💙")
st.write("JUST FILL THE PARAMETERS AND CHECK HEART DISEASE PREDICITION : ")
Age = st.slider("SELECT YOUR AGE:",2,100,20)
Sex = st.selectbox("SELECT YOUR GENDER: ",["M","F"])
ChestPainType = st.selectbox("SELECT YOUR CHESTPAIN TYPE :",["ATA","NAP","ASY","AT"])
RestingBP= st.number_input("ENTER YOUR RESTINGBP VALUE:")
Cholesterol = st.number_input("ENTER YOUR CHOLESTEROL VALUE:")
FastingBS= st.number_input("ENTER YOUR FASTINGBP VALUE:")
RestingECG	= st.selectbox("ENTER YOUR RESTINGBP VALUE:",["Normal","LVH","ST"])
MaxHR = st.number_input("ENTER YOUR MAXHR VALUE:")
ExerciseAngina	= st.selectbox("SELECT YOUR EXCERCISEANGINA TYPE :",["Y", "N"])
Oldpeak= st.number_input("ENTER YOUR OLDPEAK VALUE:")
ST_Slope= st.selectbox("SELECT YOUR STSLOPE TYPE :",["Flat", "Up"])
input = ["Age","Sex","ChestPainType","RestingBP","Cholesterol","FastingBS","RestingECG","MaxHR","ExerciseAngina","Oldpeak","ST_Slope"]
inputs = pd.DataFrame([{
        "Age": Age,
        "Sex": Sex,
        "ChestPainType": ChestPainType,
        "RestingBP": RestingBP,
        "Cholesterol":Cholesterol,
        "FastingBS":FastingBS,
        "RestingECG":RestingECG,
        "MaxHR":MaxHR,
        "ExerciseAngina":ExerciseAngina,
        "Oldpeak":Oldpeak,
        "ST_Slope":ST_Slope
    }])
if st.button("CHECK"):
    HeartDisease = model.predict(inputs)
    st.success(f"you have{HeartDisease} heart disease")
    st.subheader("📊 Your Health Parameters")

    chart_data = pd.DataFrame({
        "Parameter": ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"],
        "Value": [Age, RestingBP, Cholesterol, MaxHR, Oldpeak]
    })
    
    st.bar_chart(chart_data.set_index("Parameter"))