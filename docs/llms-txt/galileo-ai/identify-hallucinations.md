# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/identify-hallucinations.md

# Identify Hallucinations

> How to use Galileo Evaluate to find Hallucinations

*Hallucination* can have many definitions. In the realm of closed-book question answering, hallucinations may pertain to *Correctness* (i.e. is my output factually consistent). In open-book scenarios, hallucinations might be linked to the grounding of information or *Adherence* (i.e., whether the facts presented in my response "**adhere to**" or "**are grounded in**" the documents I supplied). Hallucinations happen when models produce responses outside of the context being forced upon the model via the prompt.Galileo aims to help you identify and solve these hallucinations.

## Guardrail Metrics

Galileo's Guardrail Metrics are built to help you shed light on where and why the model produces an undesirable output.

### Uncertainty

Uncertainty measures the model's certainty in its generated tokens. Because uncertainty works at the token level, it can be a great way of identifying *where* in the response the model started hallucinating.

When prompted for citations of papers on the phenomenon of "Human & AI collaboration", OpenAI's ChatGPT responds with this:

<Frame caption="ChatGPT's response to a prompt asking for citations. Low, Medium and High Uncertainty is colored in Green, Yellow and Red.">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/hallucinations.png" />
</Frame>

A quick Google Search reveals that the cited paper doesn't exist. The arxiv link takes us to a completely [unrelated paper](https://arxiv.org/abs/1903.03097).

While not every 'high uncertainty' token (shown in red) will contain hallucinations, and not every hallucination will contain high uncertainty tokens, we've seen a strong correlation between the two. Looking for *Uncertainty* is usually a good first step in identifying hallucinations.

*Note:* Uncertainty requires log probabilities and only works for certain models for now.

### Context Adherence

Context Adherence measures whether your model's response was purely based on the context provided, i.e. the response didn't state any facts not contained in the context provided. For RAG users, *Context Adherence* is a measurement of hallucinations.

If a response is *grounded* in the context (i.e. it has a value of 1 or close to 1), it only contains information given in the context. If a response is *not grounded* (i.e. it has a value of 0 or close to 0), it's likely to contain facts not included in the context provided to the model.

<Frame caption="Explanation provided by the Chainpoll methodology for a hallucination metric called Context Adherence, ideally suited for RAG systems">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/hallucinations-2.png" />
</Frame>

### Correctness

*Correctness* measures whether the facts stated in the response are based on real facts. This metric requires additional LLM calls.

If the response is *factually consistent* (value close to 1), the information is likely be correct. We use our proprietary **ChainPoll Technique** ([Research Paper Link](https://arxiv.org/abs/2310.18344)) using a combination of Chain-of-Thought prompting and Ensembling techniques to provide the user with a 0-1 score and an explanation to the Hallucination. The explanation why something was deemed incorrect or not can be seen upon hovering over the metric value.

<Info>
  Note

  Because **correctness** relies on external Large Language Models and their knowledge base, its results are only as good as those models' knowledge base.
</Info>

<Frame caption="ChainPoll Workflow">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/hallucinations-3.webp" />
</Frame>

## What if I have my own definition of Hallucination?

Enterprise users often have their own unique interpretations of what constitutes hallucinations. Galileo supports [*Custom Metrics*](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics#custom-metrics) and incorporates [*Human Feedback and Ratings*](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-with-human-feedback), empowering you to tailor Galileo Prompt to align with your specific needs and the particular definition of hallucinations relevant to your use case.

With Galileo's Experimentation and Evaluation features, you can systematically iterate on your prompts and models, ensuring a rigorous and scientific approach to improving the quality of responses and addressing hallucination-related challenges.
