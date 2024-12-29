from typing_extensions import TypedDict
import random
from typing import Literal
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    graph_state:str

def node1(state:State):
    print('node-1')
    return {"graph_state": state["graph_state"] + " I am"}


def node2(state:State):
    print('node-2')
    return {"graph_state": state["graph_state"] + " happy :)"}

def node3(state:State):
    print('node-3')
    return {"graph_state": state["graph_state"] + " sad :("}

def decide_mood(state:State) -> Literal["node2", "node3"]:
    user_input = state["graph_state"]
    if random.random() < 0.5:
        return 'node2'
    else:
        return 'node3'

builder = StateGraph(State)
builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)
builder.add_edge(START,'node1')
builder.add_conditional_edges('node1', decide_mood)
builder.add_edge('node2', END)
builder.add_edge('node3', END)
graph = builder.compile()
#display(Image(graph.get_graph().draw_mermaid_png()))
response = graph.invoke({"graph_state":"Hi this is Emi"})
print(response)