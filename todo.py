import psycopg2
import pandas as pd


try:

    user_name = "postgres"
    password = "123456"
    host = "127.0.0.1"
    database_name = "todo_db"
    connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"
    connection = psycopg2.connect(connect_str)
    connection.autocommit = True
    cursor = connection.cursor()

except psycopg2.DatabaseError as exception:
    print(exception)


def read_from_file(filepath):
    statements = []
    with open(filepath, 'r', encoding='UTF8') as file:
        for line in file:
            statements.append(line.split("+"))
    return statements


def task1():
    
    print('After task #1:\n\n')
    cursor.execute("DROP TABLE IF EXISTS users CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS todo CASCADE;")
    cursor.execute(""" CREATE TABLE users(id int PRIMARY KEY, name varchar(50));
                                    CREATE TABLE todo(id int PRIMARY KEY, task varchar(50),user_id int,
                                    FOREIGN KEY (user_id) REFERENCES users(id) );""")

    rows = pd.read_sql_query("SELECT * FROM users;", connection)
    print(rows, "\n\n")
    rows = pd.read_sql_query("SELECT * FROM todo;", connection)
    print(rows, "\n\n")


   
    
   


def task2():
    
    print('After task #2:\n\n')
    cursor.execute("""ALTER TABLE todo ADD COLUMN done boolean DEFAULT FALSE;""")

    rows = pd.read_sql_query("SELECT * FROM todo;", connection)
    print(rows, "\n\n")


def task3():
    
    print('After task #3:\n\n')

    statements = read_from_file('statements.sql')
    for statement in statements:
       
        cursor.execute(f"INSERT INTO {statement[0]} VALUES {statement[1][:-1]}")

    rows = pd.read_sql_query("SELECT * FROM users;", connection)
    print(rows, "\n\n")
    rows = pd.read_sql_query("Select * from todo;", connection)
    print(rows, "\n\n")


def task4():
    print('After task #4:\n\n')

    rows = pd.read_sql_query("SELECT * FROM todo WHERE done = true;", connection)
    print(rows, "\n\n")


def task5():
    
    print('After task #5:\n\n')

    cursor.execute("""UPDATE todo
                                   SET done = true
                                   WHERE user_id = 2;""")

    rows = pd.read_sql_query('select * from todo order by id asc', connection)
    print(rows, "\n\n")

    rows = pd.read_sql_query('select * from users order by id asc', connection)
    print(rows, "\n\n")


def task6():
    
    print('After task #6:\n\n')

    cursor.execute("Delete from todo where done = true;")
    rows = pd.read_sql_query('select * from todo', connection)
    print(rows, "\n\n")


def task7():
    
    print('After task #7:\n\n')

    cursor.execute("DROP table todo;")
    cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")

    print(cursor.fetchall(), "\n\n")

    cursor.execute("DROP table users;")
    cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
    
def manual ():
        user_input=input("Would you like to input any new record? y/n:  ").upper()
        while user_input == "Y":

            table=input("Which table would you like to update?  ")
            given_datas = []
            rows = pd.read_sql_query(f"Select * from {table};", connection)

            cursor.execute(f"""SELECT Column_name, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE 
            TABLE_NAME = '{table}'""")

            dtypes=cursor.fetchall()
            for index,item in enumerate(rows):
                for i in range(len(dtypes)):
                    if item == dtypes[i][0]:
                        temp=dtypes[index]
                        dtypes[index]=dtypes[i]
                        dtypes[i]=temp
            

            for index,item in enumerate(rows.columns):
                data=input(f"{item}: ")
                dtype=dtypes[index][1]
                if 'INT' in dtype.upper():
            
                    given_datas.append(data)
                    
                else:
                    given_datas.append(f"'{data}'")
                    
        
            
            cursor.execute(f"INSERT INTO {table} VALUES ({','.join(given_datas)})")
            user_input=input("Would you like to input any new record? y/n:  ").upper()



def main():
    task1()
    task2()
    task3()
    manual()
    task4()
    task5()
    task6()
    task7()
    cursor.close()


main()
