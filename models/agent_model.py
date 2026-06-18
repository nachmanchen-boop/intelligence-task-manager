from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
class agent_enam(str,Enum):
    Junior="Junior"
    Senior="Senior"
    Commander="Commander"

class Create_agent(BaseModel):
    name :Optional[str] = None
    specialty :Optional[str] =None
    is_active :Optional[bool] = Field(default=True)
    completed_missions :Optional[int]= Field(default=0)
    failed_missions :Optional[int]= Field(default=0)
    agent_rank : Optional[agent_enam] = None
    
class Update_agent(BaseModel):
    name :Optional[str] = None
    specialty :Optional[str] =None
    is_active :Optional[bool] = None
    completed_missions :Optional[int]= None
    failed_missions :Optional[int]= None
    agent_rank : Optional[agent_enam] = None
    
