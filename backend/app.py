from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from agent import get_agent
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="frontend")
agent = get_agent()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
def chat(req: ChatRequest):
    response = agent.invoke({
        "messages": [("user", req.message)]
    })

    return {
        "response": response["messages"][-1].content
    }