from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pprint import pprint

load_dotenv()

model = init_chat_model(model='gpt-5-nano')

response = model.invoke("What's the capital of the Moon?")

print(response.content)
#pprint(response.response_metadata)
