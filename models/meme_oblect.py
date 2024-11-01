from pydantic import  BaseModel
from typing import List, Dict, Any


class MemeObject(BaseModel):
    id: int
    text: str
    url: str
    tags: List[str]
    info: Dict[str, Any]
