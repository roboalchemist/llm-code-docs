# Source: https://docs.qodo.ai/qodo-documentation/code-review/concepts/pr-history.md

# Using PR History in Code Reviews

{% hint style="success" %}
This feature is currently in **beta** and available on **GitHub**, with support for additional Git providers coming soon.
{% endhint %}

PR History uses historical pull request data to help developers evaluate the relevance of AI code review findings.

By analyzing how similar issues were handled in past pull requests, Qodo provides additional context that helps reviewers decide whether a finding likely requires attention.

This historical context is shown directly inside the Findings section of a pull request, where developers can see how similar issues were treated in previous PRs.

For example, if your team has consistently logged errors using the same convention in the past, a deviation from that pattern would signal that the convention has been broken.

### Why PR History matters

AI code review tools often surface many findings, but it can be difficult to determine which ones are truly important for a specific repository.

PR History helps provide that context by showing how similar issues were handled in previous pull requests. This allows reviewers to quickly understand whether a finding reflects a pattern the team typically addresses or one that has historically been dismissed.

### How it works

Qodo extends code review context by incorporating PR history as an additional source.

When reviewing a pull request, Qodo analyzes past PRs with similar findings and code patterns, along with relevant comments, discussions, and how those findings were handled during previous reviews.

This helps answer questions such as:

* Is this issue actually important for this repository?
* Do teams usually fix this type of finding?

Based on how similar findings were handled in the past:

* If similar issues were usually fixed, Qodo signals that the finding is likely relevant.
* If similar issues were often dismissed, Qodo indicates that the finding may not require attention.

This helps reviewers focus on findings that are more likely to matter for the repository.

### Why historical context improves reviews

Historical PR context helps avoid common failure modes in AI code review.

By referencing how similar issues were handled in the past, Qodo can:

* Reduce false positives by recognizing patterns that were intentionally accepted in earlier PRs
* Highlight potential regressions when behavior diverges from established repository patterns
* Align review feedback with how the repository has evolved rather than relying only on generic rules

By combining full codebase context with pull request history, Qodo provides feedback that is more consistent, actionable, and easier for teams to trust. As new pull requests are merged and new review decisions are made, this historical context continues to evolve alongside the repository.

### What appears in the PR

PR History results appear in the [Relevance](https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/comment-anatomy) section of an issue finding in the PR.

This section includes:

* **Relevance classification** – indicating whether the finding is high, medium, or low relevance based on how similar findings were handled in past PRs.

  ⭐ ⭐ ⭐ **High** - similar findings were typically accepted/fixed

  ⭐ ⭐       **Medium** - mixed or inconclusive history

  ⭐             **Low** - similar findings were typically ignored
* **Historical context** - A brief explanation of the historical pattern.
* **Links to similar past PRs** – allowing reviewers to see how comparable issues were handled.

These references help reviewers understand why a finding received its relevance classification and prioritize issues that are more likely to matter for their repository.

### Get started

To view PR History insights:

1. Ensure your repository is integrated with Qodo (GitHub or GitLab).
2. Open a pull request reviewed by Qodo.
3. Expand an issue finding to view the Relevance section, which includes links and context from similar past PRs.

No additional configuration is required during the beta phase.
