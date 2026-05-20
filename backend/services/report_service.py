from workflows.research_workflow import workflow


class ReportService:

    def generate(self, topic):

        result = workflow.invoke({

            "topic": topic
        })

        return result["final_report"]