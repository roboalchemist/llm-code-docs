# Source: https://exa.ai/docs/reference/company-research-claude-skill.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Company Research Claude Skill

> This guide shows you how to set up a Claude skill and Exa MCP that helps you research companies.

<Card title="Copy and Paste in Claude Code">
  Click the copy button on the code block below and paste it into Claude Code. Claude will automatically set up both the MCP connection and the skill for you.
</Card>

```
Step 1: Install or update Exa MCP

If Exa MCP already exists in your MCP configuration, either uninstall it first and install the new one, or update your existing MCP config with this endpoint. Run this command in your terminal:

claude mcp add --transport http exa "https://mcp.exa.ai/mcp?tools=web_search_advanced_exa"


Step 2: Add this Claude skill

---
name: company-research
description: Company research using Exa search. Finds company info, competitors, news, tweets, financials, LinkedIn profiles, builds company lists.
triggers: company research, competitor analysis, market research, find companies, research company, company intel.
requires_mcp: exa
context: fork
---

# Company Research

## Tool Restriction (Critical)

ONLY use `web_search_advanced` from Exa. Do NOT use `web_search_exa` or any other Exa tools.

## Token Isolation (Critical)

Never run Exa searches in main context. Always spawn Task agents:

- Agent runs Exa search internally
- Agent processes results using LLM intelligence
- Agent returns only distilled output (compact JSON or brief markdown)
- Main context stays clean regardless of search volume

## Dynamic Tuning

No hardcoded numResults. Tune to user intent:

- User says "a few" → 10-20
- User says "comprehensive" → 50-100
- User specifies number → match it
- Ambiguous? Ask: "How many companies would you like?"

## Query Variation

Exa returns different results for different phrasings. For coverage:

- Generate 2-3 query variations
- Run in parallel
- Merge and deduplicate

## Categories

Use appropriate Exa category:

- company → homepages, gargantuan amount of metadata such as headcount,
  location, funding, revenue
- news → press coverage
- tweet → social presence
- people → LinkedIn profiles (public data)

## LinkedIn

Public LinkedIn via Exa: category "people", no other filters
Auth-required LinkedIn → use Claude in Chrome browser fallback

## Browser Fallback

Auto-fallback to Claude in Chrome when:

- Exa returns insufficient results
- Content is auth-gated
- Dynamic pages need JavaScript

## Models

- haiku: fast extraction (listing, discovery)
- opus: synthesis, analysis, browser automation


Step 3: Ask User to Restart Claude Code

You should ask the user to restart Claude Code to have the config changes take effect.
```

## What This Skill Does

Once you set up this skill, you can ask Claude to:

* Research any company and get detailed information
* Find competitors in a specific market
* Get recent news about companies or look up LinkedIn profiles of company employees

The skill is smart about how it searches - it will ask you how many results you want if you don't specify, and it uses different search strategies to get the best information.

## How to Use It

After setting up the skill, you can trigger it by saying things like:

* "Do market research on \[industry]"
* "Find competitors to \[company]"
* "Get company intel on \[company]"

The skill will automatically use Exa's powerful search tools to find and organize the information you need.
