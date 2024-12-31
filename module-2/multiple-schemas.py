from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class InputState(TypedDict):
    question:str

class OutputState(TypedDict):
    question:str

class OverallState(TypedDict):
    question:str
    answer:str
    notes:str

def thinking_node(state:InputState):
    return {"answer":"bye","notes":"his name is Emi"}

def answer_node(state:OverallState):
    return {"answer":state["notes"] +" "+ state["answer"]}


builder = StateGraph(OverallState)
builder.add_node("thinking_node", thinking_node)
builder.add_node("answer_node", answer_node)
builder.add_edge(START, "thinking_node")
builder.add_edge("thinking_node", "answer_node")
builder.add_edge("answer_node", END)
graph = builder.compile()
startState:OverallState = {"input":"what is your name","answer":"", "notes":""}
messages = graph.invoke(startState)
print(messages)
