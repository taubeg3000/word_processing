"""
We want to write a fixture. A fixture is a function that prepares test data
"""
import pytest

DATA = 'data/corpus.txt'

@pytest.fixture
def get_text_from_file():
    with open(DATA, "r") as file:
        return file.read()

