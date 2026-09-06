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
            max_output_tokens=512,
        ),
    )
    return response.text


if __name__ == "__main__":
    # No examples are provided, so this is a zero-shot prompt.
    print(get_completion("Explain trigonometry."))
