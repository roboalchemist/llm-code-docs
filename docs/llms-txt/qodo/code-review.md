# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/code-review.md

# Generate a Code Review

Qodo’s code review analyzes each pull request using a multi-agent, context-aware review system.

The review focuses on surfacing issues that matter, explaining why they matter, and helping developers resolve them efficiently, without overwhelming you with low-signal feedback.

### What is the code review&#x20;

A Qodo finding includes:

* Actionability of the finding (Action requires, review recommended or other)
* Clear, human-readable explanations
* Direct references to the relevant lines of code
* Agent-assisted fix prompts and remediation guidance

Issues are grouped and prioritized so you can quickly understand what needs attention first.<br>

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2Fagjs1FiXBPa18JnoCerN%2Fimage.png?alt=media&#x26;token=62816330-3298-4868-8550-43a0aed136e8" alt=""><figcaption></figcaption></figure>

#### Where review feedback appears

Review feedback can appear in one or both of the following places, depending on configuration:

* Summary view (Conversation tab)
  * High-level overview of findings
  * Issue prioritization and explanations
* Inline view (Files changed)
  * Issues anchored directly to the relevant code
  * Ideal for fixing problems in context

### How to run a code review

#### **Manually**

To request a review on demand, add the following comment to the pull request:

`/agentic_review`

Qodo reacts to acknowledge the request and posts the review directly in the pull request.

#### **Automatically**

Qodo can run code reviews automatically when pull requests are opened or updated.

Automatic reviews are configured using `.pr_agent.toml` and allow Qodo to:

* Run reviews on PR open, reopen, or when marked ready for review
* Update existing review comments when new commits are pushed
* Keep feedback aligned with the latest code changes

See the [**Configuration Fundamentals**](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview) for details on enabling and customizing automatic code reviews.<br>
