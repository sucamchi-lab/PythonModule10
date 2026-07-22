"""
This exercise focuses on variable scope in Python.
Scope refers to the region of a program where a variable is accessible.
Understanding scope is crucial for writing clean and maintainable code,
as it helps prevent naming conflicts and unintended side effects.

We use nonlocal to indicate that a variable is defined in an ENCLOSING
function's scope, without using a global variable.

Closures help to capture and remember the values of variables
from their enclosing scopes by creating a function
that retains access to those variables.

Global is forbidden because it goes against FP
(Functional Programming) principles and can lead to unpredictable behavior.
"""


from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate_spell(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accumulate_spell


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()
    store, recall = vault["store"], vault["recall"]
    print("Store 'secret' = 42")
    store("secret", 42)
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")
