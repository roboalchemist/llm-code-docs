# Source: https://braintrust.dev/docs/workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Braintrust workflow

> Understand how to trace, evaluate, and improve AI applications with Braintrust

Building reliable AI applications requires a different approach than traditional software development. With AI, small changes to prompts, models, or data can have unpredictable effects on quality. Braintrust provides a structured workflow that helps you measure, understand, and improve your AI applications systematically.

Effective AI development follows a continuous improvement cycle with five key stages:

1. **Instrument** → Capture traces from your application
2. **Observe** → Find patterns and issues in your data
3. **Annotate** → Review and improve with human feedback
4. **Evaluate** → Test and validate improvements
5. **Deploy** → Ship changes and monitor impact

Each stage builds on the previous one, creating a feedback loop that enables continuous improvement.

## <Icon icon="braces" iconType="solid" size={24} /> Instrument

Capture detailed traces from your AI application by integrating Braintrust logging into your code. Traces record inputs, outputs, model parameters, latency, token usage, and other metadata for every request.

**What you'll do:**

* [Wrap your AI provider clients](/instrument/wrap-providers) (OpenAI, Anthropic, Gemini, etc.)
* [Integrate with frameworks](/instrument/frameworks) like LangChain or OpenTelemetry
* [Configure structured tracing](/instrument/custom-tracing) for complex workflows

**Outcome:** Your application automatically sends trace data to Braintrust, giving you visibility into every request.

→ [Get started with instrumentation](/instrument)

## <Icon icon="activity" iconType="solid" size={24} /> Observe

Analyze your application's behavior by exploring logs, identifying patterns, and discovering issues. Use filtering, search, and custom dashboards to understand what's happening in production.

**What you'll do:**

* [View and filter logs](/observe/view-logs) to spot errors, latency issues, and unexpected outputs
* [Use deep search](/observe/deep-search) to find similar traces semantically
* [Create custom dashboards](/observe/dashboards) to track key metrics over time
* [Use Loop](/observe/loop) to ask questions and explore patterns in your logs

**Outcome:** You understand where your application succeeds and where it struggles, with concrete examples of both.

→ [Get started with observability](/observe)

## <Icon icon="list-checks" iconType="solid" size={24} /> Annotate

Improve your data quality by adding human feedback, creating datasets, and labeling important examples. Annotation transforms raw logs into high-quality evaluation data.

**What you'll do:**

* [Add human feedback](/annotate/human-review) to traces
* [Capture user feedback](/instrument/user-feedback) from production
* [Use labels](/annotate/labels) to flag interesting examples for closer examination
* [Build datasets](/annotate/datasets) from annotated traces

**Outcome:** You have curated datasets that represent real user interactions, annotated with expert feedback.

→ [Get started with annotation](/annotate)

## <Icon icon="beaker" iconType="solid" size={24} /> Evaluate

Test changes systematically by iterating in playgrounds and running experiments on your datasets. Start with rapid prototyping in playgrounds, then create immutable experiment snapshots to track improvements over time.

**What you'll do:**

* [Use playgrounds](/evaluate/playgrounds) for rapid prototyping and iteration
* [Write scorers](/evaluate/write-scorers) to quantify quality improvements
* [Run experiments](/evaluate/run-evaluations) to snapshot results and track progress
* [Compare experiment results](/evaluate/compare-experiments) to identify improvements and regressions

**Outcome:** You know which changes improve your application and which cause regressions, backed by quantitative data.

→ [Get started with evaluation](/evaluate)

## <Icon icon="rocket" iconType="solid" size={24} /> Deploy

Ship validated changes to production and monitor their impact. Deployment includes updating prompts, switching models, and running online evaluations to catch issues in real time.

**What you'll do:**

* [Deploy prompts](/deploy/prompts) and [functions](/deploy/functions) to production
* [Use the AI Proxy](/deploy/ai-proxy) to call any AI provider through a unified interface
* [Monitor production](/deploy/monitor) with online scoring and dashboards

**Outcome:** Your improvements run in production with monitoring in place to catch issues early.

→ [Get started with deployment](/deploy)

<Note>
  The cycle repeats as you deploy changes. New production logs feed back into the Observe stage, creating a continuous improvement loop.
</Note>
