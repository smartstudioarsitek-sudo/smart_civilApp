import streamlit as st
from modules.ai_service import tanya_gemini

st.set_page_config(page_title="Konsultasi AI", page_icon="🤖")

st.title("🤖 Asisten Teknik Sipil (AI)")

# Input User
pertanyaan = st.text_area("Tulis masalah teknis Anda (Misal: 'Jelaskan tahapan pengecoran beton K-300'):")

if st.button("Tanya AI"):
    if pertanyaan:
        with st.spinner("Sedang menganalisis..."):
            # Panggil fungsi dari folder modules
            jawaban = tanya_gemini(pertanyaan)
            
            st.markdown("### Jawaban AI:")
            st.write(jawaban)
    else:
        st.warning("Mohon isi pertanyaan terlebih dahulu.")