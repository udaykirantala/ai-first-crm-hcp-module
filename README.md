# ai-first-crm-hcp-module
This project is an AI-powered Healthcare CRM Interaction Logger.
The main idea of this project is to reduce manual CRM form filling using AI.

Normally, medical representatives manually enter doctor interaction details into CRM systems. That process takes time and sometimes data can be missed. So in this project, we created an AI assistant that can understand natural language and automatically fill CRM interaction details.

Project Flow

First, the user enters interaction details in chat format.

Example:

Met Dr. Sharma at Apollo Hospital today regarding diabetes medicine. Shared brochures and scheduled follow-up next Monday.

Instead of manually filling every field, the user just types the interaction naturally.

Frontend Working

On the frontend side, we used React.js.

The application has mainly two sections:

1. Interaction Form

The left side contains the CRM interaction form.

This form displays:

Doctor name
Hospital
Date
Time
Topic
Sentiment
Follow-up
Materials shared
Summary

The important point is:
the user does not manually fill this form.

The form is automatically updated using AI response data from the backend.

2. AI Chat Interface

The right side contains the AI chatbot interface.

The user types interaction details here.

When the user clicks:

AI Log

the frontend sends the message to the backend using Axios API calls.

Redux Usage

We used Redux Toolkit for state management.

Redux stores:

extracted interaction data
current interaction ID
interaction history

This helps us share data between:

Chat component
Interaction form component

without passing props everywhere.

Backend Working

On the backend side, we used FastAPI.

FastAPI handles:

API creation
AI workflow
database operations
interaction updates
Main Backend Flow

When the frontend sends interaction text:

POST /interaction/chat

the backend sends the message to the CRM AI agent.

The CRM agent controls the complete workflow.

AI Extraction Process

The extraction tool sends prompts to the AI model.

The AI extracts structured fields like:

HCP Name
Hospital
Topic
Sentiment
Follow-up
Date
Time

Example extracted response:

{
  "hcp_name": "Dr. Sharma",
  "hospital": "Apollo Hospital",
  "sentiment": "Positive"
}
Summary Generation

After extraction, another AI prompt generates a short CRM summary.

Example:

Discussed diabetes medicine with Dr. Sharma and scheduled follow-up.
Follow-Up Recommendation

Then the AI also generates the next action recommendation.

Example:

Send efficacy reports before next Monday meeting.
Database Integration

After processing, the interaction data is stored in MySQL database using SQLAlchemy ORM.

We created an Interaction model containing:

HCP Name
Hospital
Topic
Sentiment
Follow-up
Summary
Materials shared
Outcomes
Date and Time
Conversational Editing Feature

One important feature in this project is conversational editing.

Example:

change the name to Dr. Sunny

Instead of creating a new interaction, the system updates only that field while keeping old data unchanged.

For this:

frontend stores interaction ID
PUT API updates existing interaction
backend merges old and new data

This creates a real AI CRM experience.

Challenges Solved

We handled several real-world issues:

Date Handling

If the user says:

today

the backend converts it into the current actual date.

Time Handling

If the user does not provide time, the system automatically uses current system time.

Sentiment Standardization

Sometimes AI returns:

Concerned
Interested
Excited

We standardized them into:

Positive
Neutral
Negative

for proper frontend display.

APIs Used

Main APIs:

Create Interaction
POST /interaction/chat
Update Interaction
PUT /interaction/{interaction_id}
Get All Interactions
GET /interactions
Components Used
Frontend Components
Dashboard.jsx
InteractionForm.jsx
ChatInterface.jsx
Redux
interactionSlice.js
Backend Files
main.py
interaction_routes.py
crm_agent.py
extract_tool.py
summary_tool.py
followup_tool.py
log_tool.py
edit_tool.py
interaction_model.py