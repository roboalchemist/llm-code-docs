# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/code-review/review-uncommitted-changes.md

# Review Uncommitted Changes

## **Overview**

**Review Uncommitted Changes** is your built-in assistant for validating code before it becomes part of a commit.\
It scans all uncommitted modifications in your working directory and provides a structured, context-aware analysis.\
The workflow helps you ensure clarity, consistency, and correctness before your changes move into version control.

## **How It Works**

When you select `/review-uncommitted` workflow from the welcome screen, Qodo analyzes all uncommitted file changes and produces a detailed review that highlights what was changed and why.

**The workflow presents:**

* **Holistic Review**\
  Aggregates all local file changes and summarizes them by scope and purpose.
* **Thematic Walkthrough**\
  Groups modified files by topics such as *features*, *fixes*, *refactors*, and more - helping you review related changes together.
* **Intelligent Insights**\
  Detects potential issues and classifies them into categories like *correctness*, *style*, *performance*, and *best practices*.
* **Instant Fixes**\
  Apply suggestions directly with one click - no need to switch contexts or open multiple files.
* **Project Alignment**\
  Ensures all agent-written and user-modified code aligns with your team’s conventions, style guides, and PR expectations.

### When to Use This Workflow

Use this workflow any time you want to validate local progress before committing. It is particularly useful when:

* You’ve made changes across multiple files.
* You want to validate agent-generated updates.
* You want to reduce PR review friction by addressing issues early.

### **How to Access Local Review**

1. Open Qodo in your IDE.
2. Select **“review-uncommitted”** from the **Welcome Screen.**
3. Review grouped changes, read insights, and apply suggested fixes.
4. Commit with confidence.

{% hint style="info" %}
**Tip**

For higher confidence before committing, pair this workflow with **Unit Test** and **Cleanup** to validate correctness and maintainability.
{% endhint %}
