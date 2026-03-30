# Source: https://docs.linkup.so/pages/documentation/tutorials/agent-instructions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Instructions for AI Agents

> Context for your AI agents to use linkup effectively — covers MCP, SDKs, skills, and agent design patterns

Give your AI agents access to accurate, real-time web data. This guide covers how to integrate Linkup into any agent environment — from MCP-based setups to custom-built pipelines — and how to configure your agent to use Linkup effectively.

You can give this page as context to your agent. We also publish a [**Linkup Skill**](/pages/documentation/tutorials/linkup-skill) — a reusable knowledge module that agents can install and reference automatically for better Linkup API usage.

<Card title="Install the Linkup Skill" icon="graduation-cap" href="/pages/documentation/tutorials/linkup-skill">
  One command: `npx skills add LinkupPlatform/skills` — works with Claude Code, Cursor, Windsurf, and more.
</Card>

***

## 1. System Prompt Snippet

Copy this into your agent's system prompt, tool description, or `CLAUDE.md` file. It teaches any LLM how to use Linkup well.

```text  theme={null}
## Linkup Web Search — Usage Instructions

You have access to Linkup, a web search and content extraction API. Follow these rules:

### Before Writing a Query
Reason through three questions in order:
1. INPUTS: What do I already have? A URL? A company name? A topic?
   - If I have a URL → scrape it directly, don't search for it.
2. DATA LOCATION: Where does the data I need live?
   - In search snippets (facts, dates, names, short claims) → search is enough.
   - On full web pages (tables, specs, detailed content) → need to scrape.
   - Not sure → default to standard.
3. SEQUENCING: Do I need to chain steps?
   - Parallel searches only → standard.
   - Find URL then scrape it, or scrape then search again → deep.
   - Scrape multiple URLs → deep.

### Search Depth
- depth="standard" (€0.005): multiple parallel searches + scrape one provided URL. Cannot scrape multiple URLs. Cannot chain search → scrape.
- depth="deep" (€0.05): up to 10 iterative steps. Can scrape multiple URLs. Can chain search → scrape. Can run new searches based on extracted information.
- When uncertain, default to standard.

### Query Style
- Simple factual lookups → short keyword queries.
- Complex extraction → natural language instructions: what to find, where to look, what to extract.
- Broad research → "Run several searches with adjacent keywords." Works in standard.
- Don't ask Linkup to analyze or reason. Ask it to retrieve. You do the thinking.

### Scraping Rules
- Standard: scrape one URL provided in the prompt. That's it.
- Deep: scrape multiple URLs, scrape URLs discovered during search.

### Output Type
- outputType="searchResults": raw sources for you to process (default for agents).
- outputType="sourcedAnswer": natural language answer with citations.
- outputType="structured" + JSON schema: machine-parseable data.

### Fetch
- Use /fetch instead of /search for a single known URL.
- Always set renderJs=true unless the page is static HTML.
```

> **Where to put this:** System prompt, `CLAUDE.md`, `.cursorrules`, MCP tool descriptions, or framework tool docstrings. It works everywhere.

***

## 2. Query Construction — Examples

Your query should tell Linkup **what to retrieve**, not what to think. The system prompt snippet above teaches the 3-step reasoning (inputs → data location → sequencing). Here's how it plays out:

```
Task: Get a company's pricing
Reasoning: no URL → need to find it → then scrape → sequential → deep
→ query: "Find the pricing page for {company}. Scrape it. Extract plan names, prices, and features."
```

```
Task: Get a company's latest funding round
Reasoning: no URL → answer lives in snippets → no chaining → standard
→ query: "Find {company}'s latest funding round amount and date"
```

```
Task: Extract data from a known URL
Reasoning: have URL → just scrape → no chaining → standard or /fetch
→ query: "Scrape https://example.com/pricing. Extract plan names, prices, and included features."
```

```
Task: Build an ICP from a company's web presence
Reasoning: no URL → need full pages → find then scrape multiple → deep
→ query: "Find and scrape {company}'s homepage, use case pages, and 2-3 recent blog posts. Extract: industries mentioned, company sizes referenced, job titles targeted, and pain points addressed."
```

For more query examples and patterns, see the [Prompting Guide](/pages/documentation/get-started/prompting).

***

## 3. Output Types

For most agent use cases, use `searchResults`.

| Output Type     | Returns                         | Best For                                          |
| --------------- | ------------------------------- | ------------------------------------------------- |
| `searchResults` | Array of `{name, url, content}` | Agent-side reasoning, RAG, multi-source synthesis |
| `sourcedAnswer` | Answer + source citations       | User-facing chatbots, Q\&A                        |
| `structured`    | JSON matching your schema       | CRM updates, data pipelines, enrichment           |

For details on structured output schemas, see [API Reference](/pages/documentation/api-reference/endpoint/post-search).

***

## 4. `/fetch` Endpoint

Use `/fetch` instead of `/search` when your agent already has the exact URL. It's faster, cheaper, and returns clean markdown.

Always set `renderJs: true` (most sites need it).

[Full fetch documentation →](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-fetch)

***

## 5. Integration by Environment

* **MCP:** [Linkup MCP Server](https://docs.linkup.so/pages/integrations/mcp/mcp)
* **VS Code:** [MCP Configuration Examples](https://docs.linkup.so/pages/integrations/mcp/mcp#configuration-examples)
* **Claude Desktop:** [Linkup + Claude](https://docs.linkup.so/pages/integrations/linkup-claude)
* **Smithery CLI:** [Quick Start](https://docs.linkup.so/pages/integrations/mcp/mcp#quick-start-with-smithery)
* **Python SDK:** [Python](https://docs.linkup.so/pages/sdk/python/python)
* **LangChain:** [LangChain Integration](https://docs.linkup.so/pages/integrations/langchain)
* **CrewAI:** [CrewAI Integration](https://docs.linkup.so/pages/integrations/crewai)
* **Node.js:** [TypeScript / JavaScript SDK](https://docs.linkup.so/pages/sdk/js/js)
* **No-Code / Low-Code:** [Integrations](https://docs.linkup.so/pages/integrations/integrations)
* **cURL / HTTP:** [Quickstart](https://docs.linkup.so/pages/documentation/get-started/quickstart)

***

## To Go Further

* [Prompting Guide](/pages/documentation/get-started/prompting) — Detailed best practices
* [Prompt Optimizer](https://prompt.linkup.so) — Optimize prompts interactively
* [Prompt Templates](https://prompt.linkup.so/templates) — Ready-to-use templates
* [API Reference](/pages/documentation/api-reference/endpoint/post-search) — Full endpoint docs
* [MCP Server (GitHub)](https://github.com/LinkupPlatform/linkup-mcp-server) — Source and setup
* [Integrations](/pages/integrations/integrations) — n8n, Make, Zapier, and more

Need help? Reach out at [support@linkup.so](mailto:support@linkup.so), on [Discord](https://discord.com/invite/9q9mCYJa86), or [book a 15-minute call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9).


Built with [Mintlify](https://mintlify.com).