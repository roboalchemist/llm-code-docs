# Source: https://docs.airbyte.com/integrations/sources/xero-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-xero/latest/icon.svg)

# Xero Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [2.1.5](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-xero)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-xero)(last updated 14 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `6fd1e833-dd6e-45ec-a727-ab917c5be892`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

You can now choose your preferred xero authentication method. You can choose between `client_credentials` and `bearer_token` authentication methods.

For the bearer strategy, please visit the [pkce-flow documentation](https://developer.xero.com/documentation/guides/oauth2/pkce-flow) for more detailed information about how to get access token. For the client\_credentials strategy, please visit the [client-credentials-flow documentation](https://developer.xero.com/documentation/guides/oauth2/custom-connections) for more detailed information about how to set the authentication flow.

### Using postman to get access token[​](#using-postman-to-get-access-token "Direct link to Using postman to get access token")

* Move to Authorization tab of an empty http request and selected Oauth 2.0
* Set use token type as `access token`
* Set header prefix as `Bearer`
* Set grant type as `Authorization code`
* Check `Authorize using browser`
* Set Auth URL as `https://login.xero.com/identity/connect/authorize`
* Set Access token URL as `https://identity.xero.com/connect/token`
* Set Client ID, Client secret, Scope defined as your Xero settings
* Set state as any number Eg: `123`
* Set Client Authentication as `Send as Basic Auth Header` Click `Get New Access Token` for retrieving access token

Then authorize your source with the required information.

1. Go to set up `The Source` page.
2. Enter your Xero application's access token or Client ID and Client Secret.
3. Click `Reset saved source` button.

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

The authentication schema is now using `access_token` instead of Oauth 2.0. Visit the Xero documentation - <https://developer.xero.com/documentation/guides/oauth2/pkce-flow> for more detailed information about how to get access token. Optionally, you may get your access\_token via Postman:

* Move to Authorization tab of an empty http request and selected Oauth 2.0
* Set use token type as `access token`
* Set header prefix as `Bearer`
* Set grant type as `Authorization code`
* Check `Authorize using browser`
* Set Auth URL as `https://login.xero.com/identity/connect/authorize`
* Set Access token URL as `https://identity.xero.com/connect/token`
* Set Client ID, Client secret, Scope defined as your Xero settings
* Set state as any number Eg: `123`
* Set Client Authentication as `Send as Basic Auth Header` Click `Get New Access Token` for retrieving access token

Then authorize your source with `access_token`.

1. Go to set up `The Source` page.
2. Enter your Xero application's access token.
3. Click `Reset saved source` button.

As Xero API now only supports date-precision, instead of second precision filtering through If-Modified-Since header, reads are now streamlined to incremental through client side.
