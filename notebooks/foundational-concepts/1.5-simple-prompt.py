from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

agent = create_agent(model='gpt-5-nano')

question = HumanMessage(content="What's the capital of the moon?")

response = agent.invoke(
  {"messages": [question]}
)

print(response['messages'][1].content)


