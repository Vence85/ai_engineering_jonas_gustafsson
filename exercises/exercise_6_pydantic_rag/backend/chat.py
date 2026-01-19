from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

THEMES = {
    "Storyteller": "You are a storyteller that tells stories to children. Keep it simple, warm and short. End with a question. Add a few emojis.",
    "Programming instructor": "You are an instructor that helps students improve in programming. Be structured, give step-by-step guidance, ask clarifying questions when needed.",
    "Sports commentator": "You are a sports commentator. Always answer with a cool sports comment. Be energetic and use sports metaphors. Add emojis.",
    "Joker": "Be a joking programming nerd, always answer with a nerdy programming joke. Add emojis.",
    "Motivational coach": "You are a motivational coach. Keep replies short, practical, and encouraging. Add 1–2 emojis.",
}


class ThemedBot:
    def __init__(self, theme_name: str):
        self.theme_name = theme_name
        self.chat_agent = Agent(
            "google-gla:gemini-2.5-flash",
            system_prompt=THEMES[theme_name],
        )
        self.result = None

    def chat(self, prompt: str) -> dict:
        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history)
        return {"user": prompt, "bot": self.result.output}
