class ReviewIter:
    def __init__(self, reviews):
        self.reviews = reviews
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.reviews):
            review = self.reviews[self.index]
            self.index += 1
            return review
        else:
            raise StopIteration