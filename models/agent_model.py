from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime
class agent_enam(str,Enum):
    Junior="Junior"
    Senior="Senior"
    Commander="Commander"

class Create_agent(BaseModel):
    name :Optional[str] = None
    specialty :Optional[str] =None
    is_active :Optional[bool] = Field(default=True)
    completed_missions :Optional[int]= Field(default=0,ge=0)
    failed_missions :Optional[int]= Field(default=0,ge=0)
    agent_rank : Optional[agent_enam] = None
    
