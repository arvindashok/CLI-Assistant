# CLI Chat with GPT-3.5

This project enables users to interact with OpenAI's GPT-3.5 model directly through the command-line interface (CLI). Users can input text prompts, and the program will use the GPT-3.5 model to generate responses based on the input.

## Getting Started

Follow these instructions to set up and use the CLI chat with GPT-3.5:

### Prerequisites

Before running the program, make sure you have Python installed on your system. Additionally, you need to sign up for OpenAI API access to obtain an API key.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your_username/CLI-Assistant.git
   ```

2. Navigate to the project directory:
     ```bash
     cd CLI-Assistant
     ```

3. Install the required packages:
    ```bash
    pip install os openai dotenv
    ```

### Usage

1. Set your OpenAI API key as an environment variable. You can either export it in your shell or create a .env file in the project directory:

  ```bash
  export OPENAI_KEY="your_openai_api_key"
  ```
or
  ```bash
  echo "OPENAI_KEY=your_openai_api_key" > .env
  ```
2. Run the program:

  ```bash
  python main.py
  ```

3. Enter your text prompt in the CLI. The program will use the GPT-3.5 model to generate a response based on your input.

4. To exit the program, type "exit" and press Enter.

### Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature/improvement).
- Make your changes.
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature/improvement).
- Create a new Pull Request.

### Acknowledgements
-This project uses the OpenAI API to interact with the GPT-3.5 model.
