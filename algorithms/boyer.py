def compute_shift_table(pattern: str) -> dict[str, int]:
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table

def boyer_search(pattern: str, string: str) -> int | None:
    string_size = len(string)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return None

    shift_table = compute_shift_table(pattern)
    string_offset = 0

    while string_offset <= string_size - pattern_size:
        pattern_index = pattern_size - 1

        while pattern_index >= 0 and string[string_offset + pattern_index] == pattern[pattern_index]:
            pattern_index -= 1

        if pattern_index < 0:
            return string_offset

        shift = shift_table.get(string[string_offset + pattern_index], pattern_size)
        string_offset += shift

    return None
