from projects.add import add
import pytest


@pytest.mark.parametrize('x, y, result', [
    (2, 2, 4),
    (3, 2, 5)
])
def test_add(x, y, result):
    print(f"{x} + {y} = {result}")
    assert add(x, y) == result
