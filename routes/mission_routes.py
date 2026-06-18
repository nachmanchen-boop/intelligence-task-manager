from fastapi import APIRouter,HTTPException
from models.mission_model import Create_mission,Update_mission
from database.mission_db import Mission
router = APIRouter()

mission = Mission()
@router.post("",status_code=201)
def post_agent(body:Create_mission):
    data = body.model_dump(exclude_none=True)
    result = mission.create_mission(data)
    return {"message":result}
@router.get("")
def get_all():
    data = mission.get_all_missions()
    return {"message":data}
@router.get("/{id}")
def get_by_id(id:int):
    data = mission.get_mission_by_id(id)

    if not data :
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":data}

@router.put("/{id}/assign/{agent_id}")
def Assign_task_to_agent(id:int,agent_id:int):
    data=mission.assign_mission(id,agent_id)
    if data == "Mission_not_found":
        raise HTTPException(status_code=404,detail=f" mission id {id} not found")
    if data == "Mission not available" :
        raise HTTPException(status_code=400,detail="Mission not available")
    if data == "Agent not found":
        raise HTTPException(status_code=404,detail=f" agent id {id} not found")
    if data == "Agent is not active":
        raise HTTPException(status_code=400,detail="Agent is not active")
    if data == "Agent has reached maximum missions":
       raise HTTPException(status_code=400,detail= "Agent has reached maximum missions")
    if data == "Only Commander can handle critical":
        raise HTTPException(status_code=400,detail= "Only Commander can handle critical")
    if data :
        return {"message":"The task was assigned"}

@router.put("/{id}/start")
def starting_a_task(id:int):
    status= "IN_PROGRESS"
    result=mission.update_mission_status(id=id,status=status)
    if not result:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":"The mission has begun."}


    
@router.put("/{id}/complete")
def complete_a_task(id:int):
    status= "COMPLETED"
    result=mission.update_mission_status(id=id,status=status)
    if not result:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":"The mission has COMPLETED."}

@router.put("/{id}/fail")
def fail_a_task(id:int):
    status= "FAILED"
    result=mission.update_mission_status(id=id,status=status)
    if not result:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":"The mission FAILED."}


@router.put("/{id}/cancel")
def cansel_a_task(id:int):
    status= "CANCELLED"
    result=mission.update_mission_status(id=id,status=status)
    if not result:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":"The mission has CANCELLED."}


    
