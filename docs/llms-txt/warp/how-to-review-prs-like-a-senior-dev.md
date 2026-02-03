# Source: https://docs.warp.dev/university/developer-workflows/power-user/how-to-review-prs-like-a-senior-dev.md

# How To: Review PRs Like A Senior Dev

Learn how to prompt Warp’s AI to review pull requests like an experienced engineer — focusing on structure, red flags, and clarity

{% embed url="<https://youtu.be/NVwqQyphlAw?si=zcMR1ZHt-xnIS_ME>" %}

***

{% stepper %}
{% step %}
**Intro**

This tutorial teaches you how to use Warp to make **pull-request reviews faster and smarter**.\
Instead of relying on AI summaries, you’ll prompt Warp to generate an **index and priority list**, guiding your review order while flagging risky sections.

Although this example focuses on large PRs, the same workflow applies to **code reviews**, **design docs**, or **feature diffs**.
{% endstep %}

{% step %}
**The Problem**

Large PRs are difficult to parse.\
AI summaries gloss over nuance and may miss subtle issues — you need structured, prioritized insight instead.
{% endstep %}

{% step %}
**The Prompt**

Use this in Warp’s AI input:

{% code title="Prompt" %}

```
## Prompt: Structured PR Review Format

> Review this pull request and format your response for rapid scanning by a busy maintainer. Follow the structure below.

---

### 1. 🚨 Risk Assessment

**Overall Risk:** 🔴 HIGH | 🟠 MEDIUM | 🟢 LOW  
**Complexity:** [Simple | Moderate | Complex | Very Complex]  
**Blast Radius:** [Isolated | Module-wide | System-wide | External APIs affected]  
**Requires Immediate Review:** [YES / NO – why]

---

### 2. 🔍 Critical Issues  
_If none, write “None found” and skip to the next section._

#### 1. [CRITICAL ISSUE TITLE]  
**File:** `path/to/file.js:L125`  
**Impact:** Data loss / Security hole / System crash  
**Fix:**  
// Quick code fix example here

---

### 3. ⚠️ Concerns  
_Should discuss or fix before merge. If none, write “None found.”_  

**Examples:**  
- [PERFORMANCE] Unindexed query on large table  
- [SECURITY] Missing input sanitization in login form  

---

### 4. 🎯 Maintainer Decision Guide  

**Merge confidence:** [0–100]%  
- □ Safe to merge after fixing blockers  
- □ Needs architecture discussion first  
- □ Requires performance testing  
- □ Get security team review  
- □ Author should split into smaller PRs  

**Time to properly review:** ~[X] minutes  
**Recommended reviewer expertise:** [Backend | Security | Database | Frontend]  

---

### 5. 🧭 Formatting Rules  

- Use emoji headers for instant visual recognition  
- Keep sections short; if empty, say “None found”  
- Blockers get full detail, everything else stays concise  
- Include code examples only for blockers  
- Bold key impact/risk words  
- Use consistent prefixes like [SECURITY], [PERFORMANCE], [LOGIC] for easy scanning  
- If PR is genuinely fine, end with: ✅ “This PR is safe to merge as-is.”

```

{% endcode %}
{% endstep %}
{% endstepper %}
