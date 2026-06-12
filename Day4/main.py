from ai_base import BaseAIModel

# --- 1. INHERITANCE & POLYMORPHISM EXAMPLES ---
class TextSentimentModel(BaseAIModel):
    """1. INHERITANCE: TextSentimentModel 'IS-A' BaseAIModel."""
    def __init__(self, model_name: str, vocabulary_size: int) -> None:
        # Use super() to initialize the parent class attributes
        super().__init__(model_name)
        self.vocab_size: int = vocabulary_size

    def train(self, data: list) -> None:
        """2. POLYMORPHISM: Specific training logic for text data."""
        print(f"Training Text model: {self.model_name} on a Vocabulary size: {self.vocab_size}...")

    def predict(self, input_item):
        """2. POLYMORPHISM: Specific prediction logic for text strings."""
        return f"Text prediction result for '{input_item}' -> Positive"

class ImageDetectionModel(BaseAIModel):
    """1. INHERITANCE: ImageDetectionModel 'IS-A' BaseAIModel."""
    def train(self, data: list) -> None:
        """2. POLYMORPHISM: Specific training logic for matrix pixels."""
        print(f"Training image model '{self.model_name}' using custom pixel matrices...")

    def predict(self, input_item: str) -> str:
        """2. POLYMORPHISM: Specific prediction logic for images."""
        return f"Image prediction result for '{input_item}' -> Object: Cat"

# ---  COMPOSITION EXAMPLE ---

class AIPipeline:
    """
    4. COMPOSITION: This pipeline 'HAS-A' model component inside it.
    It combines independent blocks to make a functioning execution machine.
    """
    def __init__(self, model_component: BaseAIModel) -> None:
        # We inject the model component directly into our pipeline container
        self.model: BaseAIModel = model_component

    def run_inference(self, sample_data: str) -> None:
        print(f"\n Execution pipeline warming up...")
        # Delegation: The pipeline uses its inner component to do the work
        prediction = self.model.predict(sample_data)
        print(prediction)

if __name__ == "__main__":

    nlp_model = TextSentimentModel("SentimentBert", vocabulary_size=50000)
    vision_model = ImageDetectionModel("VisionResNet")

    active_models: list[BaseAIModel] = [nlp_model, vision_model]
    # Show Polymorphism in action using a simple data collection list loop
    for model in active_models:
        # Python calls the correct custom method dynamically on the fly
        model.train(["sample_raw_dataset"])

    text_pipeline = AIPipeline(model_component=nlp_model)
    vision_pipeline = AIPipeline(model_component=vision_model)

    text_pipeline.run_inference("I love learning Python..")
    vision_pipeline.run_inference("raw_image.png")
