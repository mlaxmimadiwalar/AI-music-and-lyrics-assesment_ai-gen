import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Music and Lyrics Assignment",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling to give a sleek dark theme aesthetic
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stMetric {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #334155;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #6366f1;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: Song Settings ---
with st.sidebar:
    st.title("🎼 Song Settings")
    st.markdown("---")
    
    language = st.selectbox("🌐 Language", ["English", "Spanish", "French", "German", "Hindi", "Japanese"])
    genre = st.selectbox("🎼 Genre", ["Pop", "Rock", "Hip-Hop", "R&B", "Indie", "Electronic", "Jazz"])
    bpm = st.slider("🎵 BPM", min_value=60, max_value=180, value=110)
    key = st.selectbox("🎹 Key", ["C Major", "G Major", "D Major", "A Minor", "E Minor", "F Major"])
    mood = st.selectbox("🎭 Mood", ["Hopeful", "Energetic", "Melancholic", "Chill", "Dramatic", "Upbeat"])
    
    instrumentation = st.text_input("🎹 Instrumentation", value="Piano, Acoustic Guitar, Soft Synth")
    vocal_style = st.text_input("🎤 Vocal Style", value="Warm male/female lead vocal")
    song_length = st.text_input("🎼 Song Length", value="3:30")
    
    st.markdown("---")
    generate_btn = st.button("✨ Generate Lyrics")

# --- MAIN CONTENT AREA ---
st.title("🎵 AI Music and Lyrics Assignment")
st.caption("✨ AI MUSIC CREATION STUDIO")
st.subheader("Turn your ideas into songs, lyrics, and musical direction.")

st.divider()

# Selected Parameters Overview Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="🌐 Language", value=language)
with col2:
    st.metric(label="🎼 Genre", value=genre)
with col3:
    st.metric(label="🎵 BPM", value=f"{bpm} BPM")
with col4:
    st.metric(label="🎹 Key", value=key)

st.divider()

# Layout: Lyrics vs Music Direction Blueprint
left_col, right_col = st.columns([3, 2])

with left_col:
    st.subheader("✍️ Generated Lyrics")
    
    if generate_btn:
        st.success("Lyrics generated successfully!")
        st.markdown(f"""
        **(Verse 1)**  
        Walking down this open road,  
        Shadows fading in the light.  
        Carrying a lighter load,  
        Everything is feeling right.  

        **(Chorus)**  
        We're moving with the {bpm} rhythm flow,  
        Underneath the golden skies.  
        Where the hopeful feelings grow,  
        See the world with open eyes.  
        """)
    else:
        st.info("Configure your song settings in the sidebar and click **Generate Lyrics**.")

with right_col:
    st.subheader("🎧 Music Direction")
    st.caption("Production Blueprint")
    
    with st.container(border=True):
        st.markdown(f"**🎹 Instrumentation:** {instrumentation}")
        st.markdown(f"**🥁 Rhythm:** {bpm} BPM rhythm flow")
        st.markdown(f"**🎤 Vocals:** {vocal_style}")
        st.markdown(f"**🎼 Song Length:** {song_length}")
        st.markdown(f"**🎭 Mood:** {mood}")
        st.markdown(f"**🎼 Musical Key:** {key}")