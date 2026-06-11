from config_module import Hyperparameters

class SentimentModel:
    #Class Attribute: Every model instance shares this framework configuration
    ai_framework: str = "PyTorch Enterprise V3"

    def __init__(self, model_name: str, settings: Hyperparameters) -> None:
        # Instance Attributes: Isolated unique configurations per object
        self.name: str = model_name
        self.config: Hyperparameters = settings
        self.is_trained: bool = False
    
    def train(self) -> None:
        """Simulates training the model using the imported configuration data."""
        print(f"Training started for model: {self.name}")
        print(f"Hyperparameters -> LR: {self.config.learning_rate} | Batch size: {self.config.batch_size}")
        self.is_trained = True
        print("Training completed!")

if __name__ == "__main__":
    careful_settings = Hyperparameters(learning_rate=0.001, batch_size=32, epochs=10)
    aggressive_settings = Hyperparameters(learning_rate=0.1, batch_size=64, epochs=50)

    model_alpha = SentimentModel(model_name="Alpha", settings=careful_settings)
    model_beta = SentimentModel(model_name="Beta", settings=aggressive_settings)

    model_alpha.train()
    model_beta.train()

     # Proof of shared vs isolated attributes:
    print(f"Global Framework check (Class level): {model_alpha.ai_framework} == {model_beta.ai_framework}")
    print(f"Name Isolation check(Instance Level): {model_alpha.name} vs {model_beta.name}")