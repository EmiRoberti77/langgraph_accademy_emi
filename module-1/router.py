import os
import json
from pprint import pprint
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from IPython.display import Image, display


def multiply(x:int, y:int) -> int:
    """
        Mulitply x and y.
        Args:
            x: first int
            y: second int
    """
    return x * y

def book_holiday(location:str) -> str:
    """
        book_holiday location to book a holiday.
        Args:
            location: destination of travel str
    """
    return f"{location} has been booked for Jan 2025"

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)
llm_with_tools = llm.bind_tools([multiply, book_holiday])

def tool_calling_llm(state:MessagesState):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}

builder = StateGraph(MessagesState)
builder.add_node('tool_calling_llm', tool_calling_llm)
builder.add_node('tools',ToolNode([multiply, book_holiday]))
builder.add_edge(START, 'tool_calling_llm')
builder.add_conditional_edges('tool_calling_llm', tools_condition)
builder.add_edge('tools', END)
graph = builder.compile()

messages = [HumanMessage(content="book me a holiday to Rome")]
messages = graph.invoke({"messages":messages})
for m in messages['messages']:
    m.pretty_print()
