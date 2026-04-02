Source: https://docs.slack.dev/reference/scopes/datastore.write

# datastore:write scope

Write data to Slack App Datastore

## Facts

## Supported token types

[`Bot`](/authentication/tokens#bot)

[`Legacy Bot`](/authentication/tokens#legacy-bot)

## Compatible API methods

[`apps.datastore.bulkDelete`](/reference/methods/apps.datastore.bulkdelete)

[`apps.datastore.bulkPut`](/reference/methods/apps.datastore.bulkput)

[`apps.datastore.delete`](/reference/methods/apps.datastore.delete)

[`apps.datastore.put`](/reference/methods/apps.datastore.put)

[`apps.datastore.update`](/reference/methods/apps.datastore.update)

## Usage info {#usage-info}

To initialize a datastore for use with your app:

1. Add it to the `datastores` property in your app's manifest.
2. Add the `datastore:read` and `datastore:write` permission scopes to the `botScopes` property in your app's manifest.

Refer to [Adding the datastore to your app's manifest](/tools/deno-slack-sdk/guides/using-datastores#manifest) for more information.
