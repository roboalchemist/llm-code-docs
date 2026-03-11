# Source: https://docs.anyscale.com/auth.md

# Authentication and authorization on Anyscale

[View Markdown](/auth.md)

# Authentication and authorization on Anyscale

This page describes user authentication and authorization on the Anyscale platform.

Only authorized and authenticated principals can interact with the Anyscale platform.

## Authorization on Anyscale[​](#authorization-on-anyscale "Direct link to Authorization on Anyscale")

*Authorization* refers to the permissions granted to a user or service account. See [Roles and permissions](/administration/organization/permissions.md).

A *principal* is a unique identity in your organization. You grant privileges to principals to control their authorization.

The following table describes the principals you can use to authenticate to Anyscale:

| Principal       | Description                                                                                                                                                                                                                                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User            | A user account in your Anyscale organization. Organization owners can add new users to an Anyscale organization. You must be an authorized user to use the Anyscale console or authenticate using the `anyscale login` CLI command. See [Manage users](/administration/organization/user-management.md). |
| Service account | A non-interactive entity managed by organization owners. Use service accounts to manage API keys for production integrations. See [Anyscale service accounts](/auth/service-accounts.md).                                                                                                                |

## Authentication on Anyscale[​](#authentication-on-anyscale "Direct link to Authentication on Anyscale")

*Authentication* describes the process of proving your identity. Anyscale supports the following authentication patterns:

* **Anyscale console sign in**: Log in to the Anyscale console.
* **API keys**: Generate and configure an API key for a user or service account.

### Anyscale console authentication[​](#anyscale-console-authentication "Direct link to Anyscale console authentication")

You sign in to Anyscale to create a user session. Anyscale manages user sessions with cookies. When you're using the Anyscale console, authentication is automatic as long as you have a valid user session. When your session expires, Anyscale prompts you to sign in again.

Anyscale supports single sign-on (SSO) with SAML 2.0 providers. Anyscale recommends always using SSO to manage user authentication to Anyscale. See [Configure SSO for your Anyscale organization](/administration/organization/configure-sso.md).

### Authenticate with an API key[​](#authenticate-with-an-api-key "Direct link to Authenticate with an API key")

Anyscale uses API keys to authenticate commands to the platform API. Ray and Anyscale clients send this key in HTTPS request headers to access Anyscale API calls.

You must generate and configure API keys to interact with Anyscale resources using tools other than the Anyscale console, such as the following:

* Anyscale CLI
* Anyscale SDK
* Integrated systems

See [Manage API keys](/auth/api-keys.md).

When you use an API key to authenticate, the authenticated client or system acts as the principal, meaning they have the same authorization as the user or service account that generated the API key. Anyscale attributes all actions to the principal associated with the API key used to authenticate a client. Users should never share their API keys, and organization owners should protect service account API keys.

important

Anyscale recommends using user API keys for all interactive development and commands.

Use service account API keys for production integrations, such as CI/CD and scheduling tools.

## Authenticate the Anyscale CLI[​](#cli-auth "Direct link to Authenticate the Anyscale CLI")

Anyscale provides a CLI command to easily manage authentication from your personal machine.

1. Run the following command with the Anyscale CLI to authenticate your machine to your Anyscale organization:

   ```
   anyscale login
   ```

2. Your terminal prompts you to visit a URL. Open the URL in your browser.

3. If you don't have an active user session, a prompt to sign in to Anyscale displays.

4. Once you have a valid user session, a prompt displays with the text **Log in to Anyscale command line interface**. This prompt includes the requesting IP address.

5. Click **Approve** to authenticate.

This command stores a user API key in a file at the location `~/.anyscale/credentials.json`. The Anyscale CLI and SDK automatically use this key to interact with your Anyscale organization. The key expires after seven days.

note

You can also generate an API key in the Anyscale console and store it as an environment variable. See [Create a named user API key](/auth/api-keys.md#create).
