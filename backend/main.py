from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database.database import get_db
from .agents.chat_agent import ChatAgent
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/api/chat")
async def chat_endpoint(query: Query, db: Session = Depends(get_db)):
    try:
        agent = ChatAgent(db)
        state = {"query": query.text, "results": []}  
        
        final_state = agent.executor.invoke(state)

        return {"response": final_state["response"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
