import sentiment_backend_service.settings

import uvicorn
from fastapi import FastAPI

from sentiment_backend_service.api.v1.book_service.router import BookRouter
from sentiment_backend_service.api.v1.sentiment_analysis_service.router import AnalysisRouter

VERSION = "1.0.0"

app = FastAPI(
    title="Backend Service",
    version=VERSION,
    description="Backend service developed using fastapi",
)

sub_app = FastAPI(
    title="Backend Service",
    version=VERSION,
    description="Backend service developed using fastapi",
    docs_url="/docs",
    openapi_url="/openapi.json",
)
sub_app2 = FastAPI(
    title="Sentiment Analysis",
    version=VERSION,
    description="Backend service developed using fastapi for sentiment analysis",
    docs_url="/docs",
    openapi_url="/openapi.json",
)
sub_app.include_router(BookRouter().get_router(), prefix="/book_service")
sub_app2.include_router(AnalysisRouter().get_router(), prefix="/sentiment analysis")
app.mount("/v1/sentiment_backend", sub_app)
app.mount("/v1/Analysis", sub_app2)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
