from fastapi import APIRouter,HTTPException
from database.mission_db import Mission
from database.db_connection import Connection
connection= Connection()
mission = Mission()
router = APIRouter()
@router.get("/summary")
def general_report():
    with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = """SELECT status FROM """
                 
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
    """{
        "open": 5,
        "in_progress": 3,
        "completed": 12,
        "failed": 1,
        "canceled": 2
        }
        """
@router.get("/top-agent")
def top_agent():
    data = mission.get_top_agents()
    return {"message":data}

      