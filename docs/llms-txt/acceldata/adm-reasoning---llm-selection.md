# Source: https://docs.acceldata.io/documentation/adm-reasoning---llm-selection.md

# ADM Reasoning & LLM Selection

ADM can produce different kinds of outputs: short answers, structured summaries, step-by-step investigations, and sometimes visuals/diagrams (depending on what your deployment supports). The most common customer friction is **not knowing which model/LLM setting to use** and **when to prioritize accuracy vs speed**.

This guide provides:

- A practical decision framework for selecting an LLM (when configurable)
- Guidance on how to request outputs (text vs structured vs diagrams)
- Safe patterns to reduce hallucinations and improve grounding

---

## How to Access These Features

Depending on your ADM deployment, model selection may appear as:

- A **model dropdown** in Conversation
- A **workflow setting** for runs
- An **admin/default setting** configured by your team

If model selection is not visible in your UI:

- Treat this doc as “how to prompt for the right behavior”
- Ask your admin which models are enabled and how they map to use cases

---

## What “good reasoning” Looks Like in ADM

ADM is most reliable when you:

- Provide **asset names**, **time windows**, and **what “correct” means**
- Ask for **evidence** (citations or references to sources)
- Ask for **assumptions** to be listed explicitly
- Request **next actions** and **checks** to validate results

Use this pattern:

1. What ADM concluded
2. What evidence it used
3. What it didn’t know / assumptions
4. What to do next

---

## LLM selection: Practical Guidance (When You Can Choose)

### Use a “fast” Model When

- You need quick summaries or reformatting
- You’re brainstorming questions to ask
- You want a first pass and will validate with evidence

**Examples**

- “Summarize this incident thread into 10 bullets.”
- “Rewrite this into stakeholder language.”

---

### Use a “reasoning / higher-accuracy” Model When

- You need root cause analysis
- You need careful multi-step logic
- You want fewer wrong turns

**Examples**

- “Explain why reconciliation mismatched and what changed upstream.”
- “Identify the most likely cause from multiple signals.”

---

### Use a “visual/diagram-capable” Model When (If Supported)

- You need architecture diagrams, flowcharts, or structured visuals
- You want a crisp “one-slide” output for sharing

**Examples**

- “Create a diagram of the incident flow: detection → impact → mitigation → follow-ups.”

> If your ADM does not support diagram generation directly, request a **text-based diagram format**:

- Mermaid (`flowchart TD ...`)
- ASCII diagrams
- or a “diagram description” you can paste into a diagram tool

---

## Ask for the Right Output Type (Even Without Model Selection)

### When You Want Structured Output

Ask explicitly for:

- Headings
- Tables with specific columns
- Checklists
- Decision trees

**Example**
 “Provide: (1) root cause hypothesis list with confidence, (2) evidence per hypothesis, (3) next verification steps, (4) recommended owner team.”

---

### When You Want “high precision”

Add guardrails:

- “Use only retrieved context / cite sources”
- “If unknown, say unknown”
- “List assumptions separately”

**Example**
 “Answer using only Knowledge Base citations. If the answer isn’t in sources, say what’s missing and what document we should upload.”

---

## Reducing Hallucinations

Use these techniques:

### 1) Force Evidence

- “Cite the source sections used.”
- “List which documents were referenced.”

### 2) Force Constraints

- “Only consider last 7 days.”
- “Only consider production assets.”

### 3) Force Uncertainty Handling

- “If you’re not sure, provide the top 3 hypotheses and how to validate.”

### 4) Separate “facts” vs “recommendations”

Ask for two sections:

- Facts observed
- Suggested actions

---

## Common Scenarios + Recommended Model Behavior

### Scenario: Business User Asks “Is Finance data healthy today?”

Recommended:

- Concise summary
- Clear status: green/yellow/red
- What changed
- What to do next
- Links to assets/incidents

Prompt:
 “Give me a finance reliability status update for today: top issues, impacted dashboards, and recommended actions. Keep it under 12 bullets.”

---

### Scenario: Engineer Asks “Why did this policy fail?”

Recommended:

- Deeper reasoning
- Table of failing rules
- Correlation with upstream changes
- Verification steps

Prompt:
 “Analyze the failure pattern for `customer_validation` at 2 PM: show failing rules, affected rows, what changed upstream, and how to verify root cause.”

---

### Scenario: Cross-team Incident Review

Recommended:

- Timeline
- Decisions made
- Action items
- Owners
- Prevention steps

Prompt:
 “Create a post-incident summary: timeline, root cause, impact, mitigations, and 5 preventive actions with owners.”