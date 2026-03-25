# Source: https://docs.acceldata.io/documentation/best-practices-playbook.md

# Best Practices Playbook

This playbook is a practical guide to using ADM effectively across roles—data engineers, analytics engineers, data stewards, and business stakeholders.

It focuses on:

- Asking better questions (prompting)
- Choosing modes intentionally (Conversation vs Workflows vs Notebooks)
- Building repeatable operations (triage workflows)
- Collaborating safely (multi-user + permissions)
- Grounding answers using Knowledge Base and MCP

---

## How to Access These Features

- **Conversation:** left nav → Conversation / New Conversation
- **Workflows:** left nav → Understanding Workflows / Workflows
- **Agents:** left nav → Understanding Agents
- **Business Notebooks:** left nav → Business Notebooks
- **Knowledge Base:** left nav → Knowledge Base (upload docs)
- **Collaboration:** open a conversation → Share / Add participants
- **MCP:** left nav → Understanding MCP Server (and configured integrations)

---

## Playbook by role

### Data Engineer (Triage + Remediation)

Best outcomes when you:

- Ask for root cause hypotheses + evidence
- Compare “before vs after”
- Request “what changed” upstream
- Standardize triage into workflows

**Go-to prompts**

- “Compare today vs yesterday for this asset: what changed in quality, freshness, schema?”
- “List the top 3 likely causes and the fastest checks to confirm.”

---

### Analytics Engineer (Stability + Correctness)

Best outcomes when you:

- Ask for rule-level breakdowns
- Validate assumptions about transformations
- Request impact analysis (downstream assets/dashboards)

**Go-to prompts**

- “Which downstream dashboards depend on this asset and are impacted?”
- “Which rule failures are most likely due to transformation logic?”

---

### Data Steward (Governance + Standards)

Best outcomes when you:

- Reference documented policies and definitions (Knowledge Base)
- Ask for “standard vs exception”
- Request stakeholder-ready summaries

**Go-to prompts**

- “According to our standards, what should quality thresholds be for this dataset?”
- “Summarize non-compliant assets and recommend which policies to add.”

---

### Business User (Impact + Decisions)

Best outcomes when you:

- ask for business impact first
- request non-technical language
- ask for “what should I do now”

**Go-to prompts**

- “Is this metric safe to use today? If not, what’s the recommended workaround?”
- “Summarize impact on revenue/finance reporting in 8 bullets.”

---

## Operational Best Practices (What High-performing Teams Do)

### 1) Start with a “triage checklist” Approach

Ask ADM to answer, in order:

1. What happened (symptoms)?
2. When did it start?
3. What changed?
4. What is impacted?
5. What do we do next?

This avoids skipping to conclusions.

---

### 2) Turn Repeatable Work into Workflows

Once you run the same analysis more than twice, convert it into a workflow:

- Consistent steps
- Consistent output format
- Reusable across teams

---

### 3) Use the Knowledge Base for “single source of truth”

Upload:

- Governance docs
- SLAs
- Definitions of key metrics
- Runbooks
- Incident playbooks

Then ask ADM:
 “Use Knowledge Base sources and cite them.”

---

### 4) Use Collaboration to Reduce Decision Latency

Bring in:

- Data platform (pipelines)
- Domain owners (definitions)
- Consumers (impact confirmation)

Use @mentions + short asks:

- “Can you confirm whether this is expected seasonality?”
- “Is the SLA for this report 9 AM or 11 AM?”

---

### 5) Always Ask for “next checks”

For investigations, require ADM to include:

- 3–5 verification checks
- the fastest path to confirm root cause
- recommended owner team

---

## Real-world Scenarios (Templates You Can Copy)

### Scenario A — Freshness Breach on a Tier-1 Table

Prompt:
 “Investigate why `daily_revenue_summary` is delayed today. Compare to prior runs, identify the likely cause, list impacted downstream assets, and provide a recommended mitigation plan.”

Expected output:

- Summary (5 bullets)
- Likely root cause + evidence
- Impacted dashboards/reports
- Next steps + owners

---

### Scenario B — Schema Drift Broke a Pipeline

Prompt:
 “Schema drift detected on `orders`. Identify added/removed/modified columns, assess likely pipeline breakpoints, and propose a remediation plan.”

Expected output:

- Changes table (column, change type, risk)
- Suspected breaking dependencies
- Recommended fix steps

---

### Scenario C — Data Quality Score Dropped Suddenly

Prompt:
 “Quality score for `customer_master` dropped from 97% to 85% in 24 hours. Show failing rules, affected row counts, and what upstream change could explain it. Provide verification steps.”

Expected output:

- Failing rules table
- Pattern analysis
- Verification checks
- Prevention recommendation

---

### Scenario D — Business Asks “Can I trust the dashboard?”

Prompt:
 “For the executive revenue dashboard, confirm whether data is reliable today. If not, explain impact and recommended decision guidance in plain language.”

Expected output:

- Trust status (green/yellow/red)
- What is impacted
- Recommended actions / workarounds
- Links to evidence (where supported)

---

## Common Pitfalls and Fixes

### Pitfall: Unclear Ownership

Fix: Ask ADM to suggest owner teams based on domain/asset tags (or your org’s structure).

### Pitfall: Too Much Detail for Stakeholders

Fix: Ask for “exec summary + appendix,” where appendix contains technical details.

### Pitfall: Too Many One-off Conversations

Fix: Create a workflow + notebook template for recurring reporting.

---

## Checklist: “Good ADM request”

- Asset(s) named (tables, domains, dashboards)
- Time window defined
- Goal stated (investigate / summarize / decide)
- Output format specified (bullets/table)
- Ask for evidence/citations where appropriate
- Ask for next steps + verification checks