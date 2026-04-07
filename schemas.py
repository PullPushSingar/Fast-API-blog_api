from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    """Base class for post"""
    title: str = Field(min_length=1,max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1,max_length=64)

class PostCreate(PostBase):
    """Post Create Model"""
    pass

class PostResponse(PostBase):
    """Post Response Model"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str