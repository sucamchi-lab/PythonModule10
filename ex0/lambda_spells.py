def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sorts a list of artifacts by their power in descending order."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filters a list of mages by their power."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transforms a list of spells by adding asterisks around each spell."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculates max power, min power and average (int, int, float)."""
    return {
        'max_power': int(max(mages, key=lambda m: m['power'])['power']),
        'min_power': int(min(mages, key=lambda m: m['power'])['power']),
        'avg_power': round(sum(m['power'] for m in mages) / len(mages), 2)
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'divination'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'combat'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'stealth'},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before"
        f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    spells = ["fireball", "heal", "shield"]
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))
