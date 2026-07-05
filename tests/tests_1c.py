
import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_positives():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15
    assert max_subarray_sum([0, 1, 100, 1]) == 102
    assert max_subarray_sum([0, 0]) == 0

def test_negatives():
    assert max_subarray_sum([-1, -2, -3]) == -6
    assert max_subarray_sum([-1, -1, -1000]) == -1002
    assert max_subarray_sum([-1, -(-1), 0]) == 0

def test_fractions():
    assert max_subarray_sum([1/10, 2/10, 4/10]) == 7/10
    assert max_subarray_sum([-1/10, 3/10]) == 2/10
    assert max_subarray_sum([0, -(-1/10), 2/10]) == 1/10

def test_decimals():
    assert max_subarray_sum([0.1, 0.2, 0.3]) == 0.6
    assert max_subarray_sum([-0.1, -0.2, -0.3]) == -0.6
    assert max_subarray_sum([0.3, -(-0.3)]) == 0

if __name__ == "__main__":
    pytest.main()
