from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler        
import os
from dotenv import load_dotenv
load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST")
OLLAMA_PORT = os.getenv("OLLAMA_PORT")
OLLAMA_PROTOCOL = os.getenv("OLLAMA_PROTOCOL")

llm = Ollama(model="llama2", 
             base_url=f"{OLLAMA_PROTOCOL}://{OLLAMA_HOST}:{OLLAMA_PORT}",
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

llm("you're in a docker container. how do you feel? say hello to the world! say three sentences max.")
