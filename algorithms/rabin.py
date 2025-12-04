from typing import Literal


POLY_BASE: int = 256
POLY_MOD: int = 101

def naive_hash(substring: str) -> int:
    """
    Naive hash:
    Calculate hash as a sum or ord codes: overflow and fallback to bigint is possible
    """
    return sum(map(ord, substring))

def naive_hash_recompute(current_hash: int, first: str, next: str, pattern_size: int) -> int:
    """
    Calculate new naive hash: if remove first character and add next
    """
    diff = ord(next) - ord(first)
    return current_hash + diff

def polynomial_hash(substring: str) -> int:
    """
    Simple polynomial hash
    """
    n = len(substring)
    hash_value = 0
    for i, char in enumerate(substring):
        power_of_base = pow(POLY_BASE, n - i - 1) % POLY_MOD
        hash_value = (hash_value + ord(char) * power_of_base) % POLY_MOD
    return hash_value

def polynomial_hash_recompute(current_hash: int, first: str, next: str, pattern_size: int) -> int:
    """
    Calculate new polynomial hash: if remove first character and add next

    For polynomial hash:
    Given first and next character: calculate hash difference if remove first character and add next
    """
    h_multiplier = pow(POLY_BASE, pattern_size - 1) % POLY_MOD
    current_hash = (current_hash - ord(first) * h_multiplier) % POLY_MOD
    current_hash = (current_hash * POLY_BASE + ord(next)) % POLY_MOD
    if current_hash < 0:
        current_hash += POLY_MOD
    return current_hash

def rabin_search(pattern: str, string: str, hash_algorithm: Literal["polynomial", "naive"] = "polynomial") -> int | None:
    if hash_algorithm == "polynomial":
        hash_function = polynomial_hash
        hash_function_recompute = polynomial_hash_recompute
    elif hash_algorithm == "naive":
        hash_function = naive_hash
        hash_function_recompute = naive_hash_recompute

    string_size = len(string)
    pattern_size = len(pattern)
    if pattern_size == 0 or pattern_size > string_size:
        return None

    substring_begin = 0
    substring_end = pattern_size
    substring = string[substring_begin:substring_end]
    substring_hash = hash_function(substring)
    pattern_hash = hash_function(pattern)
    if substring_hash == pattern_hash and pattern == substring:
        return 0

    while substring_end < string_size:
        substring_hash = hash_function_recompute(substring_hash, string[substring_begin], string[substring_end], pattern_size)
        substring_begin += 1
        substring_end += 1
        if substring_hash == pattern_hash and pattern == string[substring_begin:substring_end]:
            return substring_begin

    return None

def rabin_search_polynomial(pattern: str, string: str) -> int | None:
    return rabin_search(pattern, string, "polynomial")

def rabin_search_naive(pattern: str, string: str) -> int | None:
    return rabin_search(pattern, string, "naive")
