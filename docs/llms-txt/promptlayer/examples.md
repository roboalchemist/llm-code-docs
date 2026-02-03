# Source: https://docs.promptlayer.com/features/evaluations/examples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Eval Examples

## Building & Evaluating a RAG Chatbot

<div style={{ position: 'relative', paddingBottom: '56.25%', height: 0 }}>
  <iframe src="https://www.youtube.com/embed/DhKtNpvxawU?feature=youtu.be" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }} />
</div>

This example shows how you can use PromptLayer to evaluate Retrieval Augmented Generation (RAG) systems. As a cornerstone of the LLM revolution, RAG systems enhance our ability to extract precise information from vast datasets, significantly improving question-answering capabilities.

We will create a RAG system designed for financial data analysis using a dataset from the New York Stock Exchange. The tutorial video elaborates on the step-by-step process of constructing a pipeline that encompasses prompt creation, data retrieval, and the evaluation of the system's efficacy in answering finance-related queries.

Most importantly, you can use PromptLayer to build end-to-end evaluation tests for RAG systems.

## Migrating Prompts to Open-Source Models

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/migrating-prompts.jpeg?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5cd425e8b2b8453d148625d239589b29" alt="Migrating Prompts" data-og-width="1500" width="1500" data-og-height="626" height="626" data-path="images/migrating-prompts.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/migrating-prompts.jpeg?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=14c6aaa027eefcbf07cf76d869c3fa04 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/migrating-prompts.jpeg?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=f3fa269eb17ef9e413171fe1a2bf63be 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/migrating-prompts.jpeg?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=f1ebd05f93a191692d8b0fdd95936331 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/migrating-prompts.jpeg?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=7d8290f704cc4172489c2b22cce70618 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/migrating-prompts.jpeg?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=4c4236392583a5737cf097830cdb1727 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/migrating-prompts.jpeg?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=d9bc47e75d2c1b43e171a752410902dd 2500w" />

[Click Here to Read the Tutorial](https://blog.promptlayer.com/migrating-prompts-to-open-source-models-c21e1d482d6f)

This tutorial demonstrates how to use PromptLayer to migrate prompts between different language models, with a focus on open-source models like [Mistral](https://mistral.ai/). It covers techniques for batch model comparisons, allowing you to evaluate the performance of your prompt across multiple models. The example showcases migrating an existing prompt for a RAG system to the open-source Mistral model and comparing the new outputs with visual diffs.

The key steps include:

1. Setting up a batch evaluation pipeline to run the prompt on both the original model (e.g., GPT) and the new target model (Mistral), while diffing the outputs.
2. Analyzing the results, including accuracy scores, cost/latency metrics, and string output diffs, to assess the impact of migrating to the new model.
3. Seamlessly updating the prompt template to use the new model (Mistral) if the migration is beneficial.

This example highlights PromptLayer's capabilities for efficient prompt iteration and evaluation across different language models, facilitating the adoption of open-source alternatives like Mistral.
