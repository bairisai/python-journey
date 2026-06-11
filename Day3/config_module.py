from dataclasses import dataclass

@dataclass
class Hyperparameters:
    learning_rate: float
    batch_size: int
    epochs: int
    optimizer_name: str = "Adam"