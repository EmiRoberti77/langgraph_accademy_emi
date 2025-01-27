import os
import operator
from dotenv import load_dotenv
from typing_extensions import Annotated, TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WikipediaLoader
from langchain_community.tools import TavilySearchResults
from langgraph.graph import StateGraph, START, END
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
taviliy_api_key = os.getenv('TAVILY_API_KEY')

class State(TypedDict):
    question:str
    answer:str
    context:Annotated[list, operator.add]

llm = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key)

def search_web(state:State):
    """ Retrieve docs from web search """
    tavily_search = TavilySearchResults(max_results=3)
    search_docs = tavily_search.invoke(state['question'])

     # Format
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document href="{doc["url"]}"/>\n{doc["content"]}\n</Document>'
            for doc in search_docs
        ]
    )

    return {"context": [formatted_search_docs]} 

def search_wikipidia(state:State):
    """ Retrive docs from Wikipidia """
    search_doc = WikipediaLoader(query=state["question"], load_max_docs=2).load()
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content}\n</Document>'
            for doc in search_docs
        ]
    )
    return {"context": [formatted_search_docs]} 

def generate_answer(state:State):
    """ Node to answer a question """
    context = state["context"]
    question = state["question"]
    answer_template:str = """Answer the question {question} using this context {context}"""
    answer_instructions = answer_template.format(question=question, context=context)
    answer = llm.invoke([SystemMessage(content=answer_instructions)]+[HumanMessage(content="answer the question")])
    return {"answer":answer}

builder = StateGraph(State)
builder.add_node("tavily", search_web)
builder.add_node("wiki", search_wikipidia)
builder.add_node("generate_answer", generate_answer)
builder.add_edge(START, "tavily")
builder.add_edge(START, "wiki")
builder.add_edge("tavily", "generate_answer")
builder.add_edge("wiki", "generate_answer")
builder.add_edge("generate_answer", END)
graph = builder.compile()
response = graph.invoke({"question":"How were Nvidia's Q2 2024 earnings"})
print(response["answer"])



