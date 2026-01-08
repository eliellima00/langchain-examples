from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain.tools import tool
load_dotenv()

@tool
def square_root(x: float) -> float:
  """Calculate the square of a number"""
  return x ** 0.5

agent = create_agent(
  model='gpt-5-nano',
  tools=[square_root],
  system_prompt="You are an arithmetic wizard. Use your tools to calculate the square root and square of any number."
)

question = HumanMessage(content="What is the square root of 467?")

response = agent.invoke(
  {"messages": [question]}
)

# Pega apenas a ultima mensagem retornada, ou seja, a responsa AI
print(response['messages'][-1].content)


