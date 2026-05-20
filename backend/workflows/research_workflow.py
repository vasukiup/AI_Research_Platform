from langgraph.graph import StateGraph, END

from workflows.research_state import ResearchState

from agents.research_agent import ResearchAgent
from agents.factcheck_agent import FactCheckAgent
from agents.synthesis_agent import SynthesisAgent

from services.claim_extractor import ClaimExtractor
from services.status_service import StatusService


research_agent = ResearchAgent()

factcheck_agent = FactCheckAgent()

synthesis_agent = SynthesisAgent()

claim_extractor = ClaimExtractor()


def research_node(state: ResearchState):

    findings = research_agent.execute(
        state["topic"]
    )

    findings = research_agent.execute(
        state["topic"]
    )

    return {
        "findings": findings
    }


def claim_node(state: ResearchState):

    StatusService.set_status(
        "Extracting claims..."
    )
     
    claims = claim_extractor.extract(
        state["findings"]
    )

    return {
        "claims": claims
    }


def factcheck_node(state: ResearchState):

    verified_claims = []

    for claim in state["claims"]:

        verification = (
            factcheck_agent.verify_claim(
                claim
            )
        )

        verified_claims.append(
            verification
        )

    return {
        "verified_claims": verified_claims
    }


def synthesis_node(state: ResearchState):

    report = synthesis_agent.synthesize(

        state["topic"],

        state["verified_claims"]
    )

    return {
        "final_report": report
    }


graph = StateGraph(ResearchState)

graph.add_node(
    "research",
    research_node
)

graph.add_node(
    "claims",
    claim_node
)

graph.add_node(
    "factcheck",
    factcheck_node
)

graph.add_node(
    "synthesis",
    synthesis_node
)

graph.set_entry_point("research")

graph.add_edge(
    "research",
    "claims"
)

graph.add_edge(
    "claims",
    "factcheck"
)

graph.add_edge(
    "factcheck",
    "synthesis"
)

graph.add_edge(
    "synthesis",
    END
)

workflow = graph.compile()