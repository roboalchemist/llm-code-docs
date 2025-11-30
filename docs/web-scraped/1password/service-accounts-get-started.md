# Source: https://developer.1password.com/docs/service-accounts/get-started

On this page

# Get started with 1Password Service Accounts

With 1Password Service Accounts, you can build tools to automate secrets management in your applications and infrastructure without deploying additional services.

Service accounts can:

- Create, edit, delete, and share items.
- Create vaults.
- Delete vaults.\
  [A service account can only delete a vault it created. See [service account security](/docs/service-accounts/security/)].
- Retrieve information about users and groups.

Each service account has a [service account token](/docs/service-accounts/security#service-accounts-and-token-generation) that you can provide as an environment variable for authentication. You can choose which vaults the service account can access and its permissions in each vault.

# An error occurred. 

Unable to execute JavaScript.

**Limitations**

Service accounts have the following limitations:

- Service accounts have [rate limits and request quotes](/docs/service-accounts/rate-limits/).
- You can\'t grant a service account access to your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault, or your default [Shared](https://support.1password.com/1password-glossary#shared-vault) vault.
- Service accounts only work with 1Password CLI version 2.18.0 or later. See [Use service accounts with 1Password CLI](/docs/service-accounts/use-with-1password-cli/).
- You can\'t use service accounts with the [Kubernetes Operator](/docs/k8s/operator/) (only the [Kubernetes Secrets Injector](/docs/k8s/injector/)).

## Requirements[â€‹](#requirements "Direct link to Requirements") 

Before you can create and use service accounts, you\'ll need to:

- [Sign up for 1Password.](https://1password.com/pricing/password-manager)
- Have adequate account permissions to create service accounts.

If you don\'t see the option to create service accounts, ask your administrator to [give you access to create and manage service accounts](/docs/service-accounts/manage-service-accounts#manage-who-can-create-service-accounts).

## Create a service account[â€‹](#create-a-service-account "Direct link to Create a service account") 

You can create a service account on 1Password.com or with [1Password CLI](/docs/cli/).

Service account permissions and vault access are immutable. If you want to grant a service account access to additional vaults, change the permissions it has in the vaults it can access, or change its ability to create new vaults, you\'ll need to create a new service account with the appropriate permissions and access.

- 1Password.com
- 1Password CLI

To create a service account on 1Password.com:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Open the [service account creation wizard](https://start.1password.com/developer-tools/infrastructure-secrets/serviceaccount/).\
    [Or navigate to **Developer** \> **Directory**, select **Other** under Infrastructure Secrets Management, then select **Create a Service Account**.]
3.  Follow the onscreen instructions:
    1.  Choose a name for the service account.
    2.  Choose whether the service account can create vaults.
    3.  Choose the vaults the service account can access.\
        [You can\'t grant a service account access to your built-in Personal, Private, or Employee vault, or your default Shared vault.]
    4.  Select the settings icon next to each vault to choose the permissions the service account has in the vault. This can\'t be changed later.
    5.  Select **Create Account** to create the service account.
    6.  Select **Save in 1Password** to save the service account token in your 1Password account. In the next window, enter a name for the item and choose the vault where you want to save it.

    ::::: 
    ::: admonitionHeading_Qygg
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTUuMDUuMzFjLjgxIDIuMTcuNDEgMy4zOC0uNTIgNC4zMUMzLjU1IDUuNjcgMS45OCA2LjQ1LjkgNy45OGMtMS40NSAyLjA1LTEuNyA2LjUzIDMuNTMgNy43LTIuMi0xLjE2LTIuNjctNC41Mi0uMy02LjYxLS42MSAyLjAzLjUzIDMuMzMgMS45NCAyLjg2IDEuMzktLjQ3IDIuMy41MyAyLjI3IDEuNjctLjAyLjc4LS4zMSAxLjQ0LTEuMTMgMS44MSAzLjQyLS41OSA0Ljc4LTMuNDIgNC43OC01LjU2IDAtMi44NC0yLjUzLTMuMjItMS4yNS01LjYxLTEuNTIuMTMtMi4wMyAxLjEzLTEuODkgMi43NS4wOSAxLjA4LTEuMDIgMS44LTEuODYgMS4zMy0uNjctLjQxLS42Ni0xLjE5LS4wNi0xLjc4QzguMTggNS4zMSA4LjY4IDIuNDUgNS4wNS4zMkw1LjAzLjNsLjAyLjAxeiIgLz48L3N2Zz4=)]danger
    :::

    ::: admonitionContent_uHKH
    The service account creation wizard only shows the service account token once. **Save the token in 1Password** immediately to avoid losing it. Treat this token like a password, and don\'t store it in plaintext.
    :::
    :::::

You can find your new service account under \"Service accounts\" on the [**Developer**](https://start.1password.com/developer-tools/active) page.

To create a service account with 1Password CLI:

1.  Make sure you have the latest version of [1Password CLI](/docs/cli/get-started/) on your machine.

2.  Create a new service account using the [`op service-account create` command](/docs/cli/reference/management-commands/service-account#service-account-create):

    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::

    Available permissions: `read_items`, `write_items` (requires `read_items`), `share_items` (requires `read_items`)

    Include the `--can-create-vaults` flag to allow the service account to create new vaults.

    If the service account or vault name contains one or more spaces, enclose the name in quotation marks (for example, â€œMy Service Accountâ€?). You don\'t need to enclose strings in quotation marks if they don\'t contain spaces (for example, myServerName).

    Service accounts can\'t be modified after they\'re created. If you need to make changes, revoke the service account and create a new one.

3.  Save the service account token in your 1Password account.

4.  If you want to start using the service account with 1Password CLI, [export the token to the `OP_SERVICE_ACCOUNT_TOKEN` environment variable](/docs/service-accounts/use-with-1password-cli#get-started).

For example, to create a service account named `My Service Account` that has read and write permissions in a vault named `Production`, can create new vaults, and expires in 24 hours:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTUuMDUuMzFjLjgxIDIuMTcuNDEgMy4zOC0uNTIgNC4zMUMzLjU1IDUuNjcgMS45OCA2LjQ1LjkgNy45OGMtMS40NSAyLjA1LTEuNyA2LjUzIDMuNTMgNy43LTIuMi0xLjE2LTIuNjctNC41Mi0uMy02LjYxLS42MSAyLjAzLjUzIDMuMzMgMS45NCAyLjg2IDEuMzktLjQ3IDIuMy41MyAyLjI3IDEuNjctLjAyLjc4LS4zMSAxLjQ0LTEuMTMgMS44MSAzLjQyLS41OSA0Ljc4LTMuNDIgNC43OC01LjU2IDAtMi44NC0yLjUzLTMuMjItMS4yNS01LjYxLTEuNTIuMTMtMi4wMyAxLjEzLTEuODkgMi43NS4wOSAxLjA4LTEuMDIgMS44LTEuODYgMS4zMy0uNjctLjQxLS42Ni0xLjE5LS4wNi0xLjc4QzguMTggNS4zMSA4LjY4IDIuNDUgNS4wNS4zMkw1LjAzLjNsLjAyLjAxeiIgLz48L3N2Zz4=)]danger

1Password CLI only returns the service account token once. **Save the token in 1Password** immediately to avoid losing it. Treat this token like a password, and don\'t store it in plaintext.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]caution

If your [sign-in address](https://support.1password.com/1password-glossary#sign-in-address) changes, you\'ll need to [rotate your service account tokens](/docs/service-accounts/manage-service-accounts#rotate-token).

## Next steps[â€‹](#next-steps "Direct link to Next steps") 

Explore the following to learn about how you can use service accounts.

- [Use a service account with 1Password CLI.](/docs/service-accounts/use-with-1password-cli/)
- [Manage a service account.](/docs/service-accounts/manage-service-accounts/)
- [Integrate a service account with a CI/CD pipeline.](/docs/ci-cd/)
- [Integrate a service account with Kubernetes.](/docs/k8s/integrations/)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]Need help?

[Join our Developer Slack workspace](https://developer.1password.com/joinslack) to ask questions and provide feedback.