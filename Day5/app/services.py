from .decorators import logger

@logger
def predict(review):
    print(f"Prediction for the review: {review} is Positive")

