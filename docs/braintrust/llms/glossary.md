# Source: https://braintrust.dev/docs/reference/glossary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

This glossary defines key terms and concepts used in our product and documentation.

## Workflow

A type of task that can be used in playgrounds. Consists of a chained sequence of prompts that automate complex workflows, where one LLM call's output feeds into the next.

[Workflows guide](/evaluate/playgrounds#workflows)

## Alert

An automation that notifies you when a specific condition occurs on your logs in Braintrust.

[Automations guide](/admin/automations)

## Automation

A configured workflow that lets you trigger actions based on specific events in Braintrust. For example, sending an alert, or batch exporting data.

[Automations guide](/admin/automations)

## Benchmark

An evaluation designed to assess model performance across specific capabilities or against industry standards.

## Brainstore

The high-performance data engine backing logs, search, and tables.

[Brainstore blog post](https://www.braintrust.dev/blog/brainstore)

## SQL

SQL queries for filtering and analyzing eval results, logs, and metrics. Braintrust also supports BTQL, an alternative pipe-delimited syntax.

[SQL reference](/reference/sql)

## Configuration

Project-level settings that define behavior for evals, experiments, and integrations.

[Project configuration guide](/admin/projects)

## Dataset

A versioned collection of pairs of inputs and (optional) expected outputs.

[Datasets guide](/annotate/datasets)

## Evaluation / Eval

An eval consists of a task, dataset, and scorer(s). Evaluations can be:

* **Offline**: run a task on a static dataset with scoring functions.
* **Online**: real-time scoring on production or test requests.

[Evals guide](/evaluate/run-evaluations)

## Experiment

An instance of an offline eval run. Scores a specific task run on a given dataset.

[Experiment guide](/evaluate/run-evaluations)

## Human review

An option to route evaluations or tasks to human reviewers instead of, or in addition to, automated scorers.

[Human review guide](/annotate/human-review)

## Log

An instance of a live production or test interaction. Logs can include inputs, outputs, expected values, metadata, errors, scores, and tags. Scorers can also be applied to live logs to conduct online evaluations.

[Logs guide](/observe/view-logs)

## Loop

An AI assistant in the Braintrust UI that can help you with evaluation-related tasks, like optimizing prompts and generating dataset rows.

[Loop guide](/observe/loop)

## Metric

A quantitative measure of model performance (for example, accuracy, latency, or cost) tracked over time and across experiments.

## Model

An AI system (typically an LLM) that can be evaluated or monitored with Braintrust. Models can be first-party, third-party, or open-source.

## Organization

Your company or team "home" in Braintrust. It holds all your projects, members, and settings.

[Organizations reference](/admin/organizations)

## OTEL

OpenTelemetry: the instrumentation standard Braintrust uses to collect and export trace and span data from integrations.

[OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)

## Playground

An interactive space where you can prototype, iterate on, and compare multiple prompts and models against a dataset in real time. A playground can be saved as an experiment.

[Playgrounds guide](/evaluate/playgrounds)

## Project

A container for related experiments, datasets, and logs. Use projects to segment work by feature, environment (dev/prod), or team.

[Projects guide](/admin/projects)

## Prompt

The instruction given to an AI model. Prompts are editable objects you can version and reuse across experiments and playgrounds.

[Prompts guide](/deploy/prompts)

## Prompt engineering

The practice of designing, optimizing, and refining prompts to improve AI model outputs and performance.

## Regression testing

Evaluations that ensure new model or prompt configurations maintain or improve upon previous performance benchmarks.

## Remote eval

An evaluation that is executed on external or third-party systems or services, allowing you to evaluate tasks in environments outside Braintrust.

[Remote evals guide](/evaluate/remote-evals)

## Scorer

The component responsible for judging the quality of AI outputs. Scorers may be:

* Rule-based code
* LLM-based prompts as judges
* Human reviewers

[Scorers guide](/evaluate/write-scorers)

## Setting

An organization-level preference or control, including user management, billing, and global integrations.

[Organizations reference](/admin/organizations)

## Span

A single segment within a trace, representing one operation (for example, a model call or tool execution) with its timing and metadata.

[Traces guide](/observe/view-logs#view-traces)

## Structured output

A defined format (for example, JSON or XML) that models must follow, enabling consistent parsing and scoring of responses.

[Structured output guide](/deploy/prompts#structured-outputs)

## Task

A single unit of work, typically composed of an input, output, expected result, and evaluation. Tasks often appear within dataset or eval detail screens.

## Thread view

A visualization mode for traces that displays the interaction as a conversation thread, showing messages, tool calls, and scores in chronological order. Thread view is particularly useful for debugging LLM conversations and multi-turn interactions.

[Traces guide](/observe/view-logs#view-as-a-thread)

## Timeline view

A visualization mode for traces that displays spans as a gantt chart, where horizontal bars represent the duration of each operation. Timeline view is useful for identifying performance bottlenecks and understanding execution flow.

[Traces guide](/observe/view-logs#view-as-a-timeline)

## Trace

An individual recorded session detailing each step of an interaction: model calls, tool invocations, and intermediate outputs. Traces aid debugging and root-cause analysis.

[Traces guide](/observe/view-logs)

## User feedback

End-user inputs and ratings collected from production that inform model performance tracking and future evals.

[User feedback guide](/instrument/user-feedback)
