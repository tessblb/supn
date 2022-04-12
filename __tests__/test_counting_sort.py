from projects.counting_sort import get_counting_sort
import pytest

from random import randint
input = [randint(0, 5) for _ in range(20)]
expected = sorted(input)


@pytest.mark.parametrize('nums, max, result', [
    ([1, 4, 5], 6, [1, 4, 5]),
    ([2, 1, 9], 10, [1, 2, 9]),
    (input, max(input) + 1, expected)
])
def test_add(nums, max, result):
    print(f"\nInput: {nums}\nOutput: {result}")
    assert get_counting_sort(nums, max) == result
