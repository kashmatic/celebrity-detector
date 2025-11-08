import os
import requests

class QAEngine:
  def __init__(self):
    self.api_key = os.getenv("GROQ_API_KEY")
    self.api_url = "https://api.groq.com/openai/v1/chat/completions"
    self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"
  
  def ask_about(self, name, question):
    headers = {
      "Authorization": f"Bearer {self.api_key}",
      "Content-Type": "application/json",
    }

    aprompt = f"""You are an AI assistant.
You know a lot about celebrities.
You have to answer questions regarding {name} concisely and accurately

Question: {question}
"""


    payload = {
      "model": self.model,
      "messages": [{"role": "user", "content": aprompt}],
      "temperature": 0.5,
      "max_tokens": 512
    }

    response = requests.post(self.api_url, headers=headers, json=payload)
    print(response.text)

    if response.status_code==200:
      return response.json()['choices'][0]['message']['content']
    
    return "Sorry, unable to provide answer "
    
