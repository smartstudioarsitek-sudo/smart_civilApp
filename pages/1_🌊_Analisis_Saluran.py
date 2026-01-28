import streamlit as st
import pandas as pd
from modules.hidrologi import SaluranTerbuka # Import Class buatan sendiri

# Set Config lagi (supaya konsisten tiap halaman)
st.set_page_config(page_title="Analisis Saluran", page_icon="🌊")

# Load CSS
with open('assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("🌊 Analisis Saluran Terbuka")
st.markdown("Metode Manning untuk Penampang Persegi")

# --- INISIALISASI SESSION STATE ---
# Agar hasil hitungan tidak hilang saat user klik-klik yang lain
if 'hasil_analisis' not in st.session_state:
    st.session_state['hasil_analisis'] = None

# --- INPUT SECTION (SIDEBAR) ---
with st.sidebar:
    st.header("Parameter Desain")
    b_in = st.number_input("Lebar Dasar (b) [m]", value=2.0, step=0.1)
    h_in = st.number_input("Tinggi Air (h) [m]", value=1.5, step=0.1)
    s_in = st.number_input("Kemiringan (S)", value=0.001, format="%.4f", step=0.0001)
    n_in = st.number_input("Koefisien Manning (n)", value=0.025, format="%.3f", help="0.025 untuk tanah saluran lurus")
    
    btn_hitung = st.button("🚀 Hitung Sekarang")

# --- LOGIC SECTION ---
if btn_hitung:
    # Panggil fungsi dari folder modules
    hasil = SaluranTerbuka.hitung_manning(b_in, h_in, s_in, n_in)
    
    # Simpan ke session state
    st.session_state['hasil_analisis'] = hasil

# --- OUTPUT SECTION ---
# Tampilkan hasil hanya jika sudah ada di session state
if st.session_state['hasil_analisis']:
    result = st.session_state['hasil_analisis']
    
    if result['status'] == 'success':
        # Tampilkan Metrics Utama
        col1, col2, col3 = st.columns(3)
        col1.metric("Kecepatan (V)", f"{result['V']} m/s")
        col2.metric("Debit (Q)", f"{result['Q']} m³/s")
        col3.metric("Froude (Fr)", result['Fr'], delta=result['Tipe_Aliran'])
        
        st.success(f"Status Aliran: **{result['Tipe_Aliran']}**")
        
        # Placeholder untuk Integrasi AI nanti
        with st.expander("🤖 Analisis AI (Simulasi)"):
            st.write("Di sini nanti Gemini akan memberikan komentar: 'Kecepatan aman untuk saluran tanah.'")
            
    else:
        st.error(f"Terjadi Kesalahan: {result['pesan']}")

else:
    st.info("Silakan masukkan parameter di sidebar dan klik Hitung.")