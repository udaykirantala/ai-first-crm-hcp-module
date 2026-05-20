from app.database.db import SessionLocal
from app.models.interaction_model import Interaction


def log_interaction(interaction_data: dict):

    db = SessionLocal()

    try:

        new_interaction = Interaction(

            hcp_name=interaction_data.get("hcp_name"),

            hospital=interaction_data.get("hospital"),

            topic=interaction_data.get("topic"),

            sentiment=interaction_data.get("sentiment"),

            follow_up=interaction_data.get("follow_up"),

            summary=interaction_data.get("summary"),

            followup_recommendation=interaction_data.get(
                "followup_recommendation"
            )
        )

        db.add(new_interaction)

        db.commit()

        db.refresh(new_interaction)

        return {
            "status": "success",
            "message": "Interaction logged successfully",
            "interaction_id": new_interaction.id
        }

    finally:
        db.close()