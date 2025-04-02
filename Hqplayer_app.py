import streamlit as st
from streamlit.components.v1 import html
import os

st.set_page_config(page_title="HQPlayer Filterberater – Mac Mini M1 Real Setup", layout="centered")
st.markdown("""
<style>
    .stApp {
        background-color: #1e1e1e;
        color: #f5f5f5;
    }
    .highlight {
        display: inline-block;
        padding: 0.2em 0.5em;
        border-radius: 0.3em;
        font-weight: bold;
    }
    .filter { background-color: #007acc; color: white; }
    .taps { background-color: #a020f0; color: white; }
    .dither { background-color: #ffc400; color: black; }
    .rate { background-color: #00bcd4; color: black; }
    .cpu { background-color: #ff7043; color: black; }
    .sound { background-color: #7e57c2; color: white; }
</style>
""", unsafe_allow_html=True)

st.title("🎧 HQPlayer Filterberater – Mac Mini M1 + Aune X8")

if st.button("🛑 Streamlit Not-Aus beenden"):
    st.warning("Streamlit wird jetzt sofort beendet...")
    st.stop()
    os._exit(0)

recommendations = {
    "Klassik": [
        {"filter1x": "poly-sinc-gauss-short", "filterNx": "poly-sinc-gauss", "taps": "256k / 512k", "dither": "Gauss2", "rate": "384 kHz", "cpu": "🟡 Mittel", "sound": "🎻 Weich & musikalisch", "comment": "Ruhige Kombination mit musikalischem Flow"},
        {"filter1x": "sinc-M", "filterNx": "poly-sinc-gauss", "taps": "64k / 512k", "dither": "Gauss2", "rate": "384 kHz", "cpu": "🟢 Leicht", "sound": "🎼 Direkt & klar", "comment": "Kompromiss aus Natürlichkeit & Effizienz"}
    ],
    "Pop": [
        {"filter1x": "sinc-Lm", "filterNx": "poly-sinc-gauss", "taps": "512k / 512k", "dither": "Shaped", "rate": "384 kHz", "cpu": "🟡 Mittel", "sound": "🎤 Punchy & präsent", "comment": "Klassiker für moderne Musik – sauber & voll"},
        {"filter1x": "sinc-M", "filterNx": "sinc-Lm", "taps": "64k / 512k", "dither": "TPDF", "rate": "384 kHz", "cpu": "🟢 Leicht", "sound": "🎧 Klar & direkt", "comment": "Für schnelles, dynamisches Playback ohne Stolpern"}
    ],
    "Ambient": [
        {"filter1x": "sinc-MG", "filterNx": "poly-sinc-gauss", "taps": "128k / 512k", "dither": "Gauss2", "rate": "384 kHz", "cpu": "🟡 Mittel", "sound": "🌫️ Sanft & fließend", "comment": "Ideal für Klangteppiche mit weicher Note"},
        {"filter1x": "sinc-M", "filterNx": "sinc-Lm", "taps": "64k / 512k", "dither": "Gauss2", "rate": "384 kHz", "cpu": "🟢 Leicht", "sound": "🧘 Ruhig & sparsam", "comment": "Maximale Effizienz mit Ambient-Vibe"}
    ],
    "HipHop": [
        {"filter1x": "sinc-M", "filterNx": "poly-sinc-ext2", "taps": "64k / 8M", "dither": "TPDF", "rate": "352.8 / 384 kHz", "cpu": "🔴 Hoch", "sound": "🎧 Fette Bässe & Transienten", "comment": "Derb detaillierte Kombination für Vocals & Bass"},
        {"filter1x": "sinc-M", "filterNx": "sinc-Lm", "taps": "64k / 512k", "dither": "TPDF", "rate": "384 kHz", "cpu": "🟢 Leicht", "sound": "🎙️ Druckvoll & direkt", "comment": "Simpel & trotzdem mächtig im Flow"}
    ],
    "Electro": [
        {"filter1x": "poly-sinc-gauss-short", "filterNx": "poly-sinc-ext2", "taps": "1M / 8M", "dither": "TPDF", "rate": "352.8 / 384 kHz", "cpu": "🔴 Hoch", "sound": "💥 Knackig & detailreich", "comment": "Smarter Mix aus Leichtigkeit bei 1x & Power bei Nx für Beats & Transienten"},
        {"filter1x": "sinc-M", "filterNx": "sinc-Lm", "taps": "64k / 512k", "dither": "Shaped", "rate": "384 kHz", "cpu": "🟢 Leicht", "sound": "🎚️ Schnell & direkt", "comment": "Kombi für saubere Transienten & flüssiges Playback auf M1"}
    ],
    "Allround": [
        {"filter1x": "sinc-M", "filterNx": "poly-sinc-gauss", "taps": "64k / 512k", "dither": "Gauss2", "rate": "384 kHz", "cpu": "🟢 Leicht", "sound": "🪄 Vielseitig & direkt", "comment": "Allround-Empfehlung mit balancierter Filterwahl"},
        {"filter1x": "poly-sinc-gauss-short", "filterNx": "poly-sinc-gauss", "taps": "256k / 512k", "dither": "TPDF", "rate": "384 kHz", "cpu": "🟡 Mittel", "sound": "🎧 Sanft & musikalisch", "comment": "Smarte Kombi für Streaming & spontane Sessions"}
    ]
}

selected_genre = st.selectbox("Wähle deine Musikrichtung:", list(recommendations.keys()))
st.markdown(f"## Filtervorschläge für _{selected_genre}_")

for rec in recommendations[selected_genre]:
    st.markdown(f"""
    ---
    ❤️ **Loved Setting**

    - **Filter (1x):** <span class='highlight filter'>{rec['filter1x']}</span>  
    - **Filter (Nx):** <span class='highlight filter'>{rec['filterNx']}</span>  
    - **Taps:** <span class='highlight taps'>{rec['taps']}</span>  
    - **Dither:** <span class='highlight dither'>{rec['dither']}</span>  
    - **Empfohlene Ausgabe-Frequenz:** <span class='highlight rate'>{rec['rate']}</span>  
    - **CPU-Last:** <span class='highlight cpu'>{rec['cpu']}</span>  
    - **Klangprofil:** <span class='highlight sound'>{rec['sound']}</span>  

    💬 _{rec['comment']}_
    """, unsafe_allow_html=True)
