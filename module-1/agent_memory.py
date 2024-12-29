from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langgraph.checkpoint.memory import MemorySaver
from IPython.display import Image, display
from dotenv import load_dotenv
from pprint import pprint
import os
load_dotenv()
api_key:str = os.getenv("OPENAI_API_KEY")

def multiply(x:int, y:int)->int:
    """
        Mulitply x and y
        Args:
            x: first param int
            y: first param int
    """
    return x * y

def add(x:int, y:int)->int:
    """
        add x and y
        Args:
            x: first param int
            y: first param int
    """
    return x + y

def divide(x:int, y:int)->int:
    """
        divide x and y
        Args:
            x: first param int
            y: first param int
    """
    return x / y

tools = [add, multiply, divide]
llm = ChatOpenAI(model="gpt-4o",openai_api_key=api_key)
# for this example set the LLM tools calls to be sequentials as there are Math operations so
#  they are done in sequence.  By default parallel is on for efficiency
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)
sys_msg:SystemMessage = SystemMessage(content="you are a assistant to perform Math operations based on inputs")

def assistant(state:MessagesState):
    return {"messages":[llm_with_tools.invoke([sys_msg] + state["messages"])]}

#define the nodes
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
#define the edge
builder.add_edge(START, 'assistant')
builder.add_conditional_edges('assistant', tools_condition)
builder.add_edge("tools", "assistant")
checkpointer = MemorySaver()
react_graph = builder.compile(checkpointer=checkpointer)
config = {"configurable":{"thread_id":"1"}}


messages = HumanMessage(content="Add 3 by 4 then mulitply the output by 10 and divide the output by 2", name="Emi")
messages = react_graph.invoke({"messages":messages}, config)
for m in messages["messages"]:
    m.pretty_print()

messages = HumanMessage(content="Now multiple that by 3")
messages = react_graph.invoke({"messages":messages}, config)
for m in messages["messages"]:
    m.pretty_print()
