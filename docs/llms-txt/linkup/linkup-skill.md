# Source: https://docs.linkup.so/pages/documentation/tutorials/linkup-skill.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Linkup Skill

> A reusable knowledge module that teaches AI agents how to use Linkup effectively

<video autoPlay muted loop playsInline width="100%" style={{borderRadius: '8px'}}>
  <source src="https://mintcdn.com/linkup-8b5c238e/J-qMLhfHdKUVC8PD/images/linkup-skill-demo.mp4?fit=max&auto=format&n=J-qMLhfHdKUVC8PD&q=85&s=0d1b97515551a147d41282b3638cf97e" type="video/mp4" data-path="images/linkup-skill-demo.mp4" />
</video>

## What is a Skill?

Skills are **knowledge for AI agents**, not tools. They are markdown-based instruction files that agents load automatically when a task matches the skill's purpose. The agent then follows the skill's guidance to make better API calls — choosing the right parameters, writing effective queries, and avoiding common mistakes.

Skills work across agent environments: Claude Code, Cursor, Windsurf, Cline, GitHub Copilot, and any platform that supports instruction files.

Skills are installed with the Skill Comand Line Interface (CLI). Read more [here](https://skills.sh/).

<Card title="Install the Linkup Skill" icon="link" href="https://github.com/LinkupPlatform/skills" arrow="true" cta="Click here">
  Teach your agent how to use Linkup with our official Skill. Redirects to source code repository with SKILL.md file.
</Card>

***

## The Linkup Skill

The **linkup-search** skill teaches agents how to use the Linkup API effectively. Instead of relying on generic tool descriptions, agents get structured guidance on:

* **Query construction** — A 3-step reasoning framework: what inputs do I have? Where does the data live? Do I need to chain steps?
* **Depth selection** — When to use `standard` vs `deep`, with decision rules and worked examples
* **Output types** — Choosing between `searchResults`, `sourcedAnswer`, and `structured` based on the use case
* **Effective prompting** — Keyword-style for simple lookups, instruction-style for complex extraction
* **Scraping and fetch** — When to scrape within search vs use the `/fetch` endpoint directly
* **Advanced patterns** — LinkedIn extraction, parallel multi-query coverage, sequential search chains
* **MCP setup** — Configuration for Claude Code, VS Code, Cursor, and Claude Desktop

***

## Installation

```bash  theme={null}
npx skills add LinkupPlatform/skills
```

This installs the skill into your project. Agents will automatically reference it when handling web search, content extraction, or research tasks via Linkup.

### Supported environments

| Environment                | How it works                                |
| -------------------------- | ------------------------------------------- |
| **Claude Code**            | Skill is loaded automatically when relevant |
| **Cursor**                 | Loaded via `.cursor/rules/`                 |
| **Windsurf**               | Loaded via `.windsurfrules`                 |
| **Cline / GitHub Copilot** | Loaded from project-level instruction files |

***

## How It Works

When an agent encounters a task that involves web search, company research, or content extraction:

1. The agent detects it has access to Linkup tools (via MCP or SDK)
2. The skill's instructions are loaded into the agent's context
3. The agent follows the skill's reasoning framework to decide depth, query style, and output type
4. The result: more accurate queries, fewer wasted API calls, better results

No manual invocation needed — skills activate when relevant.

***

## Example

Without the skill, an agent might write:

```
query: "Tell me about Datadog"
depth: "standard"
```

With the skill, the agent reasons through the framework and writes:

```
query: "Find Datadog's pricing page. Scrape it. Extract plan names, per-host prices, and included features for each tier."
depth: "deep"
```

The skill teaches agents to be specific about what to retrieve, where to look, and how to chain steps — the same way an experienced developer would use the API.

***

## Resources

* [GitHub Repository](https://github.com/LinkupPlatform/skills) — Source code and SKILL.md
* [Prompting Guide](/pages/documentation/tutorials/prompting) — Detailed query writing best practices
* [Agent Instructions](/pages/documentation/tutorials/agent-instructions) — System prompt snippets and integration patterns
* [MCP Setup](/pages/integrations/mcp/mcp) — Connect Linkup to your agent via MCP

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).