# Source: https://docs.augmentcode.com/models/credit-based-pricing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Credit-Based Pricing

> Understand how credits work and how different models consume credits at different rates.

## Overview

Augment uses a credit-based pricing system where different models consume credits at different rates to reflect their power and cost. This gives you the flexibility to choose the right model for each task based on complexity and budget.

## Credit costs by model

Each model consumes credits at different rates based on its capabilities and underlying costs. Here's how the models compare:

| Model                 | Credits per task\* | Relative cost   | Best for                                                                                                                 |
| :-------------------- | :----------------- | :-------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **Claude Sonnet 4.5** | 293 credits        | Baseline (100%) | Balanced capability. Ideal for medium or large tasks and is optimized for complex or multi-step work.                    |
| **Claude Opus 4.5**   | 488 credits        | 167% of Sonnet  | Most capable model. Best for the hardest tasks requiring deep reasoning, nuanced understanding, and exceptional quality. |
| **Claude Haiku 4.5**  | 88 credits         | 30% of Sonnet   | Lightweight, fast reasoning. Best for quick edits and small tasks.                                                       |
| **GPT-5.1**           | 219 credits        | 75% of Sonnet   | Advanced reasoning and context. Builds great plans and works well for medium-size tasks.                                 |
| **GPT-5.2**           | 390 credits        | 133% of Sonnet  | Enhanced reasoning capabilities. Excellent for complex tasks requiring long chains of thought.                           |

<Info>
  \*Based on a standard medium-complexity task. Actual credit consumption varies based on task complexity, context size, and response length.
</Info>

## Example tasks

To illustrate the credit differences, here are examples of tasks and how much they cost with each model.

### Sonnet task: Fix a 500 error in an API endpoint

> The `/api/users/:id` endpoint returns 500 errors when a user has no associated organization. Add null checking and return a 404 with a clear error message instead. Test that users with organizations still work correctly.

**Credit cost:** 293 credits with Sonnet 4.5

| Model          | Credits     | Savings              |
| :------------- | :---------- | :------------------- |
| **Sonnet 4.5** | 293 credits | —                    |
| **Opus 4.5**   | 488 credits | Use for harder tasks |
| **GPT-5.2**    | 390 credits | Use for harder tasks |
| **Haiku 4.5**  | 88 credits  | 205 credits saved    |
| **GPT-5.1**    | 219 credits | 74 credits saved     |

***

### Opus task: Design and implement a multi-tenant billing system

> Our B2B SaaS platform needs a multi-tenant billing system. Currently we have a simple Stripe integration for single subscriptions, but we need to support:
>
> 1. **Usage-based billing**: Track API calls per tenant with tiered pricing (first 10k calls free, then \$0.001/call)
> 2. **Seat-based licensing**: Charge per active user with volume discounts
> 3. **Hybrid plans**: Combine base subscription + usage overages
> 4. **Invoice generation**: Monthly invoices with line-item breakdown by workspace
> 5. **Billing isolation**: Each tenant's billing data must be completely isolated
>
> Design the database schema, implement the metering service, integrate with Stripe's usage-based billing API, and ensure we handle edge cases like mid-cycle plan changes, prorations, and failed payments. Consider how this will scale to 10k+ tenants.

**Credit cost:** 976 credits with Opus 4.5

## Monitoring credit usage

You can track your credit consumption in multiple places:

### In your IDE

* **VS Code**: View credit usage in the Augment panel
* **JetBrains**: Check the Augment tool window for usage stats
* **Auggie CLI**: Monitor credits used per session

### On the web

Visit [app.augmentcode.com](https://app.augmentcode.com) to access detailed dashboards that show:

* Total credits used by your team
* Credit usage per team member
* Breakdown by model and activity
* Usage trends over time
* Remaining credits in your plan

<Note>
  Team administrators can access more detailed analytics to help optimize team usage and identify opportunities to save credits by using more efficient models for appropriate tasks.
</Note>

## Understanding your usage breakdown

When you view your usage analytics, you'll see credits organized by both **model** and **activity type**. Here's what each activity type means:

### Session types

These are the main session types you can use with Augment:

| Activity        | What it is                               |
| :-------------- | :--------------------------------------- |
| **Chat**        | Conversational chat session              |
| **Agent**       | Local agent session (in your IDE)        |
| **RemoteAgent** | Cloud-based agent session (asynchronous) |
| **CliAgent**    | Command-line agent session (Auggie CLI)  |

### Optional features

| Activity            | What it is                                                                                   |
| :------------------ | :------------------------------------------------------------------------------------------- |
| **Prompt Enhancer** | Appears when you use the Prompt Enhancer feature to improve your prompts before sending them |
| **Code Review**     | Automated code review for pull requests (when enabled for your repository)                   |

### Background activities

Augment performs lightweight processing in the background to keep your experience smooth:

| Activity                | What it does                                                              |
| :---------------------- | :------------------------------------------------------------------------ |
| **Context Compression** | Summarizes conversation history to keep long sessions fast and responsive |
| **System**              | General background processing that helps Augment work smoothly            |

These background activities use a small fraction of your total credit consumption. In most workflows, they're a minor part of overall usage.

## Tips for optimizing credit usage

1. **Match the model to the task**: Use Haiku for simple tasks, GPT-5.1 for medium tasks, Sonnet for complex work, and Opus for the hardest challenges
2. **Be specific in your prompts**: Clear, detailed instructions help models work more efficiently
3. **Break down large tasks**: Sometimes splitting a complex task into smaller ones can be more credit-efficient
4. **Review usage patterns**: Check your dashboards regularly to identify optimization opportunities
5. **Set team guidelines**: Establish best practices for model selection within your team

## Frequently asked questions

<AccordionGroup>
  <Accordion title="How are credits calculated?">
    Credits are consumed based on the model used, the size of the context (code being analyzed), and the length of the response generated. More complex tasks that require analyzing more code or generating longer responses will consume more credits.
  </Accordion>

  <Accordion title="What happens if I run out of credits?">
    When you run out of credits, you'll need to upgrade your plan or wait until your credits reset at the beginning of your next billing cycle. Team administrators can purchase additional credits or upgrade the team plan at any time.
  </Accordion>

  <Accordion title="Can I switch models mid-conversation?">
    Currently, you can switch models mid-conversation in **Auggie CLI** using the `/model` command. Each message will consume credits based on the model selected for that specific message. Model switching mid-conversation is not yet available in the IDE extensions (VS Code, JetBrains), but you can change your model selection between separate conversations.
  </Accordion>
</AccordionGroup>

## Related resources

<CardGroup cols={2}>
  <Card title="Available Models" icon="brain" href="/models/available-models">
    Learn about the different AI models available in Augment
  </Card>

  <Card title="Pricing Plans" icon="credit-card" href="https://augmentcode.com/pricing">
    View current pricing plans and credit allocations
  </Card>

  <Card title="Teams Admin Guide" icon="users" href="/teams/teams-admin-guide">
    Manage team subscriptions and billing
  </Card>

  <Card title="Blog: Credit-Based Plans" icon="newspaper" href="https://www.augmentcode.com/blog/our-new-credit-based-plans-are-now-live">
    Read the full announcement about credit-based pricing
  </Card>
</CardGroup>
