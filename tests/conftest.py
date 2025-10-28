import pytest
from uop.db.neo4j import adaptor

@pytest.fixture(scope="module")
def db_plugin():
    """
    Pytest fixture to set up and tear down a Neo4j test database.
    """
    # Use the adapter's class method to create a temporary test database
    db = adaptor.Neo4jUOP.make_test_database(
        uri="bolt://localhost:7687",
        user="neo4j",
        password="password"
    )
    
    yield db  # Provide the database adapter instance to the tests
    
    # Teardown: drop the database after tests are complete
    db.drop_database()
    db.close()
