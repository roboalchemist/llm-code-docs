# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/controllers/standardsalesforceclientservice.md

# StandardSalesforceClientService

## Description

Provides connection service to Salesforce APIs

## Tags

preview, salesforce

## Properties

In the list below required Properties are shown with an asterisk (\*).
Other properties are considered optional. The table also indicates any default values, and whether a property supports the NiFi Expression Language.

| Display Name | API Name | Default Value | Allowable Values | Description |
| --- | --- | --- | --- | --- |
| API Version \* | API Version | 63.0 |  | The version number of the Salesforce REST API appended to the URL after the services/data path. See Salesforce documentation for supported versions. |
| OAuth2 Access Token Provider \* | OAuth2 Access Token Provider |  |  | Service providing OAuth2 Access Tokens for authenticating using the HTTP Authorization Header |
| Salesforce Instance \* | Salesforce Instance |  |  | The hostname of the Salesforce instance including the domain such as MyDomainName.my.salesforce.com |
| Web Client Service \* | Web Client Service |  |  | The Web Client Service to use for communicating with Salesforce |

## State management

This component does not store state.

## Restricted

This component is not restricted.

## System Resource Considerations

This component does not specify system resource considerations.
