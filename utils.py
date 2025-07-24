import google.generativeai as genai
import os

# Load Gemini with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_low_level_specs_gemini(requirement_text):
    prompt = f"""
You are a software architect AI.

Given the following high-level business requirement, break it down into:
1. Modules
2. Suggested database schema (in JSON format)
3. Pseudocode for major actions

High-Level Requirement:
\"\"\"
{requirement_text}
\"\"\"

Output result in JSON format with keys: "modules", "database_schema", "pseudo_code"
    """

    response = model.generate_content(prompt)
    return response.text
