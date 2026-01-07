from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-5-nano')

response = model.invoke("Whats the capital of Rondônia?")

print(response.content)