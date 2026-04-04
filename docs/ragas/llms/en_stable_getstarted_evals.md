# Source: https://docs.ragas.io/en/stable/getstarted/evals/index.md

# Evaluate a simple LLM application

The purpose of this guide is to illustrate a simple workflow for testing and evaluating an LLM application with `ragas`. It assumes minimum knowledge in AI application building and evaluation. Please refer to our [installation instruction](https://docs.ragas.io/en/stable/getstarted/install/index.md) for installing `ragas`

Get a Working Example

The fastest way to see these concepts in action is to create a project using the quickstart command:

```sh
uvx ragas quickstart rag_eval
cd rag_eval
uv sync
```

```sh
pip install ragas
ragas quickstart rag_eval
cd rag_eval
uv sync
```

This generates a complete project with sample code. Follow along with this guide to understand what's happening in your generated code. Let's get started!

## Project Structure

Here's what gets created for you:

```sh
rag_eval/
├── README.md             # Project documentation and setup instructions
├── pyproject.toml        # Project configuration for uv and pip
├── evals.py              # Your evaluation workflow
├── rag.py                # Your RAG/LLM application
├── __init__.py           # Makes this a Python package
└── evals/                # Evaluation artifacts
    ├── datasets/         # Test data files (optional)
    ├── experiments/      # Results from running evaluations (CSV files saved here)
    └── logs/             # Evaluation execution logs
```

**Key files to focus on:**

- **`evals.py`** - Your evaluation workflow with dataset loading and evaluation logic
- **`rag.py`** - Your RAG/LLM application code (query engine, retrieval, etc.)

## Understanding the Code

In your generated project's `evals.py` file, you'll see the main workflow pattern:

1. **Load Dataset** - Define your test cases with `SingleTurnSample`
1. **Query RAG System** - Get responses from your application
1. **Evaluate Responses** - Validate responses against ground truth
1. **Display Results** - Show evaluation summary in console
1. **Save Results** - Automatically saved to CSV in `evals/experiments/` directory

The template provides modular functions you can customize:

```python
from ragas.dataset_schema import SingleTurnSample
from ragas import EvaluationDataset

def load_dataset():
    """Load test dataset for evaluation."""
    data_samples = [
        SingleTurnSample(
            user_input="What is Ragas?",
            response="",  # Will be filled by querying RAG
            reference="Ragas is an evaluation framework for LLM applications",
            retrieved_contexts=[],
        ),
        # Add more test cases...
    ]
    return EvaluationDataset(samples=data_samples)
```

You can extend this with [metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/index.md) and more sophisticated evaluation logic. Learn more about [evaluation in Ragas](https://docs.ragas.io/en/stable/getstarted/concepts/evaluation/index.md).

### Choosing Your LLM Provider

Your quickstart project initializes the OpenAI LLM by default in the `_init_clients()` function. You can easily swap to any provider through the `llm_factory`:

Set your OpenAI API key:

```sh
export OPENAI_API_KEY="your-openai-key"
```

In your `evals.py` `_init_clients()` function:

```python
from ragas.llms import llm_factory

llm = llm_factory("gpt-4o")
```

This is already set up in your quickstart project!

Set your Anthropic API key:

```sh
export ANTHROPIC_API_KEY="your-anthropic-key"
```

In your `evals.py` `_init_clients()` function:

```python
from ragas.llms import llm_factory

llm = llm_factory("claude-3-5-sonnet-20241022", provider="anthropic")
```

Set up your Google credentials:

```sh
export GOOGLE_API_KEY="your-google-api-key"
```

In your `evals.py` `_init_clients()` function:

```python
from ragas.llms import llm_factory

llm = llm_factory("gemini-1.5-pro", provider="google")
```

Install and run Ollama locally, then in your `evals.py` `_init_clients()` function:

```python
from ragas.llms import llm_factory

llm = llm_factory(
    "mistral",
    provider="ollama",
    base_url="http://localhost:11434"  # Default Ollama URL
)
```

For any LLM with OpenAI-compatible API:

```python
from ragas.llms import llm_factory

llm = llm_factory(
    "model-name",
    api_key="your-api-key",
    base_url="https://your-api-endpoint"
)
```

For more details, learn about [LLM integrations](https://docs.ragas.io/en/stable/concepts/metrics/index.md).

### Using Pre-Built Metrics

`ragas` comes with pre-built metrics for common evaluation tasks. For example, [Aspect Critique](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/aspect_critic/index.md) evaluates any aspect of your output using `DiscreteMetric`:

```python
from ragas.metrics import DiscreteMetric
from ragas.llms import llm_factory

# Setup your evaluator LLM
evaluator_llm = llm_factory("gpt-4o")

# Create a custom aspect evaluator
metric = DiscreteMetric(
    name="summary_accuracy",
    allowed_values=["accurate", "inaccurate"],
    prompt="""Evaluate if the summary is accurate and captures key information.

Response: {response}

Answer with only 'accurate' or 'inaccurate'.""",
    llm=evaluator_llm
)

# Score your application's output
score = await metric.ascore(
    response="The summary of the text is..."
)
print(f"Score: {score.value}")  # 'accurate' or 'inaccurate'
print(f"Reason: {score.reason}")
```

Pre-built metrics like this save you from defining evaluation logic from scratch. Explore [all available metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/index.md).

Info

There are many other types of metrics that are available in `ragas` (with and without `reference`), and you may also create your own metrics if none of those fits your case. To explore this more checkout [more on metrics](https://docs.ragas.io/en/stable/concepts/metrics/index.md).

### Evaluating on a Dataset

In your quickstart project, you'll see in the `load_dataset()` function, which creates test data with multiple samples:

```python
from ragas import Dataset

# Create a dataset with multiple test samples
dataset = Dataset(
    name="test_dataset",
    backend="local/csv",  # Can also use JSONL, Google Drive, or in-memory
    root_dir=".",
)

# Add samples to the dataset
data_samples = [
    {
        "user_input": "What is ragas?",
        "response": "Ragas is an evaluation framework...",
        "expected": "Ragas provides objective metrics..."
    },
    {
        "user_input": "How do metrics work?",
        "response": "Metrics score your application...",
        "expected": "Metrics evaluate performance..."
    },
]

for sample in data_samples:
    dataset.append(sample)

# Save to disk
dataset.save()
```

This gives you multiple test cases instead of evaluating one example at a time. Learn more about [datasets and experiments](https://docs.ragas.io/en/stable/concepts/components/eval_dataset/index.md).

Your generated project includes sample data in the `evals/datasets/` folder - you can edit those files to add more test cases.

### Want help in improving your AI application using evals?

In the past 2 years, we have seen and helped improve many AI applications using evals.

We are compressing this knowledge into a product to replace vibe checks with eval loops so that you can focus on building great AI applications.

If you want help with improving and scaling up your AI application using evals.

🔗 Book a [slot](https://bit.ly/3EBYq4J) or drop us a line: [founders@vibrantlabs.com](mailto:founders@vibrantlabs.com).

## Up Next

- [Evaluate a simple RAG application](https://docs.ragas.io/en/stable/getstarted/rag_eval/index.md)
