# Source: https://docs.chatling.ai/ai-agent/ai-settings.md

# AI settings

To configure the agent's AI settings, click the `Settings` button in the sidebar and select `AI`.

<img src="https://chatling-assets.b-cdn.net/access-agent-ai-settings.jpg" width="450" alt="Agent AI settings" />

## Available settings

### AI Model

The AI model that the agent will use to think, plan, and generate answers to the user queries.

Every model has different capabilities and costs. We recommend testing with different models in the [Playground](/ai-agent/playground) to see which one works best for your agent.

### Temperature

Controls randomness/creativity in the Agent's writing and decision-making.

Lower = more deterministic; Higher = more varied.

* **0.0-0.3 (Precise)**: Best for support, policy-bound replies, data extraction, or when strict adherence to facts and formats is required.

* **0.4-0.6 (Balanced)**: Good general setting for helpful responses with light creativity.

* **0.7-1.0 (Creative)**: Use for brainstorming, marketing copy, or when variety is desirable. Expect less consistency.

**Tips**

* If your Agent must follow exact steps (e.g., collecting parameters for an HTTP Request), keep temperature low.
* Raise temperature only where tone/creativity matters and accuracy isn't compromised.

### Instructions

Define the Agent's role, goals, guardrails, and style (often called the "system prompt").

Here's some of the things you can include in the instructions:

* **Role & purpose**: What the Agent is for and what success looks like.
* **Scope & boundaries**: What it should/shouldn't answer.
* **Tone & language**: Brand voice, formality level, and multilingual behavior (auto-detect language; reply in user's language).
* **Compliance & safety**: Any legal disclaimers, restricted topics, PII handling, and masking sensitive values.
* **Formatting**: Preferred reply structure (short summaries, bullet points, tables).
