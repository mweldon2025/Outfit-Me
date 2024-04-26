# Outfit-Me

class OutfitRecommendationSystem:
    def __init__(self, weather, preferences):
        self.weather = weather
        self.preferences = preferences

  def suggest_outfit(self):
      #Weather-based outfit suggestions
    if self.weather == "sunny":
        outfit = self.suggest_sunny_outfit()
    elif self.weather == "rainy":
        outfit = self.suggest_rainy_outfit()
    elif self.weather == "cold":
        outfit = self.suggest_cold_outfit()
    else:
        outfit = "Weather information unavailable"
            
    return outfit
        
def suggest_sunny_outfit(self):
        #Outfit suggestiona for warm weather
        tops = ["t-shirt", "tank top", "blouse"]
        bottoms = ["shorts", "skirt", "light trousers"]
        footwear = ["sandals", "sneakers", "flip flops"]
        
outfit = {
            "top": random.choice(tops),
            "bottom": random.choice(bottoms),
            "footwear": random.choice(footwear),
            "accessories": self.preferences.get("accessories", "Sunglasses")
