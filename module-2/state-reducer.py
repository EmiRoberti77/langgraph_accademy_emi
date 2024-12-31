import random
from operator import add
from pprint import pprint
from typing import Literal, Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from dataclasses import dataclass

def reduce_list(left: list | None, right: list | None)->list:
    """Safely combine two lists, handling cases where either or both inputs might be None.

    Args:
        left (list | None): The first list to combine, or None.
        right (list | None): The second list to combine, or None.

    Returns:
        list: A new list containing all elements from both input lists.
               If an input is None, it's treated as an empty list.
    """
    if not left:
        left = []
    if not right:
        right = []
    return left + right

@dataclass
class StateClass:
    messages:Annotated[list[str], reduce_list]

def node1(state:StateClass):
    return {"messages": state.messages + ["node1"]}

def node2(state:StateClass):
    return {"messages": state.messages + ["node2"]}

def node3(state:StateClass):
    return {"messages": state.messages + ["node3"]}

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
graph.invoke(StateClass(messages=["start"]))



