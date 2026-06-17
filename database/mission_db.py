from database.db_connection import Connection
connection  = Connection()

class Mission:
    def create_mission(data):
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
                query = f"""INSERT INTO missions
                VALUES(d) """
                cursor.execute(query,val)
                conn.commit()

    def get_all_missions():
        with connection.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor :
                cursor.execute("SELECT * FROM missions")
                data = cursor.fetchall()
        return data


    def get_mission_by_id(id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = ("SELECT * FROM missions WHERE id = %s")
                cursor.execute(query,(id,))
                data = cursor.fetchone()
        return data
    def assing_mission(m_id,a_id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "UPDATE missions SET assigned_agent_id = %s  WHERE id = %s "
                val = (
                    m_id,
                    a_id
                )
                cursor.execute(query,val)
                conn.commit()
                is_changed = cursor.rowcount > 0 
        return is_changed
    def update_mission_status(id,status):
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
    def get_open_missions_by_agent(id):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "SELECT * FROM missions WHERE id = %s AND status = IN_PROGRESS OR status = ASSIGNED"
                cursor.execute(query,(id,))
                count = cursor.fetchall()
        return count 
    def count_all_missions():
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "SELECT COUNT(*) AS count_missions FROM missions "
                cursor.execute(query)
                count = cursor.fetchone()
        return count 

    def count_by_status(status):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = f"SELECT COUNT(*) AS count_missions FROM missions WHERE status = {status}"
                cursor.execute(query)
                count = cursor.fetchone()
        return count 
    def count_open_missions(self):
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = """SELECT COUNT(status)
                                FROM misssion 
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
                for d in data.items():
                    if d["difficulty"] * 2 + d["importance"] > 25:
                        result.append(d)
            return result
                 
  

    def get_top_agents():
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
   
        