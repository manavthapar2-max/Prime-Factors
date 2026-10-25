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

def test_prime_factors_of_two():
    """Check that 2 has one prime factor."""
    assert generate_prime_factors(2) == [2]


def test_prime_factors_of_three():
    """Check that 3 has one prime factor."""
    assert generate_prime_factors(3) == [3]

def test_prime_factors_of_four():
    """Check that 4 has two prime factors."""
    assert generate_prime_factors(4) == [2, 2]

def test_prime_factors_of_six():
    """Check that 6 has two prime factors."""
    assert generate_prime_factors(6) == [2, 3]

def test_prime_factors_of_eight():
    """Check that 8 has three prime factors."""
    assert generate_prime_factors(8) == [2, 2, 2]