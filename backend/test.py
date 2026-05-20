from app.agents.crm_agent import crm_agent

response = crm_agent.invoke({
    "user_input": """
    Met Dr. Sharma at Apollo Hospital.
    Discussed diabetes medicine.
    Positive response.
    Follow up next Monday.
    """
})

print(response)
# from app.tools.summary_tool import summarize_interaction

# text = """
# Met Dr. Sharma at Apollo Hospital.
# Discussed diabetes medicine.
# Positive response.
# Follow up next Monday.
# """

# response = summarize_interaction(text)

# print(response)

# from app.tools.followup_tool import generate_followup

# text = """
# Met Dr. Sharma at Apollo Hospital.
# Discussed diabetes medicine.
# Positive response.
# Follow up next Monday.
# """

# response = generate_followup(text)

# print(response)

# from app.tools.log_tool import log_interaction

# data = {
#     "hcp_name": "Dr. Sharma",
#     "hospital": "Apollo Hospital",
#     "topic": "Diabetes medicine",
#     "sentiment": "Positive",
#     "follow_up": "Next Monday"
# }

# response = log_interaction(data)

# print(response)

# from app.tools.edit_tool import edit_interaction

# existing_data = {
#     "hcp_name": "Dr. Sharma",
#     "hospital": "Apollo Hospital",
#     "topic": "Diabetes medicine",
#     "sentiment": "Positive",
#     "follow_up": "Monday"
# }

# updates = {
#     "follow_up": "Friday"
# }

# response = edit_interaction(existing_data, updates)

# print(response)