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
    # Jika file tidak ada, aplikasi tetap jalan tapi tanpa style khusus
    pass

# 3. KONTEN DASHBOARD
st.title("🏗️ Smart Civil Engineering Dashboard")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    with col1:
    st.header("Selamat Datang, Engineer!")
    st.write("""
    Platform ini dirancang untuk membantu perhitungan teknik sipil yang presisi 
    serta didukung oleh **Artificial Intelligence** untuk verifikasi desain.
    """)
    
    st.info("💡 Tip: Gunakan menu di samping (Sidebar) atau tombol di bawah ini:")

    # --- TAMBAHAN: TOMBOL NAVIGASI CEPAT ---
    col_nav1, col_nav2 = st.columns(2)
    
    with col_nav1:
        if st.button("🌊 Buka Analisis Hidrologi", use_container_width=True):
            st.switch_page("pages/1_🌊_Analisis_Hidrologi.py")
            
    with col_nav2:
        if st.button("🤖 Buka Konsultasi AI", use_container_width=True):
            st.switch_page("pages/3_🤖_Konsultasi_AI.py")
    st.header("Selamat Datang, Engineer!")
    st.write("""
    Platform ini dirancang untuk membantu perhitungan teknik sipil yang presisi 
    serta didukung oleh **Artificial Intelligence** untuk verifikasi desain.
    
    **Modul Tersedia:**
    - 🌊 **Analisis Hidrologi:** Perhitungan saluran terbuka (Manning).
    - 💰 **Smart RAB:** (Coming Soon) Analisis harga satuan.
    - 🤖 **Konsultasi AI:** (Coming Soon) Verifikasi desain dengan Gemini 1.5.
    """)
    
    st.info("💡 Tip: Pilih menu di Sidebar sebelah kiri untuk memulai modul perhitungan.")

with col2:
    # Contoh Widget Status Proyek (Data Dummy)
    st.subheader("Status Proyek")
    st.metric(label="Proyek Aktif", value="3 Proyek")
    st.metric(label="Verifikasi AI", value="98% Aman", delta="+2%")

# Footer
st.markdown("---")

st.caption("© 2026 Smart Civil Engineering System | Versi 1.0.0 Alpha")

