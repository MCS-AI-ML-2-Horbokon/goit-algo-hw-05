def binary_search(slice: list[float], target: float) -> tuple[int, float | None]:
    if not slice:
        return (0, None)

    iterations = 0
    lower_index = 0
    upper_index = len(slice) - 1

    while lower_index < upper_index:
        iterations += 1
        middle_index = (lower_index + upper_index) // 2
        middle = slice[middle_index]
        if target > middle:
            lower_index = middle_index + 1
        else:
            upper_index = middle_index

    upper_bound = slice[upper_index]
    upper_bound_as_result = upper_bound if upper_bound >= target else None
    return (iterations, upper_bound_as_result)

if __name__ == "__main__":
    assert binary_search([], 3.14) == (0, None)
    assert binary_search([3], 3.14) == (0, None)
    assert binary_search([3.14], 3.14) == (0, 3.14)
    assert binary_search([4], 3.14) == (0, 4)
    assert binary_search([3, 3.14], 3.14) == (1, 3.14)
    assert binary_search([3, 4], 3.14) == (1, 4)
    assert binary_search([3.14, 4], 3.14) == (1, 3.14)
    assert binary_search([1, 2, 3, 4], 3.14) == (2, 4)
    assert binary_search([1, 2, 3, 4, 5], 3.14) == (2, 4)
