
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Status_enam(str,Enum):
    NEW="NEW"
    ASSIGNED="ASSIGNED"
    IN_PROGRESS="IN_PROGRESS"
    COMPLETED="COMPLETED"
    FAILED="FAILED"
    CANCELLED="CANCELLED"

class Create_mission(BaseModel):
    title :Optional[str] = None
    description :Optional[str] =None
    location :Optional[str] = None
    difficulty :Optional[int] = Field(default=None,ge=1,le=10)
    importance :Optional[int] = Field(default=None,ge=1,le=10)


class Update_mission(BaseModel):
    title :Optional[str] = None
    description :Optional[str] =None
    location :Optional[str] = None
    difficulty :Optional[int] = Field(default=None,ge=1,le=10)
    importance :Optional[int] = Field(default=None,ge=1,le=10)
    status : Optional[Status_enam] = None

