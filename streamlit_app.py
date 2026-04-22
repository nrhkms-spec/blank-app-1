
import streamlit as st
import google.generativeai as genai

# Anahtar Kontrolü
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # BURASI KRİTİK: İsim tam olarak bu olmalı
    model = genai.GenerativeModel('gemini-1.5-flash')

else:
    st.error("Secrets kısmında GEMINI_API_KEY bulunamadı!")
    st.stop()

st.title("🔮 Hoş geldin, Mustafa")
user_input = st.text_area("Kalbindekileri dök...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            response = model.generate_content(f"Mustafa diyor ki: {user_input}. Ona bilgece bir cevap ver.")
            st.success(response.text)
            st.balloons()
        except Exception as e:
            st.error(f"Hata oluştu: {e}")
