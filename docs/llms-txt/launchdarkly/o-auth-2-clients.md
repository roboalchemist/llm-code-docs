# Source: https://launchdarkly.com/docs/api/o-auth-2-clients.md

The OAuth2 client API allows you to register a LaunchDarkly OAuth client for use in your own custom integrations. Registering a LaunchDarkly OAuth client allows you to use LaunchDarkly as an identity provider so that account members can log into your application with their LaunchDarkly account.

You can create and manage LaunchDarkly OAuth clients using the LaunchDarkly OAuth client API. This API acknowledges creation of your client with a response containing a one-time, unique `_clientSecret`. If you lose your client secret, you will have to register a new client. LaunchDarkly does not store client secrets in plain text.

Several of the endpoints in the OAuth2 client API require an OAuth client ID. The OAuth client ID is returned as part of the [Create a LaunchDarkly OAuth 2.0 client](https://launchdarkly.com/docs/api/o-auth-2-clients/create-o-auth-2-client) and [Get clients](https://launchdarkly.com/docs/api/o-auth-2-clients/get-o-auth-clients) responses. It is the `_clientId` field, or the `_clientId` field of each element in the `items` array.

You must have _Admin_ privileges or an access token created by a member with _Admin_ privileges in order to be able to use this feature.

Please note that `redirectUri`s must be absolute URIs that conform to the https URI scheme. If you wish to register a client with a different URI scheme, please contact LaunchDarkly Support.
