# Source: https://docs.datadoghq.com/api/latest/action-connection/

# Action Connection
Action connections extend your installed integrations and allow you to take action in your third-party systems (e.g. AWS, GitLab, and Statuspage) with Datadog’s Workflow Automation and App Builder products.
Datadog’s Integrations automatically provide authentication for Slack, Microsoft Teams, PagerDuty, Opsgenie, JIRA, GitHub, and Statuspage. You do not need additional connections in order to access these tools within Workflow Automation and App Builder.
We offer granular access control for editing and resolving connections.
## [Get an existing Action Connection](https://docs.datadoghq.com/api/latest/action-connection/#get-an-existing-action-connection)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#get-an-existing-action-connection-v2)


GET https://api.ap1.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.ap2.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.datadoghq.eu/api/v2/actions/connections/{connection_id}https://api.ddog-gov.com/api/v2/actions/connections/{connection_id}https://api.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.us3.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.us5.datadoghq.com/api/v2/actions/connections/{connection_id}
### Overview
Get an existing Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key).
### Arguments
#### Path Parameters
Name
Type
Description
connection_id [_required_]
string
The ID of the action connection
### Response
  * [200](https://docs.datadoghq.com/api/latest/action-connection/#GetActionConnection-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/action-connection/#GetActionConnection-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#GetActionConnection-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/action-connection/#GetActionConnection-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#GetActionConnection-429-v2)


Successfully get Action Connection
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


The response for found connection
Field
Type
Description
data
object
Data related to the connection.
attributes [_required_]
object
The definition of `ActionConnectionAttributes` object.
integration [_required_]
<oneOf>
The definition of `ActionConnectionIntegration` object.
Option 1
object
The definition of `AWSIntegration` object.
credentials [_required_]
<oneOf>
The definition of `AWSCredentials` object.
Option 1
object
The definition of `AWSAssumeRole` object.
account_id [_required_]
string
AWS account the connection is created for
external_id
string
External ID used to scope which connection can be used to assume the role
principal_id
string
AWS account that will assume the role
role [_required_]
string
Role to assume
type [_required_]
enum
The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`
type [_required_]
enum
The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`
Option 2
object
The definition of the `AnthropicIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AnthropicCredentials` object.
Option 1
object
The definition of the `AnthropicAPIKey` object.
api_token [_required_]
string
The `AnthropicAPIKey` `api_token`.
type [_required_]
enum
The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`
type [_required_]
enum
The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`
Option 3
object
The definition of the `AsanaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AsanaCredentials` object.
Option 1
object
The definition of the `AsanaAccessToken` object.
access_token [_required_]
string
The `AsanaAccessToken` `access_token`.
type [_required_]
enum
The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`
type [_required_]
enum
The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`
Option 4
object
The definition of the `AzureIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AzureCredentials` object.
Option 1
object
The definition of the `AzureTenant` object.
app_client_id [_required_]
string
The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.
client_secret [_required_]
string
The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application’s secrets page. You can navigate to your application via the Azure Directory.
custom_scopes
string
If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.
tenant_id [_required_]
string
The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.
type [_required_]
enum
The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`
type [_required_]
enum
The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`
Option 5
object
The definition of the `CircleCIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CircleCICredentials` object.
Option 1
object
The definition of the `CircleCIAPIKey` object.
api_token [_required_]
string
The `CircleCIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`
type [_required_]
enum
The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`
Option 6
object
The definition of the `ClickupIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ClickupCredentials` object.
Option 1
object
The definition of the `ClickupAPIKey` object.
api_token [_required_]
string
The `ClickupAPIKey` `api_token`.
type [_required_]
enum
The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`
type [_required_]
enum
The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`
Option 7
object
The definition of the `CloudflareIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CloudflareCredentials` object.
Option 1
object
The definition of the `CloudflareAPIToken` object.
api_token [_required_]
string
The `CloudflareAPIToken` `api_token`.
type [_required_]
enum
The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`
Option 2
object
The definition of the `CloudflareGlobalAPIToken` object.
auth_email [_required_]
string
The `CloudflareGlobalAPIToken` `auth_email`.
global_api_key [_required_]
string
The `CloudflareGlobalAPIToken` `global_api_key`.
type [_required_]
enum
The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`
type [_required_]
enum
The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`
Option 8
object
The definition of the `ConfigCatIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ConfigCatCredentials` object.
Option 1
object
The definition of the `ConfigCatSDKKey` object.
api_password [_required_]
string
The `ConfigCatSDKKey` `api_password`.
api_username [_required_]
string
The `ConfigCatSDKKey` `api_username`.
sdk_key [_required_]
string
The `ConfigCatSDKKey` `sdk_key`.
type [_required_]
enum
The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`
type [_required_]
enum
The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`
Option 9
object
The definition of the `DatadogIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `DatadogCredentials` object.
Option 1
object
The definition of the `DatadogAPIKey` object.
api_key [_required_]
string
The `DatadogAPIKey` `api_key`.
app_key [_required_]
string
The `DatadogAPIKey` `app_key`.
datacenter [_required_]
string
The `DatadogAPIKey` `datacenter`.
subdomain
string
Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see <https://docs.datadoghq.com/getting_started/site>).
type [_required_]
enum
The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`
type [_required_]
enum
The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`
Option 10
object
The definition of the `FastlyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FastlyCredentials` object.
Option 1
object
The definition of the `FastlyAPIKey` object.
api_key [_required_]
string
The `FastlyAPIKey` `api_key`.
type [_required_]
enum
The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`
type [_required_]
enum
The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`
Option 11
object
The definition of the `FreshserviceIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FreshserviceCredentials` object.
Option 1
object
The definition of the `FreshserviceAPIKey` object.
api_key [_required_]
string
The `FreshserviceAPIKey` `api_key`.
domain [_required_]
string
The `FreshserviceAPIKey` `domain`.
type [_required_]
enum
The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`
type [_required_]
enum
The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`
Option 12
object
The definition of the `GCPIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GCPCredentials` object.
Option 1
object
The definition of the `GCPServiceAccount` object.
private_key [_required_]
string
The `GCPServiceAccount` `private_key`.
service_account_email [_required_]
string
The `GCPServiceAccount` `service_account_email`.
type [_required_]
enum
The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`
type [_required_]
enum
The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`
Option 13
object
The definition of the `GeminiIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GeminiCredentials` object.
Option 1
object
The definition of the `GeminiAPIKey` object.
api_key [_required_]
string
The `GeminiAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`
type [_required_]
enum
The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`
Option 14
object
The definition of the `GitlabIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GitlabCredentials` object.
Option 1
object
The definition of the `GitlabAPIKey` object.
api_token [_required_]
string
The `GitlabAPIKey` `api_token`.
type [_required_]
enum
The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`
type [_required_]
enum
The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`
Option 15
object
The definition of the `GreyNoiseIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GreyNoiseCredentials` object.
Option 1
object
The definition of the `GreyNoiseAPIKey` object.
api_key [_required_]
string
The `GreyNoiseAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`
type [_required_]
enum
The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`
Option 16
object
The definition of `HTTPIntegration` object.
base_url [_required_]
string
Base HTTP url for the integration
credentials [_required_]
<oneOf>
The definition of `HTTPCredentials` object.
Option 1
object
The definition of `HTTPTokenAuth` object.
body
object
The definition of `HTTPBody` object.
content
string
Serialized body content
content_type
string
Content type of the body
headers
[object]
The `HTTPTokenAuth` `headers`.
name [_required_]
string
The `HTTPHeader` `name`.
value [_required_]
string
The `HTTPHeader` `value`.
tokens
[object]
The `HTTPTokenAuth` `tokens`.
name [_required_]
string
The `HTTPToken` `name`.
type [_required_]
enum
The definition of `TokenType` object. Allowed enum values: `SECRET`
value [_required_]
string
The `HTTPToken` `value`.
type [_required_]
enum
The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`
url_parameters
[object]
The `HTTPTokenAuth` `url_parameters`.
name [_required_]
string
Name for tokens.
value [_required_]
string
The `UrlParam` `value`.
type [_required_]
enum
The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`
Option 17
object
The definition of the `LaunchDarklyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `LaunchDarklyCredentials` object.
Option 1
object
The definition of the `LaunchDarklyAPIKey` object.
api_token [_required_]
string
The `LaunchDarklyAPIKey` `api_token`.
type [_required_]
enum
The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`
type [_required_]
enum
The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`
Option 18
object
The definition of the `NotionIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `NotionCredentials` object.
Option 1
object
The definition of the `NotionAPIKey` object.
api_token [_required_]
string
The `NotionAPIKey` `api_token`.
type [_required_]
enum
The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`
type [_required_]
enum
The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`
Option 19
object
The definition of the `OktaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OktaCredentials` object.
Option 1
object
The definition of the `OktaAPIToken` object.
api_token [_required_]
string
The `OktaAPIToken` `api_token`.
domain [_required_]
string
The `OktaAPIToken` `domain`.
type [_required_]
enum
The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`
type [_required_]
enum
The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`
Option 20
object
The definition of the `OpenAIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OpenAICredentials` object.
Option 1
object
The definition of the `OpenAIAPIKey` object.
api_token [_required_]
string
The `OpenAIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`
type [_required_]
enum
The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`
Option 21
object
The definition of the `ServiceNowIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ServiceNowCredentials` object.
Option 1
object
The definition of the `ServiceNowBasicAuth` object.
instance [_required_]
string
The `ServiceNowBasicAuth` `instance`.
password [_required_]
string
The `ServiceNowBasicAuth` `password`.
type [_required_]
enum
The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`
username [_required_]
string
The `ServiceNowBasicAuth` `username`.
type [_required_]
enum
The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`
Option 22
object
The definition of the `SplitIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `SplitCredentials` object.
Option 1
object
The definition of the `SplitAPIKey` object.
api_key [_required_]
string
The `SplitAPIKey` `api_key`.
type [_required_]
enum
The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`
type [_required_]
enum
The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`
Option 23
object
The definition of the `StatsigIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `StatsigCredentials` object.
Option 1
object
The definition of the `StatsigAPIKey` object.
api_key [_required_]
string
The `StatsigAPIKey` `api_key`.
type [_required_]
enum
The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`
type [_required_]
enum
The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`
Option 24
object
The definition of the `VirusTotalIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `VirusTotalCredentials` object.
Option 1
object
The definition of the `VirusTotalAPIKey` object.
api_key [_required_]
string
The `VirusTotalAPIKey` `api_key`.
type [_required_]
enum
The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`
type [_required_]
enum
The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`
name [_required_]
string
Name of the connection
id
string
The connection identifier
type [_required_]
enum
The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too Many Request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  Get an existing Action Connection
Copy
```
                  # Path parameters  
export connection_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections/${connection_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an existing Action Connection
```
# Get an existing Action Connection returns "Successfully get Action Connection" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.get_action_connection("cb460d51-3c88-4e87-adac-d47131d0423d")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a new Action Connection](https://docs.datadoghq.com/api/latest/action-connection/#create-a-new-action-connection)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#create-a-new-action-connection-v2)


POST https://api.ap1.datadoghq.com/api/v2/actions/connectionshttps://api.ap2.datadoghq.com/api/v2/actions/connectionshttps://api.datadoghq.eu/api/v2/actions/connectionshttps://api.ddog-gov.com/api/v2/actions/connectionshttps://api.datadoghq.com/api/v2/actions/connectionshttps://api.us3.datadoghq.com/api/v2/actions/connectionshttps://api.us5.datadoghq.com/api/v2/actions/connections
### Overview
Create a new Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key).
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


Field
Type
Description
data [_required_]
object
Data related to the connection.
attributes [_required_]
object
The definition of `ActionConnectionAttributes` object.
integration [_required_]
<oneOf>
The definition of `ActionConnectionIntegration` object.
Option 1
object
The definition of `AWSIntegration` object.
credentials [_required_]
<oneOf>
The definition of `AWSCredentials` object.
Option 1
object
The definition of `AWSAssumeRole` object.
account_id [_required_]
string
AWS account the connection is created for
external_id
string
External ID used to scope which connection can be used to assume the role
principal_id
string
AWS account that will assume the role
role [_required_]
string
Role to assume
type [_required_]
enum
The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`
type [_required_]
enum
The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`
Option 2
object
The definition of the `AnthropicIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AnthropicCredentials` object.
Option 1
object
The definition of the `AnthropicAPIKey` object.
api_token [_required_]
string
The `AnthropicAPIKey` `api_token`.
type [_required_]
enum
The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`
type [_required_]
enum
The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`
Option 3
object
The definition of the `AsanaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AsanaCredentials` object.
Option 1
object
The definition of the `AsanaAccessToken` object.
access_token [_required_]
string
The `AsanaAccessToken` `access_token`.
type [_required_]
enum
The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`
type [_required_]
enum
The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`
Option 4
object
The definition of the `AzureIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AzureCredentials` object.
Option 1
object
The definition of the `AzureTenant` object.
app_client_id [_required_]
string
The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.
client_secret [_required_]
string
The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application’s secrets page. You can navigate to your application via the Azure Directory.
custom_scopes
string
If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.
tenant_id [_required_]
string
The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.
type [_required_]
enum
The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`
type [_required_]
enum
The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`
Option 5
object
The definition of the `CircleCIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CircleCICredentials` object.
Option 1
object
The definition of the `CircleCIAPIKey` object.
api_token [_required_]
string
The `CircleCIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`
type [_required_]
enum
The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`
Option 6
object
The definition of the `ClickupIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ClickupCredentials` object.
Option 1
object
The definition of the `ClickupAPIKey` object.
api_token [_required_]
string
The `ClickupAPIKey` `api_token`.
type [_required_]
enum
The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`
type [_required_]
enum
The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`
Option 7
object
The definition of the `CloudflareIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CloudflareCredentials` object.
Option 1
object
The definition of the `CloudflareAPIToken` object.
api_token [_required_]
string
The `CloudflareAPIToken` `api_token`.
type [_required_]
enum
The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`
Option 2
object
The definition of the `CloudflareGlobalAPIToken` object.
auth_email [_required_]
string
The `CloudflareGlobalAPIToken` `auth_email`.
global_api_key [_required_]
string
The `CloudflareGlobalAPIToken` `global_api_key`.
type [_required_]
enum
The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`
type [_required_]
enum
The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`
Option 8
object
The definition of the `ConfigCatIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ConfigCatCredentials` object.
Option 1
object
The definition of the `ConfigCatSDKKey` object.
api_password [_required_]
string
The `ConfigCatSDKKey` `api_password`.
api_username [_required_]
string
The `ConfigCatSDKKey` `api_username`.
sdk_key [_required_]
string
The `ConfigCatSDKKey` `sdk_key`.
type [_required_]
enum
The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`
type [_required_]
enum
The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`
Option 9
object
The definition of the `DatadogIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `DatadogCredentials` object.
Option 1
object
The definition of the `DatadogAPIKey` object.
api_key [_required_]
string
The `DatadogAPIKey` `api_key`.
app_key [_required_]
string
The `DatadogAPIKey` `app_key`.
datacenter [_required_]
string
The `DatadogAPIKey` `datacenter`.
subdomain
string
Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see <https://docs.datadoghq.com/getting_started/site>).
type [_required_]
enum
The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`
type [_required_]
enum
The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`
Option 10
object
The definition of the `FastlyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FastlyCredentials` object.
Option 1
object
The definition of the `FastlyAPIKey` object.
api_key [_required_]
string
The `FastlyAPIKey` `api_key`.
type [_required_]
enum
The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`
type [_required_]
enum
The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`
Option 11
object
The definition of the `FreshserviceIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FreshserviceCredentials` object.
Option 1
object
The definition of the `FreshserviceAPIKey` object.
api_key [_required_]
string
The `FreshserviceAPIKey` `api_key`.
domain [_required_]
string
The `FreshserviceAPIKey` `domain`.
type [_required_]
enum
The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`
type [_required_]
enum
The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`
Option 12
object
The definition of the `GCPIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GCPCredentials` object.
Option 1
object
The definition of the `GCPServiceAccount` object.
private_key [_required_]
string
The `GCPServiceAccount` `private_key`.
service_account_email [_required_]
string
The `GCPServiceAccount` `service_account_email`.
type [_required_]
enum
The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`
type [_required_]
enum
The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`
Option 13
object
The definition of the `GeminiIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GeminiCredentials` object.
Option 1
object
The definition of the `GeminiAPIKey` object.
api_key [_required_]
string
The `GeminiAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`
type [_required_]
enum
The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`
Option 14
object
The definition of the `GitlabIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GitlabCredentials` object.
Option 1
object
The definition of the `GitlabAPIKey` object.
api_token [_required_]
string
The `GitlabAPIKey` `api_token`.
type [_required_]
enum
The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`
type [_required_]
enum
The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`
Option 15
object
The definition of the `GreyNoiseIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GreyNoiseCredentials` object.
Option 1
object
The definition of the `GreyNoiseAPIKey` object.
api_key [_required_]
string
The `GreyNoiseAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`
type [_required_]
enum
The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`
Option 16
object
The definition of `HTTPIntegration` object.
base_url [_required_]
string
Base HTTP url for the integration
credentials [_required_]
<oneOf>
The definition of `HTTPCredentials` object.
Option 1
object
The definition of `HTTPTokenAuth` object.
body
object
The definition of `HTTPBody` object.
content
string
Serialized body content
content_type
string
Content type of the body
headers
[object]
The `HTTPTokenAuth` `headers`.
name [_required_]
string
The `HTTPHeader` `name`.
value [_required_]
string
The `HTTPHeader` `value`.
tokens
[object]
The `HTTPTokenAuth` `tokens`.
name [_required_]
string
The `HTTPToken` `name`.
type [_required_]
enum
The definition of `TokenType` object. Allowed enum values: `SECRET`
value [_required_]
string
The `HTTPToken` `value`.
type [_required_]
enum
The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`
url_parameters
[object]
The `HTTPTokenAuth` `url_parameters`.
name [_required_]
string
Name for tokens.
value [_required_]
string
The `UrlParam` `value`.
type [_required_]
enum
The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`
Option 17
object
The definition of the `LaunchDarklyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `LaunchDarklyCredentials` object.
Option 1
object
The definition of the `LaunchDarklyAPIKey` object.
api_token [_required_]
string
The `LaunchDarklyAPIKey` `api_token`.
type [_required_]
enum
The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`
type [_required_]
enum
The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`
Option 18
object
The definition of the `NotionIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `NotionCredentials` object.
Option 1
object
The definition of the `NotionAPIKey` object.
api_token [_required_]
string
The `NotionAPIKey` `api_token`.
type [_required_]
enum
The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`
type [_required_]
enum
The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`
Option 19
object
The definition of the `OktaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OktaCredentials` object.
Option 1
object
The definition of the `OktaAPIToken` object.
api_token [_required_]
string
The `OktaAPIToken` `api_token`.
domain [_required_]
string
The `OktaAPIToken` `domain`.
type [_required_]
enum
The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`
type [_required_]
enum
The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`
Option 20
object
The definition of the `OpenAIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OpenAICredentials` object.
Option 1
object
The definition of the `OpenAIAPIKey` object.
api_token [_required_]
string
The `OpenAIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`
type [_required_]
enum
The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`
Option 21
object
The definition of the `ServiceNowIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ServiceNowCredentials` object.
Option 1
object
The definition of the `ServiceNowBasicAuth` object.
instance [_required_]
string
The `ServiceNowBasicAuth` `instance`.
password [_required_]
string
The `ServiceNowBasicAuth` `password`.
type [_required_]
enum
The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`
username [_required_]
string
The `ServiceNowBasicAuth` `username`.
type [_required_]
enum
The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`
Option 22
object
The definition of the `SplitIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `SplitCredentials` object.
Option 1
object
The definition of the `SplitAPIKey` object.
api_key [_required_]
string
The `SplitAPIKey` `api_key`.
type [_required_]
enum
The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`
type [_required_]
enum
The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`
Option 23
object
The definition of the `StatsigIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `StatsigCredentials` object.
Option 1
object
The definition of the `StatsigAPIKey` object.
api_key [_required_]
string
The `StatsigAPIKey` `api_key`.
type [_required_]
enum
The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`
type [_required_]
enum
The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`
Option 24
object
The definition of the `VirusTotalIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `VirusTotalCredentials` object.
Option 1
object
The definition of the `VirusTotalAPIKey` object.
api_key [_required_]
string
The `VirusTotalAPIKey` `api_key`.
type [_required_]
enum
The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`
type [_required_]
enum
The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`
name [_required_]
string
Name of the connection
id
string
The connection identifier
type [_required_]
enum
The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/action-connection/#CreateActionConnection-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/action-connection/#CreateActionConnection-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#CreateActionConnection-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#CreateActionConnection-429-v2)


Successfully created Action Connection
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


The response for a created connection
Field
Type
Description
data
object
Data related to the connection.
attributes [_required_]
object
The definition of `ActionConnectionAttributes` object.
integration [_required_]
<oneOf>
The definition of `ActionConnectionIntegration` object.
Option 1
object
The definition of `AWSIntegration` object.
credentials [_required_]
<oneOf>
The definition of `AWSCredentials` object.
Option 1
object
The definition of `AWSAssumeRole` object.
account_id [_required_]
string
AWS account the connection is created for
external_id
string
External ID used to scope which connection can be used to assume the role
principal_id
string
AWS account that will assume the role
role [_required_]
string
Role to assume
type [_required_]
enum
The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`
type [_required_]
enum
The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`
Option 2
object
The definition of the `AnthropicIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AnthropicCredentials` object.
Option 1
object
The definition of the `AnthropicAPIKey` object.
api_token [_required_]
string
The `AnthropicAPIKey` `api_token`.
type [_required_]
enum
The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`
type [_required_]
enum
The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`
Option 3
object
The definition of the `AsanaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AsanaCredentials` object.
Option 1
object
The definition of the `AsanaAccessToken` object.
access_token [_required_]
string
The `AsanaAccessToken` `access_token`.
type [_required_]
enum
The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`
type [_required_]
enum
The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`
Option 4
object
The definition of the `AzureIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AzureCredentials` object.
Option 1
object
The definition of the `AzureTenant` object.
app_client_id [_required_]
string
The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.
client_secret [_required_]
string
The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application’s secrets page. You can navigate to your application via the Azure Directory.
custom_scopes
string
If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.
tenant_id [_required_]
string
The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.
type [_required_]
enum
The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`
type [_required_]
enum
The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`
Option 5
object
The definition of the `CircleCIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CircleCICredentials` object.
Option 1
object
The definition of the `CircleCIAPIKey` object.
api_token [_required_]
string
The `CircleCIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`
type [_required_]
enum
The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`
Option 6
object
The definition of the `ClickupIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ClickupCredentials` object.
Option 1
object
The definition of the `ClickupAPIKey` object.
api_token [_required_]
string
The `ClickupAPIKey` `api_token`.
type [_required_]
enum
The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`
type [_required_]
enum
The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`
Option 7
object
The definition of the `CloudflareIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CloudflareCredentials` object.
Option 1
object
The definition of the `CloudflareAPIToken` object.
api_token [_required_]
string
The `CloudflareAPIToken` `api_token`.
type [_required_]
enum
The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`
Option 2
object
The definition of the `CloudflareGlobalAPIToken` object.
auth_email [_required_]
string
The `CloudflareGlobalAPIToken` `auth_email`.
global_api_key [_required_]
string
The `CloudflareGlobalAPIToken` `global_api_key`.
type [_required_]
enum
The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`
type [_required_]
enum
The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`
Option 8
object
The definition of the `ConfigCatIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ConfigCatCredentials` object.
Option 1
object
The definition of the `ConfigCatSDKKey` object.
api_password [_required_]
string
The `ConfigCatSDKKey` `api_password`.
api_username [_required_]
string
The `ConfigCatSDKKey` `api_username`.
sdk_key [_required_]
string
The `ConfigCatSDKKey` `sdk_key`.
type [_required_]
enum
The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`
type [_required_]
enum
The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`
Option 9
object
The definition of the `DatadogIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `DatadogCredentials` object.
Option 1
object
The definition of the `DatadogAPIKey` object.
api_key [_required_]
string
The `DatadogAPIKey` `api_key`.
app_key [_required_]
string
The `DatadogAPIKey` `app_key`.
datacenter [_required_]
string
The `DatadogAPIKey` `datacenter`.
subdomain
string
Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see <https://docs.datadoghq.com/getting_started/site>).
type [_required_]
enum
The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`
type [_required_]
enum
The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`
Option 10
object
The definition of the `FastlyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FastlyCredentials` object.
Option 1
object
The definition of the `FastlyAPIKey` object.
api_key [_required_]
string
The `FastlyAPIKey` `api_key`.
type [_required_]
enum
The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`
type [_required_]
enum
The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`
Option 11
object
The definition of the `FreshserviceIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FreshserviceCredentials` object.
Option 1
object
The definition of the `FreshserviceAPIKey` object.
api_key [_required_]
string
The `FreshserviceAPIKey` `api_key`.
domain [_required_]
string
The `FreshserviceAPIKey` `domain`.
type [_required_]
enum
The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`
type [_required_]
enum
The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`
Option 12
object
The definition of the `GCPIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GCPCredentials` object.
Option 1
object
The definition of the `GCPServiceAccount` object.
private_key [_required_]
string
The `GCPServiceAccount` `private_key`.
service_account_email [_required_]
string
The `GCPServiceAccount` `service_account_email`.
type [_required_]
enum
The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`
type [_required_]
enum
The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`
Option 13
object
The definition of the `GeminiIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GeminiCredentials` object.
Option 1
object
The definition of the `GeminiAPIKey` object.
api_key [_required_]
string
The `GeminiAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`
type [_required_]
enum
The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`
Option 14
object
The definition of the `GitlabIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GitlabCredentials` object.
Option 1
object
The definition of the `GitlabAPIKey` object.
api_token [_required_]
string
The `GitlabAPIKey` `api_token`.
type [_required_]
enum
The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`
type [_required_]
enum
The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`
Option 15
object
The definition of the `GreyNoiseIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GreyNoiseCredentials` object.
Option 1
object
The definition of the `GreyNoiseAPIKey` object.
api_key [_required_]
string
The `GreyNoiseAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`
type [_required_]
enum
The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`
Option 16
object
The definition of `HTTPIntegration` object.
base_url [_required_]
string
Base HTTP url for the integration
credentials [_required_]
<oneOf>
The definition of `HTTPCredentials` object.
Option 1
object
The definition of `HTTPTokenAuth` object.
body
object
The definition of `HTTPBody` object.
content
string
Serialized body content
content_type
string
Content type of the body
headers
[object]
The `HTTPTokenAuth` `headers`.
name [_required_]
string
The `HTTPHeader` `name`.
value [_required_]
string
The `HTTPHeader` `value`.
tokens
[object]
The `HTTPTokenAuth` `tokens`.
name [_required_]
string
The `HTTPToken` `name`.
type [_required_]
enum
The definition of `TokenType` object. Allowed enum values: `SECRET`
value [_required_]
string
The `HTTPToken` `value`.
type [_required_]
enum
The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`
url_parameters
[object]
The `HTTPTokenAuth` `url_parameters`.
name [_required_]
string
Name for tokens.
value [_required_]
string
The `UrlParam` `value`.
type [_required_]
enum
The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`
Option 17
object
The definition of the `LaunchDarklyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `LaunchDarklyCredentials` object.
Option 1
object
The definition of the `LaunchDarklyAPIKey` object.
api_token [_required_]
string
The `LaunchDarklyAPIKey` `api_token`.
type [_required_]
enum
The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`
type [_required_]
enum
The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`
Option 18
object
The definition of the `NotionIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `NotionCredentials` object.
Option 1
object
The definition of the `NotionAPIKey` object.
api_token [_required_]
string
The `NotionAPIKey` `api_token`.
type [_required_]
enum
The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`
type [_required_]
enum
The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`
Option 19
object
The definition of the `OktaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OktaCredentials` object.
Option 1
object
The definition of the `OktaAPIToken` object.
api_token [_required_]
string
The `OktaAPIToken` `api_token`.
domain [_required_]
string
The `OktaAPIToken` `domain`.
type [_required_]
enum
The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`
type [_required_]
enum
The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`
Option 20
object
The definition of the `OpenAIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OpenAICredentials` object.
Option 1
object
The definition of the `OpenAIAPIKey` object.
api_token [_required_]
string
The `OpenAIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`
type [_required_]
enum
The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`
Option 21
object
The definition of the `ServiceNowIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ServiceNowCredentials` object.
Option 1
object
The definition of the `ServiceNowBasicAuth` object.
instance [_required_]
string
The `ServiceNowBasicAuth` `instance`.
password [_required_]
string
The `ServiceNowBasicAuth` `password`.
type [_required_]
enum
The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`
username [_required_]
string
The `ServiceNowBasicAuth` `username`.
type [_required_]
enum
The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`
Option 22
object
The definition of the `SplitIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `SplitCredentials` object.
Option 1
object
The definition of the `SplitAPIKey` object.
api_key [_required_]
string
The `SplitAPIKey` `api_key`.
type [_required_]
enum
The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`
type [_required_]
enum
The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`
Option 23
object
The definition of the `StatsigIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `StatsigCredentials` object.
Option 1
object
The definition of the `StatsigAPIKey` object.
api_key [_required_]
string
The `StatsigAPIKey` `api_key`.
type [_required_]
enum
The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`
type [_required_]
enum
The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`
Option 24
object
The definition of the `VirusTotalIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `VirusTotalCredentials` object.
Option 1
object
The definition of the `VirusTotalAPIKey` object.
api_key [_required_]
string
The `VirusTotalAPIKey` `api_key`.
type [_required_]
enum
The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`
type [_required_]
enum
The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`
name [_required_]
string
Name of the connection
id
string
The connection identifier
type [_required_]
enum
The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too Many Request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  Create a new Action Connection returns "Successfully created Action Connection" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections" \
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

                        
```

#####  Create a new Action Connection returns "Successfully created Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a new Action Connection returns "Successfully created Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a new Action Connection returns "Successfully created Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a new Action Connection returns "Successfully created Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a new Action Connection returns "Successfully created Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a new Action Connection returns "Successfully created Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update an existing Action Connection](https://docs.datadoghq.com/api/latest/action-connection/#update-an-existing-action-connection)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#update-an-existing-action-connection-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.ap2.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.datadoghq.eu/api/v2/actions/connections/{connection_id}https://api.ddog-gov.com/api/v2/actions/connections/{connection_id}https://api.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.us3.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.us5.datadoghq.com/api/v2/actions/connections/{connection_id}
### Overview
Update an existing Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key).
### Arguments
#### Path Parameters
Name
Type
Description
connection_id [_required_]
string
The ID of the action connection
### Request
#### Body Data (required)
Update an existing Action Connection request body
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


Field
Type
Description
data [_required_]
object
Data related to the connection update.
attributes [_required_]
object
The definition of `ActionConnectionAttributesUpdate` object.
integration
<oneOf>
The definition of `ActionConnectionIntegrationUpdate` object.
Option 1
object
The definition of `AWSIntegrationUpdate` object.
credentials
<oneOf>
The definition of `AWSCredentialsUpdate` object.
Option 1
object
The definition of `AWSAssumeRoleUpdate` object.
account_id
string
AWS account the connection is created for
generate_new_external_id
boolean
The `AWSAssumeRoleUpdate` `generate_new_external_id`.
role
string
Role to assume
type [_required_]
enum
The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`
type [_required_]
enum
The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`
Option 2
object
The definition of the `AnthropicIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `AnthropicCredentialsUpdate` object.
Option 1
object
The definition of the `AnthropicAPIKey` object.
api_token
string
The `AnthropicAPIKeyUpdate` `api_token`.
type [_required_]
enum
The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`
type [_required_]
enum
The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`
Option 3
object
The definition of the `AsanaIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `AsanaCredentialsUpdate` object.
Option 1
object
The definition of the `AsanaAccessToken` object.
access_token
string
The `AsanaAccessTokenUpdate` `access_token`.
type [_required_]
enum
The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`
type [_required_]
enum
The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`
Option 4
object
The definition of the `AzureIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `AzureCredentialsUpdate` object.
Option 1
object
The definition of the `AzureTenant` object.
app_client_id
string
The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.
client_secret
string
The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application’s secrets page. You can navigate to your application via the Azure Directory.
custom_scopes
string
If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.
tenant_id
string
The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.
type [_required_]
enum
The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`
type [_required_]
enum
The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`
Option 5
object
The definition of the `CircleCIIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `CircleCICredentialsUpdate` object.
Option 1
object
The definition of the `CircleCIAPIKey` object.
api_token
string
The `CircleCIAPIKeyUpdate` `api_token`.
type [_required_]
enum
The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`
type [_required_]
enum
The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`
Option 6
object
The definition of the `ClickupIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `ClickupCredentialsUpdate` object.
Option 1
object
The definition of the `ClickupAPIKey` object.
api_token
string
The `ClickupAPIKeyUpdate` `api_token`.
type [_required_]
enum
The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`
type [_required_]
enum
The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`
Option 7
object
The definition of the `CloudflareIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `CloudflareCredentialsUpdate` object.
Option 1
object
The definition of the `CloudflareAPIToken` object.
api_token
string
The `CloudflareAPITokenUpdate` `api_token`.
type [_required_]
enum
The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`
Option 2
object
The definition of the `CloudflareGlobalAPIToken` object.
auth_email
string
The `CloudflareGlobalAPITokenUpdate` `auth_email`.
global_api_key
string
The `CloudflareGlobalAPITokenUpdate` `global_api_key`.
type [_required_]
enum
The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`
type [_required_]
enum
The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`
Option 8
object
The definition of the `ConfigCatIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `ConfigCatCredentialsUpdate` object.
Option 1
object
The definition of the `ConfigCatSDKKey` object.
api_password
string
The `ConfigCatSDKKeyUpdate` `api_password`.
api_username
string
The `ConfigCatSDKKeyUpdate` `api_username`.
sdk_key
string
The `ConfigCatSDKKeyUpdate` `sdk_key`.
type [_required_]
enum
The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`
type [_required_]
enum
The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`
Option 9
object
The definition of the `DatadogIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `DatadogCredentialsUpdate` object.
Option 1
object
The definition of the `DatadogAPIKey` object.
api_key
string
The `DatadogAPIKeyUpdate` `api_key`.
app_key
string
The `DatadogAPIKeyUpdate` `app_key`.
datacenter
string
The `DatadogAPIKeyUpdate` `datacenter`.
subdomain
string
Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see <https://docs.datadoghq.com/getting_started/site>).
type [_required_]
enum
The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`
type [_required_]
enum
The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`
Option 10
object
The definition of the `FastlyIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `FastlyCredentialsUpdate` object.
Option 1
object
The definition of the `FastlyAPIKey` object.
api_key
string
The `FastlyAPIKeyUpdate` `api_key`.
type [_required_]
enum
The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`
type [_required_]
enum
The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`
Option 11
object
The definition of the `FreshserviceIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `FreshserviceCredentialsUpdate` object.
Option 1
object
The definition of the `FreshserviceAPIKey` object.
api_key
string
The `FreshserviceAPIKeyUpdate` `api_key`.
domain
string
The `FreshserviceAPIKeyUpdate` `domain`.
type [_required_]
enum
The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`
type [_required_]
enum
The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`
Option 12
object
The definition of the `GCPIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `GCPCredentialsUpdate` object.
Option 1
object
The definition of the `GCPServiceAccount` object.
private_key
string
The `GCPServiceAccountUpdate` `private_key`.
service_account_email
string
The `GCPServiceAccountUpdate` `service_account_email`.
type [_required_]
enum
The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`
type [_required_]
enum
The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`
Option 13
object
The definition of the `GeminiIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `GeminiCredentialsUpdate` object.
Option 1
object
The definition of the `GeminiAPIKey` object.
api_key
string
The `GeminiAPIKeyUpdate` `api_key`.
type [_required_]
enum
The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`
type [_required_]
enum
The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`
Option 14
object
The definition of the `GitlabIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `GitlabCredentialsUpdate` object.
Option 1
object
The definition of the `GitlabAPIKey` object.
api_token
string
The `GitlabAPIKeyUpdate` `api_token`.
type [_required_]
enum
The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`
type [_required_]
enum
The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`
Option 15
object
The definition of the `GreyNoiseIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `GreyNoiseCredentialsUpdate` object.
Option 1
object
The definition of the `GreyNoiseAPIKey` object.
api_key
string
The `GreyNoiseAPIKeyUpdate` `api_key`.
type [_required_]
enum
The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`
type [_required_]
enum
The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`
Option 16
object
The definition of `HTTPIntegrationUpdate` object.
base_url
string
Base HTTP url for the integration
credentials
<oneOf>
The definition of `HTTPCredentialsUpdate` object.
Option 1
object
The definition of `HTTPTokenAuthUpdate` object.
body
object
The definition of `HTTPBody` object.
content
string
Serialized body content
content_type
string
Content type of the body
headers
[object]
The `HTTPTokenAuthUpdate` `headers`.
deleted
boolean
Should the header be deleted.
name [_required_]
string
The `HTTPHeaderUpdate` `name`.
value
string
The `HTTPHeaderUpdate` `value`.
tokens
[object]
The `HTTPTokenAuthUpdate` `tokens`.
deleted
boolean
Should the header be deleted.
name [_required_]
string
The `HTTPToken` `name`.
type [_required_]
enum
The definition of `TokenType` object. Allowed enum values: `SECRET`
value [_required_]
string
The `HTTPToken` `value`.
type [_required_]
enum
The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`
url_parameters
[object]
The `HTTPTokenAuthUpdate` `url_parameters`.
deleted
boolean
Should the header be deleted.
name [_required_]
string
Name for tokens.
value
string
The `UrlParamUpdate` `value`.
type [_required_]
enum
The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`
Option 17
object
The definition of the `LaunchDarklyIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `LaunchDarklyCredentialsUpdate` object.
Option 1
object
The definition of the `LaunchDarklyAPIKey` object.
api_token
string
The `LaunchDarklyAPIKeyUpdate` `api_token`.
type [_required_]
enum
The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`
type [_required_]
enum
The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`
Option 18
object
The definition of the `NotionIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `NotionCredentialsUpdate` object.
Option 1
object
The definition of the `NotionAPIKey` object.
api_token
string
The `NotionAPIKeyUpdate` `api_token`.
type [_required_]
enum
The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`
type [_required_]
enum
The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`
Option 19
object
The definition of the `OktaIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `OktaCredentialsUpdate` object.
Option 1
object
The definition of the `OktaAPIToken` object.
api_token
string
The `OktaAPITokenUpdate` `api_token`.
domain
string
The `OktaAPITokenUpdate` `domain`.
type [_required_]
enum
The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`
type [_required_]
enum
The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`
Option 20
object
The definition of the `OpenAIIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `OpenAICredentialsUpdate` object.
Option 1
object
The definition of the `OpenAIAPIKey` object.
api_token
string
The `OpenAIAPIKeyUpdate` `api_token`.
type [_required_]
enum
The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`
type [_required_]
enum
The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`
Option 21
object
The definition of the `ServiceNowIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `ServiceNowCredentialsUpdate` object.
Option 1
object
The definition of the `ServiceNowBasicAuth` object.
instance
string
The `ServiceNowBasicAuthUpdate` `instance`.
password
string
The `ServiceNowBasicAuthUpdate` `password`.
type [_required_]
enum
The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`
username
string
The `ServiceNowBasicAuthUpdate` `username`.
type [_required_]
enum
The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`
Option 22
object
The definition of the `SplitIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `SplitCredentialsUpdate` object.
Option 1
object
The definition of the `SplitAPIKey` object.
api_key
string
The `SplitAPIKeyUpdate` `api_key`.
type [_required_]
enum
The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`
type [_required_]
enum
The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`
Option 23
object
The definition of the `StatsigIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `StatsigCredentialsUpdate` object.
Option 1
object
The definition of the `StatsigAPIKey` object.
api_key
string
The `StatsigAPIKeyUpdate` `api_key`.
type [_required_]
enum
The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`
type [_required_]
enum
The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`
Option 24
object
The definition of the `VirusTotalIntegrationUpdate` object.
credentials
<oneOf>
The definition of the `VirusTotalCredentialsUpdate` object.
Option 1
object
The definition of the `VirusTotalAPIKey` object.
api_key
string
The `VirusTotalAPIKeyUpdate` `api_key`.
type [_required_]
enum
The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`
type [_required_]
enum
The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`
name
string
Name of the connection
type [_required_]
enum
The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/action-connection/#UpdateActionConnection-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/action-connection/#UpdateActionConnection-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#UpdateActionConnection-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/action-connection/#UpdateActionConnection-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#UpdateActionConnection-429-v2)


Successfully updated Action Connection
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


The response for an updated connection.
Field
Type
Description
data
object
Data related to the connection.
attributes [_required_]
object
The definition of `ActionConnectionAttributes` object.
integration [_required_]
<oneOf>
The definition of `ActionConnectionIntegration` object.
Option 1
object
The definition of `AWSIntegration` object.
credentials [_required_]
<oneOf>
The definition of `AWSCredentials` object.
Option 1
object
The definition of `AWSAssumeRole` object.
account_id [_required_]
string
AWS account the connection is created for
external_id
string
External ID used to scope which connection can be used to assume the role
principal_id
string
AWS account that will assume the role
role [_required_]
string
Role to assume
type [_required_]
enum
The definition of `AWSAssumeRoleType` object. Allowed enum values: `AWSAssumeRole`
type [_required_]
enum
The definition of `AWSIntegrationType` object. Allowed enum values: `AWS`
Option 2
object
The definition of the `AnthropicIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AnthropicCredentials` object.
Option 1
object
The definition of the `AnthropicAPIKey` object.
api_token [_required_]
string
The `AnthropicAPIKey` `api_token`.
type [_required_]
enum
The definition of the `AnthropicAPIKey` object. Allowed enum values: `AnthropicAPIKey`
type [_required_]
enum
The definition of the `AnthropicIntegrationType` object. Allowed enum values: `Anthropic`
Option 3
object
The definition of the `AsanaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AsanaCredentials` object.
Option 1
object
The definition of the `AsanaAccessToken` object.
access_token [_required_]
string
The `AsanaAccessToken` `access_token`.
type [_required_]
enum
The definition of the `AsanaAccessToken` object. Allowed enum values: `AsanaAccessToken`
type [_required_]
enum
The definition of the `AsanaIntegrationType` object. Allowed enum values: `Asana`
Option 4
object
The definition of the `AzureIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `AzureCredentials` object.
Option 1
object
The definition of the `AzureTenant` object.
app_client_id [_required_]
string
The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.
client_secret [_required_]
string
The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application’s secrets page. You can navigate to your application via the Azure Directory.
custom_scopes
string
If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.
tenant_id [_required_]
string
The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.
type [_required_]
enum
The definition of the `AzureTenant` object. Allowed enum values: `AzureTenant`
type [_required_]
enum
The definition of the `AzureIntegrationType` object. Allowed enum values: `Azure`
Option 5
object
The definition of the `CircleCIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CircleCICredentials` object.
Option 1
object
The definition of the `CircleCIAPIKey` object.
api_token [_required_]
string
The `CircleCIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `CircleCIAPIKey` object. Allowed enum values: `CircleCIAPIKey`
type [_required_]
enum
The definition of the `CircleCIIntegrationType` object. Allowed enum values: `CircleCI`
Option 6
object
The definition of the `ClickupIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ClickupCredentials` object.
Option 1
object
The definition of the `ClickupAPIKey` object.
api_token [_required_]
string
The `ClickupAPIKey` `api_token`.
type [_required_]
enum
The definition of the `ClickupAPIKey` object. Allowed enum values: `ClickupAPIKey`
type [_required_]
enum
The definition of the `ClickupIntegrationType` object. Allowed enum values: `Clickup`
Option 7
object
The definition of the `CloudflareIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `CloudflareCredentials` object.
Option 1
object
The definition of the `CloudflareAPIToken` object.
api_token [_required_]
string
The `CloudflareAPIToken` `api_token`.
type [_required_]
enum
The definition of the `CloudflareAPIToken` object. Allowed enum values: `CloudflareAPIToken`
Option 2
object
The definition of the `CloudflareGlobalAPIToken` object.
auth_email [_required_]
string
The `CloudflareGlobalAPIToken` `auth_email`.
global_api_key [_required_]
string
The `CloudflareGlobalAPIToken` `global_api_key`.
type [_required_]
enum
The definition of the `CloudflareGlobalAPIToken` object. Allowed enum values: `CloudflareGlobalAPIToken`
type [_required_]
enum
The definition of the `CloudflareIntegrationType` object. Allowed enum values: `Cloudflare`
Option 8
object
The definition of the `ConfigCatIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ConfigCatCredentials` object.
Option 1
object
The definition of the `ConfigCatSDKKey` object.
api_password [_required_]
string
The `ConfigCatSDKKey` `api_password`.
api_username [_required_]
string
The `ConfigCatSDKKey` `api_username`.
sdk_key [_required_]
string
The `ConfigCatSDKKey` `sdk_key`.
type [_required_]
enum
The definition of the `ConfigCatSDKKey` object. Allowed enum values: `ConfigCatSDKKey`
type [_required_]
enum
The definition of the `ConfigCatIntegrationType` object. Allowed enum values: `ConfigCat`
Option 9
object
The definition of the `DatadogIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `DatadogCredentials` object.
Option 1
object
The definition of the `DatadogAPIKey` object.
api_key [_required_]
string
The `DatadogAPIKey` `api_key`.
app_key [_required_]
string
The `DatadogAPIKey` `app_key`.
datacenter [_required_]
string
The `DatadogAPIKey` `datacenter`.
subdomain
string
Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses `https://acme.datadoghq.com` to access Datadog, set this field to `acme`. If this field is omitted, generated URLs will use the default site URL for its datacenter (see <https://docs.datadoghq.com/getting_started/site>).
type [_required_]
enum
The definition of the `DatadogAPIKey` object. Allowed enum values: `DatadogAPIKey`
type [_required_]
enum
The definition of the `DatadogIntegrationType` object. Allowed enum values: `Datadog`
Option 10
object
The definition of the `FastlyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FastlyCredentials` object.
Option 1
object
The definition of the `FastlyAPIKey` object.
api_key [_required_]
string
The `FastlyAPIKey` `api_key`.
type [_required_]
enum
The definition of the `FastlyAPIKey` object. Allowed enum values: `FastlyAPIKey`
type [_required_]
enum
The definition of the `FastlyIntegrationType` object. Allowed enum values: `Fastly`
Option 11
object
The definition of the `FreshserviceIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `FreshserviceCredentials` object.
Option 1
object
The definition of the `FreshserviceAPIKey` object.
api_key [_required_]
string
The `FreshserviceAPIKey` `api_key`.
domain [_required_]
string
The `FreshserviceAPIKey` `domain`.
type [_required_]
enum
The definition of the `FreshserviceAPIKey` object. Allowed enum values: `FreshserviceAPIKey`
type [_required_]
enum
The definition of the `FreshserviceIntegrationType` object. Allowed enum values: `Freshservice`
Option 12
object
The definition of the `GCPIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GCPCredentials` object.
Option 1
object
The definition of the `GCPServiceAccount` object.
private_key [_required_]
string
The `GCPServiceAccount` `private_key`.
service_account_email [_required_]
string
The `GCPServiceAccount` `service_account_email`.
type [_required_]
enum
The definition of the `GCPServiceAccount` object. Allowed enum values: `GCPServiceAccount`
type [_required_]
enum
The definition of the `GCPIntegrationType` object. Allowed enum values: `GCP`
Option 13
object
The definition of the `GeminiIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GeminiCredentials` object.
Option 1
object
The definition of the `GeminiAPIKey` object.
api_key [_required_]
string
The `GeminiAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GeminiAPIKey` object. Allowed enum values: `GeminiAPIKey`
type [_required_]
enum
The definition of the `GeminiIntegrationType` object. Allowed enum values: `Gemini`
Option 14
object
The definition of the `GitlabIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GitlabCredentials` object.
Option 1
object
The definition of the `GitlabAPIKey` object.
api_token [_required_]
string
The `GitlabAPIKey` `api_token`.
type [_required_]
enum
The definition of the `GitlabAPIKey` object. Allowed enum values: `GitlabAPIKey`
type [_required_]
enum
The definition of the `GitlabIntegrationType` object. Allowed enum values: `Gitlab`
Option 15
object
The definition of the `GreyNoiseIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `GreyNoiseCredentials` object.
Option 1
object
The definition of the `GreyNoiseAPIKey` object.
api_key [_required_]
string
The `GreyNoiseAPIKey` `api_key`.
type [_required_]
enum
The definition of the `GreyNoiseAPIKey` object. Allowed enum values: `GreyNoiseAPIKey`
type [_required_]
enum
The definition of the `GreyNoiseIntegrationType` object. Allowed enum values: `GreyNoise`
Option 16
object
The definition of `HTTPIntegration` object.
base_url [_required_]
string
Base HTTP url for the integration
credentials [_required_]
<oneOf>
The definition of `HTTPCredentials` object.
Option 1
object
The definition of `HTTPTokenAuth` object.
body
object
The definition of `HTTPBody` object.
content
string
Serialized body content
content_type
string
Content type of the body
headers
[object]
The `HTTPTokenAuth` `headers`.
name [_required_]
string
The `HTTPHeader` `name`.
value [_required_]
string
The `HTTPHeader` `value`.
tokens
[object]
The `HTTPTokenAuth` `tokens`.
name [_required_]
string
The `HTTPToken` `name`.
type [_required_]
enum
The definition of `TokenType` object. Allowed enum values: `SECRET`
value [_required_]
string
The `HTTPToken` `value`.
type [_required_]
enum
The definition of `HTTPTokenAuthType` object. Allowed enum values: `HTTPTokenAuth`
url_parameters
[object]
The `HTTPTokenAuth` `url_parameters`.
name [_required_]
string
Name for tokens.
value [_required_]
string
The `UrlParam` `value`.
type [_required_]
enum
The definition of `HTTPIntegrationType` object. Allowed enum values: `HTTP`
Option 17
object
The definition of the `LaunchDarklyIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `LaunchDarklyCredentials` object.
Option 1
object
The definition of the `LaunchDarklyAPIKey` object.
api_token [_required_]
string
The `LaunchDarklyAPIKey` `api_token`.
type [_required_]
enum
The definition of the `LaunchDarklyAPIKey` object. Allowed enum values: `LaunchDarklyAPIKey`
type [_required_]
enum
The definition of the `LaunchDarklyIntegrationType` object. Allowed enum values: `LaunchDarkly`
Option 18
object
The definition of the `NotionIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `NotionCredentials` object.
Option 1
object
The definition of the `NotionAPIKey` object.
api_token [_required_]
string
The `NotionAPIKey` `api_token`.
type [_required_]
enum
The definition of the `NotionAPIKey` object. Allowed enum values: `NotionAPIKey`
type [_required_]
enum
The definition of the `NotionIntegrationType` object. Allowed enum values: `Notion`
Option 19
object
The definition of the `OktaIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OktaCredentials` object.
Option 1
object
The definition of the `OktaAPIToken` object.
api_token [_required_]
string
The `OktaAPIToken` `api_token`.
domain [_required_]
string
The `OktaAPIToken` `domain`.
type [_required_]
enum
The definition of the `OktaAPIToken` object. Allowed enum values: `OktaAPIToken`
type [_required_]
enum
The definition of the `OktaIntegrationType` object. Allowed enum values: `Okta`
Option 20
object
The definition of the `OpenAIIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `OpenAICredentials` object.
Option 1
object
The definition of the `OpenAIAPIKey` object.
api_token [_required_]
string
The `OpenAIAPIKey` `api_token`.
type [_required_]
enum
The definition of the `OpenAIAPIKey` object. Allowed enum values: `OpenAIAPIKey`
type [_required_]
enum
The definition of the `OpenAIIntegrationType` object. Allowed enum values: `OpenAI`
Option 21
object
The definition of the `ServiceNowIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `ServiceNowCredentials` object.
Option 1
object
The definition of the `ServiceNowBasicAuth` object.
instance [_required_]
string
The `ServiceNowBasicAuth` `instance`.
password [_required_]
string
The `ServiceNowBasicAuth` `password`.
type [_required_]
enum
The definition of the `ServiceNowBasicAuth` object. Allowed enum values: `ServiceNowBasicAuth`
username [_required_]
string
The `ServiceNowBasicAuth` `username`.
type [_required_]
enum
The definition of the `ServiceNowIntegrationType` object. Allowed enum values: `ServiceNow`
Option 22
object
The definition of the `SplitIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `SplitCredentials` object.
Option 1
object
The definition of the `SplitAPIKey` object.
api_key [_required_]
string
The `SplitAPIKey` `api_key`.
type [_required_]
enum
The definition of the `SplitAPIKey` object. Allowed enum values: `SplitAPIKey`
type [_required_]
enum
The definition of the `SplitIntegrationType` object. Allowed enum values: `Split`
Option 23
object
The definition of the `StatsigIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `StatsigCredentials` object.
Option 1
object
The definition of the `StatsigAPIKey` object.
api_key [_required_]
string
The `StatsigAPIKey` `api_key`.
type [_required_]
enum
The definition of the `StatsigAPIKey` object. Allowed enum values: `StatsigAPIKey`
type [_required_]
enum
The definition of the `StatsigIntegrationType` object. Allowed enum values: `Statsig`
Option 24
object
The definition of the `VirusTotalIntegration` object.
credentials [_required_]
<oneOf>
The definition of the `VirusTotalCredentials` object.
Option 1
object
The definition of the `VirusTotalAPIKey` object.
api_key [_required_]
string
The `VirusTotalAPIKey` `api_key`.
type [_required_]
enum
The definition of the `VirusTotalAPIKey` object. Allowed enum values: `VirusTotalAPIKey`
type [_required_]
enum
The definition of the `VirusTotalIntegrationType` object. Allowed enum values: `VirusTotal`
name [_required_]
string
Name of the connection
id
string
The connection identifier
type [_required_]
enum
The definition of `ActionConnectionDataType` object. Allowed enum values: `action_connection`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too Many Request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  Update an existing Action Connection returns "Successfully updated Action Connection" response
Copy
```
                          # Path parameters  
export connection_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections/${connection_id}" \
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

                        
```

#####  Update an existing Action Connection returns "Successfully updated Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update an existing Action Connection returns "Successfully updated Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update an existing Action Connection returns "Successfully updated Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update an existing Action Connection returns "Successfully updated Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update an existing Action Connection returns "Successfully updated Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update an existing Action Connection returns "Successfully updated Action Connection" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete an existing Action Connection](https://docs.datadoghq.com/api/latest/action-connection/#delete-an-existing-action-connection)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#delete-an-existing-action-connection-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.ap2.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.datadoghq.eu/api/v2/actions/connections/{connection_id}https://api.ddog-gov.com/api/v2/actions/connections/{connection_id}https://api.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.us3.datadoghq.com/api/v2/actions/connections/{connection_id}https://api.us5.datadoghq.com/api/v2/actions/connections/{connection_id}
### Overview
Delete an existing Action Connection. This API requires a [registered application key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). Alternatively, you can configure these permissions [in the UI](https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access). This endpoint requires the `connection_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
connection_id [_required_]
string
The ID of the action connection
### Response
  * [204](https://docs.datadoghq.com/api/latest/action-connection/#DeleteActionConnection-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#DeleteActionConnection-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/action-connection/#DeleteActionConnection-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#DeleteActionConnection-429-v2)


The resource was deleted successfully.
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too Many Request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  Delete an existing Action Connection
Copy
```
                  # Path parameters  
export connection_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/connections/${connection_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an existing Action Connection
```
# Delete an existing Action Connection returns "The resource was deleted successfully." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new

# there is a valid "action_connection" in the system
ACTION_CONNECTION_DATA_ID = ENV["ACTION_CONNECTION_DATA_ID"]
api_instance.delete_action_connection(ACTION_CONNECTION_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete an existing Action Connection
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Register a new App Key](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key-v2)


PUT https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.ap2.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.datadoghq.eu/api/v2/actions/app_key_registrations/{app_key_id}https://api.ddog-gov.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.us3.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}
### Overview
Register a new App Key This endpoint requires any of the following permissions:
* `user_access_manage`
* `user_app_keys`
* `service_account_write`
  

### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the app key
### Response
  * [201](https://docs.datadoghq.com/api/latest/action-connection/#RegisterAppKey-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/action-connection/#RegisterAppKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#RegisterAppKey-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#RegisterAppKey-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


The response object after creating an app key registration.
Field
Type
Description
data
object
Data related to the app key registration.
id
uuid
The app key registration identifier
type [_required_]
enum
The definition of `AppKeyRegistrationDataType` object. Allowed enum values: `app_key_registration`
```
{
  "data": {
    "id": "string",
    "type": "app_key_registration"
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  Register a new App Key
Copy
```
                  # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Register a new App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Register a new App Key
```
# Register a new App Key returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.register_app_key("b7feea52-994e-4714-a100-1bd9eff5aee1")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Register a new App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Register a new App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Register a new App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Register a new App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [List App Key Registrations](https://docs.datadoghq.com/api/latest/action-connection/#list-app-key-registrations)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#list-app-key-registrations-v2)


GET https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrationshttps://api.ap2.datadoghq.com/api/v2/actions/app_key_registrationshttps://api.datadoghq.eu/api/v2/actions/app_key_registrationshttps://api.ddog-gov.com/api/v2/actions/app_key_registrationshttps://api.datadoghq.com/api/v2/actions/app_key_registrationshttps://api.us3.datadoghq.com/api/v2/actions/app_key_registrationshttps://api.us5.datadoghq.com/api/v2/actions/app_key_registrations
### Overview
List App Key Registrations This endpoint requires the `org_app_keys_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
The number of App Key Registrations to return per page.
page[number]
integer
The page number to return.
### Response
  * [200](https://docs.datadoghq.com/api/latest/action-connection/#ListAppKeyRegistrations-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/action-connection/#ListAppKeyRegistrations-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#ListAppKeyRegistrations-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#ListAppKeyRegistrations-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


A paginated list of app key registrations.
Field
Type
Description
data
[object]
An array of app key registrations.
id
uuid
The app key registration identifier
type [_required_]
enum
The definition of `AppKeyRegistrationDataType` object. Allowed enum values: `app_key_registration`
meta
object
The definition of `ListAppKeyRegistrationsResponseMeta` object.
total
int64
The total number of app key registrations.
total_filtered
int64
The total number of app key registrations that match the specified filters.
```
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

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  List App Key Registrations
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List App Key Registrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List App Key Registrations
```
# List App Key Registrations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.list_app_key_registrations()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List App Key Registrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List App Key Registrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List App Key Registrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List App Key Registrations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Unregister an App Key](https://docs.datadoghq.com/api/latest/action-connection/#unregister-an-app-key)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#unregister-an-app-key-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.ap2.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.datadoghq.eu/api/v2/actions/app_key_registrations/{app_key_id}https://api.ddog-gov.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.us3.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}
### Overview
Unregister an App Key This endpoint requires any of the following permissions:
* `user_access_manage`
* `user_app_keys`
* `service_account_write`
  

### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the app key
### Response
  * [204](https://docs.datadoghq.com/api/latest/action-connection/#UnregisterAppKey-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/action-connection/#UnregisterAppKey-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#UnregisterAppKey-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/action-connection/#UnregisterAppKey-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#UnregisterAppKey-429-v2)


No Content
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  Unregister an App Key
Copy
```
                  # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/${app_key_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Unregister an App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Unregister an App Key
```
# Unregister an App Key returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
api_instance.unregister_app_key("57cc69ae-9214-4ecc-8df8-43ecc1d92d99")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Unregister an App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Unregister an App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Unregister an App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Unregister an App Key
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get an existing App Key Registration](https://docs.datadoghq.com/api/latest/action-connection/#get-an-existing-app-key-registration)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/action-connection/#get-an-existing-app-key-registration-v2)


GET https://api.ap1.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.ap2.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.datadoghq.eu/api/v2/actions/app_key_registrations/{app_key_id}https://api.ddog-gov.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.us3.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/{app_key_id}
### Overview
Get an existing App Key Registration This endpoint requires the `org_app_keys_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
app_key_id [_required_]
string
The ID of the app key
### Response
  * [200](https://docs.datadoghq.com/api/latest/action-connection/#GetAppKeyRegistration-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/action-connection/#GetAppKeyRegistration-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/action-connection/#GetAppKeyRegistration-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/action-connection/#GetAppKeyRegistration-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/action-connection/#GetAppKeyRegistration-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


The response object after getting an app key registration.
Field
Type
Description
data
object
Data related to the app key registration.
id
uuid
The app key registration identifier
type [_required_]
enum
The definition of `AppKeyRegistrationDataType` object. Allowed enum values: `app_key_registration`
```
{
  "data": {
    "id": "string",
    "type": "app_key_registration"
  }
}
```

Copy
Bad request
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/action-connection/)
  * [Example](https://docs.datadoghq.com/api/latest/action-connection/)


API error response.
Field
Type
Description
errors [_required_]
[object]
A list of errors.
detail
string
A human-readable explanation specific to this occurrence of the error.
meta
object
Non-standard meta-information about the error
source
object
References to the source of the error.
header
string
A string indicating the name of a single request header which caused the error.
parameter
string
A string indicating which URI query parameter caused the error.
pointer
string
A JSON pointer to the value in the request document that caused the error.
status
string
Status code of the response.
title
string
Short human-readable summary of the error.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/action-connection/?code-lang=typescript)


#####  Get an existing App Key Registration
Copy
```
                  # Path parameters  
export app_key_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/actions/app_key_registrations/${app_key_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an existing App Key Registration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an existing App Key Registration
```
# Get an existing App Key Registration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ActionConnectionAPI.new
p api_instance.get_app_key_registration("b7feea52-994e-4714-a100-1bd9eff5aee1")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an existing App Key Registration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an existing App Key Registration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get an existing App Key Registration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get an existing App Key Registration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d281a251-581b-46d0-bf2a-22262fe396d1&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=dea7f038-498d-4446-8f7c-77b275287acd&pt=Action%20Connection&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faction-connection%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d281a251-581b-46d0-bf2a-22262fe396d1&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=dea7f038-498d-4446-8f7c-77b275287acd&pt=Action%20Connection&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faction-connection%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=60345456-6951-4902-870b-140634b8edef&bo=2&sid=bf71a970f0be11f0814e1f63b85d6398&vid=bf72bca0f0be11f09feacba66159d584&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Action%20Connection&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Faction-connection%2F&r=&lt=2210&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=554673)
