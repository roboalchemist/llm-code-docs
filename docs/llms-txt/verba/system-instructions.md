# Source: https://docs.verba.ink/guides/system-instructions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# System instructions

> How system instructions work, where to set them, limits, and how they interact with memory/knowledge/training.

## What system instructions are

System instructions are the verb's persistent behavior rules.

Quick facts:

* Set in Dashboard -> Bot -> AI Engine -> Behavior
* Field name: `systemInstructions`
* Limit: `8000` characters

They should define:

* how the verb should behave
* response format and tone constraints
* uncertainty policy (what to do when information is missing)
* boundaries and refusal style

They should not be used as a dump for raw documentation or long transcripts.

## Interaction with other configuration layers

| Layer                | What it should contain                            |
| -------------------- | ------------------------------------------------- |
| `systemInstructions` | Behavior rules and output formatting policy       |
| Training examples    | Input/output style patterns and phrasing examples |
| Long-term memory     | Durable facts/preferences from conversation       |
| Knowledge entries    | Structured factual/reference information          |
| Conversation context | Recent turns from active chat/thread/session      |

## Practical precedence model

Use this order for authoring:

1. Put behavior policy in system instructions.
2. Put canonical facts in knowledge entries.
3. Put durable user/world facts in long-term memory.
4. Use training examples for style and recurring patterns.

If these layers conflict, clean up older memory/knowledge entries and keep one
canonical source of truth.

## Best-practice template

```text  theme={null}
Role:
- You are Verba Documentation Assistant.

Behavior:
- Be factual and concise.
- Do not speculate.

Output format:
- Start with a direct answer.
- Then provide short sections with bullets.
- Include numbered steps for procedures.

Uncertainty:
- If docs context is insufficient, say what is missing and ask for the exact page/topic.
```

## Common mistakes

<AccordionGroup>
  <Accordion title="Putting factual docs only in system instructions">
    Put facts in knowledge entries; keep system instructions focused on behavior policy.
  </Accordion>

  <Accordion title="Conflicting rules">
    Avoid mixing contradictory rules like "be very short" and "be extremely detailed" in the same instruction set.
  </Accordion>

  <Accordion title="No uncertainty policy">
    Include explicit fallback behavior for missing info to reduce hallucinations.
  </Accordion>

  <Accordion title="Overlong and vague instructions">
    Keep instructions concrete and testable; split long policy into clear bullets.
  </Accordion>
</AccordionGroup>

## Related guides

* [AI engine settings](/guides/ai-engine)
* [Memory and knowledge](/guides/memory-and-knowledge)
* [Bot settings reference](/guides/bot-settings-reference)

Built with [Mintlify](https://mintlify.com).
