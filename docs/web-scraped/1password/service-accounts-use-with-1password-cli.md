# Source: https://developer.1password.com/docs/service-accounts/use-with-1password-cli

On this page

# Use service accounts with 1Password CLI

You can use 1Password Service Accounts with 1Password CLI to manage vaults and items. See [supported commands](#supported-commands).

## Requirements[â€‹](#requirements "Direct link to Requirements") 

Before you use service accounts with 1Password CLI, you need to:

- [Sign up for 1Password.](https://1password.com/pricing/password-manager)
- Install [1Password CLI](/docs/cli/get-started/).\
  [Service Accounts require 1Password CLI version 2.18.0 or later.]
- [Create a service account.](/docs/service-accounts/get-started#create-a-service-account)

## Get started[â€‹](#get-started "Direct link to Get started") 

To use a service account with 1Password CLI:

1.  Set the `OP_SERVICE_ACCOUNT_TOKEN` environment variable to the service account token:

    ::::::::::::::::::: 
    - bash, sh, zsh
    - fish
    - Powershell

    :::::::::::::::::: margin-top--md
    ::::::: 
    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::
    :::::::

    ::::::: 
    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::
    :::::::

    ::::::: 
    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::
    :::::::
    ::::::::::::::::::
    :::::::::::::::::::

2.  Run the following command to make sure the service account is configured:

    ::::::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::

    See result\...

    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: actions_KOEz
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    :::::::::

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]caution

If you have 1Password CLI configured to work with [1Password Connect](/docs/connect/), the `OP_CONNECT_HOST` and `OP_CONNECT_TOKEN` environment variables take precedence over `OP_SERVICE_ACCOUNT_TOKEN`.

Clear the Connect environment variables to configure a service account instead.

### Supported commands[â€‹](#supported-commands "Direct link to Supported commands") 

You can now run supported 1Password CLI commands authenticated as the service account:

- [`op read`](/docs/cli/reference/commands/read/)
- [`op inject`](/docs/cli/reference/commands/inject/)
- [`op service-account ratelimit`](/docs/cli/reference/management-commands/service-account#service-account-ratelimit)

- [`op run`](/docs/cli/reference/commands/run/)
- [`op vault create`](/docs/cli/reference/management-commands/vault#vault-create)

To use the following commands, you must specify a vault with the `--vault` flag if the service account has access to more than one vault:

- [`op item`](/docs/cli/reference/management-commands/item/)

- [`op document`](/docs/cli/reference/management-commands/document/)

The following commands are only supported for vaults created by the service account:

- [`op vault delete`](/docs/cli/reference/management-commands/vault#vault-delete)
- [`op vault group grant`](/docs/cli/reference/management-commands/vault#vault-group-grant)
- [`op vault user grant`](/docs/cli/reference/management-commands/vault#vault-user-grant)

- [`op vault group revoke`](/docs/cli/reference/management-commands/vault#vault-group-revoke)
- [`op vault user revoke`](/docs/cli/reference/management-commands/vault#vault-user-revoke)

Unsupported commands

When using a service account, the following commands aren\'t supported:

- [`op connect`](/docs/cli/reference/management-commands/connect)
- [`op group`](/docs/cli/reference/management-commands/group/)
- [`op user provision`](/docs/cli/reference/management-commands/user#user-provision)
- [`op user confirm`](/docs/cli/reference/management-commands/user#user-confirm)
- [`op user suspend`](/docs/cli/reference/management-commands/user#user-suspend)
- [`op user delete`](/docs/cli/reference/management-commands/user#user-delete)
- [`op user recovery`](/docs/cli/reference/management-commands/user#user-recovery)

- [`op events-api`](/docs/cli/reference/management-commands/events-api/)
- [`op vault edit`](/docs/cli/reference/management-commands/vault#vault-edit)

Although service accounts support some user, group, and vault management commands, we recommend against using them because a full provisioning workflow isn\'t supported:

- [`op user get`](/docs/cli/reference/management-commands/user#user-get)
- [`op user list`](/docs/cli/reference/management-commands/user#user-list)

- [`op group get`](/docs/cli/reference/management-commands/group#group-get)
- [`op group list`](/docs/cli/reference/management-commands/group#group-list)

### Commands that make multiple requests[â€‹](#commands-that-make-multiple-requests "Direct link to Commands that make multiple requests") 

Service accounts have [hourly and daily limits](/docs/service-accounts/rate-limits) on the total number of requests the service account can make.

You can sometimes reduce the number of requests made by passing a vault or item\'s [unique identifier (ID)](/docs/cli/reference#unique-identifiers-ids) instead of its name.

1Password CLI commands make one request unless otherwise noted. The following commands make more than one request:

  Command             Total requests                                      Notes
  ------------------- --------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------
  `op item list`      1 + 1 per vault the service account has access to   To limit total requests to 3, list items in a specific vault using the `--vault` flag. Pass the vault\'s ID to further limit requests to 2.
  `op item get`       3 reads                                             To reduce to 1 request, pass the item and vault IDs.
  `op item create`    1 read and 1 write                                  To reduce to 1 request, pass the vault ID.
  `op item delete`    5 reads and 1 write                                 To reduce the read requests by 1, pass the vault ID.
  `op item edit`      5 reads and 1 write                                 To reduce the read requests by 1, pass the vault ID.
  `op read`           3 reads                                             To reduce to 1 request, pass the item and vault IDs.
  `op vault delete`   2 reads + 1 write                                   To reduce the read requests by 1, pass the vault ID.
  `op vault edit`     up to 3 writes                                      The number of requests may vary depending on how many changes are made with a single command.
  `op vault get`      2 reads                                             To reduce the read requests by 1, pass the vault ID.