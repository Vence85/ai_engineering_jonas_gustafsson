from pydantic import BaseModel, Field

class Restaurant(BaseModel):
    name: str
    food: str =Field(description= "Type of cousine, e.g. Italian, Sushi, Indian")
    price_level: int = Field(gt=0, lt=5)
    rating: float = Field(gt=0, lt=5 )
    description: str
    opening_hours: str = Field(description="e.g Open today between 11:00AM and 23:00 PM")
    location: str =Field(description="The adress of the restaurant, e.g. Hantverksgatan 11 Göteborg")

class Prompt(BaseModel):
    prompt: str