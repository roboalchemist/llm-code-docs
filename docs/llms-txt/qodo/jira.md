# Source: https://docs.qodo.ai/qodo-documentation/code-review/integrations/ticketing-integrations/jira.md

# Integrate Qodo with Jira

### Jira Cloud <a href="#jira-cloud" id="jira-cloud"></a>

Jira is supported as an external ticketing integration and can be used with supported repository platforms by referencing tickets in the PR description or branch name.

There are two ways to authenticate with Jira Cloud:

#### **Jira App Authentication**

The recommended way to authenticate with Jira Cloud is to install the Qodo app in your Jira Cloud instance. This will allow Qodo to access Jira data on your behalf.

1. Go to the Qodo Integrations page.
2. Click on **Connect Jira Cloud** to connect the Jira Cloud app.
3. Click **Accept**.

   ![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2Fwww.qodo.ai%2Fimages%2Fpr_agent%2Fjira_app_installation1.png\&width=768\&dpr=3\&quality=100\&sign=7b7286fe\&sv=2)
4. After installing the app, you’ll be redirected to the Qodo registration page with a confirmation message.&#x20;

Qodo can now fetch Jira ticket context for your pull requests.

#### **Email/Token Authentication**

You can create an API token from your Atlassian account:

1. Log in to the [API tokens page on Jira](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Click **Create API token**.
3. Enter a name for your new token and click **Create**.
4. Click **Copy to clipboard**.\
   ![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fzsv3d0ugroxu%2F1RYvh9lqgeZjjNe5S3Hbfb%2F155e846a1cb38f30bf17512b6dfd2229%2Fscreenshot_NewAPIToken\&width=768\&dpr=3\&quality=100\&sign=fb523a81\&sv=2)
5. Add the following lines in your [configuration file](https://docs.qodo.ai/qodo-documentation/qodo-merge/configuration/configuration-file):

```
[jira]
jira_api_token = "YOUR_API_TOKEN"
jira_api_email = "YOUR_EMAIL"
```

### Jira Data Center/Server <a href="#jira-data-centerserver" id="jira-data-centerserver"></a>

#### Basic authentication

You can authenticate with Jira Data Center or Server using your Jira username and password.

Add the following values to your configuration file, environment variables, or secrets file:

```
jira_api_email = "your_username"
jira_api_token = "your_password"
```

#### **Validating Basic authentication via Python script**

If you’re experiencing issues retrieving tickets in Qodo when using Basic authentication, you can validate the setup with a Python script. The steps below help verify that Basic authentication is working correctly and that Jira ticket details are accessible.

1. Run:

```
pip install jira==3.8.0
```

2. Run the following Python script. Make sure to replace the placeholders with your actual values:

```
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

### How to link a PR to a Jira ticket <a href="#how-to-link-a-pr-to-a-jira-ticket" id="how-to-link-a-pr-to-a-jira-ticket"></a>

Qodo automatically detects Jira tickets using one of the following methods:

#### Method 1: PR description reference

Include a ticket reference in your pull request description using either:

* The full Jira ticket URL:\
  `https://<JIRA_ORG>.atlassian.net/browse/<TICKET_ID>`
* The shortened ticket ID (for example, `ISSUE-123`)

For shortened ticket IDs, the Jira base URL must be configured (see below).

#### Method 2: Branch name detection

Prefix your branch name with the ticket ID, for example:

* `ISSUE-123-feature-description`
* `feature/ISSUE-123/feature-description`

***

### Jira base URL

For shortened ticket IDs or branch name detection (Jira Cloud), configure the Jira base URL in your configuration file under the `[jira]` section:

```toml
[jira]
jira_base_url = "https://<JIRA_ORG>.atlassian.net"
```

Where `<JIRA_ORG>` is your Jira organization identifier (for example, `mycompany` for `https://mycompany.atlassian.net`).

### Multi-JIRA server configuration <a href="#multi-jira-server-configuration" id="multi-jira-server-configuration"></a>

Qodo supports connecting to multiple JIRA servers using different authentication methods.

#### **Email/token (basic auth)**

Configure multiple servers using Email/Token authentication in your [ configuration file](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/configuration-file).

**Example configuration:**

```
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

#### **PAT auth**

Configure multiple servers using Personal Access Token authentication in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/configuration-file).

**Example Configuration:**

```
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

**Mixed authentication (E\email/token + PAT):**

```
[jira]
jira_servers = ["https://company.atlassian.net", "https://server.jira.com"]
jira_api_token = ["cloud_api_token", "server_pat_token"]
jira_api_email = ["user@company.com", ""]  # Empty for PAT
```

#### Jira Cloud app

For Jira Cloud instances using app authentication:

1. Install the Qodo app on each Jira Cloud instance you want to connect.
2. In your configuration file, set the default server for ticket ID resolution:

```
[jira]
jira_base_url = "https://primary-team.atlassian.net"
```

Full URLs (for example, `https://other-team.atlassian.net/browse/TASK-456`) automatically resolve to the correct connected Jira instance.

[<br>](https://docs.qodo.ai/qodo-documentation/qodo-merge/integrations/ticketing-integrations/linear)
