#Basic Sentiment Analysis System.
reviews = [
    "I absolutely love this new software, it is amazing!",
    "This is the worst experience I have ever had.",
    "The weather today is cloudy and quite normal.",
    "Fantastic customer service, I am highly satisfied!",
    "It is okay, nothing special but it works."
]

# Dictionaries mapping specific words to a dummy relevance score (or just presence)
positive_words = {"love": 1, "amazing": 1, "fantastic": 1, "satisfied": 1}
negative_words = {"worst": 1, "terrible": 1, "bad": 1, "hate": 1}

def analyze_sentiment(text):
    # 1. Clean the text: convert to lowercase so matching isn't case-sensitive
    cleaned_text = text.lower()
    # 2. Split the sentence into individual words (a list of words)
    words = cleaned_text.split()
    # 3. Track the emotional score of the sentence
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in  negative_words:
            score -= 1
    
    # 4. Determine the final label based on the score
    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    # 5. Return the result structured as a dictionary
    return {"text": text, "score": score, "sentiment": sentiment}

if __name__ == "__main__":
    ai_results = []
    for review in reviews:
        analysis = analyze_sentiment(review)

        ai_results.append(analysis)
    
    for result in ai_results:
        print(f"Review: {result['text']}")
        print(f"Sentiment: {result['sentiment']} (Score: {result['score']})\n")

