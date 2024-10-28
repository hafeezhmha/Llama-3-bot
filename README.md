# 🦙 Llama-3-bot 
This application is a simple chatbot interface built using Streamlit, designed to interact with users using the LLaMA 3 language model. The chatbot is capable of processing user inputs and generating responses, creating a conversational experience.

## Features
- **Interactive Chat Interface**: Users can communicate with the chatbot in a clean, easy-to-navigate interface.
- **Dynamic Response Generation**: The chatbot generates responses using the LLaMA 3 model, simulating a typing effect to enhance realism.
-**Session Management**: The app retains chat history throughout the session, allowing users to view previous messages.
-**Configuration Options**: Users can input their Groq API key to enable the chatbot functionality.
-**Clear Chat History**: Users can clear the chat history with a simple button click.

## Requirements
Python 3.7 or higher
Streamlit
Groq SDK
python-dotenv for managing environment variables

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hafeezhmha/Llama3-bot.git
   cd llama3-chatbot
2. **Install the required packages** :
   ```bash
   pip install requirements.txt
3. **Obtain your API key and paste it in the application**.
4. **To run the application, navigate to the project directory and execute**:
   ```bash
   streamlit run app.py
