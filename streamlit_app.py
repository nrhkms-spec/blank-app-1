
import streamlit as st
from openai import OpenAI

# API anahtarını doğrudan "Sırlar" (Secrets) kısmından çekiyoruz
# Buradaki ismin Secrets kısmındakiyle AYNI olması şart
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("API anahtarı bulunamadı! Lütfen Secrets kısmına OPENAI_API_KEY ekleyin.")
