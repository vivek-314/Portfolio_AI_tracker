import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_portfolio(stocks):

    prompt = f"""
You are a professional investment advisor.

Analyze this portfolio:

{stocks}

Format your answer exactly like this:

## Portfolio Score
<score>

## Risk Level
<risk>

## Diversification
<diversification>

## Strengths
• Point 1
• Point 2
• Point 3

## Weaknesses
• Point 1
• Point 2
• Point 3

## Recommendations
• Point 1
• Point 2
• Point 3

Keep it under 200 words.
"""

    response = model.generate_content(prompt)

    return response.text