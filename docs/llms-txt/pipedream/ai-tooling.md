# Source: https://pipedream.com/docs/ai-tooling.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using AI tooling with Pipedream

> Enable your AI tools to help integrate Pipedream Connect

Pipedream provides developer tools to make it easy to work with Pipedream Connect alongside whatever AI tools you use. You can use these tools to get instant access to Pipedream's documentation, API references, and code examples directly in your AI assistant or IDE.

## AI contextual menu

Pipedream's documentation includes built-in tools to make it easy to share content with AI assistants:

### Copy a page as Markdown

Press <kbd>Command</kbd> + <kbd>C</kbd> (<kbd>Ctrl</kbd> + <kbd>C</kbd> on Windows) on any page in the docs to copy it as Markdown to your clipboard. You can then paste this directly into your AI assistant for context-aware help.

### Send a page to your AI assistant

Click the AI menu in the top right of any page in the docs to send the current page to ChatGPT, Claude, or Perplexity to easily get immediate help with the specific topic you're reading about.

## LLM-optimized documentation

Pipedream's documentation is optimized for AI consumption with automatically generated `llms.txt` and `llms-full.txt` files:

### llms.txt

Similar to how a sitemap helps search engines, `llms.txt` provides a structured index of all the pages in the docs. AI tools can use this to quickly understand our documentation structure and find relevant content.

View it at: [pipedream.com/docs/llms.txt](https://pipedream.com/docs/llms.txt)

### llms-full.txt

For comprehensive context, `llms-full.txt` flattens the entire docs site into a single file. You can provide this URL to AI tools for more accurate responses about Pipedream.

View it at: [pipedream.com/docs/llms-full.txt](https://pipedream.com/docs/llms-full.txt)

## Pipedream Docs MCP Server

For a more integrated development experience, you can add the Pipedream Docs MCP ([Model Context Protocol](https://modelcontextprotocol.io/)) server directly to your IDE. This enables your AI assistant or agent to directly access and search Pipedream's documentation without leaving your development environment.

<Note>
  If you're looking to use Pipedream MCP to add thousands of tools to the app you're building, see [these docs](/connect/mcp/developers).
</Note>

### Benefits

Adding the Pipedream Docs MCP server to your development environment provides:

* **Instant docs access**: Your AI assistant can search and reference Pipedream docs without leaving your IDE
* **Faster development**: Reduce context switching between documentation and code
* **Accurate answers**: AI responses are grounded in our official documentation

### Installation

To add the Pipedream Docs MCP server, use this URL:

```bash  theme={null}
https://pipedream.com/docs/mcp
```

The Pipedream Docs MCP server works with any IDE or AI assistant that supports MCP, including:

* Cursor
* VSCode
* Claude Code
* claude.ai
* Any other MCP-compatible IDE

### What you can do

With the Pipedream Docs MCP server enabled, your AI assistant can help you:

* Find the right Connect SDK methods and parameters
* Generate code examples for common integration patterns
* Troubleshoot authentication and API issues
* Discover available endpoints and capabilities

### Example prompts

Here are some example prompts you can use with your AI assistant once the MCP server is configured:

* "How do list apps in Pipedream Connect?"
* "Show me how to send a Slack message on behalf of my users with Pipedream Connect"
* "How can I add Pipedream MCP to my agent?"
* "How do I deploy a Google Sheets trigger for my end users?"

## Next steps

* Go through the [Pipedream Connect Quickstart](/connect/quickstart) to get started
* Check out the [SDK playground](https://pipedream.com/connect/demo) to see Connect in action
* Use [Pipedream Chat](https://chat.pipedream.com) to see how you can add Pipedream MCP to your AI app

Built with [Mintlify](https://mintlify.com).
