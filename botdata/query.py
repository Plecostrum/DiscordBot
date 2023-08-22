import sqlite3

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS rules (id INTEGER PRIMARY KEY, name TEXT,  desc TEXT, type TEXT);"

INSERT_RULE = "INSERT INTO rules(name, desc, type) VALUES (?,?,?);"

GET_ALL_RULES = "SELECT \"name\" FROM rules;"
GET_RULE_BY_NAME = "SELECT \"name\",\"desc\" FROM rules WHERE name = ?;"

GET_ALL_ACTIONS = "SELECT \"name\" FROM rules WHERE type = \"ACTION\";"
GET_ACTION_BY_NAME = "SELECT \"name\",\"desc\" FROM rules WHERE type = \"ACTION\" AND name = ?;"

GET_ALL_CONDITIONS = "SELECT \"name\" FROM rules WHERE type = \"CONDITION\";"
GET_CONDITION_BY_NAME = "SELECT \"name\",\"desc\" FROM rules WHERE type = \"CONDITION\" AND name = ?;"

GET_ALL_MOVEMENTS = "SELECT \"name\" FROM rules WHERE type = \"MOVEMENT\";"
GET_MOVEMENT_BY_NAME = "SELECT \"name\",\"desc\" FROM rules WHERE type = \"MOVEMENT\" AND name = ?;"

GET_ALL_BONUS_ACTIONS = "SELECT \"name\" FROM rules WHERE type = \"BONUS ACTION\";"
GET_BONUS_ACTION_BY_NAME = "SELECT \"name\",\"desc\" FROM rules WHERE type = \"BONUS ACTION\" AND name = ?;"

GET_ALL_REACTIONS = "SELECT \"name\" FROM rules WHERE type = \"REACTION\";"
GET_REACTION_BY_NAME = "SELECT \"name\",\"desc\" FROM rules WHERE type = \"REACTION\" AND name = ?;"



def connect():
    return sqlite3.connect("dnd_Database.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE)
        
def add_rule(connection, name, desc,type):
    with connection:
        connection.execute(INSERT_RULE,(name, desc,type))
      
def get_all_rules(connection):
    with connection:
        return connection.execute(GET_ALL_ACTIONS).fetchall()
    
def get_rule_by_name(connection,name):
    with connection:
        return connection.execute(GET_RULE_BY_NAME,(name,)).fetchall()
    
def get_all_actions(connection):
    with connection:
        return connection.execute(GET_ALL_ACTIONS).fetchall()
    
def get_action_by_name(connection,name):
    with connection:
        return connection.execute(GET_ACTION_BY_NAME,(name,)).fetchall()
    
def get_all_conditions(connection):
    with connection:
        return connection.execute(GET_ALL_CONDITIONS).fetchall()
        
def get_condition_by_name(connection,name):
    with connection:
        return connection.execute(GET_CONDITION_BY_NAME,(name,)).fetchall()
    
def get_all_movements(connection):
    with connection:
        return connection.execute(GET_ALL_MOVEMENTS).fetchall()
        
def get_movement_by_name(connection,name):
    with connection:
        return connection.execute(GET_MOVEMENT_BY_NAME,(name,)).fetchall()

def get_all_bonus_actions(connection):
    with connection:
        return connection.execute(GET_ALL_BONUS_ACTIONS).fetchall()
        
def get_bonus_action_by_name(connection,name):
    with connection:
        return connection.execute(GET_BONUS_ACTION_BY_NAME,(name,)).fetchall()
    
def get_all_reactions(connection):
    with connection:
        return connection.execute(GET_ALL_REACTIONS).fetchall()
        
def get_reaction_by_name(connection,name):
    with connection:
        return connection.execute(GET_REACTION_BY_NAME,(name,)).fetchall()