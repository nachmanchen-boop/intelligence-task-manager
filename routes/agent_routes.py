from fastapi import APIRouter,HTTPException
router = APIRouter()
from models.agent_model import Create_agent,Update_agent
from database.agent_db import Agent
agent = Agent()

@router.post("",status_code=201)
def posr_agent(body:Create_agent):
    
    data = body.model_dump(exclude_none=True)
    if not data :
        HTTPException(status_code=400,detail="tehris not data")
    result = agent.create_agent(data)
    return {"message":result}

@router.get("")
def get_all():
    data = agent.get_all_agents()
    return {"message":data}
@router.get("/{id}")
def get_by_id(id:int):
    data = agent.get_agent_by_id(id)
    if not data :
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":data}
@router.put("/{id}")
def Agent_update(id:int,body:Update_agent):
    data = body.model_dump(exclude_none=True)
    if not data :
        raise HTTPException(status_code=400,detail="There is nothing to update.")
    result = agent.update_agent(data)
    if not result:
                raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":result}
@router.put("/{id}/deactivate")
def agent_deactivation(id:int):
    is_exsust = agent.get_agent_by_id(id)
    if not is_exsust:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    result = agent.deactivate_agent(id)

    if not result:
         raise HTTPException(status_code=400,detail="not sucssus")
    return {"message":"The change was successful."}
@router.get("/{id}/performance")
def agent_performance(id:int):
    result = agent.get_agent_performance(id)
    if not result:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return result

         
     
