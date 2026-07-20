"""
This exercise focuses on the functools module.
functools is a standard Python library that provides higher-order
functions and tools for working with callable objects.

functools.reduce applies a binary function cumulatively to the items
of an iterable, reducing the sequence to a single value. This enables
powerful data aggregation on lists or dictionaries
without writing explicit loops.

functools.partial creates a new function by pre-filling some arguments
of an existing function. This is useful for creating specialized
versions of general-purpose functions, reducing boilerplate and
making code more declarative.

functools.lru_cache is a decorator that memoizes function results using
a Least Recently Used (LRU) cache. Memoization avoids recomputing
expensive function calls by storing previously computed results.
This dramatically improves performance for recursive functions like
Fibonacci, reducing the time complexity from O(2^n) to O(n).

functools.singledispatch transforms a function into a single-dispatch
generic function, allowing different behavior based on the type of
the first argument. This is Python's approach to function overloading,
enabling clean, type-based dispatch without complex if-else chains.
"""

from collections.abc import Callable
from typing import Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the specified operation."""
    ops: dict[str, Callable[[int, int], int]] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min,
    }
    if not spells:
        return 0
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Return a dictionary of partially applied enchantment functions.

    Each version pre-fills power=50 and the respective element.
    """
    return {
        'fire': functools.partial(base_enchantment, power=50, element='Fire'),
        'ice': functools.partial(base_enchantment, power=50, element='Ice'),
        'dark': functools.partial(base_enchantment, power=50, element='Dark'),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a singledispatch-based dispatcher for different spell types."""
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    spells = [10, 20, 30, 40]
    try:
        print("\nTesting spell reducer...")
        print(f"Sum: {spell_reducer(spells, 'add')}")
        print(f"Product: {spell_reducer(spells, 'multiply')}")
        print(f"Max: {spell_reducer(spells, 'max')}")
        print(f"Min: {spell_reducer(spells, 'min')}")
        print(f"Invalid operation: {spell_reducer(spells, 'invalid')}")

    except ValueError as e:
        print(e)

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "dark"]))
    print(dispatch(3.14))  # Unknown spell type
