from database.db_connection import Connection
connection  = Connection()

class Mission:
    def create_mission(data):
        pass
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
        pass
    def count_all_missions():
        with connection.get_connection() as conn:
            with conn.cursor() as cursor :
                query = "SELECT COUNT(*) AS count_missions FROM missions "
                cursor.execute(query)
                count = cursor.fetchone()
        return count 

    def count_by_status(status):
        pass
    def count_open_missions():
        pass
    def count_critical_missions():
        pass
    def get_top_agents():
        pass
        
        