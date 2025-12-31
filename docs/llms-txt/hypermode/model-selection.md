# Source: https://docs.hypermode.com/agents/model-selection.md

# Model Selection Guide

> Select the optimal model for your agent based on your goals and use case.

Choosing the right model is essential to building effective agents. This guide
helps you evaluate trade-offs, pick the right model for your use case, and
iterate quickly.

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/agents/model-selection.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b0c0050cd589381e88cae8625622eca7" alt="Select your model" width="896" height="696" data-path="images/agents/model-selection.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/agents/model-selection.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f114e397f20aadadadd13f9d698256bb 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/agents/model-selection.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=04c542b20a7467da5aedd73beea45d73 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/agents/model-selection.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=9bb7327ecb661f2f1cddd57148414b97 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/agents/model-selection.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=84bd7b3fb7836316ddc52d9f148e800e 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/agents/model-selection.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f65676cac0d85141f969cd96291e4258 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/agents/model-selection.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=231ed5bc469477d9cb04259e18326a54 2500w" data-optimize="true" data-opv="2" />

## Key considerations

* **Accuracy and output quality:** Advanced logic, mathematical problem-solving,
  and multi-step analysis may require high-capability models.
* **Domain expertise:** Performance varies by domain (for example, creative
  writing, code, scientific analysis). Review model benchmarks or test with your
  own examples.
* **Context window:** Long documents, extensive conversations, or large
  codebases require models with longer context windows.
* **Embeddings:** For semantic search or similarity, consider embedding models.
  These aren't for text generation.
* **Latency:** Real-time apps may need low-latency responses. Smaller models (or
  “Mini,” “Nano,” and “Flash” variants) typically respond faster than larger
  models.

## Models by task / use case at a glance

| Task / use case                         | Example models                                     | Key strengths                                  | Considerations                       |
| --------------------------------------- | -------------------------------------------------- | ---------------------------------------------- | ------------------------------------ |
| General-purpose conversation            | Claude 4 Sonnet, GPT-4.1, Gemini Pro               | Balanced, reliable, creative                   | May not handle edge cases as well    |
| Complex reasoning and research          | Claude 4 Opus, O3, Gemini 2.5 Pro                  | Highest accuracy, multi-step analysis          | Higher cost, quality critical        |
| Creative writing and content            | Claude 4 Opus, GPT-4.1, Gemini 2.5 Pro             | High-quality output, creativity, style control | High cost for premium content        |
| Document analysis and summarization     | Claude 4 Opus, Gemini 2.5 Pro, Llama 3.3           | Handles long inputs, comprehension             | Higher cost, slower                  |
| Real-time apps                          | Claude 3.5 Haiku, GPT-4o Mini, Gemini 1.5 Flash 8B | Low latency, high throughput                   | Less nuanced, shorter context        |
| Semantic search and embeddings          | OpenAI Embedding 3, Nomic AI, Hugging Face         | Vector search, similarity, retrieval           | Not for text generation              |
| Custom model training & experimentation | Llama 4 Scout, Llama 3.3, DeepSeek, Mistral        | Open source, customizable                      | Requires setup, variable performance |

<Note>
  Hypermode provides access to the most popular open source and commercial
  models through [Hypermode Model Router documentation](/model-router). We're
  constantly evaluating model usage and adding new models to our catalog based
  on demand.
</Note>

## Get started

You can change models at any time in your agent settings. Start with a
general-purpose model, then iterate and optimize as you learn more about your
agent's needs.

1. [**Create an agent**](/create-agent) with GPT-4.1 (default).
2. **Define clear instructions and [connections](/connections)** for the agent's
   role.
3. **Test with real examples** from your workflow.
4. **Refine and iterate** based on results.
5. **Evaluate alternatives** once you understand patterns and outcomes.

<Tip>
  **Value first, optimize second.** Clarify the task requirements before tuning
  for specialized capabilities or cost.
</Tip>

## Comparison of select large language models

| Model                | Best For                            | Considerations                          | Context Window+      | Speed     | Cost++   |
| -------------------- | ----------------------------------- | --------------------------------------- | -------------------- | --------- | -------- |
| **Claude 4 Opus**    | Complex reasoning, long docs        | Higher cost, slower than lighter models | Very long (200K+)    | Moderate  | \$\$\$\$ |
| **Claude 4 Sonnet**  | General-purpose, balanced workloads | Less capable than Opus for edge cases   | Long (100K+)         | Fast      | \$\$\$   |
| **GPT-4.1**          | Most tasks, nuanced output          | Higher cost, moderate speed             | Long (128K)          | Moderate  | \$\$\$   |
| **GPT-4.1 Mini**     | High-volume, cost-sensitive         | Less nuanced, shorter context           | Medium (32K-64K)     | Very Fast | \$\$     |
| **GPT o3**           | General chat, broad compatibility   | May lack latest features/capabilities   | Medium (32K-64K)     | Fast      | \$\$     |
| **Gemini 2.5 Pro**   | Up-to-date info                     | Limited access, higher cost             | Long (128K+)         | Moderate  | \$\$\$   |
| **Gemini 2.5 Flash** | Real-time, rapid responses          | Shorter context, less nuanced           | Medium (32K-64K)     | Very Fast | \$\$     |
| **Llama 4 Scout**    | Privacy, customization, open source | Variable performance                    | Medium-Long (varies) | Fast      | \$       |

<sup>
  \+ Context window sizes are approximate and may vary by deployment/version.
</sup>

<sup>++ Relative cost per 1K tokens (\$ = lowest, \$\$\$\$ = highest)</sup>
