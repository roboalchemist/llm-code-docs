# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/understand-your-metric-s-values.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Metric Values | Galileo Observe How-To

> Gain insights into your metric values in Galileo Observe with explainability features, including token-level highlighting and generated explanations for better analysis.

Our metrics have explainability built-in, helping you understand which parts of the input or output are leading to certain outcomes. We have two types of explainability: Highlighting and generated Explanations.

## Explainability via Token Highlighting

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-1.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a9dc4851ef7637106cbbd2c09aab2403" width="400" data-og-width="1044" data-og-height="800" data-path="images/metrics-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-1.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=516b4d30bf3daf56f7aeb9b543e8e7ce 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-1.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=12564944d653d8f9179d1dd8831188a6 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-1.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=ae478b54873f0908e53abf40f5989d6f 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-1.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7db4a1429450b432b08907907e2e31fa 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-1.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0d5b162a6342117f3de6aa1e759e9ed5 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-1.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=f4e618137e0b651e8132c9ddb80deaae 2500w" />
</Frame>

When looking at a workflow in the expanded view, some metric values will have an <Icon icon="eye" />icon next to them. Clicking on it will turn token-level highlighting on the input / output section of the node.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-2.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=fb7d25a9c02c5e2093e49d0f6d0045ee" width="400" data-og-width="594" data-og-height="246" data-path="images/metrics-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-2.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=65a2e130c6571ae53eac3fa90e1d2140 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-2.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c1c9b05be92b990f0c9a2c1c152b2c44 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-2.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=e7c8cf9c2aac97a00663f86441957b3d 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-2.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d696ab403e25bfd763d332893612cf0c 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-2.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2966b8543ec4168b0ad8841e71b48800 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-2.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7e9b52c49c38e3fe862e09cea5d0acb3 2500w" />
</Frame>

The following metrics have token-level highlighting:

| Metric                                                                                                                         | Where to see it                        |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| [PII](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information)                              | Input or Output into LLM or Chat Nodes |
| [Prompt Perplexity](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-perplexity)                               | Input into LLM or Chat Node            |
| [Uncertainty](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty)                                           | Output of LLM or Chat Node             |
| [Context Adherence (Luna)](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) | Output of LLM or Chat Node             |
| [Chunk Relevance (Luna)](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-relevance)                            | Output of Retriever Node               |
| [Chunk Utilization (Luna)](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) | Output of Retriever Node               |

## Explainability via Explanations

For metrics powered by [Chainpoll](/galileo/gen-ai-studio-products/galileo-ai-research/chainpoll), we provide an explanation or rationale generated by LLMs. 🪄 next to metric values indicate that this metric has an explanation available. This explanation will include the reasoning the model followed to get to its conclusion. To view the explanation, simply hover over the metric value.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-5.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=eb13d01f020ffff156475eef9ae4634b" width="300" data-og-width="778" data-og-height="826" data-path="images/metrics-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-5.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0b59e11cb10ef8b73666545bd091883c 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-5.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=96e9287439c60c89ec4a35f2be9cd770 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-5.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7a3e5e9353f097b49a9b48d9dd13e31a 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-5.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a6a76444b4d1926ce0df717288920054 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-5.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=ec4453832b2e64cd8c3f2345dac42cd2 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/metrics-5.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6ad0c3a118cfd1001c606f7b3aa82328 2500w" />
</Frame>

The following metrics have generated explanations:

* [*Correctness*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/correctness)

* [*Context Adherence Plus*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus)

* [*Completeness Plus*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus)
