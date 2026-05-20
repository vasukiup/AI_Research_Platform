from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.report_service import ReportService
from services.status_service import StatusService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

report_service = ReportService()


class ReportRequest(BaseModel):

    topic: str


@app.get("/")
def home():

    return {
        "status": "running"
    }


@app.post("/generate-report")
def generate_report(request: ReportRequest):

    report = report_service.generate(
        request.topic
    )

    return {
        "report": report
    }

@app.get("/workflow-status")
def workflow_status():

    return StatusService.get_status()