
from pydantic import BaseModel, Field
from typing import Optional
class Create_agent(BaseModel):
    title :Optional[str] = None
    description :Optional[str] =None
    location :Optional[bool] = Field(default=True)
    difficulty :Optional[int] = Field(default=None,)
    importance :Optional[int] = Field(default=None)
    status : Optional[str] = Field(default="NEW")
    
