# Source: https://flatfile.com/docs/core-concepts/environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Environments

> Use Environments for testing and authentication

Environments are isolated entities and are intended to be a safe place to create and test different configurations. Environments serve as self-contained, secure domains where diverse configurations can be created and tested. By default, a development and a production environment are set up.

| isProd  | Name        | Description                                                                                  |
| ------- | ----------- | -------------------------------------------------------------------------------------------- |
| *false* | development | Use this default environment, and it's associated test API keys, as you build with Flatfile. |
| *true*  | production  | When you're ready to launch, create a new environment and swap out your keys.                |

The development environment does not count towards your paid credits.

## Listeners

[Listeners](/core-concepts/listeners) are functions you write that respond to Events by executing custom code. They enable all the powerful functionality in your Flatfile implementation: data transformations, validations, integrations, and workflows. Each Listener - whether run locally or deployed as an [Agent](/core-concepts/listeners#agents) – connects to a specific [Environment](/core-concepts/environments) using that Environment's ID and API key as environment variables. To switch between different Environments (or promote a development Environment to production), you simply update your environment variables with the corresponding Environment ID and API key.

By default, Listeners respond to Events from all [Apps](/core-concepts/apps) within an [Environment](/core-concepts/environments). You can use [Namespaces](/guides/namespaces-and-filters#namespaces) to partition your Listeners into isolated functions that only respond to Events from specific Apps.

## Creating an Environment

Your `publishableKey` and `secretKey` are specific to an environment therefore to create a new Environment, you'll have to use a personal access token.

1. Open Settings
2. Click to Personal Tokens
3. You can use the key pair in there to create an access token like:

```bash  theme={null}
curl -X POST https://platform.flatfile.com/v1/auth -H 'Content-Type: application/json' -d '{"clientId":"1234-1234", "secret":"1234-1234"}'
```

4. The response will include an `accessToken`. You can present that as your **Bearer `token`** in place of the `secretKey`.

[Or click here to create an environment in the dashboard](https://platform.flatfile.com/dashboard)

## Guest Authentication

Environments support two types of guest authentication:

1. `magic_link`: This method dispatches an email to your guests, which includes a magic link to facilitate login.
2. `shared_link`: This method transforms the Space URL into a public one, typically used in conjunction with embedded Flatfile.

### Additional Info

Should the `guestAuthentication` be left unspecified, both `magic_link` and `shared_link` types are enabled by default.

It's important to note that `guestAuthentication` settings can be applied at both Environment and Space levels. However, in case of any conflicting settings, the authentication type set at the Space level will take precedence over the Environment level setting. This flexibility enables customization based on specific needs, ensuring the right balance of accessibility and security.

## Secret and publishable keys

All Accounts have two key types for each environment. Learn when to use each type of key:

| Type            | Id                    | Description                                                                                                             |
| --------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Secret key      | sk\_23ghsyuyshs7dcrty | **On the server-side:** Store this securely in your server-side code. Don't expose this key in an application.          |
| Publishable key | pk\_23ghsyuyshs7dcert | **On the client-side:** Can be publicly-accessible in your application's client-side code. Use when embedding Flatfile. |

The publishable key only has permissions to create a Space.
