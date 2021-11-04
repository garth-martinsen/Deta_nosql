#  file: main.py
from deta import Deta  # Import Deta
from fastapi import FastAPI

# Initialize with a Project Key unless detabase is within a micro-- then automatic
# deta = Deta("project key")
deta = Deta()
# This how to connect to or create a database.
db = deta.Base("pins")

# You can create as many db's as you want without additional charges.
# books = deta.Base("books")


class PinsIn(BaseModel):
    ts: str
    src: str
    A1: int = None
    D2: int = None
    D3: int = None


class Pins(PinsIn):
    id: int


app = FastAPI()


@app.get("/")
def read_root():
    return {"Testing": "NoSQL_Pins"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/pins", response_model=Pins)
async def create_pins(pns: PinsIn):
    rspns = db.put({"ts": pns.ts, "src": pns.src,
                    "D2": pns.D2, "D3": pns.D3, "A1": pns.A1})
    return rspns
