# Outfit-Me
An application that will help indecisive users choose outfits based on personal preferences and weather. 
class OutfitRecommendationSystem:
    def __init__(self, weather, preferences):
        self.weather = weather
        self.preferences = preferences

  def suggest_outfit(self):
        if self.weather == "sunny":
            outfit = self.suggest_sunny_outfit()
        elif self.weather == "rainy":
            outfit = self.suggest_rainy_outfit()
        elif self.weather == "cold":
            outfit = self.suggest_cold_outfit()
        else:
            outfit = "Weather information not available"
