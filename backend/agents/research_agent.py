from tools.exa_search_tool import ExaSearchTool


class ResearchAgent:

    def __init__(self):

        self.search_tool = ExaSearchTool()

    def execute(self, topic):

        queries = [

            topic,

            f"{topic} trends",

            f"{topic} case studies",

            f"{topic} challenges"
        ]

        findings = []

        for query in queries:

            results = self.search_tool.search(query)

            findings.extend(results)

        return findings