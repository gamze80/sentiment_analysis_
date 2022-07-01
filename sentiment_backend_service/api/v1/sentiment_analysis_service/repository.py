from sentiment_backend_service.api.v1.sentiment_analysis_service.sentiment_analyzer.model import model
from sentiment_backend_service.models.analysis import SentimentRequest, SentimentResponse


class AnalysisRepository:
    def predict(request:SentimentRequest):
        sentiment, confidence, probabilities = model.predict(request.text)
        return SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)


