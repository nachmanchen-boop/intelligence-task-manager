import mysql.connector

class Connection:
    def get_connection(self):
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            password="1234",
            user="root",
            database="intelligence_db"
        )
        return conn

    def create_tables(self):
        with self.get_connection() as conn:
            with conn.cursor() as cursor :
                query_agents = """
                CREATE TABLE IF NOT EXISTS agents(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(256) ,
                specialty VARCHAR (256),
                is_active BOOLEAN DEFAULT TRUE,
                completed_missions  INT DEFAULT 0,
                failed_missions     INT DEFAULT 0 ,
                agent_rank  ENUM('Junior' , 'Senior' , 'Commander')
                   )
                    """
                cursor.execute(query_agents)
                conn.commit()
                query_missions = """
                CREATE TABLE IF NOT EXISTS missions(
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(256),
                description TEXT,
                location VARCHAR(256),
                difficulty INT CHECK (difficulty > 0 AND difficulty < 11),
                importance INT CHECK (importance > 0 AND importance < 11),
                status VARCHAR(256) DEFAULT 'NEW',
                level_risk VARCHAR(256),
                assigned_agent_id INT DEFAULT NULL

                )
           """
                cursor.execute(query_missions)
                conn.commit()
    def database_create(self):
        with self.get_connection() as conn:
            with conn.cursor() as cursor :
                cursor.execute("CREATE DATABASE IF NOT EXISTS intelligence_db")
                conn.commit()
        
s = Connection()
s.create_tables()