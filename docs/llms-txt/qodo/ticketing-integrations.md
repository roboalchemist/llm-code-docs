# Source: https://docs.qodo.ai/qodo-documentation/code-review/integrations/ticketing-integrations.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/ticketing-integrations.md

# Ticketing Integrations

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, Jira, Linear, Azure DevOps
{% endhint %}

Qodo enhances the code review process by integrating with your ticket management system. It automatically surfaces relevant ticket data alongside code changes, helping reviewers understand the intent behind a pull request.

### Ticket data fetched

The table below shows which ticket fields are fetched and used by Qodo for ticket context and compliance, per provider.

| Provider          | Title              | Description              | Custom Fields        | Subtasks / Children | Acceptance Criteria | Attachments              | Labels / Tags     |
| ----------------- | ------------------ | ------------------------ | -------------------- | ------------------- | ------------------- | ------------------------ | ----------------- |
| **Jira**          | ✔                  | ✔                        | ✔ (`customfield_*`)  | ✔                   | ✔\*                 | ✔ (≤3 images)            | ✔                 |
| **Linear**        | ✔                  | ✔                        | ✖                    | ✔                   | ✖                   | ✔ (≤3 images + embedded) | ✔                 |
| **Azure DevOps**  | ✔ (`System.Title`) | ✔ (`System.Description`) | ✖                    | ✖                   | ✔ (dedicated field) | ✖                        | ✔ (`System.Tags`) |
| **Monday.com**    | ✔                  | ✔                        | ✔ (`long_text` cols) | ✔                   | ✖                   | ✖                        | ✔                 |
| **GitHub Issues** | ✔                  | ✔                        | ✖                    | ✔                   | ✖                   | ✖                        | ✔                 |
| **GitLab Issues** | ✔                  | ✔                        | ✖                    | ✔                   | ✖                   | ✖                        | ✔                 |

\* Acceptance criteria in Jira is supported only when stored in a custom field.

### Ticket Recognition Criteria

A ticket is linked to a PR if:

* The PR description contains a direct link to the ticket, **or**
* The branch name matches an accepted ticket reference pattern (see accepted syntax for details)

#### Accepted syntax

| Provider   | Supported examples                                                                                                                                                                                                                                                                                                                                                                                                 | Not supported                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Jira**   | <p><code>PROJ-123</code><br><code>proj-123</code><br><code>feature/PROJ-123</code><br><code>feature/PROJ-123/add-new-feature</code><br><code>feature/PROJ-123-add-new-feature</code><br><code>fix-PROJ-123-bug</code><br><code>TSAASO-3250-cluster-labels</code><br><code>ABC-5678\_v2</code><br><code>\[PROJ-123]-hotfix</code><br><code>release-v1.2-PROJ-123-impl</code><br><code>bugfix-abc-456-fix</code></p> | <p><code>PROJ123</code><br><code>P-123</code><br><code>PROJ1-123</code><br><code>VERYLONGPROJECT-123</code><br><code>PROJ-12345678</code></p>                              |
| **Linear** | <p><code>PLT-2837</code><br><code>plt-2837</code><br><code>plt-2837-be-rename-env-file</code><br><code>A1B2-456</code><br><code>feature/PLT-2837</code><br><code>feature/PLT-2837-add-feature</code><br><code>release/v1.2/PLT-2837</code><br><code>hotfix/ABC-123/urgent</code></p>                                                                                                                               | <p><code>fix-PLT-2837</code><br><code>bugfix\_PLT-2837</code><br><code>feature-PLT-2837-bug</code><br><code>\[PLT-2837]</code><br><code>PREFIX/feature-PLT-2837</code></p> |

> **Notes:**
>
> * Branch-based detection is always enabled
> * Supported patterns are fixed in production and cannot be configured
> * Matching is case-insensitive
> * The ticket ID must appear at the start of the branch name or immediately after a `/`

***

### Tool Behavior

#### Describe tool <a href="#describe-tool" id="describe-tool"></a>

When a ticket is recognized, the describe tool includes ticket content (title, description, labels) in its analysis. This provides the model with additional context for understanding the purpose behind the code changes.

#### Review tool <a href="#review-tool" id="review-tool"></a>

The review tool also incorporates ticket context into its analysis. Additionally, it evaluates whether the PR aligns with the ticket’s intent, assigning one of the following labels:

* **Fully Compliant:** PR directly addresses the ticket requirements
* **Partially Compliant:** PR covers some but not all of the requirements
* **Not Compliant:** PR does not align with the ticket’s intent
* **PR Code Verified:** Code appears valid for the ticket, but additional manual testing (e.g., UI checks across devices) is required

<figure><img src="https://www.qodo.ai/images/pr_agent/ticket_compliance_review.png" alt="" width="563"><figcaption></figcaption></figure>

***

## Configuration Options

By default, the tool will automatically validate if the PR complies with the referenced ticket. If you want to disable this feedback, add the following line to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[pr_reviewer]
require_ticket_analysis_review=false
```

You can also set:

```toml
[pr_reviewer]
check_pr_additional_content=true
```

When enabled, Qodo will check that all code changes are related to the ticket. If unrelated content is found, the PR will be downgraded (e.g., to **PR Code Verified**), and a comment will indicate the extra content. The default is `false`.
