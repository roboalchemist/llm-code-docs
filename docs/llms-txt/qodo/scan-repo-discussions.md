# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/scan-repo-discussions.md

# Scan Repo Discussions

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub
{% endhint %}

The `scan_repo_discussions` tool analyzes past PR discussions and metadata to identify recurring feedback patterns, then generates a `best_practices.md` file with key insights and recommendations.

The `best_practices.md` file captures patterns specific to your team's workflow, based on real PR discussions. Qodo uses it to give more tailored, context-aware suggestions in future pull requests.&#x20;

[Learn more about the best practices file.](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/best-practices)

{% hint style="warning" %}

### Active repositories are needed

The tool is designed to work with real-life repositories, as it relies on actual discussions to generate meaningful insights.

Notice that **at least 50 merged PRs** are required to generate a `best_practices.md` file.
{% endhint %}

## How to use the `/scan_repo_discussions` tool

**Manual usage**

Comment on the PR:

```
/scan_repo_discussions
```

Qodo will create a new PR that contains an auto-generated `best_practices.md` file.

{% hint style="info" %}
**Note:** Since up to 250 PRs are scanned, the scan could take several minutes to complete.
{% endhint %}

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

To force generating a PR with a new `best_practices.md` file, even if it already exists, use:

```bash
/scan_repo_discussions --scan_repo_discussions.force_scan=true
```

To specify how many days of discussions should be included in the scan, use:

```bash
/scan_repo_discussions --scan_repo_discussions.days_back=X # Default is 365
```

&#x20;To specify the minimum number of merged PRs needed to generate the `best_practices.md` file, use:

```bash
/scan_repo_discussions --scan_repo_discussions.minimal_number_of_prs=X # Default is 50
```

## Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://codium.ai/images/pr_agent/scan_repo_discussions_1.png" alt="" width="563"><figcaption></figcaption></figure>

The PR created by the bot:

<figure><img src="https://codium.ai/images/pr_agent/scan_repo_discussions_2.png" alt="" width="563"><figcaption></figcaption></figure>

The `best_practices.md` file in the PR:

<figure><img src="https://codium.ai/images/pr_agent/scan_repo_discussions_3.png" alt="" width="563"><figcaption></figcaption></figure>
