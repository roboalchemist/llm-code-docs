# Source: https://docs.helicone.ai/guides/prompt-engineering/use-thread-of-thought-prompting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Thread-of-Thought prompting

> Maintain a coherent line of reasoning between LLM interactions by building on previous ideas. 

## What is Thread-of-Thought (ThoT) prompting

Thread-of-Thought is an approach that extends [chain-of-thought prompting](use-chain-of-thought-prompting) by maintaining a continuous, evolving reasoning process across multiple, related prompts.
It's like having a conversation where each new idea builds on previous ones, helping the LLM to think more deeply and keep track of all the details as we explore a topic.

## How to implement Thread-of-Thought prompting

1. **Provide the original query and context.**
2. **Use a clear structure.** Clearly mark sections with headings, bullet points, or other delimiters for easier parsing.
3. **Follow conventions.** For instance, use Markdown headings or JSON keys.
4. **Use follow-up prompts.** Build upon previous thoughts and insights to create a more natural, ongoing thought process.

## Example

**Initial Prompt:**

> Let's develop an AI-powered travel planning application. Begin by identifying a key pain point in current travel planning experiences.

*Model responds with a challenge in traveling planning, e.g., overwhelming information.*

**Follow-up:**

> Great observation! Outline a preliminary concept for an AI travel companion that can address these personalization challenges.

*Model suggests what the travel planning platform can offer*

**Next in thread:**

> Let's explore the technological capabilities we need to create such a personalized travel experience. What specific AI and data technologies would power this platform?

*Model suggests the technologies needed to create the platform*

**Continuing:**

> Consider the user experience and data collection. How would the AI gather and utilize user preferences while maintaining privacy and providing increasing personalization?

*Model suggests how the AI can gather and utilize user preferences while maintaining privacy and providing increasing personalization*

*... The thread continues, building upon previous responses*

## Why use Thread-of-Thought prompting

* Promotes coherent reasoning and logical flow over time.
* Improved context handling builds upon previously established knowledge.
* Better problem decomposition breaks large challenges into manageable steps.
* The model is flexible and adapts its reasoning based on evolving information.
* This approach mimics the natural human-like thought progression.

## Tips for effective Thread-of-Thought prompting

* Begin with a well-defined initial prompt.
* Encourage referencing of earlier points as needed.
* Periodically summarize key points to maintain focus.
* Regularly filter or refocus context to avoid overload.
* Structured Progression: Move through logical phases of reasoning.
* Allow revision of earlier ideas to refine them.

***

<Accordion title="Need more help?">
  Additional questions or feedback? Reach out to
  [help@helicone.ai](mailto:help@helicone.ai) or [schedule a
  call](https://cal.com/team/helicone/helicone-discovery) with us.
</Accordion>
