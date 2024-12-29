import os
import json
from pprint import pprint
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage


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
