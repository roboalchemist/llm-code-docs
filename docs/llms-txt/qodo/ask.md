# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/capabilities/ask.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/ask.md

# Ask

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

The `ask` tool answers questions about the PR, based on the PR code changes.

Make sure to be specific and clear in your questions. It can be invoked manually by commenting on any PR:

```
/ask ...
```

***

## Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FNEVoveqMkuSuI6YdZ39z%2Fimage.png?alt=media&#x26;token=3ace434c-571a-4eaf-ab59-0f3fb03e9f14" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F92oFrLdhfT7oDbr28RcS%2Fimage.png?alt=media&#x26;token=3c899332-d94b-43ad-ae50-0c4a3cad50bc" alt="" width="563"><figcaption></figcaption></figure>

***

## How to use the `ask` tool

**Manual usage**

Comment on the PR:

```bash
/ask
```

### Ask on specific lines <a href="#ask-lines" id="ask-lines"></a>

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

You can run `/ask` on specific lines of code in the PR from the PR's diff view. The tool will answer questions based on the code changes in the selected lines.

1. Click on the **+** sign next to the line number to select the line.
2. To select multiple lines, click on the **+** sign of the first line, then hold and drag to select more lines.
3. In the comment box, type `/ask` followed by your question.
4. Click the `Add single comment` button.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FOrzBbVZ98IvlTo9bZjbH%2Fimage.png?alt=media&#x26;token=b942f395-2648-4d16-ade8-add000b59204" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**: The tool does not hold memory of previous questions, and answers each question independently.
{% endhint %}

### Ask on images <a href="#ask-on-images" id="ask-on-images"></a>

You can ask questions about images in comments, where the entire PR code will be used as context:

```bash
/ask "..."[Image](https://real_link_to_image)
```

Where `https://real_link_to_image` is the direct link to the image.

GitHub has a built-in mechanism of pasting images in comments. However, a pasted image does not provide a direct link. To get a direct link to an image, we recommend using the following scheme:

1\. First, post a comment that contains **only** the image:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fv4WpvoDU6At30DaIpf9s%2Fimage.png?alt=media&#x26;token=9385da7e-6d8c-46bd-b7b7-3a01f68cbff6" alt="" width="563"><figcaption></figcaption></figure>

2\. Click the **three dots ...** on the top right of the comment, then choose **Quote reply**.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F5bx8wf5TRF4gDjs6RscW%2Fimage.png?alt=media&#x26;token=45c0ae00-6dcd-4d62-874f-df2f01be6421" alt="" width="563"><figcaption></figcaption></figure>

3\. In the opened chatbox, type the question below the image:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FaB1WMgHmeCVEiuP5LCKd%2Fimage.png?alt=media&#x26;token=043e0cef-4588-4bdd-980f-2ab653df9b46" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FJHAFuE0cfuH014UfmYU6%2Fimage.png?alt=media&#x26;token=30f7e303-e34b-4f19-a278-ee022cf74d84" alt="" width="563"><figcaption></figcaption></figure>

4\. Post the comment, and receive the answer:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fr1kpvASBdKaOWMSFs894%2Fimage.png?alt=media&#x26;token=70e4ca71-76d4-4aa5-b1f8-a48fc2d8cbbd" alt="" width="563"><figcaption></figcaption></figure>
