from pydantic import BaseModel


class todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool