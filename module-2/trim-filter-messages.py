from pprint import pprint
from langchain_openai import ChatOpenAI
from langchain_core.messages import RemoveMessage
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
import os
import json
load_dotenv()
# get openai api_key
api_key:str = os.getenv("OPENAI_API_KEY")
#create message[] 
messages = [AIMessage(content="so you like cars")]
messages.append(HumanMessage(content="my favourite cars are ferraris"))
# create instance of the llm model
model = ChatOpenAI(model="gpt-4", openai_api_key=api_key)
def filterMessages(state: MessagesState):
    # Access messages directly from the state
    filtered_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-1]]
    return {"messages": filtered_messages}
# invole model method to use the in the graph
def invokeModel(state:MessagesState):
    response = model.invoke(state["messages"])
    return {"messages":state["messages"] + [response]}
#build the graph
builder = StateGraph(MessagesState)
builder.add_node("filtered_messages", filterMessages)
builder.add_node("invoke_model", invokeModel)
builder.add_edge(START, "filtered_messages")
builder.add_edge("filtered_messages", "invoke_model")
builder.add_edge("invoke_model", END)
graph = builder.compile()
output = graph.invoke({"messages": messages})
for message in output["messages"]:
    print(f"Role: {message.type}")
    print(f"Content: {message.content}\n")