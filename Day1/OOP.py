""" 
A Class is just a code blueprint.
It doesn't create a character yet; it just defines what data a character will have (Attributes) 
and what actions they can take (Methods).
 
"""

class HousingPriceModel:
    # 1. The Constructor: Setup the model's settings (Hyperparameters)
    def __init__(self, learning_rate):
        self.lr = learning_rate
        self.is_trained = False
    # 2. Method 1: The action to train the AI on data
    def train(self, data):
        print(f"Training the AI using a learning rate of {self.lr}.")
        self.is_trained = True
        print("Traning Complete!")
    # 3. Method 2: The action to make a prediction
    def predict(self, house_size):
        if not self.is_trained:
            return "Error, please train the model first"
        # Simple dummy math to simulate a prediction
        estimated_price = house_size * 300
        return f"Estimated price: ${estimated_price}"
    
if __name__ == "__main__":
    # Creating the actual objects using the blueprint
    model_a = HousingPriceModel(learning_rate=0.1)
    model_a.train("Housing_data.csv")
    print(model_a.predict(1500))

    model_b = HousingPriceModel(learning_rate=0.01)
    model_b.train("Housing_data.csv")
    print(model_b.predict(2000))

