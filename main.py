from typing import Annotated
import json
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


df = open('./q-vercel-python.json', 'r').read()
df = json.loads(df)


@app.get("/api")
def read_items(name: Annotated[list[str] | None, Query()] = None):
  res = []
  for n in name:
    for item in df:
      if item["name"] == n:
        res.append(item)
  # print(json_response(res))
  return res
