# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/gitbook-agent/what-is-gitbook-agent.md

# Source: https://gitbook.com/docs/documentation/zh/gitbook-dai-li-agent/what-is-gitbook-agent.md

# Source: https://gitbook.com/docs/documentation/fr/agent-gitbook/what-is-gitbook-agent.md

# Source: https://gitbook.com/docs/gitbook-agent/what-is-gitbook-agent.md

# What is GitBook Agent?

GitBook Agent is an AI teammate that works alongside you, helping you keep your documentation accurate, complete, and current.

The Agent is deeply integrated into GitBook, so you don’t need to learn new workflows to take advantage of it — it works alongside you using the processes you already know.

{% hint style="info" %}
If you’d like to edit your docs in your local environment using an AI assistant, you can use [GitBook's skill.md file](https://gitbook.com/docs/creating-content/ai-coding-assistants-and-skill.md).
{% endhint %}

### What can GitBook Agent do?

GitBook Agent can:

* **Write docs based on a prompt:** Ask the Agent to update a page with the latest information, replace every mention of a product name with a new name, or anything else you need.
* **Ideate and implement bigger changes:** Describe what you need and the Agent will open a change request, explain its planned edits, respond to your feedback, and then implement the plan you’ve created together.
* **Understand your style guide:** Add your style guide into your org’s settings and it will always apply it when writing or reviewing content.
* **Follow custom, organization-level instructions:** Give the Agent specific instructions at an organization level, such as adding links in specific ways, or avoiding specific block types.
* **Translate your documentation:** Choose the content you want to translate, select a language and the Agent will do the work of localizing your docs.
* **Summon from a comment:** Add a comment to any block on your page, type @gitbook and tell the Agent what you need.
* **Review change requests:** Add the Agent as a reviewer on your change request. It can act as a docs linter, identifying or fixing errors, suggesting improvements and flagging style guide deviations.

#### Automatic documentation suggestions

The Agent can also connect to the same signals your team uses to understand your product and what your users need: support conversations, tickets, and threads from your connected tools.

With this context, the Agent can proactively identify gaps, propose updates and generate docs changes automatically. So your docs can evolve with your product, and your users always get the right information when and where they need it.

{% hint style="info" %}
**Automatic docs suggestions are in early access**

Head to **Organization Settings → GitBook Agent** to request access.
{% endhint %}

### Explore GitBook Agent’s features

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Write with GitBook Agent</strong></td><td>Create content based on a prompt or edit a single block</td><td><a href="write-and-edit-with-ai">write-and-edit-with-ai</a></td></tr><tr><td><strong>Review with GitBook Agent</strong></td><td>Ask the Agent to check your work for spelling, grammar and style</td><td><a href="review-change-requests-with-gitbook-agent">review-change-requests-with-gitbook-agent</a></td></tr><tr><td><strong>Translate your docs site</strong></td><td>GitBook Agent can create auto-updating localizations</td><td><a href="translations">translations</a></td></tr></tbody></table>

### Add a style guide and custom instructions

You can configure GitBook Agent by adding your team’s style guide or specific instructions on how you’d like it to work with your team. The Agent will use these as context whenever it creates or edits content in your organization.

To add a style guide or custom instructions, open your **Organization settings** and then choose the **GitBook Agent** section. Click the **Settings** tab and add your instructions in the text entry field.

You can quickly access this screen by opening the GitBook Agent chat window in a change request, then opening the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt=""></picture> and choosing **Configure GitBook Agent** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F6uYUpJto7WTkJf9BUPHv%2Fsettings%20-%20dark.svg?alt=media&#x26;token=bf52415f-e999-43a2-9a1a-c85176a014cd" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwkBqgOPry9HAcW4cxJk0%2Fsettings.svg?alt=media&#x26;token=67bdbb00-ebf3-4a2d-9df8-0c822406f71c" alt=""></picture>.

#### Custom instructions example

Here’s an example of the kind of custom instructions you could add in GitBook Agent’s settings.

<pre data-overflow="wrap"><code><strong>You are a technical writer at Stripe. Use clear, direct language and prioritize accuracy over flourish. For guides, always introduce the concept with a one-sentence summary and break content into well-structured sections. For quickstarts, always use a stepper and keep every step action-first and concise.
</strong></code></pre>

### FAQs

<details>

<summary>How does GitBook Agent use my data?</summary>

We always follow our data protection practices to keep your data private.

GitBook Agent does not use your data to train AI models. We share the information you add to GitBook Agent with OpenAI for the sole purpose of providing you with GitBook AI’s features. Take a look at OpenAI’s privacy policy for more information.

</details>

<details>

<summary>How much does GitBook Agent cost?</summary>

GitBook Agent is free for all plans while in beta.

[Translations](https://gitbook.com/docs/gitbook-agent/translations) are priced separately as a monthly add-on. Visit [the pricing section](https://gitbook.com/docs/translations#pricing) to find out more.

</details>
