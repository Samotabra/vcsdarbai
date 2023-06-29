import psycopg2

db_params = {
    'host': 'localhost',
    'port': 5432,
    'db': 'real_estate'
    'user': 'postgres',
    'password': 'x'
}

def create_table():
    connection = psycopg2.connect(**db_params)  #perduodam dictionary reiksmes i connection su **


    cursor = connection.cursor()

    create_table="""
    CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    kaina INTEGER,
    vieta VARCHAR(225),
    plotas VARCHAR(225)
    )           
    """
    cursor.execute(create_table)

    connection.commit()
    cursor.close()
    connection.close()

def insert_data(data):
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    insert_table = """
    INSERT INTO properties(kaina, vieta, plotas)
    VALUES(%s,%s,%s)
    """
    cursor.executemany(insert_table, data)
    connection.commit()
    cursor.close()
    connection.close()

def ikelti_duomenis():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    select_query = """
    SELECT kaina, vieta, plotas FROM properties  # gal real_estate?
    """
    cursor.execute(select_query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return rows
