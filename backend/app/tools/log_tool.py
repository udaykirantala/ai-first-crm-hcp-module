from app.database.db import SessionLocal
from app.models.interaction_model import Interaction


def log_interaction(interaction_data: dict):

    db = SessionLocal()

    try:

        # CONVERT COMPLEX TYPES

        for key, value in interaction_data.items():

            # LIST → STRING
            if isinstance(value, list):

                interaction_data[key] = ", ".join(
                    map(str, value)
                )

            # DICT → STRING
            elif isinstance(value, dict):

                interaction_data[key] = str(value)


        # CREATE NEW INTERACTION
        new_interaction = Interaction(

            hcp_name=interaction_data.get(
                "hcp_name"
            ),

            hospital=interaction_data.get(
                "hospital"
            ),

            interaction_type=interaction_data.get(
                "interaction_type"
            ),

            date=interaction_data.get(
                "date"
            ),

            time=interaction_data.get(
                "time"
            ),

            attendees=interaction_data.get(
                "attendees"
            ),

            topic=interaction_data.get(
                "topic"
            ),

            materials_shared=interaction_data.get(
                "materials_shared"
            ),

            samples_distributed=interaction_data.get(
                "samples_distributed"
            ),

            sentiment=interaction_data.get(
                "sentiment"
            ),

            outcomes=interaction_data.get(
                "outcomes"
            ),

            follow_up=interaction_data.get(
                "follow_up"
            ),

            summary=interaction_data.get(
                "summary"
            ),

            followup_recommendation=interaction_data.get(
                "followup_recommendation"
            )

        )

        db.add(new_interaction)

        db.commit()

        db.refresh(new_interaction)

        return {

            "status": "success",

            "message":
                "Interaction logged successfully",

            "interaction_id":
                new_interaction.id

        }

    finally:

        db.close()