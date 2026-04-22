
import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Mistik Mesaj", page_icon="🔮")
st.title("🔮 Hoş geldin, Mustafa")
st.subheader("Evren bugün senin için ne fısıldıyor?")

# Kasa Kontrolü
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # YENİ MODEL İSMİ BURADA
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Lütfen Secrets kısmına GEMINI_API_KEY ekle.")
    st.stop()

user_input = st.text_area("Kalbindekileri dök...", placeholder="Yanlızım...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            with st.spinner('Yıldızlarla bağlantı kuruluyor...'):
                response = model.generate_content(f"Sen mistik bir falcısın. Mustafa ' {user_input} ' diyor. Ona moral verecek, bilgece ve kısa bir cevap yaz.")
                st.success(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")
