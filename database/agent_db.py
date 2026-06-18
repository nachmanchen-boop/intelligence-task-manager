from database.db_connection import Connection
connection  = Connection()
from logger import logger
#Connection.get_connection()
class Agent:
    def create_agent(self,data:dict):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                logger.info ("start create_agent")
                count = ", ".join(['%s'] * len(data))
                names = ", ".join(data.keys())
                val = tuple(data.values())
                query = f"INSERT INTO agents({names})  VALUES({count})"
                print(query)
                print(val)
                cursor.execute(query,val)
                conn.commit()
                create = cursor.fetchone()
        return create


    def get_all_agents(self):
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor :
                cursor.execute("SELECT * FROM agents")
                data = cursor.fetchall()
        return data



    def get_agent_by_id(self,id):
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor :
                query = "SELECT * FROM agents WHERE id = %s"
                cursor.execute(query,(id,))
                data = cursor.fetchone()
        return data
                
    def update_agent(self,id,data):
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                parts = []
                values = []
                for key,value in data.items() :
                    parts.append(f"{key} = %s")
                    values.append(value)
                values.append(id)
                conect_parts =", ".join(parts)
                query = f"UPDATE agents SET {conect_parts} WHERE id = %s"
                cursor.execute(query,values)
                conn.commit()
                is_change = cursor.rowcount > 0 
        return is_change
    def deactivate_agent(self,id:int):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = f"UPDATE agents SET is_active = False WHERE id = %s"
                
                cursor.execute(query,(id,))
                conn.commit()
                is_change = cursor.rowcount > 0 
        return is_change

    def increment_completed(self,id:int):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query_completed = "UPDATE agents SET completed_missions = completed_missions + 1 WHERE id  = %s"
                cursor.execute(query_completed,(id,))

                conn.commit()
                compliet = cursor.fetchone()
        return compliet





                
    def increment_failde(self,id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query_failed = "UPDATE agents SET failed_missions = failed_missions + 1 WHERE id  = %s"

                cursor.execute(query_failed,(id,))
                conn.commit()
                failed = cursor.fetchone()
        return failed

    def get_agent_performance(self,id):
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor :
                query_completed = "SELECT completed_missions,failed_missions  FROM agents WHERE id  = %s"
                cursor.execute(query_completed,(id,))
                all =  cursor.fetchone()
                if not all :
                    return None
                completed =all['completed_missions']
                failed = all['failed_missions']
                total = completed + failed
                if not total:
                   return{  
                    'completed':completed,
                    'failed':failed,
                    'total':total,
                    'success_rate' : 0}
                success_rate = (completed / total) * 100

                data = {
                    
                'completed':completed,
                'failed':failed,
                'total':total,
                'success_rate' : success_rate
                }
        return data



                
    def count_active_agents(self):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "SELECT COUNT(*) AS active FROM agents WHERE is_active = True"
                cursor.execute(query)
                count = cursor.fetchone()
                if not count:
                    return 0
        return count

