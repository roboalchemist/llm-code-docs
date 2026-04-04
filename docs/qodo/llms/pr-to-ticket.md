# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/pr-to-ticket.md

# PR to Ticket

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Supported Ticket providers:** Jira, Linear, GitHub Issues, GitLab Issues
{% endhint %}

The `create_ticket` tool automatically generates tickets in your ticket tracking system (Jira, Linear, GitHub Issues, or GitLab Issues) based on PR content.

It analyzes the PR’s data — including code changes, commit messages, and the PR description — to create well-structured tickets that capture the essence of the development work. This helps teams maintain traceability between code changes and project management systems.

When a ticket is created, it is added to the PR description under an **Auto-created Ticket** section, complete with a link to the generated ticket.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FNPthaPzqZ4OjC544wMof%2Fimage.png?alt=media&#x26;token=73668fb6-e8a8-4439-8774-c2bd2c1aa2ed" alt="" width="375"><figcaption></figcaption></figure>

## How to use the create\_ticket tool

### Pre-requisites

To use this tool, you must integrate your ticketing system with Qodo. [See the Ticket Compliance Documentation for setup instructions.](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/ticketing-integrations)

* **Jira Cloud users:** re-integrate your connection through the Qodo integration page to enable the update permission required for ticket creation.
* Configure the project key for the repository where the PR is created by adding `default_project_key` to your configuration:

```toml
[pr_to_ticket]
default_project_key = "PROJECT_KEY" # e.g., "SCRUM"
```

***

### Automatic Ticket Creation

The tool can automatically create tickets when:

* A PR is opened or updated
* The PR does not already have an associated ticket

To enable automatic ticket creation, add the following to your `.pr_agent.toml` configuration:

```toml
[pr_description]
auto_create_ticket = true
```

This ensures that every code change is documented in the ticketing system without manual intervention.

***

### Interactive Ticket Creation via Compliance Tool

{% hint style="info" %}
**Supported only on GitHub and GitLab**
{% endhint %}

The tool can be triggered interactively via a checkbox in the Compliance Tool during the PR Compliance Review workflow:

1. Check the **Create ticket** box in the Compliance Tool.
2. The tool will create the ticket and update the PR Description with an **Auto-created Ticket** section containing the link.
3. Click **Update** in the **Ticket Compliance** section to finalize.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FghOAGlKuFpTVm8iUv4H5%2Fimage.png?alt=media&#x26;token=10b68e9a-6a74-47a0-938b-84c26c72c106" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fx7We2byIcAN24yEpxqTC%2Fimage.png?alt=media&#x26;token=a855664f-ee30-420a-8e7c-f01064f1ed48" alt="" width="375"><figcaption></figcaption></figure>

***

### Manual Ticket Creation

You can trigger ticket creation manually from any PR by commenting:

```
/create_ticket
```

Once triggered, the tool will create the ticket and update the PR Description with an **Auto-created Ticket** section containing the link.

***

### Configuration Options

Configure the `create_ticket` tool by setting configurations under the `pr_to_ticket` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table data-header-hidden><thead><tr><th width="240.40234375">Possible configurations</th><th width="152.8359375">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>default_project_key</code></td><td>(none)</td><td>The default project key for your ticketing system (e.g., <code>"SCRUM"</code>). Required unless <code>fallback_to_git_provider_issues</code> is <code>true</code>.</td></tr><tr><td><code>default_base_url</code></td><td>(none)</td><td>If your organization uses multiple ticketing systems, you can set the default base URL here (e.g., <code>https://YOUR-ORG.atlassian.net</code>). Tickets will be created in this system by default.</td></tr><tr><td><code>fallback_to_git_provider_issues</code></td><td><code>false</code></td><td>If set to <code>true</code>, the tool will create issues in the Git provider's tracker (GitHub/GitLab) when <code>default_project_key</code> is not configured.</td></tr></tbody></table>

***

### Compliance Benefits <a href="#helping-your-organization-meet-soc-2-requirements" id="helping-your-organization-meet-soc-2-requirements"></a>

The `create_ticket` tool supports SOC-2 compliance by automatically creating tickets from PRs and establishing bidirectional links between them. This ensures every code change is traceable to its corresponding business requirement or task.
