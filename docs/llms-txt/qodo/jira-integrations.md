# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/ticketing-integrations/jira-integrations.md

# Jira Integrations

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

## Jira Cloud <a href="#jira-cloud" id="jira-cloud"></a>

There are two ways to authenticate with Jira Cloud:

#### **1. Jira App Authentication**

The recommended way to authenticate with Jira Cloud is to install the Qodo app in your Jira Cloud instance. This will allow Qodo to access Jira data on your behalf.

**Installation steps:**

1. Go to the [Qodo integrations page](https://app.qodo.ai/qodo-merge/integrations).
2. Click on **Connect Jira Cloud** to connect the Jira Cloud app.
3. Click **Accept**.<br>

   <figure><img src="https://www.qodo.ai/images/pr_agent/jira_app_installation1.png" alt="" width="375"><figcaption></figcaption></figure>
4. After installing the app, you will be redirected to the Qodo registration page where you'll see a success message.
5. Qodo is now able to fetch Jira ticket context for your PRs.

#### **2. Email/Token Authentication**

You can create an API token from your Atlassian account:

1. Log in to the [API tokens page on Jira](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Click **Create API token**.
3. Enter a name for your new token and click **Create**.
4. Click **Copy to clipboard**.

<figure><img src="https://images.ctfassets.net/zsv3d0ugroxu/1RYvh9lqgeZjjNe5S3Hbfb/155e846a1cb38f30bf17512b6dfd2229/screenshot_NewAPIToken" alt="" width="375"><figcaption></figcaption></figure>

5. Add the following lines in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[jira]
jira_api_token = "YOUR_API_TOKEN"
jira_api_email = "YOUR_EMAIL"
```

## Jira Data Center/Server <a href="#jira-data-centerserver" id="jira-data-centerserver"></a>

#### **Using Basic Authentication**

You can use your Jira username and password to authenticate with Jira Data Center/Server.

In your Configuration file/Environment variables/Secrets file, add the following lines:

```bash
jira_api_email = "your_username"
jira_api_token = "your_password"
```

#### **Validating Basic authentication via Python script**

If you are facing issues retrieving tickets in Qodo with Basic auth, you can validate the flow using a Python script.

The following steps will help you check if the basic auth is working correctly, and if you can access the Jira ticket details:

1. Run:

```bash
pip install jira==3.8.0
```

2. Run the following Python script. Make sure to replace the placeholders with your actual values:

```python
from jira import JIRA


if __name__ == "__main__":
    try:
        # Jira server URL
        server = "https://..."
        # Jira PAT token
        token_auth = "..."
        # Jira ticket code (e.g. "PROJ-123")
        ticket_id = "..."

        print("Initializing JiraServerTicketProvider with JIRA server")
        # Initialize JIRA client
        jira = JIRA(
            server=server,
            token_auth=token_auth,
            timeout=30
        )
        if jira:
            print(f"JIRA client initialized successfully")
        else:
            print("Error initializing JIRA client")

        # Fetch ticket details
        ticket = jira.issue(ticket_id)
        print(f"Ticket title: {ticket.fields.summary}")

    except Exception as e:
        print(f"Error fetching JIRA ticket details: {e}")
```

## How to link a PR to a Jira ticket <a href="#how-to-link-a-pr-to-a-jira-ticket" id="how-to-link-a-pr-to-a-jira-ticket"></a>

To integrate with Jira, you can link your PR to a ticket using either of these methods:

#### **Method 1: Description Reference**

Include a ticket reference in your PR description, using either the complete URL format `https://<JIRA_ORG>.atlassian.net/browse/ISSUE-123` or the shortened ticket ID `ISSUE-123` (without prefix or suffix for the shortened ID).

#### **Method 2: Branch Name Detection**

Name your branch with the ticket ID as a prefix (e.g., `ISSUE-123-feature-description` or `ISSUE-123/feature-description`).

#### Jira Base URL

For shortened ticket IDs or branch detection (method 2 for JIRA cloud), you must configure the Jira base URL in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file) under the `[jira]` section:

```toml
[jira]
jira_base_url = "https://<JIRA_ORG>.atlassian.net"
```

Where `<JIRA_ORG>` is your Jira organization identifier (e.g., `mycompany` for `https://mycompany.atlassian.net`).

## Multi-JIRA Server Configuration <a href="#multi-jira-server-configuration" id="multi-jira-server-configuration"></a>

Qodo supports connecting to multiple JIRA servers using different authentication methods.

#### Email/Token (Basic Auth)

Configure multiple servers using Email/Token authentication in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

**Example Configuration:**

```toml
[jira]
# List of Jira Server URLs
jira_servers = ["https://company.atlassian.net", "https://datacenter.jira.com"]

# List of API tokens (for Cloud) or passwords (for Data Center)
jira_api_token = ["cloud_api_token_here", "datacenter_password"]

# List of emails (for Cloud) or usernames (for Data Center)
jira_api_email = ["user@company.com", "datacenter_username"]

# Default server for ticket IDs
# Each repository can configure its own jira_base_url in a local config file
# to choose which server to use by default.
jira_base_url = "https://company.atlassian.net"
```

#### PAT Auth

Configure multiple servers using Personal Access Token authentication in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

**Example Configuration:**

```toml
[jira]
# List of JIRA server URLs
jira_servers = ["https://server1.jira.com", "https://server2.jira.com"]

# List of PAT tokens
jira_api_token = ["pat_token_1", "pat_token_2"]

# Default server for ticket IDs
# Each repository can configure its own jira_base_url in a local config file
# to choose which server to use by default.
jira_base_url = "https://server1.jira.com"
```

**Mixed Authentication (Email/Token + PAT):**

```toml
[jira]
jira_servers = ["https://company.atlassian.net", "https://server.jira.com"]
jira_api_token = ["cloud_api_token", "server_pat_token"]
jira_api_email = ["user@company.com", ""]  # Empty for PAT
```

#### Jira Cloud App

For Jira Cloud instances using App Authentication:

1. Install the Qodo app on each JIRA Cloud instance you want to connect to.
2. In your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file), set the default server for ticket ID resolution:

```toml
[jira]
jira_base_url = "https://primary-team.atlassian.net"
```

Full URLs (e.g., `https://other-team.atlassian.net/browse/TASK-456`) will automatically use the correct connected instance.
