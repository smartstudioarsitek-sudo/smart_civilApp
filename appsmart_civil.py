import streamlit as st

# 1. KONFIGURASI HALAMAN (Wajib di baris pertama)
st.set_page_config(
    page_title="Smart Civil Engineering",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. LOAD CSS (Dengan Pengaman Error)
try:
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    pass # Jika file tidak ada, lanjut saja

# 3. KONTEN DASHBOARD
st.title("🏗️ Smart Civil Engineering Dashboard")
st.markdown("---")

col1, col2 = st.columns([2, 1])

# --- KOLOM KIRI: Sambutan & Navigasi ---
with col1:
    st.header("Selamat Datang, Engineer!")
    st.write("""
    Platform ini dirancang untuk membantu perhitungan teknik sipil yang presisi 
    serta didukung oleh **Artificial Intelligence** untuk verifikasi desain.
    """)
    
    st.info("💡 Tip: Gunakan menu di samping (Sidebar) atau tombol cepat di bawah ini:")

    # Tombol Navigasi Cepat
    col_nav1, col_nav2 = st.columns(2)
    
    with col_nav1:
        if st.button("🌊 Buka Analisis Hidrologi", use_container_width=True):
            st.switch_page("pages/1_🌊_Analisis_Hidrologi.py")
            
    with col_nav2:
        if st.button("🤖 Buka Konsultasi AI", use_container_width=True):
            st.switch_page("pages/3_🤖_Konsultasi_AI.py")

# --- KOLOM KANAN: Status Proyek ---
with col2:
    st.subheader("Status Proyek")
    # Contoh Widget Status (Data Dummy)
    st.metric(label="Proyek Aktif", value="3 Proyek")
    st.metric(label="Verifikasi AI", value="98% Aman", delta="+2%")
    
    with st.expander("Lihat Detail Proyek"):
        st.write("- D.I. Way Sekampung (On Progress)")
        st.write("- Embung A (Selesai)")

# Footer
st.markdown("---")
st.caption("© 2026 Smart Civil Engineering System | Versi 1.0.0 Alpha")
