# Source: https://mastra.ai/guides/getting-started/quickstart

# Mastra Quickstart

The `create mastra` CLI command is the quickest way to get started. It walks you through setup and creates example agents, workflows, and tools for you to run locally or adapt.

If you need more control over the setup, see the [manual installation guide](https://mastra.ai/docs/getting-started/manual-install). You can also use [`mastra init`](https://mastra.ai/reference/cli/mastra) for existing projects.

## Before you begin

- You'll need an API key from a supported [model provider](https://mastra.ai/models). If you don't have a preference, use [OpenAI](https://mastra.ai/models/providers/openai).

## Initialize Mastra

You can run `create mastra` anywhere on your machine.

When prompted, choose a provider (e.g. OpenAI) and enter your key:

**npm**:

```bash
npm create mastra@latest
```

**pnpm**:

```bash
pnpm create mastra
```

**Yarn**:

```bash
yarn create mastra
```

**Bun**:

```bash
bunx create-mastra
```

This creates a new directory for your project with a `src/mastra` folder containing an example weather agent and the following files:

- `index.ts`: Entry point for all Mastra-related code and configuration
- `agents/weather-agent.ts`: A weather agent with a prompt that uses the tool
- `tools/weather-tool.ts`: A tool to fetch weather for a given location
- `workflows/weather-workflow.ts`: A workflow that runs the weather agent
- `scorers/weather-scorer.ts`: A scorer to evaluate the weather agent's responses

Depending on your choices, you'll also end up with [Mastra Skills](https://mastra.ai/docs/build-with-ai/skills) or the [MCP Docs Server](https://mastra.ai/docs/build-with-ai/mcp-docs-server) installed.

> **Tip:** You can use [flags](https://mastra.ai/reference/cli/create-mastra) with `create mastra` like `--no-example` to skip the example weather agent or `--template` to start from a specific [template](https://mastra.ai/templates).

## Test your agent

Once setup is complete, follow the instructions in your terminal to start the Mastra dev server, then open Studio at [localhost:4111](http://localhost:4111).

Try asking about the weather. If your API key is set up correctly, you'll get a response:

[Studio](https://mastra.ai/docs/getting-started/studio) lets you rapidly build and prototype agents without needing to build a UI. Once you're ready, you can integrate your Mastra agent into your app using the guides below.

## Next steps

- Integrate Mastra with your frontend framework: [Next.js](https://mastra.ai/guides/getting-started/next-js), [React](https://mastra.ai/guides/getting-started/vite-react), or [Astro](https://mastra.ai/guides/getting-started/astro)
- Read more about [Mastra's features](https://mastra.ai/docs)
- Learn how you can [build Mastra with AI](https://mastra.ai/docs/getting-started/build-with-ai)
- Build an agent from scratch following one of our [guides](https://mastra.ai/guides)
- Watch conceptual guides on our [YouTube channel](https://www.youtube.com/@mastra-ai) and [subscribe](https://www.youtube.com/@mastra-ai?sub_confirmation=1)