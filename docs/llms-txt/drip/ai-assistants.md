# Source: https://docs.drip.re/developer/ai-assistants.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Coding Assistants

> Use DRIP docs with AI tools (MCP, llms.txt, Markdown export) for faster development

Accelerate development by connecting your favorite AI coding assistants to the DRIP docs and API. This page shows the fastest, safest ways to give AI the right context.

<Warning>
  Never paste secrets into public chats. When AI tools ask for API keys, provide them securely via the tool’s secret manager or environment settings.
</Warning>

## Model Context Protocol (MCP)

The Model Context Protocol lets AI tools query and call APIs directly against the DRIP docs.

* Install the DRIP MCP server:

```bash  theme={"dark"}
npx mint-mcp add driprewards
```

* Reference: [Model Context Protocol](https://mintlify.com/docs/ai/model-context-protocol)

### Use with Cursor

1. Run the install command above.
2. Open the command palette → “Open MCP settings” and confirm “driprewards” is listed.
3. In chat, ask: “What tools do you have available?” You should see the DRIP docs search tool and any exposed endpoints.

### Use with Claude

* From any docs page, use the contextual menu → “Open in Claude” to start a conversation with this page as context.
* Alternatively, add the DRIP docs MCP server using Claude’s Connectors flow if your workspace supports it.

## llms.txt and llms-full.txt

llms files help AI index your docs efficiently.

* **Mintlify guide**: [llms.txt](https://mintlify.com/docs/ai/llmstxt)
* DRIP docs expose:
  * `https://docs.drip.re/llms.txt` (site map for LLMs)
  * `https://docs.drip.re/llms-full.txt` (entire docs in one file)

How to use:

* Add one of the above URLs in your AI editor’s settings so it can index DRIP docs for context-aware answers.
* In tools that support it, reference docs explicitly in prompts (e.g., “Use DRIP docs for this task”).

## Markdown export

Get clean Markdown versions of any page for better AI ingestion.

* **Mintlify guide**: [Markdown export](https://mintlify.com/docs/ai/markdown-export)
* Add `.md` to any page URL on these docs (e.g., `https://docs.drip.re/developer/app-development.md`).
* Many tools have a shortcut to copy a page as Markdown (Command + C in Mintlify).

## Recommended workflows

* **Quick search + call generation**: Ask your AI to “Find the points balance update endpoint in DRIP, generate Node/TS code using fetch with retries.”
* **Fix missing scopes**: “Given this error, which scopes are required and how do I request reauthorization?”
* **Docs-first answer**: “Summarize app authorization flow from DRIP docs, then produce a checklist for publishing.”

<Info>
  If you expose API tools via MCP, the AI will prompt you for your DRIP API key at call time. The key is handled by the client tool, not stored in the docs system.
</Info>

Built with [Mintlify](https://mintlify.com).
