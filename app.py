import streamlit as st
from agent.graph import agent, save_files

# --- Page Config ---
st.set_page_config(
    page_title="Auto Code Builder",
    page_icon="💻",
    layout="wide"
)

# --- Custom Styling ---
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
    font-family: 'Segoe UI', sans-serif;
}

/* Center container */
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #94a3b8;
    margin-bottom: 30px;
}

/* Card UI */
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
    margin-bottom: 20px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 17px;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #0ea5e9, #4f46e5);
}

/* Text Area */
textarea {
    border-radius: 12px !important;
    padding: 10px !important;
}

/* Expander */
.streamlit-expanderHeader {
    font-size: 17px;
    font-weight: 600;
    color: #38bdf8;
}

/* Code block */
pre {
    border-radius: 10px !important;
}

/* Success box */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">💻 Auto Code Builder</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Turn your idea into working code instantly</div>', unsafe_allow_html=True)

# --- Input Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)

user_prompt = st.text_area(
    "📝 Describe your project",
    placeholder="Example: Build a full-stack todo app with authentication using FastAPI and React...",
    height=180
)

generate_btn = st.button("🚀 Generate Code")

st.markdown('</div>', unsafe_allow_html=True)

# --- Tips Section ---
with st.expander("💡 Tips for better results"):
    st.write("""
    - Clearly describe features  
    - Mention frameworks or languages  
    - Add constraints (e.g., "simple UI", "REST API only")  
    - Example: *"Create a blog API using FastAPI with JWT auth"*  
    """)

# --- Generation Logic ---
if generate_btn:
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a project description.")
    else:
        with st.spinner("⚙️ Generating your project..."):
            try:
                result = agent.invoke({"user_prompt": user_prompt.strip()})

                plan = result.get("plan", "")
                task_plan = result.get("task_plan", "")
                code_files = result.get("code_files", {})

                save_files(code_files)

                st.success(f"✅ Successfully generated {len(code_files)} files!")

                # --- Output Section ---
                st.markdown('<div class="card">', unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    with st.expander("📌 Project Plan"):
                        st.write(plan)

                with col2:
                    with st.expander("🧩 Architecture"):
                        st.write(task_plan)

                st.markdown("### 📂 Generated Files")

                # File viewer
                for filename, content in code_files.items():
                    with st.expander(f"📄 {filename}"):
                        ext = filename.split(".")[-1] if "." in filename else "text"
                        st.code(content, language=ext)

                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Error: {e}")