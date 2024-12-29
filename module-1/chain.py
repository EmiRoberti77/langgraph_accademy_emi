import os
import json
from pprint import pprint
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from IPython.display import Image, display

def multiply(x:int, y:int) -> int:
    """
        Mulitply x and y.
        Args:
            x: first int
            y: second int
    """
    return x * y

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

messages = [AIMessage(content="You said you are doing research", name="Model")]
messages.append(HumanMessage(content="yes thats right", name="Emi"))
messages.append(AIMessage(content="great, what would you like to learn about it", name="Model"))
messages.append(HumanMessage(content="I want to learn how AI works", name="Emi"))

for m in messages:
    m.pretty_print()

llm = ChatOpenAI(model='gpt-4o', openai_api_key=api_key)
result = llm.invoke(messages)
print(type(result))
result.pretty_print()

llm_with_tools = llm.bind_tools([multiply])
tool_call = llm_with_tools.invoke([HumanMessage(content="what is 2 * 3?", name="emi")])
tool_call.pretty_print()
print(tool_call)

