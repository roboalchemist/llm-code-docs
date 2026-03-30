# Source: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent

Title: Evaluate your AI agents - Microsoft Foundry

URL Source: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent

Markdown Content:
Evaluation is essential for ensuring your agent meets quality and safety standards before deployment. By running evaluations during development, you establish a baseline for your agent's performance and can set acceptance thresholds, such as an 85% task adherence passing rate, before releasing it to users.

In this article, you learn how to run an agent-targeted evaluation against a [Foundry agent](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) using built-in evaluators for quality, safety, and agent behavior. Specifically, you:

*   Set up the SDK client for evaluation.
*   Choose evaluators for quality, safety, and agent behavior.
*   Create a test dataset and run an evaluation.
*   Interpret results and integrate them into your workflow.

Tip

For general-purpose evaluation of generative AI models and applications, including custom evaluators, different data sources, and additional SDK options, see [Run evaluations from the SDK](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation).

*   A [Foundry project](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-projects) with an [agent](https://learn.microsoft.com/en-us/azure/foundry/agents/overview).
*   An Azure OpenAI deployment with a GPT model that supports chat completion (for example, `gpt-4o` or `gpt-4o-mini`).
*   **Azure AI User** role on the Foundry project.

Note

Some evaluation features have regional restrictions. See [supported regions](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/risk-safety-evaluators#foundry-project-configuration-and-region-support) for details.

Install the Foundry SDK and set up authentication:

```
pip install "azure-ai-projects>=2.0.0"
```

Create the project client. The following code samples assume you run them in this context:

```
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
model_deployment = os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]

credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint=endpoint, credential=credential)
client = project_client.get_openai_client()
```

Evaluators are functions that assess your agent's responses. Some evaluators use AI models as judges, while others use rules or algorithms. For agent evaluation, consider this set:

| Evaluator | What it measures |
| --- | --- |
| **Task Adherence** | Does the agent follow its system instructions? |
| **Coherence** | Is the response logical and well-structured? |
| **Violence** | Does the response contain violent content? |

For more built-in evaluators, see:

*   [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) - Tool Call Accuracy, Intent Resolution
*   [Quality evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/general-purpose-evaluators) - Fluency, Relevance, Groundedness
*   [Text similarity evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/textual-similarity-evaluators) - F1 Score, BLEU, ROUGE
*   [Safety evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/risk-safety-evaluators) - Hate, Self-Harm, Sexual Content

To build your own evaluators, see [Custom evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/custom-evaluators).

Create a JSONL file with test queries for your agent. Each line contains a JSON object with a `query` field:

```
{"query": "What's the weather in Seattle?"}
{"query": "Book a flight to Paris"}
{"query": "Tell me a joke"}
```

Upload this file as a dataset in your project:

```
dataset = project_client.datasets.upload_file(
    name="agent-test-queries",
    version="1",
    file_path="./test-queries.jsonl",
)
```

When you run an evaluation, the service sends each test query to your agent, captures the response, and applies your selected evaluators to score the results.

First, configure your evaluators. Each evaluator needs a data mapping that tells it where to find inputs:

*   `{{item.X}}` references fields from your test data, like `query`.
*   `{{sample.output_items}}` references the full agent response, including tool calls.
*   `{{sample.output_text}}` references just the response message text.

AI-assisted evaluators, like Task Adherence and Coherence, require a model deployment in `initialization_parameters`. Some evaluators might require additional fields, like `ground_truth` or tool definitions. For more information, see the [evaluator documentation](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/general-purpose-evaluators).

```
testing_criteria = [
    {
        "type": "azure_ai_evaluator",
        "name": "Task Adherence",
        "evaluator_name": "builtin.task_adherence",
        "data_mapping": {
            "query": "{{item.query}}",
            "response": "{{sample.output_items}}",
        },
        "initialization_parameters": {"deployment_name": model_deployment},
    },
    {
        "type": "azure_ai_evaluator",
        "name": "Coherence",
        "evaluator_name": "builtin.coherence",
        "data_mapping": {
            "query": "{{item.query}}",
            "response": "{{sample.output_items}}",
        },
        "initialization_parameters": {"deployment_name": model_deployment},
    },
    {
        "type": "azure_ai_evaluator",
        "name": "Violence",
        "evaluator_name": "builtin.violence",
        "data_mapping": {
            "query": "{{item.query}}",
            "response": "{{sample.output_items}}",
        },
    },
]
```

Next, create the evaluation. An evaluation defines the test data schema and testing criteria. It serves as a container for multiple runs. All runs under the same evaluation conform to the same schema and produce the same set of metrics. This consistency is important for comparing results across runs.

```
data_source_config = {
    "type": "custom",
    "item_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
        },
        "required": ["query"],
    },
    "include_sample_schema": True,
}

evaluation = client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=data_source_config,
    testing_criteria=testing_criteria,
)
```

Finally, create a run that sends your test queries to the agent and applies the evaluators:

```
eval_run = client.evals.runs.create(
    eval_id=evaluation.id,
    name="Agent Evaluation Run",
    data_source={
        "type": "azure_ai_target_completions",
        "source": {
            "type": "file_id",
            "id": dataset.id,
        },
        "input_messages": {
            "type": "template",
            "template": [{"type": "message", "role": "user", "content": {"type": "input_text", "text": "{{item.query}}"}}],
        },
        "target": {
            "type": "azure_ai_agent",
            "name": "my-agent",  # Replace with your agent name
            "version": "1",  # Optional; omit to use latest version
        },
    },
)

print(f"Evaluation run started: {eval_run.id}")
```

Evaluations typically complete in a few minutes, depending on the number of queries. Poll for completion and retrieve the report URL to view the results in the Microsoft Foundry portal under the **Evaluations** tab:

```
import time

# Wait for completion
while True:
    run = client.evals.runs.retrieve(run_id=eval_run.id, eval_id=evaluation.id)
    if run.status in ["completed", "failed"]:
        break
    time.sleep(5)

print(f"Status: {run.status}")
print(f"Report URL: {run.report_url}")
```

[![Image 1: Screenshot showing evaluation results for an agent in the Microsoft Foundry portal.](https://learn.microsoft.com/en-us/azure/foundry/media/observability/agent-evaluation-results.png)](https://learn.microsoft.com/en-us/azure/foundry/media/observability/agent-evaluation-results.png#lightbox)

At the run level, you can see aggregated data, including pass and fail counts, token usage per model, and results per evaluator:

```
{
    "result_counts": {
        "total": 3,
        "passed": 1,
        "failed": 2,
        "errored": 0
    },
    "per_model_usage": [
        {
            "model_name": "gpt-4o-mini-2024-07-18",
            "invocation_count": 6,
            "total_tokens": 9285,
            "prompt_tokens": 8326,
            "completion_tokens": 959
        },
        ...
    ],
    "per_testing_criteria_results": [
        {
            "testing_criteria": "Task Adherence",
            "passed": 1,
            "failed": 2
        },
        ... // remaining testing criteria
    ]
}
```

Each evaluation run returns output items per row in your test dataset, providing detailed visibility into your agent's performance. Output items include the original query, agent response, individual evaluator results with scores and reasoning, and token usage:

```
{
    "object": "eval.run.output_item",
    "id": "1",
    "run_id": "evalrun_abc123",
    "eval_id": "eval_xyz789",
    "status": "completed",
    "datasource_item": {
        "query": "What's the weather in Seattle?",
        "response_id": "resp_abc123",
        "agent_name": "my-agent",
        "agent_version": "10",
        "sample.output_text": "I'd be happy to help with the weather! However, I need to check the current conditions. Let me look that up for you.",
        "sample.output_items": [
            ... // agent response messages with tool calls
        ]
    },
    
    "results": [
        {
            "type": "azure_ai_evaluator",
            "name": "Task Adherence",
            "metric": "task_adherence",
            "label": "pass",
            "reason": "Agent followed system instructions correctly",
            "threshold": 3,
            "passed": true,
            "sample":
            {
               ... // evaluator input/output and token usage
            }
        },
        ... // remaining evaluation results
    ]
}
```

*   **CI/CD pipeline**: Use evaluation as a quality gate in your deployment pipeline. For detailed integration, see [Run evaluations with GitHub Actions](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action).
*   **Production monitoring**: Monitor your agent in production by using continuous evaluation. For setup instructions, see [Set up continuous evaluation](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard#set-up-continuous-evaluation).

Use evaluation to iterate and improve your agent:

1.   Run evaluation to identify weak areas. Use [cluster analysis](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/cluster-analysis) to find patterns and errors.
2.   Adjust agent instructions or tools based on findings.
3.   Reevaluate and [compare runs](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-results#compare-the-evaluation-results) to measure improvement.
4.   Repeat until quality thresholds are met.

*   [Python SDK evaluation samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/samples/evaluations/README.md)
*   [Run AI red teaming](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/run-ai-red-teaming-cloud)
*   [Agent Monitoring Dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard)
*   [Agent evaluators reference](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators)
*   [REST API reference](https://learn.microsoft.com/en-us/azure/foundry/reference/foundry-project-rest-preview#openai-evals---list-evals)
