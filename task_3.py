from pathlib import Path
from time import perf_counter_ns
from timeit import timeit
from typing import Callable
from algorithms.knuth import knuth_search
from algorithms.boyer import boyer_search
from algorithms.rabin import rabin_search

SearchFunction = Callable[[str, str], int | None]

def verify_asserts(search: SearchFunction) -> None:
    assert search("basdd", "basddadaadddasdadabaabdadaada") == 0
    assert search("basdd", "basddadaadddasdadabasddadaada") == 0
    assert search("abaab", "basddadaadddasdadabaabdadaada") == 17
    assert search("daada", "basddadaadddasdadabaabdadaada") == 24
    assert search("abaab", "basddadaadddasdadaxaabdadaada") is None
    assert search("", "basddadaadddasdadaxaabdadaada") is None
    assert search("basddadaadddasdadaxaabdadaada", "") is None
    assert search("basddadaadddasdadaxaabdadaada", "basddadaadddasdadaxaabdadaada") == 0
    assert search("basddadaadddasdadaxaabdadaada", "basddadaadddasdadaxaabdadaad") is None

def benchmark(search: SearchFunction, pattern: str, string: str):
    start = perf_counter_ns()
    result = search(pattern, string)
    end = perf_counter_ns()
    ms = (end - start) / 1000
    print(f"{search.__name__} completed search in {ms:.2f} ms, result: {result}")

if __name__ == "__main__":
    verify_asserts(knuth_search)
    verify_asserts(boyer_search)
    verify_asserts(rabin_search)

    data = Path("./data").resolve()
    article_1 = data / "article_1.txt"
    article_1_text = article_1.read_text(encoding="utf-8")
    article_2 = data / "article_2.txt"
    article_2_text = article_2.read_text(encoding="utf-8")
    pattern_2_good = "8. Meleshko Ye. Computer model of virtual social network with recommendation"
    pattern_2_bad = "18. Meleshko Ye. Computer model of virtual social network with recommendation"

    print("===== GOOD =====")
    benchmark(knuth_search, pattern_2_good, article_2_text)
    benchmark(boyer_search, pattern_2_good, article_2_text)
    benchmark(rabin_search, pattern_2_good, article_2_text)

    print("===== BAD ======")
    benchmark(knuth_search, pattern_2_bad, article_2_text)
    benchmark(boyer_search, pattern_2_bad, article_2_text)
    benchmark(rabin_search, pattern_2_bad, article_2_text)
