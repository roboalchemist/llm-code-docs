# Source: https://exa.ai/docs/reference/x-search-claude-skill.md

> ## Documentation Index

> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt

> Use this file to discover all available pages before exploring further.

# X/Twitter Search

> This guide shows you how to set up a Claude skill and Exa MCP that helps you search tweets and Twitter/X discussions.

<Card title="Copy and Paste in Claude Code">
  Click the copy button on the code block below and paste it into Claude Code. Claude will automatically set up both the MCP connection and the skill for you.
</Card>

````text

claude mcp add --transport http exa "https://mcp.exa.ai/mcp?tools=web_search_advanced_exa"


Step 2: Add this Claude skill

---
name: web-search-advanced-tweet
description: Search tweets and Twitter/X content using Exa advanced search. Limited filter support - text and domain filters are NOT supported. Use when searching for tweets, Twitter/X discussions, or social media sentiment.
context: fork
---

# Web Search Advanced - Tweet Category

## Tool Restriction (Critical)

ONLY use `web_search_advanced_exa` with `category: "tweet"`. Do NOT use other categories or tools.

## Filter Restrictions (Critical)

The `tweet` category has **LIMITED filter support**. The following parameters are **NOT supported** and will cause 400 errors:

- `includeText` - NOT SUPPORTED
- `excludeText` - NOT SUPPORTED
- `includeDomains` - NOT SUPPORTED
- `excludeDomains` - NOT SUPPORTED
- `moderation` - NOT SUPPORTED (causes 500 server error)

## Supported Parameters

### Core
- `query` (required)
- `numResults`
- `type` ("auto", "fast", "deep", "neural")

### Date filtering (ISO 8601) - Use these instead of text filters!
- `startPublishedDate` / `endPublishedDate`
- `startCrawlDate` / `endCrawlDate`

### Content extraction
- `textMaxCharacters` / `contextMaxCharacters`
- `enableHighlights` / `highlightsNumSentences` / `highlightsPerUrl` / `highlightsQuery`
- `enableSummary` / `summaryQuery`

### Additional
- `additionalQueries` - useful for hashtag variations
- `livecrawl` / `livecrawlTimeout` - use "preferred" for recent tweets

## Token Isolation (Critical)

Never run Exa searches in main context. Always spawn Task agents:
- Agent calls `web_search_advanced_exa` with `category: "tweet"`
- Agent merges + deduplicates results before presenting
- Agent returns distilled output (brief markdown or compact JSON)
- Main context stays clean regardless of search volume

## When to Use

Use this category when you need:
- Social discussions on a topic
- Product announcements from company accounts
- Developer opinions and experiences
- Trending topics and community sentiment
- Expert takes and threads

## Examples

Recent tweets on a topic:

```text
  "category": "tweet",
  "startPublishedDate": "2025-01-01",
  "numResults": 20,
  "type": "auto",
  "livecrawl": "preferred"
}

```text
  "query": "launching announcing new open source release",
  "category": "tweet",
  "startPublishedDate": "2025-12-01",
  "numResults": 15,
  "type": "auto"
}

```text
  "query": "developer experience DX frustrating painful",
  "category": "tweet",
  "numResults": 20,
  "type": "deep",
  "livecrawl": "preferred"
}

```text
1) Results (tweet content, author handle, date, engagement if visible)
2) Sources (Tweet URLs)
3) Notes (sentiment summary, notable accounts, threads vs single tweets)

Important: Be aware that tweet content can be informal, sarcastic, or context-dependent.


Step 3: Ask User to Restart Claude Code

You should ask the user to restart Claude Code to have the config changes take effect.

````