from fastapi import HTTPxception
from db_connection import Connection
connection  = Connection()

#Connection.get_connection()
class Agent:
    def create_agent(self,data:dict):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                parts = []
                val = []
                print("ddd")
                for key,value in data.items() :
                    parts.append(f"{key} = %s")
                    val.append(value)
                d = {f", ".join(parts)}
                val.append(id)
                query = f"""INSERT INTO agents
                VALUES(d) """
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
                
    def update_agent(id,data):
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                parts = []
                values = []
                for key,value in data.items() :
                    parts.append(f"{key} = %s")
                    values.append(value)
                values.append(id)
                query = f"UPDATE agents SET {", ".join(parts)} WHERE id = %s"
                cursor.execute(query,values)
                conn.commit()
                is_change = cursor.rowcount > 0 
            return is_change
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
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query_completed = "SELECT completed_missions FROM agents WHERE id  = %s"
                cursor.execute(query_completed(id,))
                completed = cursor.fetchone()
                completed +=1 
                query = "UPDATE agents SET completed_missions = {completed}  WHERE id = %s "
                cursor.execute(query(id,))
                conn.commit()





                
    def increment_failde(id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query_completed = "SELECT failed_missions FROM agents WHERE id  = %s"
                cursor.execute(query_completed(id,))
                completed = cursor.fetchone()
                completed +=1 
                query = "UPDATE agents SET failed_missions = {completed}  WHERE id = %s "
                cursor.execute(query(id,))
                conn.commit()

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

