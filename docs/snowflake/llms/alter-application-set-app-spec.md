# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-set-app-spec.md

# ALTER APPLICATION SET SPECIFICATION

Creates or updates an [app specification](../../developer-guide/native-apps/requesting-app-specs.md) for a Snowflake Native App.

> **Note:**
>
> This command can only be used by a Snowflake Native App.

See also:
:   [ALTER APPLICATION](alter-application.md),
    [ALTER APPLICATION … { APPROVE | DECLINE} SPECIFICATION](alter-application-sequence-number.md), [ALTER APPLICATION DROP SPECIFICATION](alter-application-drop-app-spec.md)

## Syntax

### External access integration

```sqlsyntax
ALTER APPLICATION SET SPECIFICATION <app_spec_name>
  TYPE = EXTERNAL_ACCESS
  LABEL = '<label>'
  DESCRIPTION = '<description>'
  { HOST_PORTS | PRIVATE_HOST_PORTS } = ( '<value>' [, '<value>', ... ] )
```

### Security integration (CLIENT_CREDENTIALS)

```sqlsyntax
ALTER APPLICATION SET SPECIFICATION <app_spec_name>
    TYPE = SECURITY_INTEGRATION
    LABEL = '<string_literal>'
    DESCRIPTION = '<string_literal>'
    OAUTH_TYPE = 'CLIENT_CREDENTIALS'
    OAUTH_TOKEN_ENDPOINT = '<string_literal>'
    OAUTH_ALLOWED_SCOPES = ( '<scope>' [ , '<scope>' ... ] );
```

### Security integration (AUTHORIZATION_CODE)

```sqlsyntax
ALTER APPLICATION SET SPECIFICATION <app_spec_name>
  TYPE = SECURITY_INTEGRATION
  LABEL = '<string_literal>'
  DESCRIPTION = '<string_literal>'
  OAUTH_TYPE = 'AUTHORIZATION_CODE'
  OAUTH_TOKEN_ENDPOINT = '<string_literal>'
  [ OAUTH_AUTHORIZATION_ENDPOINT = '<string_literal>' ]
  [ OAUTH_ALLOWED_SCOPES = ( '<scope>' [ , '<scope>' ... ] ) ];
```

### Security integration (JWT_BEARER)

```sqlsyntax
ALTER APPLICATION SET SPECIFICATION <app_spec_name>
  TYPE = SECURITY_INTEGRATION
  LABEL = '<string_literal>'
  DESCRIPTION = '<string_literal>'
  OAUTH_TYPE = 'JWT_BEARER'
  OAUTH_TOKEN_ENDPOINT = '<string_literal>'
  [ OAUTH_AUTHORIZATION_ENDPOINT = '<string_literal>' ]
  [ OAUTH_ALLOWED_SCOPES = ( '<scope>' [ , '<scope>' ... ] ) ];
```

### Listing

```sqlsyntax
ALTER APPLICATION SET SPECIFICATION <app_spec_name>
  TYPE = LISTING
  LABEL = '<string_literal>'
  DESCRIPTION = '<string_literal>'
  TARGET_ACCOUNTS = '<account_list>'
  LISTING = <listing_name>
  [ AUTO_FULFILLMENT_REFRESH_SCHEDULE = '<schedule>' ]
```

### Inter-App Communication

```sqlsyntax
ALTER APPLICATION SET SPECIFICATION <app_spec_name>
  TYPE = CONNECTION
        LABEL = '<label>'
        DESCRIPTION = '<description>'
        SERVER_APPLICATION = <server_app>
        SERVER_APPLICATION_ROLES = ( <app_role1> [ , <app_role2> ... ] );
```

## General parameters

`app_spec_name`
:   Identifier for the [app specification](../../developer-guide/native-apps/requesting-app-specs.md).

`TYPE = {EXTERNAL_ACCESS | SECURITY_INTEGRATION | LISTING | CONNECTION}}`
:   Specifies the type of app specification. Supported values are:

    * [EXTERNAL_ACCESS](../../developer-guide/external-network-access/creating-using-external-network-access.md)
    * [SECURITY_INTEGRATION](create-security-integration-api-auth.md)
    * [LISTING](../../developer-guide/native-apps/requesting-app-specs-listing.md)
    * [CONNECTION](../../developer-guide/native-apps/inter-app-communication.md)

    > **Important:**
    >
    > The type of an app specification cannot be changed once it has been created. Attempting to
    > alter the type will result in an error.

`LABEL = 'label'`
:   Specifies a label for the app specification. This label is the name of the
    app specification that is visible to the consumer. Each app specification must
    have a unique label.

    > **Note:**
    >
    > Changing only the label will not trigger a new approval request. To require consumer
    > approval, you must also change the app specification definition (such as HOST_PORTS,
    > OAUTH_TOKEN_ENDPOINT, or TARGET_ACCOUNTS).

`DESCRIPTION = 'description'`
:   Specifies a description of the app specification. Snowflake recommends
    including information about the app specification type and why it is
    required by the app.

    > **Note:**
    >
    > Changing only the description will not trigger a new approval request. To require consumer
    > approval, you must also change the app specification definition (such as HOST_PORTS,
    > OAUTH_TOKEN_ENDPOINT, or TARGET_ACCOUNTS).

## External access integration parameters

`HOST_PORTS | PRIVATE_HOST_PORTS = ( 'value' [ , 'value', ... ] )`
:   Specifies a list of host ports or private host ports that the app can connect to.
    These ports are used by external access integrations.

## Security integration parameters - CLIENT_CREDENTIALS

`OAUTH_TYPE = 'CLIENT_CREDENTIALS'`
:   Specifies the type of security integration for external API Authentication. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_TOKEN_ENDPOINT = 'string_literal'`
:   Specifies the token endpoint used by the client to obtain an access token by presenting its authorization
    grant or refresh token. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_ALLOWED_SCOPES = ( 'scope' [  , 'scope' ... ]  )`
:   Specifies a comma-separated list of scopes, with single quotes surrounding each scope, to use when making
    a request from the OAuth by a role with USAGE on the integration during the OAuth client credentials
    flow. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_ACCESS_TOKEN_VALIDITY = integer`
:   Specifies the default lifetime of the OAuth access token (in seconds) issued by an OAuth server. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

## Security integration parameters - AUTHORIZATION_CODE

`OAUTH_TYPE = 'AUTHORIZATION_CODE'`
:   Specifies the type of security integration for external API Authentication. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_TOKEN_ENDPOINT = 'string_literal'`
:   Specifies the token endpoint used by the client to obtain an access token by presenting its authorization
    grant or refresh token. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_AUTHORIZATION_ENDPOINT = 'string_literal'`
:   Specifies the URL for authenticating to the external service. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_ACCESS_TOKEN_VALIDITY = integer`
:   Specifies the default lifetime of the OAuth access token (in seconds) issued by an OAuth server. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_REFRESH_TOKEN_VALIDITY = integer`
:   Specifies the default lifetime of the OAuth refresh token (in seconds) issued by an OAuth server. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

## Security integration parameters - JWT_BEARER

`OAUTH_TYPE = 'JWT_BEARER'`
:   Specifies the type of security integration for external API Authentication. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_TOKEN_ENDPOINT = 'string_literal'`
:   Specifies the token endpoint used by the client to obtain an access token by presenting its authorization
    grant or refresh token. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_AUTHORIZATION_ENDPOINT = 'string_literal'`
:   Specifies the URL for authenticating to the external service. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

`OAUTH_REFRESH_TOKEN_VALIDITY = integer`
:   Specifies the default lifetime of the OAuth refresh token (in seconds) issued by an OAuth server. See
    [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md) for more information.

## Listing parameters

`TARGET_ACCOUNTS = 'account_list'`
:   Specifies a single-quoted string of target accounts, separated by commas, with
    no spaces. Each account must be specified in the format
    `OrgName.AccountName`; for example:
    `'ProviderOrg.ProviderAccount,PartnerOrg.PartnerAccount'`. When the
    specification is approved, these accounts are added to the listing. When
    declined, all accounts are removed from the listing.

`LISTING = listing_name`
:   Specifies the identifier of the external listing created by the app. The listing must already exist
    and must have been created by the app with a share attached. After the listing is set in an app specification,
    the listing name cannot be changed.

`AUTO_FULFILLMENT_REFRESH_SCHEDULE = 'schedule'`
:   Optional. Specifies the refresh schedule for cross-region data sharing. This parameter is required
    when sharing data across regions. The value can be specified in two formats:

    * `num MINUTE`: Number of minutes, with a minimum of 10 minutes and
      a maximum of 11,520 minutes (eight days).
    * `USING CRON expression time_zone`: Cron expression with time zone
      for the refresh.

## Inter-app communication parameters

`SERVER_APPLICATION = server_app`
:   The name of the server application to be connected to. The following operations
    are not supported:

    * Updating this setting for an existing specification.
    * More than one specification targeting the same server application.

`SERVER_APPLICATION_ROLES = ( app_role1 [ , app_role2 ... ] )`
:   Specifies a comma-separated list of application roles in the server application
    to be granted to this application.

## Usage notes

* To use this command, providers must ensure that the manifest file of the app
  uses `manifest_version: 2`.

## Examples

Create an app specification for external access:

```sqlexample
ALTER APPLICATION SET SPECIFICATION eai_spec
  TYPE = EXTERNAL_ACCESS
  LABEL = 'External API Access'
  DESCRIPTION = 'Connect to external weather API'
  HOST_PORTS = ('api.weather.com:443', 'api.openweather.org:443');
```

Create an app specification for OAuth security integration:

```sqlexample
ALTER APPLICATION SET SPECIFICATION oauth_spec
  TYPE = SECURITY_INTEGRATION
  LABEL = 'OAuth Integration'
  DESCRIPTION = 'Connect to Microsoft Graph API'
  OAUTH_TYPE = 'CLIENT_CREDENTIALS'
  OAUTH_TOKEN_ENDPOINT = 'https://login.microsoftonline.com/YOUR_TENANT_ID/oauth2/v2.0/token'
  OAUTH_ALLOWED_SCOPES = ('https://graph.microsoft.com/.default');
```

Create an app specification for data sharing through a listing:

```sqlexample
ALTER APPLICATION SET SPECIFICATION shareback_spec
  TYPE = LISTING
  LABEL = 'Telemetry Data Sharing'
  DESCRIPTION = 'Share telemetry and usage data with provider'
  TARGET_ACCOUNTS = 'ProviderOrg.ProviderAccount,PartnerOrg.PartnerAccount'
  LISTING = telemetry_listing
  AUTO_FULFILLMENT_REFRESH_SCHEDULE = '720 MINUTE';
```
