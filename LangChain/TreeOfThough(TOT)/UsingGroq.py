import openai
from groq import Groq
import os

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

prompt = """
Solve the following problem:

A farmer has 100 meters of fencing and wants to enclose the
maximum possible area for a rectangular field.

Let's think about this in a few different ways:

1. If the field is a square, each side would be:

   100 / 4 = 25 meters

   The area would be:

   25 × 25 = 625 square meters

2. What if the field is not a square?

   Let's consider a rectangle with a 4:1 ratio.

   The dimensions would be 40 meters and 10 meters.

   The perimeter would be:

   40 + 40 + 10 + 10 = 100 meters

   The area would be:

   40 × 10 = 400 square meters

3. Consider whether any other rectangular dimensions could
   produce a larger area than the square.

Compare the different approaches, reason through the problem,
and provide:

- The best dimensions
- The maximum possible area
- A brief justification
"""

response = get_completion(prompt)

print("AI Response:")
print(response)


