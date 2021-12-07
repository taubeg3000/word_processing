import pytest
from word_processor import count_words


class TestWordProcessor:
    ONE_WORD = "Everline"

    def test_one_word(self):
        assert count_words(TestWordProcessor.ONE_WORD) == 1

    def test_two_words(self):
        assert count_words("He comes") == 2

    def test_type_error(self):
        text = ["I am in class"]
        with pytest.raises(TypeError) as type_error:
            assert count_words(text) == 4
        assert "only accepts strings" in str(type_error.value)

    def test_accents(self):
        assert count_words("straße 15 in üoö+p") == 5

    def test_html(self):
        text = '<h1>This is a heading</h>'
        assert count_words(text) == 4

    def test_html_with_attributes(self):
        text = '<h1 class="foo">This is a heading</h>'
        assert count_words(text) == 5

    def test_linebreaks(self):
        text = "Tosin\nKetan\nTobi"
        assert count_words(text) == 3