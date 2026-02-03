# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/experiment-with-multiple-prompts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Experiment with Multiple Prompts

> Experiment with multiple prompts in Galileo Evaluate to optimize generative AI performance using iterative testing and comprehensive analysis tools.

In Galileo, you can execute multiple prompt runs using what we call "Prompt Sweeps".

A sweep allows you to execute, in bulk, multiple LLM runs with different combinations of - prompt templates, models, data, and hyperparameters such as temperature. Prompt Sweeps allows you to battle test an LLM completion step in your workflow.

<Info>Looking to run "sweeps" on more complex systems, such as Chains, RAG, or Agents? Check out [Chain Sweeps](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/experiment-with-multiple-chain-workflows).</Info>

<iframe src="https://cdn.iframe.ly/pl5CFiY" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

```Python  theme={null}
import promptquality as pq
from promptquality import Scorers
from promptquality import SupportedModels

models = [
    SupportedModels.text_davinci_3,
    SupportedModels.chat_gpt_16k,
    SupportedModels.gpt_4
]

templates = [
    """ Given the following context, please answer the question.
Context: {context}
Question: {question}
Your answer: """,
    """ You are a helpful assistant. Given the following context,
    please answer the question.
----
Context: {context}
----
Question: {question}
----
Your answer:
""",
    """ You are a helpful assistant. Given the following context,
    please answer the question. Provide an accurate and factual answer.
----
Context: {context}
----
Question: {question}
----
Your answer: """,
    """ You are a helpful assistant. Given the following context,
    please answer the question. Provide an accurate and factual answer.
    If the question is about science, religion or politics, say "I don't
     have enough information to answer that question based on the given context."
----
Context: {context}
----
Question: {question}
----
Your answer: """]

from promptquality import Scorers
from promptquality import SupportedModels

metrics = [
    Scorers.context_adherence_plus,
    Scorers.context_relevance,
    Scorers.correctness,
    Scorers.latency,
    Scorers.sexist,
    Scorers.pii
    # Uncertainty, BLEU and ROUGE are automatically included
]

pq.run_sweep(project_name='my_project_name',
             templates=templates,
             dataset='my_dataset.csv',
             scorers=metrics,
             model_aliases=models,
             execute=True)
```

See the [PromptQuality Python Library Docs](https://promptquality.docs.rungalileo.io/) for more information.
