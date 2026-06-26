from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Prediction started...")
        result = func(*args, **kwargs)
        print("Prediction Ended...")
        return result

    return wrapper