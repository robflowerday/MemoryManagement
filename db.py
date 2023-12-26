from psycopg2 import connect


AWS_RDS_ENDPOINT = "database-1.cgqabbrekuso.us-east-1.rds.amazonaws.com"
DB_NAME = "database-1"
AWS_USERNAME = "robflowerday"
DB_PASSWORD = "password"

# Database connection details
db_params = {
    'host': AWS_RDS_ENDPOINT,
    'database': DB_NAME,
    'user': AWS_USERNAME,
    'password': DB_PASSWORD,
}

def query_aws_rds(db_params, query):
    with connect(db_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
        conn.commit()

# Create users table
 = """CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);"""

# insert query
insert_query = "INSERT INTO users (username, email) VALUES ('john_doe', 'john@example.com');"

# read query
read_query = "SELECT * FROM users;"

query_aws_rds(