
import streamlit as st
import google.generativeai as genai

# Anahtarı kasadan alıyoruz
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.warning("Lütfen API anahtarını bağla.")
    st.stop()

st.title("🔮 Mistik Falcı")
st.write("Hoş geldin Mustafa! Bugün yıldızlar senin için ne söylüyor?")

user_input = st.text_input("Bir soru sor veya içinden geçeni yaz...")

if st.button("Falıma Bak"):
    if user_input:
        with st.spinner('Yıldızlarla konuşuyorum...'):
            try:
                response = model.generate_content(f"Mustafa'ya mistik ve bilgece bir fal bak: {user_input}")
                st.balloons()
                st.success(response.text)
            except:
                st.error("Bir bağlantı sorunu oldu, tekrar dene.")
    else:
        st.info("Lütfen önce bir şeyler yaz.")
