def validate_character(data):
    required = ["name","skin_color","race","strength","agility","magic","knowledge"]
    for f in required:
        if f not in data:
            return f"Missing field: {f}"

    for stat in ["strength","agility","magic","knowledge"]:
        if not isinstance(data[stat], int) or data[stat] < 0 or data[stat] > 100:
            return f"{stat} must be between 0 and 100"

    return None
