"""
This exercise focuses on decorators.

Decorators are a design pattern in Python that adds new
functionality to an existing object without modifying its structure.
Decorators enable separation of concerns by allowing you to wrap a function
with additional behavior without changing the function's code.

The difference between @staticmethod and regular instance methods:

- A regular instance method receives `self` as its first argument
  automatically, giving it access to the object attributes
  and other methods. It operates on a specific object.

- A @staticmethod does NOT receive `self`. It behaves like a
  regular function that happens to live in the class namespace. It
  cannot access instance or class state directly. Use @staticmethod
  for utility functions that are related to the class but
  don't need access to instance or class data.

Args and kwargs are used to pass a variable number of arguments to a
function without explicitly defining them,
similar to (int argc, char ** argv) in C.
"""

from collections.abc import Callable
from functools import wraps
from time import sleep, time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints function execution time."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time() - start
        print(f"Spell completed in {end:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator that validates power levels.
    If the 'power' argument is below min_power, the spell is not cast
    and an error message is returned instead.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if 'power' in kwargs:
                pwr = kwargs['power']
            else:
                pwr = args[-1]  # Assumes power is the last positional argument
            if pwr < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells up to max_attempts."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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
    """A class that uses static methods and instance methods.
    Here, we demonstrate how static methods don't require self and
    can be called on the class itself,while instance methods
    operate on specific instances of the class.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is valid (>=3 chars, letters/spaces only)."""
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with the given name and power level.
        This function calls the previously defined power_validator
        decorator to ensure that the power level is sufficient
        before casting the spell."""
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
