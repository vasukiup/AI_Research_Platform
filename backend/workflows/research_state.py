from typing import TypedDict, List


class ResearchState(TypedDict):

    topic: str

    findings: List

    claims: List

    verified_claims: List

    final_report: str