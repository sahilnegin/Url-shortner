import string
import random

# In-memory database to store code -> URL mapping
url_db = {}

# Characters allowed in short codes
ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 6


def generate_short_code(length=CODE_LENGTH) -> str:
    """Generates a random short code."""
    return ''.join(random.choices(ALPHABET, k=length))


def shorten_url(long_url: str) -> str:
    """Shortens a long URL and stores the mapping."""
    # Check if already shortened
    for code, url in url_db.items():
        if url == long_url:
            return code
    
    # Generate a new unique short code
    while True:
        code = generate_short_code()
        if code not in url_db:
            break

    url_db[code] = long_url
    return code


def get_original_url(short_code: str) -> str | None:
    """Returns the original URL for a given short code."""
    return url_db.get(short_code)


if __name__ == "__main__":
    long_url = "https://youtube.com"
    short_code = shorten_url(long_url)
    print("Short code:", short_code)

    original_url = get_original_url(short_code)
    print("Original URL:", original_url)
