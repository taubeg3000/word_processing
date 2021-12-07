import pytest
from word_processor import count_words

test_data = [
    ("I am in class", 4),
    ("Everlyn", 1),
    ("He comes", 2),
    ('<h1>This is a heading</h>', 4),
    ('<h1 class="foo">This is a heading</h>', 5),
    ("straße 15 in üoö+p", 5)
]


@pytest.mark.parametrize('input, output', test_data)
def test_all_in_one(input, output):
    assert count_words(input) == output
