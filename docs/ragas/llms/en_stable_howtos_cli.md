# Source: https://docs.ragas.io/en/stable/howtos/cli/index.md

# Ragas CLI

The Ragas Command Line Interface (CLI) provides tools for quickly setting up evaluation projects and running experiments from the terminal.

## Installation

The CLI is included with the ragas package:

```sh
pip install ragas
```

Or use `uvx` to run without installation:

```sh
uvx ragas --help
```

## Available Commands

### `ragas quickstart`

Create a complete evaluation project from a template. This is the fastest way to get started with Ragas.

```sh
ragas quickstart [TEMPLATE] [OPTIONS]
```

**Arguments:**

- `TEMPLATE`: Template name (optional). Leave empty to see available templates.

**Options:**

- `-o, --output-dir`: Directory to create the project in (default: current directory)

**Examples:**

```sh
# List available templates
ragas quickstart

# Create a RAG evaluation project
ragas quickstart rag_eval

# Create project in a specific directory
ragas quickstart rag_eval --output-dir ./my-project
```

### `ragas evals`

Run evaluations on a dataset using an evaluation file.

```sh
ragas evals EVAL_FILE [OPTIONS]
```

**Arguments:**

- `EVAL_FILE`: Path to the evaluation file (required)

**Options:**

- `--dataset`: Name of the dataset in the project (required)
- `--metrics`: Comma-separated list of metric field names to evaluate (required)
- `--baseline`: Baseline experiment name to compare against (optional)
- `--name`: Name of the experiment run (optional)

**Example:**

```sh
ragas evals evals.py --dataset test_data --metrics accuracy,relevance
```

### `ragas hello_world`

Create a simple hello world example to verify your installation.

```sh
ragas hello_world [DIRECTORY]
```

**Arguments:**

- `DIRECTORY`: Directory to create the example in (default: current directory)

## Quickstart Templates

### RAG & Retrieval

- [RAG Evaluation (`rag_eval`)](https://docs.ragas.io/en/stable/howtos/cli/rag_eval/index.md) - Evaluate RAG systems with custom metrics
- [Improve RAG (`improve_rag`)](https://docs.ragas.io/en/stable/howtos/cli/improve_rag/index.md) - Compare naive vs agentic RAG approaches

### Agent Evaluation

- [Agent Evaluation (`agent_evals`)](https://docs.ragas.io/en/stable/howtos/cli/agent_evals/index.md) - Evaluate AI agents solving math problems
- [LlamaIndex Agent Evaluation (`llamaIndex_agent_evals`)](https://docs.ragas.io/en/stable/howtos/cli/llamaIndex_agent_evals/index.md) - Evaluate LlamaIndex agents with tool call metrics

### Specialized Use Cases

- [Text-to-SQL Evaluation (`text2sql`)](https://docs.ragas.io/en/stable/howtos/cli/text2sql/index.md) - Evaluate text-to-SQL systems with execution accuracy
- [Workflow Evaluation (`workflow_eval`)](https://docs.ragas.io/en/stable/howtos/cli/workflow_eval/index.md) - Evaluate complex LLM workflows
- [Prompt Evaluation (`prompt_evals`)](https://docs.ragas.io/en/stable/howtos/cli/prompt_evals/index.md) - Compare different prompt variations

### LLM Testing

- [Judge Alignment (`judge_alignment`)](https://docs.ragas.io/en/stable/howtos/cli/judge_alignment/index.md) - Measure LLM-as-judge alignment with human standards
- [LLM Benchmarking (`benchmark_llm`)](https://docs.ragas.io/en/stable/howtos/cli/benchmark_llm/index.md) - Benchmark and compare different LLM models

## Quick Start

Get running in 60 seconds:

```sh
# Create project
uvx ragas quickstart rag_eval
cd rag_eval

# Install dependencies
uv sync

# Set API key
export OPENAI_API_KEY="your-key"

# Run evaluation
uv run python evals.py
```

## Next Steps

- [RAG Evaluation Guide](https://docs.ragas.io/en/stable/howtos/cli/rag_eval/index.md) - Detailed walkthrough of the rag_eval template
- [Improve RAG Guide](https://docs.ragas.io/en/stable/howtos/cli/improve_rag/index.md) - Compare naive vs agentic RAG approaches
- [Custom Metrics](https://docs.ragas.io/en/stable/howtos/customizations/metrics/_write_your_own_metric.md) - Create your own evaluation metrics
