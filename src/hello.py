from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler        
import os
from dotenv import load_dotenv
load_dotenv()
OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL")
OLLAMA_PORT = os.getenv("OLLAMA_PORT")
        
llm = Ollama(model="llama2", 
             base_url=f"http://{OLLAMA_HOST_URL}:{OLLAMA_PORT}",
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

llm("you're in a docker container. how do you feel? say hello to the world! say three sentences max.")
