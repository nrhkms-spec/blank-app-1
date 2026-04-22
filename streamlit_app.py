
import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Mistik Mesaj", page_icon="🔮")
st.title("🔮 Hoş geldin, Mustafa")
st.subheader("Evren bugün senin için ne fısıldıyor?")

# Kasadaki (Secrets) anahtarı çekiyoruz
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # BURASI ÇOK ÖNEMLİ: Yeni model adını yazdık
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Lütfen Secrets kısmına GEMINI_API_KEY ekleyin.")
    st.stop()

user_input = st.text_area("Kalbindekileri dök...", placeholder="Şu an ne hissediyorsun?")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            with st.spinner('Yıldızlarla konuşuyorum...'):
                # Falcıya talimat veriyoruz
                response = model.generate_content(f"Sen bilge bir falcısın. Mustafa sana '{user_input}' diyor. Ona Türkçe, kısa, samimi ve moral verici bir cevap yaz.")
                st.success(response.text)
                st.balloons() # Kutlama balonları patlasın!
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")
