import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Smart Civil Engineering",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. LOAD CSS
try:
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    pass

# 3. KONTEN DASHBOARD
st.title("🏗️ Smart Civil Engineering Dashboard")
st.markdown("---")

col1, col2 = st.columns([2, 1])

# --- KOLOM KIRI ---
with col1:
    st.header("Selamat Datang, Engineer!")
    st.write("""
    Platform ini dirancang untuk membantu perhitungan teknik sipil yang presisi 
    serta didukung oleh **Artificial Intelligence** untuk verifikasi desain.
    """)
    
    st.info("💡 Tip: Silakan klik menu di **Sidebar (Kiri Atas)** untuk membuka modul.")
    
    # KITA HAPUS TOMBOL YANG ERROR, GANTI DENGAN INFO SAJA
    st.success("✅ Sistem Siap Digunakan. Pilih menu di samping kiri.")

# --- KOLOM KANAN ---
with col2:
    st.subheader("Status Proyek")
    st.metric(label="Proyek Aktif", value="3 Proyek")
    st.metric(label="Verifikasi AI", value="98% Aman", delta="+2%")

# Footer
st.markdown("---")
st.caption("© 2026 Smart Civil Engineering System | Versi 1.0.0 Alpha")
