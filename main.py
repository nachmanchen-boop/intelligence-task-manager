import uvicorn
from fastapi import FastAPI
from logger import logger
from routes.agent_routes import router as router_agent
from routes.mission_routes import router as router_mission
from routes.report_routes import router as router_report
from database.db_connection import Connection

app = FastAPI()
app.include_router(router_agent,prefix="/agents")
app.include_router(router_mission,prefix="/missions")
app.include_router(router_report,prefix="/reports")




if "__main__"== __name__:
    logger.info("start app")
    connection = Connection()

    connection.create_tables()

    uvicorn.run("main:app",port=8000,host='127.0.0.1',reload=True)
