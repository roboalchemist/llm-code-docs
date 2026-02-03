# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/sexism.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Sexism

> Understand Galileo's Sexism Metric

***Definition:*** Flags whether a response contains sexist content. Output is a binary classification of whether a response is sexist or not.

***Calculation:*** We leverage a Small Language Model (SLM) trained on open-source and internal datasets.

Our model's accuracy on the [Explainable Detection of Online Sexism](https://github.com/rewire-online/edos) dataset (open-source) is 83%.

***Usefulness:*** Identify responses that contain sexist comments and take preventive measures such as fine-tuning or implementing guardrails that flag responses before being served in order to prevent future occurrences.
