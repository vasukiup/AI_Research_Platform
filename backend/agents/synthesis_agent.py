from services.llm_service import LLMService


class SynthesisAgent:

    def __init__(self):

        self.llm = LLMService()

    def synthesize(
        self,
        topic,
        verified_claims
    ):

        findings_text = ""

        for item in verified_claims:

            findings_text += (
                f"Claim: {item['claim']}\n"
            )

            findings_text += (
                f"Confidence: "
                f"{item['confidence']}\n"
            )

            findings_text += "Sources:\n"

            for source in item["sources"]:

                findings_text += (
                    f"- {source['title']} "
                    f"({source['url']})\n"
                )

            findings_text += "\n"

        prompt = f"""
You are an expert research analyst.

Create a professional AI research report.

Topic:
{topic}

Verified Findings:
{findings_text}

Requirements:

1. Use ONLY verified findings
2. Maintain factual accuracy
3. Reference supporting sources naturally
4. Create:
   - Executive Summary
   - Key Insights
   - Industry Analysis
   - Challenges
   - Recommendations
   - Future Outlook
   - Conclusion
5. Add a References section

Write in a professional consulting style.
"""

        return self.llm.generate(prompt)