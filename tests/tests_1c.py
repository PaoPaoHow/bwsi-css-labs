
import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def same_numbers():
    assert max_subarray_sum([1, 1, 1, 1, 1]) == 5
    assert max_subarray_sum([0, 0, 0, 0]) == 0
    assert max_subarray_sum([-1, -1, -1]) == -3

def alternating():
    assert max_subarray_sum([1, 0, 1, 0, 1]) == 1
    assert max_subarray_sum([-1, 0, -1, 0, -1]) == -1

def opposites():
    assert max_subarray_sum([-1, 1, -1, 1]) == 1

def randoms():
    assert max_subarray_sum([2, -1, 9, -2, 1, -4, 3]) == 10


if __name__ == "__main__":
    pytest.main()
