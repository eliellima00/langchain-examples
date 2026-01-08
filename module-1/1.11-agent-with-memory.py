from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

inicial_chat = HumanMessage(content="Hello my name is Eliel and my favourite colour is green")
config = {"configurable": {"thread_id": "1"}}

question = HumanMessage(content="What's my favourite colour?")

agent = create_agent(
  model='gpt-5-nano',
  checkpointer=InMemorySaver()
)

response = agent.invoke(
  {"messages": [inicial_chat]},
  config,  
)

response2 = agent.invoke(
  {"messages": [question]},
  config,  
)

pprint(response2)