from fastapi import APIRouter,HTTPException
from database.mission_db import Mission
from database.db_connection import Connection
from logger import logger
from database.agent_db import Agent
agent = Agent()
connection= Connection()
mission = Mission()
router = APIRouter()
@router.get("/summary")
def general_report():
    with connection.get_connection() as conn:
        result = {
            "active_agents_count": agent.count_active_agents(),
            "total_missions": mission.count_all_missions(),
            "open_missions": mission.count_open_missions(),
            "completed_missions": mission.count_by_status("COMPLETED"),
            "failed_missions": mission.count_by_status("FAILED"),
            "critical_missions": mission.count_critical_missions(),
        }
    return result                 
        # {
        #     "active_agents_count": 0,
        #     "total_missions": 0,
        #     "open_missions": 0,
        #     "completed_missions": 0,
        #     "failed_missions": 0,
        #     "critical_missions": 0
        #     }
@router.get("/missions-by-status")
def missions_by_status():
    result = {
            "open": mission.count_by_status("NEW"),
            "in_progress": mission.count_by_status("IN_PROGRESS"),
            "completed": mission.count_by_status("COMPLETED"),
            "failed": mission.count_by_status("FAILED"),
            "canceled": mission.count_by_status("CANCELLED"),
        }
    return result
    
@router.get("/top-agent")
def top_agent():
    data = mission.get_top_agents()
    return {"message":data}


