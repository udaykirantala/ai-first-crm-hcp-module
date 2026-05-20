from app.services.llm_service import ask_llm


def generate_followup(text: str):

    prompt = f"""
    You are a healthcare CRM assistant.

    Based on the interaction, suggest the next follow-up action.

    STRICT RULES:
    - Maximum 20 words
    - Only 1 sentence
    - Professional tone
    - Action-oriented
    - No headings
    - No bullet points

    Interaction:
    {text}
    """

    response = ask_llm(prompt)

    return response.strip()