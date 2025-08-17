from getpass import getpass
from mysql.connector import connect, Error

def create_database():
    try:
        # Connect to MYSQL server 
        connection = connect(
            host='localhost',
            user= input("Enter MySQL username: "),
            password= getpass("Enter MySQL password: ")
        )

        # Create the database
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store" 
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            print("Database 'alx_book_store created sucessfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if  connection.is_connected():
            connection.close()

if __name__ == "__main___":
    create_database()

        