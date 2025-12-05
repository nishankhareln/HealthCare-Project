import streamlit as st
import requests

API_URL = "http://localhost:8000/chat/"

st.header("💬 Medical Chat Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Describe your symptoms..."):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # API Call
    try:
        response = requests.post(API_URL, json={"message": prompt})
        if response.status_code == 200:
            data = response.json()
            bot_reply = data["response"]
            
            # Append recommended doctors if any
            if data.get("recommended_doctors"):
                bot_reply += "\n\n**Recommended Doctors:**"
                for doc in data["recommended_doctors"]:
                    bot_reply += f"\n- {doc['name']} ({doc['department']} "

            # Add bot response to state
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            with st.chat_message("assistant"):
                if data.get("is_emergency"):
                    st.error(bot_reply)
                else:
                    st.markdown(bot_reply)
        else:
            st.error("Error connecting to server.")
    except Exception as e:
        st.error(f"Connection failed: {e}")