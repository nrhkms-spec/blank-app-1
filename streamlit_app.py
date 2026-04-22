
import streamlit as st
from openai import OpenAI

# BAŞLIK VE GÖRSEL
st.title("🔮 Hoş geldin, Mustafa")
st.subheader("Evren bugün senin için ne fısıldıyor?")

# ANAHTARI ÇAĞIRMA (İsim tam olarak bu olmalı)
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    st.error("Hata: Secrets kısmında 'OPENAI_API_KEY' bulunamadı.")
    st.stop()

user_input = st.text_area("Şu an ne hissediyorsun?", placeholder="Kalbindekileri dök...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            # AI Yanıtı
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Sen mistik bir falcısın. Mustafa'ya kısa ve anlamlı bir mesaj ver."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Eyvah! OpenAI bir hata verdi: {e}")
    else:
        st.warning("Lütfen önce bir şeyler yaz.")
