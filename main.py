import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

while True:

    prompt = input ("\nYou: ")

    if prompt == "exit":
        print ("GPT: Goodbye!")
        break

    message = "Do no exceed 10 words: " + prompt

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")