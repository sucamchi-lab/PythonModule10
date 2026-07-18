from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} health"


def lightning_strike(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_blast = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Troll', 10)}")
    print(f"Amplified: {mega_blast('Troll', 10)}")

    print("\nTesting conditional caster...")

    def condition(target: str, power: int) -> bool:
        return target == "Goblin" and power < 20
    cautious_fireball = conditional_caster(condition, fireball)
    print(f"Against invalid target: {cautious_fireball('Dragon', 50)}")
    print(f"Against valid target: {cautious_fireball('Goblin', 10)}")
    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, lightning_strike])
    results = combo("Orc", 30)
    print(f"Sequence results: {results}")

    print("\nTest spell combiner with amplified spells...")
    mega_combo = spell_combiner(
        power_amplifier(fireball, 2), power_amplifier(heal, 2))
    print(f"Amplified combo: {mega_combo('Dragon', 10)}")

    print("\n=== callable() test ===")
    print(f"Is fireball (function) callable? {callable(fireball)}")
    print(f"Is 'fireball' (string) callable? {callable('fireball')}")
    x = 42
    print(f"Is x (variable) callable? {callable(x)}")
    print(f"Is 42 (integer) callable? {callable(42)}")
