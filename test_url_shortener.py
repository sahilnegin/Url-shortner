from url_shortener import shorten_url, get_original_url

def test_url_shortening_and_retrieval():
    long_url = "https://google.com"
    short_code = shorten_url(long_url)
    assert isinstance(short_code, str)
    assert len(short_code) == 6

    retrieved_url = get_original_url(short_code)
    assert retrieved_url == long_url
