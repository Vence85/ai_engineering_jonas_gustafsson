from pydantic_ai import Agent
from dotenv import load_dotenv
from data_models import Restaurant

load_dotenv()

restaurant_agent = Agent(
    model = "google-gla:gemini-2.5-flash",
    system_prompt="You are here to help a user find real restaurants based on location. ",
    output_type = Restaurant,
)