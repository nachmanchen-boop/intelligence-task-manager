import mysql.connector


class Connection:

    @staticmethod
    def get_connection():
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            password="1234",
            user="root",
            database="intelligence_db"
        )
        return conn
