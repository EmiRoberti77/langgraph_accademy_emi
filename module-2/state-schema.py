import random
from pprint import pprint
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from dataclasses import dataclass

@dataclass
class StateClass:
    name:str
    mood:Literal["happy", "sad"]

def node1(state:StateClass):
    return {"name":state.name + " is .."}

def node2(state:StateClass):
    return {"mood":"happy"}

def node3(state:StateClass):
    print("__Node 3__")
    return {"mood":"sad"}

def decide_mood(state:StateClass): 
    if random.random() < 0.5:
        return "node2"
    return "node3"

#build the graph
builder = StateGraph(StateClass)
#build the nodes
builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)
#add logic
builder.add_edge(START, "node1")
builder.add_conditional_edges("node1",decide_mood)
builder.add_edge("node2", END)
builder.add_edge("node3", END)

graph = builder.compile()
graph.invoke(StateClass(name="emi", mood="happy"))



