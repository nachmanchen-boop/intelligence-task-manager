from fastapi import HTTPException
from db_connection import Connection
connection  = Connection()
#Connection.get_connection()
class Agent:
    def create_agent(self,data:dict):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                parts = []
                val = []
                for key,value in data.items() :
                    parts.append(f"{key} = %s")
                    val.append(value)
                val.append(id)
                query = f"""INSERT INTO agents
                VALUES({f", ".join(parts)}) """
                cursor.execute(query,val)
                conn.commit()

    def get_all_agents(self):
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor :
                cursor.execute("SELECT * FROM agents")
                data = cursor.fetchall()
        return data



    def get_agent_by_id(self,id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = ("SELECT * FROM agents WHERE id = %s")
                cursor.execute(query,(id,))
                data = cursor.fetchone()
        return data
                
    def update_agent(id):
        pass
    def deactivate_agent(id):
         with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = f"UPDATE agents SET is_active = %s WHERE id = %s"
                val = (
                    False,
                    id
                )
                cursor.execute(query,val)
                conn.commit()

    def increment_completed(id):
        pass
    def increment_failde(id):
        pass
    def get_agent_performance(id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query_completed = "SELECT completed_missions FROM agents WHERE id  = %s"
                cursor.execute(query_completed(id,))
                completed = cursor.fetchone()
                query_failed = "SELECT failed_missions FROM agents WHERE id  = %s"
                cursor.execute(query_failed(id,))
                failed = cursor.fetchone()



                
    def agents_active_count():
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "SELECT COUNT(*) AS active FROM agents WHERE is_active = True"
                cursor.execute(query)
                count = cursor.fetchone()
        return count


s = Agent()
a = {
    'name':"david"
}
s.create_agent(a)