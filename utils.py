import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your API key securely
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment. Please add it to your .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

#  Use Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash")

def get_low_level_specs_gemini(requirement_text):
    prompt = f"""
You are a software architect AI.

Given this high-level business requirement, break it down into:
1. Modules
2. Database schema (as JSON)
3. Pseudocode

Output result as JSON with keys: "modules", "database_schema", "pseudo_code".

High-Level Requirement:
\"\"\"
{requirement_text}
\"\"\"
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"
