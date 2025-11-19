# Source: https://docs.galileo.ai/galileo-ai-research/rag-quality-metrics-using-chainpoll.md

# Rag Quality Metrics Using Chainpoll

> Learn how ChainPoll metrics assess retrieval-augmented generation (RAG) system quality, improving accuracy and performance of generative AI models.

[ChainPoll](/galileo/gen-ai-studio-products/galileo-ai-research/chainpoll) powers the "Plus" versions of our four RAG Quality Guardrail Metrics:

* [Context Adherence Plus](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll#context-adherence)

* [Completeness Plus](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll#completeness)

* [Chunk Attribution Plus](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll#chunk-attribution)

* [Chunk Utilization Plus](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll#chunk-utilization)

This page provides a brief overview of the research behind these metrics.

Our research investments in RAG measurement are built on the foundation of our earlier work on LLM hallucination detection.

For a full overview of that earlier work, check out our paper [Chainpoll: A high efficacy method for LLM hallucination detection](https://arxiv.org/abs/2310.18344). We're currently working on a companion paper, which will more comprehensively describe our work on RAG.

### Overall Metric Performance Results

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/rag-q-m.avif" />
</Frame>

### Methodology

In [Chainpoll: A high efficacy method for LLM hallucination detection](https://arxiv.org/abs/2310.18344), we found (among other things) that:

* OpenAI's GPT-4 is a capable judge of content produced by other LLMs.

  * For example, on a hallucination detection task, we found that GPT-4's assessments aligned just as well with human annotations as human annotations (made by different annotators) aligned with each another.

* Models such as GPT-3.5-Turbo -- which are more cost-effective than GPT-4 and more appropriate for routine use -- are not as effective as GPT-4 at this type of judgment task.

  * However, by using a technique we call **ChainPoll** with GPT-3.5, we can close much of this quality gap between GPT-3.5 and GPT-4.

These observations shaped the research methodology we use today to develop new metrics. In particular,

* We make extensive use of GPT-4 as an annotator, and use GPT-4 annotations as a reference against which to compare each metric we develop.

  * While GPT-4 produces high-quality results, using GPT-4 to compute metrics would be prohibitively slow and expensive for our users.

  * Hence, we focus on building metrics that use more cost-effective models under the hood, viewing GPT-4 results as a quality bar to shoot for. The ideal, here, would be GPT-4-*quality* results, offered up with the *cost and speed* of GPT-3.5-like models.

* While we benchmark all metrics against GPT-4, we also supplement these evals where possible with other, complementary ways of assessing whether our metrics do what we want them to do.

* To create new metrics, we design new prompts that can be used with ChainPoll.

  * We evaluate many different potential prompts, evaluating them against GPT-4 and other sources of information, before settling on one to release.

  * We also experiment with different ways of eliciting and aggregating results -- i.e. with variants on the basic ChainPoll recipe, tailored to the needs of each metric.

    * For example, we've developed a novel evaluation methodology for RAG Attribution metrics, which involves "counterfactual" responses generated without access to some of the original chunks. We'll present this methodology in our forthcoming paper.

### Metrics

#### Response-level metrics: Context Adherence Plus and Completeness Plus

These two metrics capture different facets of RAG response quality. Both involve assessing the relationship between the response, the retrieved context, and the query that the RAG system is responding to.

These metrics use ChainPoll. To recap, that means:

* We construct a prompt requesting a judgment from an LLM.

  * In this case, the prompt includes the response and the retrieved context, and a set of instructions asking the LLM to make a particular judgment about these texts.

  * The prompt requests an extensive, detailed chain of thought in which the LLM describes its step-by-step reasoning. (This is the "chain" part of ChainPoll.)

* We fetch *multiple* responses from this single prompt. (This is the "poll" part of ChainPoll.)

* We *aggregate* the judgments across the responses, producing a single score.

The overall approach is inspired by the [self-consistency for chain of thought](https://arxiv.org/abs/2203.11171) technique.

#### Context Adherence Plus

In our earlier paper [Chainpoll: A high efficacy method for LLM hallucination detection](https://arxiv.org/abs/2310.18344), we presented results on the quality of our Context Adherence Plus metric on a dataset suite we called **RealHall**.

In our work on RAG, we've extended these experiments to benchmark Context Adherence Plus on some additional RAG-like datasets.

Here's a peek into those results, showing the precision-recall curves for Context Adherence Plus on three RAG datasets, with GPT-4 annotations as ground truth labels.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/rag-q-m-2.avif" />
</Frame>

As baselines, we compare Context Adherence Plus to a simpler prompting approach with
GPT-3.5-Turbo, as well as the Faithfulness score defined by the RAGAS RAG evaluation
library.

#### Completeness Plus

Completeness differs from our other ChainPoll metrics like Context Adherence Plus in that it elicits a numeric score -- not a boolean -- directly from the LLM, then aggregates by taking an average over the scores.

We chose this approach over a boolean + aggregate approach after trying both, because we found the numeric + aggregate approach gave more useful and interpretable scores.

The next figure illustrates the difference in quality between our "final cut" of the Completeness metric and a simpler prompting approach with GPT-3.5-Turbo.

Each pane is a histogram, where larger numbers mean better alignment with the ground truth. Taller bars near 1.0 indicate that a larger fraction of scores from the metric fall very close to the ground truth.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/completeness-histogram.png)

#### Chunk-level metrics: Chunk Attribution and Chunk Utilization

These metrics evaluate individual chunks retrieved by a RAG system, in light of the response written by the system.

We initially prototyped these metrics with ChainPoll, but after closer investigation, we found that ChainPoll aggregation provided minimal quality lift relative to only eliciting a single response.

As a result, we use a single LLM response to compute these metrics. Although we don't use ChainPoll here, we are still able to improve upon simple prompting approaches through careful prompt engineering and task formulation.

#### Chunk Attribution Plus

Here are precision-recall curves from one of our evals for Chunk Attribution Plus, namely evaluation against GPT-4.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/rag-q-m-4.avif" />
</Frame>

#### Chunk Utilization Plus

For Chunk Utilization Plus, we experimented with a number of ways to frame the task. Our most effective framing, which powers the Chunk Utilization metric in the Galileo product, involves

* Pre-splitting each chunk into sentences

* Providing the LLM with brief, unique string keys which it can use to refer to individual chunk sentences (to improve token efficiency)

* Asking the LLM to specify, using the keys, which sentences in each chunk were used

Here are the results of one of our evals for Utilization. This is the same style of plot used above for Completeness -- see that section for information on how to read it.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/rag-q-m-5.avif" />
</Frame>
