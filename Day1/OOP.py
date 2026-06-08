""" 
A Class is just a code blueprint.
It doesn't create a character yet; it just defines what data a character will have (Attributes) 
and what actions they can take (Methods).
 
"""

class GameCharacter:
    # 1. The Constructor: This defines what info EVERY character needs when born
    def __init__(self, character_name, special_power):
        self.character_name = character_name
        self.special_power = special_power
        self.health = 100
    # 2. A Method: This is just a function inside a class that represents an action
    def introduce(self):
        print(f"Hi! I am {self.character_name} and my power is {self.special_power}.")
    
if __name__ == "__main__":
    # Creating the actual objects using the blueprint
    player_one = GameCharacter("Wizard Wayne", "Fireballs")
    player_two = GameCharacter("Knight Kelly", "Shield Bash")
    # Now we tell them to perform an action using their methods
    player_one.introduce()
    player_two.introduce()

