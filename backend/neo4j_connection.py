import os

from neo4j import GraphDatabase

NEO4J_USER = os.getenv('NEO4J_USER', "neo4j")
NEO4J_PASS = os.getenv('NEO4J_PASS', "admin")
NEO4J_URI = os.getenv('NEO4J_URI', "bolt://localhost:7687")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
