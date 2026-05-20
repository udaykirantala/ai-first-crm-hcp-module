import json
import re

from app.services.llm_service import ask_llm


def extract_interaction(text: str):

    prompt = f"""
    You are a CRM assistant.

    Extract the following fields.

    Return ONLY valid JSON.

    Fields:
    - hcp_name
    - hospital
    - topic
    - sentiment
    - follow_up

    Interaction:
    {text}
    """

    response = ask_llm(prompt)

    # Remove markdown formatting
    cleaned_response = re.sub(r"```json|```", "", response).strip()

    # Convert string to JSON object
    parsed_response = json.loads(cleaned_response)

    return parsed_response