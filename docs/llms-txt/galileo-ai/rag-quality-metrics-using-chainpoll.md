# Source: https://docs.galileo.ai/galileo-ai-research/rag-quality-metrics-using-chainpoll.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m.avif?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=39130d083e0a1450ada1f96985c2c8c6" data-og-width="800" width="800" data-og-height="242" height="242" data-path="images/rag-q-m.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m.avif?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=578f2673a0dbba9fceaa37a120e9c2d2 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m.avif?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=02bfd3be9188844728b1839c4837b14b 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m.avif?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=9d772a5cfc7b0e56ef32b040fc76a986 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m.avif?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=12aff9688c2d3a66ca127b67ff5645d2 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m.avif?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=391cd504b08e8d3d4c8b1de3207c3f6a 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m.avif?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b465eba597394e2a6bee700ca1faa943 2500w" />
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
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-2.avif?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6bee55ed5331a6451b63218e56806a88" data-og-width="800" width="800" data-og-height="271" height="271" data-path="images/rag-q-m-2.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-2.avif?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=5a75eeb8a0c81c694c072d93c7ac9ede 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-2.avif?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b265c48b93a622dfe0ba78575e208ab2 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-2.avif?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=734a70578a31085bfc1d1640a28924eb 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-2.avif?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=4de2aa16491d9ab20e3fb5c9e1b90e47 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-2.avif?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d1fd1eab61ca2a218ac190f23972d82d 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-2.avif?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=fef527212900f18ccd3bc2ad583c9ec0 2500w" />
</Frame>

As baselines, we compare Context Adherence Plus to a simpler prompting approach with
GPT-3.5-Turbo, as well as the Faithfulness score defined by the RAGAS RAG evaluation
library.

#### Completeness Plus

Completeness differs from our other ChainPoll metrics like Context Adherence Plus in that it elicits a numeric score -- not a boolean -- directly from the LLM, then aggregates by taking an average over the scores.

We chose this approach over a boolean + aggregate approach after trying both, because we found the numeric + aggregate approach gave more useful and interpretable scores.

The next figure illustrates the difference in quality between our "final cut" of the Completeness metric and a simpler prompting approach with GPT-3.5-Turbo.

Each pane is a histogram, where larger numbers mean better alignment with the ground truth. Taller bars near 1.0 indicate that a larger fraction of scores from the metric fall very close to the ground truth.

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/completeness-histogram.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=4db62530fdc05fe53c48e08a43009aef" alt="" data-og-width="1263" width="1263" data-og-height="415" height="415" data-path="images/completeness-histogram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/completeness-histogram.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=a0926c0e83427a9c55224b4276f3ba0e 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/completeness-histogram.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=61a04af9a5647d928b496a4cc68e14c7 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/completeness-histogram.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c684ffb354cd3bb93ba4a176b9452447 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/completeness-histogram.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=fa6113a7b98f2e48c8cd0265521b5e03 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/completeness-histogram.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=cc9a5e2dab2c15e5a13e36b5f9eaf98a 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/completeness-histogram.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c67129394fb61747ad223965f94c1946 2500w" />

#### Chunk-level metrics: Chunk Attribution and Chunk Utilization

These metrics evaluate individual chunks retrieved by a RAG system, in light of the response written by the system.

We initially prototyped these metrics with ChainPoll, but after closer investigation, we found that ChainPoll aggregation provided minimal quality lift relative to only eliciting a single response.

As a result, we use a single LLM response to compute these metrics. Although we don't use ChainPoll here, we are still able to improve upon simple prompting approaches through careful prompt engineering and task formulation.

#### Chunk Attribution Plus

Here are precision-recall curves from one of our evals for Chunk Attribution Plus, namely evaluation against GPT-4.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-4.avif?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=88a615ce7bef33a95729aebd0e2756dd" data-og-width="800" width="800" data-og-height="271" height="271" data-path="images/rag-q-m-4.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-4.avif?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f86d6458f7183def2538ab267ac146cb 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-4.avif?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ba1ba6c5a214fb496755ca19777ca284 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-4.avif?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=21fb18e66c5457da963acb2db58be4b1 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-4.avif?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=9e22d4de8a47a82529831e5f141c41a1 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-4.avif?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=45c8ad7ee9437f554253d2ec068b6683 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-4.avif?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=0a7b346fc1d3c78b8081bb5d862f2e23 2500w" />
</Frame>

#### Chunk Utilization Plus

For Chunk Utilization Plus, we experimented with a number of ways to frame the task. Our most effective framing, which powers the Chunk Utilization metric in the Galileo product, involves

* Pre-splitting each chunk into sentences

* Providing the LLM with brief, unique string keys which it can use to refer to individual chunk sentences (to improve token efficiency)

* Asking the LLM to specify, using the keys, which sentences in each chunk were used

Here are the results of one of our evals for Utilization. This is the same style of plot used above for Completeness -- see that section for information on how to read it.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-5.avif?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=67bc9977627130563bb91f1551616598" data-og-width="800" width="800" data-og-height="262" height="262" data-path="images/rag-q-m-5.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-5.avif?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=51da30208e19545b81af125306834624 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-5.avif?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=82fc3ca58325d865fc3b03357660c9f5 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-5.avif?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=fa2830ce13867e925ff4a2ef4fd590b6 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-5.avif?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f1b9f73a1089b1d0f16c414d83551c29 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-5.avif?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=fce309008a51d050e56e471a1c746b0a 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-q-m-5.avif?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=aa5db3ae228a760afebb937d20dd38fd 2500w" />
</Frame>
