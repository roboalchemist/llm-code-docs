# Source: https://docs.datadoghq.com/api/latest/slack-integration.md

---
title: Slack Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Slack Integration
---

# Slack Integration

Configure your [Datadog-Slack integration](https://docs.datadoghq.com/integrations/slack) directly through the Datadog API.

## Delete a Slack integration{% #delete-a-slack-integration %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/slack |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/slack |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/slack      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/slack      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/slack     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/slack |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/slack |

### Overview

Delete a Datadog-Slack integration.

### Response

{% tab title="200" %}
OK
{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.delete_integration('slack')
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
## Get all channels in a Slack integration{% #get-all-channels-in-a-slack-integration %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                              |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |

### Overview

Get a list of all channels configured for your Datadog-Slack integration. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| account_name [*required*] | string | Your Slack account name. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A list of configured Slack channels.

| Parent field | Field        | Type    | Description                                                        |
| ------------ | ------------ | ------- | ------------------------------------------------------------------ |
|              | display      | object  | Configuration options for what is shown in an alert event message. |
| display      | message      | boolean | Show the main body of the alert event.                             |
| display      | mute_buttons | boolean | Show interactive buttons to mute the alerting monitor.             |
| display      | notified     | boolean | Show the list of @-handles in the alert event.                     |
| display      | snapshot     | boolean | Show the alert event's snapshot image.                             |
| display      | tags         | boolean | Show the scopes on which the monitor alerted.                      |
|              | name         | string  | Your channel name.                                                 |

{% /tab %}

{% tab title="Example" %}

```json
[
  {
    "display": {
      "message": true,
      "mute_buttons": true,
      "notified": true,
      "snapshot": true,
      "tags": true
    },
    "name": "#channel_name_main_account"
  },
  {
    "display": {
      "message": true,
      "mute_buttons": true,
      "notified": true,
      "snapshot": false,
      "tags": true
    },
    "name": "#channel_name_doghouse"
  }
]
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Item Not Found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport account_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all channels in a Slack integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    response = api_instance.get_slack_integration_channels(
        account_name="account_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all channels in a Slack integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new
p api_instance.get_slack_integration_channels("account_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all channels in a Slack integration returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewSlackIntegrationApi(apiClient)
    resp, r, err := api.GetSlackIntegrationChannels(ctx, "account_name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SlackIntegrationApi.GetSlackIntegrationChannels`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SlackIntegrationApi.GetSlackIntegrationChannels`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all channels in a Slack integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.SlackIntegrationApi;
import com.datadog.api.client.v1.model.SlackIntegrationChannel;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SlackIntegrationApi apiInstance = new SlackIntegrationApi(defaultClient);

    try {
      List<SlackIntegrationChannel> result =
          apiInstance.getSlackIntegrationChannels("account_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlackIntegrationApi#getSlackIntegrationChannels");
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
// Get all channels in a Slack integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_slack_integration::SlackIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SlackIntegrationAPI::with_config(configuration);
    let resp = api
        .get_slack_integration_channels("account_name".to_string())
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
 * Get all channels in a Slack integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.SlackIntegrationApi(configuration);

const params: v1.SlackIntegrationApiGetSlackIntegrationChannelsRequest = {
  accountName: "account_name",
};

apiInstance
  .getSlackIntegrationChannels(params)
  .then((data: v1.SlackIntegrationChannel[]) => {
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

## Add channels to Slack integration{% #add-channels-to-slack-integration %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/integration/slack |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/integration/slack |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/integration/slack      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/integration/slack      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/integration/slack     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/integration/slack |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/integration/slack |

### Overview



Add channels to your existing Datadog-Slack integration.

This method updates your integration configuration by **replacing** your current configuration with the new one sent to your Datadog organization.



### Request

#### Body Data (required)

Update an existing Datadog-Slack integration request body.

{% tab title="Model" %}

| Parent field | Field                          | Type     | Description                                                                                                                                               |
| ------------ | ------------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | channels                       | [object] | An array of slack channel configurations.                                                                                                                 |
| channels     | account [*required*]      | string   | Account to which the channel belongs to.                                                                                                                  |
| channels     | channel_name [*required*] | string   | Your channel name.                                                                                                                                        |
| channels     | transfer_all_user_comments     | boolean  | To be notified for every comment on a graph, set it to `true`. If set to `False` use the `@slack-channel_name` syntax for comments to be posted to slack. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "channels": [
    {
      "account": "jane.doe",
      "channel_name": "#general",
      "transfer_all_user_comments": false
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "channels": [
    {
      "account": "jane.doe",
      "channel_name": "#general"
    }
  ]
}
EOF

## Create a Slack integration channel{% #create-a-slack-integration-channel %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels |

### Overview

Add a channel to your Datadog-Slack integration. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| account_name [*required*] | string | Your Slack account name. |

### Request

#### Body Data (required)

Payload describing Slack channel to be created

{% tab title="Model" %}

| Parent field | Field        | Type    | Description                                                        |
| ------------ | ------------ | ------- | ------------------------------------------------------------------ |
|              | display      | object  | Configuration options for what is shown in an alert event message. |
| display      | message      | boolean | Show the main body of the alert event.                             |
| display      | mute_buttons | boolean | Show interactive buttons to mute the alerting monitor.             |
| display      | notified     | boolean | Show the list of @-handles in the alert event.                     |
| display      | snapshot     | boolean | Show the alert event's snapshot image.                             |
| display      | tags         | boolean | Show the scopes on which the monitor alerted.                      |
|              | name         | string  | Your channel name.                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "display": {
    "message": false,
    "mute_buttons": false,
    "notified": false,
    "snapshot": false,
    "tags": false
  },
  "name": "#general"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The Slack channel configuration.

| Parent field | Field        | Type    | Description                                                        |
| ------------ | ------------ | ------- | ------------------------------------------------------------------ |
|              | display      | object  | Configuration options for what is shown in an alert event message. |
| display      | message      | boolean | Show the main body of the alert event.                             |
| display      | mute_buttons | boolean | Show interactive buttons to mute the alerting monitor.             |
| display      | notified     | boolean | Show the list of @-handles in the alert event.                     |
| display      | snapshot     | boolean | Show the alert event's snapshot image.                             |
| display      | tags         | boolean | Show the scopes on which the monitor alerted.                      |
|              | name         | string  | Your channel name.                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "display": {
    "message": false,
    "mute_buttons": false,
    "notified": false,
    "snapshot": false,
    "tags": false
  },
  "name": "#general"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Item Not Found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport account_name="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF

#####

```python
"""
Create a Slack integration channel returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi
from datadog_api_client.v1.model.slack_integration_channel import SlackIntegrationChannel
from datadog_api_client.v1.model.slack_integration_channel_display import SlackIntegrationChannelDisplay

body = SlackIntegrationChannel(
    display=SlackIntegrationChannelDisplay(
        message=True,
        mute_buttons=False,
        notified=True,
        snapshot=True,
        tags=True,
    ),
    name="#general",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    response = api_instance.create_slack_integration_channel(account_name="account_name", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a Slack integration channel returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new

body = DatadogAPIClient::V1::SlackIntegrationChannel.new({
  display: DatadogAPIClient::V1::SlackIntegrationChannelDisplay.new({
    message: true,
    mute_buttons: false,
    notified: true,
    snapshot: true,
    tags: true,
  }),
  name: "#general",
})
p api_instance.create_slack_integration_channel("account_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Create a Slack integration channel returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.SlackIntegrationChannel{
        Display: &datadogV1.SlackIntegrationChannelDisplay{
            Message:     datadog.PtrBool(true),
            MuteButtons: datadog.PtrBool(false),
            Notified:    datadog.PtrBool(true),
            Snapshot:    datadog.PtrBool(true),
            Tags:        datadog.PtrBool(true),
        },
        Name: datadog.PtrString("#general"),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewSlackIntegrationApi(apiClient)
    resp, r, err := api.CreateSlackIntegrationChannel(ctx, "account_name", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SlackIntegrationApi.CreateSlackIntegrationChannel`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SlackIntegrationApi.CreateSlackIntegrationChannel`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a Slack integration channel returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.SlackIntegrationApi;
import com.datadog.api.client.v1.model.SlackIntegrationChannel;
import com.datadog.api.client.v1.model.SlackIntegrationChannelDisplay;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SlackIntegrationApi apiInstance = new SlackIntegrationApi(defaultClient);

    SlackIntegrationChannel body =
        new SlackIntegrationChannel()
            .display(
                new SlackIntegrationChannelDisplay()
                    .message(true)
                    .muteButtons(false)
                    .notified(true)
                    .snapshot(true)
                    .tags(true))
            .name("#general");

    try {
      SlackIntegrationChannel result =
          apiInstance.createSlackIntegrationChannel("account_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling SlackIntegrationApi#createSlackIntegrationChannel");
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
// Create a Slack integration channel returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_slack_integration::SlackIntegrationAPI;
use datadog_api_client::datadogV1::model::SlackIntegrationChannel;
use datadog_api_client::datadogV1::model::SlackIntegrationChannelDisplay;

#[tokio::main]
async fn main() {
    let body = SlackIntegrationChannel::new()
        .display(
            SlackIntegrationChannelDisplay::new()
                .message(true)
                .mute_buttons(false)
                .notified(true)
                .snapshot(true)
                .tags(true),
        )
        .name("#general".to_string());
    let configuration = datadog::Configuration::new();
    let api = SlackIntegrationAPI::with_config(configuration);
    let resp = api
        .create_slack_integration_channel("account_name".to_string(), body)
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
 * Create a Slack integration channel returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.SlackIntegrationApi(configuration);

const params: v1.SlackIntegrationApiCreateSlackIntegrationChannelRequest = {
  body: {
    display: {
      message: true,
      muteButtons: false,
      notified: true,
      snapshot: true,
      tags: true,
    },
    name: "#general",
  },
  accountName: "account_name",
};

apiInstance
  .createSlackIntegrationChannel(params)
  .then((data: v1.SlackIntegrationChannel) => {
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

## Create a Slack integration{% #create-a-slack-integration %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/slack |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/slack |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/slack      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/slack      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/slack     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/slack |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/slack |

### Overview



Create a Datadog-Slack integration. Once created, add a channel to it with the [Add channels to Slack integration endpoint](https://docs.datadoghq.com/api/?lang=bash#add-channels-to-slack-integration).

This method updates your integration configuration by **adding** your new configuration to the existing one in your Datadog organization.



### Request

#### Body Data (required)

Create Datadog-Slack integration request body.

{% tab title="Model" %}

| Parent field  | Field                     | Type     | Description                        |
| ------------- | ------------------------- | -------- | ---------------------------------- |
|               | service_hooks             | [object] | The array of service hook objects. |
| service_hooks | account [*required*] | string   | Your Slack account name.           |
| service_hooks | url [*required*]     | string   | Your Slack service hook URL.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "service_hooks": [
    {
      "account": "joe.doe",
      "url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "service_hooks": [
    {
      "account": "joe.doe",
      "url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    }
  ]
}
EOF

#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

config= {
    "service_hooks": [
      {
        "account": "Main_Account",
        "url": "https://hooks.slack.com/services/1/1/1"
      },
      {
        "account": "doghouse",
        "url": "https://hooks.slack.com/services/2/2/2"
      }
    ]
  }

dog = Dogapi::Client.new(api_key, app_key)

dog.create_integration('slack', config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
## Get a Slack integration channel{% #get-a-slack-integration-channel %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |

### Overview

Get a channel configured for your Datadog-Slack integration. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                      |
| ------------------------------ | ------ | ------------------------------------------------ |
| account_name [*required*] | string | Your Slack account name.                         |
| channel_name [*required*] | string | The name of the Slack channel being operated on. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The Slack channel configuration.

| Parent field | Field        | Type    | Description                                                        |
| ------------ | ------------ | ------- | ------------------------------------------------------------------ |
|              | display      | object  | Configuration options for what is shown in an alert event message. |
| display      | message      | boolean | Show the main body of the alert event.                             |
| display      | mute_buttons | boolean | Show interactive buttons to mute the alerting monitor.             |
| display      | notified     | boolean | Show the list of @-handles in the alert event.                     |
| display      | snapshot     | boolean | Show the alert event's snapshot image.                             |
| display      | tags         | boolean | Show the scopes on which the monitor alerted.                      |
|              | name         | string  | Your channel name.                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "display": {
    "message": false,
    "mute_buttons": false,
    "notified": false,
    "snapshot": false,
    "tags": false
  },
  "name": "#general"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Item Not Found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport account_name="CHANGE_ME"export channel_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels/${channel_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a Slack integration channel returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    response = api_instance.get_slack_integration_channel(
        account_name="account_name",
        channel_name="channel_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a Slack integration channel returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new
p api_instance.get_slack_integration_channel("account_name", "channel_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a Slack integration channel returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewSlackIntegrationApi(apiClient)
    resp, r, err := api.GetSlackIntegrationChannel(ctx, "account_name", "channel_name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SlackIntegrationApi.GetSlackIntegrationChannel`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SlackIntegrationApi.GetSlackIntegrationChannel`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a Slack integration channel returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.SlackIntegrationApi;
import com.datadog.api.client.v1.model.SlackIntegrationChannel;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SlackIntegrationApi apiInstance = new SlackIntegrationApi(defaultClient);

    try {
      SlackIntegrationChannel result =
          apiInstance.getSlackIntegrationChannel("account_name", "channel_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlackIntegrationApi#getSlackIntegrationChannel");
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
// Get a Slack integration channel returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_slack_integration::SlackIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SlackIntegrationAPI::with_config(configuration);
    let resp = api
        .get_slack_integration_channel("account_name".to_string(), "channel_name".to_string())
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
 * Get a Slack integration channel returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.SlackIntegrationApi(configuration);

const params: v1.SlackIntegrationApiGetSlackIntegrationChannelRequest = {
  accountName: "account_name",
  channelName: "channel_name",
};

apiInstance
  .getSlackIntegrationChannel(params)
  .then((data: v1.SlackIntegrationChannel) => {
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

## Get info about a Slack integration{% #get-info-about-a-slack-integration %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/slack |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/slack |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/slack      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/slack      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/slack     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/slack |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/slack |

### Overview

Get all information about your Datadog-Slack integration.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Item Not Found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.get_integration('slack')
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
## Update a Slack integration channel{% #update-a-slack-integration-channel %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |

### Overview

Update a channel used in your Datadog-Slack integration. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                      |
| ------------------------------ | ------ | ------------------------------------------------ |
| account_name [*required*] | string | Your Slack account name.                         |
| channel_name [*required*] | string | The name of the Slack channel being operated on. |

### Request

#### Body Data (required)

Payload describing fields and values to be updated.

{% tab title="Model" %}

| Parent field | Field        | Type    | Description                                                        |
| ------------ | ------------ | ------- | ------------------------------------------------------------------ |
|              | display      | object  | Configuration options for what is shown in an alert event message. |
| display      | message      | boolean | Show the main body of the alert event.                             |
| display      | mute_buttons | boolean | Show interactive buttons to mute the alerting monitor.             |
| display      | notified     | boolean | Show the list of @-handles in the alert event.                     |
| display      | snapshot     | boolean | Show the alert event's snapshot image.                             |
| display      | tags         | boolean | Show the scopes on which the monitor alerted.                      |
|              | name         | string  | Your channel name.                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "display": {
    "message": false,
    "mute_buttons": false,
    "notified": false,
    "snapshot": false,
    "tags": false
  },
  "name": "#general"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The Slack channel configuration.

| Parent field | Field        | Type    | Description                                                        |
| ------------ | ------------ | ------- | ------------------------------------------------------------------ |
|              | display      | object  | Configuration options for what is shown in an alert event message. |
| display      | message      | boolean | Show the main body of the alert event.                             |
| display      | mute_buttons | boolean | Show interactive buttons to mute the alerting monitor.             |
| display      | notified     | boolean | Show the list of @-handles in the alert event.                     |
| display      | snapshot     | boolean | Show the alert event's snapshot image.                             |
| display      | tags         | boolean | Show the scopes on which the monitor alerted.                      |
|              | name         | string  | Your channel name.                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "display": {
    "message": false,
    "mute_buttons": false,
    "notified": false,
    "snapshot": false,
    "tags": false
  },
  "name": "#general"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Item Not Found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport account_name="CHANGE_ME"export channel_name="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels/${channel_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF

#####

```python
"""
Update a Slack integration channel returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi
from datadog_api_client.v1.model.slack_integration_channel import SlackIntegrationChannel
from datadog_api_client.v1.model.slack_integration_channel_display import SlackIntegrationChannelDisplay

body = SlackIntegrationChannel(
    display=SlackIntegrationChannelDisplay(
        message=True,
        mute_buttons=False,
        notified=True,
        snapshot=True,
        tags=True,
    ),
    name="#general",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    response = api_instance.update_slack_integration_channel(
        account_name="account_name", channel_name="channel_name", body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a Slack integration channel returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new

body = DatadogAPIClient::V1::SlackIntegrationChannel.new({
  display: DatadogAPIClient::V1::SlackIntegrationChannelDisplay.new({
    message: true,
    mute_buttons: false,
    notified: true,
    snapshot: true,
    tags: true,
  }),
  name: "#general",
})
p api_instance.update_slack_integration_channel("account_name", "channel_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update a Slack integration channel returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.SlackIntegrationChannel{
        Display: &datadogV1.SlackIntegrationChannelDisplay{
            Message:     datadog.PtrBool(true),
            MuteButtons: datadog.PtrBool(false),
            Notified:    datadog.PtrBool(true),
            Snapshot:    datadog.PtrBool(true),
            Tags:        datadog.PtrBool(true),
        },
        Name: datadog.PtrString("#general"),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewSlackIntegrationApi(apiClient)
    resp, r, err := api.UpdateSlackIntegrationChannel(ctx, "account_name", "channel_name", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SlackIntegrationApi.UpdateSlackIntegrationChannel`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `SlackIntegrationApi.UpdateSlackIntegrationChannel`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a Slack integration channel returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.SlackIntegrationApi;
import com.datadog.api.client.v1.model.SlackIntegrationChannel;
import com.datadog.api.client.v1.model.SlackIntegrationChannelDisplay;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SlackIntegrationApi apiInstance = new SlackIntegrationApi(defaultClient);

    SlackIntegrationChannel body =
        new SlackIntegrationChannel()
            .display(
                new SlackIntegrationChannelDisplay()
                    .message(true)
                    .muteButtons(false)
                    .notified(true)
                    .snapshot(true)
                    .tags(true))
            .name("#general");

    try {
      SlackIntegrationChannel result =
          apiInstance.updateSlackIntegrationChannel("account_name", "channel_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling SlackIntegrationApi#updateSlackIntegrationChannel");
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
// Update a Slack integration channel returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_slack_integration::SlackIntegrationAPI;
use datadog_api_client::datadogV1::model::SlackIntegrationChannel;
use datadog_api_client::datadogV1::model::SlackIntegrationChannelDisplay;

#[tokio::main]
async fn main() {
    let body = SlackIntegrationChannel::new()
        .display(
            SlackIntegrationChannelDisplay::new()
                .message(true)
                .mute_buttons(false)
                .notified(true)
                .snapshot(true)
                .tags(true),
        )
        .name("#general".to_string());
    let configuration = datadog::Configuration::new();
    let api = SlackIntegrationAPI::with_config(configuration);
    let resp = api
        .update_slack_integration_channel(
            "account_name".to_string(),
            "channel_name".to_string(),
            body,
        )
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
 * Update a Slack integration channel returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.SlackIntegrationApi(configuration);

const params: v1.SlackIntegrationApiUpdateSlackIntegrationChannelRequest = {
  body: {
    display: {
      message: true,
      muteButtons: false,
      notified: true,
      snapshot: true,
      tags: true,
    },
    name: "#general",
  },
  accountName: "account_name",
  channelName: "channel_name",
};

apiInstance
  .updateSlackIntegrationChannel(params)
  .then((data: v1.SlackIntegrationChannel) => {
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

## Remove a Slack integration channel{% #remove-a-slack-integration-channel %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} |

### Overview

Remove a channel from your Datadog-Slack integration. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                      |
| ------------------------------ | ------ | ------------------------------------------------ |
| account_name [*required*] | string | Your Slack account name.                         |
| channel_name [*required*] | string | The name of the Slack channel being operated on. |

### Response

{% tab title="204" %}
The channel was removed successfully.
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Item Not Found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport account_name="CHANGE_ME"export channel_name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels/${channel_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove a Slack integration channel returns "The channel was removed successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SlackIntegrationApi(api_client)
    api_instance.remove_slack_integration_channel(
        account_name="account_name",
        channel_name="channel_name",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Remove a Slack integration channel returns "The channel was removed successfully." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new
api_instance.remove_slack_integration_channel("account_name", "channel_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Remove a Slack integration channel returns "The channel was removed successfully." response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewSlackIntegrationApi(apiClient)
    r, err := api.RemoveSlackIntegrationChannel(ctx, "account_name", "channel_name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `SlackIntegrationApi.RemoveSlackIntegrationChannel`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Remove a Slack integration channel returns "The channel was removed successfully." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.SlackIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SlackIntegrationApi apiInstance = new SlackIntegrationApi(defaultClient);

    try {
      apiInstance.removeSlackIntegrationChannel("account_name", "channel_name");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling SlackIntegrationApi#removeSlackIntegrationChannel");
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
// Remove a Slack integration channel returns "The channel was removed
// successfully." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_slack_integration::SlackIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SlackIntegrationAPI::with_config(configuration);
    let resp = api
        .remove_slack_integration_channel("account_name".to_string(), "channel_name".to_string())
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
 * Remove a Slack integration channel returns "The channel was removed successfully." response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.SlackIntegrationApi(configuration);

const params: v1.SlackIntegrationApiRemoveSlackIntegrationChannelRequest = {
  accountName: "account_name",
  channelName: "channel_name",
};

apiInstance
  .removeSlackIntegrationChannel(params)
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
