import openai
from groq import Groq
import os
from langchain_core.prompts import PromptTemplate
from sympy.solvers.diophantine.diophantine import length

groqKey = os.getenv("GROQ_API_KEY")



client = Groq(api_key=groqKey)



def get_completion(prompt, model = "groq/compound"):
     messages = [
         {"role":"user", "content":prompt}
     ]

     response = client.chat.completions.create(
         model = model,
         messages = messages,
         temperature=0,
         max_tokens=512
     )
     return response.choices[0].message.content

template = "Please write a {length} review of the book {book_title}."
input_variables =["length", "book_title"]

prompt = PromptTemplate(
    input_variables = input_variables,
    template = template
)

formatted_prompt = prompt.format(length = "short",book_title = "House Of Dragon")
print("Formatted Prompt:")
print(formatted_prompt)

response = get_completion(formatted_prompt)
print("\n Response:")
print(response)



