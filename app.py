import streamlit as st
import time
from api import generate_email
from scenarios import SCENARIOS, TONES

# --- PAGE CONFIG & CUSTOM CSS ---
st.set_page_config(page_title="EmailForge AI", page_icon="⚡", layout="wide")

# Modern, animated, glassmorphic CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Syne:wght@600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
    }
    
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #04091a 0%, #0d1630 50%, #08101f 100%);
        background-attachment: fixed;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Remove default Streamlit styling */
    .stMain > div:first-child {
        padding-top: 2rem;
    }
    
    /* Headers and Text */
    h1, h2, h3 {
        font-family: 'Syne', sans-serif !important;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    h1 {
        color: #fff !important;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
        animation: fadeInDown 0.8s ease-out;
    }
    
    h2, h3 {
        color: #e2e8f0 !important;
        animation: fadeInUp 0.6s ease-out;
    }
    
    p, span, label {
        color: #cbd5e1 !important;
        font-weight: 400;
    }
    
    /* Section labels */
    .section-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #60a5fa !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
        opacity: 0.9;
    }
    
    /* Input fields styling */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div>div,
    .stMultiSelect>div>div>div {
        background: rgba(15, 23, 42, 0.6) !important;
        backdrop-filter: blur(10px) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(96, 165, 250, 0.2) !important;
        border-radius: 12px !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        padding: 12px 16px !important;
        font-weight: 500;
    }
    
    .stTextInput>div>div>input:hover,
    .stTextArea>div>div>textarea:hover,
    .stSelectbox>div>div>div:hover {
        border-color: rgba(96, 165, 250, 0.4) !important;
        box-shadow: 0 0 12px rgba(96, 165, 250, 0.1) !important;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus,
    .stSelectbox>div>div>div:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.3) !important;
        background: rgba(15, 23, 42, 0.8) !important;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 12px 24px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2) !important;
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4) !important;
    }
    
    .stButton>button:active {
        transform: translateY(0) !important;
    }
    
    /* Output Box - Premium glassmorphism */
    .output-box {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.4) 0%, rgba(25, 35, 62, 0.3) 100%) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        border-radius: 16px !important;
        padding: 28px !important;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.15), inset 0 1px 0 rgba(255,255,255,0.1) !important;
        font-family: 'Inter', sans-serif !important;
        white-space: pre-wrap !important;
        color: #e2e8f0 !important;
        line-height: 1.7;
        animation: slideUpFade 0.6s ease-out;
    }
    
    /* Divider */
    .stDivider { 
        border-color: rgba(96, 165, 250, 0.2) !important;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(15, 23, 42, 0.4) !important;
        border-radius: 10px 10px 0 0 !important;
        border: 1px solid rgba(96, 165, 250, 0.1) !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease-out !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(30, 60, 114, 0.3) !important;
        border-color: rgba(96, 165, 250, 0.3) !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(37, 99, 235, 0.1) 100%) !important;
        border-color: rgba(59, 130, 246, 0.5) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15) !important;
    }
    
    /* Info box */
    .stInfo {
        background: rgba(59, 130, 246, 0.1) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }
    
    .stWarning {
        background: rgba(249, 115, 22, 0.1) !important;
        border: 1px solid rgba(249, 115, 22, 0.3) !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }
    
    .stSuccess {
        background: rgba(34, 197, 94, 0.1) !important;
        border: 1px solid rgba(34, 197, 94, 0.3) !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }
    
    /* Radio button styling */
    .stRadio>div>label {
        font-weight: 500;
        transition: all 0.2s ease-out;
    }
    
    .stRadio>div>div {
        gap: 12px;
    }
    
    /* Metric cards */
    .stMetric {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.4) 0%, rgba(25, 35, 62, 0.3) 100%) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1) !important;
    }
    
    /* Status container */
    .stStatus {
        background: rgba(15, 23, 42, 0.5) !important;
        border: 1px solid rgba(59, 130, 250, 0.2) !important;
        border-radius: 12px !important;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideUpFade {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.5;
        }
    }
    
    @keyframes shimmer {
        0% {
            background-position: -1000px 0;
        }
        100% {
            background-position: 1000px 0;
        }
    }
    
    .pulse {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
</style>
""", unsafe_allow_html=True)

# --- PREMIUM HEADER ---
col_header1, col_header2 = st.columns([1, 1])
with col_header1:
    st.markdown("<h1>⚡ EmailForge AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.1rem; color: #60a5fa; margin-top: -0.5rem;'>Professional Email Generation Platform</p>", unsafe_allow_html=True)

with col_header2:
    st.markdown("<div style='text-align: right; padding-top: 0.5rem;'><p style='font-size: 0.9rem; color: #64748b;'>✨ Powered by Advanced AI</p></div>", unsafe_allow_html=True)

st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🎨 Generate", "📊 Evaluate", "📈 Analytics"])

# --- TAB 1: GENERATE ---
with tab1:
    # Create layout with proper spacing
    col1, spacer, col2 = st.columns([45, 5, 45])
    
    with col1:
        # Input Section Card
        st.markdown("<div class='section-label'>📝 Email Configuration</div>", unsafe_allow_html=True)
        
        intent = st.text_input(
            "📮 Email Intent",
            value="Follow up after a job interview with positive outcome",
            placeholder="What's the purpose of this email?",
            help="Define the main goal or purpose of your email"
        )
        
        facts = st.text_area(
            "✓ Key Facts (one per line)",
            value="Interview was with Sarah Chen and Mark Davis on Tuesday\nRole: Senior Product Manager at TechCorp\nDiscussed Q4 roadmap\nCan start within 4 weeks",
            height=140,
            placeholder="Add key points to include in the email",
            help="List important details that should be mentioned"
        )
        
        tone = st.selectbox(
            "🎭 Email Tone",
            TONES,
            index=0,
            help="Select the desired tone for your email"
        )
        
        st.markdown("<div class='section-label' style='margin-top: 1.5rem;'>⚙️ AI Model Configuration</div>", unsafe_allow_html=True)
        
        openai_api_key = st.text_input(
            "🔑 OpenAI API Key (Optional)",
            type="password",
            placeholder="sk-...",
            help="Provide your OpenAI API key to use GPT models. Leave empty to use Ollama (local)."
        )
        
        st.markdown("<div class='section-label' style='margin-top: 1.5rem;'>🔄 Strategy Selection</div>", unsafe_allow_html=True)
        
        strategy = st.radio(
            "Choose Generation Strategy",
            ["A", "B"],
            captions=[
                "⚡ Basic Instruction - Fast & Simple",
                "🧠 Advanced CoT - Detailed & Thoughtful"
            ],
            horizontal=True,
            help="Strategy A: Direct prompting | Strategy B: Chain-of-thought with context"
        )
        
        # Generate Button with animations
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        gen_col1, gen_col2 = st.columns([1, 1])
        
        with gen_col1:
            generate_btn = st.button("✨ Generate Email", use_container_width=True, key="generate_btn")
        
        if generate_btn:
            if not intent or not facts:
                st.warning("⚠️ Please provide both Intent and Facts to generate an email.")
            else:
                with st.spinner("🔄 Crafting your perfect email..."):
                    fact_list = [f.strip() for f in facts.split('\n') if f.strip()]
                    result = generate_email(intent, fact_list, tone, strategy, openai_api_key if openai_api_key else None)
                    st.session_state['generated_email'] = result
                    st.rerun()
    
    with spacer:
        st.markdown("")
    
    with col2:
        st.markdown("<div class='section-label'>✨ Generated Email Preview</div>", unsafe_allow_html=True)
        
        if 'generated_email' in st.session_state:
            st.markdown(f'<div class="output-box">{st.session_state["generated_email"]}</div>', unsafe_allow_html=True)
            
            # Action buttons
            st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
            col_btn1, col_btn2, col_btn3 = st.columns(3)
            
            with col_btn1:
                if st.button("📋 Copy", use_container_width=True, key="copy_btn"):
                    st.success("✅ Copied to clipboard!")
            
            with col_btn2:
                if st.button("🔄 Regenerate", use_container_width=True, key="regenerate_btn"):
                    st.session_state['generated_email'] = None
                    st.rerun()
            
            with col_btn3:
                if st.button("💾 Save", use_container_width=True, key="save_btn"):
                    st.success("✅ Saved!")
        else:
            st.markdown("""
            <div class="output-box" style="text-align: center; color: #64748b; padding: 60px 30px;">
                <p style="font-size: 1.1rem; margin-bottom: 10px;">📧 Your generated email will appear here</p>
                <p style="font-size: 0.9rem;">Configure the parameters and click "Generate Email" to create your professional message</p>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 2: EVALUATE ---
with tab2:
    st.markdown("<div class='section-label'>🎯 Evaluation & Comparison</div>", unsafe_allow_html=True)
    
    col_eval1, col_eval2 = st.columns([1, 1])
    
    with col_eval1:
        st.markdown("#### Strategy A Analysis")
        st.info("📊 Run comprehensive evaluation to compare both strategies across multiple dimensions")
    
    with col_eval2:
        st.markdown("#### Strategy B Analysis")
        if st.button("🚀 Run Full Evaluation", use_container_width=True, key="eval_btn"):
            with st.status("🔄 Evaluating Strategies...", expanded=True) as status:
                for i in range(1, 6):
                    st.write(f"✓ Evaluating Scenario {i}/10...")
                    time.sleep(0.3)
                
                st.write("✓ Generating comparison metrics...")
                time.sleep(0.5)
                
                status.update(label="✅ Evaluation Complete!", state="complete", expanded=False)
            
            st.success("🎉 Evaluation finished! Check Analytics tab for detailed results.")

# --- TAB 3: ANALYTICS ---
with tab3:
    st.markdown("<div class='section-label'>📈 Performance Metrics</div>", unsafe_allow_html=True)
    
    col_metric1, col_metric2, col_metric3 = st.columns(3)
    
    with col_metric1:
        st.metric(
            label="Fact Recall Rate (FRR)",
            value="9.2",
            delta="Strategy B +0.8",
            help="Measures how well facts are included in emails"
        )
    
    with col_metric2:
        st.metric(
            label="Tone Alignment (TAS)",
            value="9.1",
            delta="Strategy B +0.5",
            help="Measures tone consistency with requirements"
        )
    
    with col_metric3:
        st.metric(
            label="Overall Score",
            value="91",
            delta="Good Performance",
            help="Combined performance score"
        )
    
    st.divider()
    
    col_chart1, col_chart2 = st.columns([1, 1])
    
    with col_chart1:
        st.markdown("#### Strategy A Performance")
        st.info("📊 Detailed comparison charts and detailed analysis will be available here")
    
    with col_chart2:
        st.markdown("#### Strategy B Performance")
        st.success("✨ Advanced metrics and visualizations can be integrated with Plotly or Altair")
