# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/code-review/feedback-location.md

# Control Where Review Feedback Appears in PRs

Display mode controls **where Qodo’s review feedback appears** in a pull request.\
You can choose to surface feedback as a high-level summary, inline on the relevant code, or both, depending on how your team prefers to review and fix issues.

This setting helps balance **visibility vs. focus**: summaries are useful for understanding the overall state of a PR, while inline comments are ideal for resolving issues directly in context.

Example:

````toml
```toml
comments_location_policy = "both"
````

Supported values:&#x20;

* **`summary`**\
  Feedback appears only in the **Conversation** tab.\
  Best for reviewing the overall impact and prioritization of findings.
* **`inline`**\
  Feedback appears only in the **Files changed** view.\
  Best for fixing issues directly next to the affected code.
* **`both`**\
  Feedback appears in both the summary and inline views.

Summary example:

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FUcp4D5RK6HRt012YS3xW%2FSummary.png?alt=media&#x26;token=c8573011-a3a9-41c4-bb43-381565624fa1" alt=""><figcaption></figcaption></figure>

Inline example:

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2Fnj0VqbJtc9trtmXwTTDN%2FInline%20(2).png?alt=media&#x26;token=69fce705-d128-44ee-b427-c2a6af83b30a" alt=""><figcaption></figcaption></figure>
