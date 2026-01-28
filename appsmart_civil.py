import streamlit as st

# 1. KONFIGURASI HALAMAN (Wajib di baris pertama)
st.set_page_config(
    page_title="Smart Civil Engineering",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. LOAD CSS (Agar tampilan profesional)
with open('assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 3. KONTEN DASHBOARD
st.title("🏗️ Smart Civil Engineering Dashboard")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
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