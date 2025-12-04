from typing import Callable
from pathlib import Path
from time import perf_counter_ns
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

def benchmark_article(index: int, article: str, patterns: tuple[str, str]):
    print(f"\n========== Article {index} ==========")
    good, bad = patterns

    print("\n===== GOOD =====")
    benchmark(knuth_search, good, article)
    benchmark(boyer_search, good, article)
    benchmark(rabin_search, good, article)

    print("\n===== BAD ======")
    benchmark(knuth_search, bad, article)
    benchmark(boyer_search, bad, article)
    benchmark(rabin_search, bad, article)

if __name__ == "__main__":
    verify_asserts(knuth_search)
    verify_asserts(boyer_search)
    verify_asserts(rabin_search)

    data = Path("./data").resolve()
    article_1 = data / "article_1.txt"
    article_1_text = article_1.read_text(encoding="utf-8")
    pattern_1_good = (
        "Тому основне завдання програміста - аналізувати і вирішувати проблеми, "
        "де код - це всього лише інструмент досягнення мети. Часто виникають проблеми, "
        "які важко вирішити, тоді програмісту слід розробити новий алгоритм або поміркувати, "
        "як використовувати існуючий. Адже якщо знати про принципи роботи алгоритмів, "
        "тоді існує більша ймовірність знайти краще рішення. Іноді навіть нову проблему"
        " можна звести до старої, але для цього потрібно володіти фундаментальними знаннями."
    )
    pattern_1_bad = pattern_1_good + "!"
    benchmark_article(1, article_1_text, (pattern_1_good, pattern_1_bad))

    article_2 = data / "article_2.txt"
    article_2_text = article_2.read_text(encoding="utf-8")
    pattern_2_good = "8. Meleshko Ye. Computer model of virtual social network with recommendation"
    pattern_2_bad = "1" + pattern_2_good
    benchmark_article(2, article_2_text, (pattern_2_good, pattern_2_bad))
