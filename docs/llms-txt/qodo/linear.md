# Source: https://docs.qodo.ai/qodo-documentation/code-review/integrations/ticketing-integrations/linear.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/ticketing-integrations/linear.md

# Linear

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

### Linear App Authentication <a href="#linear-app-authentication" id="linear-app-authentication"></a>

The recommended way to authenticate with Linear is to connect the Linear app through the Qodo portal.

#### Installation steps:

1. Go to the [Qodo integrations page](https://app.qodo.ai/qodo-merge/integrations).
2. Navigate to the **Integrations** tab.
3. Click on the **Linear** button to connect the Linear app.
4. Follow the authentication flow to authorize Qodo to access your Linear workspace.
5. Once connected, Qodo will be able to fetch Linear ticket context for your PRs.

### How to link a PR to a Linear ticket <a href="#how-to-link-a-pr-to-a-linear-ticket" id="how-to-link-a-pr-to-a-linear-ticket"></a>

Qodo will automatically detect Linear tickets using either of these methods:

#### **Method 1: Description Reference:**

Include a ticket reference in your PR description using either:

* **The complete Linear ticket URL:** `https://linear.app/[ORG_ID]/issue/[TICKET_ID]`&#x20;
* **The shortened ticket ID:**\
  `[TICKET_ID]` (e.g., `ABC-123`)\
  This method requires `linear_base_url` configuration (see below).

#### **Method 2: Branch Name Detection:**

Name your branch with the ticket ID as a prefix (e.g., `ABC-123-feature-description` or `feature/ABC-123/feature-description`).

### Linear Base URL

For shortened ticket IDs or branch detection, you must configure the Linear base URL in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file) under the \[linear] section:

```toml
[linear]
linear_base_url = "https://linear.app/[ORG_ID]" # your Linear organization identifier
```
