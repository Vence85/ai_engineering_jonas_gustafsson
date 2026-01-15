import streamlit as st
from chat import JokeBot

def init_session_sates():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "bot" not in st.session_state:
        st.session_state.bot = JokeBot()

def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    if prompt := st.chat_input("Talk to the Tjöt gbg"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt).get("bot")

        response = f"Tjöt Gbg: {bot_response}"

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

    

def layout():
    st.markdown("# Chat with Tjöt Gbg")
    st.write(
    "Tjöt Gbg is a story telling chat bot from Gothenburg"
    )

    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    init_session_sates()
    layout()