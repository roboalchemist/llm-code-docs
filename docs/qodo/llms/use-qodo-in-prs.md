# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs.md

# Use Qodo in PRs

This guide explains how to use Qodo in pull requests, how reviews run, what you’ll see, and how to interact with review feedback as a developer.

Qodo works directly inside your Git provider and integrates into your existing pull request workflow. You can start using it immediately with default behavior, and customize it later as needed.

### What can you configure

Qodo works out of the box with sensible defaults, but its behavior can be customized to match your team’s standards and workflows.

Configuration controls things like:

* When reviews run (manual or automatic)
* Where feedback appears (summary, inline, or both)
* How strict or verbose reviews should be
* What content should be ignored

For a full breakdown of configuration options, file locations, and precedence, see the [**Configuration**](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview) fundamentals guide.

### Run a code review

Qodo can review pull requests in two ways: **manually** or **automatically**. Both approaches produce the same review experience and findings—the difference is when and how the review is triggered.

#### Run a review manually

You can request a review directly from the pull request by adding a comment:

```
/agentic_review
```

When you post the comment:

* Qodo acknowledges the request with a 👀 reaction
* The review is generated and posted directly in the pull request
* Feedback appears based on your configuration (summary, inline, or both)

Manual reviews are useful when:

* You want to review on demand
* You’re testing configuration changes
* You don’t want reviews to run on every PR update

#### Run reviews automatically

Qodo can also run reviews automatically when pull requests are opened or updated.

Automatic reviews are configured via `pr_agent.toml` and allow Qodo to:

* Run reviews when a PR is opened, reopened, or marked ready for review
* Update existing review comments when new commits are pushed
* Keep review feedback in sync with the latest code changes

Automatic reviews are ideal for teams that want:

* Consistent review coverage
* Less manual intervention
* Faster feedback loops

Automatic behavior is fully configurable. See the [**Configuration**](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview) fundamentals for details.&#x20;
