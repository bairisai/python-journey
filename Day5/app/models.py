from dataclasses import dataclass

@dataclass
class Review:
    text: str

@dataclass
class Prediction:
    """
    Sentiment prediction result.
    
    Attributes:
        review (str): The review text being analyzed
        sentiment (str): Classification - "Positive" or "Negative"
        confidence (float): Confidence score between 0.0 and 1.0
    """
    review: str
    sentiment: str
    confidence: float