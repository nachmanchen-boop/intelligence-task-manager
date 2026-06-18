import uvicorn
from fastapi import FastAPI
from logger import logger
from routers.agent_routes import router as router_agent
from routers.mission_routes import router as router_mission
from routers.report_routes import router as router_report
app = FastAPI()
app.include_router(router_agent,prefix="/agents")
app.include_router(router_mission,prefix="/missions")
app.include_router(router_report,prefix="/reports")



if "__main__"== __name__:
    
    uvicorn.run("main:app",port=8000,host='127.0.0.1',reload=True)
