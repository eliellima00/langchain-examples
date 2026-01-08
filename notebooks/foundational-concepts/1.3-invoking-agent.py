from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
from langchain.messages import AIMessage, HumanMessage
from pprint import pprint

agent = create_agent(model='gpt-5-nano')

response = agent.invoke(
    {"messages": [HumanMessage(content="What's the capital of the Moon?"),
    AIMessage(content="The capital of the Moon is Luna City."),
    HumanMessage(content="Interesting, tell me more about Luna City")]},
)

pprint(response)