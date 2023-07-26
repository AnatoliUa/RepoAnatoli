import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None
    def create(self):
        self.name = "Anatoli"
        self.second_name = "Muliar"
    def remove(self):
        self.name = ""
        self.second_name = ""

@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    
@pytest.fixture
def github_api():
    api = GitHub()
    yield api

@pytest.fixture
def db_object():
    """Create database object"""
    db = Database()
    yield db

@pytest.fixture
def db_del_rec_after_test():
    """Delete temporal record after test"""
    db0 = Database()
    yield
    db0.delete_product_by_id(4)
