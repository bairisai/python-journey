class ReviewService:

    def analyze_review(self, review):

        review = review.lower()

        if "good" in review:
            return "Positive"

        return "Negative"