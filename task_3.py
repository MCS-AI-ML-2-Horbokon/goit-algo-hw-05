from typing import Callable
from algorithms.knuth import knuth_search
from algorithms.boyer import boyer_search
from algorithms.rabin import rabin_search

def verify_asserts(search: Callable[[str, str], int | None]) -> None:
    assert search("basdd", "basddadaadddasdadabaabdadaada") == 0
    assert search("basdd", "basddadaadddasdadabasddadaada") == 0
    assert search("abaab", "basddadaadddasdadabaabdadaada") == 17
    assert search("daada", "basddadaadddasdadabaabdadaada") == 24
    assert search("abaab", "basddadaadddasdadaxaabdadaada") is None
    assert search("", "basddadaadddasdadaxaabdadaada") is None
    assert search("basddadaadddasdadaxaabdadaada", "") is None
    assert search("basddadaadddasdadaxaabdadaada", "basddadaadddasdadaxaabdadaada") == 0
    assert search("basddadaadddasdadaxaabdadaada", "basddadaadddasdadaxaabdadaad") is None

if __name__ == "__main__":
    verify_asserts(knuth_search)
    verify_asserts(boyer_search)
    verify_asserts(rabin_search)
