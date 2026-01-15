from fastapi import FastAPI
from pydantic_ai import Agent
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse
from data_models import Prompt
from agents import restaurant_agent
from utils import query_duckdb

load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/restaurants")
async def read_restaurants():
    restaurants = query_duckdb("SELECT * FROM restaurant;")
    return restaurants.to_dict(orient="records")

@app.post("/restaurant")
async def create_restaurant(query: Prompt):
    result = await restaurant_agent.run(query.prompt)
    restaurant = result.output

    # protect against SQL injection
    query_duckdb(
        "INSERT INTO restaurant VALUES (?,?,?,?,?,?,?)",
        parameters=[restaurant.name, restaurant.food, restaurant.price_level, restaurant.rating, restaurant.description, restaurant.opening_hours, restaurant.location ],
    )

    return restaurant
