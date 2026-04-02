Source: https://docs.slack.dev/reference/scopes/authorizations.read

# authorizations:read scope

Grants permission to list authorizations associated with the Events API

## Facts

## Supported token types

[`App-level`](/authentication/tokens#app-level)

## Compatible API methods

[`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list)

## Usage info {#usage-info}

This scope may only be used with an [app-level token](/authentication/tokens#app). App-level tokens represent your app across an entire organization.

You can obtain an app-level token for your app by going to your [App Management page](https://api.slack.com/apps) and scrolling to the **App-Level Tokens** heading on the Basic Information page. Click `Generate Token` to get the token representing your app as a whole.

From there, request the [`authorizations:read`](/reference/scopes/authorizations.read) scope just like you would normally—either by going to the **OAuth & Permissions** section of your App Management page, or modifying your [OAuth flow](/authentication/installing-with-oauth) to request the scope with your fancy new app-level token.
