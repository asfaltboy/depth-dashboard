import os

from neo4j import GraphDatabase

NEO4J_USER = os.getenv('NEO4J_USER', "neo4j")
NEO4J_PASS = os.getenv('NEO4J_PASS', "admin")
NEO4J_URI = os.getenv('NEO4J_URI', "bolt://localhost:7687")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

def add_user(tx, data):
    tx.run(
        statement="CREATE (x:User) SET x = {dict_param}",
        parameters={'dict_param': data}
    )

def add_relation(tx, team):
    tx.run(
    "MATCH (p1:User{team:$team}), (p2:User {team:$team}) MERGE (p1)-[:WORK_WITH3]-(p2)", team=team
    )

#with driver.session() as session:
#    session.write_transaction(add_user, test_data)
#    session.write_transaction(add_user, test_data2)
#    session.write_transaction(add_relation,"ABCDE")