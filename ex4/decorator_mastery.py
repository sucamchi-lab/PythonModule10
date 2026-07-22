"""
This exercise focuses on mastering decorators.

Decorators are a design pattern in Python that adds new
functionality to an existing object without modifying its structure.
Decorators work by wrapping a function, method, or class with another function
that can add more logic or modify its behavior.
Each decorator handles one specific responsibility,
keeping functions focused on their primary purpose.

The difference between @staticmethod and regular instance methods:

- A regular instance method receives `self` as its first argument
  automatically, giving it access to the object attributes
  and other methods. It operates on a specific object.

- A @staticmethod does NOT receive `self`. It behaves like a
  regular function that happens to live in the class namespace. It
  cannot access instance or class state directly. Use @staticmethod
  for utility functions that are logically related to the class but
  don't need access to instance data.
"""

from collections.abc import Callable
from functools import wraps
from time import sleep, time


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates power levels.
    If the 'power' argument is below min_power, the spell is not cast
    and an error message is returned instead.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'power' in kwargs:
                pwr = kwargs['power']
            else:
                pwr = args[-1]  # Assume power is the last positional argument
            if pwr < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells up to max_attempts."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return (
                f"Spell casting failed after {max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    """A guild of mages with static and instance methods."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is valid (>=3 chars, letters/spaces only)."""
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with the given name and power level."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        sleep(0.5)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def waaagh_spell() -> str:
        sleep(0.5)
        raise ValueError("Spell failed")

    print(waaagh_spell())
    print("Waaaaaaagh spelled !")

    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
