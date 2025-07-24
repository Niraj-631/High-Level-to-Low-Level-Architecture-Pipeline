import streamlit as st
import json
from utils import get_low_level_specs_gemini


st.set_page_config(page_title="Gemini HL to LL Tool", layout="wide")

st.title("High-Level → Low-Level Architecture (Gemini)")
st.markdown("Uses Google Gemini to convert business requirements into modules, schemas, and pseudocode.")

requirement_text = st.text_area("Enter your business requirement:", height=200)

if st.button("🔍 Generate Specification"):
    if not requirement_text.strip():
        st.warning("Please enter a requirement.")
    else:
        with st.spinner("Gemini is thinking..."):
            output = get_low_level_specs_gemini(requirement_text)

        try:
            parsed = json.loads(output)
            st.success("Gemini generated a structured output!")

            st.subheader("Modules")
            st.json(parsed.get("modules", {}))

            st.subheader("🗄️ Database Schema")
            st.json(parsed.get("database_schema", {}))

            st.subheader("Pseudocode")
            st.json(parsed.get("pseudo_code", {}))

        except Exception as e:
            st.error("Output could not be parsed. Showing raw response:")
            st.code(output)
