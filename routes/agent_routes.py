from fastapi import APIRouter,HTTPException
router = APIRouter()
from models.agent_model import Create_agent,Update_agent
from database.agent_db import Agent
agent = Agent()
from logger import logger
@router.post("",status_code=201)
def posr_agent(body:Create_agent):
    logger.info("start posr_agent")
    data = body.model_dump(exclude_none=True)
    if not data :
        logger.error("error")
        HTTPException(status_code=400,detail="tehris not data")
    result = agent.create_agent(data)
    return {"message":result}

@router.get("")
def get_all():
    logger.info("start ")

    data = agent.get_all_agents()
    return {"message":data}
@router.get("/{id}")
def get_by_id(id:int):
    logger.info("start get_by_id")

    data = agent.get_agent_by_id(id)
    if not data :
        logger.error("error get_by_id")

        raise HTTPException(status_code=404,detail=f"id {id} not found")
    logger.info("end get_by_id")

    return {"message":data}
@router.put("/{id}")
def Agent_update(id:int,body:Update_agent):
    logger.info("start Agent_update")

    data = body.model_dump(exclude_none=True)
    if not data :
        logger.error("error Agent_update")

        raise HTTPException(status_code=400,detail="There is nothing to update.")
    result = agent.update_agent(data)
    if not result:
                logger.error("error Agent_update")

                raise HTTPException(status_code=404,detail=f"id {id} not found")
    logger.info("end Agent_update")

    return {"message":result}
@router.put("/{id}/deactivate")
def agent_deactivation(id:int):
    logger.info("start agent_deactivation")

    is_exsust = agent.get_agent_by_id(id)
    if not is_exsust:
        logger.error("error agent_deactivation")

        raise HTTPException(status_code=404,detail=f"id {id} not found")

    result = agent.deactivate_agent(id)

    if not result:
        logger.error("error agent_deactivation")

        raise HTTPException(status_code=400,detail="not sucssus")
    logger.info("end agent_deactivation")

    return {"message":"The change was successful."}
    
@router.get("/{id}/performance")
def agent_performance(id:int):
    logger.info("start agent_performance")


    result = agent.get_agent_performance(id)
    if not result:
        logger.error("error agent_performance")

        raise HTTPException(status_code=404,detail=f"id {id} not found")
    
    logger.info("end agent_performance")

    return result

         
     
