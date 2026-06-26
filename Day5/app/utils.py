def clean_text(txt: str):
    return txt.strip().lower()

def count_words(txt: str):
    words = txt.split()
    return len(words)
