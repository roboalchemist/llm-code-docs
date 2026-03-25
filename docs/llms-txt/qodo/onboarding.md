# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/rule-enforcement/onboarding.md

# Onboarding to the Rule System

{% hint style="success" %}
**Rules System availability**

The Rules System is currently available on **GitHub only**.\
It is **enabled by default for new Qodo customers**.\
Existing customers can **contact Qodo** to request access.
{% endhint %}

This page explains how the Rule System is initialized for customers when Qodo is first connected to an organization’s repositories.

During onboarding, Qodo helps teams establish a baseline rule set by importing existing standards, enriching them with additional context, and generating suggested rules based on real development activity.

### What happens during onboarding

When you install Qodo in your Git organization, Qodo performs the following steps to initialize the Rule System.

#### Importing existing rules

Qodo discovers and imports existing rules from supported files in the organization’s repositories.

* Rules can be extracted from full or partial documents
* Relevant sections are identified and converted into rules
* Imported rules are added to the Rules table

After import, rules are normalized and enriched to align with the Qodo rule system.

**Supported file names:**

* AGENTS.md
* CLAUDE.md
* GEMINI.md
* best\_practices.md
* RULE.md
* .cursorrules
* pr\_compliance\_checklist.yaml

**Rule enrichment**

Imported rules are enriched with additional structure to make them enforceable and reviewable. Enrichment includes category, severity, scope, and examples.

This ensures imported rules behave the same as rules created directly in the portal.

#### Suggested rules generation

As part of onboarding, Qodo also generates a set of suggested rules based on the organization’s pull request history.

* Based on retroactive analysis of recent PRs
* Identifies repeated review patterns and behaviors
* Suggested rules are not enforced automatically

All suggested rules require explicit admin review and approval before activation.

#### What to expect after onboarding

Within minutes of installing Qodo, you’ll start to see the following:

* Imported rules appear in the Rules table
* Suggested rules appear under **Rules → Suggestions**
* No rules are enforced until explicitly activated

This approach enables teams to review, refine, and activate rules at their own pace while maintaining full control over enforcement.

#### **Triggering additional suggested rules**&#x20;

After onboarding, you can optionally trigger additional suggested rule discovery as your review practices evolve. Add `/scan_repo_discussions` as a comment on any pull request to generate more suggested rules from recent discussions. Automatic, ongoing discovery will be available soon.
