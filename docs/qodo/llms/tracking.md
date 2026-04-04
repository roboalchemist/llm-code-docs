# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/learn-more/tracking.md

# Tracking

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

## Tracking Implemented Suggestions

**Qodo** automatically tracks when AI-generated suggestions are applied, helping teams measure the impact of the tool and improve future results.

There are two ways Qodo detects implementation:

* **Direct Implementation:** When the PR author clicks the **Apply** checkbox next to a suggestion.
* **Indirect Implementation:** When the suggestion is applied manually (e.g., through the user’s IDE). Qodo checks each new commit to identify if the suggested change was implemented, even without clicking **Apply**.

These implementations are logged and used to generate stats and insights into how suggestions are being used across pull requests.

<figure><img src="https://codium.ai/images/pr_agent/code_suggestions_asses_impact.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/code_suggestions_asses_impact_stats_1.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/code_suggestions_asses_impact_stats_2.png" alt="" width="563"><figcaption></figcaption></figure>

***

## Suggestion tracking <a href="#suggestion-tracking" id="suggestion-tracking"></a>

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

{% hint style="warning" %}
**Wiki must be enabled**

Repositories require a one-time manual wiki setup to enable this feature.
{% endhint %}

All accepted suggestions are automatically saved in a dedicated file: `.pr_agent_accepted_suggestions`, within your repo's wiki.

This file serves multiple purposes:

* Tracks which suggestions were implemented
* Offers a historical view of accepted improvements
* Helps assess Qodo’s long-term value and influence
* Feeds future model training to improve the quality of recommendations

This feature is controlled by [the configuration](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file)\
`pr_code_suggestions.wiki_page_accepted_suggestions` (default: `true`).

<figure><img src="https://qodo.ai/images/pr_agent/pr_agent_accepted_suggestions1.png" alt=""><figcaption></figcaption></figure>

### Why a Wiki?

Your code stays private. Instead of using an external server or database, Qodo stores accepted suggestions in your repository’s **private wiki**.

This ensures:

* Full control over your data
* No interference with the main repo or pull requests
* A secure, organized place to track suggestions
