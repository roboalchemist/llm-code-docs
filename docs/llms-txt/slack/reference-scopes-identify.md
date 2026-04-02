Source: https://docs.slack.dev/reference/scopes/identify

# identify scope

View information about a user's identity

## Facts

## Supported token types

[`User`](/authentication/tokens#user)

## Usage info {#usage-info}

This scope allows a token to identify itself and utilize the Web API.

For classic apps, it was issued to all user tokens. User tokens issued by apps that have migrated to the Slack app model will also continue to include this scope.

For Slack apps, the permissions this scope grants is inherent to the user token itself.

All tokens in the Slack Platform can identify themselves using the [`auth.test`](/reference/methods/auth.test) API method. In classic apps, this ability is made explicit with the `identify` scope. In Slack apps, the scope is implicit and unnamed unless as part of an app that has migrated from a classic app.
