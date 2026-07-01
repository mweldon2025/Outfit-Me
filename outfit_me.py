# OutFit-Me: Weather-Based Outfit Recommendation Tool

def get_temperature_category(temperature):
    if temperature >= 85:
        return "hot"
    elif temperature >= 65:
        return "warm"
    elif temperature >= 45:
        return "cool"
    else:
        return "cold"


def recommend_base_outfit(category, occasion):
    outfits = {
        "hot": {
            "casual": "T-shirt, shorts, and sneakers",
            "work": "Light polo, chinos, and loafers",
            "gym": "Athletic shirt, shorts, and trainers"
        },
        "warm": {
            "casual": "Light jacket, jeans, and sneakers",
            "work": "Button-down shirt, slacks, and loafers",
            "gym": "Athletic shirt, joggers, and trainers"
        },
        "cool": {
            "casual": "Sweater, jeans, and boots",
            "work": "Sweater, dress pants, and boots",
            "gym": "Long-sleeve athletic shirt, joggers, and trainers"
        },
        "cold": {
            "casual": "Heavy coat, sweater, jeans, and boots",
            "work": "Coat, sweater, dress pants, and boots",
            "gym": "Thermal athletic wear, running jacket, and trainers"
        }
    }

    return outfits[category][occasion]


def add_weather_items(outfit, weather):
    weather = weather.lower().strip()

    accessories = {
        "sunny": ["Sunglasses"],
        "rain": ["Umbrella", "Rain jacket"],
        "snow": ["Scarf", "Gloves", "Waterproof boots"],
        "windy": ["Windbreaker"]
    }

    if weather in accessories:
        outfit += "\n\nAccessories:"
        for item in accessories[weather]:
            outfit += f"\n- {item}"

    return outfit


def add_preference(outfit, preference):
    preference = preference.lower().strip()

    if preference == "warm":
        outfit += "\n\nTip: Add an extra layer if you usually get cold."
    elif preference == "cool":
        outfit += "\n\nTip: Choose lighter clothing if you tend to get warm."

    return outfit


def validate_temperature(value):
    try:
        return int(value)
    except ValueError:
        return None


def recommend_outfit(temperature, weather, occasion, preference):
    category = get_temperature_category(temperature)
    outfit = recommend_base_outfit(category, occasion)
    outfit = add_weather_items(outfit, weather)
    outfit = add_preference(outfit, preference)

    return outfit


def main():
    print("=" * 45)
    print("        Welcome to OutFit-Me")
    print("=" * 45)

    while True:
        temp_input = input("\nEnter today's temperature (°F): ")
        temperature = validate_temperature(temp_input)

        if temperature is not None:
            break

        print("Please enter a valid number.")

    weather = input(
        "Enter the weather (sunny, rain, snow, windy): "
    ).lower().strip()

    while weather not in ["sunny", "rain", "snow", "windy"]:
        weather = input(
            "Please enter sunny, rain, snow, or windy: "
        ).lower().strip()

    occasion = input(
        "Occasion (casual, work, gym): "
    ).lower().strip()

    while occasion not in ["casual", "work", "gym"]:
        occasion = input(
            "Please enter casual, work, or gym: "
        ).lower().strip()

    preference = input(
        "Do you usually prefer warmer or cooler clothing? (warm/cool): "
    ).lower().strip()

    while preference not in ["warm", "cool"]:
        preference = input(
            "Please enter warm or cool: "
        ).lower().strip()

    recommendation = recommend_outfit(
        temperature,
        weather,
        occasion,
        preference
    )

    print("\n" + "=" * 45)
    print("Recommended Outfit")
    print("=" * 45)
    print(recommendation)


if __name__ == "__main__":
    main()