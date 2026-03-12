# Source: https://docs.acceldata.io/documentation/query-mode-selection.md

# Query Mode Selection

ADM supports different interaction styles depending on what you’re trying to accomplish—quick answers, deep investigation, repeatable work, or collaboration. Choosing the right **mode** makes results more accurate, faster, and easier to operationalize.

This guide helps you:

- Decide which mode to use for **data questions vs business questions**
- Write prompts that produce consistent results
- Understand **when to bring in context** (Knowledge Base, MCP sources, people)

---

## How to Access These Features

- **Conversation mode:** Open ADM and start a chat from the left navigation (or “New Conversation”).
- **Workflow mode:** Open **Understanding Workflows** (or Workflows) in the left nav and create/run a workflow.
- **Agents:** Open **Understanding Agents** to see available agents and when to use them.
- **Business Notebooks:** Open **Business Notebooks** from the left nav to build structured, shareable analyses.
- **Knowledge Base:** Open **Knowledge Base** to upload documents used for grounding and citations.
- **Multi-User Collaboration:** Open a conversation → Share/Add participants (or use your platform’s collaboration entry point).
- **MCP Servers:** Open **Understanding MCP Server** (or Settings → Integrations → MCP Servers, if your UI supports it).

> **Tip**: If your UI supports slash commands, use them to jump quickly (example: `/knowledge-base`).

---

## Choosing the Right Mode (Most Common Situations)

### Use **Conversation** When You Want Fast Answers or Iterative Investigation

Best for:

- Asking “what is happening?” and “why did this happen?”
- Exploring root cause hypotheses
- Getting suggestions for next steps
- Summarizing, translating, or explaining results to stakeholders

Not ideal for:

- Repeatable, standardized execution (use Workflows)
- Producing a structured artifact every time (use Business Notebooks or Workflows)

**Examples**

- “Why did the customer freshness alert trigger today?”
- “Summarize the top issues impacting revenue metrics this week.”

---

### Use **Workflows** When You Want Repeatability and Consistency

Best for:

- Standard operating procedures (SOPs)
- Running the same investigation steps across assets/teams
- Turning analysis into an operational process

Not ideal for:

- Exploratory “brainstorming” without a clear endpoint

**Examples**

- “Every morning: check freshness + reconciliation + quality score for Tier-1 tables and summarize failures.”
- “Run a standard triage workflow whenever an incident is created.”

---

### Use **Business Notebooks** When You Want a Shareable Narrative + Structured Outputs

Best for:

- Executive-ready summaries
- Consistent reporting format (tables/sections)
- Combining business context with technical detail

Not ideal for:

- Simple one-off Q&A

**Examples**

- “Create a weekly reliability briefing for Finance domain: top failing assets, trends, recommended actions.”

---

### Use **Multi-User Collaboration** When the Work Requires Multiple Roles

Best for:

- Incident response across data/platform/business stakeholders
- Shared investigation context and decisions
- Keeping a living record of “what we tried and why”

**Examples**

- “Bring in the data engineer + business analyst to validate whether this is expected seasonal drift or a pipeline defect.”

---

## Best Practices for Mode Selection (Data vs Business Queries)

### Data / Technical Queries (Engineers, Platform teams)

Use **Conversation** for exploration, then **Workflows** for operationalization.

**Good fits**

- “Identify which upstream dependencies changed before the schema drift alert.”
- “Show which assets are failing policies and whether failures share a pattern.”

**Recommended pattern**

1. Conversation: explore and confirm the hypothesis
2. Workflow: standardize the triage steps
3. Notebook: publish a stable summary for stakeholders

---

### Business / Stakeholder Queries (Analysts, Data Stewards, Leadership)

Use **Business Notebooks** or **Conversation** with clear context and constraints.

**Good fits**

- “Which customer metrics are impacted by delayed data today?”
- “Summarize reliability risks for Finance domain in plain language.”

**Recommended pattern**

1. Provide business context (which metric/process matters)
2. Ask for a stakeholder-ready output (bullets/table)
3. Request citations (Knowledge Base, sources) where applicable

---

## Prompting Patterns that Work (Reusable Templates)

### Template A — Investigation Prompt (Conversation)

**Context** + **Question** + **Constraints** + **Expected output**

- Context: asset / domain / incident link
- Question: what happened / why / what changed
- Constraints: timeframe, environment, severity
- Output: bullets, table, short summary + next actions

**Example**
 “For the `customer_360_view` asset, investigate why quality score dropped in the last 24 hours. Compare today vs yesterday, identify the top failing rules, and suggest the most likely root causes. Output: (1) 5-bullet summary, (2) table of failing rules and impact, (3) recommended next steps.”

---

### Template B — Business Translation Prompt

“Explain this issue for [audience] focusing on [business impact], using [constraints], and include [links/citations].”

**Example**
 “Explain today’s freshness delay for Finance leadership: what business reports are impacted, estimated risk, and what teams are doing. Keep it under 10 bullets, and include links to the affected assets and incidents.”

---

### Template C — Workflow Design Prompt

“Create a repeatable workflow that takes [input] and produces [output], including decision points.”

**Example**
 “Design a workflow: given an incident on a Tier-1 table, run triage steps (freshness, schema drift, policy failures), produce a summary, and assign recommended owner teams based on domain tags.”

---

## Common Mistakes and How to Fix Them

### Mistake: Asking without Scope

Bad: “Why did it fail?”
 Better: “Why did `customer_validation` fail today at 2 PM? Show the failure pattern and what changed upstream.”

### Mistake: Mixing Business + Technical Asks without Structure

Better: break into two steps:

1. Technical diagnosis
2. Business impact summary

### Mistake: Not Specifying Output Format

Ask for exactly what you need:

- Table with columns
- Summary length
- Include links / citations
- Include “what to do next”

---

## Quick Decision Guide

Use this when you’re not sure:

- Need a fast answer now? → **Conversation**
- Need consistency / repeatability? → **Workflows**
- Need a polished narrative for sharing? → **Business Notebooks**
- Need multiple roles to decide/act? → **Multi-User Collaboration**
- Need company-specific grounding? → **Knowledge Base** (and request citations)
- Need external systems context? → **MCP** (if configured)

---

## Examples: “data” vs “business” Version of the Same Request

### Data Version

“Identify which rules failed on `orders` today, how many rows were affected, and whether failures correlate with a pipeline run or schema change.”

### Business Version

“Summarize today’s `orders` reliability issue: impact on dashboards, customer experience risk, and expected resolution timeline. Keep it non-technical.”