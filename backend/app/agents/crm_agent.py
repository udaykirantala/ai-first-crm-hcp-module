from langgraph.graph import StateGraph, END
from typing import TypedDict

from app.tools.extract_tool import extract_interaction
from app.tools.summary_tool import summarize_interaction
from app.tools.followup_tool import generate_followup
from app.tools.log_tool import log_interaction


# STATE
class CRMState(TypedDict):
    user_input: str
    extracted_data: dict
    summary: str
    followup: str
    logged_response: dict


# NODE 1 — EXTRACTION
def extraction_node(state: CRMState):

    extracted = extract_interaction(state["user_input"])

    return {
        "extracted_data": extracted
    }


# NODE 2 — SUMMARY
def summary_node(state: CRMState):

    summary = summarize_interaction(state["user_input"])

    return {
        "summary": summary
    }


# NODE 3 — FOLLOWUP
def followup_node(state: CRMState):

    followup = generate_followup(state["user_input"])

    return {
        "followup": followup
    }


# NODE 4 — LOG INTERACTION
def log_node(state: CRMState):

    interaction_data = {
        **state["extracted_data"],
        "summary": state["summary"],
        "followup_recommendation": state["followup"]
    }

    logged = log_interaction(interaction_data)

    return {
        "logged_response": logged
    }


# CREATE GRAPH
graph = StateGraph(CRMState)


# ADD NODES
graph.add_node("extract", extraction_node)
graph.add_node("summary", summary_node)
graph.add_node("followup", followup_node)
graph.add_node("log", log_node)


# ENTRY POINT
graph.set_entry_point("extract")


# FLOW
graph.add_edge("extract", "summary")
graph.add_edge("summary", "followup")
graph.add_edge("followup", "log")
graph.add_edge("log", END)


# COMPILE
crm_agent = graph.compile()