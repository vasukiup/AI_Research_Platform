from tools.exa_search_tool import ExaSearchTool


class FactCheckAgent:

    def __init__(self):

        self.search_tool = ExaSearchTool()

    def verify_claim(self, claim):

        query = f"Evidence supporting: {claim}"

        results = self.search_tool.search(
            query,
            num_results=3
        )

        confidence = self.calculate_confidence(
            results
        )

        return {

    "claim": claim,

    "verified": confidence > 0.6,

    "confidence": confidence,

    "sources": [

        {
            "title": source["title"],
            "url": source["url"]
        }

        for source in results
    ]
}
    def calculate_confidence(self, results):

        count = len(results)

        if count >= 3:
            return 0.9

        elif count == 2:
            return 0.75

        return 0.5