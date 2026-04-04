# Source: https://www.comet.com/docs/opik/opik-university/observability/annotate-traces.mdx

***

headline: Annotate Traces | Opik Documentation
'og:description': >-
Learn to effectively annotate traces in Opik to improve observability and gain
deeper insights into your applications.
'og:site\_name': Opik Documentation
'og:title': Annotate Traces with Opik for Enhanced Observability
title: Annotate Traces
----------------------

<div>
  <iframe src="https://www.loom.com/embed/c61ce69e245840489dd90b25489493a8?sid=37e03eeb-e709-4182-9889-f80d113dade2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen />
</div>

## Building Feedback Loops with Trace Annotations

This video demonstrates how to add human feedback and annotations to your LLM [traces](/tracing/log_traces), creating a powerful feedback loop for continuous improvement. You'll learn to mark [traces](/tracing/log_traces) as high or low quality, add specific [feedback scores](/tracing/annotate_traces), and build [datasets](/evaluation/manage_datasets) of annotated examples for future [evaluation](/evaluation/overview) and fine-tuning. Annotations bridge the gap between raw trace data and actionable insights for model improvement.

## Key Highlights

* **Easy Feedback Addition**: Use the [feedback scores](/tracing/annotate_traces) section and pen icon to quickly add human annotations directly to [traces](/tracing/log_traces) in the Opik UI
* **Custom Feedback Definitions**: Create categorical or numerical feedback [metrics](/evaluation/metrics/overview) in Configuration → Feedback Definitions to match your specific evaluation needs
* **Flexible Scoring Options**: Define custom categories (pass/fail, quality ratings) or sliding scales (0-1) based on [metrics](/evaluation/metrics/overview) like accuracy, relevance, or tone
* **Smart Filtering**: Filter [traces](/tracing/log_traces) by [feedback scores](/tracing/annotate_traces) to quickly identify high-performing or problematic outputs for targeted analysis
* **[Dataset](/evaluation/manage_datasets) Creation**: Convert annotated [traces](/tracing/log_traces) directly into [datasets](/evaluation/manage_datasets) for training data collection and model improvement workflows
* **Built-in [Metrics](/evaluation/metrics/overview) Library**: Access pre-built metrics like [answer relevance](/evaluation/metrics/answer_relevance), [Levenshtein distance](/evaluation/metrics/heuristic_metrics), and [hallucination](/evaluation/metrics/hallucination) detection out of the box
* **LLM as a Judge**: Use automated LLM-based [evaluation](/evaluation/metrics/g_eval) where a second LLM evaluates responses from your primary model
* **Pattern Identification**: Annotations help identify performance patterns, create training data, and establish feedback loops between users and developers
