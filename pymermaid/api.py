"""
API module for PyMermaid.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .app import parse_and_render

app = FastAPI(title="PyMermaid API")

class DiagramRequest(BaseModel):
    content: str
    format: str = 'png'

@app.post("/render")
async def render_diagram(request: DiagramRequest):
    try:
        result = parse_and_render(request.content, request.format)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
