def naive_hash(substring: str) -> int:
    return sum(map(ord, substring))

def naive_compare(a: str, b: str) -> bool:
    index = 0
    size = len(a) # assume has equal size
    for index in range(size):
        if a[index] != b[index]:
            return False
    return True

def rabin_search(pattern: str, string: str) -> int | None:

    string_size = len(string)
    pattern_size = len(pattern)
    if pattern_size == 0 or pattern_size > string_size:
        return None

    substring_begin = 0
    substring_end = pattern_size
    substring = string[substring_begin:substring_end]
    substring_hash = naive_hash(substring)
    pattern_hash = naive_hash(pattern)
    if substring_hash == pattern_hash and naive_compare(pattern, substring):
        return 0

    while substring_end < string_size:
        substring_hash += ord(string[substring_end]) - ord(string[substring_begin])
        substring_begin += 1
        substring_end += 1
        if substring_hash == pattern_hash and naive_compare(pattern, string[substring_begin:substring_end]):
            return substring_begin

    return None
