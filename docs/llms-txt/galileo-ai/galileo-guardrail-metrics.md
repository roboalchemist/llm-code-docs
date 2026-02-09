# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview of Galileo Guardrail Metrics

> Utilize Galileo's Guardrail Metrics to monitor generative AI models, ensuring adherence to quality, correctness, and alignment with project goals.

Understand Galileo's Guardrail Metrics in LLM Studio

Galileo has built a menu of **Guardrail Metrics** to help you evaluate, observe and protect your generative AI applications. These metrics are tailored to your use case and are designed to help you ensure your application quality and behavior. The `Scorer` definition for each metric is listed immediately below.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-backbone.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=04be9b026c95e9cec1144ef38e640b9f" data-og-width="1864" width="1864" data-og-height="772" height="772" data-path="images/metrics-backbone.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-backbone.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a956c9acefa740401f198603c6e61221 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-backbone.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c799731be443a35c646168cf51203b3a 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-backbone.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1cbae5aca80e34b669df474360cee299 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-backbone.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=858a139688cc45a56c89e137f2098796 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-backbone.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=3e2618ec480c5879501db47d6accb1d8 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-backbone.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1fb302640aef2ffa8fec88d5179df8e8 2500w" />
</Frame>

Galileo's Guardrail Metrics are a combination of industry-standard metrics and an outcome of Galileo's in-house ML Research Team.

#### Output Quality Metrics

* [Correctness](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/correctness) (Open Domain Hallucinations)

* [Instruction Adherence:](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/instruction-adherence) `Scorers.instruction_adherence_plus`

* [Uncertainty](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty)

* [Ground Truth Adherence:](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/ground-truth-adherence) `Scorers.ground_truth_adherence_plus`

* [Completeness](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus)
  * [Completeness Luna](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-luna): `Scorers.completeness_luna`

  * [Completeness Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus): `Scorers.completeness_plus`

* [BLEU and ROUGE](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/bleu-and-rouge-1)

#### Agent Quality Metrics

* [Action Completion:](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/action-completion) `Scorers.action_completion_plus`

* [Action Advancement:](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/action-advancement) `Scorers.action_advancement_plus`

* [Tool Selection Quality:](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tool-selection-quality) `Scorers.tool_selection_quality_plus`

* [Tool Error:](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tool-error) `Scorers.tool_errors_plus`

#### RAG Quality Metrics

* [Context Adherence](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence) (Closed Domain Hallucinations)
  * [Context Adherence Luna](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna): `Scorers.context_adherence_luna`

  * [Context Adherence Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-plus): `Scorers.context_adherence_plus`

* [Chunk Attribution](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution)
  * [Chunk Attribution Luna](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution/chunk-attribution-luna): `Scorers.chunk_attribution_utilization_luna`

  * [Chunk Attribution Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution/chunk-attribution-plus): `Scorers.chunk_attribution_utilization_plus`

* [Chunk Utilization](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization)
  * [Chunk Utilization Luna](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-luna): `Scorers.chunk_attribution_utilization_luna`

  * [Chunk Utilization Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-plus): `Scorers.chunk_attribution_utilization_plus`

#### Input Quality Metrics

* [Prompt Perplexity](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-perplexity)

#### Safety Metrics

* [Input & Output PII](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information)

* [Input & Output Tone](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tone)

* [Input & Output Toxicity](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/toxicity)

* [Input & Output Sexism](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/sexism)

* [Prompt Injection](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-injection)

Looking for something more specific? You can always add your own [custom metric](/galileo/gen-ai-studio-products/galileo-observe/how-to/registering-and-using-custom-metrics).
