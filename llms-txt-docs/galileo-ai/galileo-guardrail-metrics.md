# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics.md

# Overview of Galileo Guardrail Metrics

> Utilize Galileo's Guardrail Metrics to monitor generative AI models, ensuring adherence to quality, correctness, and alignment with project goals.

Understand Galileo's Guardrail Metrics in LLM Studio

Galileo has built a menu of **Guardrail Metrics** to help you evaluate, observe and protect your generative AI applications. These metrics are tailored to your use case and are designed to help you ensure your application quality and behavior. The `Scorer` definition for each metric is listed immediately below.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/metrics-backbone.png" />
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
