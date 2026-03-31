import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent import get_agent
from fastapi.responses import StreamingResponse
from langchain_core.messages import HumanMessage  , SystemMessage

app = FastAPI()

# ✅ CORS (optional now, but keep)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Mount frontend folder
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

agent = get_agent()

class ChatRequest(BaseModel):
    message: str

# ✅ Serve main HTML
@app.get("/")
def serve_home():
    return FileResponse("../frontend/index.html")

# ✅ Chat API
@app.post("/chat")
async def chat(req: ChatRequest):

    async def stream():
        # response = agent.invoke({
        #     "messages": [("user", req.message)]
        # })
        response = agent.invoke({
                         "messages": [
                         ("system", "You are a helpful assistant. ALWAYS use search tools when asked about current events, news, or future information."),
                          ("user", req.message)
                         ]
                        })

        full_text = response["messages"][-1].content

        # simulate streaming (token by token)
        for word in full_text.split(" "):
            yield word + " "
            await asyncio.sleep(0.05)

    return StreamingResponse(stream(), media_type="text/plain")


# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
# from agent import get_agent
# from fastapi.templating import Jinja2Templates
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # allow all (for dev)
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# templates = Jinja2Templates(directory="frontend")
# agent = get_agent()

# class ChatRequest(BaseModel):
#     message: str

# @app.get("/")
# def root():
#     return {"status": "API running"}

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/chat")
# def chat(req: ChatRequest):
#     response = agent.invoke({
#         "messages": [("user", req.message)]
#     })

#     return {
#         "response": response["messages"][-1].content
#     }