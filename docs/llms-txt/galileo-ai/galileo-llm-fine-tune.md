# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview of Galileo LLM Fine-Tune

> Fine-tune large language models with Galileo's LLM Fine-Tune tools, enabling precise adjustments for optimized AI performance and output quality.

<Info>Galileo Fine-Tune is in beta. If you're interested in trying out this module, reach out to join our Early Access Program.</Info>

<iframe src="https://cdn.iframe.ly/V1Xs7LL" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

Fine Tuning an LLM with the famous Alpaca Dataset and using Galileo to find errors

Using Galileo Fine-Tune you can improve the quality of your fine-tuned LLMs by improving the quality of your training data. Research has shown that small high-quality datasets can lead to powerful LLMs. Galileo Fine-Tune helps you achieve that.

Galileo integrates into your training workflow through its `dataquality` Python library. During Training, Galileo sees your samples and your model's output to find errors in your data. Galileo uses **Guardrail Metrics** as well as its **Data Error Potential** score to help you find your most problematic samples.

The **Galileo Data Error Potential (DEP)** score has been built to provide a per-sample holistic data quality score to identify samples in the dataset contributing to low or high model performance i.e. ‘pulling’ the model up or down respectively. In other words, the DEP score measures the potential for "misfit" of an observation to the given model.

Galileo surfaces token-level DEP scores to understand which parts of your Target Output or Ground Truth your model is struggling with.

**Getting Started**

See the [Quickstart](/galileo/gen-ai-studio-products/galileo-llm-fine-tune/quickstart) section to get started.

There are a few ways to get started using Galileo Finetune. You can choose between hooking into your model training, or uploading your data via Galileo Auto.
