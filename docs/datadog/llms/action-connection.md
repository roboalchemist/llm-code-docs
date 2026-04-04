# Source: https://docs.datadoghq.com/api/latest/action-connection.md

---
title: Action Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Action Connection
---

# Action Connection

Action connections extend your installed integrations and allow you to take action in your third-party systems (e.g. AWS, GitLab, and Statuspage) with Datadog's Workflow Automation and App Builder products.

Datadog's Integrations automatically provide authentication for Slack, Microsoft Teams, PagerDuty, Opsgenie, JIRA, GitHub, and Statuspage. You do not need additional connections in order to access these tools within Workflow Automation and App Builder.

We offer granular access control for editing and resolving connections.

## Get an existing Action Connection{% #get-an-existing-action-connection %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/actions/connections/{connection_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/actions/connections/{connection_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/actions/connections/{connection_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/actions/connections/{connection_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/actions/connections/{connection_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/actions/connections/{connection_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/actions/connections/{connection_id} |

### Overview

Get an existing Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key).

### Arguments

#### Path Parameters

| Name                            | Type   | Description                     |
| ------------------------------- | ------ | ------------------------------- |
| connection_id [*required*] | string | The ID of the action connection |

### Response

{% tab title="200" %}
Successfully get Action Connection
{% tab title="Model" %}
The response for found connection

| Parent field   | Field                                   | Type          | Description                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | --------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data                                    | object        | Data related to the connection.                                                                                                                                                                                                                                                                                                                                                    |
| data           | attributes [*required*]            | object        | The definition of `ActionConnectionAttributes` object.                                                                                                                                                                                                                                                                                                                             |
| attributes     | integration [*required*]           |  <oneOf> | The definition of `ActionConnectionIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| integration    | Option 1                                | object        | The definition of `AWSIntegration` object.                                                                                                                                                                                                                                                                                                                                         |
| Option 1       | credentials [*required*]           |  <oneOf> | The definition of `AWSCredentials` object.                                                                                                                                                                                                                                                                                                                                         |
| credentials    | Option 1                                | object        | The definition of `AWSAssumeRole` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | account_id [*required*]            | string        | AWS account the connection is created for                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | external_id                             | string        | External ID used to scope which connection can be used to assume the role                                                                                                                                                                                                                                                                                                          |
| Option 1       | principal_id                            | string        | AWS account that will assume the role                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | role [*required*]                  | string        | Role to assume                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`                                                                                                                                                                                                                                                                                                          |
| integration    | Option 2                                | object        | The definition of the `AnthropicIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 2       | credentials [*required*]           |  <oneOf> | The definition of the `AnthropicCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `AnthropicAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_token [*required*]             | string        | The `AnthropicAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 2       | type [*required*]                  | enum          | The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`                                                                                                                                                                                                                                                                                          |
| integration    | Option 3                                | object        | The definition of the `AsanaIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 3       | credentials [*required*]           |  <oneOf> | The definition of the `AsanaCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AsanaAccessToken` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | access_token [*required*]          | string        | The `AsanaAccessToken` `access_token`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]                  | enum          | The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`                                                                                                                                                                                                                                                                                           |
| Option 3       | type [*required*]                  | enum          | The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 4                                | object        | The definition of the `AzureIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 4       | credentials [*required*]           |  <oneOf> | The definition of the `AzureCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AzureTenant` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | app_client_id [*required*]         | string        | The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.                                                             |
| Option 1       | client_secret [*required*]         | string        | The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application's secrets page. You can navigate to your application via the Azure Directory.                                                                                             |
| Option 1       | custom_scopes                           | string        | If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.                                        |
| Option 1       | tenant_id [*required*]             | string        | The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.                                                                                                                                        |
| Option 1       | type [*required*]                  | enum          | The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`                                                                                                                                                                                                                                                                                                     |
| Option 4       | type [*required*]                  | enum          | The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 5                                | object        | The definition of the `CircleCIIntegration` object.                                                                                                                                                                                                                                                                                                                                |
| Option 5       | credentials [*required*]           |  <oneOf> | The definition of the `CircleCICredentials` object.                                                                                                                                                                                                                                                                                                                                |
| credentials    | Option 1                                | object        | The definition of the `CircleCIAPIKey` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | api_token [*required*]             | string        | The `CircleCIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`                                                                                                                                                                                                                                                                                               |
| Option 5       | type [*required*]                  | enum          | The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`                                                                                                                                                                                                                                                                                            |
| integration    | Option 6                                | object        | The definition of the `ClickupIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 6       | credentials [*required*]           |  <oneOf> | The definition of the `ClickupCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `ClickupAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_token [*required*]             | string        | The `ClickupAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 6       | type [*required*]                  | enum          | The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`                                                                                                                                                                                                                                                                                              |
| integration    | Option 7                                | object        | The definition of the `CloudflareIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 7       | credentials [*required*]           |  <oneOf> | The definition of the `CloudflareCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `CloudflareAPIToken` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `CloudflareAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`                                                                                                                                                                                                                                                                                       |
| credentials    | Option 2                                | object        | The definition of the `CloudflareGlobalAPIToken` object.                                                                                                                                                                                                                                                                                                                           |
| Option 2       | auth_email [*required*]            | string        | The `CloudflareGlobalAPIToken` `auth_email`.                                                                                                                                                                                                                                                                                                                                       |
| Option 2       | global_api_key [*required*]        | string        | The `CloudflareGlobalAPIToken` `global_api_key`.                                                                                                                                                                                                                                                                                                                                   |
| Option 2       | type [*required*]                  | enum          | The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`                                                                                                                                                                                                                                                                           |
| Option 7       | type [*required*]                  | enum          | The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`                                                                                                                                                                                                                                                                                        |
| integration    | Option 8                                | object        | The definition of the `ConfigCatIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 8       | credentials [*required*]           |  <oneOf> | The definition of the `ConfigCatCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `ConfigCatSDKKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_password [*required*]          | string        | The `ConfigCatSDKKey` `api_password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | api_username [*required*]          | string        | The `ConfigCatSDKKey` `api_username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | sdk_key [*required*]               | string        | The `ConfigCatSDKKey` `sdk_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`                                                                                                                                                                                                                                                                                             |
| Option 8       | type [*required*]                  | enum          | The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`                                                                                                                                                                                                                                                                                          |
| integration    | Option 9                                | object        | The definition of the `DatadogIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 9       | credentials [*required*]           |  <oneOf> | The definition of the `DatadogCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `DatadogAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `DatadogAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | app_key [*required*]               | string        | The `DatadogAPIKey` `app_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | datacenter [*required*]            | string        | The `DatadogAPIKey` `datacenter`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | subdomain                               | string        | Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see [https://docs.datadoghq.com/getting_started/site](https://docs.datadoghq.com/getting_started/site)). |
| Option 1       | type [*required*]                  | enum          | The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 9       | type [*required*]                  | enum          | The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`                                                                                                                                                                                                                                                                                              |
| integration    | Option 10                               | object        | The definition of the `FastlyIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 10      | credentials [*required*]           |  <oneOf> | The definition of the `FastlyCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `FastlyAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `FastlyAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 10      | type [*required*]                  | enum          | The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`                                                                                                                                                                                                                                                                                                |
| integration    | Option 11                               | object        | The definition of the `FreshserviceIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 11      | credentials [*required*]           |  <oneOf> | The definition of the `FreshserviceCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `FreshserviceAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_key [*required*]               | string        | The `FreshserviceAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                |
| Option 1       | domain [*required*]                | string        | The `FreshserviceAPIKey` `domain`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 11      | type [*required*]                  | enum          | The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`                                                                                                                                                                                                                                                                                    |
| integration    | Option 12                               | object        | The definition of the `GCPIntegration` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 12      | credentials [*required*]           |  <oneOf> | The definition of the `GCPCredentials` object.                                                                                                                                                                                                                                                                                                                                     |
| credentials    | Option 1                                | object        | The definition of the `GCPServiceAccount` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | private_key [*required*]           | string        | The `GCPServiceAccount` `private_key`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | service_account_email [*required*] | string        | The `GCPServiceAccount` `service_account_email`.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`                                                                                                                                                                                                                                                                                         |
| Option 12      | type [*required*]                  | enum          | The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`                                                                                                                                                                                                                                                                                                      |
| integration    | Option 13                               | object        | The definition of the `GeminiIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 13      | credentials [*required*]           |  <oneOf> | The definition of the `GeminiCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GeminiAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `GeminiAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 13      | type [*required*]                  | enum          | The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`                                                                                                                                                                                                                                                                                                |
| integration    | Option 14                               | object        | The definition of the `GitlabIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 14      | credentials [*required*]           |  <oneOf> | The definition of the `GitlabCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GitlabAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `GitlabAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 14      | type [*required*]                  | enum          | The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`                                                                                                                                                                                                                                                                                                |
| integration    | Option 15                               | object        | The definition of the `GreyNoiseIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 15      | credentials [*required*]           |  <oneOf> | The definition of the `GreyNoiseCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `GreyNoiseAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_key [*required*]               | string        | The `GreyNoiseAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 15      | type [*required*]                  | enum          | The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`                                                                                                                                                                                                                                                                                          |
| integration    | Option 16                               | object        | The definition of `HTTPIntegration` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 16      | base_url [*required*]              | string        | Base HTTP url for the integration                                                                                                                                                                                                                                                                                                                                                  |
| Option 16      | credentials [*required*]           |  <oneOf> | The definition of `HTTPCredentials` object.                                                                                                                                                                                                                                                                                                                                        |
| credentials    | Option 1                                | object        | The definition of `HTTPTokenAuth` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | body                                    | object        | The definition of `HTTPBody` object.                                                                                                                                                                                                                                                                                                                                               |
| body           | content                                 | string        | Serialized body content                                                                                                                                                                                                                                                                                                                                                            |
| body           | content_type                            | string        | Content type of the body                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | headers                                 | [object]      | The `HTTPTokenAuth` `headers`.                                                                                                                                                                                                                                                                                                                                                     |
| headers        | name [*required*]                  | string        | The `HTTPHeader` `name`.                                                                                                                                                                                                                                                                                                                                                           |
| headers        | value [*required*]                 | string        | The `HTTPHeader` `value`.                                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | tokens                                  | [object]      | The `HTTPTokenAuth` `tokens`.                                                                                                                                                                                                                                                                                                                                                      |
| tokens         | name [*required*]                  | string        | The `HTTPToken` `name`.                                                                                                                                                                                                                                                                                                                                                            |
| tokens         | type [*required*]                  | enum          | The definition of `TokenType` object. Allowed enum values: `SECRET`                                                                                                                                                                                                                                                                                                                |
| tokens         | value [*required*]                 | string        | The `HTTPToken` `value`.                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | type [*required*]                  | enum          | The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`                                                                                                                                                                                                                                                                                                 |
| Option 1       | url_parameters                          | [object]      | The `HTTPTokenAuth` `url_parameters`.                                                                                                                                                                                                                                                                                                                                              |
| url_parameters | name [*required*]                  | string        | Name for tokens.                                                                                                                                                                                                                                                                                                                                                                   |
| url_parameters | value [*required*]                 | string        | The `UrlParam` `value`.                                                                                                                                                                                                                                                                                                                                                            |
| Option 16      | type [*required*]                  | enum          | The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`                                                                                                                                                                                                                                                                                                        |
| integration    | Option 17                               | object        | The definition of the `LaunchDarklyIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 17      | credentials [*required*]           |  <oneOf> | The definition of the `LaunchDarklyCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `LaunchDarklyAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `LaunchDarklyAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 17      | type [*required*]                  | enum          | The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`                                                                                                                                                                                                                                                                                    |
| integration    | Option 18                               | object        | The definition of the `NotionIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 18      | credentials [*required*]           |  <oneOf> | The definition of the `NotionCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `NotionAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `NotionAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 18      | type [*required*]                  | enum          | The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`                                                                                                                                                                                                                                                                                                |
| integration    | Option 19                               | object        | The definition of the `OktaIntegration` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 19      | credentials [*required*]           |  <oneOf> | The definition of the `OktaCredentials` object.                                                                                                                                                                                                                                                                                                                                    |
| credentials    | Option 1                                | object        | The definition of the `OktaAPIToken` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OktaAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | domain [*required*]                | string        | The `OktaAPIToken` `domain`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`                                                                                                                                                                                                                                                                                                   |
| Option 19      | type [*required*]                  | enum          | The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`                                                                                                                                                                                                                                                                                                    |
| integration    | Option 20                               | object        | The definition of the `OpenAIIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 20      | credentials [*required*]           |  <oneOf> | The definition of the `OpenAICredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `OpenAIAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OpenAIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 20      | type [*required*]                  | enum          | The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`                                                                                                                                                                                                                                                                                                |
| integration    | Option 21                               | object        | The definition of the `ServiceNowIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 21      | credentials [*required*]           |  <oneOf> | The definition of the `ServiceNowCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `ServiceNowBasicAuth` object.                                                                                                                                                                                                                                                                                                                                |
| Option 1       | instance [*required*]              | string        | The `ServiceNowBasicAuth` `instance`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | password [*required*]              | string        | The `ServiceNowBasicAuth` `password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`                                                                                                                                                                                                                                                                                     |
| Option 1       | username [*required*]              | string        | The `ServiceNowBasicAuth` `username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 21      | type [*required*]                  | enum          | The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`                                                                                                                                                                                                                                                                                        |
| integration    | Option 22                               | object        | The definition of the `SplitIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 22      | credentials [*required*]           |  <oneOf> | The definition of the `SplitCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `SplitAPIKey` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | api_key [*required*]               | string        | The `SplitAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`                                                                                                                                                                                                                                                                                                     |
| Option 22      | type [*required*]                  | enum          | The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 23                               | object        | The definition of the `StatsigIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 23      | credentials [*required*]           |  <oneOf> | The definition of the `StatsigCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `StatsigAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `StatsigAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 23      | type [*required*]                  | enum          | The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`                                                                                                                                                                                                                                                                                              |
| integration    | Option 24                               | object        | The definition of the `VirusTotalIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 24      | credentials [*required*]           |  <oneOf> | The definition of the `VirusTotalCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `VirusTotalAPIKey` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | api_key [*required*]               | string        | The `VirusTotalAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`                                                                                                                                                                                                                                                                                           |
| Option 24      | type [*required*]                  | enum          | The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`                                                                                                                                                                                                                                                                                        |
| attributes     | name [*required*]                  | string        | Name of the connection                                                                                                                                                                                                                                                                                                                                                             |
| data           | id                                      | string        | The connection identifier                                                                                                                                                                                                                                                                                                                                                          |
| data           | type [*required*]                  | enum          | The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`                                                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "integration": {
        "credentials": {
          "account_id": "111222333444",
          "external_id": "33a1011635c44b38a064cf14e82e1d8f",
          "principal_id": "123456789012",
          "role": "my-role",
          "type": "AWSAssumeRole"
        },
        "type": "AWS"
      },
      "name": "My AWS Connection"
    },
    "id": "string",
    "type": "action_connection"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too Many Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport connection_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections/${connection_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get an existing Action Connection returns "Successfully get Action Connection" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.get_action_connection(
        connection_id="cb460d51-3c88-4e87-adac-d47131d0423d",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get an existing Action Connection returns "Successfully get Action Connection" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.get_action_connection("cb460d51-3c88-4e87-adac-d47131d0423d")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get an existing Action Connection returns "Successfully get Action Connection" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    resp, r, err := api.GetActionConnection(ctx, "cb460d51-3c88-4e87-adac-d47131d0423d")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.GetActionConnection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ActionConnectionApi.GetActionConnection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get an existing Action Connection returns "Successfully get Action Connection" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;
import com.datadog.api.client.v2.model.GetActionConnectionResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    try {
      GetActionConnectionResponse result =
          apiInstance.getActionConnection("cb460d51-3c88-4e87-adac-d47131d0423d");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#getActionConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get an existing Action Connection returns "Successfully get Action Connection"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api
        .get_action_connection("cb460d51-3c88-4e87-adac-d47131d0423d".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get an existing Action Connection returns "Successfully get Action Connection" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

const params: v2.ActionConnectionApiGetActionConnectionRequest = {
  connectionId: "cb460d51-3c88-4e87-adac-d47131d0423d",
};

apiInstance
  .getActionConnection(params)
  .then((data: v2.GetActionConnectionResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create a new Action Connection{% #create-a-new-action-connection %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/actions/connections |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/actions/connections |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/actions/connections      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/actions/connections      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/actions/connections     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/actions/connections |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/actions/connections |

### Overview

Create a new Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key).

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field   | Field                                   | Type          | Description                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | --------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data [*required*]                  | object        | Data related to the connection.                                                                                                                                                                                                                                                                                                                                                    |
| data           | attributes [*required*]            | object        | The definition of `ActionConnectionAttributes` object.                                                                                                                                                                                                                                                                                                                             |
| attributes     | integration [*required*]           |  <oneOf> | The definition of `ActionConnectionIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| integration    | Option 1                                | object        | The definition of `AWSIntegration` object.                                                                                                                                                                                                                                                                                                                                         |
| Option 1       | credentials [*required*]           |  <oneOf> | The definition of `AWSCredentials` object.                                                                                                                                                                                                                                                                                                                                         |
| credentials    | Option 1                                | object        | The definition of `AWSAssumeRole` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | account_id [*required*]            | string        | AWS account the connection is created for                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | external_id                             | string        | External ID used to scope which connection can be used to assume the role                                                                                                                                                                                                                                                                                                          |
| Option 1       | principal_id                            | string        | AWS account that will assume the role                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | role [*required*]                  | string        | Role to assume                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`                                                                                                                                                                                                                                                                                                          |
| integration    | Option 2                                | object        | The definition of the `AnthropicIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 2       | credentials [*required*]           |  <oneOf> | The definition of the `AnthropicCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `AnthropicAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_token [*required*]             | string        | The `AnthropicAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 2       | type [*required*]                  | enum          | The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`                                                                                                                                                                                                                                                                                          |
| integration    | Option 3                                | object        | The definition of the `AsanaIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 3       | credentials [*required*]           |  <oneOf> | The definition of the `AsanaCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AsanaAccessToken` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | access_token [*required*]          | string        | The `AsanaAccessToken` `access_token`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]                  | enum          | The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`                                                                                                                                                                                                                                                                                           |
| Option 3       | type [*required*]                  | enum          | The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 4                                | object        | The definition of the `AzureIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 4       | credentials [*required*]           |  <oneOf> | The definition of the `AzureCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AzureTenant` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | app_client_id [*required*]         | string        | The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.                                                             |
| Option 1       | client_secret [*required*]         | string        | The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application's secrets page. You can navigate to your application via the Azure Directory.                                                                                             |
| Option 1       | custom_scopes                           | string        | If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.                                        |
| Option 1       | tenant_id [*required*]             | string        | The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.                                                                                                                                        |
| Option 1       | type [*required*]                  | enum          | The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`                                                                                                                                                                                                                                                                                                     |
| Option 4       | type [*required*]                  | enum          | The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 5                                | object        | The definition of the `CircleCIIntegration` object.                                                                                                                                                                                                                                                                                                                                |
| Option 5       | credentials [*required*]           |  <oneOf> | The definition of the `CircleCICredentials` object.                                                                                                                                                                                                                                                                                                                                |
| credentials    | Option 1                                | object        | The definition of the `CircleCIAPIKey` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | api_token [*required*]             | string        | The `CircleCIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`                                                                                                                                                                                                                                                                                               |
| Option 5       | type [*required*]                  | enum          | The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`                                                                                                                                                                                                                                                                                            |
| integration    | Option 6                                | object        | The definition of the `ClickupIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 6       | credentials [*required*]           |  <oneOf> | The definition of the `ClickupCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `ClickupAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_token [*required*]             | string        | The `ClickupAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 6       | type [*required*]                  | enum          | The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`                                                                                                                                                                                                                                                                                              |
| integration    | Option 7                                | object        | The definition of the `CloudflareIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 7       | credentials [*required*]           |  <oneOf> | The definition of the `CloudflareCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `CloudflareAPIToken` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `CloudflareAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`                                                                                                                                                                                                                                                                                       |
| credentials    | Option 2                                | object        | The definition of the `CloudflareGlobalAPIToken` object.                                                                                                                                                                                                                                                                                                                           |
| Option 2       | auth_email [*required*]            | string        | The `CloudflareGlobalAPIToken` `auth_email`.                                                                                                                                                                                                                                                                                                                                       |
| Option 2       | global_api_key [*required*]        | string        | The `CloudflareGlobalAPIToken` `global_api_key`.                                                                                                                                                                                                                                                                                                                                   |
| Option 2       | type [*required*]                  | enum          | The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`                                                                                                                                                                                                                                                                           |
| Option 7       | type [*required*]                  | enum          | The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`                                                                                                                                                                                                                                                                                        |
| integration    | Option 8                                | object        | The definition of the `ConfigCatIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 8       | credentials [*required*]           |  <oneOf> | The definition of the `ConfigCatCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `ConfigCatSDKKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_password [*required*]          | string        | The `ConfigCatSDKKey` `api_password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | api_username [*required*]          | string        | The `ConfigCatSDKKey` `api_username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | sdk_key [*required*]               | string        | The `ConfigCatSDKKey` `sdk_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`                                                                                                                                                                                                                                                                                             |
| Option 8       | type [*required*]                  | enum          | The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`                                                                                                                                                                                                                                                                                          |
| integration    | Option 9                                | object        | The definition of the `DatadogIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 9       | credentials [*required*]           |  <oneOf> | The definition of the `DatadogCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `DatadogAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `DatadogAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | app_key [*required*]               | string        | The `DatadogAPIKey` `app_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | datacenter [*required*]            | string        | The `DatadogAPIKey` `datacenter`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | subdomain                               | string        | Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see [https://docs.datadoghq.com/getting_started/site](https://docs.datadoghq.com/getting_started/site)). |
| Option 1       | type [*required*]                  | enum          | The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 9       | type [*required*]                  | enum          | The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`                                                                                                                                                                                                                                                                                              |
| integration    | Option 10                               | object        | The definition of the `FastlyIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 10      | credentials [*required*]           |  <oneOf> | The definition of the `FastlyCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `FastlyAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `FastlyAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 10      | type [*required*]                  | enum          | The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`                                                                                                                                                                                                                                                                                                |
| integration    | Option 11                               | object        | The definition of the `FreshserviceIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 11      | credentials [*required*]           |  <oneOf> | The definition of the `FreshserviceCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `FreshserviceAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_key [*required*]               | string        | The `FreshserviceAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                |
| Option 1       | domain [*required*]                | string        | The `FreshserviceAPIKey` `domain`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 11      | type [*required*]                  | enum          | The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`                                                                                                                                                                                                                                                                                    |
| integration    | Option 12                               | object        | The definition of the `GCPIntegration` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 12      | credentials [*required*]           |  <oneOf> | The definition of the `GCPCredentials` object.                                                                                                                                                                                                                                                                                                                                     |
| credentials    | Option 1                                | object        | The definition of the `GCPServiceAccount` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | private_key [*required*]           | string        | The `GCPServiceAccount` `private_key`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | service_account_email [*required*] | string        | The `GCPServiceAccount` `service_account_email`.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`                                                                                                                                                                                                                                                                                         |
| Option 12      | type [*required*]                  | enum          | The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`                                                                                                                                                                                                                                                                                                      |
| integration    | Option 13                               | object        | The definition of the `GeminiIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 13      | credentials [*required*]           |  <oneOf> | The definition of the `GeminiCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GeminiAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `GeminiAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 13      | type [*required*]                  | enum          | The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`                                                                                                                                                                                                                                                                                                |
| integration    | Option 14                               | object        | The definition of the `GitlabIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 14      | credentials [*required*]           |  <oneOf> | The definition of the `GitlabCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GitlabAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `GitlabAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 14      | type [*required*]                  | enum          | The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`                                                                                                                                                                                                                                                                                                |
| integration    | Option 15                               | object        | The definition of the `GreyNoiseIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 15      | credentials [*required*]           |  <oneOf> | The definition of the `GreyNoiseCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `GreyNoiseAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_key [*required*]               | string        | The `GreyNoiseAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 15      | type [*required*]                  | enum          | The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`                                                                                                                                                                                                                                                                                          |
| integration    | Option 16                               | object        | The definition of `HTTPIntegration` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 16      | base_url [*required*]              | string        | Base HTTP url for the integration                                                                                                                                                                                                                                                                                                                                                  |
| Option 16      | credentials [*required*]           |  <oneOf> | The definition of `HTTPCredentials` object.                                                                                                                                                                                                                                                                                                                                        |
| credentials    | Option 1                                | object        | The definition of `HTTPTokenAuth` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | body                                    | object        | The definition of `HTTPBody` object.                                                                                                                                                                                                                                                                                                                                               |
| body           | content                                 | string        | Serialized body content                                                                                                                                                                                                                                                                                                                                                            |
| body           | content_type                            | string        | Content type of the body                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | headers                                 | [object]      | The `HTTPTokenAuth` `headers`.                                                                                                                                                                                                                                                                                                                                                     |
| headers        | name [*required*]                  | string        | The `HTTPHeader` `name`.                                                                                                                                                                                                                                                                                                                                                           |
| headers        | value [*required*]                 | string        | The `HTTPHeader` `value`.                                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | tokens                                  | [object]      | The `HTTPTokenAuth` `tokens`.                                                                                                                                                                                                                                                                                                                                                      |
| tokens         | name [*required*]                  | string        | The `HTTPToken` `name`.                                                                                                                                                                                                                                                                                                                                                            |
| tokens         | type [*required*]                  | enum          | The definition of `TokenType` object. Allowed enum values: `SECRET`                                                                                                                                                                                                                                                                                                                |
| tokens         | value [*required*]                 | string        | The `HTTPToken` `value`.                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | type [*required*]                  | enum          | The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`                                                                                                                                                                                                                                                                                                 |
| Option 1       | url_parameters                          | [object]      | The `HTTPTokenAuth` `url_parameters`.                                                                                                                                                                                                                                                                                                                                              |
| url_parameters | name [*required*]                  | string        | Name for tokens.                                                                                                                                                                                                                                                                                                                                                                   |
| url_parameters | value [*required*]                 | string        | The `UrlParam` `value`.                                                                                                                                                                                                                                                                                                                                                            |
| Option 16      | type [*required*]                  | enum          | The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`                                                                                                                                                                                                                                                                                                        |
| integration    | Option 17                               | object        | The definition of the `LaunchDarklyIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 17      | credentials [*required*]           |  <oneOf> | The definition of the `LaunchDarklyCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `LaunchDarklyAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `LaunchDarklyAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 17      | type [*required*]                  | enum          | The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`                                                                                                                                                                                                                                                                                    |
| integration    | Option 18                               | object        | The definition of the `NotionIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 18      | credentials [*required*]           |  <oneOf> | The definition of the `NotionCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `NotionAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `NotionAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 18      | type [*required*]                  | enum          | The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`                                                                                                                                                                                                                                                                                                |
| integration    | Option 19                               | object        | The definition of the `OktaIntegration` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 19      | credentials [*required*]           |  <oneOf> | The definition of the `OktaCredentials` object.                                                                                                                                                                                                                                                                                                                                    |
| credentials    | Option 1                                | object        | The definition of the `OktaAPIToken` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OktaAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | domain [*required*]                | string        | The `OktaAPIToken` `domain`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`                                                                                                                                                                                                                                                                                                   |
| Option 19      | type [*required*]                  | enum          | The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`                                                                                                                                                                                                                                                                                                    |
| integration    | Option 20                               | object        | The definition of the `OpenAIIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 20      | credentials [*required*]           |  <oneOf> | The definition of the `OpenAICredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `OpenAIAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OpenAIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 20      | type [*required*]                  | enum          | The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`                                                                                                                                                                                                                                                                                                |
| integration    | Option 21                               | object        | The definition of the `ServiceNowIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 21      | credentials [*required*]           |  <oneOf> | The definition of the `ServiceNowCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `ServiceNowBasicAuth` object.                                                                                                                                                                                                                                                                                                                                |
| Option 1       | instance [*required*]              | string        | The `ServiceNowBasicAuth` `instance`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | password [*required*]              | string        | The `ServiceNowBasicAuth` `password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`                                                                                                                                                                                                                                                                                     |
| Option 1       | username [*required*]              | string        | The `ServiceNowBasicAuth` `username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 21      | type [*required*]                  | enum          | The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`                                                                                                                                                                                                                                                                                        |
| integration    | Option 22                               | object        | The definition of the `SplitIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 22      | credentials [*required*]           |  <oneOf> | The definition of the `SplitCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `SplitAPIKey` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | api_key [*required*]               | string        | The `SplitAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`                                                                                                                                                                                                                                                                                                     |
| Option 22      | type [*required*]                  | enum          | The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 23                               | object        | The definition of the `StatsigIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 23      | credentials [*required*]           |  <oneOf> | The definition of the `StatsigCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `StatsigAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `StatsigAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 23      | type [*required*]                  | enum          | The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`                                                                                                                                                                                                                                                                                              |
| integration    | Option 24                               | object        | The definition of the `VirusTotalIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 24      | credentials [*required*]           |  <oneOf> | The definition of the `VirusTotalCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `VirusTotalAPIKey` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | api_key [*required*]               | string        | The `VirusTotalAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`                                                                                                                                                                                                                                                                                           |
| Option 24      | type [*required*]                  | enum          | The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`                                                                                                                                                                                                                                                                                        |
| attributes     | name [*required*]                  | string        | Name of the connection                                                                                                                                                                                                                                                                                                                                                             |
| data           | id                                      | string        | The connection identifier                                                                                                                                                                                                                                                                                                                                                          |
| data           | type [*required*]                  | enum          | The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`                                                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "action_connection",
    "attributes": {
      "name": "Cassette Connection exampleactionconnection",
      "integration": {
        "type": "AWS",
        "credentials": {
          "type": "AWSAssumeRole",
          "role": "MyRoleUpdated",
          "account_id": "123456789123"
        }
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Successfully created Action Connection
{% tab title="Model" %}
The response for a created connection

| Parent field   | Field                                   | Type          | Description                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | --------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data                                    | object        | Data related to the connection.                                                                                                                                                                                                                                                                                                                                                    |
| data           | attributes [*required*]            | object        | The definition of `ActionConnectionAttributes` object.                                                                                                                                                                                                                                                                                                                             |
| attributes     | integration [*required*]           |  <oneOf> | The definition of `ActionConnectionIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| integration    | Option 1                                | object        | The definition of `AWSIntegration` object.                                                                                                                                                                                                                                                                                                                                         |
| Option 1       | credentials [*required*]           |  <oneOf> | The definition of `AWSCredentials` object.                                                                                                                                                                                                                                                                                                                                         |
| credentials    | Option 1                                | object        | The definition of `AWSAssumeRole` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | account_id [*required*]            | string        | AWS account the connection is created for                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | external_id                             | string        | External ID used to scope which connection can be used to assume the role                                                                                                                                                                                                                                                                                                          |
| Option 1       | principal_id                            | string        | AWS account that will assume the role                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | role [*required*]                  | string        | Role to assume                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`                                                                                                                                                                                                                                                                                                          |
| integration    | Option 2                                | object        | The definition of the `AnthropicIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 2       | credentials [*required*]           |  <oneOf> | The definition of the `AnthropicCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `AnthropicAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_token [*required*]             | string        | The `AnthropicAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 2       | type [*required*]                  | enum          | The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`                                                                                                                                                                                                                                                                                          |
| integration    | Option 3                                | object        | The definition of the `AsanaIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 3       | credentials [*required*]           |  <oneOf> | The definition of the `AsanaCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AsanaAccessToken` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | access_token [*required*]          | string        | The `AsanaAccessToken` `access_token`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]                  | enum          | The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`                                                                                                                                                                                                                                                                                           |
| Option 3       | type [*required*]                  | enum          | The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 4                                | object        | The definition of the `AzureIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 4       | credentials [*required*]           |  <oneOf> | The definition of the `AzureCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AzureTenant` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | app_client_id [*required*]         | string        | The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.                                                             |
| Option 1       | client_secret [*required*]         | string        | The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application's secrets page. You can navigate to your application via the Azure Directory.                                                                                             |
| Option 1       | custom_scopes                           | string        | If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.                                        |
| Option 1       | tenant_id [*required*]             | string        | The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.                                                                                                                                        |
| Option 1       | type [*required*]                  | enum          | The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`                                                                                                                                                                                                                                                                                                     |
| Option 4       | type [*required*]                  | enum          | The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 5                                | object        | The definition of the `CircleCIIntegration` object.                                                                                                                                                                                                                                                                                                                                |
| Option 5       | credentials [*required*]           |  <oneOf> | The definition of the `CircleCICredentials` object.                                                                                                                                                                                                                                                                                                                                |
| credentials    | Option 1                                | object        | The definition of the `CircleCIAPIKey` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | api_token [*required*]             | string        | The `CircleCIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`                                                                                                                                                                                                                                                                                               |
| Option 5       | type [*required*]                  | enum          | The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`                                                                                                                                                                                                                                                                                            |
| integration    | Option 6                                | object        | The definition of the `ClickupIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 6       | credentials [*required*]           |  <oneOf> | The definition of the `ClickupCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `ClickupAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_token [*required*]             | string        | The `ClickupAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 6       | type [*required*]                  | enum          | The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`                                                                                                                                                                                                                                                                                              |
| integration    | Option 7                                | object        | The definition of the `CloudflareIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 7       | credentials [*required*]           |  <oneOf> | The definition of the `CloudflareCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `CloudflareAPIToken` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `CloudflareAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`                                                                                                                                                                                                                                                                                       |
| credentials    | Option 2                                | object        | The definition of the `CloudflareGlobalAPIToken` object.                                                                                                                                                                                                                                                                                                                           |
| Option 2       | auth_email [*required*]            | string        | The `CloudflareGlobalAPIToken` `auth_email`.                                                                                                                                                                                                                                                                                                                                       |
| Option 2       | global_api_key [*required*]        | string        | The `CloudflareGlobalAPIToken` `global_api_key`.                                                                                                                                                                                                                                                                                                                                   |
| Option 2       | type [*required*]                  | enum          | The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`                                                                                                                                                                                                                                                                           |
| Option 7       | type [*required*]                  | enum          | The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`                                                                                                                                                                                                                                                                                        |
| integration    | Option 8                                | object        | The definition of the `ConfigCatIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 8       | credentials [*required*]           |  <oneOf> | The definition of the `ConfigCatCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `ConfigCatSDKKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_password [*required*]          | string        | The `ConfigCatSDKKey` `api_password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | api_username [*required*]          | string        | The `ConfigCatSDKKey` `api_username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | sdk_key [*required*]               | string        | The `ConfigCatSDKKey` `sdk_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`                                                                                                                                                                                                                                                                                             |
| Option 8       | type [*required*]                  | enum          | The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`                                                                                                                                                                                                                                                                                          |
| integration    | Option 9                                | object        | The definition of the `DatadogIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 9       | credentials [*required*]           |  <oneOf> | The definition of the `DatadogCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `DatadogAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `DatadogAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | app_key [*required*]               | string        | The `DatadogAPIKey` `app_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | datacenter [*required*]            | string        | The `DatadogAPIKey` `datacenter`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | subdomain                               | string        | Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see [https://docs.datadoghq.com/getting_started/site](https://docs.datadoghq.com/getting_started/site)). |
| Option 1       | type [*required*]                  | enum          | The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 9       | type [*required*]                  | enum          | The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`                                                                                                                                                                                                                                                                                              |
| integration    | Option 10                               | object        | The definition of the `FastlyIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 10      | credentials [*required*]           |  <oneOf> | The definition of the `FastlyCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `FastlyAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `FastlyAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 10      | type [*required*]                  | enum          | The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`                                                                                                                                                                                                                                                                                                |
| integration    | Option 11                               | object        | The definition of the `FreshserviceIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 11      | credentials [*required*]           |  <oneOf> | The definition of the `FreshserviceCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `FreshserviceAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_key [*required*]               | string        | The `FreshserviceAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                |
| Option 1       | domain [*required*]                | string        | The `FreshserviceAPIKey` `domain`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 11      | type [*required*]                  | enum          | The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`                                                                                                                                                                                                                                                                                    |
| integration    | Option 12                               | object        | The definition of the `GCPIntegration` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 12      | credentials [*required*]           |  <oneOf> | The definition of the `GCPCredentials` object.                                                                                                                                                                                                                                                                                                                                     |
| credentials    | Option 1                                | object        | The definition of the `GCPServiceAccount` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | private_key [*required*]           | string        | The `GCPServiceAccount` `private_key`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | service_account_email [*required*] | string        | The `GCPServiceAccount` `service_account_email`.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`                                                                                                                                                                                                                                                                                         |
| Option 12      | type [*required*]                  | enum          | The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`                                                                                                                                                                                                                                                                                                      |
| integration    | Option 13                               | object        | The definition of the `GeminiIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 13      | credentials [*required*]           |  <oneOf> | The definition of the `GeminiCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GeminiAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `GeminiAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 13      | type [*required*]                  | enum          | The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`                                                                                                                                                                                                                                                                                                |
| integration    | Option 14                               | object        | The definition of the `GitlabIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 14      | credentials [*required*]           |  <oneOf> | The definition of the `GitlabCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GitlabAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `GitlabAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 14      | type [*required*]                  | enum          | The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`                                                                                                                                                                                                                                                                                                |
| integration    | Option 15                               | object        | The definition of the `GreyNoiseIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 15      | credentials [*required*]           |  <oneOf> | The definition of the `GreyNoiseCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `GreyNoiseAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_key [*required*]               | string        | The `GreyNoiseAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 15      | type [*required*]                  | enum          | The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`                                                                                                                                                                                                                                                                                          |
| integration    | Option 16                               | object        | The definition of `HTTPIntegration` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 16      | base_url [*required*]              | string        | Base HTTP url for the integration                                                                                                                                                                                                                                                                                                                                                  |
| Option 16      | credentials [*required*]           |  <oneOf> | The definition of `HTTPCredentials` object.                                                                                                                                                                                                                                                                                                                                        |
| credentials    | Option 1                                | object        | The definition of `HTTPTokenAuth` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | body                                    | object        | The definition of `HTTPBody` object.                                                                                                                                                                                                                                                                                                                                               |
| body           | content                                 | string        | Serialized body content                                                                                                                                                                                                                                                                                                                                                            |
| body           | content_type                            | string        | Content type of the body                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | headers                                 | [object]      | The `HTTPTokenAuth` `headers`.                                                                                                                                                                                                                                                                                                                                                     |
| headers        | name [*required*]                  | string        | The `HTTPHeader` `name`.                                                                                                                                                                                                                                                                                                                                                           |
| headers        | value [*required*]                 | string        | The `HTTPHeader` `value`.                                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | tokens                                  | [object]      | The `HTTPTokenAuth` `tokens`.                                                                                                                                                                                                                                                                                                                                                      |
| tokens         | name [*required*]                  | string        | The `HTTPToken` `name`.                                                                                                                                                                                                                                                                                                                                                            |
| tokens         | type [*required*]                  | enum          | The definition of `TokenType` object. Allowed enum values: `SECRET`                                                                                                                                                                                                                                                                                                                |
| tokens         | value [*required*]                 | string        | The `HTTPToken` `value`.                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | type [*required*]                  | enum          | The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`                                                                                                                                                                                                                                                                                                 |
| Option 1       | url_parameters                          | [object]      | The `HTTPTokenAuth` `url_parameters`.                                                                                                                                                                                                                                                                                                                                              |
| url_parameters | name [*required*]                  | string        | Name for tokens.                                                                                                                                                                                                                                                                                                                                                                   |
| url_parameters | value [*required*]                 | string        | The `UrlParam` `value`.                                                                                                                                                                                                                                                                                                                                                            |
| Option 16      | type [*required*]                  | enum          | The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`                                                                                                                                                                                                                                                                                                        |
| integration    | Option 17                               | object        | The definition of the `LaunchDarklyIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 17      | credentials [*required*]           |  <oneOf> | The definition of the `LaunchDarklyCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `LaunchDarklyAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `LaunchDarklyAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 17      | type [*required*]                  | enum          | The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`                                                                                                                                                                                                                                                                                    |
| integration    | Option 18                               | object        | The definition of the `NotionIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 18      | credentials [*required*]           |  <oneOf> | The definition of the `NotionCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `NotionAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `NotionAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 18      | type [*required*]                  | enum          | The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`                                                                                                                                                                                                                                                                                                |
| integration    | Option 19                               | object        | The definition of the `OktaIntegration` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 19      | credentials [*required*]           |  <oneOf> | The definition of the `OktaCredentials` object.                                                                                                                                                                                                                                                                                                                                    |
| credentials    | Option 1                                | object        | The definition of the `OktaAPIToken` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OktaAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | domain [*required*]                | string        | The `OktaAPIToken` `domain`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`                                                                                                                                                                                                                                                                                                   |
| Option 19      | type [*required*]                  | enum          | The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`                                                                                                                                                                                                                                                                                                    |
| integration    | Option 20                               | object        | The definition of the `OpenAIIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 20      | credentials [*required*]           |  <oneOf> | The definition of the `OpenAICredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `OpenAIAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OpenAIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 20      | type [*required*]                  | enum          | The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`                                                                                                                                                                                                                                                                                                |
| integration    | Option 21                               | object        | The definition of the `ServiceNowIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 21      | credentials [*required*]           |  <oneOf> | The definition of the `ServiceNowCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `ServiceNowBasicAuth` object.                                                                                                                                                                                                                                                                                                                                |
| Option 1       | instance [*required*]              | string        | The `ServiceNowBasicAuth` `instance`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | password [*required*]              | string        | The `ServiceNowBasicAuth` `password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`                                                                                                                                                                                                                                                                                     |
| Option 1       | username [*required*]              | string        | The `ServiceNowBasicAuth` `username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 21      | type [*required*]                  | enum          | The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`                                                                                                                                                                                                                                                                                        |
| integration    | Option 22                               | object        | The definition of the `SplitIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 22      | credentials [*required*]           |  <oneOf> | The definition of the `SplitCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `SplitAPIKey` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | api_key [*required*]               | string        | The `SplitAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`                                                                                                                                                                                                                                                                                                     |
| Option 22      | type [*required*]                  | enum          | The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 23                               | object        | The definition of the `StatsigIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 23      | credentials [*required*]           |  <oneOf> | The definition of the `StatsigCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `StatsigAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `StatsigAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 23      | type [*required*]                  | enum          | The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`                                                                                                                                                                                                                                                                                              |
| integration    | Option 24                               | object        | The definition of the `VirusTotalIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 24      | credentials [*required*]           |  <oneOf> | The definition of the `VirusTotalCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `VirusTotalAPIKey` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | api_key [*required*]               | string        | The `VirusTotalAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`                                                                                                                                                                                                                                                                                           |
| Option 24      | type [*required*]                  | enum          | The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`                                                                                                                                                                                                                                                                                        |
| attributes     | name [*required*]                  | string        | Name of the connection                                                                                                                                                                                                                                                                                                                                                             |
| data           | id                                      | string        | The connection identifier                                                                                                                                                                                                                                                                                                                                                          |
| data           | type [*required*]                  | enum          | The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`                                                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "integration": {
        "credentials": {
          "account_id": "111222333444",
          "external_id": "33a1011635c44b38a064cf14e82e1d8f",
          "principal_id": "123456789012",
          "role": "my-role",
          "type": "AWSAssumeRole"
        },
        "type": "AWS"
      },
      "name": "My AWS Connection"
    },
    "id": "string",
    "type": "action_connection"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too Many Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "action_connection",
    "attributes": {
      "name": "Cassette Connection exampleactionconnection",
      "integration": {
        "type": "AWS",
        "credentials": {
          "type": "AWSAssumeRole",
          "role": "MyRoleUpdated",
          "account_id": "123456789123"
        }
      }
    }
  }
}
EOF

#####

```go
// Create a new Action Connection returns "Successfully created Action Connection" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.CreateActionConnectionRequest{
        Data: datadogV2.ActionConnectionData{
            Type: datadogV2.ACTIONCONNECTIONDATATYPE_ACTION_CONNECTION,
            Attributes: datadogV2.ActionConnectionAttributes{
                Name: "Cassette Connection exampleactionconnection",
                Integration: datadogV2.ActionConnectionIntegration{
                    AWSIntegration: &datadogV2.AWSIntegration{
                        Type: datadogV2.AWSINTEGRATIONTYPE_AWS,
                        Credentials: datadogV2.AWSCredentials{
                            AWSAssumeRole: &datadogV2.AWSAssumeRole{
                                Type:      datadogV2.AWSASSUMEROLETYPE_AWSASSUMEROLE,
                                Role:      "MyRoleUpdated",
                                AccountId: "123456789123",
                            }},
                    }},
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    resp, r, err := api.CreateActionConnection(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.CreateActionConnection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ActionConnectionApi.CreateActionConnection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a new Action Connection returns "Successfully created Action Connection" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;
import com.datadog.api.client.v2.model.AWSAssumeRole;
import com.datadog.api.client.v2.model.AWSAssumeRoleType;
import com.datadog.api.client.v2.model.AWSCredentials;
import com.datadog.api.client.v2.model.AWSIntegration;
import com.datadog.api.client.v2.model.AWSIntegrationType;
import com.datadog.api.client.v2.model.ActionConnectionAttributes;
import com.datadog.api.client.v2.model.ActionConnectionData;
import com.datadog.api.client.v2.model.ActionConnectionDataType;
import com.datadog.api.client.v2.model.ActionConnectionIntegration;
import com.datadog.api.client.v2.model.CreateActionConnectionRequest;
import com.datadog.api.client.v2.model.CreateActionConnectionResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    CreateActionConnectionRequest body =
        new CreateActionConnectionRequest()
            .data(
                new ActionConnectionData()
                    .type(ActionConnectionDataType.ACTION_CONNECTION)
                    .attributes(
                        new ActionConnectionAttributes()
                            .name("Cassette Connection exampleactionconnection")
                            .integration(
                                new ActionConnectionIntegration(
                                    new AWSIntegration()
                                        .type(AWSIntegrationType.AWS)
                                        .credentials(
                                            new AWSCredentials(
                                                new AWSAssumeRole()
                                                    .type(AWSAssumeRoleType.AWSASSUMEROLE)
                                                    .role("MyRoleUpdated")
                                                    .accountId("123456789123")))))));

    try {
      CreateActionConnectionResponse result = apiInstance.createActionConnection(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#createActionConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
"""
Create a new Action Connection returns "Successfully created Action Connection" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
from datadog_api_client.v2.model.action_connection_data import ActionConnectionData
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.aws_assume_role import AWSAssumeRole
from datadog_api_client.v2.model.aws_assume_role_type import AWSAssumeRoleType
from datadog_api_client.v2.model.aws_integration import AWSIntegration
from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="Cassette Connection exampleactionconnection",
            integration=AWSIntegration(
                type=AWSIntegrationType.AWS,
                credentials=AWSAssumeRole(
                    type=AWSAssumeRoleType.AWSASSUMEROLE,
                    role="MyRoleUpdated",
                    account_id="123456789123",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.create_action_connection(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a new Action Connection returns "Successfully created Action Connection" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new

body = DatadogAPIClient::V2::CreateActionConnectionRequest.new({
  data: DatadogAPIClient::V2::ActionConnectionData.new({
    type: DatadogAPIClient::V2::ActionConnectionDataType::ACTION_CONNECTION,
    attributes: DatadogAPIClient::V2::ActionConnectionAttributes.new({
      name: "Cassette Connection exampleactionconnection",
      integration: DatadogAPIClient::V2::AWSIntegration.new({
        type: DatadogAPIClient::V2::AWSIntegrationType::AWS,
        credentials: DatadogAPIClient::V2::AWSAssumeRole.new({
          type: DatadogAPIClient::V2::AWSAssumeRoleType::AWSASSUMEROLE,
          role: "MyRoleUpdated",
          account_id: "123456789123",
        }),
      }),
    }),
  }),
})
p api_instance.create_action_connection(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a new Action Connection returns "Successfully created Action Connection"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;
use datadog_api_client::datadogV2::model::AWSAssumeRole;
use datadog_api_client::datadogV2::model::AWSAssumeRoleType;
use datadog_api_client::datadogV2::model::AWSCredentials;
use datadog_api_client::datadogV2::model::AWSIntegration;
use datadog_api_client::datadogV2::model::AWSIntegrationType;
use datadog_api_client::datadogV2::model::ActionConnectionAttributes;
use datadog_api_client::datadogV2::model::ActionConnectionData;
use datadog_api_client::datadogV2::model::ActionConnectionDataType;
use datadog_api_client::datadogV2::model::ActionConnectionIntegration;
use datadog_api_client::datadogV2::model::CreateActionConnectionRequest;

#[tokio::main]
async fn main() {
    let body = CreateActionConnectionRequest::new(ActionConnectionData::new(
        ActionConnectionAttributes::new(
            ActionConnectionIntegration::AWSIntegration(Box::new(AWSIntegration::new(
                AWSCredentials::AWSAssumeRole(Box::new(AWSAssumeRole::new(
                    "123456789123".to_string(),
                    "MyRoleUpdated".to_string(),
                    AWSAssumeRoleType::AWSASSUMEROLE,
                ))),
                AWSIntegrationType::AWS,
            ))),
            "Cassette Connection exampleactionconnection".to_string(),
        ),
        ActionConnectionDataType::ACTION_CONNECTION,
    ));
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api.create_action_connection(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Create a new Action Connection returns "Successfully created Action Connection" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

const params: v2.ActionConnectionApiCreateActionConnectionRequest = {
  body: {
    data: {
      type: "action_connection",
      attributes: {
        name: "Cassette Connection exampleactionconnection",
        integration: {
          type: "AWS",
          credentials: {
            type: "AWSAssumeRole",
            role: "MyRoleUpdated",
            accountId: "123456789123",
          },
        },
      },
    },
  },
};

apiInstance
  .createActionConnection(params)
  .then((data: v2.CreateActionConnectionResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update an existing Action Connection{% #update-an-existing-action-connection %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/actions/connections/{connection_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/actions/connections/{connection_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/actions/connections/{connection_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/actions/connections/{connection_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/actions/connections/{connection_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/actions/connections/{connection_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/actions/connections/{connection_id} |

### Overview

Update an existing Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key).

### Arguments

#### Path Parameters

| Name                            | Type   | Description                     |
| ------------------------------- | ------ | ------------------------------- |
| connection_id [*required*] | string | The ID of the action connection |

### Request

#### Body Data (required)

Update an existing Action Connection request body

{% tab title="Model" %}

| Parent field   | Field                        | Type          | Description                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | ---------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data [*required*]       | object        | Data related to the connection update.                                                                                                                                                                                                                                                                                                                                             |
| data           | attributes [*required*] | object        | The definition of `ActionConnectionAttributesUpdate` object.                                                                                                                                                                                                                                                                                                                       |
| attributes     | integration                  |  <oneOf> | The definition of `ActionConnectionIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                      |
| integration    | Option 1                     | object        | The definition of `AWSIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | credentials                  |  <oneOf> | The definition of `AWSCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                     | object        | The definition of `AWSAssumeRoleUpdate` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | account_id                   | string        | AWS account the connection is created for                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | generate_new_external_id     | boolean       | The `AWSAssumeRoleUpdate` `generate_new_external_id`.                                                                                                                                                                                                                                                                                                                              |
| Option 1       | role                         | string        | Role to assume                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]       | enum          | The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]       | enum          | The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`                                                                                                                                                                                                                                                                                                          |
| integration    | Option 2                     | object        | The definition of the `AnthropicIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                         |
| Option 2       | credentials                  |  <oneOf> | The definition of the `AnthropicCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                         |
| credentials    | Option 1                     | object        | The definition of the `AnthropicAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_token                    | string        | The `AnthropicAPIKeyUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | type [*required*]       | enum          | The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 2       | type [*required*]       | enum          | The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`                                                                                                                                                                                                                                                                                          |
| integration    | Option 3                     | object        | The definition of the `AsanaIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                             |
| Option 3       | credentials                  |  <oneOf> | The definition of the `AsanaCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                             |
| credentials    | Option 1                     | object        | The definition of the `AsanaAccessToken` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | access_token                 | string        | The `AsanaAccessTokenUpdate` `access_token`.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]       | enum          | The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`                                                                                                                                                                                                                                                                                           |
| Option 3       | type [*required*]       | enum          | The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 4                     | object        | The definition of the `AzureIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                             |
| Option 4       | credentials                  |  <oneOf> | The definition of the `AzureCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                             |
| credentials    | Option 1                     | object        | The definition of the `AzureTenant` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | app_client_id                | string        | The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.                                                             |
| Option 1       | client_secret                | string        | The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application's secrets page. You can navigate to your application via the Azure Directory.                                                                                             |
| Option 1       | custom_scopes                | string        | If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.                                        |
| Option 1       | tenant_id                    | string        | The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.                                                                                                                                        |
| Option 1       | type [*required*]       | enum          | The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`                                                                                                                                                                                                                                                                                                     |
| Option 4       | type [*required*]       | enum          | The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 5                     | object        | The definition of the `CircleCIIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                          |
| Option 5       | credentials                  |  <oneOf> | The definition of the `CircleCICredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                          |
| credentials    | Option 1                     | object        | The definition of the `CircleCIAPIKey` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | api_token                    | string        | The `CircleCIAPIKeyUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                            |
| Option 1       | type [*required*]       | enum          | The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`                                                                                                                                                                                                                                                                                               |
| Option 5       | type [*required*]       | enum          | The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`                                                                                                                                                                                                                                                                                            |
| integration    | Option 6                     | object        | The definition of the `ClickupIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                           |
| Option 6       | credentials                  |  <oneOf> | The definition of the `ClickupCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                           |
| credentials    | Option 1                     | object        | The definition of the `ClickupAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_token                    | string        | The `ClickupAPIKeyUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]       | enum          | The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 6       | type [*required*]       | enum          | The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`                                                                                                                                                                                                                                                                                              |
| integration    | Option 7                     | object        | The definition of the `CloudflareIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                        |
| Option 7       | credentials                  |  <oneOf> | The definition of the `CloudflareCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                        |
| credentials    | Option 1                     | object        | The definition of the `CloudflareAPIToken` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token                    | string        | The `CloudflareAPITokenUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | type [*required*]       | enum          | The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`                                                                                                                                                                                                                                                                                       |
| credentials    | Option 2                     | object        | The definition of the `CloudflareGlobalAPIToken` object.                                                                                                                                                                                                                                                                                                                           |
| Option 2       | auth_email                   | string        | The `CloudflareGlobalAPITokenUpdate` `auth_email`.                                                                                                                                                                                                                                                                                                                                 |
| Option 2       | global_api_key               | string        | The `CloudflareGlobalAPITokenUpdate` `global_api_key`.                                                                                                                                                                                                                                                                                                                             |
| Option 2       | type [*required*]       | enum          | The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`                                                                                                                                                                                                                                                                           |
| Option 7       | type [*required*]       | enum          | The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`                                                                                                                                                                                                                                                                                        |
| integration    | Option 8                     | object        | The definition of the `ConfigCatIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                         |
| Option 8       | credentials                  |  <oneOf> | The definition of the `ConfigCatCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                         |
| credentials    | Option 1                     | object        | The definition of the `ConfigCatSDKKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_password                 | string        | The `ConfigCatSDKKeyUpdate` `api_password`.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | api_username                 | string        | The `ConfigCatSDKKeyUpdate` `api_username`.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | sdk_key                      | string        | The `ConfigCatSDKKeyUpdate` `sdk_key`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]       | enum          | The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`                                                                                                                                                                                                                                                                                             |
| Option 8       | type [*required*]       | enum          | The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`                                                                                                                                                                                                                                                                                          |
| integration    | Option 9                     | object        | The definition of the `DatadogIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                           |
| Option 9       | credentials                  |  <oneOf> | The definition of the `DatadogCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                           |
| credentials    | Option 1                     | object        | The definition of the `DatadogAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key                      | string        | The `DatadogAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                               |
| Option 1       | app_key                      | string        | The `DatadogAPIKeyUpdate` `app_key`.                                                                                                                                                                                                                                                                                                                                               |
| Option 1       | datacenter                   | string        | The `DatadogAPIKeyUpdate` `datacenter`.                                                                                                                                                                                                                                                                                                                                            |
| Option 1       | subdomain                    | string        | Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see [https://docs.datadoghq.com/getting_started/site](https://docs.datadoghq.com/getting_started/site)). |
| Option 1       | type [*required*]       | enum          | The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 9       | type [*required*]       | enum          | The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`                                                                                                                                                                                                                                                                                              |
| integration    | Option 10                    | object        | The definition of the `FastlyIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| Option 10      | credentials                  |  <oneOf> | The definition of the `FastlyCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                     | object        | The definition of the `FastlyAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key                      | string        | The `FastlyAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                                |
| Option 1       | type [*required*]       | enum          | The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 10      | type [*required*]       | enum          | The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`                                                                                                                                                                                                                                                                                                |
| integration    | Option 11                    | object        | The definition of the `FreshserviceIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                      |
| Option 11      | credentials                  |  <oneOf> | The definition of the `FreshserviceCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                      |
| credentials    | Option 1                     | object        | The definition of the `FreshserviceAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_key                      | string        | The `FreshserviceAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | domain                       | string        | The `FreshserviceAPIKeyUpdate` `domain`.                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | type [*required*]       | enum          | The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 11      | type [*required*]       | enum          | The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`                                                                                                                                                                                                                                                                                    |
| integration    | Option 12                    | object        | The definition of the `GCPIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                               |
| Option 12      | credentials                  |  <oneOf> | The definition of the `GCPCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                     | object        | The definition of the `GCPServiceAccount` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | private_key                  | string        | The `GCPServiceAccountUpdate` `private_key`.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | service_account_email        | string        | The `GCPServiceAccountUpdate` `service_account_email`.                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]       | enum          | The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`                                                                                                                                                                                                                                                                                         |
| Option 12      | type [*required*]       | enum          | The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`                                                                                                                                                                                                                                                                                                      |
| integration    | Option 13                    | object        | The definition of the `GeminiIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| Option 13      | credentials                  |  <oneOf> | The definition of the `GeminiCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                     | object        | The definition of the `GeminiAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key                      | string        | The `GeminiAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                                |
| Option 1       | type [*required*]       | enum          | The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 13      | type [*required*]       | enum          | The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`                                                                                                                                                                                                                                                                                                |
| integration    | Option 14                    | object        | The definition of the `GitlabIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| Option 14      | credentials                  |  <oneOf> | The definition of the `GitlabCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                     | object        | The definition of the `GitlabAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token                    | string        | The `GitlabAPIKeyUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]       | enum          | The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 14      | type [*required*]       | enum          | The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`                                                                                                                                                                                                                                                                                                |
| integration    | Option 15                    | object        | The definition of the `GreyNoiseIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                         |
| Option 15      | credentials                  |  <oneOf> | The definition of the `GreyNoiseCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                         |
| credentials    | Option 1                     | object        | The definition of the `GreyNoiseAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_key                      | string        | The `GreyNoiseAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]       | enum          | The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 15      | type [*required*]       | enum          | The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`                                                                                                                                                                                                                                                                                          |
| integration    | Option 16                    | object        | The definition of `HTTPIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 16      | base_url                     | string        | Base HTTP url for the integration                                                                                                                                                                                                                                                                                                                                                  |
| Option 16      | credentials                  |  <oneOf> | The definition of `HTTPCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                     | object        | The definition of `HTTPTokenAuthUpdate` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | body                         | object        | The definition of `HTTPBody` object.                                                                                                                                                                                                                                                                                                                                               |
| body           | content                      | string        | Serialized body content                                                                                                                                                                                                                                                                                                                                                            |
| body           | content_type                 | string        | Content type of the body                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | headers                      | [object]      | The `HTTPTokenAuthUpdate` `headers`.                                                                                                                                                                                                                                                                                                                                               |
| headers        | deleted                      | boolean       | Should the header be deleted.                                                                                                                                                                                                                                                                                                                                                      |
| headers        | name [*required*]       | string        | The `HTTPHeaderUpdate` `name`.                                                                                                                                                                                                                                                                                                                                                     |
| headers        | value                        | string        | The `HTTPHeaderUpdate` `value`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | tokens                       | [object]      | The `HTTPTokenAuthUpdate` `tokens`.                                                                                                                                                                                                                                                                                                                                                |
| tokens         | deleted                      | boolean       | Should the header be deleted.                                                                                                                                                                                                                                                                                                                                                      |
| tokens         | name [*required*]       | string        | The `HTTPToken` `name`.                                                                                                                                                                                                                                                                                                                                                            |
| tokens         | type [*required*]       | enum          | The definition of `TokenType` object. Allowed enum values: `SECRET`                                                                                                                                                                                                                                                                                                                |
| tokens         | value [*required*]      | string        | The `HTTPToken` `value`.                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | type [*required*]       | enum          | The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`                                                                                                                                                                                                                                                                                                 |
| Option 1       | url_parameters               | [object]      | The `HTTPTokenAuthUpdate` `url_parameters`.                                                                                                                                                                                                                                                                                                                                        |
| url_parameters | deleted                      | boolean       | Should the header be deleted.                                                                                                                                                                                                                                                                                                                                                      |
| url_parameters | name [*required*]       | string        | Name for tokens.                                                                                                                                                                                                                                                                                                                                                                   |
| url_parameters | value                        | string        | The `UrlParamUpdate` `value`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 16      | type [*required*]       | enum          | The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`                                                                                                                                                                                                                                                                                                        |
| integration    | Option 17                    | object        | The definition of the `LaunchDarklyIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                      |
| Option 17      | credentials                  |  <oneOf> | The definition of the `LaunchDarklyCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                      |
| credentials    | Option 1                     | object        | The definition of the `LaunchDarklyAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token                    | string        | The `LaunchDarklyAPIKeyUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | type [*required*]       | enum          | The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 17      | type [*required*]       | enum          | The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`                                                                                                                                                                                                                                                                                    |
| integration    | Option 18                    | object        | The definition of the `NotionIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| Option 18      | credentials                  |  <oneOf> | The definition of the `NotionCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                     | object        | The definition of the `NotionAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token                    | string        | The `NotionAPIKeyUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]       | enum          | The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 18      | type [*required*]       | enum          | The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`                                                                                                                                                                                                                                                                                                |
| integration    | Option 19                    | object        | The definition of the `OktaIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                              |
| Option 19      | credentials                  |  <oneOf> | The definition of the `OktaCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                     | object        | The definition of the `OktaAPIToken` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token                    | string        | The `OktaAPITokenUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | domain                       | string        | The `OktaAPITokenUpdate` `domain`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]       | enum          | The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`                                                                                                                                                                                                                                                                                                   |
| Option 19      | type [*required*]       | enum          | The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`                                                                                                                                                                                                                                                                                                    |
| integration    | Option 20                    | object        | The definition of the `OpenAIIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| Option 20      | credentials                  |  <oneOf> | The definition of the `OpenAICredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                     | object        | The definition of the `OpenAIAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token                    | string        | The `OpenAIAPIKeyUpdate` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]       | enum          | The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 20      | type [*required*]       | enum          | The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`                                                                                                                                                                                                                                                                                                |
| integration    | Option 21                    | object        | The definition of the `ServiceNowIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                        |
| Option 21      | credentials                  |  <oneOf> | The definition of the `ServiceNowCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                        |
| credentials    | Option 1                     | object        | The definition of the `ServiceNowBasicAuth` object.                                                                                                                                                                                                                                                                                                                                |
| Option 1       | instance                     | string        | The `ServiceNowBasicAuthUpdate` `instance`.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | password                     | string        | The `ServiceNowBasicAuthUpdate` `password`.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | type [*required*]       | enum          | The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`                                                                                                                                                                                                                                                                                     |
| Option 1       | username                     | string        | The `ServiceNowBasicAuthUpdate` `username`.                                                                                                                                                                                                                                                                                                                                        |
| Option 21      | type [*required*]       | enum          | The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`                                                                                                                                                                                                                                                                                        |
| integration    | Option 22                    | object        | The definition of the `SplitIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                             |
| Option 22      | credentials                  |  <oneOf> | The definition of the `SplitCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                             |
| credentials    | Option 1                     | object        | The definition of the `SplitAPIKey` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | api_key                      | string        | The `SplitAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]       | enum          | The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`                                                                                                                                                                                                                                                                                                     |
| Option 22      | type [*required*]       | enum          | The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 23                    | object        | The definition of the `StatsigIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                           |
| Option 23      | credentials                  |  <oneOf> | The definition of the `StatsigCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                           |
| credentials    | Option 1                     | object        | The definition of the `StatsigAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key                      | string        | The `StatsigAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                               |
| Option 1       | type [*required*]       | enum          | The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 23      | type [*required*]       | enum          | The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`                                                                                                                                                                                                                                                                                              |
| integration    | Option 24                    | object        | The definition of the `VirusTotalIntegrationUpdate` object.                                                                                                                                                                                                                                                                                                                        |
| Option 24      | credentials                  |  <oneOf> | The definition of the `VirusTotalCredentialsUpdate` object.                                                                                                                                                                                                                                                                                                                        |
| credentials    | Option 1                     | object        | The definition of the `VirusTotalAPIKey` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | api_key                      | string        | The `VirusTotalAPIKeyUpdate` `api_key`.                                                                                                                                                                                                                                                                                                                                            |
| Option 1       | type [*required*]       | enum          | The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`                                                                                                                                                                                                                                                                                           |
| Option 24      | type [*required*]       | enum          | The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`                                                                                                                                                                                                                                                                                        |
| attributes     | name                         | string        | Name of the connection                                                                                                                                                                                                                                                                                                                                                             |
| data           | type [*required*]       | enum          | The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`                                                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "action_connection",
    "attributes": {
      "name": "Cassette Connection",
      "integration": {
        "type": "AWS",
        "credentials": {
          "type": "AWSAssumeRole",
          "role": "MyRoleUpdated",
          "account_id": "123456789123"
        }
      }
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Successfully updated Action Connection
{% tab title="Model" %}
The response for an updated connection.

| Parent field   | Field                                   | Type          | Description                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | --------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | data                                    | object        | Data related to the connection.                                                                                                                                                                                                                                                                                                                                                    |
| data           | attributes [*required*]            | object        | The definition of `ActionConnectionAttributes` object.                                                                                                                                                                                                                                                                                                                             |
| attributes     | integration [*required*]           |  <oneOf> | The definition of `ActionConnectionIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| integration    | Option 1                                | object        | The definition of `AWSIntegration` object.                                                                                                                                                                                                                                                                                                                                         |
| Option 1       | credentials [*required*]           |  <oneOf> | The definition of `AWSCredentials` object.                                                                                                                                                                                                                                                                                                                                         |
| credentials    | Option 1                                | object        | The definition of `AWSAssumeRole` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | account_id [*required*]            | string        | AWS account the connection is created for                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | external_id                             | string        | External ID used to scope which connection can be used to assume the role                                                                                                                                                                                                                                                                                                          |
| Option 1       | principal_id                            | string        | AWS account that will assume the role                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | role [*required*]                  | string        | Role to assume                                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`                                                                                                                                                                                                                                                                                                          |
| integration    | Option 2                                | object        | The definition of the `AnthropicIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 2       | credentials [*required*]           |  <oneOf> | The definition of the `AnthropicCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `AnthropicAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_token [*required*]             | string        | The `AnthropicAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 2       | type [*required*]                  | enum          | The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`                                                                                                                                                                                                                                                                                          |
| integration    | Option 3                                | object        | The definition of the `AsanaIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 3       | credentials [*required*]           |  <oneOf> | The definition of the `AsanaCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AsanaAccessToken` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | access_token [*required*]          | string        | The `AsanaAccessToken` `access_token`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | type [*required*]                  | enum          | The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`                                                                                                                                                                                                                                                                                           |
| Option 3       | type [*required*]                  | enum          | The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 4                                | object        | The definition of the `AzureIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 4       | credentials [*required*]           |  <oneOf> | The definition of the `AzureCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `AzureTenant` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | app_client_id [*required*]         | string        | The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.                                                             |
| Option 1       | client_secret [*required*]         | string        | The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application's secrets page. You can navigate to your application via the Azure Directory.                                                                                             |
| Option 1       | custom_scopes                           | string        | If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.                                        |
| Option 1       | tenant_id [*required*]             | string        | The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.                                                                                                                                        |
| Option 1       | type [*required*]                  | enum          | The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`                                                                                                                                                                                                                                                                                                     |
| Option 4       | type [*required*]                  | enum          | The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 5                                | object        | The definition of the `CircleCIIntegration` object.                                                                                                                                                                                                                                                                                                                                |
| Option 5       | credentials [*required*]           |  <oneOf> | The definition of the `CircleCICredentials` object.                                                                                                                                                                                                                                                                                                                                |
| credentials    | Option 1                                | object        | The definition of the `CircleCIAPIKey` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | api_token [*required*]             | string        | The `CircleCIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`                                                                                                                                                                                                                                                                                               |
| Option 5       | type [*required*]                  | enum          | The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`                                                                                                                                                                                                                                                                                            |
| integration    | Option 6                                | object        | The definition of the `ClickupIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 6       | credentials [*required*]           |  <oneOf> | The definition of the `ClickupCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `ClickupAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_token [*required*]             | string        | The `ClickupAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 6       | type [*required*]                  | enum          | The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`                                                                                                                                                                                                                                                                                              |
| integration    | Option 7                                | object        | The definition of the `CloudflareIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 7       | credentials [*required*]           |  <oneOf> | The definition of the `CloudflareCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `CloudflareAPIToken` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `CloudflareAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`                                                                                                                                                                                                                                                                                       |
| credentials    | Option 2                                | object        | The definition of the `CloudflareGlobalAPIToken` object.                                                                                                                                                                                                                                                                                                                           |
| Option 2       | auth_email [*required*]            | string        | The `CloudflareGlobalAPIToken` `auth_email`.                                                                                                                                                                                                                                                                                                                                       |
| Option 2       | global_api_key [*required*]        | string        | The `CloudflareGlobalAPIToken` `global_api_key`.                                                                                                                                                                                                                                                                                                                                   |
| Option 2       | type [*required*]                  | enum          | The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`                                                                                                                                                                                                                                                                           |
| Option 7       | type [*required*]                  | enum          | The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`                                                                                                                                                                                                                                                                                        |
| integration    | Option 8                                | object        | The definition of the `ConfigCatIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 8       | credentials [*required*]           |  <oneOf> | The definition of the `ConfigCatCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `ConfigCatSDKKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_password [*required*]          | string        | The `ConfigCatSDKKey` `api_password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | api_username [*required*]          | string        | The `ConfigCatSDKKey` `api_username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | sdk_key [*required*]               | string        | The `ConfigCatSDKKey` `sdk_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`                                                                                                                                                                                                                                                                                             |
| Option 8       | type [*required*]                  | enum          | The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`                                                                                                                                                                                                                                                                                          |
| integration    | Option 9                                | object        | The definition of the `DatadogIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 9       | credentials [*required*]           |  <oneOf> | The definition of the `DatadogCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `DatadogAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `DatadogAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | app_key [*required*]               | string        | The `DatadogAPIKey` `app_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | datacenter [*required*]            | string        | The `DatadogAPIKey` `datacenter`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | subdomain                               | string        | Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see [https://docs.datadoghq.com/getting_started/site](https://docs.datadoghq.com/getting_started/site)). |
| Option 1       | type [*required*]                  | enum          | The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 9       | type [*required*]                  | enum          | The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`                                                                                                                                                                                                                                                                                              |
| integration    | Option 10                               | object        | The definition of the `FastlyIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 10      | credentials [*required*]           |  <oneOf> | The definition of the `FastlyCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `FastlyAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `FastlyAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 10      | type [*required*]                  | enum          | The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`                                                                                                                                                                                                                                                                                                |
| integration    | Option 11                               | object        | The definition of the `FreshserviceIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 11      | credentials [*required*]           |  <oneOf> | The definition of the `FreshserviceCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `FreshserviceAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_key [*required*]               | string        | The `FreshserviceAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                |
| Option 1       | domain [*required*]                | string        | The `FreshserviceAPIKey` `domain`.                                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | type [*required*]                  | enum          | The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 11      | type [*required*]                  | enum          | The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`                                                                                                                                                                                                                                                                                    |
| integration    | Option 12                               | object        | The definition of the `GCPIntegration` object.                                                                                                                                                                                                                                                                                                                                     |
| Option 12      | credentials [*required*]           |  <oneOf> | The definition of the `GCPCredentials` object.                                                                                                                                                                                                                                                                                                                                     |
| credentials    | Option 1                                | object        | The definition of the `GCPServiceAccount` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | private_key [*required*]           | string        | The `GCPServiceAccount` `private_key`.                                                                                                                                                                                                                                                                                                                                             |
| Option 1       | service_account_email [*required*] | string        | The `GCPServiceAccount` `service_account_email`.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`                                                                                                                                                                                                                                                                                         |
| Option 12      | type [*required*]                  | enum          | The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`                                                                                                                                                                                                                                                                                                      |
| integration    | Option 13                               | object        | The definition of the `GeminiIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 13      | credentials [*required*]           |  <oneOf> | The definition of the `GeminiCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GeminiAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_key [*required*]               | string        | The `GeminiAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | type [*required*]                  | enum          | The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 13      | type [*required*]                  | enum          | The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`                                                                                                                                                                                                                                                                                                |
| integration    | Option 14                               | object        | The definition of the `GitlabIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 14      | credentials [*required*]           |  <oneOf> | The definition of the `GitlabCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `GitlabAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `GitlabAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 14      | type [*required*]                  | enum          | The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`                                                                                                                                                                                                                                                                                                |
| integration    | Option 15                               | object        | The definition of the `GreyNoiseIntegration` object.                                                                                                                                                                                                                                                                                                                               |
| Option 15      | credentials [*required*]           |  <oneOf> | The definition of the `GreyNoiseCredentials` object.                                                                                                                                                                                                                                                                                                                               |
| credentials    | Option 1                                | object        | The definition of the `GreyNoiseAPIKey` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | api_key [*required*]               | string        | The `GreyNoiseAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | type [*required*]                  | enum          | The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`                                                                                                                                                                                                                                                                                             |
| Option 15      | type [*required*]                  | enum          | The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`                                                                                                                                                                                                                                                                                          |
| integration    | Option 16                               | object        | The definition of `HTTPIntegration` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 16      | base_url [*required*]              | string        | Base HTTP url for the integration                                                                                                                                                                                                                                                                                                                                                  |
| Option 16      | credentials [*required*]           |  <oneOf> | The definition of `HTTPCredentials` object.                                                                                                                                                                                                                                                                                                                                        |
| credentials    | Option 1                                | object        | The definition of `HTTPTokenAuth` object.                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | body                                    | object        | The definition of `HTTPBody` object.                                                                                                                                                                                                                                                                                                                                               |
| body           | content                                 | string        | Serialized body content                                                                                                                                                                                                                                                                                                                                                            |
| body           | content_type                            | string        | Content type of the body                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | headers                                 | [object]      | The `HTTPTokenAuth` `headers`.                                                                                                                                                                                                                                                                                                                                                     |
| headers        | name [*required*]                  | string        | The `HTTPHeader` `name`.                                                                                                                                                                                                                                                                                                                                                           |
| headers        | value [*required*]                 | string        | The `HTTPHeader` `value`.                                                                                                                                                                                                                                                                                                                                                          |
| Option 1       | tokens                                  | [object]      | The `HTTPTokenAuth` `tokens`.                                                                                                                                                                                                                                                                                                                                                      |
| tokens         | name [*required*]                  | string        | The `HTTPToken` `name`.                                                                                                                                                                                                                                                                                                                                                            |
| tokens         | type [*required*]                  | enum          | The definition of `TokenType` object. Allowed enum values: `SECRET`                                                                                                                                                                                                                                                                                                                |
| tokens         | value [*required*]                 | string        | The `HTTPToken` `value`.                                                                                                                                                                                                                                                                                                                                                           |
| Option 1       | type [*required*]                  | enum          | The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`                                                                                                                                                                                                                                                                                                 |
| Option 1       | url_parameters                          | [object]      | The `HTTPTokenAuth` `url_parameters`.                                                                                                                                                                                                                                                                                                                                              |
| url_parameters | name [*required*]                  | string        | Name for tokens.                                                                                                                                                                                                                                                                                                                                                                   |
| url_parameters | value [*required*]                 | string        | The `UrlParam` `value`.                                                                                                                                                                                                                                                                                                                                                            |
| Option 16      | type [*required*]                  | enum          | The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`                                                                                                                                                                                                                                                                                                        |
| integration    | Option 17                               | object        | The definition of the `LaunchDarklyIntegration` object.                                                                                                                                                                                                                                                                                                                            |
| Option 17      | credentials [*required*]           |  <oneOf> | The definition of the `LaunchDarklyCredentials` object.                                                                                                                                                                                                                                                                                                                            |
| credentials    | Option 1                                | object        | The definition of the `LaunchDarklyAPIKey` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 1       | api_token [*required*]             | string        | The `LaunchDarklyAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`                                                                                                                                                                                                                                                                                       |
| Option 17      | type [*required*]                  | enum          | The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`                                                                                                                                                                                                                                                                                    |
| integration    | Option 18                               | object        | The definition of the `NotionIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 18      | credentials [*required*]           |  <oneOf> | The definition of the `NotionCredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `NotionAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `NotionAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 18      | type [*required*]                  | enum          | The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`                                                                                                                                                                                                                                                                                                |
| integration    | Option 19                               | object        | The definition of the `OktaIntegration` object.                                                                                                                                                                                                                                                                                                                                    |
| Option 19      | credentials [*required*]           |  <oneOf> | The definition of the `OktaCredentials` object.                                                                                                                                                                                                                                                                                                                                    |
| credentials    | Option 1                                | object        | The definition of the `OktaAPIToken` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OktaAPIToken` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | domain [*required*]                | string        | The `OktaAPIToken` `domain`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`                                                                                                                                                                                                                                                                                                   |
| Option 19      | type [*required*]                  | enum          | The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`                                                                                                                                                                                                                                                                                                    |
| integration    | Option 20                               | object        | The definition of the `OpenAIIntegration` object.                                                                                                                                                                                                                                                                                                                                  |
| Option 20      | credentials [*required*]           |  <oneOf> | The definition of the `OpenAICredentials` object.                                                                                                                                                                                                                                                                                                                                  |
| credentials    | Option 1                                | object        | The definition of the `OpenAIAPIKey` object.                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | api_token [*required*]             | string        | The `OpenAIAPIKey` `api_token`.                                                                                                                                                                                                                                                                                                                                                    |
| Option 1       | type [*required*]                  | enum          | The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`                                                                                                                                                                                                                                                                                                   |
| Option 20      | type [*required*]                  | enum          | The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`                                                                                                                                                                                                                                                                                                |
| integration    | Option 21                               | object        | The definition of the `ServiceNowIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 21      | credentials [*required*]           |  <oneOf> | The definition of the `ServiceNowCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `ServiceNowBasicAuth` object.                                                                                                                                                                                                                                                                                                                                |
| Option 1       | instance [*required*]              | string        | The `ServiceNowBasicAuth` `instance`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | password [*required*]              | string        | The `ServiceNowBasicAuth` `password`.                                                                                                                                                                                                                                                                                                                                              |
| Option 1       | type [*required*]                  | enum          | The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`                                                                                                                                                                                                                                                                                     |
| Option 1       | username [*required*]              | string        | The `ServiceNowBasicAuth` `username`.                                                                                                                                                                                                                                                                                                                                              |
| Option 21      | type [*required*]                  | enum          | The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`                                                                                                                                                                                                                                                                                        |
| integration    | Option 22                               | object        | The definition of the `SplitIntegration` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 22      | credentials [*required*]           |  <oneOf> | The definition of the `SplitCredentials` object.                                                                                                                                                                                                                                                                                                                                   |
| credentials    | Option 1                                | object        | The definition of the `SplitAPIKey` object.                                                                                                                                                                                                                                                                                                                                        |
| Option 1       | api_key [*required*]               | string        | The `SplitAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                       |
| Option 1       | type [*required*]                  | enum          | The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`                                                                                                                                                                                                                                                                                                     |
| Option 22      | type [*required*]                  | enum          | The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`                                                                                                                                                                                                                                                                                                  |
| integration    | Option 23                               | object        | The definition of the `StatsigIntegration` object.                                                                                                                                                                                                                                                                                                                                 |
| Option 23      | credentials [*required*]           |  <oneOf> | The definition of the `StatsigCredentials` object.                                                                                                                                                                                                                                                                                                                                 |
| credentials    | Option 1                                | object        | The definition of the `StatsigAPIKey` object.                                                                                                                                                                                                                                                                                                                                      |
| Option 1       | api_key [*required*]               | string        | The `StatsigAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1       | type [*required*]                  | enum          | The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`                                                                                                                                                                                                                                                                                                 |
| Option 23      | type [*required*]                  | enum          | The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`                                                                                                                                                                                                                                                                                              |
| integration    | Option 24                               | object        | The definition of the `VirusTotalIntegration` object.                                                                                                                                                                                                                                                                                                                              |
| Option 24      | credentials [*required*]           |  <oneOf> | The definition of the `VirusTotalCredentials` object.                                                                                                                                                                                                                                                                                                                              |
| credentials    | Option 1                                | object        | The definition of the `VirusTotalAPIKey` object.                                                                                                                                                                                                                                                                                                                                   |
| Option 1       | api_key [*required*]               | string        | The `VirusTotalAPIKey` `api_key`.                                                                                                                                                                                                                                                                                                                                                  |
| Option 1       | type [*required*]                  | enum          | The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`                                                                                                                                                                                                                                                                                           |
| Option 24      | type [*required*]                  | enum          | The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`                                                                                                                                                                                                                                                                                        |
| attributes     | name [*required*]                  | string        | Name of the connection                                                                                                                                                                                                                                                                                                                                                             |
| data           | id                                      | string        | The connection identifier                                                                                                                                                                                                                                                                                                                                                          |
| data           | type [*required*]                  | enum          | The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`                                                                                                                                                                                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "integration": {
        "credentials": {
          "account_id": "111222333444",
          "external_id": "33a1011635c44b38a064cf14e82e1d8f",
          "principal_id": "123456789012",
          "role": "my-role",
          "type": "AWSAssumeRole"
        },
        "type": "AWS"
      },
      "name": "My AWS Connection"
    },
    "id": "string",
    "type": "action_connection"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too Many Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Path parametersexport connection_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections/${connection_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "action_connection",
    "attributes": {
      "name": "Cassette Connection",
      "integration": {
        "type": "AWS",
        "credentials": {
          "type": "AWSAssumeRole",
          "role": "MyRoleUpdated",
          "account_id": "123456789123"
        }
      }
    }
  }
}
EOF

#####

```go
// Update an existing Action Connection returns "Successfully updated Action Connection" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.UpdateActionConnectionRequest{
        Data: datadogV2.ActionConnectionDataUpdate{
            Type: datadogV2.ACTIONCONNECTIONDATATYPE_ACTION_CONNECTION,
            Attributes: datadogV2.ActionConnectionAttributesUpdate{
                Name: datadog.PtrString("Cassette Connection"),
                Integration: &datadogV2.ActionConnectionIntegrationUpdate{
                    AWSIntegrationUpdate: &datadogV2.AWSIntegrationUpdate{
                        Type: datadogV2.AWSINTEGRATIONTYPE_AWS,
                        Credentials: &datadogV2.AWSCredentialsUpdate{
                            AWSAssumeRoleUpdate: &datadogV2.AWSAssumeRoleUpdate{
                                Type:      datadogV2.AWSASSUMEROLETYPE_AWSASSUMEROLE,
                                Role:      datadog.PtrString("MyRoleUpdated"),
                                AccountId: datadog.PtrString("123456789123"),
                            }},
                    }},
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    resp, r, err := api.UpdateActionConnection(ctx, "cb460d51-3c88-4e87-adac-d47131d0423d", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.UpdateActionConnection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ActionConnectionApi.UpdateActionConnection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update an existing Action Connection returns "Successfully updated Action Connection" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;
import com.datadog.api.client.v2.model.AWSAssumeRoleType;
import com.datadog.api.client.v2.model.AWSAssumeRoleUpdate;
import com.datadog.api.client.v2.model.AWSCredentialsUpdate;
import com.datadog.api.client.v2.model.AWSIntegrationType;
import com.datadog.api.client.v2.model.AWSIntegrationUpdate;
import com.datadog.api.client.v2.model.ActionConnectionAttributesUpdate;
import com.datadog.api.client.v2.model.ActionConnectionDataType;
import com.datadog.api.client.v2.model.ActionConnectionDataUpdate;
import com.datadog.api.client.v2.model.ActionConnectionIntegrationUpdate;
import com.datadog.api.client.v2.model.UpdateActionConnectionRequest;
import com.datadog.api.client.v2.model.UpdateActionConnectionResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    UpdateActionConnectionRequest body =
        new UpdateActionConnectionRequest()
            .data(
                new ActionConnectionDataUpdate()
                    .type(ActionConnectionDataType.ACTION_CONNECTION)
                    .attributes(
                        new ActionConnectionAttributesUpdate()
                            .name("Cassette Connection")
                            .integration(
                                new ActionConnectionIntegrationUpdate(
                                    new AWSIntegrationUpdate()
                                        .type(AWSIntegrationType.AWS)
                                        .credentials(
                                            new AWSCredentialsUpdate(
                                                new AWSAssumeRoleUpdate()
                                                    .type(AWSAssumeRoleType.AWSASSUMEROLE)
                                                    .role("MyRoleUpdated")
                                                    .accountId("123456789123")))))));

    try {
      UpdateActionConnectionResponse result =
          apiInstance.updateActionConnection("cb460d51-3c88-4e87-adac-d47131d0423d", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#updateActionConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
"""
Update an existing Action Connection returns "Successfully updated Action Connection" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes_update import ActionConnectionAttributesUpdate
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.action_connection_data_update import ActionConnectionDataUpdate
from datadog_api_client.v2.model.aws_assume_role_type import AWSAssumeRoleType
from datadog_api_client.v2.model.aws_assume_role_update import AWSAssumeRoleUpdate
from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType
from datadog_api_client.v2.model.aws_integration_update import AWSIntegrationUpdate
from datadog_api_client.v2.model.update_action_connection_request import UpdateActionConnectionRequest

body = UpdateActionConnectionRequest(
    data=ActionConnectionDataUpdate(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributesUpdate(
            name="Cassette Connection",
            integration=AWSIntegrationUpdate(
                type=AWSIntegrationType.AWS,
                credentials=AWSAssumeRoleUpdate(
                    type=AWSAssumeRoleType.AWSASSUMEROLE,
                    role="MyRoleUpdated",
                    account_id="123456789123",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.update_action_connection(connection_id="cb460d51-3c88-4e87-adac-d47131d0423d", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update an existing Action Connection returns "Successfully updated Action Connection" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new

body = DatadogAPIClient::V2::UpdateActionConnectionRequest.new({
  data: DatadogAPIClient::V2::ActionConnectionDataUpdate.new({
    type: DatadogAPIClient::V2::ActionConnectionDataType::ACTION_CONNECTION,
    attributes: DatadogAPIClient::V2::ActionConnectionAttributesUpdate.new({
      name: "Cassette Connection",
      integration: DatadogAPIClient::V2::AWSIntegrationUpdate.new({
        type: DatadogAPIClient::V2::AWSIntegrationType::AWS,
        credentials: DatadogAPIClient::V2::AWSAssumeRoleUpdate.new({
          type: DatadogAPIClient::V2::AWSAssumeRoleType::AWSASSUMEROLE,
          role: "MyRoleUpdated",
          account_id: "123456789123",
        }),
      }),
    }),
  }),
})
p api_instance.update_action_connection("cb460d51-3c88-4e87-adac-d47131d0423d", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update an existing Action Connection returns "Successfully updated Action
// Connection" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;
use datadog_api_client::datadogV2::model::AWSAssumeRoleType;
use datadog_api_client::datadogV2::model::AWSAssumeRoleUpdate;
use datadog_api_client::datadogV2::model::AWSCredentialsUpdate;
use datadog_api_client::datadogV2::model::AWSIntegrationType;
use datadog_api_client::datadogV2::model::AWSIntegrationUpdate;
use datadog_api_client::datadogV2::model::ActionConnectionAttributesUpdate;
use datadog_api_client::datadogV2::model::ActionConnectionDataType;
use datadog_api_client::datadogV2::model::ActionConnectionDataUpdate;
use datadog_api_client::datadogV2::model::ActionConnectionIntegrationUpdate;
use datadog_api_client::datadogV2::model::UpdateActionConnectionRequest;

#[tokio::main]
async fn main() {
    let body = UpdateActionConnectionRequest::new(ActionConnectionDataUpdate::new(
        ActionConnectionAttributesUpdate::new()
            .integration(ActionConnectionIntegrationUpdate::AWSIntegrationUpdate(
                Box::new(
                    AWSIntegrationUpdate::new(AWSIntegrationType::AWS).credentials(
                        AWSCredentialsUpdate::AWSAssumeRoleUpdate(Box::new(
                            AWSAssumeRoleUpdate::new(AWSAssumeRoleType::AWSASSUMEROLE)
                                .account_id("123456789123".to_string())
                                .role("MyRoleUpdated".to_string()),
                        )),
                    ),
                ),
            ))
            .name("Cassette Connection".to_string()),
        ActionConnectionDataType::ACTION_CONNECTION,
    ));
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api
        .update_action_connection("cb460d51-3c88-4e87-adac-d47131d0423d".to_string(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Update an existing Action Connection returns "Successfully updated Action Connection" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

const params: v2.ActionConnectionApiUpdateActionConnectionRequest = {
  body: {
    data: {
      type: "action_connection",
      attributes: {
        name: "Cassette Connection",
        integration: {
          type: "AWS",
          credentials: {
            type: "AWSAssumeRole",
            role: "MyRoleUpdated",
            accountId: "123456789123",
          },
        },
      },
    },
  },
  connectionId: "cb460d51-3c88-4e87-adac-d47131d0423d",
};

apiInstance
  .updateActionConnection(params)
  .then((data: v2.UpdateActionConnectionResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete an existing Action Connection{% #delete-an-existing-action-connection %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/actions/connections/{connection_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/actions/connections/{connection_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/actions/connections/{connection_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/actions/connections/{connection_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/actions/connections/{connection_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/actions/connections/{connection_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/actions/connections/{connection_id} |

### Overview

Delete an existing Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `connection_write` permission.

### Arguments

#### Path Parameters

| Name                            | Type   | Description                     |
| ------------------------------- | ------ | ------------------------------- |
| connection_id [*required*] | string | The ID of the action connection |

### Response

{% tab title="204" %}
The resource was deleted successfully.
{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too Many Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport connection_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections/${connection_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete an existing Action Connection returns "The resource was deleted successfully." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

# there is a valid "action_connection" in the system
ACTION_CONNECTION_DATA_ID = environ["ACTION_CONNECTION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    api_instance.delete_action_connection(
        connection_id=ACTION_CONNECTION_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete an existing Action Connection returns "The resource was deleted successfully." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new

# there is a valid "action_connection" in the system
ACTION_CONNECTION_DATA_ID = ENV["ACTION_CONNECTION_DATA_ID"]
api_instance.delete_action_connection(ACTION_CONNECTION_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete an existing Action Connection returns "The resource was deleted successfully." response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "action_connection" in the system
    ActionConnectionDataID := os.Getenv("ACTION_CONNECTION_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    r, err := api.DeleteActionConnection(ctx, ActionConnectionDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.DeleteActionConnection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete an existing Action Connection returns "The resource was deleted successfully." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    // there is a valid "action_connection" in the system
    String ACTION_CONNECTION_DATA_ID = System.getenv("ACTION_CONNECTION_DATA_ID");

    try {
      apiInstance.deleteActionConnection(ACTION_CONNECTION_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#deleteActionConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Delete an existing Action Connection returns "The resource was deleted
// successfully." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;

#[tokio::main]
async fn main() {
    // there is a valid "action_connection" in the system
    let action_connection_data_id = std::env::var("ACTION_CONNECTION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api
        .delete_action_connection(action_connection_data_id.clone())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Delete an existing Action Connection returns "The resource was deleted successfully." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

// there is a valid "action_connection" in the system
const ACTION_CONNECTION_DATA_ID = process.env
  .ACTION_CONNECTION_DATA_ID as string;

const params: v2.ActionConnectionApiDeleteActionConnectionRequest = {
  connectionId: ACTION_CONNECTION_DATA_ID,
};

apiInstance
  .deleteActionConnection(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Register a new App Key{% #register-a-new-app-key %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/actions/app_key_registrations/{app_key_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/actions/app_key_registrations/{app_key_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |

### Overview

Register a new App Key This endpoint requires any of the following permissions:
`user_access_manage``user_app_keys``service_account_write`


### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| app_key_id [*required*] | string | The ID of the app key |

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
The response object after creating an app key registration.

| Parent field | Field                  | Type   | Description                                                                                        |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------------------------------- |
|              | data                   | object | Data related to the app key registration.                                                          |
| data         | id                     | uuid   | The app key registration identifier                                                                |
| data         | type [*required*] | enum   | The definition of `AppKeyRegistrationDataType` object. Allowed enum values: `app_key_registration` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "string",
    "type": "app_key_registration"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Register a new App Key returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.register_app_key(
        app_key_id="b7feea52-994e-4714-a100-1bd9eff5aee1",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Register a new App Key returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.register_app_key("b7feea52-994e-4714-a100-1bd9eff5aee1")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Register a new App Key returns "Created" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    resp, r, err := api.RegisterAppKey(ctx, "b7feea52-994e-4714-a100-1bd9eff5aee1")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.RegisterAppKey`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ActionConnectionApi.RegisterAppKey`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Register a new App Key returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;
import com.datadog.api.client.v2.model.RegisterAppKeyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    try {
      RegisterAppKeyResponse result =
          apiInstance.registerAppKey("b7feea52-994e-4714-a100-1bd9eff5aee1");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#registerAppKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Register a new App Key returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api
        .register_app_key("b7feea52-994e-4714-a100-1bd9eff5aee1".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Register a new App Key returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

const params: v2.ActionConnectionApiRegisterAppKeyRequest = {
  appKeyId: "b7feea52-994e-4714-a100-1bd9eff5aee1",
};

apiInstance
  .registerAppKey(params)
  .then((data: v2.RegisterAppKeyResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## List App Key Registrations{% #list-app-key-registrations %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrations |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/actions/app_key_registrations |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/actions/app_key_registrations      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/actions/app_key_registrations      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/actions/app_key_registrations     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/actions/app_key_registrations |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations |

### Overview

List App Key Registrations This endpoint requires the `org_app_keys_read` permission.

### Arguments

#### Query Strings

| Name         | Type    | Description                                             |
| ------------ | ------- | ------------------------------------------------------- |
| page[size]   | integer | The number of App Key Registrations to return per page. |
| page[number] | integer | The page number to return.                              |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A paginated list of app key registrations.

| Parent field | Field                  | Type     | Description                                                                                        |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data                   | [object] | An array of app key registrations.                                                                 |
| data         | id                     | uuid     | The app key registration identifier                                                                |
| data         | type [*required*] | enum     | The definition of `AppKeyRegistrationDataType` object. Allowed enum values: `app_key_registration` |
|              | meta                   | object   | The definition of `ListAppKeyRegistrationsResponseMeta` object.                                    |
| meta         | total                  | int64    | The total number of app key registrations.                                                         |
| meta         | total_filtered         | int64    | The total number of app key registrations that match the specified filters.                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "string",
      "type": "app_key_registration"
    }
  ],
  "meta": {
    "total": 1,
    "total_filtered": 1
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List App Key Registrations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.list_app_key_registrations()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List App Key Registrations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.list_app_key_registrations()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List App Key Registrations returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    resp, r, err := api.ListAppKeyRegistrations(ctx, *datadogV2.NewListAppKeyRegistrationsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.ListAppKeyRegistrations`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ActionConnectionApi.ListAppKeyRegistrations`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List App Key Registrations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;
import com.datadog.api.client.v2.model.ListAppKeyRegistrationsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    try {
      ListAppKeyRegistrationsResponse result = apiInstance.listAppKeyRegistrations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#listAppKeyRegistrations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// List App Key Registrations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;
use datadog_api_client::datadogV2::api_action_connection::ListAppKeyRegistrationsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api
        .list_app_key_registrations(ListAppKeyRegistrationsOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * List App Key Registrations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

apiInstance
  .listAppKeyRegistrations()
  .then((data: v2.ListAppKeyRegistrationsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Unregister an App Key{% #unregister-an-app-key %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                           |
| ----------------- | -------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/actions/app_key_registrations/{app_key_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/actions/app_key_registrations/{app_key_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |

### Overview

Unregister an App Key This endpoint requires any of the following permissions:
`user_access_manage``user_app_keys``service_account_write`


### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| app_key_id [*required*] | string | The ID of the app key |

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Unregister an App Key returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    api_instance.unregister_app_key(
        app_key_id="57cc69ae-9214-4ecc-8df8-43ecc1d92d99",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Unregister an App Key returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
api_instance.unregister_app_key("57cc69ae-9214-4ecc-8df8-43ecc1d92d99")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Unregister an App Key returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    r, err := api.UnregisterAppKey(ctx, "57cc69ae-9214-4ecc-8df8-43ecc1d92d99")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.UnregisterAppKey`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Unregister an App Key returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    try {
      apiInstance.unregisterAppKey("57cc69ae-9214-4ecc-8df8-43ecc1d92d99");
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#unregisterAppKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Unregister an App Key returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api
        .unregister_app_key("57cc69ae-9214-4ecc-8df8-43ecc1d92d99".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Unregister an App Key returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

const params: v2.ActionConnectionApiUnregisterAppKeyRequest = {
  appKeyId: "57cc69ae-9214-4ecc-8df8-43ecc1d92d99",
};

apiInstance
  .unregisterAppKey(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get an existing App Key Registration{% #get-an-existing-app-key-registration %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/actions/app_key_registrations/{app_key_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/actions/app_key_registrations/{app_key_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id} |

### Overview

Get an existing App Key Registration This endpoint requires the `org_app_keys_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| app_key_id [*required*] | string | The ID of the app key |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object after getting an app key registration.

| Parent field | Field                  | Type   | Description                                                                                        |
| ------------ | ---------------------- | ------ | -------------------------------------------------------------------------------------------------- |
|              | data                   | object | Data related to the app key registration.                                                          |
| data         | id                     | uuid   | The app key registration identifier                                                                |
| data         | type [*required*] | enum   | The definition of `AppKeyRegistrationDataType` object. Allowed enum values: `app_key_registration` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "string",
    "type": "app_key_registration"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not found
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport app_key_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get an existing App Key Registration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.get_app_key_registration(
        app_key_id="b7feea52-994e-4714-a100-1bd9eff5aee1",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get an existing App Key Registration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.get_app_key_registration("b7feea52-994e-4714-a100-1bd9eff5aee1")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get an existing App Key Registration returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewActionConnectionApi(apiClient)
    resp, r, err := api.GetAppKeyRegistration(ctx, "b7feea52-994e-4714-a100-1bd9eff5aee1")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ActionConnectionApi.GetAppKeyRegistration`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ActionConnectionApi.GetAppKeyRegistration`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get an existing App Key Registration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ActionConnectionApi;
import com.datadog.api.client.v2.model.GetAppKeyRegistrationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ActionConnectionApi apiInstance = new ActionConnectionApi(defaultClient);

    try {
      GetAppKeyRegistrationResponse result =
          apiInstance.getAppKeyRegistration("b7feea52-994e-4714-a100-1bd9eff5aee1");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionConnectionApi#getAppKeyRegistration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get an existing App Key Registration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_action_connection::ActionConnectionAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ActionConnectionAPI::with_config(configuration);
    let resp = api
        .get_app_key_registration("b7feea52-994e-4714-a100-1bd9eff5aee1".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get an existing App Key Registration returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ActionConnectionApi(configuration);

const params: v2.ActionConnectionApiGetAppKeyRegistrationRequest = {
  appKeyId: "b7feea52-994e-4714-a100-1bd9eff5aee1",
};

apiInstance
  .getAppKeyRegistration(params)
  .then((data: v2.GetAppKeyRegistrationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
