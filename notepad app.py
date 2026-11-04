
import sqlite3
import subprocess

# TEST 1: SQL Injection
def find_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


# TEST 2: Hardcoded fake secret
API_KEY = "FAKE_TEST_KEY_123456789"


# TEST 3: Command injection risk
def run_command(user_input):
    subprocess.call("echo " + user_input, shell=True)


# TEST 4: Unsafe eval
def calculate(expression):
    return eval(expression)


# TEST 5: Bare exception
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except:
        return None
# TEST 6: Insecure deserialization pattern
def load_user_data(data):
    import pickle
    return pickle.loads(data)