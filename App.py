import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up Streamlit page
st.set_page_config(page_title="Evia", page_icon="💬", layout="centered")

# Title and UI
st.title("💬 Evia – Your Emotional AI Companion")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are Evia, a friendly and emotionally aware chatbot. Be supportive, curious, and adapt to the user's mood."}]

# Display chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Generate response
    with st.spinner("Evia is thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=st.session_state.messages,
            temperature=0.7,
        )

        bot_reply = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.chat_message("assistant").markdown(bot_reply)
