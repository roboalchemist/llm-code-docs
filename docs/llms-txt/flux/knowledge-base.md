# Source: https://docs.flux.ai/reference/knowledge-base.md

# Flux Knowledge Base

Flux Knowledge Base allows you to teach Flux how you work—once, and it remembers forever. This persistent memory system helps Flux retain your design preferences, best practices, and project-specific guidance across conversations.

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/fwwu4ubistg3tjkg8rxbu130gmlk54jtxxc4ctcuwpyirn4teygd5nw1hdgwcg2n.png)

Overview

The Knowledge Base feature enables Flux to automatically apply your design context during conversations without requiring you to repeat the same instructions. Whether it's your preferred components, naming conventions, review checklists, or layout guidelines—Knowledge Base helps Flux work like someone who's been on your team for years.

## What is Knowledge?

Knowledge is persistent memory for Flux that stores information about how you design, allowing it to apply that context automatically during conversations.

You can save Knowledge about:

- Preferred components or manufacturers
- Naming and labeling conventions
- Derating protocols
- Testing protocols

Each Knowledge entry includes:

- A summary of the instruction
- When it should be used (its "trigger")
- Where it applies (user-wide or project-specific)

> Knowledge entries are automatically suggested based on your conversations but can also be created manually.

## How Knowledge Works

### Getting Started with Knowledge

1. Open a project in Flux
2. Interact with Flux normally.
3. Look for Knowledge suggestions—and start teaching.

You can also add Knowledge manually from your profile or the project sidebar:

### Automatic Suggestion Generation

As you chat with Flux, it listens for teachable moments in your conversations. For example:

```none
"I usually use TI for voltage boosters."
"We prefix signal nets with SIG_."
"Make sure to check DRC before routing."
```



Flux will then suggest turning these statements into Knowledge entries.

You'll see suggestions in the Knowledge tab, where you can:

- **Accept** (save it as-is)
- **Edit** (customize the wording or trigger)
- **Reject** (ignore or dismiss)

Once accepted, Flux will reference that Knowledge automatically when relevant to future conversations.

## Where Knowledge Lives

Knowledge entries can be stored at two different levels:

### User-Level Knowledge

Stored in your profile and applied across all your projects. Ideal for:

- Personal preferences
- Naming conventions
- General workflow habits

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/6dv4eids5wf4bn7o5h8xsx9wyuxkiluemimangsxaokkxgmzq7ud8r2pechh00ej.png)

### Project-Level Knowledge

Tied to a specific Flux project. Ideal for:

- Project-specific constraints
- Unique design rules

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/j50ch6qjmnlug6m26o47tylsbq03501320o9rw8dzbvb4fc7b24yn9xo4l5160wt.png)

> Project-level Knowledge takes precedence over user-level Knowledge when both apply to the same situation.

## Example Use Cases

Here are a few ways you might use Knowledge:

| Scenario | Knowledge Entry | 
| ---- | ---- | 
| You always use TI boost converters | "When selecting voltage boosters, prefer Texas Instruments." | 
| You use a specific test point label format | "Use TP_ prefix for all test point nets." | 
| Your team has a DRC-first layout policy | "Always run DRC before starting layout." | 
| You want Flux to avoid certain part families | "Avoid recommending parts from ABC123 series." | 


## Using Knowledge in Conversations

When Flux uses a Knowledge entry in a response, you'll see a reference under the "Accessed Knowledge" section in the chat. You can click to view which entry was used, and make edits if needed.

This builds trust—and lets you fine-tune how Flux applies your expertise over time.

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/50e3enabl37gaukhis46rjcysu3598kutedxfji7939fhecjwdtzo07az9j2ck5x.png)

> You can disable specific Knowledge entries temporarily without deleting them if you don't want them to apply to a particular conversation.

## Best Practices

Think of Flux like onboarding a new team member. The better you teach it, the more helpful it becomes.

- **Start small.** Save preferences you often repeat.
- **Set clear triggers.** The more specific, the better the match.
- **Keep it organized.** Use project-level entries when information isn't universal.
- **Review and prune.** Clean up entries as your workflows evolve.

## What's Next

- [Getting Started with Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Learn the basics of using Flux in your workflow
- [Adapt Flux to Your Goals](/tutorials/getting-started-copilot/adapt-copilot-to-your-goals) - Customize Flux for your specific design needs
- [Flux Use Cases](https://docs.flux.ai/flux/tutorials/copilot-use-cases) - Discover different ways to leverage Flux in your workflow
- [AI for Hardware Design](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design) - Understand how AI can enhance your hardware design process