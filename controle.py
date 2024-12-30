from dotenv import load_dotenv
import os
from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()
chave_api = os.getenv('OPIA_API_KEY')

mensagens = [
    SystemMessage('Traduza o texto a seguir para inglês'), 
    HumanMessage('Olá, tudo bem?')
]

modelo = ChatOpenAI(model='gpt-4o-mini')

resposta = modelo.invoke(mensagens)
print(resposta)