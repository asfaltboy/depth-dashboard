#from neo4j import GraphDatabase

#from neo4j.v1 import GraphDatabase, basic_auth

#from py2neo import authenticate, Graph, Path, Node, Relationship
#from py2neo import Graph, Node

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

test_data = {
    "name":"John241",
    "nationality":"Anywhere2",
    "team":"ABCDE"
}

test_data2 = {
    "name":"John541",
    "nationality":"Anywhere2",
    "team":"ABCDE"
}

def add_user(tx, data):
    tx.run(
        statement="CREATE (x:User) SET x = {dict_param}",
        parameters={'dict_param': data}
    )

def add_relation(tx, team):
    tx.run(
    "MATCH (p1:User{team:$team}), (p2:User {team:$team}) MERGE (p1)-[:WORK_WITH3]-(p2)", team=team
    )

with driver.session() as session:
    session.write_transaction(add_user, test_data)
    session.write_transaction(add_user, test_data2)
    session.write_transaction(add_relation,"ABCDE")
