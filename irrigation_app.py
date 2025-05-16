import streamlit as st

st.set_page_config(page_title="Irrigation Water Calculator", layout="centered")

st.title("🌾 Irrigation Water Requirement Calculator")
st.markdown("""
This tool helps estimate how much water you need to irrigate your field based on soil properties and current moisture.
""")

st.header("Step 1: Field Capacity (FC) Calculation")

with st.expander("🔍 What is Field Capacity?"):
    st.info("Field Capacity is the amount of water soil retains after excess water drains, expressed as a % of soil volume.")

col1, col2 = st.columns(2)

with col1:
    vw = st.number_input("🌊 Volume of water held after drainage (VW) [m³]", min_value=0.0, step=0.01)
with col2:
    vs = st.number_input("🪨 Total soil volume (VS) [m³]", min_value=0.01, step=0.01)

fc = None
if vs > 0:
    fc = (vw / vs) * 100
    st.success(f"📈 Field Capacity (FC): {fc:.2f}%")

st.divider()
st.header("Step 2: Irrigation Requirement")

with st.expander("🔍 Irrigation Formula"):
    st.code("I = (FC − θ) × BD × D", language="markdown")
    st.markdown("""
    - **I** = Required irrigation (cm)  
    - **FC** = Field capacity (%)  
    - **θ** = Current soil moisture (%)  
    - **BD** = Bulk density (g/cm³)  
    - **D** = Root zone depth (cm)
    """)

col3, col4 = st.columns(2)

with col3:
    theta = st.number_input("🌡️ Current Soil Moisture (θ) [%]", min_value=0.0, max_value=100.0, step=0.1)
    bd = st.number_input("🧱 Bulk Density (BD) [g/cm³]", min_value=0.0, step=0.1, value=1.3)
with col4:
    d = st.number_input("🌱 Root Zone Depth (D) [cm]", min_value=0.0, step=1.0, value=30.0)

if fc is not None:
    raw_irrigation = (fc - theta) * bd * d
    irrigation_cm = max(0, raw_irrigation)
    irrigation_mm = irrigation_cm * 10  # Optional conversion

    st.success(f"💧 Required Irrigation: {irrigation_cm:.2f} cm  (~{irrigation_mm:.1f} mm)")
    if irrigation_cm == 0:
        st.info("Soil moisture is already at or above Field Capacity. No irrigation needed.")

st.markdown("---")
st.caption("Developed by Prateek Majumder | © 2025")
