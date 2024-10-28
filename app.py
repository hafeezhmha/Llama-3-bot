import streamlit as st
import groq  # Import the Groq SDK
import os
from dotenv import load_dotenv
from datetime import datetime
import time

# Load environment variables from .env file
load_dotenv()

# App title and custom header
st.set_page_config(page_title="LLAMA 3 Chatbot", page_icon="🦙")
st.title("🤖 Welcome to the LLAMA 3 Chatbot!")
st.markdown("### Your personal AI assistant to answer your queries")

# Groq API Credentials
with st.sidebar:
    st.header('Configuration')
    groq_api = os.getenv('GROQ_API_TOKEN')  # Change this to your Groq API key environment variable name
    if groq_api:
        st.success('API key loaded from environment!', icon='✅')
    else:
        groq_api = st.text_input('Enter Groq API token:', type='password')
        if not groq_api:
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to enter your prompt message!', icon='👉')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Function to display messages with timestamps
def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f"**{message['role'].capitalize()}** ({datetime.now().strftime('%H:%M:%S')}): {message['content']}")

display_messages()

# Clear chat history functionality
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response using Groq
def generate_llama2_response(prompt_input):
    user_message = prompt_input  # The user's input will be directly used here
    
    try:
        # Initialize Groq client
        client = groq.Client(api_key=groq_api)  # Ensure the Groq client is correctly initialized
        
        # Create a chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama3-70b-8192",  # Replace this with your model
        )

        # Extract and return the assistant's response
        return chat_completion.choices[0].message.content

    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "Sorry, I couldn't generate a response."

# User-provided prompt
if prompt := st.chat_input(disabled=not groq_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if the last message is not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Assistant is typing..."):
            # Generate the response
            full_response = generate_llama2_response(prompt)
            time.sleep(0.5)  # Short delay to simulate typing without making it feel slow

            # Show the full response after generating
            st.markdown(full_response)

    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
