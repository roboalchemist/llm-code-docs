# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/code-review/auto-detected-questions.md

# Enable Automatic Question Detection

{% hint style="success" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

Let Qodo automatically recognize questions written in pull request comments. When enabled, Qodo scans comments and replies when it detects a question related to the code or PR discussion.

This is useful for more natural conversations during code reviews.

#### How it works

* You write a comment that includes a question (for example: *“Why are we handling retries here instead of the caller?”*)
* Qodo detects the question
* Qodo replies using the relevant pull request context

#### Enable automatic question recognition

To enable this behavior, add the following to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/configuration-file):

```toml
[pr_code_suggestions]
enable_chat_in_code_suggestions = true
```

Once enabled, Qodo will automatically respond to recognized questions in PR comments.

{% tabs %}
{% tab title="Asking for more details" %}

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2Fix4Xdb0kykpdDXe2wlK4%2Fimage.png?alt=media&#x26;token=ede3ef34-1e77-44f5-9438-1f981f5932b2" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Implementing suggestions" %}

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FqcTfHX3tl2awnaPHw6uG%2Fimage.png?alt=media&#x26;token=2f9add41-e78b-4989-a592-d420b8f844e8" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Providing additional help" %}

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FBkEfwPxzb04K5xaoYn81%2Fimage.png?alt=media&#x26;token=3a3098e8-b49c-411c-b572-09d085ed0962" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### Tips for better automatic responses

* Phrase your comment clearly as a question
* Use words like *why*, *how*, *what*, or *can we*
* Keep questions focused on the code or changes in the PR
