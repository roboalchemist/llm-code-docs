# Source: https://docs.datadoghq.com/api/latest/microsoft-teams-integration/

# Microsoft Teams Integration
Configure your [Datadog Microsoft Teams integration](https://docs.datadoghq.com/integrations/microsoft_teams/) directly through the Datadog API. Note: These endpoints do not support legacy connector handles.
## [Create tenant-based handle](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#create-tenant-based-handle)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#create-tenant-based-handle-v2)


POST https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles
### Overview
Create a tenant-based handle in the Datadog Microsoft Teams integration.
### Request
#### Body Data (required)
Tenant-based handle payload.
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Field
Type
Description
data [_required_]
object
Tenant-based handle data from a response.
attributes [_required_]
object
Tenant-based handle attributes.
channel_id [_required_]
string
Channel id.
name [_required_]
string
Tenant-based handle name.
team_id [_required_]
string
Team id.
tenant_id [_required_]
string
Tenant id.
type [_required_]
enum
Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle`
default: `tenant-based-handle`
```
{
  "data": {
    "attributes": {
      "channel_id": "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
      "name": "Example-Microsoft-Teams-Integration",
      "team_id": "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
      "tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97"
    },
    "type": "tenant-based-handle"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateTenantBasedHandle-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateTenantBasedHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateTenantBasedHandle-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateTenantBasedHandle-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateTenantBasedHandle-409-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateTenantBasedHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateTenantBasedHandle-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response of a tenant-based handle.
Field
Type
Description
data [_required_]
object
Tenant-based handle data from a response.
attributes
object
Tenant-based handle attributes.
channel_id
string
Channel id.
name
string
Tenant-based handle name.
team_id
string
Team id.
tenant_id
string
Tenant id.
id
string
The ID of the tenant-based handle.
type
enum
Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle`
default: `tenant-based-handle`
```
{
  "data": {
    "attributes": {
      "channel_id": "fake-channel-id",
      "name": "fake-handle-name",
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "tenant-based-handle"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Create api handle returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "channel_id": "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
      "name": "Example-Microsoft-Teams-Integration",
      "team_id": "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
      "tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97"
    },
    "type": "tenant-based-handle"
  }
}
EOF  

                        
```

#####  Create api handle returns "CREATED" response
```
// Create api handle returns "CREATED" response

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
	body := datadogV2.MicrosoftTeamsCreateTenantBasedHandleRequest{
		Data: datadogV2.MicrosoftTeamsTenantBasedHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsTenantBasedHandleRequestAttributes{
				ChannelId: "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
				Name:      "Example-Microsoft-Teams-Integration",
				TeamId:    "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
				TenantId:  "4d3bac44-0230-4732-9e70-cc00736f0a97",
			},
			Type: datadogV2.MICROSOFTTEAMSTENANTBASEDHANDLETYPE_TENANT_BASED_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.CreateTenantBasedHandle(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.CreateTenantBasedHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.CreateTenantBasedHandle`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create api handle returns "CREATED" response
```
// Create api handle returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsCreateTenantBasedHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleRequestAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleRequestData;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    MicrosoftTeamsCreateTenantBasedHandleRequest body =
        new MicrosoftTeamsCreateTenantBasedHandleRequest()
            .data(
                new MicrosoftTeamsTenantBasedHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsTenantBasedHandleRequestAttributes()
                            .channelId(
                                "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2")
                            .name("Example-Microsoft-Teams-Integration")
                            .teamId("e5f50a58-c929-4fb3-8866-e2cd836de3c2")
                            .tenantId("4d3bac44-0230-4732-9e70-cc00736f0a97"))
                    .type(MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE));

    try {
      MicrosoftTeamsTenantBasedHandleResponse result = apiInstance.createTenantBasedHandle(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#createTenantBasedHandle");
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

#####  Create api handle returns "CREATED" response
```
"""
Create api handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_create_tenant_based_handle_request import (
    MicrosoftTeamsCreateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_request_attributes import (
    MicrosoftTeamsTenantBasedHandleRequestAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_request_data import (
    MicrosoftTeamsTenantBasedHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType

body = MicrosoftTeamsCreateTenantBasedHandleRequest(
    data=MicrosoftTeamsTenantBasedHandleRequestData(
        attributes=MicrosoftTeamsTenantBasedHandleRequestAttributes(
            channel_id="19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
            name="Example-Microsoft-Teams-Integration",
            team_id="e5f50a58-c929-4fb3-8866-e2cd836de3c2",
            tenant_id="4d3bac44-0230-4732-9e70-cc00736f0a97",
        ),
        type=MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_tenant_based_handle(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create api handle returns "CREATED" response
```
# Create api handle returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

body = DatadogAPIClient::V2::MicrosoftTeamsCreateTenantBasedHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleRequestAttributes.new({
      channel_id: "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
      name: "Example-Microsoft-Teams-Integration",
      team_id: "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
      tenant_id: "4d3bac44-0230-4732-9e70-cc00736f0a97",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
  }),
})
p api_instance.create_tenant_based_handle(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create api handle returns "CREATED" response
```
// Create api handle returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsCreateTenantBasedHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleRequestAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleRequestData;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleType;

#[tokio::main]
async fn main() {
    let body = MicrosoftTeamsCreateTenantBasedHandleRequest::new(
        MicrosoftTeamsTenantBasedHandleRequestData::new(
            MicrosoftTeamsTenantBasedHandleRequestAttributes::new(
                "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2".to_string(),
                "Example-Microsoft-Teams-Integration".to_string(),
                "e5f50a58-c929-4fb3-8866-e2cd836de3c2".to_string(),
                "4d3bac44-0230-4732-9e70-cc00736f0a97".to_string(),
            ),
            MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api.create_tenant_based_handle(body).await;
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

#####  Create api handle returns "CREATED" response
```
/**
 * Create api handle returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiCreateTenantBasedHandleRequest = {
  body: {
    data: {
      attributes: {
        channelId:
          "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
        name: "Example-Microsoft-Teams-Integration",
        teamId: "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
        tenantId: "4d3bac44-0230-4732-9e70-cc00736f0a97",
      },
      type: "tenant-based-handle",
    },
  },
};

apiInstance
  .createTenantBasedHandle(params)
  .then((data: v2.MicrosoftTeamsTenantBasedHandleResponse) => {
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
## [Create Workflows webhook handle](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#create-workflows-webhook-handle)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#create-workflows-webhook-handle-v2)


POST https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles
### Overview
Create a Workflows webhook handle in the Datadog Microsoft Teams integration.
### Request
#### Body Data (required)
Workflows Webhook handle payload.
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Field
Type
Description
data [_required_]
object
Workflows Webhook handle data from a response.
attributes [_required_]
object
Workflows Webhook handle attributes.
name [_required_]
string
Workflows Webhook handle name.
url [_required_]
string
Workflows Webhook URL.
type [_required_]
enum
Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle`
default: `workflows-webhook-handle`
```
{
  "data": {
    "attributes": {
      "name": "Example-Microsoft-Teams-Integration",
      "url": "https://example.logic.azure.com/workflows/123"
    },
    "type": "workflows-webhook-handle"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateWorkflowsWebhookHandle-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateWorkflowsWebhookHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateWorkflowsWebhookHandle-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateWorkflowsWebhookHandle-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateWorkflowsWebhookHandle-409-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateWorkflowsWebhookHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#CreateWorkflowsWebhookHandle-429-v2)


CREATED
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response of a Workflows webhook handle.
Field
Type
Description
data [_required_]
object
Workflows Webhook handle data from a response.
attributes
object
Workflows Webhook handle attributes.
name
string
Workflows Webhook handle name.
id
string
The ID of the Workflows webhook handle.
type
enum
Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle`
default: `workflows-webhook-handle`
```
{
  "data": {
    "attributes": {
      "name": "fake-handle-name"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "workflows-webhook-handle"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Create workflow webhook handle returns "CREATED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-Microsoft-Teams-Integration",
      "url": "https://example.logic.azure.com/workflows/123"
    },
    "type": "workflows-webhook-handle"
  }
}
EOF  

                        
```

#####  Create workflow webhook handle returns "CREATED" response
```
// Create workflow webhook handle returns "CREATED" response

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
	body := datadogV2.MicrosoftTeamsCreateWorkflowsWebhookHandleRequest{
		Data: datadogV2.MicrosoftTeamsWorkflowsWebhookHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes{
				Name: "Example-Microsoft-Teams-Integration",
				Url:  "https://example.logic.azure.com/workflows/123",
			},
			Type: datadogV2.MICROSOFTTEAMSWORKFLOWSWEBHOOKHANDLETYPE_WORKFLOWS_WEBHOOK_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.CreateWorkflowsWebhookHandle(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.CreateWorkflowsWebhookHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.CreateWorkflowsWebhookHandle`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create workflow webhook handle returns "CREATED" response
```
// Create workflow webhook handle returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsCreateWorkflowsWebhookHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleRequestData;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    MicrosoftTeamsCreateWorkflowsWebhookHandleRequest body =
        new MicrosoftTeamsCreateWorkflowsWebhookHandleRequest()
            .data(
                new MicrosoftTeamsWorkflowsWebhookHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes()
                            .name("Example-Microsoft-Teams-Integration")
                            .url("https://example.logic.azure.com/workflows/123"))
                    .type(MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE));

    try {
      MicrosoftTeamsWorkflowsWebhookHandleResponse result =
          apiInstance.createWorkflowsWebhookHandle(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#createWorkflowsWebhookHandle");
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

#####  Create workflow webhook handle returns "CREATED" response
```
"""
Create workflow webhook handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_create_workflows_webhook_handle_request import (
    MicrosoftTeamsCreateWorkflowsWebhookHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_request_attributes import (
    MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_request_data import (
    MicrosoftTeamsWorkflowsWebhookHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
    MicrosoftTeamsWorkflowsWebhookHandleType,
)

body = MicrosoftTeamsCreateWorkflowsWebhookHandleRequest(
    data=MicrosoftTeamsWorkflowsWebhookHandleRequestData(
        attributes=MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes(
            name="Example-Microsoft-Teams-Integration",
            url="https://example.logic.azure.com/workflows/123",
        ),
        type=MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_workflows_webhook_handle(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create workflow webhook handle returns "CREATED" response
```
# Create workflow webhook handle returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

body = DatadogAPIClient::V2::MicrosoftTeamsCreateWorkflowsWebhookHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes.new({
      name: "Example-Microsoft-Teams-Integration",
      url: "https://example.logic.azure.com/workflows/123",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
  }),
})
p api_instance.create_workflows_webhook_handle(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create workflow webhook handle returns "CREATED" response
```
// Create workflow webhook handle returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsCreateWorkflowsWebhookHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleRequestData;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleType;

#[tokio::main]
async fn main() {
    let body = MicrosoftTeamsCreateWorkflowsWebhookHandleRequest::new(
        MicrosoftTeamsWorkflowsWebhookHandleRequestData::new(
            MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes::new(
                "Example-Microsoft-Teams-Integration".to_string(),
                "https://example.logic.azure.com/workflows/123".to_string(),
            ),
            MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api.create_workflows_webhook_handle(body).await;
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

#####  Create workflow webhook handle returns "CREATED" response
```
/**
 * Create workflow webhook handle returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiCreateWorkflowsWebhookHandleRequest =
  {
    body: {
      data: {
        attributes: {
          name: "Example-Microsoft-Teams-Integration",
          url: "https://example.logic.azure.com/workflows/123",
        },
        type: "workflows-webhook-handle",
      },
    },
  };

apiInstance
  .createWorkflowsWebhookHandle(params)
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandleResponse) => {
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
## [Delete tenant-based handle](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#delete-tenant-based-handle)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#delete-tenant-based-handle-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}
### Overview
Delete a tenant-based handle from the Datadog Microsoft Teams integration.
### Arguments
#### Path Parameters
Name
Type
Description
handle_id [_required_]
string
Your tenant-based handle id.
### Response
  * [204](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteTenantBasedHandle-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteTenantBasedHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteTenantBasedHandle-403-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteTenantBasedHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteTenantBasedHandle-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Delete tenant-based handle
Copy
```
                  # Path parameters  
export handle_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/${handle_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete tenant-based handle
```
"""
Delete tenant-based handle returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    api_instance.delete_tenant_based_handle(
        handle_id="handle_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete tenant-based handle
```
# Delete tenant-based handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
api_instance.delete_tenant_based_handle("handle_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete tenant-based handle
```
// Delete tenant-based handle returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	r, err := api.DeleteTenantBasedHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.DeleteTenantBasedHandle`: %v\n", err)
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

#####  Delete tenant-based handle
```
// Delete tenant-based handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      apiInstance.deleteTenantBasedHandle("handle_id");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#deleteTenantBasedHandle");
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

#####  Delete tenant-based handle
```
// Delete tenant-based handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_tenant_based_handle("handle_id".to_string())
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

#####  Delete tenant-based handle
```
/**
 * Delete tenant-based handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiDeleteTenantBasedHandleRequest = {
  handleId: "handle_id",
};

apiInstance
  .deleteTenantBasedHandle(params)
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
## [Delete Workflows webhook handle](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#delete-workflows-webhook-handle)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#delete-workflows-webhook-handle-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}
### Overview
Delete a Workflows webhook handle from the Datadog Microsoft Teams integration.
### Arguments
#### Path Parameters
Name
Type
Description
handle_id [_required_]
string
Your Workflows webhook handle id.
### Response
  * [204](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteWorkflowsWebhookHandle-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteWorkflowsWebhookHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteWorkflowsWebhookHandle-403-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteWorkflowsWebhookHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#DeleteWorkflowsWebhookHandle-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Delete Workflows webhook handle
Copy
```
                  # Path parameters  
export handle_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/${handle_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete Workflows webhook handle
```
"""
Delete Workflows webhook handle returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    api_instance.delete_workflows_webhook_handle(
        handle_id="handle_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete Workflows webhook handle
```
# Delete Workflows webhook handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
api_instance.delete_workflows_webhook_handle("handle_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete Workflows webhook handle
```
// Delete Workflows webhook handle returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	r, err := api.DeleteWorkflowsWebhookHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.DeleteWorkflowsWebhookHandle`: %v\n", err)
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

#####  Delete Workflows webhook handle
```
// Delete Workflows webhook handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      apiInstance.deleteWorkflowsWebhookHandle("handle_id");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#deleteWorkflowsWebhookHandle");
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

#####  Delete Workflows webhook handle
```
// Delete Workflows webhook handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_workflows_webhook_handle("handle_id".to_string())
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

#####  Delete Workflows webhook handle
```
/**
 * Delete Workflows webhook handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiDeleteWorkflowsWebhookHandleRequest =
  {
    handleId: "handle_id",
  };

apiInstance
  .deleteWorkflowsWebhookHandle(params)
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
## [Get all tenant-based handles](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-all-tenant-based-handles)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-all-tenant-based-handles-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handleshttps://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles
### Overview
Get a list of all tenant-based handles from the Datadog Microsoft Teams integration.
### Arguments
#### Query Strings
Name
Type
Description
tenant_id
string
Your tenant id.
name
string
Your tenant-based handle name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListTenantBasedHandles-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListTenantBasedHandles-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListTenantBasedHandles-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListTenantBasedHandles-404-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListTenantBasedHandles-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListTenantBasedHandles-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response with a list of tenant-based handles.
Field
Type
Description
data [_required_]
[object]
An array of tenant-based handles.
attributes
object
Tenant-based handle attributes.
channel_id
string
Channel id.
channel_name
string
Channel name.
name
string
Tenant-based handle name.
team_id
string
Team id.
team_name
string
Team name.
tenant_id
string
Tenant id.
tenant_name
string
Tenant name.
id
string
The ID of the tenant-based handle.
type
enum
Tenant-based handle resource type. Allowed enum values: `ms-teams-tenant-based-handle-info`
default: `ms-teams-tenant-based-handle-info`
```
{
  "data": [
    {
      "attributes": {
        "channel_id": "fake-channel-id",
        "channel_name": "fake-channel-name",
        "name": "fake-handle-name",
        "team_id": "00000000-0000-0000-0000-000000000000",
        "team_name": "fake-team-name",
        "tenant_id": "00000000-0000-0000-0000-000000000001",
        "tenant_name": "fake-tenant-name"
      },
      "id": "596da4af-0563-4097-90ff-07230c3f9db3",
      "type": "ms-teams-tenant-based-handle-info"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Get all tenant-based handles
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all tenant-based handles
```
"""
Get all tenant-based handles returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.list_tenant_based_handles()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all tenant-based handles
```
# Get all tenant-based handles returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.list_tenant_based_handles()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all tenant-based handles
```
// Get all tenant-based handles returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.ListTenantBasedHandles(ctx, *datadogV2.NewListTenantBasedHandlesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.ListTenantBasedHandles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.ListTenantBasedHandles`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all tenant-based handles
```
// Get all tenant-based handles returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandlesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsTenantBasedHandlesResponse result = apiInstance.listTenantBasedHandles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#listTenantBasedHandles");
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

#####  Get all tenant-based handles
```
// Get all tenant-based handles returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::ListTenantBasedHandlesOptionalParams;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .list_tenant_based_handles(ListTenantBasedHandlesOptionalParams::default())
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

#####  Get all tenant-based handles
```
/**
 * Get all tenant-based handles returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

apiInstance
  .listTenantBasedHandles()
  .then((data: v2.MicrosoftTeamsTenantBasedHandlesResponse) => {
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
## [Get all Workflows webhook handles](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-all-workflows-webhook-handles)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-all-workflows-webhook-handles-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handleshttps://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles
### Overview
Get a list of all Workflows webhook handles from the Datadog Microsoft Teams integration.
### Arguments
#### Query Strings
Name
Type
Description
name
string
Your Workflows webhook handle name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListWorkflowsWebhookHandles-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListWorkflowsWebhookHandles-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListWorkflowsWebhookHandles-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListWorkflowsWebhookHandles-404-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListWorkflowsWebhookHandles-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#ListWorkflowsWebhookHandles-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response with a list of Workflows webhook handles.
Field
Type
Description
data [_required_]
[object]
An array of Workflows webhook handles.
attributes
object
Workflows Webhook handle attributes.
name
string
Workflows Webhook handle name.
id
string
The ID of the Workflows webhook handle.
type
enum
Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle`
default: `workflows-webhook-handle`
```
{
  "data": [
    {
      "attributes": {
        "name": "fake-handle-name"
      },
      "id": "596da4af-0563-4097-90ff-07230c3f9db3",
      "type": "workflows-webhook-handle"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Get all Workflows webhook handles
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all Workflows webhook handles
```
"""
Get all Workflows webhook handles returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.list_workflows_webhook_handles()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all Workflows webhook handles
```
# Get all Workflows webhook handles returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.list_workflows_webhook_handles()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all Workflows webhook handles
```
// Get all Workflows webhook handles returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.ListWorkflowsWebhookHandles(ctx, *datadogV2.NewListWorkflowsWebhookHandlesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.ListWorkflowsWebhookHandles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.ListWorkflowsWebhookHandles`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all Workflows webhook handles
```
// Get all Workflows webhook handles returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandlesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsWorkflowsWebhookHandlesResponse result =
          apiInstance.listWorkflowsWebhookHandles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#listWorkflowsWebhookHandles");
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

#####  Get all Workflows webhook handles
```
// Get all Workflows webhook handles returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::ListWorkflowsWebhookHandlesOptionalParams;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .list_workflows_webhook_handles(ListWorkflowsWebhookHandlesOptionalParams::default())
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

#####  Get all Workflows webhook handles
```
/**
 * Get all Workflows webhook handles returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

apiInstance
  .listWorkflowsWebhookHandles()
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandlesResponse) => {
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
## [Get channel information by name](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-channel-information-by-name)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-channel-information-by-name-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}
### Overview
Get the tenant, team, and channel ID of a channel in the Datadog Microsoft Teams integration.
### Arguments
#### Path Parameters
Name
Type
Description
tenant_name [_required_]
string
Your tenant name.
team_name [_required_]
string
Your team name.
channel_name [_required_]
string
Your channel name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetChannelByName-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetChannelByName-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetChannelByName-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetChannelByName-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetChannelByName-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response with channel, team, and tenant ID information.
Field
Type
Description
data
object
Channel data from a response.
attributes
object
Channel attributes.
is_primary
boolean
Indicates if this is the primary channel.
team_id
string
Team id.
tenant_id
string
Tenant id.
id
string
The ID of the channel.
type
enum
Channel info resource type. Allowed enum values: `ms-teams-channel-info`
default: `ms-teams-channel-info`
```
{
  "data": {
    "attributes": {
      "is_primary": true,
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "19:b41k24b14bn1nwffkernfkwrnfneubgkr@thread.tacv2",
    "type": "ms-teams-channel-info"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Get channel information by name
Copy
```
                  # Path parameters  
export tenant_name="CHANGE_ME"  
export team_name="CHANGE_ME"  
export channel_name="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/${tenant_name}/${team_name}/${channel_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get channel information by name
```
"""
Get channel information by name returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_channel_by_name(
        tenant_name="tenant_name",
        team_name="team_name",
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

#####  Get channel information by name
```
# Get channel information by name returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.get_channel_by_name("tenant_name", "team_name", "channel_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get channel information by name
```
// Get channel information by name returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.GetChannelByName(ctx, "tenant_name", "team_name", "channel_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.GetChannelByName`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.GetChannelByName`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get channel information by name
```
// Get channel information by name returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsGetChannelByNameResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsGetChannelByNameResponse result =
          apiInstance.getChannelByName("tenant_name", "team_name", "channel_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrosoftTeamsIntegrationApi#getChannelByName");
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

#####  Get channel information by name
```
// Get channel information by name returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .get_channel_by_name(
            "tenant_name".to_string(),
            "team_name".to_string(),
            "channel_name".to_string(),
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

#####  Get channel information by name
```
/**
 * Get channel information by name returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiGetChannelByNameRequest = {
  tenantName: "tenant_name",
  teamName: "team_name",
  channelName: "channel_name",
};

apiInstance
  .getChannelByName(params)
  .then((data: v2.MicrosoftTeamsGetChannelByNameResponse) => {
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
## [Get tenant-based handle information](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-tenant-based-handle-information)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-tenant-based-handle-information-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}
### Overview
Get the tenant, team, and channel information of a tenant-based handle from the Datadog Microsoft Teams integration.
### Arguments
#### Path Parameters
Name
Type
Description
handle_id [_required_]
string
Your tenant-based handle id.
### Response
  * [200](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetTenantBasedHandle-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetTenantBasedHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetTenantBasedHandle-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetTenantBasedHandle-404-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetTenantBasedHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetTenantBasedHandle-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response of a tenant-based handle.
Field
Type
Description
data [_required_]
object
Tenant-based handle data from a response.
attributes
object
Tenant-based handle attributes.
channel_id
string
Channel id.
name
string
Tenant-based handle name.
team_id
string
Team id.
tenant_id
string
Tenant id.
id
string
The ID of the tenant-based handle.
type
enum
Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle`
default: `tenant-based-handle`
```
{
  "data": {
    "attributes": {
      "channel_id": "fake-channel-id",
      "name": "fake-handle-name",
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "tenant-based-handle"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Get tenant-based handle information
Copy
```
                  # Path parameters  
export handle_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/${handle_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get tenant-based handle information
```
"""
Get tenant-based handle information returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_tenant_based_handle(
        handle_id="handle_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get tenant-based handle information
```
# Get tenant-based handle information returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.get_tenant_based_handle("handle_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get tenant-based handle information
```
// Get tenant-based handle information returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.GetTenantBasedHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.GetTenantBasedHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.GetTenantBasedHandle`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get tenant-based handle information
```
// Get tenant-based handle information returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsTenantBasedHandleResponse result =
          apiInstance.getTenantBasedHandle("handle_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#getTenantBasedHandle");
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

#####  Get tenant-based handle information
```
// Get tenant-based handle information returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api.get_tenant_based_handle("handle_id".to_string()).await;
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

#####  Get tenant-based handle information
```
/**
 * Get tenant-based handle information returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiGetTenantBasedHandleRequest = {
  handleId: "handle_id",
};

apiInstance
  .getTenantBasedHandle(params)
  .then((data: v2.MicrosoftTeamsTenantBasedHandleResponse) => {
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
## [Get Workflows webhook handle information](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-workflows-webhook-handle-information)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#get-workflows-webhook-handle-information-v2)


GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}
### Overview
Get the name of a Workflows webhook handle from the Datadog Microsoft Teams integration.
### Arguments
#### Path Parameters
Name
Type
Description
handle_id [_required_]
string
Your Workflows webhook handle id.
### Response
  * [200](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetWorkflowsWebhookHandle-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetWorkflowsWebhookHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetWorkflowsWebhookHandle-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetWorkflowsWebhookHandle-404-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetWorkflowsWebhookHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#GetWorkflowsWebhookHandle-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response of a Workflows webhook handle.
Field
Type
Description
data [_required_]
object
Workflows Webhook handle data from a response.
attributes
object
Workflows Webhook handle attributes.
name
string
Workflows Webhook handle name.
id
string
The ID of the Workflows webhook handle.
type
enum
Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle`
default: `workflows-webhook-handle`
```
{
  "data": {
    "attributes": {
      "name": "fake-handle-name"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "workflows-webhook-handle"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Get Workflows webhook handle information
Copy
```
                  # Path parameters  
export handle_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/${handle_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Workflows webhook handle information
```
"""
Get Workflows webhook handle information returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_workflows_webhook_handle(
        handle_id="handle_id",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get Workflows webhook handle information
```
# Get Workflows webhook handle information returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.get_workflows_webhook_handle("handle_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get Workflows webhook handle information
```
// Get Workflows webhook handle information returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.GetWorkflowsWebhookHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.GetWorkflowsWebhookHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.GetWorkflowsWebhookHandle`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get Workflows webhook handle information
```
// Get Workflows webhook handle information returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsWorkflowsWebhookHandleResponse result =
          apiInstance.getWorkflowsWebhookHandle("handle_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#getWorkflowsWebhookHandle");
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

#####  Get Workflows webhook handle information
```
// Get Workflows webhook handle information returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .get_workflows_webhook_handle("handle_id".to_string())
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

#####  Get Workflows webhook handle information
```
/**
 * Get Workflows webhook handle information returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiGetWorkflowsWebhookHandleRequest =
  {
    handleId: "handle_id",
  };

apiInstance
  .getWorkflowsWebhookHandle(params)
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandleResponse) => {
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
## [Update tenant-based handle](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#update-tenant-based-handle)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#update-tenant-based-handle-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}
### Overview
Update a tenant-based handle from the Datadog Microsoft Teams integration.
### Arguments
#### Path Parameters
Name
Type
Description
handle_id [_required_]
string
Your tenant-based handle id.
### Request
#### Body Data (required)
Tenant-based handle payload.
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Field
Type
Description
data [_required_]
object
Tenant-based handle data from a response.
attributes [_required_]
object
Tenant-based handle attributes.
channel_id
string
Channel id.
name
string
Tenant-based handle name.
team_id
string
Team id.
tenant_id
string
Tenant id.
type [_required_]
enum
Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle`
default: `tenant-based-handle`
```
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "tenant-based-handle"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateTenantBasedHandle-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateTenantBasedHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateTenantBasedHandle-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateTenantBasedHandle-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateTenantBasedHandle-409-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateTenantBasedHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateTenantBasedHandle-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response of a tenant-based handle.
Field
Type
Description
data [_required_]
object
Tenant-based handle data from a response.
attributes
object
Tenant-based handle attributes.
channel_id
string
Channel id.
name
string
Tenant-based handle name.
team_id
string
Team id.
tenant_id
string
Tenant id.
id
string
The ID of the tenant-based handle.
type
enum
Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle`
default: `tenant-based-handle`
```
{
  "data": {
    "attributes": {
      "channel_id": "fake-channel-id",
      "name": "fake-handle-name",
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "tenant-based-handle"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Update api handle returns "OK" response
Copy
```
                          # Path parameters  
export handle_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/${handle_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "tenant-based-handle"
  }
}
EOF  

                        
```

#####  Update api handle returns "OK" response
```
// Update api handle returns "OK" response

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
	// there is a valid "tenant_based_handle" in the system
	TenantBasedHandleDataID := os.Getenv("TENANT_BASED_HANDLE_DATA_ID")

	body := datadogV2.MicrosoftTeamsUpdateTenantBasedHandleRequest{
		Data: datadogV2.MicrosoftTeamsUpdateTenantBasedHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsTenantBasedHandleAttributes{
				Name: datadog.PtrString("fake-handle-name--updated"),
			},
			Type: datadogV2.MICROSOFTTEAMSTENANTBASEDHANDLETYPE_TENANT_BASED_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.UpdateTenantBasedHandle(ctx, TenantBasedHandleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.UpdateTenantBasedHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.UpdateTenantBasedHandle`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update api handle returns "OK" response
```
// Update api handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleType;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateTenantBasedHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateTenantBasedHandleRequestData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    // there is a valid "tenant_based_handle" in the system
    String TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME =
        System.getenv("TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME");
    String TENANT_BASED_HANDLE_DATA_ID = System.getenv("TENANT_BASED_HANDLE_DATA_ID");

    MicrosoftTeamsUpdateTenantBasedHandleRequest body =
        new MicrosoftTeamsUpdateTenantBasedHandleRequest()
            .data(
                new MicrosoftTeamsUpdateTenantBasedHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsTenantBasedHandleAttributes()
                            .name("fake-handle-name--updated"))
                    .type(MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE));

    try {
      MicrosoftTeamsTenantBasedHandleResponse result =
          apiInstance.updateTenantBasedHandle(TENANT_BASED_HANDLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#updateTenantBasedHandle");
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

#####  Update api handle returns "OK" response
```
"""
Update api handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_attributes import (
    MicrosoftTeamsTenantBasedHandleAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType
from datadog_api_client.v2.model.microsoft_teams_update_tenant_based_handle_request import (
    MicrosoftTeamsUpdateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_tenant_based_handle_request_data import (
    MicrosoftTeamsUpdateTenantBasedHandleRequestData,
)

# there is a valid "tenant_based_handle" in the system
TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME = environ["TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME"]
TENANT_BASED_HANDLE_DATA_ID = environ["TENANT_BASED_HANDLE_DATA_ID"]

body = MicrosoftTeamsUpdateTenantBasedHandleRequest(
    data=MicrosoftTeamsUpdateTenantBasedHandleRequestData(
        attributes=MicrosoftTeamsTenantBasedHandleAttributes(
            name="fake-handle-name--updated",
        ),
        type=MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_tenant_based_handle(handle_id=TENANT_BASED_HANDLE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update api handle returns "OK" response
```
# Update api handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

# there is a valid "tenant_based_handle" in the system
TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME = ENV["TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME"]
TENANT_BASED_HANDLE_DATA_ID = ENV["TENANT_BASED_HANDLE_DATA_ID"]

body = DatadogAPIClient::V2::MicrosoftTeamsUpdateTenantBasedHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsUpdateTenantBasedHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleAttributes.new({
      name: "fake-handle-name--updated",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
  }),
})
p api_instance.update_tenant_based_handle(TENANT_BASED_HANDLE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update api handle returns "OK" response
```
// Update api handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleType;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateTenantBasedHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateTenantBasedHandleRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "tenant_based_handle" in the system
    let tenant_based_handle_data_id = std::env::var("TENANT_BASED_HANDLE_DATA_ID").unwrap();
    let body = MicrosoftTeamsUpdateTenantBasedHandleRequest::new(
        MicrosoftTeamsUpdateTenantBasedHandleRequestData::new(
            MicrosoftTeamsTenantBasedHandleAttributes::new()
                .name("fake-handle-name--updated".to_string()),
            MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .update_tenant_based_handle(tenant_based_handle_data_id.clone(), body)
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

#####  Update api handle returns "OK" response
```
/**
 * Update api handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

// there is a valid "tenant_based_handle" in the system
const TENANT_BASED_HANDLE_DATA_ID = process.env
  .TENANT_BASED_HANDLE_DATA_ID as string;

const params: v2.MicrosoftTeamsIntegrationApiUpdateTenantBasedHandleRequest = {
  body: {
    data: {
      attributes: {
        name: "fake-handle-name--updated",
      },
      type: "tenant-based-handle",
    },
  },
  handleId: TENANT_BASED_HANDLE_DATA_ID,
};

apiInstance
  .updateTenantBasedHandle(params)
  .then((data: v2.MicrosoftTeamsTenantBasedHandleResponse) => {
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
## [Update Workflows webhook handle](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#update-workflows-webhook-handle)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#update-workflows-webhook-handle-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}
### Overview
Update a Workflows webhook handle from the Datadog Microsoft Teams integration.
### Arguments
#### Path Parameters
Name
Type
Description
handle_id [_required_]
string
Your Workflows webhook handle id.
### Request
#### Body Data (required)
Workflows Webhook handle payload.
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Field
Type
Description
data [_required_]
object
Workflows Webhook handle data from a response.
attributes [_required_]
object
Workflows Webhook handle attributes.
name
string
Workflows Webhook handle name.
url
string
Workflows Webhook URL.
type [_required_]
enum
Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle`
default: `workflows-webhook-handle`
```
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "workflows-webhook-handle"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateWorkflowsWebhookHandle-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateWorkflowsWebhookHandle-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateWorkflowsWebhookHandle-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateWorkflowsWebhookHandle-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateWorkflowsWebhookHandle-409-v2)
  * [412](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateWorkflowsWebhookHandle-412-v2)
  * [429](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/#UpdateWorkflowsWebhookHandle-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


Response of a Workflows webhook handle.
Field
Type
Description
data [_required_]
object
Workflows Webhook handle data from a response.
attributes
object
Workflows Webhook handle attributes.
name
string
Workflows Webhook handle name.
id
string
The ID of the Workflows webhook handle.
type
enum
Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle`
default: `workflows-webhook-handle`
```
{
  "data": {
    "attributes": {
      "name": "fake-handle-name"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "workflows-webhook-handle"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Failed Precondition
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
  * [Example](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/?code-lang=typescript)


#####  Update workflow webhook handle returns "OK" response
Copy
```
                          # Path parameters  
export handle_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/${handle_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "workflows-webhook-handle"
  }
}
EOF  

                        
```

#####  Update workflow webhook handle returns "OK" response
```
// Update workflow webhook handle returns "OK" response

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
	// there is a valid "workflows_webhook_handle" in the system
	WorkflowsWebhookHandleDataID := os.Getenv("WORKFLOWS_WEBHOOK_HANDLE_DATA_ID")

	body := datadogV2.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest{
		Data: datadogV2.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsWorkflowsWebhookHandleAttributes{
				Name: datadog.PtrString("fake-handle-name--updated"),
			},
			Type: datadogV2.MICROSOFTTEAMSWORKFLOWSWEBHOOKHANDLETYPE_WORKFLOWS_WEBHOOK_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.UpdateWorkflowsWebhookHandle(ctx, WorkflowsWebhookHandleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.UpdateWorkflowsWebhookHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.UpdateWorkflowsWebhookHandle`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update workflow webhook handle returns "OK" response
```
// Update workflow webhook handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    // there is a valid "workflows_webhook_handle" in the system
    String WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME =
        System.getenv("WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME");
    String WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = System.getenv("WORKFLOWS_WEBHOOK_HANDLE_DATA_ID");

    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest body =
        new MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest()
            .data(
                new MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsWorkflowsWebhookHandleAttributes()
                            .name("fake-handle-name--updated"))
                    .type(MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE));

    try {
      MicrosoftTeamsWorkflowsWebhookHandleResponse result =
          apiInstance.updateWorkflowsWebhookHandle(WORKFLOWS_WEBHOOK_HANDLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#updateWorkflowsWebhookHandle");
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

#####  Update workflow webhook handle returns "OK" response
```
"""
Update workflow webhook handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_update_workflows_webhook_handle_request import (
    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_workflows_webhook_handle_request_data import (
    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_attributes import (
    MicrosoftTeamsWorkflowsWebhookHandleAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
    MicrosoftTeamsWorkflowsWebhookHandleType,
)

# there is a valid "workflows_webhook_handle" in the system
WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME = environ["WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME"]
WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = environ["WORKFLOWS_WEBHOOK_HANDLE_DATA_ID"]

body = MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest(
    data=MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData(
        attributes=MicrosoftTeamsWorkflowsWebhookHandleAttributes(
            name="fake-handle-name--updated",
        ),
        type=MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_workflows_webhook_handle(handle_id=WORKFLOWS_WEBHOOK_HANDLE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update workflow webhook handle returns "OK" response
```
# Update workflow webhook handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

# there is a valid "workflows_webhook_handle" in the system
WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME = ENV["WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME"]
WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = ENV["WORKFLOWS_WEBHOOK_HANDLE_DATA_ID"]

body = DatadogAPIClient::V2::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleAttributes.new({
      name: "fake-handle-name--updated",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
  }),
})
p api_instance.update_workflows_webhook_handle(WORKFLOWS_WEBHOOK_HANDLE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update workflow webhook handle returns "OK" response
```
// Update workflow webhook handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleType;

#[tokio::main]
async fn main() {
    // there is a valid "workflows_webhook_handle" in the system
    let workflows_webhook_handle_data_id =
        std::env::var("WORKFLOWS_WEBHOOK_HANDLE_DATA_ID").unwrap();
    let body = MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest::new(
        MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData::new(
            MicrosoftTeamsWorkflowsWebhookHandleAttributes::new()
                .name("fake-handle-name--updated".to_string()),
            MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .update_workflows_webhook_handle(workflows_webhook_handle_data_id.clone(), body)
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

#####  Update workflow webhook handle returns "OK" response
```
/**
 * Update workflow webhook handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

// there is a valid "workflows_webhook_handle" in the system
const WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = process.env
  .WORKFLOWS_WEBHOOK_HANDLE_DATA_ID as string;

const params: v2.MicrosoftTeamsIntegrationApiUpdateWorkflowsWebhookHandleRequest =
  {
    body: {
      data: {
        attributes: {
          name: "fake-handle-name--updated",
        },
        type: "workflows-webhook-handle",
      },
    },
    handleId: WORKFLOWS_WEBHOOK_HANDLE_DATA_ID,
  };

apiInstance
  .updateWorkflowsWebhookHandle(params)
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandleResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ee0f81ff-0294-44d3-b93c-e23f39cf6a14&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=caad0665-5b71-407f-9da6-85f28f22d1e1&pt=Microsoft%20Teams%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmicrosoft-teams-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ee0f81ff-0294-44d3-b93c-e23f39cf6a14&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=caad0665-5b71-407f-9da6-85f28f22d1e1&pt=Microsoft%20Teams%20Integration&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmicrosoft-teams-integration%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=d3dfe749-5766-464c-abc6-78ea51f51f90&bo=2&sid=e35c08c0f0bf11f08fae81183ca9ad9c&vid=e35c1ef0f0bf11f0823753b5c8db39b1&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Microsoft%20Teams%20Integration&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmicrosoft-teams-integration%2F&r=&lt=1785&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=577097)
