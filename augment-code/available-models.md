# Source: https://docs.augmentcode.com/models/available-models.md

# Available Models

> The LLMs currently available in Augment and how we use them.

## Current models

Augment uses world-class large language models together with our Context Engine. We currently support the following models:

* Claude Haiku 4.5 by Anthropic
* Claude Sonnet 4 by Anthropic
* Claude Sonnet 4.5 by Anthropic
* GPT-5 by OpenAI

## Choosing a model

You can select the model directly using the Model Picker in the Augment.

* In VS Code and JetBrains, open the Augment panel and use the model dropdown near the input box to switch models.
* In Auggie CLI, use the `/model` slash command or pass the `--model` flag with the desired model.
* Your selection applies only to Agent in that workspace and can be changed at any time.

If you don't pick a model, Augment will use your last selection or the default set by your organization.

## Feature compatibility

Both models support the core Augment Agent features:

* Deep code understanding with Augment's Context Engine
* Tool use (integrations and MCP), file edits, and multi-step planning

Some behaviors (e.g., wording or style) may vary slightly between models. We'll continue to refine prompts and guardrails to provide a consistent developer experience.

## Notes and transparency

* We may roll out model updates gradually. If you're part of a staged rollout, different workspaces or teammates may see updates at different times.
* For troubleshooting, you can share the request ID with our support team; they can confirm which model handled a specific request.

If you have questions about model availability or want to participate in early access programs, please reach out via Support.
