from fastapi import FastAPI, HTTPException, status
from pathlib import Path
import json
from pydantic import BaseModel

glossary_data = json.loads(
    (Path(__file__).parents[2]/"data"/"fastapi_glossary.json").read_text(encoding="utf-8")
)
app = FastAPI()

class Glossary(BaseModel):
    id: int
    word: str
    meaning: str

class GlossaryCreate(BaseModel):
    word: str
    meaning: str

@app.get("/glossary", response_model=list[Glossary])
async def get_glossary(word: str | None = None ):
    if word:
        w = word.casefold()
        return [item for item in glossary_data if item["word"].casefold() == w]
    return glossary_data

@app.post("/add_glossary")
async def add_glossary(payload: GlossaryCreate):
    w = payload.word.casefold()
    if any(item["word"].casefold() == w for item in glossary_data):
        raise HTTPException(status_code=409, detail="Word already exist")
    

    new_id = max(x["id"] for x in glossary_data) + 1
    new_item = {"id": new_id, "word": payload.word, "meaning": payload.meaning}
    glossary_data.append(new_item)
    return new_item


