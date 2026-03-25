# Source: https://docs.anyscale.com/auth/service-accounts.md

# Anyscale service accounts

[View Markdown](/auth/service-accounts.md)

# Anyscale service accounts

Anyscale service accounts are non-user identities managed by organization owners. Anyscale recommends using service accounts for authenticating production integrations and other tools that need to interact with the Anyscale CLI or SDK.

You provide a unique name for your service account during creation. Anyscale creates an email identifier for your service account using the following format:

```
<service-account-name>@org-<organization-id>.serviceaccount.com
```

You use service accounts by creating one or more API keys for the service account and configuring them using the `ANYSCALE_CLI_TOKEN` environment variable. See [Manage API keys](/auth/api-keys.md).

important

You must be an organization owner to create, delete, or manage service accounts and related API keys.

Some service account operations require the Anyscale console, while others require the Anyscale CLI. See [Service Account API Reference](/reference/service-account.md).

## Create a service account[​](#create-a-service-account "Direct link to Create a service account")

Use the following CLI command to create a service account:

```
anyscale service-account create --name <name>
```

## List service accounts[​](#list-service-accounts "Direct link to List service accounts")

Use the following CLI command to list all service accounts in your Anyscale organization:

```
anyscale service-account list
```

You can also view service accounts for your organization in the Anyscale console. See [Manage service account API keys](#manage).

## Delete a service account[​](#delete-a-service-account "Direct link to Delete a service account")

Use the following CLI command to delete a service account:

```
anyscale service-account delete --name <name>
```

## Manage service account API keys[​](#manage "Direct link to Manage service account API keys")

You create and revoke API keys for service accounts using the Anyscale console.

Complete the following steps to list all service accounts in your organization and manage API keys:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click the user icon.
3. Click **Organization settings**.
4. Click **Service accounts**.

All service accounts for your Anyscale organization display.

### Create a service account API key[​](#create-a-service-account-api-key "Direct link to Create a service account API key")

Click **+ Create API key** to create a new service account API key.

The API key displays, along with optional commands to configure the key as an environment variable through your local terminal.

note

Record the last six digits of the API key to identify the unique key when revoking individual keys. See [View and revoke API keys](/auth/api-keys.md#revoke).

Service account API keys don't expire.

### Delete a service account API key[​](#revoke "Direct link to Delete a service account API key")

Click **Revoke all keys** to revoke all API keys for a service account.

To revoke individual keys for a service account, you can filter by the service account email and identify desired keys by the last six digits. See [View and revoke API keys](/auth/api-keys.md#revoke).
