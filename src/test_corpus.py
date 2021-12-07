from word_processor import count_words

def test_corpus(get_text_from_file):
    assert count_words(get_text_from_file) > 10