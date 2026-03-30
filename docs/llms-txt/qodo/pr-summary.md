# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/pr-summary.md

# Generate a PR Summary

Qodo can generate or enhance pull request descriptions to make reviews easier and more efficient.

### What is a PR summary

The PR summary helps reviewers quickly understand the change by providing:

* A clear description of the purpose and scope of the pull request
* A walkthrough of the main changes across files
* Highlights of important or risky modifications
* Optional diagrams that explain complex flows or interactions

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FAzqAMCzOBmK7ElOxjkVD%2FPR%20summary.png?alt=media&#x26;token=c156bd33-789f-4b8a-9931-369a3c8010f2" alt=""><figcaption></figcaption></figure>

### How to generate a PR summary

#### **Manually**&#x20;

You can generate or update the summary manually by commenting on the pull request:

`/agentic_describe`

Qodo acknowledges the request and posts the generated summary directly in the pull request.

#### **Automatically**&#x20;

You can configure Qodo to generate summaries automatically when pull requests are opened or updated.

Automatic behavior is configured using `.pr_agent.toml`. See the [**Configuration Fundamentals** ](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview) for details on enabling automatic summaries.<br>
