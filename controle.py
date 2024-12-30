from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
chave_api = os.getenv('OPIA_API_KEY')