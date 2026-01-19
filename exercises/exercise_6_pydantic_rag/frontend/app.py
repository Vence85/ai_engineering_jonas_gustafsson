import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).absolute().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from backend.chat import ThemedBot, THEMES






def init_state():
    if "theme" not in st.session_state:
        st.session_state.theme = list(THEMES.keys())[0]

    # En bot per tema, så de får eget “minne”
    if "bots" not in st.session_state:
        st.session_state.bots = {t: ThemedBot(t) for t in THEMES.keys()}

    # Separat chattlogg per tema, så UI inte blandas
    if "messages" not in st.session_state:
        st.session_state.messages = {t: [] for t in THEMES.keys()}


def render_messages(theme: str):
    for msg in st.session_state.messages[theme]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def main():
    st.title("Themed Chatbot")

    init_state()

    theme = st.selectbox("Choose theme", list(THEMES.keys()))
    st.session_state.theme = theme

    with st.expander("Current theme prompt"):
        st.write(THEMES[theme])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Reset this theme chat"):
            st.session_state.bots[theme] = ThemedBot(theme)
            st.session_state.messages[theme] = []
    with col2:
        if st.button("Reset ALL themes"):
            st.session_state.bots = {t: ThemedBot(t) for t in THEMES.keys()}
            st.session_state.messages = {t: [] for t in THEMES.keys()}

    render_messages(theme)

    if prompt := st.chat_input(f"Talk to {theme} bot..."):
        st.session_state.messages[theme].append({"role": "user", "content": prompt})

        bot = st.session_state.bots[theme]
        answer = bot.chat(prompt)["bot"]

        st.session_state.messages[theme].append({"role": "assistant", "content": answer})
        st.rerun()


if __name__ == "__main__":
    main()
