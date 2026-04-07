import asyncio
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.agent import get_agent
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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
# app.mount("/static", StaticFiles(directory="../frontend"), name="static")

agent = get_agent()

session_memory = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str

# ✅ Serve main HTML
@app.get("/")
def serve_home():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
    # return FileResponse("../frontend/index.html")

# ✅ Chat API
# @app.post("/chat")
# async def chat(req: ChatRequest):

#     async def stream():
#         # response = agent.invoke({
#         #     "messages": [("user", req.message)]
#         # })
#         response = agent.invoke({
#                          "messages": [
#                          ("system", "You are a helpful assistant. ALWAYS use search tools when asked about current events, news, or future information."),
#                           ("user", req.message)
#                          ]
#                         })

#         full_text = response["messages"][-1].content

#         # simulate streaming (token by token)
#         for word in full_text.split(" "):
#             yield word + " "
#             await asyncio.sleep(0.05)

#     return StreamingResponse(stream(), media_type="text/plain")

@app.post("/chat")
async def chat(req: ChatRequest):

    # get session history
    if req.session_id not in session_memory:
        session_memory[req.session_id] = []

    history = session_memory[req.session_id]

    async def stream():

        # combine history + new message
        messages = [
            ("system", "You are a helpful assistant. ALWAYS use search tools when needed.")
        ] + history + [("user", req.message)]

        response = agent.invoke({
            "messages": messages
        })

        full_text = response["messages"][-1].content

        # save user + assistant message
        history.append(("user", req.message))
        history.append(("assistant", full_text))

        # stream response
        for word in full_text.split():
            yield word + " "
            await asyncio.sleep(0.03)

    return StreamingResponse(stream(), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

