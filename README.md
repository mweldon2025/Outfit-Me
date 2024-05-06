# Outfit-Me

class OutfitRecommendationSystem:
    def __init__(self, weather, preferences):
        self.weather = weather
        self.preferences = preferences

 def pick_outfit(self):
        if "sunny" in self.weather.lower():
            return random.choice(["Shorts and T-shirt", "Sundress", "Light blouse and jeans"])
        elif "rainy" in self.weather.lower():
            return random.choice(["Raincoat and boots", "Umbrella and waterproof jacket", "Jeans and rain boots"])
        elif "windy" in self.weather.lower():
            return random.choice(["Windbreaker jacket", "Long sleeve shirt and jeans", "Scarf and sweater"])
        elif "cold" in self.weather.lower():
            return random.choice(["Coat and scarf", "Sweater and jeans", "Thick jacket and gloves"])
        else:
            return "Sorry, I couldn't find suitable outfit recommendation for this weather."

def get_weather_from_user():
    while True:
        weather = input("Enter the current weather condition (e.g., sunny, rainy, windy, cold): ")
        if weather.lower() in ["sunny", "rainy", "windy", "cold"]:
            return weather
        else:
            print("Invalid weather condition. Please enter sunny, rainy, windy, or cold.")

if __name__ == "__main__":
    print("Welcome to the Outfit Picker App!")
    print("I can help you choose an outfit based on the weather conditions.")
    
  
