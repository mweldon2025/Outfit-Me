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


def recommend_base_outfit(category):
    outfits = {
        "hot": "T-shirt, shorts, and sneakers",
        "warm": "Light jacket, jeans, and sneakers",
        "cool": "Sweater, jeans, and boots",
        "cold": "Heavy coat, scarf, gloves, and boots"
    }

    return outfits[category]


def add_weather_items(outfit, weather):
    weather = weather.lower().strip()

    if weather == "rain":
        outfit += " + umbrella or rain jacket"
    elif weather == "snow":
        outfit += " + warm socks and waterproof boots"
    elif weather == "windy":
        outfit += " + windbreaker"
    elif weather == "sunny":
        outfit += " + sunglasses"

    return outfit


def validate_temperature(user_input):
    try:
        temperature = int(user_input)
        return temperature
    except ValueError:
        return None


def recommend_outfit(temperature, weather):
    category = get_temperature_category(temperature)
    outfit = recommend_base_outfit(category)
    final_outfit = add_weather_items(outfit, weather)

    return final_outfit


def main():
    print("Welcome to OutFit-Me!")
    print("Get an outfit recommendation based on temperature and weather.\n")

    temp_input = input("Enter today's temperature: ")
    temperature = validate_temperature(temp_input)

    if temperature is None:
        print("Invalid temperature. Please enter a number.")
        return

    weather = input("Enter the weather condition (sunny, rain, snow, windy): ")

    recommendation = recommend_outfit(temperature, weather)

    print("\nRecommended Outfit:")
    print(recommendation)


if __name__ == "__main__":
    main()