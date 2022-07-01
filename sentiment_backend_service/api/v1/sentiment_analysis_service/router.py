from sentiment_backend_service.interfaces.generic_router import GenericRouter
from sentiment_backend_service.models.analysis import SentimentRequest, SentimentResponse
from .repository import AnalysisRepository



class AnalysisRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind_routes()

    def bind_routes(self):
        self.get_router().post("/predict", response_model=SentimentResponse, tags=["Predict Text"])(self.predict)

    def predict(self,
                request: SentimentRequest):
        return AnalysisRepository.predict(request)

