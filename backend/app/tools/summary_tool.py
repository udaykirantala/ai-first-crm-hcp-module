from app.services.llm_service import ask_llm


def summarize_interaction(text: str):

    prompt = f"""
    You are a healthcare CRM assistant.

    Generate a concise CRM summary.

    STRICT RULES:
    - Maximum 25 words
    - Only 1 sentence
    - No extra explanation
    - No headings
    - No formatting
    - No future assumptions
    - Keep professional tone

    Interaction:
    {text}
    """

    response = ask_llm(prompt)

    return response.strip()