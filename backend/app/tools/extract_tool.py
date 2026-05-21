import json
import re

from datetime import datetime

from app.services.llm_service import ask_llm


def extract_interaction(text: str):

    prompt = f"""
    You are a CRM assistant.

    Extract the following fields.

    Return ONLY valid JSON.

    STRICT RULES:

    - sentiment must ONLY be:
    positive, neutral, or negative

    -Keep relative dates exactly as written
    like today, tomorrow, next Monday, etc.
    Do not convert them into actual dates.

    Fields:
    - hcp_name
    - hospital
    - interaction_type
    - date
    - time
    - attendees
    - topic
    - materials_shared
    - samples_distributed
    - sentiment
    - outcomes
    - follow_up

    Interaction:
    {text}
    """

    response = ask_llm(prompt)

    # REMOVE MARKDOWN
    cleaned_response = re.sub(
        r"```json|```",
        "",
        response
    ).strip()


    # STRING → JSON
    parsed_response = json.loads(
        cleaned_response
    )


    # HANDLE TODAY DATE
    if parsed_response.get("date"):

        if (
            parsed_response["date"]
            .lower() == "today"
        ):

            parsed_response["date"] = (
                datetime.now()
                .strftime("%Y-%m-%d")
            )
    else:
        parsed_response["date"]=(
            datetime.now()
            .strftime("%Y-%m-%d")
        )


    # HANDLE CURRENT TIME
    if parsed_response.get("time"):

        if (
            parsed_response["time"]
            .lower() == "now"
        ):

            parsed_response["time"] = (
                datetime.now()
                .strftime("%I:%M %p")
            )
    else:
        parsed_response["time"] = (
            datetime.now()
            .strftime("%I:%M %p")
        )


    return parsed_response