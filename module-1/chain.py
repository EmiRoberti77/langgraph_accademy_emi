from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage

messages = [AIMessage(content="You said you are doing research", name="Model")]
messages.append(HumanMessage(content="yes thats right", name="Emi"))
messages.append(AIMessage(content="great, what would you like to learn about it", name="Model"))
messages.append(HumanMessage(content="I want to learn how AI works", name="Emi"))

for m in messages:
    m.pretty_print()