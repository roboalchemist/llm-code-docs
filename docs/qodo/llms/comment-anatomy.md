# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/comment-anatomy.md

# Anatomy of Qodo Findings in a PR

Qodo surfaces code review feedback directly inside your pull requests in a way that is actionable, focused, and easy to resolve. \
\
This guide explains how Qodo structures pull request feedback, from high-level context to individual issue findings, and how to read, prioritize, and act on it effectively.

Designed for developers, Qodo’s code suggestions focus on what requires attention and why, with clear links back to the relevant code. Information is exposed incrementally, starting with a high-level summary and expanding into details only when needed, making it easy to ignore low-signal noise. Each finding is meant to be resolved explicitly, either by fixing the issue or dismissing it, so reviews feel finite and manageable rather than an ongoing inbox.

### High-level context

Before presenting individual issues, Qodo provides context to help you understand *what changed* and *why it matters*.

#### PR description enhancement

Qodo adds an AI-generated description to the pull request that summarizes the intent and impact of the change.

* Your original PR description remains unchanged
* The generated description is appended below it
* The summary highlights key changes and potential areas of interest

This helps reviewers align quickly on the purpose of the pull request.

#### Walkthroughs

Qodo provides walkthroughs that explain the changes at a conceptual level before diving into individual issues.

**Description walkthrough**

The description walkthrough outlines the most important changes, such as:

* New functionality or methods introduced
* Refactors or behavioral changes
* Logging, security, or performance-related updates
* Risky or noteworthy patterns

This section reads like a reviewer-friendly changelog.

**Diagrams**

When applicable, Qodo includes diagrams to visually explain:

* Control flow
* Component interactions
* Execution order changes

Diagrams help reviewers understand complex logic at a glance, without reconstructing behavior from the diff.

#### File changes overview

Qodo provides a file-level overview of the pull request.

For each modified file, you can see:

* The file path
* The type of change (for example, Bug Fix or Enhancement)
* Lines added and removed

This helps reviewers understand the scope of the change set before examining individual findings.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FAzqAMCzOBmK7ElOxjkVD%2FPR%20summary.png?alt=media&#x26;token=c156bd33-789f-4b8a-9931-369a3c8010f2" alt=""><figcaption></figcaption></figure>

### Summary of findings

After providing context, Qodo presents a **summary of findings**, grouped by category with counts for each type.

Categories include:

* **🐞 Bugs** – Issues that may cause incorrect behavior or failures
* **📘 Rule violations** – Violations of organizational or repository rules
* **📎 Requirement gaps** – Missing or unmet business or ticket requirements

This summary gives you an immediate sense of the review’s focus and severity.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FKPcZmXl51vcAOkvs0Yi1%2FIssues%20overview.png?alt=media&#x26;token=1a8b6a47-ef4c-489e-95f3-f1a7d3d4b33d" alt=""><figcaption></figcaption></figure>

### Quality impact labels

In addition to categories, each finding includes a **quality impact label**. This label indicates which quality dimension is affected by the issue.

Common labels include:

* **Correctness** – Issues that may cause incorrect behavior or wrong results
* **Security** – Issues that could expose vulnerabilities or sensitive data
* **Reliability** – Issues that may affect stability, error handling, or fault tolerance
* **Performance** – Issues that impact efficiency, latency, or resource usage
* **Observability** – Issues that affect logging, metrics, or system visibility

These labels provide quick semantic context, helping you understand *what kind of quality is impacted* before diving into the full issue details.

### Severity and prioritization

Findings are grouped by **priority**, making it clear what needs attention first.

#### Action required

High-priority or blocking issues that should be addressed before merging, such as:

* Security or compliance violations
* Sensitive data exposure
* Critical correctness issues

#### Remediation recommended

Non-blocking issues that improve:

* Code quality
* Maintainability
* Consistency with defined standards

#### Other

Lower-impact or informational findings that provide context or optional guidance.

This prioritization helps you focus on what matters most without losing visibility into the full set of findings.

### Issue details

Each finding can be expanded to reveal full details. You can access issues:

* From the prioritized summary list
* Inline, directly in the **Files changed** view

Regardless of how you access it, each issue presents the same structured information.

#### Description

A clear, human-readable explanation of the issue and its potential impact.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FTPrOI7Ms0aGQLi6z1PCm%2FDescription.png?alt=media&#x26;token=b2cbc20a-f3d3-476a-a596-b6239f503a2f" alt=""><figcaption></figcaption></figure>

#### Code references

* A snippet showing where the issue occurs
* Direct links to the relevant lines in the pull request

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2Fl9r4vKWAlb0uwc2ZzPby%2FCode.png?alt=media&#x26;token=05ce0beb-b9a0-43d7-b0fb-6fb43926fd4d" alt=""><figcaption></figcaption></figure>

#### Relevance&#x20;

{% hint style="success" %}
This feature is currently available in beta for single-tenant customers and is supported for GitHub and GitLab repositories. Entries are generated automatically based on [PR history.](https://docs.qodo.ai/qodo-documentation/code-review/concepts/pr-history)
{% endhint %}

The **Relevance** section highlights related pull requests with similar findings from past reviews. This provides historical context by linking to previous PRs where a similar issue was discussed, accepted, or rejected.

Each entry includes:

* A relevance classification indicating whether the finding has high, medium, or low relevance based on how similar findings were handled in past PRs.\
  ⭐ ⭐ ⭐ **High** - similar findings were typically accepted/fixed\
  ⭐ ⭐       **Medium** - mixed or inconclusive history\
  ⭐             **Low** - similar findings were typically ignored
* A brief explanation of the historical pattern
* Links to relevant past pull requests
* An indicator that the insight was generated from similar findings

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FWYNvboeauYgQZO5DEqHy%2FRelevance.png?alt=media&#x26;token=3a93c3ed-8fa6-4b7a-9321-d7108ace81ca" alt=""><figcaption></figcaption></figure>

#### Evidence

Context explaining *why* the issue was flagged, such as:

* The specific rule involved
* Linked requirements or tickets (when applicable)

This transparency makes it easier to trust and validate the feedback.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2Fu75TAApbR8FfHEFTvQNz%2FEvidence.png?alt=media&#x26;token=9d3f84a3-697f-4014-a4ba-9c3244350fd3" alt=""><figcaption></figcaption></figure>

#### Agent prompt (fix assistance)

For issues that can be fixed programmatically, Qodo provides an **agent prompt**. You can copy the prompt and use it in an AI coding tool to apply the suggested fix with full context, helping you move from feedback to resolution faster.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FizaEfrzEe9BPJNOrZQA7%2FPrompt.png?alt=media&#x26;token=0998eb27-175d-464f-8c16-ac0957c2f312" alt=""><figcaption></figcaption></figure>

### Audit trail

The Audit section shows how findings change as the pull request evolves:

* ⭐ Starred findings highlight newly added findings in the latest commit
* Findings resolved or dismissed as changes are made
* A clear view of progress across commits

This helps reviewers understand how issues were introduced and resolved over time.

### Resolved findings

As you address issues:

* Findings update as relevant code changes
* Resolved issues are reflected in the review
* Remaining items stay visible until fixed or dismissed

This supports a clear, zero-inbox workflow where reviews move steadily toward completion.
