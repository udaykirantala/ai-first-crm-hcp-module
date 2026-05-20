def edit_interaction(existing_data: dict, updates: dict):

    updated_data = existing_data.copy()

    updated_data.update(updates)

    return {
        "status": "success",
        "message": "Interaction updated successfully",
        "updated_data": updated_data
    }