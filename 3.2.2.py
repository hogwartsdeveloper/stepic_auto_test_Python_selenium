def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"

s = 'My name is Zhannur'
n = 'Zhannur'

test_substring(s, n)