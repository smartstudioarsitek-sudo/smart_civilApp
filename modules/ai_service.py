import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key dari file .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def tanya_gemini(prompt_text):
    """
    Fungsi universal untuk bertanya ke Gemini.
    """
    if not api_key:
        return "ERROR: API Key belum disetting di file .env"
    
    try:
        genai.configure(api_key=api_key)
        # Gunakan model flash agar cepat & murah
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"Terjadi kesalahan koneksi AI: {str(e)}"