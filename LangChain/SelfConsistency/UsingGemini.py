import os

from google import genai
from google.genai import types


def get_completion(prompt: str, model: str = "gemini-3.5-flash-lite") -> str:
    """Generate a response using the Gemini API."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set the GEMINI_API_KEY environment variable before running this script."
        )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a math tutor.",
            temperature=0.9,
            top_p=0.8,

        ),
    )
    return response.text


prompt = """
Let's consider which is heavier: 1000 feathers or a 30-pound weight.

I will analyse the question using a few different approaches.

1. First line of reasoning:
A single feather is very light. Therefore, 1000 feathers may still
be lighter than a 30-pound weight.

2. Second line of reasoning:
1000 is a large number. When the weight of all the feathers is added,
they might be heavier than a 30-pound weight.

3. Third line of reasoning:
The average weight of one feather is very small. Even 1000 feathers
would normally not add up to 30 pounds.

Compare the three approaches and identify the most logically
consistent answer.

Provide:
- The correct answer
- A brief justification
"""

response = get_completion(prompt)

print(response)

prompt = """
A farmer has 17 sheep. All but 9 run away.

How many sheep are left?

Consider the following approaches:

1. "All but 9 ran away" means 9 sheep did not run away.
Therefore, 9 sheep are left.

2. "All but 9" means 9 sheep stayed.
Therefore, 9 sheep are left.

3. Subtracting 9 from 17 gives 8.
Therefore, 8 sheep are left.

Compare the approaches and identify the most logically
consistent answer.

Provide:
- The correct answer
- A brief justification
"""

response = get_completion(prompt)

print(response)

prompt = """
I will solve the following problem using several approaches.

Problem:
There were 15 apples, and you took away 4 apples.
How many apples do you have?

Consider the following approaches:

1. Subtract 4 from 15:
15 - 4 = 11 apples.
This tells us how many apples remain in the original place.

2. You personally took away 4 apples.
Therefore, you now have those 4 apples.

3. The question asks how many apples "you have," not how many
apples are left.
Therefore, you have 4 apples.

4. Subtracting 4 from 15 gives 11, but this answers how many
apples remain, not how many you took.

Compare all the approaches and identify the most logically
consistent answer.

Provide:
- The correct answer
- A brief justification
"""

response = get_completion(prompt)

print(response)