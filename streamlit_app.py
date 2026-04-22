
import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Mistik Mesaj", page_icon="🔮")
st.title("🔮 Hoş geldin, Mustafa")
st.subheader("Evren bugün senin için ne fısıldıyor?")

# Gemini Anahtarını Çek
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("Hata: Secrets kısmında 'GEMINI_API_KEY' bulunamadı.")
    st.stop()

user_input = st.text_area("Kalbindekileri dök...", placeholder="Buraya yaz...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            # Ücretsiz Gemini Yanıtı
            response = model.generate_content(f"Sen mistik bir falcısın. Mustafa'ya şu konuda kısa, bilgece ve moral verici bir mesaj yaz: {user_input}")
            st.success(response.text)
        except Exception as e:
            st.error(f"Bir sorun oluştu: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")
