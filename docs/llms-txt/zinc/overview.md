# Source: https://zinc-staging.vercel.app/docs/v2/agent-skills/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Universal Checkout Skill

> Let AI agents buy anything with a URL using the Zinc API.

The **Universal Checkout Skill** is an [Agent Skill](https://agentskills.io) that enables AI agents to place and manage e-commerce orders through the [Zinc API](https://zinc.com). Once installed, you can ask your AI agent to buy products from online retailers, check order statuses, and list recent orders — all through natural language.

<CardGroup cols={3}>
  <Frame caption="Order anything">
    <video src="https://mintcdn.com/zinc/JcZ_00yHjkmfiMBl/videos/agent-skills/claw-demo-1.mp4?fit=max&auto=format&n=JcZ_00yHjkmfiMBl&q=85&s=fc80277ca75010ace7d79133488b883c" controls muted loop data-path="videos/agent-skills/claw-demo-1.mp4" />
  </Frame>

  <Frame caption="Visual search">
    <video src="https://mintcdn.com/zinc/JcZ_00yHjkmfiMBl/videos/agent-skills/claw-demo-2.mp4?fit=max&auto=format&n=JcZ_00yHjkmfiMBl&q=85&s=c887518353c5ac9a75ec1de8a418d184" controls muted loop data-path="videos/agent-skills/claw-demo-2.mp4" />
  </Frame>

  <Frame caption="Handle complex tasks">
    <video src="https://mintcdn.com/zinc/JcZ_00yHjkmfiMBl/videos/agent-skills/claw-demo-3.mp4?fit=max&auto=format&n=JcZ_00yHjkmfiMBl&q=85&s=d8b2c4930218c87505b0e1a38ff6b555" controls muted loop data-path="videos/agent-skills/claw-demo-3.mp4" />
  </Frame>
</CardGroup>

## What is an Agent Skill?

An Agent Skill is a declarative specification (a `SKILL.md` file) that teaches AI agents how to interact with an API. There's no executable code — the skill simply provides instructions, endpoint definitions, and safety guidelines that the agent follows.

Agent Skills use **progressive disclosure**: at startup only the skill name and description are loaded. The full instructions are read into context only when the agent detects a matching task, keeping your agent fast and focused.

## What Can It Do?

The Universal Checkout Skill gives your agent three capabilities:

| Capability             | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| **Place orders**       | Buy products from supported retailers using a product URL |
| **Check order status** | Look up the current status and tracking info for an order |
| **List orders**        | View recent orders placed through Zinc                    |

<Warning>
  Placing an order spends real money from your Zinc account. The agent will
  always confirm with you before submitting an order.
</Warning>

## Supported Platforms

The Universal Checkout Skill works with any agent platform that supports the [Agent Skills](https://agentskills.io) standard, including:

* [OpenClaw](https://openclaw.ai)
* [Claude Code](https://claude.ai/code)
* [Gemini CLI](https://github.com/google-gemini/gemini-cli)

## Prerequisites

Before you begin, you'll need:

1. A **Zinc API key**. [Sign up at app.zinc.com](https://app.zinc.com) to get one.
2. Funds deposited in your Zinc account to place orders.
3. A supported AI agent platform (see above).

## Next Steps

<CardGroup cols={2}>
  <Card title="Setup" icon="wrench" href="/v2/agent-skills/setup">
    Install and configure the skill for your platform.
  </Card>

  <Card title="Usage Guide" icon="cart-shopping" href="/v2/agent-skills/usage">
    Learn how to place orders and track them with your agent.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).