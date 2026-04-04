# Source: https://docs.augmentcode.com/models/available-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Available Models

> The LLMs currently available in Augment and how we use them.

## Current models

Augment uses world-class large language models together with our Context Engine. We currently support the following models:

* Claude Haiku 4.5 by Anthropic
* Claude Opus 4.5 by Anthropic
* Claude Sonnet 4 by Anthropic
* Claude Sonnet 4.5 by Anthropic
* GPT-5.1 by OpenAI
* GPT-5.2 by OpenAI

## Choosing a model

You can select the model directly using the Model Picker in the Augment.

* In VS Code and JetBrains, open the Augment panel and use the model dropdown near the input box to switch models.
* In Auggie CLI, use the `/model` slash command or pass the `--model` flag with the desired model.
* Your selection applies only to Agent in that workspace and can be changed at any time.

If you don't pick a model, Augment will use your last selection or the default set by your organization.

## Model pricing

Augment uses a credit-based pricing system. Different models consume credits at different rates based on their capabilities and costs:

* **Sonnet 4.5**: Baseline credit consumption for balanced, complex tasks
* **Opus 4.5**: \~167% of Sonnet's cost - most capable model for the hardest tasks
* **Haiku 4.5**: \~30% of Sonnet's cost - ideal for quick, simple tasks
* **GPT-5.1**: \~75% of Sonnet's cost - great for medium-complexity work
* **GPT-5.2**: \~133% of Sonnet's cost - enhanced reasoning for complex tasks

<Card title="Credit-Based Pricing" icon="credit-card" href="/models/credit-based-pricing">
  Learn more about credit costs, see detailed examples, and discover tips for optimizing your credit usage
</Card>

## Feature compatibility

Both models support the core Augment Agent features:

* Deep code understanding with Augment's Context Engine
* Tool use (integrations and MCP), file edits, and multi-step planning

Some behaviors (e.g., wording or style) may vary slightly between models. We'll continue to refine prompts and guardrails to provide a consistent developer experience.

## Notes and transparency

* We may roll out model updates gradually. If you're part of a staged rollout, different workspaces or teammates may see updates at different times.
* For troubleshooting, you can share the request ID with our support team; they can confirm which model handled a specific request.

If you have questions about model availability or want to participate in early access programs, please reach out via Support.
