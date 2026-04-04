# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/bleu-and-rouge-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# BLEU and ROUGE

> Understand BLEU & ROUGE-1 scores

***Definition:*** Metrics used heavily in sequence-to-sequence tasks measuring n-gram overlap between a generated response and a target output. Higher BLEU and ROUGE-1 scores equates to better overlap between the generated and target output.

***Calculation:*** A measure of n-gram overlap. A more lengthy explanation of BLEU provided [here](https://towardsdatascience.com/foundations-of-nlp-explained-bleu-score-and-wer-metrics-1a5ba06d812b). A more lengthy explanation of ROUGE-1 provided [here](https://www.galileo.ai/blog/rouge-ai). These metrics require a {target} column in your dataset.

***Usefulness:*** Evaluate the accuracy of model outputs in comparison to target outputs, enabling a metric to guide improvement and examination of areas where a model has trouble adhering to expected output.

<Info>
  *Note:* These metrics require a Ground Truth to be set. Check out [this page](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/logging-and-comparing-against-your-expected-answers) to learn how to add a Ground Truth to your runs.
</Info>
