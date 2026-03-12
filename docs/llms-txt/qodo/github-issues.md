# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/ticketing-integrations/github-issues.md

# GitHub Issues

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

Qodo will automatically recognize GitHub issues mentioned in the PR description and fetch the issue content.

Examples of valid GitHub issue references:

* `https://github.com/<ORG_NAME>/<REPO_NAME>/issues/<ISSUE_NUMBER>`
* `#<ISSUE_NUMBER>`
* `<ORG_NAME>/<REPO_NAME>#<ISSUE_NUMBER>`

Since Qodo is integrated with GitHub, it doesn't require any additional configuration to fetch GitHub issues.
