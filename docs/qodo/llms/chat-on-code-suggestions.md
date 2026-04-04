# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/chat-on-code-suggestions.md

# Chat on Code Suggestions

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

Qodo lets you leave comments on code suggestions to make changes. Its smart agent reads your comments and figures out what you want to do—whether that’s applying a change, asking a question, or requesting help—and uses the right tool automatically.

## How does it work?

Behind the scenes, Qodo calls an orchestrator agent. The orchestrator analyzes your responses to determine if you want to implement a suggestion, ask a question, or request help, then uses the right tool automatically.

## Setup <a href="#setup" id="setup"></a>

Enable interactive code discussions by adding the following to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file) (default is `True`):

```toml
[pr_code_suggestions]
enable_chat_in_code_suggestions = true
```

### Activation <a href="#activation" id="activation"></a>

[**`/improve`**](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/improve)

To get dynamic responses from Qodo after running `/improve`, follow these steps:

1. Run the `/improve` command.
2. Check the `/improve` recommendation checkboxes (**Apply this suggestion** button) to have Qodo generate a new inline code suggestion discussion.
3. The orchestrator agent will then automatically listen to and reply to comments within the discussion without requiring additional commands.

[**`/implement`**](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/implement)

To get dynamic responses from Qodo after running `/implement`, follow these steps:

1. Select code lines in the PR diff and run the `/implement` command.
2. Wait for Qodo to generate a new inline code suggestion.
3. The orchestrator agent will then automatically listen to and reply to comments within the discussion without requiring additional commands.

{% hint style="success" %}
**Tip: Direct the agent with keywords.**

Use "implement" or "apply" for code generation.

Use "explain", "why" or "how" for information and help.
{% endhint %}

## Example Usage

{% tabs %}
{% tab title="Asking for more details" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fri0E61RG1y5mbMM85QHG%2Fimage.png?alt=media&#x26;token=bbbc707b-4a3e-41f9-83f6-d9718d78d69f" alt="" width="563"><figcaption><p>Asking for more details</p></figcaption></figure>
{% endtab %}

{% tab title="Implementing suggestions" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FBhUgaaTTSwaf2DvufItt%2Fimage.png?alt=media&#x26;token=2dde956e-f6fe-4c61-b289-07fbc3345dcd" alt="" width="563"><figcaption><p>Implementing suggestions</p></figcaption></figure>
{% endtab %}

{% tab title="Providing additional help" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FVzOtIZFIz4gy0Ib3JzsO%2Fimage.png?alt=media&#x26;token=a34f277d-2d09-4b54-9e28-57a669b5d5a4" alt="" width="563"><figcaption><p>Providing additional help</p></figcaption></figure>
{% endtab %}
{% endtabs %}
