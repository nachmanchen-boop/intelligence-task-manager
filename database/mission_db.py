from database.db_connection import Connection
from agent_db import Agent

connection  = Connection()
agent = Agent()
class Mission:
    def create_mission(self,data:dict):
         with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                print("ddd")
                count = ", ".join(['%s'] * len(data))
                names = ", ".join(data.keys())
                
                val = list(data.values())

               
                    
                query = f"INSERT INTO missions({names})  VALUES({count}) "
                cursor.execute(query,val)
                conn.commit()

    def get_all_missions(self):
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor :
                cursor.execute("SELECT * FROM missions")
                data = cursor.fetchall()
        return data


    def get_mission_by_id(self,id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = ("SELECT * FROM missions WHERE id = %s")
                cursor.execute(query,(id,))
                data = cursor.fetchone()
        return data
    def assing_mission(self,m_id,a_id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                check_agent  = agent.get_agent_by_id(a_id)
                missions_count = len(self.get_open_missions_by_agent(a_id))

                mission = self.get_mission_by_id(m_id)
                if not mission:
                    return "Mission not found"
                if mission["status"] != 'NEW':
                    return "Mission not available"
                if not check_agent:
                    return "Agent not found"
                if check_agent["is_active"] == False:
                    return "Agent is not active"
                missions_count = len(self.get_open_missions_by_agent(a_id))
                if missions_count > 3:
                    return "Agent has reached maximum missions"
                if mission["level_risk"] == "CRITICAL" and check_agent["agent_rank"] != "Commander":
                    return "Only Commander can handle critical"

                query = "UPDATE missions SET assigned_agent_id = %s  WHERE id = %s "
                val = (
                    a_id,
                    m_id
                )
                cursor.execute(query,val)
                conn.commit()
                is_changed = cursor.rowcount > 0 
        return is_changed
    def update_mission_status(self,id,status):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "UPDATE missions SET status = %s  WHERE id = %s "
                val = (
                    status,
                    id
                )
                cursor.execute(query,val)
                conn.commit()
                is_changed = cursor.rowcount > 0 
        return is_changed
    def get_open_missions_by_agent(self,id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "SELECT * FROM missions WHERE id = %s AND (status = 'IN_PROGRESS' OR status = 'ASSIGNED')"
                cursor.execute(query,(id,))
                count = cursor.fetchall()
        return count 
    def count_all_missions(self):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "SELECT COUNT(*) AS count_missions FROM missions "
                cursor.execute(query)
                count = cursor.fetchone()
        return count 

    def count_by_status(self,status):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = f"SELECT COUNT(*) AS count_missions FROM missions WHERE status = %s"
                cursor.execute(query,(status,))
                count = cursor.fetchone()
        return count 
    def count_open_missions(self):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = """SELECT COUNT(status)
                                FROM misssions 
                                WHERE status = 'NEW';
                                """
                cursor.execute(query)
                data = cursor.fetchall()
        return data

    def count_critical_missions(self):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                data = self.get_all_missions()
                result = []
                for d in data:
                    if (d["difficulty"] * 2 + d["importance"]) > 25:
                        result.append(d)
            return len(result)
                 
  

    def get_top_agents(self):
         with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = """
                SELECT  assigned_agent_id
                FROM  missions
                ORDER BY status = COMPLETED DESC 
                LIMIT 1
                """
                cursor.execute(query)
                top_member = cursor.fetchone()

                
            return top_member
   
        