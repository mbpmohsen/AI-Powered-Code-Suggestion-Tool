# AI-Powered Code Suggestion Tool

## Project Description
This project is a simple AI-powered tool that helps you generate code snippets based on natural language descriptions. It uses OpenAI's GPT-based models to interpret your input and generate relevant code suggestions. The tool can be used via the command line or extended into a web-based interface using Flask.

## Features
- Generate code snippets based on descriptions provided by the user.
- Supports Python code suggestions.
- Extendable to a web interface using Flask.

## Installation

### 1. Clone the Repository
First, clone the project repository to your local machine.

```bash
cd AI-Powered-Code-Suggestion-Tool
```

## 2. Create Virtual Env
# For macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

# For Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## Install the Dependencies

```bash
pip install openai python-dotenv flask
```

## Usage
Command-Line Tool
You can use the tool from the command line. Run the following command to start the code suggestion prompt:

```bash
python3 code_suggestion.py
```


You’ll be prompted to describe the code you need help with. For example:

```bash
Describe what code you need help with (or type 'exit' to quit): Write a Python function to sort a list of numbers.
```