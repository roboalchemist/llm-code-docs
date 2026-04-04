Source: https://docs.slack.dev/reference/scopes/datastore.read

# datastore:read scope

View and see data from Slack App Datastore

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

[`Legacy Bot`](/authentication/tokens#legacy-bot)

## Compatible API methods

[`apps.datastore.bulkGet`](/reference/methods/apps.datastore.bulkget)

[`apps.datastore.count`](/reference/methods/apps.datastore.count)

[`apps.datastore.get`](/reference/methods/apps.datastore.get)

[`apps.datastore.query`](/reference/methods/apps.datastore.query)

## Usage info {#usage-info}

To initialize a datastore for use with your app:

1. Add it to the `datastores` property in your app's manifest.
2. Add add the `datastore:read` and `datastore:write` permission scopes to the `botScopes` property in your app's manifest.

Refer to [Adding the datastore to your app's manifest](/tools/deno-slack-sdk/guides/using-datastores#manifest) for more information.
