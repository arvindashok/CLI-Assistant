import os
import typer
from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

app = typer.Typer()

@app.command()
def chat(text: Optional[str] = typer.Option(None, "--text", "-t", help="Start with text"),
         max_tokens: int = typer.Option(20, help="Control length of response. Defaults to 150")
        ):

    typer.echo(
        "Starting chat. Type exit to end session."
    )

    messages = []

    while True:
        if text:
            prompt = text
            text = None
        
        else:
            prompt = typer.prompt("You: ")

        messages.append ({"role":"user", "content":prompt})

        if prompt == "exit":
            typer.echo("GPT: Goodbye!")
            break

        response = client.completions.create(model = "babbage-002", prompt = prompt, max_tokens=max_tokens)

        typer.echo(f'ChatGPT: {response["choices"][0]["message"]["content"]}')
        messages.append(response["choices"][0]["message"])

if __name__ == "__main__":
    app()

