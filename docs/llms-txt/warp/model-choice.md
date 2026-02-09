# Source: https://docs.warp.dev/agent-platform/agent/using-agents/model-choice.md

# Model Choice

## Available models

Warp lets you choose from a curated set of Large Language Models (LLMs) to power your Agentic Development Environment.

**Warp supports the following models:**

* OpenAI:
  * `GPT-5.2` (*low, medium,* *high* and *extra high* reasoning)
  * `GPT-5.2 Codex` (*low, medium, high*, and *extra high* reasoning)
  * `GPT-5.1 Codex Max` (*low, medium, high*, and *extra high* reasoning)
  * `GPT-5.1 Codex` *(low, medium,* and *high* reasoning)
  * `GPT-5.1` (*low, medium,* and *high* reasoning)
  * `GPT-5` (*low, medium,* and *high* reasoning)
* Anthropic:
  * `Claude Opus 4.5` with thinking mode
  * `Claude Sonnet 4.5` with thinking mode
  * `Claude Opus 4.1`
  * `Claude Haiku 4.5`
  * `Claude Sonnet 4`
* Google:
  * `Gemini 3 Pro`
  * `Gemini 2.5 Pro`
* z.ai: `GLM 4.6` (hosted in the US, by [Fireworks AI](https://fireworks.ai/models/fireworks/glm-4p6))

### Auto Models

Warp also offers three *Auto* modes that intelligently select the best model for your task based on the context and request type:

1. **Auto (Cost-efficient)**: Optimizes for lower credit consumption while maintaining strong output quality, helping extend your available usage.
2. **Auto (Responsive)**: Prioritizes the highest-quality results using the fastest available model, though it may consume credits more quickly.
3. **Auto (Genius)**: Adapts to the complexity of your task and selects Warp’s most capable model when it’s worth it. Best for deep debugging, architecture decisions, and /plan-style sessions where you want maximum reasoning quality.

All Auto models perform well across all agent workflows and are ideal if you prefer Warp to manage model selection dynamically.

### How to change models

You can use the model picker in your prompt input to quickly switch between models. The currently active model appears directly in the input editor.

<figure><img src="https://769506432-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAULCelT4yIUOcSwWWvPk%2Fuploads%2Fgit-blob-4c4f5c6af395a6aa3835eca0cf62f3073b145274%2Fnew-models-oct-2025.png?alt=media" alt=""><figcaption><p>Model selector in Warp's Universal Input.</p></figcaption></figure>

To change models, click the displayed model name (for example, *Claude Sonnet 4.5*) to open a dropdown with all supported options. Your selection will automatically persist for future prompts.

### Model fallback

Warp uses a model fallback system to ensure uninterrupted service if your selected model becomes temporarily unavailable due to provider outages or capacity issues.

**How it works:**

* If your selected model isn't available, Warp automatically uses a fallback model from a predefined chain to continue your conversation without errors.
* As soon as your originally selected model becomes available again, Warp automatically switches back to it.
* The fallback model is selected to provide comparable quality and capabilities to your original choice.

### Configuring models per Agent Profile

You can configure the base and planning models for each [Agent Profiles & Permissions](https://docs.warp.dev/agent-platform/agent/using-agents/agent-profiles-permissions), defining the Agent’s autonomy, tool access, and other permissions.

Edit your default profile or more profiles directly in `Settings > AI > Agents > Profiles`.

<figure><img src="https://769506432-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAULCelT4yIUOcSwWWvPk%2Fuploads%2Fgit-blob-fbc1b3e768939a6b52ca17d7da2cc995907b0eae%2Fbase-planning-model-pickers.png?alt=media" alt=""><figcaption><p>Model choice example, where the base model is Auto (Claude 4 Sonnet) and the planning model is o3.</p></figcaption></figure>

### Zero Data Retention Policies

Warp integrates with multiple Large Language Model (LLM) providers to power its AI-driven features.

**These providers include, but are not limited to:**

* OpenAI
* Anthropic
* Google
* Fireworks AI

Warp has executed **Zero Data Retention (ZDR)** agreements with these providers. This means that, by default across all plans:

* LLM providers commit not to train their models on any customer-generated data processed through Warp’s services.
* LLM providers commit to delete inputs and outputs after generating the relevant output, within a fixed time period.

Warp enforces these commitments through both technical measures and contractual safeguards with the LLM providers.
