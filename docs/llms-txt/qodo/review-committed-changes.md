# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/code-review/review-committed-changes.md

# Review Committed Changes

### Overview

**Review Committed Changes** helps you examine code after it has been committed, usually before opening a pull request.\
It provides the same structured analysis and insights as reviewing uncommitted changes, but optimized for comparing your branch against another branch.

This workflow supports two types of committed reviews:

1. **Against the main branch - `/review-committed (main)`**
2. **Against another branch - `/review-committed (other)`** (a branch selector appears automatically when choosing this option)

### How It Works

When choosing **Review Committed Changes**, Qodo compares the current branch with the selected target branch and generates a complete contextual review.

The workflow includes:

* **Holistic Review**\
  Shows all differences between the branches and summarizes them by purpose and impact.
* **Thematic Walkthrough**\
  Groups changed files by topics such as new features, bug fixes, or refactors for easier navigation.
* **Intelligent Insights**\
  Detects issues across correctness, style, performance, and best practices.
* **Instant Fixes**\
  Enables applying recommended adjustments directly from the workflow.
* **Project Alignment**\
  Validates that code in the commit history remains consistent with team conventions and expectations before PR submission.

### Branch Selection

After selecting the workflow, Qodo automatically displays available branches:

* **Review against main branch** – quickest way to review work that is about to be merged to main.
* **Review against another branch** – used when working with long-lived feature branches or cross-branch changes.

### When to Use This Workflow

Use this workflow before preparing a PR or when reviewing changes accumulated across several commits. It is especially helpful when:

* You want to validate the final state of your branch before merge.
* The changes span multiple commits or files.
* You want to catch issues that may not appear when reviewing only local diffs.

### How to Access

1. Open Qodo in your IDE.
2. Select one of the **Review Committed Changes** workflows from the welcome screen.
3. Review differences, explore insights, and apply fixes.
4. Move forward with a clean and consistent PR.

{% hint style="info" %}
**Tip**

Use this workflow as a final checkpoint before creating a pull request to ensure alignment with team standards and reduce review cycles.
{% endhint %}
