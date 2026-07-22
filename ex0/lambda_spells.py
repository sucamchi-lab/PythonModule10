"""
This exercise focuses on using lambda functions.
Lambda functions are anonymous functions that make code more concise.
They are ideal for simple, one-off operations
that can be defined in a single line.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power in descending order."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter a list of mages by their power."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform a list of spells by adding asterisks around each spell."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate max power, min power and average (int, int, float)."""
    return (lambda pow: {
        'max_power': max(pow),
        'min_power': min(pow),
        'avg_power': float(sum(pow) / len(pow))
    })([m['power'] for m in mages])


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'divination'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'combat'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'stealth'},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before"
        f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    spells = ["fireball", "heal", "shield"]
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    mages = [
        {'name': 'Merlin', 'power': 95},
        {'name': 'Gandalf', 'power': 88},
        {'name': 'Radagast', 'power': 72},
    ]
    print("\nTesting power filter (min_power=80)...")
    over_80 = power_filter(mages, 80)
    for m in over_80:
        print(f"{m['name']} ({m['power']} power)")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"max_power: {stats['max_power']}, "
        f"min_power: {stats['min_power']}, "
        f"avg_power: {stats['avg_power']}"
    )
