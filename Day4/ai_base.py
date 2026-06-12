from abc import ABC, abstractmethod

class BaseAIModel(ABC):
    """
    ABSTRACT BASE CLASS (ABC): Act as a strict interface contract.
    Forces all production models to have 'train' and 'predict' methods.
    """
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    @abstractmethod
    def train(self, data: list) -> None:
        """Enforces implementation of a training loop."""
        pass
    
    @abstractmethod
    def predict(self, input_item: str) -> str:
        """Enforces implementation of an inference pipeline."""
        pass