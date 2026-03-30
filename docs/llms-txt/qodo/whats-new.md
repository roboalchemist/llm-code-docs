# Source: https://docs.qodo.ai/qodo-documentation/whats-new/whats-new.md

# What's New

## Qodo 2.1  <a href="#qodo-2.1-introducing-qodos-rule-system" id="qodo-2.1-introducing-qodos-rule-system"></a>

### Introducing Qodo’s [Rule System](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/rule-enforcement) (beta) <a href="#qodo-2.1-introducing-qodos-rule-system" id="qodo-2.1-introducing-qodos-rule-system"></a>

{% hint style="success" %}
&#x20;Currently supported for GitHub single and multi tenant.
{% endhint %}

Qodo 2.1 expands the platform with Qodo’s Rule System, a centralized and intelligent framework for defining, managing, and enforcing engineering standards at scale.

As AI tools generate more code across teams and environments, standards can drift across linters, markdown files, and informal conventions. The Rule System creates a single source of truth for organizational standards and integrates them directly into the review workflow.

The Rule System enables:

* Converting existing rules into structured, enforceable standards
* Generating structured rules from natural language
* Discovering implicit standards from codebase patterns and PR history
* Identifying duplicate, conflicting, or outdated rules to maintain rule health
* Measuring rule adoption and violations to track effectiveness over time

Rules that are violated are flagged by Qodo during pull request review, ensuring changes align with organizational standards.

The Rule System supports scoped enforcement at the organization, repository group, and repository levels, with inheritance and override controls. It also continuously evaluates rule health by detecting duplicates, conflicts, and outdated standards to keep governance clean and effective over time.

With Qodo 2.1, standards become a living system that evolves with your code and scales consistently across teams and tools.

<figure><img src="https://764298175-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsjA3HjeOPlxDJ3ZoBNVZ%2Fuploads%2FhZ6hAqvG49iuCVDbfzHr%2Fimage.png?alt=media&#x26;token=5ee59995-38da-4062-b28d-2c10c0dc1301" alt=""><figcaption></figcaption></figure>

### [Azure DevOps integration](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/install/azure-devops) <a href="#azure-devops-integration" id="azure-devops-integration"></a>

Qodo now integrates natively with Azure DevOps for Enterprise customers, bringing advanced AI powered code review directly into Microsoft based development environments.

Using Microsoft Entra ID authentication and Azure DevOps service hooks, Qodo connects securely to your repositories and pull request workflows without requiring additional tools or process changes.

With this integration, Qodo:

* Publishes AI powered reviews directly inside Azure DevOps pull requests
* Uses Azure Boards work items and associated tickets for added context and compliance checks
* Supports repository level or project level configuration for flexible deployment

Once configured, Qodo automatically analyzes pull requests and delivers prioritized findings and structured suggestions directly in the workflow teams already use.

<figure><img src="https://764298175-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsjA3HjeOPlxDJ3ZoBNVZ%2Fuploads%2FPZ2uC2ZDl3Ij9mS6yaVC%2Fimage.png?alt=media&#x26;token=5e059c83-747e-4108-b31f-38da919cbfc8" alt=""><figcaption></figcaption></figure>

## Qodo 2.0 <a href="#qodo-2.0-next-generation-agentic-pr-review" id="qodo-2.0-next-generation-agentic-pr-review"></a>

### Next generation [agentic PR review](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/) (beta) <a href="#qodo-2.0-next-generation-agentic-pr-review" id="qodo-2.0-next-generation-agentic-pr-review"></a>

Qodo 2.0 introduces a major upgrade to AI powered code review with a next generation agentic PR review experience designed for teams shipping increasing volumes of AI generated code.

Instead of a single review pass, Qodo uses a **multi agent system** where specialized agents collaborate using multi step reasoning. Each agent focuses on specific responsibilities including:

* Critical issue detection
* Duplicated logic
* Ticket compliance
* Standards enforcement

This approach increases both coverage and depth, enabling Qodo to surface issues that traditional AI review tools often miss.

In each pull request, Qodo has access to leverage **full repository context, repository structure awareness, and PR history**. By understanding how the codebase evolved and how past decisions were made, Qodo evaluates changes in architectural and historical context, not just as isolated diffs.

Findings are **prioritized by impact, clearly explained, and paired with structured remediation guidance**. The result is higher recall, improved precision, and significantly less noise, delivering reviews developers trust and act on.

<figure><img src="https://764298175-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsjA3HjeOPlxDJ3ZoBNVZ%2Fuploads%2FAs0xqGjdFKTHZ8bs3sjR%2Fimage.png?alt=media&#x26;token=73505ba3-512e-4982-ae52-91e84ee2a697" alt=""><figcaption></figcaption></figure>

## Qodo 1.7

### Code Review, Reinvented - Meet Local Review

We’re thrilled to introduce Qodo Gen **version 1.7.0**, bringing a smarter way to review your code before you commit. This release puts quality and clarity front and center — helping you keep every branch clean, consistent, and ready for fast PRs.

#### Review Your Local Changes — Before You Commit

Meet the **Local Review** workflow — your new pre-commit review companion.

Before you push your code, get a complete understanding of what’s changed and why.

Here’s what it does for you:

* **Holistic Review:** Scans all local changes before commit, summarizing updates across files and themes.
* **Thematic Walkthrough:** Groups modified files by topic (features, fixes, refactors, etc.) for easier navigation.
* **Intelligent Insights:** Surfaces potential issues and suggestions by category (correctness, style, performance, best practices).
* **Instant Fixes:** With one click, resolve detected issues or apply suggestions — no context switching needed.
* **Project Alignment:** Validates that agent-written code follows your team’s conventions and rules, ensuring smoother PR reviews.

It’s like having a **senior reviewer on demand** — keeping your local branch clean, consistent, and production-ready.

<figure><img src="https://764298175-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsjA3HjeOPlxDJ3ZoBNVZ%2Fuploads%2FcWCqf6HJaQYFRjigY4LQ%2Flocal-review.gif?alt=media&#x26;token=b3aa1228-d527-4813-8113-5bcd62c03a57" alt=""><figcaption></figcaption></figure>

***

#### Farewell to Standard Mode

We’ve **removed the Standard mode** — it’s officially deprecated.\
Our smarter workflows now cover everything it used to do, and more.

***

#### A New Welcome Experience

Start strong with the **new Welcome Screen** — featuring quick access to your top quality-focused workflows:

* **Local Review**
* **Unit Test**
* **Cleanup**
* **Fix**

Keep your codebase clean, consistent, and bug-free from the very first click.

<figure><img src="https://764298175-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsjA3HjeOPlxDJ3ZoBNVZ%2Fuploads%2FEQCxMfq1e2Jb0mffFMKv%2Fimage.png?alt=media&#x26;token=371aaf25-427e-46c9-9bf8-7a43effa050d" alt=""><figcaption></figcaption></figure>
