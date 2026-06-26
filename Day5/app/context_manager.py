class AIModel:
    def __enter__(self):
        print("Loading AI Model...")
        print("AI Model Loaded...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing AI Model...")
        return False
    