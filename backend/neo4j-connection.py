#from neo4j import GraphDatabase

#from neo4j.v1 import GraphDatabase, basic_auth

#from py2neo import authenticate, Graph, Path, Node, Relationship
#from py2neo import Graph, Node

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

test_data = {
    "name":"John14",
    "nationality":"Anywhere2",
    "team":"ABCD"
}

def add_user(tx, data):
    tx.run(
        statement="CREATE (x) SET x = {dict_param}",
        parameters={'dict_param': data}
    )


def add_relations(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])


with driver.session() as session:
    session.write_transaction(add_user, test_data)


'''
with driver.session() as session:
    session.write_transaction(add_friend, "Arthur", "Guinevere")
    session.write_transaction(add_friend, "Arthur", "Lancelot")
    session.write_transaction(add_friend, "Arthur", "Merlin")
    session.read_transaction(print_friends, "Arthur")
'''
#node1 = Node("FirstLabel", name="MyPythonNode1", neo4j_version="3.5.11")

#node2 = Node("FirstLabel", "SecondLabel", name="MyPythonNode2", neo4j_version="3.5.11")
#graph.create(node1)
#graph.create(node2)
#resultNodes = graph.create(node1, node2)


'''
py2neo.authenticate("localhost:7474", "neo4j", "admin")
graph = Graph("http://localhost:7474/db/data/")

def add_friend(tx, name, friend_name):
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)

def print_friends(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])

with driver.session() as session:
    session.write_transaction(add_friend, "Arthur", "Guinevere")
    session.write_transaction(add_friend, "Arthur", "Lancelot")
    session.write_transaction(add_friend, "Arthur", "Merlin")
    session.read_transaction(print_friends, "Arthur")

'''
'''
CREATE (PennyM:Person {name:'Penny Marshall', born:1943})
CREATE
  (TomH)-[:ACTED_IN {roles:['Jimmy Dugan']}]->(ALeagueofTheirOwn),

{
  "User": [
    {
      "Name": '',
      "Email": '',
      "Tounge": '',
      "Sex": '',
      "Program_languages": '',
      "Nationalities": '',
      "Projects": '',
      "Team": '',
      "Role": '',
      "Oficce_location": '',
      "Age": '',
      "Fav_movie": '',
      "OS": '',
    }
  ],
  "Project": [
    {
      "Languages": '',
      "Name": '',
      "vertical": '',
      "Hosting _rovider": '',
      "Services": '',
      "Jira": '',
    }
  ]
}



'''