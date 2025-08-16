from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",  # specify model
    device=-1  # CPU, or 0 for GPU if available
)

# Initialize sentiment analysis pipeline (uses free distilbert-base model)
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_message(message: str):
    """Return sentiment label and score for a donor message."""
    if not message:
        return None
    result = sentiment_analyzer(message)[0]  # returns dict with 'label' and 'score'
    return result
