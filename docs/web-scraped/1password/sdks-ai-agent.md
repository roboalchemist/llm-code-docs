# Source: https://developer.1password.com/docs/sdks/ai-agent

On this page

# Tutorial: Integrate 1Password SDKs with AI agents

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]Security notice

This article demonstrates how to use 1Password developer tools in conjunction with an agentic AI application. **It is not our recommended integration approach**. Exposing raw credentials directly to an AI model carries significant risks. Where possible, avoid passing secrets to the model. Instead, use short-lived, tightly scoped tokens, implement strong auditing practices, and minimize the modelâ€™s access to sensitive data.

For more insight into our security recommendations and philosophy, please refer to our blog post: [Securing the Agentic Future](https://blog.1password.com/where-mcp-fits-and-where-it-doesnt/).

In this tutorial, you\'ll learn a workflow for providing credentials stored in 1Password to an AI agent using 1Password SDKs.

We\'ll walk through the process using an example integration with [Anthropic Claude ](https://www.anthropic.com/claude) that automatically books a flight with your company credit card then submits an expense report in Ramp, all without hardcoding any secrets. By the end, you\'ll understand how to:

- Follow the principle of least privilege to make sure your AI agent only has the minimum access needed to perform your task.
- Create a 1Password Service Account with least privilege access to relevant items in your 1Password account.
- Create secret reference URIs that point to where your credentials are stored in 1Password, so you can avoid hardcoding your secrets in plaintext.
- Use the 1Password SDKs to fetch the secrets your AI agent needs at runtime.

With this workflow, your AI agent can access only the secrets in 1Password it needs to authenticate into services. And you can see what items the agent accesses by creating a [service account usage report](https://support.1password.com/reports#create-a-usage-report-for-a-team-member-service-account-or-vault).

## Prerequisites[â€‹](#prerequisites "Direct link to Prerequisites") 

1.  [1Password subscription](https://1password.com/pricing/password-manager).
2.  [1Password desktop app](https://1password.com/downloads/). (Optional)
3.  Basic knowledge of AI agents.
4.  Basic knowledge of Python.
5.  Familiarity with 1Password SDKs. To learn how to get started, see the [end-to-end setup tutorial](/docs/sdks/setup-tutorial).

## Part 1: Set up a 1Password Service Account scoped to a vault[â€‹](#part-1-set-up-a-1password-service-account-scoped-to-a-vault "Direct link to Part 1: Set up a 1Password Service Account scoped to a vault") 

In the first part of this tutorial, you\'ll learn how to use 1Password to follow the security [principle of least privilege](https://blog.1password.com/guiding-principles-how-least-privilege-leads-to-more-security/), which requires that a process only be given the minimum level of access needed to complete its task.

To do this, you\'ll create a vault in your 1Password account that only contains the secrets your AI agent needs. Then you\'ll create a service account that only has read access to the new vault, and can\'t access any other items in your account. When your agent authenticates to 1Password using the service account, it won\'t have any unnecessary access or permissions beyond the bare minimum.

### Step 1: Create a vault that only contains items required for the task[â€‹](#step-1-create-a-vault-that-only-contains-items-required-for-the-task "Direct link to Step 1: Create a vault that only contains items required for the task") 

First, create a vault that only contains the credentials you\'ll need to perform the task you want the AI agent to complete. For our example, we\'ll create a new vault `Tutorial` that contains our Navan and Ramp logins, and our travel credit card.

1.  Open and unlock the [1Password app](https://1password.com/downloads/).
2.  Select the plus button in the sidebar next to your account name.
3.  Enter `Tutorial` for the vault name, then select **Create**.
4.  [Move or copy](https://support.1password.com/move-copy-items/) the items you need for the task into the vault.

### Step 2: Create a service account scoped to the vault[â€‹](#step-2-create-a-service-account-scoped-to-the-vault "Direct link to Step 2: Create a service account scoped to the vault") 

[Service accounts](/docs/service-accounts) are a token-based authentication method that you can scope to specific vaults and permissions. For this tutorial, we\'ll create a service account that only has read access in the `Tutorial` vault.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

If you don\'t see the option to create service accounts, ask your administrator to [give you access to create and manage service accounts](/docs/service-accounts/manage-service-accounts#manage-who-can-create-service-accounts).

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Select [**Developer**](https://start.1password.com/developer-tools/directory) in the sidebar. Or, if you already have active applications and services, select **Directory** at the top of the Developer page.
3.  Under Access Tokens, select **Service Account**.
4.  Give your service account a name. For example, `AI Agent Workflow Service Account`, then select **Next**.
5.  On the next screen, you\'ll see a list of your 1Password vaults. Select the **Tutorial** vault you created in the previous step, then select the gear icon next to it. In the permissions dropdown, select **Read Items**.
6.  Select **Create Account**.
7.  On the next screen, select **Save in 1Password**, then save your newly-created service account token in the Tutorial vault.

## Part 2: Provide your credentials to the agent[â€‹](#part-2-provide-your-credentials-to-the-agent "Direct link to Part 2: Provide your credentials to the agent") 

In the second part of this tutorial, you\'ll learn how to build an AI agent integration that fetches your credentials from 1Password at runtime.

To do this, you\'ll use the `secrets.resolve()` method with secret reference URIs that point to where your credentials are stored in your 1Password account. When the agent runs, 1Password injects the actual secrets referenced by the URIs.

This setup makes sure that your agent can only work with the credentials you explicitly provide as secret references in your non-dynamic controller code. This creates a clear boundary between your 1Password account and the AI agent, and prevents the agent from crafting its own requests to 1Password or accessing other credentials.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]Before you proceed

Set up a project for your AI agent integration using 1Password SDKs. In the example below, we\'ve created an integration using the Python SDK. Learn how to [get started with 1Password SDKs](/docs/sdks/setup-tutorial).

### Step 1: Export your service account token[â€‹](#step-1-export-your-service-account-token "Direct link to Step 1: Export your service account token") 

Export the service account token you saved [in part one](#step-2-create-a-service-account-scoped-to-the-vault) to the `OP_SERVICE_ACCOUNT_TOKEN` environment variable.

- Bash, Zsh, sh
- fish
- PowerShell

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Step 2: Define your credentials[â€‹](#step-2-define-your-credentials "Direct link to Step 2: Define your credentials") 

Define the credentials your AI agent will need using the `secrets.resolve()` method from the 1Password SDK. You can use placeholder secret references for now â€" we\'ll replace them with real secret references in the next step.

In our example, we\'ve defined:

- Our Navan username and password.
- Our travel credit card number, expiration date, and CVC.
- Our Ramp username and password.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Step 3: Get secret references[â€‹](#step-3-get-secret-references "Direct link to Step 3: Get secret references") 

Get [secret reference URIs](/docs/cli/secret-reference-syntax) for your credentials, then paste them into your script in place of the placeholders from the previous step.

1.  Open and unlock the [1Password desktop app](https://1password.com/downloads/).
2.  Turn on the [integration with 1Password CLI](/docs/cli/app-integration).
3.  Open the Tutorial vault and select an item that contains a credential you want to reference in your script.
4.  Select the down arrow next to the field for the secret you want to reference, then select **Copy Secret Reference**.
5.  Paste the secret reference into your code in place of `op://vault/item/field`.

You can also create secret references using the [1Password for VS Code extension](/docs/vscode/).

Here\'s our example updated with secret references:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Step 4: Define your agent instructions[â€‹](#step-4-define-your-agent-instructions "Direct link to Step 4: Define your agent instructions") 

Now, provide the AI agent instructions for how to use the credentials you fetched in the previous step. In our example, we instruct the agent to book a flight using our company credit card, then file an expense report for reimbursement.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]caution

AI agents can make mistakes. Make sure to double check the results of your prompts.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Run the script, and the agent will load your secrets from 1Password and perform the defined tasks.

## Conclusion[â€‹](#conclusion "Direct link to Conclusion") 

In this tutorial, you learned how to provide an AI agent with access credentials to perform a specific task, without hardcoding any secrets or giving the agent unnecessary access permissions.

You can modify the provided example to work with other AI agents or language models, and extend it to support a wide range of tasks.

## Learn more[â€‹](#learn-more "Direct link to Learn more") 

- [Tutorial: Get started with 1Password SDKs](/docs/sdks/setup-tutorial)
- [Load secrets using 1Password SDKs](/docs/sdks/load-secrets)
- [Manage items using 1Password SDKs](/docs/sdks/manage-items)