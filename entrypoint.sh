#!/bin/bash

# Wait for Service B to be up (you can use tools like `wait-for-it.sh` or similar)
# Example using a simple loop:
until nc -z ollama 11434; do
  echo "Waiting for Ollama..."
  sleep 1
done


docker exec ollama ollama pull llama2
echo "LLama2 pulled"

docker exec -d ollama ollama run llama2
sleep 5
echo "Running LLama2"

python hello.py
