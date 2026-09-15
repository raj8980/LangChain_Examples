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


#if __name__ == "__main__":
    # No examples are provided, so this is a zero-shot prompt.
    #print(get_completion("Explain trigonometry."))

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