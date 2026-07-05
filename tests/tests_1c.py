
import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_same_numbers():
    assert max_subarray_sum([1, 1, 1, 1, 1]) == 5
    assert max_subarray_sum([0, 0, 0, 0]) == 0
    assert max_subarray_sum([-1, -1, -1]) == -1

def test_alternating():
    assert max_subarray_sum([1, 0, 1, 0, 1]) == 3
    assert max_subarray_sum([-1, 0, -1, 0, -1]) == 0

def test_opposites():
    assert max_subarray_sum([-1, 1, -1, 1]) == 1

def test_randoms():
    assert max_subarray_sum([2, -1, 9, -2, 1, -4, 3]) == 10


if __name__ == "__main__":
    pytest.main()
