import psycopg2
import pandas as pd

def read_from_file(filepath):
    statements=[]
    with open(filepath, 'r',encoding='UTF8') as file:
        for line in file:
            statements.append(line)
    return statements


def task1():
    print('After task #1:\n\n')
    
    try:

        user_name = "postgres"
        password = "123456"
        host = "127.0.0.1"
        database_name = "todo_db"
        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
      
        
        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS users CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS todo CASCADE;")

        cursor.execute("""CREATE TABLE users(id int PRIMARY KEY, name varchar(50));

                          CREATE TABLE todo(id int PRIMARY KEY, task varchar(50),user_id int, 
                          FOREIGN KEY (user_id) REFERENCES users(id) );""")

        
        rows = pd.read_sql_query("SELECT * FROM users ;", connection)
        print(rows,"\n\n")
        rows = pd.read_sql_query("SELECT * FROM todo ;", connection)
        print(rows,"\n\n")
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()
def task2():
    print('After task #2:\n\n')
    try:

        user_name = "postgres"
        password = "123456"
        host = "127.0.0.1"
        database_name = "todo_db"
        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
      
        
        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        cursor = connection.cursor()

     

        cursor.execute("""ALTER TABLE todo ADD COLUMN done boolean DEFAULT FALSE;""")

        rows = pd.read_sql_query("SELECT * FROM todo;", connection)
        print(rows,"\n\n")

        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()
        


def task3():
    print('After task #3:\n\n')
    try:

        user_name = "postgres"
        password = "123456"
        host = "127.0.0.1"
        database_name = "todo_db"
        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
      
        
        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        cursor = connection.cursor()
        statements=read_from_file('statements.txt')
        for statement in statements:
            cursor.execute(statement)

       
        rows = pd.read_sql_query("SELECT * FROM users;", connection)
        print(rows,"\n\n")
        rows = pd.read_sql_query("Select * from todo;", connection)
        print(rows,"\n\n")
            
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()



def task4():
    print('After task #4:\n\n')
    try:

        user_name = "postgres"
        password = "123456"
        host = "127.0.0.1"
        database_name = "todo_db"
        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
      
        
        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        rows = pd.read_sql_query("SELECT * FROM todo WHERE done = true;", connection)
        print(rows,"\n\n")
            
       

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()
def task5():
    print('After task #5:\n\n')
    try:

        user_name = "postgres"
        password = "123456"
        host = "127.0.0.1"
        database_name = "todo_db"
        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
      
        
        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        cursor = connection.cursor()
       
        

       
        cursor.execute("""UPDATE todo
SET done = true
WHERE user_id = 2;""")
        rows = pd.read_sql_query('select * from todo', connection)
        print(rows,"\n\n")
            
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()

def task6():
    print('After task #6:\n\n')
    try:

        user_name = "postgres"
        password = "123456"
        host = "127.0.0.1"
        database_name = "todo_db"
        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
      
        
        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        cursor = connection.cursor()
       
        

       
        cursor.execute("Delete from todo where done = true;")
        rows = pd.read_sql_query('select * from todo', connection)
        print(rows,"\n\n")
            
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()
def task7():
    print('After task #7:\n\n')
    try:

        user_name = "postgres"
        password = "123456"
        host = "127.0.0.1"
        database_name = "todo_db"
        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
      
        
        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        cursor = connection.cursor()
       
        

       
        cursor.execute("DROP table todo;")
        cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
        
        print(cursor.fetchall(),"\n\n")
        
        cursor.execute("DROP table users;")
        cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
        print(cursor.fetchall(),"\n\n")
       
            
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()

def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
main()    