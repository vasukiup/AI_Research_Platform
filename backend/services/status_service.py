workflow_status = {
    "status": "idle"
}


class StatusService:

    @staticmethod
    def set_status(status):

        workflow_status["status"] = status

    @staticmethod
    def get_status():

        return workflow_status