# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/concepts/metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Metrics

> Metrics are quantitative or qualitative ways to express insights about the [run](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/run).

What are Galileo metrics?

They are aggregated to show insights across multiple runs, or across a [project](/galileo/gen-ai-studio-products/galileo-evaluate/concepts/project). The metrics offered by Galileo will provide insights based on what metrics they are. For example, some metrics like [Context Adherence](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence) return a float between 0.0 and 1.0 to represent whether the response was adherent to the context input to the model. Other metrics, like [PII](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information), provide a string from a set of possible strings to denote what private identifiable information was provided by the input or output.

Galileo metrics are a powerful way to automate and standardize the evaluations of your generative AI applications. By using the Galileo metrics, teams can organize around a standardized evaluation framework incorporating any relevant metrics for a given project or run. Galileo's metrics are also powered by our industry leading Luna models, so you can be sure you can trust the results that you receive. For more detail on each metric, visit the [Galileo Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) section.

Galileo also offers the capability to define your own metrics, by importing or creating scorers for what is important to you. For more information about custom metrics, visit the [Register Custom Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/register-custom-metrics) page.
