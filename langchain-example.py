import os

from langchain_openai import ChatOpenAI

# Set up OpenAI API key
openai_api_key = '<YOUR-API-KEY>'

llm = ChatOpenAI(api_key=openai_api_key)

response = llm.invoke("Explain the concept of quantum computing in simple terms.")

print(response)


