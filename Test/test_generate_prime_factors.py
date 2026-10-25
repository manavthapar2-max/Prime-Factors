"""Tests for the prime factors program."""

import pytest
from prime import generate_prime_factors


def test_invalid_input():
    """Check that non-integer input raises ValueError."""
    with pytest.raises(ValueError):
        generate_prime_factors("hello")


def test_prime_factors_of_one():
    """Check that 1 has no prime factors."""
    assert generate_prime_factors(1) == []