
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mistik Mesaj", page_icon="🔮")
st.title("🔮 Hoş geldin, Mustafa")
st.subheader("Evren bugün senin için ne fısıldıyor?")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.warning("Lütfen API anahtarını bağla.")
    st.stop()

user_input = st.text_area("Kalbindekileri dök...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            with st.spinner('Yıldızlarla konuşuyorum...'):
                response = model.generate_content(f"Sen bilge bir falcısın. Mustafa sana '{user_input}' diyor. Ona Türkçe, kısa ve moral verici bir cevap yaz.")
                st.success(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"Hata: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")
