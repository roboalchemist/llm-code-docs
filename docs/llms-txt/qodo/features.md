# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/chrome-extension/features.md

# Features

## &#x20;<a href="#pr-chat" id="pr-chat"></a>

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

## PR Chat <a href="#pr-chat" id="pr-chat"></a>

The **PR Chat** feature allows you to ask questions and get AI-powered responses based on the content of your pull request, within your GitHub environment.

It uses the PR's code changes, description, and commits to build a rich context for the conversation.

### How to use PR Chat

PR Chat is available directly in the **Files changed** tab after installing the Qodo Chrome extension.

After installation, open at least one new PR to initialize access. You'll then be able to chat on both new and existing PRs.

### Privacy

All conversations are private and visible only to you.

PR Chat supports both public and private repositories.

For private repos, make sure Qodo Git interface is installed in your GitHub organization.

***

## **Context-aware PR Chat**

Qodo constructs a dynamic context for each PR that includes:

* Code changes
* PR description
* Commit messages
* Additional PR metadata

This context enables the AI to generate more accurate and relevant responses to user queries.

<figure><img src="https://codium.ai/images/pr_agent/pr_chat_1.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/pr_chat_2.png" alt="" width="563"><figcaption></figcaption></figure>

***

## Toolbar Extension <a href="#toolbar-extension" id="toolbar-extension"></a>

The Chrome extension adds a toolbar to the GitHub UI, allowing you to:

* Interactively test and configure Qodo tools
* Experiment with different settings
* For private repos, export the configuration to apply it automatically via commands or config files

<figure><img src="https://codium.ai/images/pr_agent/toolbar1.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/toolbar2.png" alt="" width="563"><figcaption></figcaption></figure>

***

## Qodo filters <a href="#qodo-merge-filters" id="qodo-merge-filters"></a>

The extension adds a side panel in the **Conversation** tab where you can filter messages by type:

* Show only Qodo messages
* Hide Qodo messages
* Focus on user-only messages

This helps in reviewing PR discussions more effectively.

<figure><img src="https://codium.ai/images/pr_agent/pr_agent_filters1.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/pr_agent_filters2.png" alt="" width="563"><figcaption></figcaption></figure>

***

## Enhanced code suggestions <a href="#enhanced-code-suggestions" id="enhanced-code-suggestions"></a>

The Chrome extension improves usability for the **code suggestions** feature by:

* Automatically expanding clipped code blocks for full visibility
* Adding a **"Quote & Reply"** button to suggestion comments for targeted follow-ups or review feedback

<figure><img src="https://codium.ai/images/pr_agent/chrome_extension_code_suggestion1.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/chrome_extension_code_suggestion2.png" alt="" width="563"><figcaption></figcaption></figure>
