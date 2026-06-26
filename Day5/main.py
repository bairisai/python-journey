from app.decorators import logger
from app.models import Prediction
from app.services import predict
from app.utils import clean_text, count_words
from app.iterator import ReviewIter
from app.context_manager import AIModel


@logger
def main():
    """Main function that calls all modules."""
    
    # Use services module
    print("1. Using Services Module (Decorator + Prediction):")
    predict("This product is amazing!")
    
    # Use utils module
    print("\n2. Using Utils Module:")
    review = "  Great quality and fast shipping  "
    cleaned = clean_text(review)
    word_count = count_words(cleaned)
    print(f"Original: '{review}'")
    print(f"Cleaned: '{cleaned}'")
    print(f"Word Count: {word_count}")
    
    # Use models module
    print("\n3. Using Models Module (Prediction Dataclass):")
    prediction = Prediction(
        review="excellent service",
        sentiment="Positive",
        confidence=0.95
    )
    print(f"Full Prediction: {prediction}")
    print(f"  Review: {prediction.review}")
    print(f"  Sentiment: {prediction.sentiment}")
    print(f"  Confidence: {prediction.confidence}")
    
    # Use iterator module
    reviews = ["Great product!", "Not satisfied", "Excellent!"]
    for review in ReviewIter(reviews):
        print(f"  - {review}")
    
    # Use context manager module
    with AIModel() as model:
        print("  Analyzing with AI Model...")
        prediction = Prediction(
            review="fantastic experience",
            sentiment="Positive",
            confidence=0.98
        )
        print(f"  Result: {prediction}")


if __name__ == "__main__":
    main()
