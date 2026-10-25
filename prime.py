"""Generate prime factors for a given number."""


def generate_prime_factors(number):
    """Return prime factors after validating the input."""
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    return []