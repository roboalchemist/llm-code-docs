Source: https://docs.slack.dev/reference/scopes/triggers.read

# triggers:read scope

Read new Platform triggers

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

## Compatible API methods

[`workflows.triggers.permissions.list`](/reference/methods/workflows.triggers.permissions.list)

## Usage info {#usage-info}

Triggers can be added to your [workflows](/workflows) either via the CLI or at runtime.

Triggers created at runtime by [custom functions](/tools/deno-slack-sdk/guides/creating-custom-functions) use your app’s bot token. Your app must have the `triggers:read` scope defined within your [app's manifest](/tools/deno-slack-sdk/guides/using-the-app-manifest).
