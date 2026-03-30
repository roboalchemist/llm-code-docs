# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/implement.md

# Implement

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

The `implement` tool converts human code review discussions and feedback into ready-to-commit code changes.

It leverages LLM technology to transform PR comments and review suggestions into concrete implementation code, helping developers quickly turn feedback into working solutions.

Note that the implementation will occur within the review discussion thread.

## How to use the `/implement` tool

{% tabs %}
{% tab title="For Reviewers" %}
Reviewers can request code changes by:

1. Selecting the code block to be modified.
2. Adding a comment:

```bash
/implement <code-change-description>
```

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fz5LAprMa7rSUr5dJ5Sde%2Fimage.png?alt=media&#x26;token=bc959bd0-ca03-41bf-b5cb-e6a9efda7edf" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="For PR Authors" %}
PR authors can implement suggested changes by replying to a review comment.

You can do this by either:

* Adding specific implementation details by commenting:

```bash
/implement <code-change-description>
```

* Using the original review comment as instructions:

```bash
/implement
```

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F3yNs0aQd46QYizEqFRCR%2Fimage.png?alt=media&#x26;token=727c5932-947c-4865-8976-b6ce37de09f0" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="For Referencing Comments" %}
You can respond to an inline comment by triggering the tool from anywhere in the thread:

```bash
/implement <link-to-an-inline-comment>
```

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FAnnvUy2NelANBdXtT7Qh%2Fimage.png?alt=media&#x26;token=902baa76-bc2e-4f98-9711-66a97f910931" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## **Configuration options**

To implement based on the review discussion:

```bash
/implement
```

To implement specific instructions, inside a review discussion use:

```bash
/implement <code-change-description>
```

To indirectly call the tool from any comment, use:

```bash
/implement <link-to-review-comment>
```
