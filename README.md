# intelligence-task-manager


# System explanation

## A system for managing tasks and agents for the ShadowNet intelligence unit with tables in SQL rules organized with departments for managing data and connections.

## Folder structure
```
intelligence-task-manager/
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
|-- routes/
| ├── agent_routes.py
│ ├── mission_routes.py
│ └── report_routes.py
├── models/
│ ├── agent_model.py
│ └── mission_model.py
├── README.md
├── requirements.txt
└── .gitignore
```
# Table structure 

## agents
```
id INT PRIMARY KEY AUTO_INCREMENT
name                VARCHAR(50) 
specialty           VARCHAR (100)
is_active           BOOLEAN DEFAULT TRUE
completed_missions  INT DEFAULT 0
failed_missions     INT DEFAULT 0 
agent_rank VARCHAR()  ENUM(Junior | Senior | Commander)
```
## missions
```
id INT PRIMARY KEY AUTO_INCREMENT
title             VARCHAR()
description       TEXT 
location          VARCHAR()
difficulty        INT CHECK (difficulty > 0 AND difficulty < 11)
importance        INT CHECK (importance > 0 AND importance < 11)
status            VARCHAR(15) DEFAULT NEW (NEW,ASSIGNED,PROGRESS_IN,COMPLETED,FAILED,CANCELLED)
level_risk        VARCHAR()
assigned_agent_id INT DEFAULT NULL
```
# Function structure


## db_coonection
```
get_connection()
create_tables()
database_create()
```
##  AgentDB class
```
create_agent(data)       POST.router("",status_code=201)   Add an agent
get_all_agents()         GET.router("")                    Returning all agents
get_agent_by_id(id)      GET.router("/{id}")               Returning an agent by ID
update_agent(id, data)   PUT.router("/{id}")               Returning an agent by ID
deactivate_agent(id)     PATCH.router("/{id}")             Making an agent not active
increment_completed(id)                                    The number of tasks the agent completed
increment_failed(id)                                       The number of tasks the agent failed
get_agent_performance(id)                                  Returns a dictionary with the TOTAL FAILED COMPLETED success_rate and the success_rate needs to be calculated from the total
count_active_agents()                                      Number of active agents
```
## MissionDB class
```
create_mission(data)              POST.router("",status_code=201)   Create a task
get_all_missions()                GET.router("")                    Return all tasks
get_mission_by_id(id)             GET.router("/{id}")               Returning a task by ID
assign_mission(m_id, a_id)        PATCH.router(")                   Assign a task to an agent
update_mission_status(id, status)                                   Change task status
get_open_missions_by_agent(id)                                      Returns ASSIGNED/IN_PROGRESS agent tasks
count_all_missions()                                                count of tasks
count_by_status(status)                                             Number of tasks by status
count_open_missions()                                               Number of open tasks
count_critical_missions()                                           COUNT of CRITICAL tasks
get_top_agent()                                                     Agent with the highest number of completed missions
```
# חוקי המערכת 
```
1) rank must be Junior/Senior/Commander other value is an error
2) Difficulty and importance must be between 1 and 10, different is an error.
3) Risk level is calculated only when creating a machine, not by the user.
4) An agent with active_is=false cannot accept tasks.
5) An agent can have up to three open tasks (ASSIGNED/IN_PROGRES) at the same time
6) If CRITICAL=level_risk — only an agent with the rank of Commander can accept the mission
7) Only a task with a status of NEW can be assigned. After assignment: ASSIGNED=status.
8) Only a task with the ASSIGNED status can be started. After: PROGRESS_IN=status
9) Only a task can be completed. PROGRESS_IN and changed to completed or failed status.
10) Only a task with a status of NEW or ASSIGNED can be canceled — otherwise an error.
```

stAPI, מחבר את כל ה-routers, ובעת עליית השרת קורא ל-database_create)(
ו-tables_create)(. זהו נקודת הכניסה היחידה לאפליקציה.
Agents endpoints
.AgentDB של גלובלי instance מכיל — agent_routes.py :קובץ
Method Endpoint תיאור
יצירת סוכן חדש agents/[ POST]
כל הסוכנים agents/[ GET]
]GET[ /agents/{id} ID לפי סוכן
]PUT[ /agents/{id} סוכן עדכון
]PUT[ /agents/{id}/deactivate סוכן השבתת
]GET[ /agents/{id}/performance סוכן ביצועי
Missions endpoints
.AgentDB-ו MissionDB של גלובלי instance מכיל — mission_routes.py :קובץ
Method Endpoint תיאור
יצירת משימה missions/[ POST]
כל המשימות missions/[ GET]
]GET[ /missions/{id} ID לפי משימה
]PUT[ /missions/{id}/assign/{agent_id} )בהמשך מוסבר בדיקות 6 )לסוכן שיוך
]PUT[ /missions/{id}/start משימה התחלת
]PUT[ /missions/{id}/complete בהצלחה סיום
]PUT[ /missions/{id}/fail בכישלון סיום
]PUT[ /missions/{id}/cancel משימה ביטול
Reports endpoints
report_routes.py :קובץ
Method Endpoint תיאור
דוח כללי של המערכת summary/reports/[ GET]
]GET[ /reports/missions-by-status סטטוס לפי משימות
]GET[ /reports/top-agent )get_top_agent( המצטיין ה
## Database (Docker)

```bash
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=intelligence_db -p 3306:3306 mysql:8.0
```
## database name
db_Intelligence
## Run

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

.