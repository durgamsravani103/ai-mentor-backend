from pydantic import BaseModel

class RoadmapResponse(BaseModel):
    roadmap_content: str

    class Config:
        from_attributes = True