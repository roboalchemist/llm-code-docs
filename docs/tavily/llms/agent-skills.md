# Source: https://docs.tavily.com/documentation/agent-skills.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tavily Agent Skills

> Official skills that define best practices for working with the Tavily API. Useful for AI agents like Claude Code, Codex, or Cursor.

<CardGroup cols={2}>
  <Card title="GitHub" icon="github" href="https://github.com/tavily-ai/skills" horizontal>
    `/tavily-ai/skills`
  </Card>

  <Card title="Get API Key" icon="key" href="https://app.tavily.com" horizontal>
    Sign up at tavily.com
  </Card>
</CardGroup>

## Why Use These Skills?

These official skills define best practices for working with the Tavily API, going beyond just using the endpoints. They give AI agents low-level control to build custom web tooling directly in your development environment.

These skills bring Tavily's services (search, extract, crawl, research) right where you work. The real-time context these tools provide significantly enhances your agent's capabilities for development tasks.

Most importantly, the **tavily-best-practices** skill turns your AI agent into a true Tavily expert. Instead of reading API docs, just ask your agent how to integrate Tavily into your project. All API best practices are baked in, dramatically accelerating your build process.

## What You Can Build

Copy-paste these prompts into your AI agent and start building:

<AccordionGroup>
  <Accordion title="AI Chatbot with Real-Time Search">
    Build a chatbot that can answer questions about current events and up-to-date information.

    **Try these prompts:**

    ```
    /tavily-best-practices Build a chatbot that integrates Tavily search to answer questions with up-to-date web information
    ```

    ```
    /tavily-best-practices Add Tavily search to my internal company chatbot so it can answer questions about our competitors
    ```
  </Accordion>

  <Accordion title="News Dashboard with Sentiment Analysis">
    Create a live news dashboard that tracks topics and analyzes sentiment.

    **Try these prompts:**

    ```
    /tavily-best-practices Build a website that refreshes daily with Tesla news and gives a sentiment score on each article
    ```

    ```
    /tavily-best-practices Create a news monitoring dashboard that tracks AI industry news and sends daily Slack summaries
    ```
  </Accordion>

  <Accordion title="Lead Enrichment Tool">
    Build tools that automatically enrich leads with company data from the web.

    **Try these prompts:**

    ```
    /tavily-best-practices Build a lead enrichment tool that uses Tavily to find company information from their website
    ```

    ```
    /tavily-best-practices Create a script that takes a list of company URLs and extracts key business information
    ```
  </Accordion>

  <Accordion title="Competitive Intelligence Agent">
    Build an autonomous agent that monitors competitors and surfaces insights.

    **Try these prompts:**

    ```
    /tavily-best-practices Build a market research tool that crawls competitor documentation and pricing pages
    ```

    ```
    /tavily-best-practices Create an agent that monitors competitor product launches and generates weekly reports
    ```
  </Accordion>
</AccordionGroup>

<Tip>
  The `/tavily-best-practices` skill is your fastest path to production. Describe what you want to build and your agent generates working code with best practices baked in.
</Tip>

## Installation

### Prerequisites

<AccordionGroup>
  <Accordion title="Required" icon="wrench">
    * [Tavily API key](https://app.tavily.com/home) - Sign up for free
    * An AI agent that supports skills (Claude Code, Codex, Cursor, etc.)
  </Accordion>
</AccordionGroup>

### Step 1: Configure Your API Key

Add your Tavily API key to your agent's environment. For Claude Code, add it to your settings file:

<CodeGroup>
  ```bash macOS theme={null}
  # Open your Claude settings file
  open -e "$HOME/.claude/settings.json"

  # Or with VS Code
  code "$HOME/.claude/settings.json"
  ```

  ```bash Linux theme={null}
  # Open your Claude settings file
  nano "$HOME/.claude/settings.json"

  # Or with VS Code
  code "$HOME/.claude/settings.json"
  ```

  ```bash Windows theme={null}
  code %USERPROFILE%\.claude\settings.json
  ```
</CodeGroup>

Add the following configuration:

```json  theme={null}
{
  "env": {
    "TAVILY_API_KEY": "tvly-YOUR_API_KEY"
  }
}
```

<Warning>Replace `tvly-YOUR_API_KEY` with your actual Tavily API key from [app.tavily.com](https://app.tavily.com/home)</Warning>

### Step 2: Install the Skills

Run this command in your terminal:

```bash  theme={null}
npx skills add tavily-ai/skills
```

### Step 3: Restart Your Agent

After installation, restart your AI agent to load the skills.

## Available Skills

<AccordionGroup>
  <Accordion title="Tavily Best Practices" icon="book" defaultOpen="true">
    Build production-ready Tavily integrations with best practices baked in. Reference documentation for implementing web search, content extraction, crawling, and research in agentic workflows, RAG systems, or autonomous agents.

    **Invoke explicitly:**

    ```
    /tavily-best-practices
    ```

    **Example prompts:**

    * "Add Tavily search to my internal company chatbot so it can answer questions about our competitors"
    * "Build a lead enrichment tool that uses Tavily to find company information from their website"
    * "Create a news monitoring agent that tracks mentions of our brand using Tavily search"
    * "Implement a RAG pipeline that uses Tavily extract to pull content from industry reports"
  </Accordion>

  <Accordion title="Search" icon="magnifying-glass">
    Search the web using Tavily's LLM-optimized search API. Returns relevant results with content snippets, scores, and metadata.

    **Invoke explicitly:**

    ```
    /search
    ```

    **Example prompts:**

    * "Search for the latest news on AI regulations"
    * "/search current React best practices"
    * "Search for Python async patterns"
  </Accordion>

  <Accordion title="Research" icon="magnifying-glass-chart">
    Get AI-synthesized research on any topic with citations. Supports structured JSON output for integration into pipelines.

    **Invoke explicitly:**

    ```
    /research
    ```

    **Example prompts:**

    * "Research the latest developments in quantum computing"
    * "/research AI agent frameworks and save to report.json"
    * "Research the competitive landscape for AI coding assistants"
  </Accordion>

  <Accordion title="Crawl" icon="spider-web">
    Crawl any website and save pages as local markdown files. Ideal for downloading documentation, knowledge bases, or web content for offline access or analysis.

    **Invoke explicitly:**

    ```
    /crawl
    ```

    **Example prompts:**

    * "Crawl the Stripe API docs and save them locally"
    * "/crawl [https://docs.example.com](https://docs.example.com)"
    * "Download the Next.js documentation for offline reference"
  </Accordion>

  <Accordion title="Extract" icon="file-lines">
    Extract content from specific URLs using Tavily's extraction API. Returns clean markdown/text from web pages.

    **Invoke explicitly:**

    ```
    /extract
    ```

    **Example prompts:**

    * "Extract the content from this article URL"
    * "/extract [https://example.com/blog/post](https://example.com/blog/post)"
    * "Extract content from these three documentation pages"
  </Accordion>
</AccordionGroup>

## Usage Examples

### Automatic Skill Invocation

Your AI agent will automatically use Tavily skills when appropriate. Simply describe what you need:

```
Research the latest developments in AI agents and summarize the key trends
```

```
Search for the latest news on AI regulations
```

```
Crawl the Stripe API docs and save them locally
```

### Explicit Skill Invocation

You can also invoke skills directly using slash commands:

```
/research AI agent frameworks and save to report.json
```

```
/search current React best practices
```

```
/crawl https://docs.example.com
```

```
/extract https://example.com/blog/post
```

```
/tavily-best-practices
```

## Claude Code Plugin

If you're using Claude Code specifically, you can also install the skills as a plugin.

### Step 1: Configure Your API Key

Add your Tavily API key to your Claude Code settings file:

```bash  theme={null}
code ~/.claude/settings.json
```

Add the following configuration:

```json  theme={null}
{
  "env": {
    "TAVILY_API_KEY": "tvly-YOUR_API_KEY"
  }
}
```

### Step 2: Install the Skills

Run these commands inside Claude Code:

```
/plugin marketplace add tavily-ai/skills
```

```
/plugin install tavily@skills
```

### Step 3: Restart Claude Code

Clear your session and restart to load the plugin:

```
/clear
```

Then press `Ctrl+C` to restart.
