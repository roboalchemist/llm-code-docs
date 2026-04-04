# Source: https://docs.datadoghq.com/api/latest/slack-integration/

# Slack Integration
Configure your [Datadog-Slack integration](https://docs.datadoghq.com/integrations/slack) directly through the Datadog API.
## [Delete a Slack integration](https://docs.datadoghq.com/api/latest/slack-integration/#delete-a-slack-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/slack-integration/#delete-a-slack-integration-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/slackhttps://api.ap2.datadoghq.com/api/v1/integration/slackhttps://api.datadoghq.eu/api/v1/integration/slackhttps://api.ddog-gov.com/api/v1/integration/slackhttps://api.datadoghq.com/api/v1/integration/slackhttps://api.us3.datadoghq.com/api/v1/integration/slackhttps://api.us5.datadoghq.com/api/v1/integration/slack
### Overview
Delete a Datadog-Slack integration.
### Response
  * [200](https://docs.datadoghq.com/api/latest/slack-integration/#DeleteSlackIntegration-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#DeleteSlackIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#DeleteSlackIntegration-429-v1)


OK
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby-legacy)


#####  Delete a Slack integration
Copy
```
                  # Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a Slack integration
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.delete_integration('slack')

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

* * *
## [Get all channels in a Slack integration](https://docs.datadoghq.com/api/latest/slack-integration/#get-all-channels-in-a-slack-integration)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/slack-integration/#get-all-channels-in-a-slack-integration-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels
### Overview
Get a list of all channels configured for your Datadog-Slack integration. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_name [_required_]
string
Your Slack account name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannels-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannels-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannels-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannels-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannels-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


A list of configured Slack channels.
Field
Type
Description
display
object
Configuration options for what is shown in an alert event message.
message
boolean
Show the main body of the alert event.
default: `true`
mute_buttons
boolean
Show interactive buttons to mute the alerting monitor.
notified
boolean
Show the list of @-handles in the alert event.
default: `true`
snapshot
boolean
Show the alert event's snapshot image.
default: `true`
tags
boolean
Show the scopes on which the monitor alerted.
default: `true`
name
string
Your channel name.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=typescript)


#####  Get all channels in a Slack integration
Copy
```
                  # Path parameters  
export account_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all channels in a Slack integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all channels in a Slack integration
```
# Get all channels in a Slack integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new
p api_instance.get_slack_integration_channels("account_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all channels in a Slack integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all channels in a Slack integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get all channels in a Slack integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get all channels in a Slack integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Add channels to Slack integration](https://docs.datadoghq.com/api/latest/slack-integration/#add-channels-to-slack-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/slack-integration/#add-channels-to-slack-integration-v1)


PUT https://api.ap1.datadoghq.com/api/v1/integration/slackhttps://api.ap2.datadoghq.com/api/v1/integration/slackhttps://api.datadoghq.eu/api/v1/integration/slackhttps://api.ddog-gov.com/api/v1/integration/slackhttps://api.datadoghq.com/api/v1/integration/slackhttps://api.us3.datadoghq.com/api/v1/integration/slackhttps://api.us5.datadoghq.com/api/v1/integration/slack
### Overview
Add channels to your existing Datadog-Slack integration.
This method updates your integration configuration by **replacing** your current configuration with the new one sent to your Datadog organization.
### Request
#### Body Data (required)
Update an existing Datadog-Slack integration request body.
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Field
Type
Description
channels
[object]
An array of slack channel configurations.
account [_required_]
string
Account to which the channel belongs to.
channel_name [_required_]
string
Your channel name.
transfer_all_user_comments
boolean
To be notified for every comment on a graph, set it to `true`. If set to `False` use the `@slack-channel_name` syntax for comments to be posted to slack.
```
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

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegration-204-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegration-429-v1)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)


#####  Add channels to Slack integration
Copy
```
                  # Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
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

                
```

* * *
## [Create a Slack integration channel](https://docs.datadoghq.com/api/latest/slack-integration/#create-a-slack-integration-channel)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/slack-integration/#create-a-slack-integration-channel-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channelshttps://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels
### Overview
Add a channel to your Datadog-Slack integration. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_name [_required_]
string
Your Slack account name.
### Request
#### Body Data (required)
Payload describing Slack channel to be created
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Field
Type
Description
display
object
Configuration options for what is shown in an alert event message.
message
boolean
Show the main body of the alert event.
default: `true`
mute_buttons
boolean
Show interactive buttons to mute the alerting monitor.
notified
boolean
Show the list of @-handles in the alert event.
default: `true`
snapshot
boolean
Show the alert event's snapshot image.
default: `true`
tags
boolean
Show the scopes on which the monitor alerted.
default: `true`
name
string
Your channel name.
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegrationChannel-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegrationChannel-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegrationChannel-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegrationChannel-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegrationChannel-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


The Slack channel configuration.
Field
Type
Description
display
object
Configuration options for what is shown in an alert event message.
message
boolean
Show the main body of the alert event.
default: `true`
mute_buttons
boolean
Show interactive buttons to mute the alerting monitor.
notified
boolean
Show the list of @-handles in the alert event.
default: `true`
snapshot
boolean
Show the alert event's snapshot image.
default: `true`
tags
boolean
Show the scopes on which the monitor alerted.
default: `true`
name
string
Your channel name.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=typescript)


#####  Create a Slack integration channel
Copy
```
                  # Path parameters  
export account_name="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Create a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a Slack integration](https://docs.datadoghq.com/api/latest/slack-integration/#create-a-slack-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/slack-integration/#create-a-slack-integration-v1)


POST https://api.ap1.datadoghq.com/api/v1/integration/slackhttps://api.ap2.datadoghq.com/api/v1/integration/slackhttps://api.datadoghq.eu/api/v1/integration/slackhttps://api.ddog-gov.com/api/v1/integration/slackhttps://api.datadoghq.com/api/v1/integration/slackhttps://api.us3.datadoghq.com/api/v1/integration/slackhttps://api.us5.datadoghq.com/api/v1/integration/slack
### Overview
Create a Datadog-Slack integration. Once created, add a channel to it with the [Add channels to Slack integration endpoint](https://docs.datadoghq.com/api/?lang=bash#add-channels-to-slack-integration).
This method updates your integration configuration by **adding** your new configuration to the existing one in your Datadog organization.
### Request
#### Body Data (required)
Create Datadog-Slack integration request body.
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Field
Type
Description
service_hooks
[object]
The array of service hook objects.
account [_required_]
string
Your Slack account name.
url [_required_]
string
Your Slack service hook URL.
```
{
  "service_hooks": [
    {
      "account": "joe.doe",
      "url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    }
  ]
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegration-204-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegration-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#CreateSlackIntegration-429-v1)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby-legacy)


#####  Create a Slack integration
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
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

                
```

#####  Create a Slack integration
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

* * *
## [Get a Slack integration channel](https://docs.datadoghq.com/api/latest/slack-integration/#get-a-slack-integration-channel)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/slack-integration/#get-a-slack-integration-channel-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}
### Overview
Get a channel configured for your Datadog-Slack integration. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_name [_required_]
string
Your Slack account name.
channel_name [_required_]
string
The name of the Slack channel being operated on.
### Response
  * [200](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannel-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannel-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannel-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannel-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegrationChannel-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


The Slack channel configuration.
Field
Type
Description
display
object
Configuration options for what is shown in an alert event message.
message
boolean
Show the main body of the alert event.
default: `true`
mute_buttons
boolean
Show interactive buttons to mute the alerting monitor.
notified
boolean
Show the list of @-handles in the alert event.
default: `true`
snapshot
boolean
Show the alert event's snapshot image.
default: `true`
tags
boolean
Show the scopes on which the monitor alerted.
default: `true`
name
string
Your channel name.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=typescript)


#####  Get a Slack integration channel
Copy
```
                  # Path parameters  
export account_name="CHANGE_ME"  
export channel_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels/${channel_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a Slack integration channel
```
# Get a Slack integration channel returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new
p api_instance.get_slack_integration_channel("account_name", "channel_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get info about a Slack integration](https://docs.datadoghq.com/api/latest/slack-integration/#get-info-about-a-slack-integration)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/slack-integration/#get-info-about-a-slack-integration-v1)


GET https://api.ap1.datadoghq.com/api/v1/integration/slackhttps://api.ap2.datadoghq.com/api/v1/integration/slackhttps://api.datadoghq.eu/api/v1/integration/slackhttps://api.ddog-gov.com/api/v1/integration/slackhttps://api.datadoghq.com/api/v1/integration/slackhttps://api.us3.datadoghq.com/api/v1/integration/slackhttps://api.us5.datadoghq.com/api/v1/integration/slack
### Overview
Get all information about your Datadog-Slack integration.
### Response
  * [200](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegration-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegration-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegration-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegration-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#GetSlackIntegration-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby-legacy)


#####  Get info about a Slack integration
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get info about a Slack integration
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.get_integration('slack')

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

* * *
## [Update a Slack integration channel](https://docs.datadoghq.com/api/latest/slack-integration/#update-a-slack-integration-channel)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/slack-integration/#update-a-slack-integration-channel-v1)


PATCH https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}
### Overview
Update a channel used in your Datadog-Slack integration. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_name [_required_]
string
Your Slack account name.
channel_name [_required_]
string
The name of the Slack channel being operated on.
### Request
#### Body Data (required)
Payload describing fields and values to be updated.
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Field
Type
Description
display
object
Configuration options for what is shown in an alert event message.
message
boolean
Show the main body of the alert event.
default: `true`
mute_buttons
boolean
Show interactive buttons to mute the alerting monitor.
notified
boolean
Show the list of @-handles in the alert event.
default: `true`
snapshot
boolean
Show the alert event's snapshot image.
default: `true`
tags
boolean
Show the scopes on which the monitor alerted.
default: `true`
name
string
Your channel name.
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegrationChannel-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegrationChannel-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegrationChannel-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegrationChannel-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#UpdateSlackIntegrationChannel-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


The Slack channel configuration.
Field
Type
Description
display
object
Configuration options for what is shown in an alert event message.
message
boolean
Show the main body of the alert event.
default: `true`
mute_buttons
boolean
Show interactive buttons to mute the alerting monitor.
notified
boolean
Show the list of @-handles in the alert event.
default: `true`
snapshot
boolean
Show the alert event's snapshot image.
default: `true`
tags
boolean
Show the scopes on which the monitor alerted.
default: `true`
name
string
Your channel name.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=typescript)


#####  Update a Slack integration channel
Copy
```
                  # Path parameters  
export account_name="CHANGE_ME"  
export channel_name="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels/${channel_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Update a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Remove a Slack integration channel](https://docs.datadoghq.com/api/latest/slack-integration/#remove-a-slack-integration-channel)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/slack-integration/#remove-a-slack-integration-channel-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.ap2.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.datadoghq.eu/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.ddog-gov.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.us3.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}
### Overview
Remove a channel from your Datadog-Slack integration. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_name [_required_]
string
Your Slack account name.
channel_name [_required_]
string
The name of the Slack channel being operated on.
### Response
  * [204](https://docs.datadoghq.com/api/latest/slack-integration/#RemoveSlackIntegrationChannel-204-v1)
  * [400](https://docs.datadoghq.com/api/latest/slack-integration/#RemoveSlackIntegrationChannel-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/slack-integration/#RemoveSlackIntegrationChannel-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/slack-integration/#RemoveSlackIntegrationChannel-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/slack-integration/#RemoveSlackIntegrationChannel-429-v1)


The channel was removed successfully.
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Item Not Found
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/slack-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/slack-integration/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/slack-integration/?code-lang=typescript)


#####  Remove a Slack integration channel
Copy
```
                  # Path parameters  
export account_name="CHANGE_ME"  
export channel_name="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/slack/configuration/accounts/${account_name}/channels/${channel_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Remove a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Remove a Slack integration channel
```
# Remove a Slack integration channel returns "The channel was removed successfully." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::SlackIntegrationAPI.new
api_instance.remove_slack_integration_channel("account_name", "channel_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Remove a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Remove a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Remove a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Remove a Slack integration channel
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=02b90dc1-d04d-42fe-98f1-8f7ab7a82636&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=73736a74-ae36-4955-88aa-fb424771d23e&pt=Slack%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fslack-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=02b90dc1-d04d-42fe-98f1-8f7ab7a82636&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=73736a74-ae36-4955-88aa-fb424771d23e&pt=Slack%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fslack-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
Feedback
## Was this page helpful?
Yes 🎉
No 👎
Next
![](https://survey-images.hotjar.com/surveys/logo/90f40352a7464c849f5ce82ccd0e758d)
