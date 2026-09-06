import openai
from groq import Groq
import os

groqKey = os.getenv("GROQ_API_KEY")



client = Groq(api_key=groqKey)

def get_completion(prompt, model = "groq/compound"):
     messages = [
         {"role":"system", "content":"You are a math tutor"},
         {"role":"user", "content":prompt}
     ]

     response = client.chat.completions.create(
         model = model,
         messages = messages,
         temperature=0.9,
         top_p=0.8,
         max_tokens=512,
     )
     return response.choices[0].message.content

 # Here we are not having example for prompt which means
 # We are using the zero shot prompt to get output from model.

prompt = "explain trignometry"
response= get_completion(prompt)
print(response)

