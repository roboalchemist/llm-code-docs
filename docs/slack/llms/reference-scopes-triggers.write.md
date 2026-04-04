Source: https://docs.slack.dev/reference/scopes/triggers.write

# triggers:write scope

Create new Platform triggers

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

## Compatible API methods

[`workflows.triggers.permissions.add`](/reference/methods/workflows.triggers.permissions.add)

[`workflows.triggers.permissions.remove`](/reference/methods/workflows.triggers.permissions.remove)

[`workflows.triggers.permissions.set`](/reference/methods/workflows.triggers.permissions.set)

## Usage info {#usage-info}

Triggers can be added to your [workflows](/workflows) either via the CLI or at runtime.

Triggers created via the CLI use the CLI token. New tokens have the `triggers:write` scope. Old tokens will fail with instructions to log out and log back in. The following sections describe how to create triggers using the CLI:

* [Create a link trigger with the CLI](/tools/deno-slack-sdk/guides/creating-link-triggers#create-trigger)
* [Create an event trigger with the CLI](/tools/deno-slack-sdk/guides/creating-event-triggers#create-trigger)
* [Create a scheduled trigger with the CLI](/tools/deno-slack-sdk/guides/creating-scheduled-triggers#create-trigger)
* [Create a webhook trigger with the CLI](/tools/deno-slack-sdk/guides/creating-webhook-triggers#create-trigger)

Triggers created at runtime by [custom functions](/tools/deno-slack-sdk/guides/creating-custom-functions) use your app’s bot token. In this case, your app must have the `triggers:write` scope defined within your [app's manifest](/tools/deno-slack-sdk/guides/using-the-app-manifest) in order to use a trigger at runtime.
