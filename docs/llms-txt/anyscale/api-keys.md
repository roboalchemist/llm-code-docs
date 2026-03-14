# Source: https://docs.anyscale.com/auth/api-keys.md

# Manage API keys

[View Markdown](/auth/api-keys.md)

# Manage API keys

This page provides an overview of creating and managing API keys on Anyscale.

## API key generation patterns[​](#api-key-generation-patterns "Direct link to API key generation patterns")

All users can generate a user API key using the Anyscale CLI or the Anyscale console. Organization admins can generate API keys for service accounts.

The following table provides a brief description of these patterns with recommended use cases:

| API key generation pattern                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Login with Anyscale CLI                           | Anyscale recommends using the Anyscale CLI `anyscale login` command to authenticate your local machine for interactive development with the CLI or SDK.This pattern stores an API key in the location `~/.anyscale/credentials.json` of your machine. User API keys generated in this way expire after 7 days.                                                                                                                     |
| Generate a user API key with the Anyscale console | You can generate an API key for your user account and configure the environment variable `ANYSCALE_CLI_TOKEN` to authenticate to Anyscale with your user credentials.Use this pattern when developing and testing integrated systems and services. Anyscale doesn't recommend using user API keys in production systems.                                                                                                           |
| Service account API keys                          | Organization owners can create service accounts and then create API keys for a service account. You can create service account API keys in the Anyscale console. Assign the API key to the `ANYSCALE_CLI_TOKEN` in your configured environment.Anyscale recommends using service account API keys for all production integrations, such as CI/CD and scheduling tools. See [Anyscale service accounts](/auth/service-accounts.md). |

note

If you have an `ANYSCALE_CLI_TOKEN` variable defined in your environment, this takes precedence over credentials stored in `~/.anyscale/credentials.json`.

Anyscale workspaces configure an `ANYSCALE_CLI_TOKEN` automatically, allowing you to use the CLI and SDK from your workspace.

## Create a named user API key[​](#create "Direct link to Create a named user API key")

All users can create user API keys in the Anyscale console. User API keys have the following requirements:

* API key names must be unique for each user.

  <!-- -->

  * You can reuse a key name if you revoke the previous version or the key expires.
  * Multiple users can create API keys with the same name.
  * If you don't specify a name when creating an API key, Anyscale generates a unique hash.

* You must set an expiration date for your API key. The maximum lifetime for a user API key is 30 days.

important

Legacy user API keys didn't require an expiration date. Anyscale recommends revoking legacy API keys to enforce expiration.

Complete the following steps to create a user API key in the Anyscale console:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click the user icon.
3. Click **API keys**.
4. Click **+ Create**.
5. (Optional) Enter a name for the API key in the **Name** field.
6. (Optional) Change the expiration date.
   <!-- -->
   * The expiration date is 30 days by default. This is the maximum expiration date.
7. Click **Create a secret key**.

The API key displays, along with optional commands to configure the key as an environment variable through your local terminal.

note

Service accounts use a different flow for API key creation. See [Manage service account API keys](/auth/service-accounts.md#manage).

## View and revoke API keys[​](#revoke "Direct link to View and revoke API keys")

You can use the Anyscale console to view and revoke API keys. The following table describes permissions for each role:

| Organization role | Permission                                                   |
| ----------------- | ------------------------------------------------------------ |
| Owner             | View and revoke API keys for all users and service accounts. |
| Collaborator      | View and revoke API keys created by the user.                |

You can search for a user API key by name. Organization owners can filter results by user or service account email address.

To revoke an API token:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click the user icon.
3. Click **API keys**.
4. Locate the API key you need to revoke.
5. Click the box to the left of the **Key name**.
   <!-- -->
   * You can select multiple API keys, or click the box in the header to select all key entries on a page.
6. Click **Revoke**. A confirmation dialog appears.
7. Click **Revoke** to confirm.

note

You can display a maximum of 50 keys per page, meaning you can revoke 50 keys at once when selecting all.

If you need to fully remove all keys for a user quickly, an organization owner can remove the user account from the organization. You can't remove yourself from an organization. See [Delete users](/administration/organization/user-management.md#delete).

The Anyscale console provides a separate page to revoke all keys for a service account. See [Manage service account API keys](/auth/service-accounts.md#manage).
