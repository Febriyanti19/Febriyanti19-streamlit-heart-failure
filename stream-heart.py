from ast import If
import pickle
import streamlit as st

#Membaca Model
heart_model = pickle.load(open('heart_model.sav', 'rb'))

#Judul Web
st.title('DATA MINING PREDIKSI GAGAL JANTUNG')

st.subheader('NAMA : FEBRIYANTI SYOFIANI')
st.subheader('NIM : 191351031')

#Membagi Kolom
col1, col2 = st.columns (2)

with col1 :
 Age = st.number_input('Input Nilai Age')

with col2 :
 Anaemia = st.number_input ('Input Nilai Anaemia')

with col1 :
 Creatinine_phosphokinase = st.number_input (' Input Nilai atinine_phosphokinase')

with col2 :
 Diabetes = st.number_input ('Input Nilai Diabetes')

with col1 :
 Ejection_fraction = st.number_input ('Input Nilai Ejection_fraction')

with col2 :
 High_blood_pressure = st.number_input ('Input Nilai High_blood_pressure')

with col1 :
 Platelets = st.number_input (' Input Nilai Platelets')

with col2 :
 Serum_creatinine = st.number_input ('Input Nilai Serum_creatinine')

with col1 :
 Serum_sodium = st.number_input ('Input Nilai Serum_sodium')

with col2 :
 Sex = st.number_input ('Input Nilai Sex')

with col1 :
 Smoking = st.number_input ('Input Nilai Smoking')

with col2 :
 Time = st.number_input ('Input Nilai Time')

#code untuk prediksi
 heart_diagnosis = ''

#membuat tombol
if st.button('Test') :
    heart_prediction = heart_model.predict([[Age, Anaemia, Creatinine_phosphokinase, Diabetes, Ejection_fraction, High_blood_pressure, Platelets, Serum_creatinine, Serum_sodium, Sex, Smoking, Time]])
    
    if  (heart_prediction[0] == 1):
           heart_diagnosis = 'Pasien terkena Gagal jantung'
    else :
           heart_diagnosis = 'Pasien tidak terkena Gagal jantung'

st.success(heart_diagnosis)
