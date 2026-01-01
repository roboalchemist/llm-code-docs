# Source: https://braintrust.dev/docs/cookbook/recipes/EvalionVoiceAgentEval.md

# Evaluating voice AI agents with Evalion

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/EvalionVoiceAgentEval/EvalionVoiceAgentEvaluation.ipynb) by [Marc Vergara Ferrer](https://www.linkedin.com/in/marc-vergara-b72472144/), [Miguel Andres](https://www.linkedin.com/in/gueles/) on 2024-12-05</div>

[Evalion](https://www.evalion.ai) is a voice-agent evaluation platform that simulates real user interactions and normalizes results across scenarios, enabling teams to detect regressions, compare runs over time, and validate an agent’s readiness for production. Their platform enables teams to test voice agents by creating autonomous testing agents that conduct realistic conversations: interrupting mid-sentence, changing their mind, and expressing frustration just like real customers.

This cookbook demonstrates how to evaluate voice agents by combining Evalion's simulation capabilities with Braintrust. Voice agents require assessment beyond simple text accuracy: they must handle real-time latency constraints (\< 500ms responses), manage interruptions gracefully, maintain context across multi-turn conversations, and deliver natural-sounding interactions.

By the end of this guide, you'll learn how to:

* Create test scenarios in Braintrust datasets
* Orchestrate automated voice simulations with Evalion's API
* Extract and normalize voice-specific metrics (latency, CSAT, goal completion)
* Track evaluation results across iterations

## Prerequisites

* A [Braintrust account](https://www.braintrust.dev/signup) and [API key](https://www.braintrust.dev/app/settings?subroute=api-keys)
* Evalion backend access with API credentials
* Python 3.8+

## Getting started

Export your API keys to your environment:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export BRAINTRUST_API_KEY="YOUR_BRAINTRUST_API_KEY"
export EVALION_API_TOKEN="YOUR_EVALION_API_TOKEN"
export EVALION_PROJECT_ID="YOUR_EVALION_PROJECT_ID"
export EVALION_PERSONA_ID="YOUR_EVALION_PERSONA_ID"
```

Install the required packages:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust httpx pydantic
```

<Callout type="info">
  Best practice is to export your API key as an environment variable. However, to make it easier to follow along with this cookbook, you can also hardcode it into the code below.
</Callout>

Import the required libraries and set up your API credentials:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
import asyncio
import json
import time
import uuid
from typing import Any, Dict, List, Optional
import httpx
import nest_asyncio

from braintrust import init_dataset, EvalAsync, Score

# Uncomment to hardcode your API keys
# os.environ["BRAINTRUST_API_KEY"] = "YOUR_BRAINTRUST_API_KEY"
# os.environ["EVALION_API_TOKEN"] = "YOUR_EVALION_API_TOKEN"
# os.environ["EVALION_PROJECT_ID"] = "YOUR_EVALION_PROJECT_ID"
# os.environ["EVALION_PERSONA_ID"] = "YOUR_EVALION_PERSONA_ID"

BRAINTRUST_API_KEY = os.getenv("BRAINTRUST_API_KEY", "")
EVALION_API_TOKEN = os.getenv("EVALION_API_TOKEN", "")
EVALION_PROJECT_ID = os.getenv("EVALION_PROJECT_ID", "")
EVALION_PERSONA_ID = os.getenv("EVALION_PERSONA_ID", "")

nest_asyncio.apply()
```

## Creating test scenarios

We'll create test scenarios for an airline customer service agent. Each scenario includes the customer's situation (input) and success criteria (expected outcome). These range from straightforward bookings to high-stress cancellation handling. We'll add all the scenarios to a dataset in Braintrust.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Initialize Braintrust
project_name = "Voice Agent Evaluation"
dataset_name = "Customer Service Scenarios"

# Create test scenarios
test_scenarios = [
    {
        "input": "Customer calling to book a flight from New York to Los Angeles for next Tuesday. They want a morning flight and have a budget of $400.",
        "expected": [
            "Agent introduces themselves professionally",
            "Agent confirms the departure city (New York) and destination (Los Angeles)",
            "Agent confirms the date (next Tuesday)",
            "Agent asks about preferred time of day (morning)",
            "Agent presents available flight options within budget",
            "Agent confirms the booking details before finalizing",
        ],
    },
    {
        "input": "Frustrated customer calling because their flight was cancelled. They need to get to Chicago for an important business meeting tomorrow morning.",
        "expected": [
            "Agent shows empathy for the situation",
            "Agent apologizes for the inconvenience",
            "Agent asks for booking reference number",
            "Agent proactively searches for alternative flights",
            "Agent offers multiple rebooking options",
            "Agent provides compensation information if applicable",
        ],
    },
    {
        "input": "Customer wants to change their existing reservation to add extra baggage and select a window seat.",
        "expected": [
            "Agent asks for booking confirmation number",
            "Agent retrieves existing reservation details",
            "Agent explains baggage fees and options",
            "Agent checks seat availability",
            "Agent confirms changes and new total cost",
            "Agent sends confirmation of modifications",
        ],
    },
]

# Create dataset
dataset = init_dataset(project_name, dataset_name)

# Insert test scenarios
for scenario in test_scenarios:
    dataset.insert(**scenario)
```

## Creating scorers

Evalion provides objective metrics (latency, duration) and subjective assessments (CSAT, clarity). We'll normalize all scores to 0-1 for consistent tracking in Braintrust.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def normalize_score(
    score_value: Optional[float], has_succeeded: Optional[bool] = None
) -> Optional[float]:
    """Normalize scores to 0-1 range."""
    if has_succeeded is not None:
        return 1.0 if has_succeeded else 0.0

    if score_value is None:
        return None

    # Normalize 1-10 scale to 0-1
    return max(0.0, min(1.0, score_value / 10.0))


def extract_custom_metrics(output: Dict[str, Any]) -> List[Score]:
    """Extract custom metric scores from simulation results."""
    scores = []
    simulations = output.get("simulations", [])
    if not simulations:
        return scores

    simulation = simulations[0]
    evaluations = simulation.get("evaluations", [])

    for evaluation in evaluations:
        if not evaluation.get("is_applicable", True):
            continue

        metric = evaluation.get("metric", {})
        metric_name = metric.get("name", "unknown")
        measurement_type = metric.get("measurement_type")

        if measurement_type == "boolean":
            score_value = normalize_score(None, evaluation.get("has_succeeded"))
        else:
            score_value = normalize_score(evaluation.get("score"))

        if score_value is not None:
            scores.append(
                Score(
                    name=metric_name,
                    score=score_value,
                    metadata={
                        "reasoning": evaluation.get("reasoning"),
                        "improvement_suggestions": evaluation.get(
                            "improvement_suggestions"
                        ),
                    },
                )
            )

    return scores


def extract_builtin_metrics(output: Dict[str, Any]) -> List[Score]:
    """Extract builtin metric scores from simulation results."""
    scores = []
    simulations = output.get("simulations", [])
    if not simulations:
        return scores

    simulation = simulations[0]
    builtin_evaluations = simulation.get("builtin_evaluations", [])

    for evaluation in builtin_evaluations:
        if not evaluation.get("is_applicable", True):
            continue

        builtin_metric = evaluation.get("builtin_metric", {})
        metric_name = builtin_metric.get("name", "unknown")
        measurement_type = builtin_metric.get("measurement_type")

        # Handle latency specially
        if metric_name == "avg_latency":
            latency_ms = evaluation.get("score")
            if latency_ms is None:
                continue

            # Score based on distance from 1500ms target
            target_latency = 1500
            if latency_ms <= target_latency:
                normalized_score = 1.0
            else:
                normalized_score = max(
                    0.0, 1.0 - (latency_ms - target_latency) / target_latency
                )

            scores.append(
                Score(
                    name="avg_latency_ms",
                    score=normalized_score,
                    metadata={
                        "actual_latency_ms": latency_ms,
                        "target_latency_ms": target_latency,
                        "is_within_target": latency_ms <= target_latency,
                    },
                )
            )
            continue

        if measurement_type == "boolean":
            score_value = normalize_score(None, evaluation.get("has_succeeded"))
        else:
            score_value = normalize_score(evaluation.get("score"))

        if score_value is not None:
            scores.append(
                Score(
                    name=metric_name,
                    score=score_value,
                    metadata={"reasoning": evaluation.get("reasoning")},
                )
            )

    return scores
```

## Evalion API integration

The `EvalionAPIService` class handles all interactions with Evalion's API for creating agents, test setups, and running simulations. The task function orchestrates the workflow: creating agents in Evalion, running simulations, and extracting results. This enables reproducible evaluation across iterations.

The function performs the following steps:

1. Creates a hosted agent in Evalion with your prompt
2. Sets up test scenarios and personas
3. Runs the voice simulation
4. Polls for completion and retrieves results
5. Cleans up temporary resources

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
class EvalionAPIService:
    """Service class for interacting with the Evalion API."""

    def __init__(
        self, base_url: str = "https://api.evalion.ai/api/v1", api_token: str = ""
    ):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_token}"}

    async def create_hosted_agent(
        self, prompt: str, name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a hosted agent with the given prompt."""
        if not name:
            name = f"Voice Agent - {uuid.uuid4()}"

        payload = {
            "name": name,
            "description": "Agent created for evaluation",
            "agent_type": "outbound",
            "prompt": prompt,
            "is_active": True,
            "speaks_first": False,
            "llm_provider": "openai",
            "llm_model": "gpt-4o-mini",
            "llm_temperature": 0.7,
            "tts_provider": "elevenlabs",
            "tts_model": "eleven_turbo_v2_5",
            "tts_voice": "5IDdqnXnlsZ1FCxoOFYg",
            "stt_provider": "openai",
            "stt_model": "gpt-4o-mini-transcribe",
            "language": "en",
            "max_conversation_time_in_minutes": 5,
            "llm_max_tokens": 800,
        }

        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{self.base_url}/hosted-agents",
                headers=self.headers,
                json=payload,
            )
            response.raise_for_status()
            return response.json()

    async def delete_hosted_agent(self, hosted_agent_id: str) -> None:
        """Delete a hosted agent."""
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.delete(
                f"{self.base_url}/hosted-agents/{hosted_agent_id}",
                headers=self.headers,
            )
            response.raise_for_status()

    async def create_agent(
        self,
        project_id: str,
        hosted_agent_id: str,
        prompt: str,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create an agent that references a hosted agent."""
        if not name:
            name = f"Test Agent {int(time.time())}"

        payload = {
            "name": name,
            "description": "Agent for evaluation testing",
            "agent_type": "inbound",
            "interaction_mode": "voice",
            "integration_type": "phone",
            "language": "en",
            "speaks_first": False,
            "prompt": prompt,
            "is_active": True,
            "hosted_agent_id": hosted_agent_id,
            "project_id": project_id,
        }

        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{self.base_url}/projects/{project_id}/agents",
                headers=self.headers,
                json=payload,
            )
            response.raise_for_status()
            return response.json()

    async def delete_agent(self, project_id: str, agent_id: str) -> None:
        """Delete an agent."""
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.delete(
                f"{self.base_url}/projects/{project_id}/agents/{agent_id}",
                headers=self.headers,
            )
            response.raise_for_status()

    async def create_test_set(
        self, project_id: str, name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a test set."""
        if not name:
            name = f"Test Set {int(time.time())}"

        payload = {
            "name": name,
            "description": "Test set for evaluation",
            "project_id": project_id,
        }

        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{self.base_url}/projects/{project_id}/test-sets",
                headers=self.headers,
                json=payload,
            )
            response.raise_for_status()
            return response.json()

    async def delete_test_set(self, project_id: str, test_set_id: str) -> None:
        """Delete a test set."""
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.delete(
                f"{self.base_url}/projects/{project_id}/test-sets/{test_set_id}",
                headers=self.headers,
            )
            response.raise_for_status()

    async def create_test_case(
        self, project_id: str, test_set_id: str, scenario: str, expected_outcome: str
    ) -> Dict[str, Any]:
        """Create a test case."""
        payload = {
            "name": f"Test Case {int(time.time())}",
            "description": "Test case for evaluation",
            "scenario": scenario,
            "expected_outcome": expected_outcome,
            "test_set_id": test_set_id,
        }

        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{self.base_url}/projects/{project_id}/test-cases",
                headers=self.headers,
                json=payload,
            )
            response.raise_for_status()
            return response.json()

    async def create_test_setup(
        self,
        project_id: str,
        agent_id: str,
        persona_id: str,
        test_set_id: str,
        metrics: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Create a test setup."""
        payload = {
            "name": f"Test Setup {int(time.time())}",
            "description": "Test setup for evaluation",
            "project_id": project_id,
            "agents": [agent_id],
            "personas": [persona_id],
            "test_sets": [test_set_id],
            "metrics": metrics or [],
            "testing_mode": "voice",
        }

        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{self.base_url}/test-setups",
                headers=self.headers,
                json=payload,
            )
            response.raise_for_status()
            return response.json()

    async def delete_test_setup(self, project_id: str, test_setup_id: str) -> None:
        """Delete a test setup."""
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.delete(
                f"{self.base_url}/test-setups/{test_setup_id}?project_id={project_id}",
                headers=self.headers,
            )
            response.raise_for_status()

    async def run_test_setup(self, project_id: str, test_setup_id: str) -> str:
        """Prepare and run a test setup."""
        # First prepare
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{self.base_url}/test-setup-runs/prepare",
                headers=self.headers,
                json={"project_id": project_id, "test_setup_id": test_setup_id},
            )
            response.raise_for_status()
            test_setup_run_id = response.json()["test_setup_run_id"]

        # Then run
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{self.base_url}/test-setup-runs/{test_setup_run_id}/run",
                headers=self.headers,
                json={"project_id": project_id},
            )
            response.raise_for_status()

        return test_setup_run_id

    async def poll_for_completion(
        self, project_id: str, test_setup_run_id: str, max_wait: int = 600
    ) -> Optional[Dict[str, Any]]:
        """Poll for simulation completion."""
        start_time = time.time()

        while time.time() - start_time < max_wait:
            async with httpx.AsyncClient(timeout=300.0) as client:
                response = await client.get(
                    f"{self.base_url}/test-setup-runs/{test_setup_run_id}/simulations",
                    headers=self.headers,
                    params={"project_id": project_id},
                )

                if response.status_code == 200:
                    data = response.json()
                    simulations = data.get("data", [])

                    if simulations:
                        sim = simulations[0]
                        status = sim.get("run_status")

                        if status in ["COMPLETED", "FAILED"]:
                            return sim

            await asyncio.sleep(5)

        return None
```

Then, we'll define the agent prompt that will be evaluated:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Define the agent prompt to evaluate
AGENT_PROMPT = """
You are a professional travel agent assistant. Your role is to help customers with:
- Booking flights
- Modifying existing reservations
- Handling cancellations and rebooking
- Answering questions about flights and policies

Guidelines:
- Always introduce yourself at the beginning of the call
- Be empathetic, especially with frustrated customers
- Confirm all details before making changes
- Provide clear pricing information
- Thank the customer at the end of the call
"""
```

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
async def run_evaluation_task(input: Dict[str, Any] | str) -> Dict[str, Any]:
    """Main task function that orchestrates the evaluation workflow."""

    # Extract scenario and expected outcome from input
    if isinstance(input, dict):
        scenario = input.get("scenario", "")
        expected_list = input.get("expected", [])
        expected_outcome = (
            "\n".join(expected_list)
            if isinstance(expected_list, list)
            else str(expected_list)
        )
    elif isinstance(input, str):
        scenario = input
        expected_outcome = ""

    # Initialize Evalion API service
    api_service = EvalionAPIService(
        base_url="https://api.evalion.ai/api/v1", api_token=EVALION_API_TOKEN
    )

    # Store resource IDs for cleanup
    hosted_agent_id = None
    agent_id = None
    test_set_id = None
    test_setup_id = None

    try:
        # Create hosted agent
        hosted_agent = await api_service.create_hosted_agent(
            prompt=AGENT_PROMPT, name="Travel Agent Eval"
        )
        hosted_agent_id = hosted_agent["id"]

        # Create agent
        agent = await api_service.create_agent(
            project_id=EVALION_PROJECT_ID,
            hosted_agent_id=hosted_agent_id,
            prompt=AGENT_PROMPT,
        )
        agent_id = agent["id"]

        # Create test set
        test_set = await api_service.create_test_set(project_id=EVALION_PROJECT_ID)
        test_set_id = test_set["id"]

        # Create test case
        await api_service.create_test_case(
            project_id=EVALION_PROJECT_ID,
            test_set_id=test_set_id,
            scenario=scenario,
            expected_outcome=expected_outcome,
        )

        # Create test setup
        test_setup = await api_service.create_test_setup(
            project_id=EVALION_PROJECT_ID,
            agent_id=agent_id,
            persona_id=EVALION_PERSONA_ID,
            test_set_id=test_set_id,
            metrics=None,
        )
        test_setup_id = test_setup["id"]

        # Run test setup
        test_setup_run_id = await api_service.run_test_setup(
            project_id=EVALION_PROJECT_ID, test_setup_id=test_setup_id
        )

        # Poll for completion
        simulation = await api_service.poll_for_completion(
            project_id=EVALION_PROJECT_ID, test_setup_run_id=test_setup_run_id
        )

        # Clean up Evalion resources
        if test_setup_id:
            await api_service.delete_test_setup(EVALION_PROJECT_ID, test_setup_id)
        if agent_id:
            await api_service.delete_agent(EVALION_PROJECT_ID, agent_id)
        if test_set_id:
            await api_service.delete_test_set(EVALION_PROJECT_ID, test_set_id)
        if hosted_agent_id:
            await api_service.delete_hosted_agent(hosted_agent_id)

        if not simulation:
            return {"success": False, "error": "Simulation timed out", "transcript": ""}

        # Return results
        return {
            "success": True,
            "transcript": simulation.get("transcript", ""),
            "simulations": [simulation],
        }

    except Exception as e:
        return {"success": False, "error": str(e), "transcript": ""}
```

Finally, we'll run the evaluation with Braintrust:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Run the evaluation
await EvalAsync(
    "Voice Agent Evaluation",
    data=dataset,
    task=run_evaluation_task,
    scores=[
        extract_custom_metrics,
        extract_builtin_metrics,
    ],
    parameters={
        "main": {
            "type": "prompt",
            "description": "Prompt to be tested by Evalion simulations",
            "default": {
                "prompt": {
                    "type": "chat",
                    "messages": [
                        {
                            "role": "system",
                            "content": AGENT_PROMPT,
                        }
                    ],
                },
                "options": {"model": "gpt-4o"},
            },
        },
    },
)
```

## Analyzing results

After running evaluations, navigate to **Experiments** in Braintrust to analyze your results. You'll see metrics like average latency, CSAT scores, and goal completion rates across all test scenarios.

<img src="https://mintcdn.com/braintrust/qoil-xuAuRRMU5aj/cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png?fit=max&auto=format&n=qoil-xuAuRRMU5aj&q=85&s=b2925f61b769e5d9e422eb5d00e03bec" alt="braintrust-results.png" data-og-width="2554" width="2554" data-og-height="1846" height="1846" data-path="cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/qoil-xuAuRRMU5aj/cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png?w=280&fit=max&auto=format&n=qoil-xuAuRRMU5aj&q=85&s=04af19867ccbd60525262ae508ace65a 280w, https://mintcdn.com/braintrust/qoil-xuAuRRMU5aj/cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png?w=560&fit=max&auto=format&n=qoil-xuAuRRMU5aj&q=85&s=bf7357390b51c90f97bbdc36698133bc 560w, https://mintcdn.com/braintrust/qoil-xuAuRRMU5aj/cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png?w=840&fit=max&auto=format&n=qoil-xuAuRRMU5aj&q=85&s=e03b07dc9b1dc7c80761fc33764353cd 840w, https://mintcdn.com/braintrust/qoil-xuAuRRMU5aj/cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png?w=1100&fit=max&auto=format&n=qoil-xuAuRRMU5aj&q=85&s=4cbd5f24cc912b525d410de93cd000ef 1100w, https://mintcdn.com/braintrust/qoil-xuAuRRMU5aj/cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png?w=1650&fit=max&auto=format&n=qoil-xuAuRRMU5aj&q=85&s=d4fa548b11f6082c1caa53664c4966c9 1650w, https://mintcdn.com/braintrust/qoil-xuAuRRMU5aj/cookbook/assets/EvalionVoiceAgentEval/braintrust-results.png?w=2500&fit=max&auto=format&n=qoil-xuAuRRMU5aj&q=85&s=4466798ef7d70952fdfe3736af76549d 2500w" />

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Example of what the results look like
example_results = {
    "scenario": "Customer calling to book a flight from New York to Los Angeles",
    "scores": {
        "Expected Outcome": 0.9,
        "conversation_flow": 0.85,
        "empathy": 0.92,
        "clarity": 0.88,
        "avg_latency_ms": 0.95,  # 1450ms actual, target 1500ms
    },
    "metadata": {
        "transcript_length": 450,
        "duration_seconds": 180,
    },
}

print(json.dumps(example_results, indent=2))
```

## Next steps

Now that you have a working evaluation pipeline, you can:

1. **Expand test coverage**: Add more scenarios covering edge cases
2. **Iterate on prompts**: Adjust your agent's prompt and compare results
3. **Monitor production**: Set up online evaluation for live traffic
4. **Track trends**: Use Braintrust's experiment comparison to identify improvements

For more agent cookbooks, check out:

* [Evaluating a voice agent](/cookbook/recipes/VoiceAgent) with OpenAI Realtime API
* [Building reliable AI agents](/cookbook/recipes/AgentWhileLoop) with tool calling


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt