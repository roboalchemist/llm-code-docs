# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/code-review/persistent-review-comments.md

# Persistent Review Comments

Persistent review comments allow Qodo to update an existing review comment when new commits are pushed, instead of posting a new review each time.

To enable this behavior, push-trigger handling must be enabled in your repository configuration.

Add the following inside your relevant git provider section in `.pr_agent.toml`. Do not include this in multiple provider sections.

Example (GitLab):

```toml
[gitlab]
handle_push_trigger = true
push_commands = [
  "/agentic_review"
]
```

After this is enabled, Qodo will automatically update the existing review comment whenever new commits are pushed to the pull/merge request.

### How it works

* With every new commit, Qodo updates the existing review comment.
* If a new issue is introduced in a new commit, it appears as an additional finding marked with a ⭐️ **New** label.
* All findings are visible directly in the pull request code review.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FiZRdgkKyALdWFUwm7NrZ%2FScreenshot%202026-02-10%20133103.png?alt=media&#x26;token=cc0f279b-b0ae-442c-a22d-ba4557c00b4c" alt=""><figcaption></figcaption></figure>

**Benefits**

* Keeps pull request conversations clean
* Makes it easier to track progress across commits
* Reduces noise during iterative reviews

### Audit trail

Qodo maintains an audit trail of review findings, including:

* Findings added per commit
* Findings resolved per commit

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FtcHRQVlBuSl6NHPyKly0%2FScreenshot%202026-02-10%20133126.png?alt=media&#x26;token=eb2e662f-0dd7-4c15-86c9-3d49a110646c" alt=""><figcaption></figcaption></figure>
