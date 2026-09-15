import os
from google import genai


def run_detective_story(prompts: list[str], model: str = "gemini-3.5-flash-lite") -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Set the GEMINI_API_KEY environment variable before running this script.")

    client = genai.Client(api_key=api_key)

    # Initialize a multi-turn chat session
    chat = client.chats.create(model=model)

    for prompt in prompts:
        # Send message within the existing conversation session
        response = chat.send_message(prompt)

        print(f"Prompt: {prompt}")
        print(f"Response: {response.text}")
        print("-" * 80)


# List of detective prompts
prompts = [
    "Imagine you are a detective trying to solve a mystery.",
    "You arrive at the crime scene and start looking for clues.",
    "You find a strange object at the crime scene. What is it?",
    "How does this object relate to the crime?",
    "Who do you think is the suspect and why?"
]

run_detective_story(prompts)