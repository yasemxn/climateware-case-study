from typing import List, Dict
import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

# API and Azure settings
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_API_VERSION")

DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

# Ask GPT Function
def ask_gpt(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            engine=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant specializing in carbon emission reduction strategies."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error calling GPT: {e}"

# Reasoning prompt Function for multi recommendations
def build_reasoning_prompt(recommendations: List[Dict]) -> str:
    return f"""
You are a sustainability advisor for a carbon reduction company. You are given a list of emission reduction recommendations.

Evaluate each recommendation based on these criteria:
- **Impact Level:** HIGH (>20%), MEDIUM (5–20%), LOW (<5%)
- **Feasibility Score:** HIGH (≥8), MEDIUM (5–8), LOW (<5)
- **Cost** and **Technology Status**

Your goal:
- Identify which recommendations are most effective
- Prioritize them
- Justify your reasoning based on the data

Return your response as a **ranked list**, with a clear explanation for each.

Here is the data:
{json.dumps(recommendations, indent=2)}
"""

# Reasonming prompt function for single recommendation

def build_single_reasoning_prompt(activity_name: str, recommendation: Dict) -> str:
    return f"""
You are a sustainability advisor evaluating a recommendation for the activity '{activity_name}'.

Assess this recommendation using:
- **Impact level**
- **Feasibility score**
- **Cost**
- **Technology readiness**

Explain whether this recommendation is strong or weak, and why.

Recommendation:
{json.dumps(recommendation, indent=2)}
"""