
from config import Config
from logger import logger
from review_service import ReviewService

service = ReviewService()
config = Config()

logger.info("Starting the AI Review Analyzer application...")

print(config.APP_NAME)

result = service.analyze_review("This product is good")

print(f"Review Analysis Result: {result}")

logger.info("Prediction completed successfully.")