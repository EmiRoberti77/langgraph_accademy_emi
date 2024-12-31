from pprint import pprint
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
import os
import json
messages = [AIMessage(content="so you like cars")]
messages.append(HumanMessage(content="my favourite cars are ferraris"))
load_dotenv()
api_key:str = os.getenv("OPENAI_API_KEY")

for m in messages:
    m.pretty_print()

model = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)
response = model.invoke(messages)

print(response.content)