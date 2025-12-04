def compute_LPS(pattern: str) -> list[int]:
    lps = [0] * len(pattern)
    length = 0
    index = 1
    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            lps[index] = length
            index += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[index] = 0
                index += 1
    return lps

def knuth_search(pattern: str, string: str) -> int | None:
    pattern_size = len(pattern)
    string_size = len(string)
    lps = compute_LPS(pattern)
    string_index = 0
    pattern_index = 0

    while string_index < string_size:
        if pattern[pattern_index] == string[string_index]:
            string_index += 1
            pattern_index += 1
        elif pattern_index != 0:
            pattern_index = lps[pattern_index - 1]
        else:
            string_index += 1

        if pattern_index == pattern_size:
            return string_index - pattern_index

    return None


if __name__ == "__main__":
    assert knuth_search("basdd", "basddadaadddasdadabaabdadaada") == 0
    assert knuth_search("abaab", "basddadaadddasdadabaabdadaada") == 17
    assert knuth_search("daada", "basddadaadddasdadabaabdadaada") == 24
    assert knuth_search("abaab", "basddadaadddasdadaxaabdadaada") is None
