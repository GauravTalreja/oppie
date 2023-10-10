from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler        

# ideally we run in a separate script first but rn only one entrypoint python file
import os
from dotenv import load_dotenv

load_dotenv("../config/.env")

# Now you can access the environment variables using os.getenv or os.environ
OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL")
OLLAMA_PORT = os.getenv("OLLAMA_PORT")
print("arbitrary change3")
        
llm = Ollama(model="llama2", 
             base_url=f"{OLLAMA_HOST_URL}:{OLLAMA_PORT}",
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

llm("you're in a docker container. how do you feel? say hello to the world! say three sentences max.")
