from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.crm_agent import crm_agent

from app.database.db import SessionLocal
from app.models.interaction_model import Interaction

from app.tools.log_tool import log_interaction
from app.tools.edit_tool import edit_interaction


router = APIRouter()


# REQUEST MODEL
class InteractionRequest(BaseModel):
    message: str


# UPDATE MODEL
class UpdateInteractionRequest(BaseModel):
    message: str


# FORM MODEL
class FormInteractionRequest(BaseModel):

    hcp_name: str
    hospital: str
    topic: str
    sentiment: str
    follow_up: str
    summary: str
    followup_recommendation: str


# CHAT INTERACTION
@router.post("/interaction/chat")
def chat_interaction(data: InteractionRequest):

    response = crm_agent.invoke({

        "user_input": data.message

    })

    return response


# FORM INTERACTION
@router.post("/interaction/form")
def create_form_interaction(
    data: FormInteractionRequest
):

    interaction_data = {

        "hcp_name": data.hcp_name,

        "hospital": data.hospital,

        "topic": data.topic,

        "sentiment": data.sentiment,

        "follow_up": data.follow_up,

        "summary": data.summary,

        "followup_recommendation":
            data.followup_recommendation

    }

    response = log_interaction(
        interaction_data
    )

    return response


# GET ALL INTERACTIONS
@router.get("/interactions")
def get_interactions():

    db = SessionLocal()

    try:

        interactions = db.query(
            Interaction
        ).all()

        result = []

        for interaction in interactions:

            result.append({

                "id": interaction.id,

                "hcp_name":
                    interaction.hcp_name,

                "hospital":
                    interaction.hospital,

                "topic":
                    interaction.topic,

                "sentiment":
                    interaction.sentiment,

                "follow_up":
                    interaction.follow_up,

                "summary":
                    interaction.summary,

                "followup_recommendation":
                    interaction.followup_recommendation

            })

        return result

    finally:

        db.close()


# EDIT INTERACTION
@router.put("/interaction/{interaction_id}")
def update_interaction(

    interaction_id: int,

    updates: UpdateInteractionRequest

):

    db = SessionLocal()

    try:

        interaction = db.query(
            Interaction
        ).filter(

            Interaction.id == interaction_id

        ).first()

        if not interaction:

            return {

                "status": "error",

                "message":
                    "Interaction not found"

            }

        existing_data = {

            "hcp_name":
                interaction.hcp_name,

            "hospital":
                interaction.hospital,

            "topic":
                interaction.topic,

            "sentiment":
                interaction.sentiment,

            "follow_up":
                interaction.follow_up,

            "summary":
                interaction.summary,

            "followup_recommendation":
                interaction.followup_recommendation

        }

        updated = edit_interaction(

            existing_data,

            {
                "message":
                    updates.message
            }

        )

        updated_data = updated[
            "updated_data"
        ]


        interaction.hcp_name = (
            updated_data.get(
                "hcp_name"
            )
        )

        interaction.hospital = (
            updated_data.get(
                "hospital"
            )
        )

        interaction.topic = (
            updated_data.get(
                "topic"
            )
        )

        interaction.sentiment = (
            updated_data.get(
                "sentiment"
            )
        )

        interaction.follow_up = (
            updated_data.get(
                "follow_up"
            )
        )

        interaction.summary = (
            updated_data.get(
                "summary"
            )
        )

        interaction.followup_recommendation = (
            updated_data.get(
                "followup_recommendation"
            )
        )

        db.commit()

        return {

            "status": "success",

            "message":
                "Interaction updated successfully",

            "updated_data":
                updated_data

        }

    finally:

        db.close()