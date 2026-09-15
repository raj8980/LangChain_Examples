import openai
from groq import Groq
import os

groqKey = os.getenv("GROQ_API_KEY")



client = Groq(api_key=groqKey)

def get_completion(prompt, model = "groq/compound"):
     messages = [
         {"role":"system", "content":"You are a master to answer or find out and question details."},
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


  # Few shot prompting
prompt = """
 Feedback: "I loved the quick service and friendly staff."
 Classification: Great we are delighed to have a Positive sentiment
 Score: 0.9

 Feedback: "The product did not meet any expectations."
 Classification: Oops, we are afraid its a Negative sentiment
 Score: 0.2

 Feedback: "I am not sure if this is the right product for me."
 Classification: We will try to improve and satisfy you next time as its a Neutral sentiment.
 Score: 0.5

 Feedback: "Your customer support was helpful, very satified."
 Classification:
 Score:
 """
print(get_completion(prompt))

prompt = """
Q: What is the capital of Italy?
A: "Imperium Romanum in aeternum stabit.", Rome

Q: What is the capital of France?
A: "L'Empire romain devrait tenir pour l'éternité.", Paris

Q: What is the capital of Japan?
A: "日本は永遠に生き続けるべきです。", Tokyo

Q: What is the capital of Germany?
A: "Das Deutsche Reich sollte für immer bestehen.", Berlin

Q: What is the capital of Brazil?
A: "O Império Brasileiro deve durar para sempre.", Brasília

Q: What is the capital of USA?
A:
"""

print(get_completion(prompt))
