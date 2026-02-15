# Source: https://exa.ai/docs/reference/personal-site-search-claude-skill.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.


## # Personal Site Search

> This guide shows you how to set up a Claude skill and Exa MCP that helps you find personal blogs, portfolios, and independent content.

<Card title="Copy and Paste in Claude Code">
  Click the copy button on the code block below and paste it into Claude Code. Claude will automatically set up both the MCP connection and the skill for you.
</Card>

````markdown
Step 1: Install or update Exa MCP

If Exa MCP already exists in your MCP configuration, either uninstall it first and install the new one, or update your existing MCP config with this endpoint. Run this command in your terminal:

claude mcp add --transport http exa "https://mcp.exa.ai/mcp?tools=web_search_advanced_exa"


Step 2: Add this Claude skill

---
name: web-search-advanced-personal-site
description: Search personal websites and blogs using Exa advanced search. Full filter support for finding individual perspectives, portfolios, and personal blogs. Use when searching for personal sites, blog posts, or portfolio websites.
context: fork
---

# Web Search Advanced - Personal Site Category

## Tool Restriction (Critical)

ONLY use `web_search_advanced_exa` with `category: "personal site"`. Do NOT use other categories or tools.

## Full Filter Support

The `personal site` category supports ALL available parameters:

### Core
- `query` (required)
- `numResults`
- `type` ("auto", "fast", "deep", "neural")

### Domain filtering
- `includeDomains`
- `excludeDomains` (e.g., exclude Medium if you want independent blogs)

### Date filtering (ISO 8601)
- `startPublishedDate` / `endPublishedDate`
- `startCrawlDate` / `endCrawlDate`

### Text filtering
- `includeText` (must contain ALL)
- `excludeText` (exclude if ANY match)

__Array size restriction:__ `includeText` and `excludeText` only support __single-item arrays__. Multi-item arrays (2+ items) cause 400 errors. To match multiple terms, put them in the `query` string or run separate searches.

### Content extraction
- `textMaxCharacters` / `contextMaxCharacters`
- `enableSummary` / `summaryQuery`
- `enableHighlights` / `highlightsNumSentences` / `highlightsPerUrl` / `highlightsQuery`

### Additional
- `additionalQueries`
- `livecrawl` / `livecrawlTimeout`
- `subpages` / `subpageTarget` - useful for exploring portfolio sites

## Token Isolation (Critical)

Never run Exa searches in main context. Always spawn Task agents:
- Agent calls `web_search_advanced_exa` with `category: "personal site"`
- Agent merges + deduplicates results before presenting
- Agent returns distilled output (brief markdown or compact JSON)
- Main context stays clean regardless of search volume

## When to Use

Use this category when you need:
- Individual expert opinions and experiences
- Personal blog posts on technical topics
- Portfolio websites
- Independent analysis (not corporate content)
- Deep dives and tutorials from practitioners

## Examples

Technical blog posts:
```text

web_search_advanced_exa {
  "query": "building production LLM applications lessons learned",
  "category": "personal site",
  "numResults": 15,
  "type": "deep",
  "enableSummary": true
}

```text

Recent posts on a topic:
```text

web_search_advanced_exa {
  "query": "Rust async runtime comparison",
  "category": "personal site",
  "startPublishedDate": "2025-01-01",
  "numResults": 10,
  "type": "auto"
}

```text

Exclude aggregators:
```text

web_search_advanced_exa {
  "query": "startup founder lessons",
  "category": "personal site",
  "excludeDomains": ["medium.com", "substack.com"],
  "numResults": 15,
  "type": "auto"
}

```text

## Output Format

Return:
1) Results (title, author/site name, date, key insights)
2) Sources (URLs)
3) Notes (author expertise, potential biases, depth of coverage)


Step 3: Ask User to Restart Claude Code

You should ask the user to restart Claude Code to have the config changes take effect.
````
