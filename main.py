#  file: main.py
from deta import Deta  # Import Deta
from fastapi import FastAPI
from pydantic import BaseModel

# If detabase is within a micro-- Projedeta = Deta("project key")
deta = Deta()
# to connect to or create a database.
db = deta.Base("pins")
app = FastAPI()

"""Models"""


class PinsIn(BaseModel):
    ts: str
    src: str
    A1: int = None
    D2: int = None
    D3: int = None


class Pins(PinsIn):
    key: str   # in Deta nosql, key is a str


"""Routes"""


@app.get("/")
def read_root():
    return {"Testing": "NoSQL_Pins"}


@app.get("/pins")
def read_pins():
    respns = db.fetch({})
    return respns


@app.get("/pin/{pin_id}")
def read_pin(pin_id: str):
    respns = db.get(pin_id)
    return respns


@app.post("/pins/", response_model=Pins)
async def create_pins(pns: PinsIn):
    rspns = db.put({"ts": pns.ts, "src": pns.src,
                    "D2": pns.D2, "D3": pns.D3, "A1": pns.A1})
    return rspns
