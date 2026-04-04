# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/identify-hallucinations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Identify Hallucinations

> How to use Galileo Evaluate to find Hallucinations

*Hallucination* can have many definitions. In the realm of closed-book question answering, hallucinations may pertain to *Correctness* (i.e. is my output factually consistent). In open-book scenarios, hallucinations might be linked to the grounding of information or *Adherence* (i.e., whether the facts presented in my response "**adhere to**" or "**are grounded in**" the documents I supplied). Hallucinations happen when models produce responses outside of the context being forced upon the model via the prompt.Galileo aims to help you identify and solve these hallucinations.

## Guardrail Metrics

Galileo's Guardrail Metrics are built to help you shed light on where and why the model produces an undesirable output.

### Uncertainty

Uncertainty measures the model's certainty in its generated tokens. Because uncertainty works at the token level, it can be a great way of identifying *where* in the response the model started hallucinating.

When prompted for citations of papers on the phenomenon of "Human & AI collaboration", OpenAI's ChatGPT responds with this:

<Frame caption="ChatGPT's response to a prompt asking for citations. Low, Medium and High Uncertainty is colored in Green, Yellow and Red.">
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=106263ab7b8ade6730974bb94008168a" data-og-width="974" width="974" data-og-height="284" height="284" data-path="images/hallucinations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=f6b1d003ad04287bdf12c6476e8443ce 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=3493a7e54e5690359de8132658da90b1 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=41500cd24aea82955f88046916bce121 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=437dade5fda445f73e4977402e657a10 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=2966be447fc42b630aeb54eec11f78c5 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=634219930d10b3e9ce8e406ae8d0db5f 2500w" />
</Frame>

A quick Google Search reveals that the cited paper doesn't exist. The arxiv link takes us to a completely [unrelated paper](https://arxiv.org/abs/1903.03097).

While not every 'high uncertainty' token (shown in red) will contain hallucinations, and not every hallucination will contain high uncertainty tokens, we've seen a strong correlation between the two. Looking for *Uncertainty* is usually a good first step in identifying hallucinations.

*Note:* Uncertainty requires log probabilities and only works for certain models for now.

### Context Adherence

Context Adherence measures whether your model's response was purely based on the context provided, i.e. the response didn't state any facts not contained in the context provided. For RAG users, *Context Adherence* is a measurement of hallucinations.

If a response is *grounded* in the context (i.e. it has a value of 1 or close to 1), it only contains information given in the context. If a response is *not grounded* (i.e. it has a value of 0 or close to 0), it's likely to contain facts not included in the context provided to the model.

<Frame caption="Explanation provided by the Chainpoll methodology for a hallucination metric called Context Adherence, ideally suited for RAG systems">
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-2.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=6c8586239b6fdb4626adbd4086d3b557" data-og-width="344" width="344" data-og-height="420" height="420" data-path="images/hallucinations-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-2.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=c1dd109fe1eab936b8de67144ae43146 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-2.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7be0533c62e542cda6765221c15f5032 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-2.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=2835a5a3816fae83ef129459c2b7bfd8 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-2.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=1b6881407937f13236e8f823b57ad3d9 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-2.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=8c88088e6447185e7bd54cee9aed2e32 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-2.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=6ab5c1e70311e6f583c44627037e45e6 2500w" />
</Frame>

### Correctness

*Correctness* measures whether the facts stated in the response are based on real facts. This metric requires additional LLM calls.

If the response is *factually consistent* (value close to 1), the information is likely be correct. We use our proprietary **ChainPoll Technique** ([Research Paper Link](https://arxiv.org/abs/2310.18344)) using a combination of Chain-of-Thought prompting and Ensembling techniques to provide the user with a 0-1 score and an explanation to the Hallucination. The explanation why something was deemed incorrect or not can be seen upon hovering over the metric value.

<Info>
  Note

  Because **correctness** relies on external Large Language Models and their knowledge base, its results are only as good as those models' knowledge base.
</Info>

<Frame caption="ChainPoll Workflow">
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-3.webp?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=5de16a36889361f00d80a69da6d3f7ff" data-og-width="2280" width="2280" data-og-height="1138" height="1138" data-path="images/hallucinations-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-3.webp?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=4e149eeff9e4f97d768083ecdf80390d 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-3.webp?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e83c8c7aa2dec0b3c4225b8fc79ff1f1 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-3.webp?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=6812dd7248f96ae3ec5496529c455ea7 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-3.webp?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=35b6be04cfeb863df550877fcf3e6f8f 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-3.webp?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7bb7f51af4af2d01393f840dbaeec9c1 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/hallucinations-3.webp?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=2879ccd98b132a91206703beb8b93da9 2500w" />
</Frame>

## What if I have my own definition of Hallucination?

Enterprise users often have their own unique interpretations of what constitutes hallucinations. Galileo supports [*Custom Metrics*](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics#custom-metrics) and incorporates [*Human Feedback and Ratings*](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-with-human-feedback), empowering you to tailor Galileo Prompt to align with your specific needs and the particular definition of hallucinations relevant to your use case.

With Galileo's Experimentation and Evaluation features, you can systematically iterate on your prompts and models, ensuring a rigorous and scientific approach to improving the quality of responses and addressing hallucination-related challenges.
