import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- CSS Styling ---
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0 !important;
        font-family: 'Times New Roman', Times, serif;
    }
    .main-container {
        background-color: #ffffffcc;
        padding: 40px 30px;
        border-radius: 20px;
        max-width: 800px;
        margin: auto;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
    }
    h1 {
        color: #cc3399;
        text-align: center;
        font-size: 36px;
    }
    label, .stNumberInput label, .stRadio label {
        font-weight: bold;
        color: #800040;
    }
    .stButton button {
        background-color: #ff66b2;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #a64d79;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
with open('Hepatitis_model.sav', 'rb') as file:
    model = pickle.load(file)

# Container utama
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown("## 💉 Prediksi Kategori Hepatitis")
    st.write("Masukkan data berikut untuk memprediksi kemungkinan kondisi kesehatan berdasarkan hasil tes darah.")

    # Form input
    age = st.number_input("🧍 Usia", min_value=1, max_value=100, value=30, step=1)
    sex = st.radio("🚻 Jenis Kelamin", ['Laki-laki', 'Perempuan'])
    alb = st.number_input("🧪 Albumin (ALB)", value=35.0, step=0.1)
    alp = st.number_input("🧪 Alkaline Phosphatase (ALP)", value=80.0, step=0.1)
    alt = st.number_input("🧪 Alanine Transaminase (ALT)", value=30.0, step=0.1)
    ast = st.number_input("🧪 Aspartate Transaminase (AST)", value=35.0, step=0.1)
    bil = st.number_input("🧪 Bilirubin (BIL)", value=0.9, step=0.1)
    che = st.number_input("🧪 Cholinesterase (CHE)", value=8.0, step=0.1)
    chol = st.number_input("🧪 Kolesterol (CHOL)", value=180.0, step=0.1)
    crea = st.number_input("🧪 Kreatinin (CREA)", value=1.0, step=0.1)
    ggt = st.number_input("🧪 Gamma-GT (GGT)", value=25.0, step=0.1)
    prot = st.number_input("🧪 Protein Total (PROT)", value=70.0, step=0.1)

    # Encode jenis kelamin
    sex_encoded = 1 if sex == 'Laki-laki' else 0
    features = np.array([[age, sex_encoded, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot]])

    # Tombol prediksi
    if st.button("🔍 Prediksi Sekarang"):
        prediction = model.predict(features)[0]
        label_dict = {
            0: "Blood Donor 🩸 (Sehat)",
            1: "Suspected Blood Donor 🤔",
            2: "Hepatitis 🦠",
            3: "Fibrosis 🧬",
            4: "Cirrhosis ⚠️"
        }
        st.success(f"Hasil Prediksi: **{label_dict.get(prediction, 'Tidak diketahui')}**")

    # Footer
    st.markdown('<div class="footer">© 2025 Sistem Informasi Kelautan - Prediksi Hepatitis</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
