# Source: https://docs.datadoghq.com/api/latest/restriction-policies/

# Restriction Policies
A restriction policy defines the access control rules for a resource, mapping a set of relations (such as editor and viewer) to a set of allowed principals (such as roles, teams, or users). The restriction policy determines who is authorized to perform what actions on the resource.
## [Update a restriction policy](https://docs.datadoghq.com/api/latest/restriction-policies/#update-a-restriction-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/restriction-policies/#update-a-restriction-policy-v2)


POST https://api.ap1.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.ap2.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.datadoghq.eu/api/v2/restriction_policy/{resource_id}https://api.ddog-gov.com/api/v2/restriction_policy/{resource_id}https://api.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.us3.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.us5.datadoghq.com/api/v2/restriction_policy/{resource_id}
### Overview
Updates the restriction policy associated with a resource.
#### [Supported resources](https://docs.datadoghq.com/api/latest/restriction-policies/#supported-resources)
Restriction policies can be applied to the following resources:
  * Dashboards: `dashboard`
  * Integration Services: `integration-service`
  * Integration Webhooks: `integration-webhook`
  * Notebooks: `notebook`
  * Powerpacks: `powerpack`
  * Reference Tables: `reference-table`
  * Security Rules: `security-rule`
  * Service Level Objectives: `slo`
  * Synthetic Global Variables: `synthetics-global-variable`
  * Synthetic Tests: `synthetics-test`
  * Synthetic Private Locations: `synthetics-private-location`
  * Monitors: `monitor`
  * Workflows: `workflow`
  * App Builder Apps: `app-builder-app`
  * Connections: `connection`
  * Connection Groups: `connection-group`
  * RUM Applications: `rum-application`
  * Cross Org Connections: `cross-org-connection`
  * Spreadsheets: `spreadsheet`
  * On-Call Schedules: `on-call-schedule`
  * On-Call Escalation Policies: `on-call-escalation-policy`
  * On-Call Team Routing Rules: `on-call-team-routing-rules`
  * Logs Pipelines: `logs-pipeline`


#### [Supported relations for resources](https://docs.datadoghq.com/api/latest/restriction-policies/#supported-relations-for-resources)
Resource Type | Supported Relations  
---|---  
Dashboards |  `viewer`, `editor`  
Integration Services |  `viewer`, `editor`  
Integration Webhooks |  `viewer`, `editor`  
Notebooks |  `viewer`, `editor`  
Powerpacks |  `viewer`, `editor`  
Security Rules |  `viewer`, `editor`  
Service Level Objectives |  `viewer`, `editor`  
Synthetic Global Variables |  `viewer`, `editor`  
Synthetic Tests |  `viewer`, `editor`  
Synthetic Private Locations |  `viewer`, `editor`  
Monitors |  `viewer`, `editor`  
Reference Tables |  `viewer`, `editor`  
Workflows |  `viewer`, `runner`, `editor`  
App Builder Apps |  `viewer`, `editor`  
Connections |  `viewer`, `resolver`, `editor`  
Connection Groups |  `viewer`, `editor`  
RUM Application |  `viewer`, `editor`  
Cross Org Connections |  `viewer`, `editor`  
Spreadsheets |  `viewer`, `editor`  
On-Call Schedules |  `viewer`, `overrider`, `editor`  
On-Call Escalation Policies |  `viewer`, `editor`  
On-Call Team Routing Rules |  `viewer`, `editor`  
Logs Pipelines |  `viewer`, `processors_editor`, `editor`  
### Arguments
#### Path Parameters
Name
Type
Description
resource_id [_required_]
string
Identifier, formatted as `type:id`. Supported types: `dashboard`, `integration-service`, `integration-webhook`, `notebook`, `reference-table`, `security-rule`, `slo`, `workflow`, `app-builder-app`, `connection`, `connection-group`, `rum-application`, `cross-org-connection`, `spreadsheet`, `on-call-schedule`, `on-call-escalation-policy`, `on-call-team-routing-rules`, `logs-pipeline`.
#### Query Strings
Name
Type
Description
allow_self_lockout
boolean
Allows admins (users with the `user_access_manage` permission) to remove their own access from the resource if set to `true`. By default, this is set to `false`, preventing admins from locking themselves out.
### Request
#### Body Data (required)
Restriction policy payload
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


Field
Type
Description
data [_required_]
object
Restriction policy object.
attributes [_required_]
object
Restriction policy attributes.
bindings [_required_]
[object]
An array of bindings.
principals [_required_]
[string]
An array of principals. A principal is a subject or group of subjects. Each principal is formatted as `type:id`. Supported types: `role`, `team`, `user`, and `org`. The org ID can be obtained through the api/v2/current_user API. The user principal type accepts service account IDs.
relation [_required_]
string
The role/level of access.
id [_required_]
string
The identifier, always equivalent to the value specified in the `resource_id` path parameter.
type [_required_]
enum
Restriction policy type. Allowed enum values: `restriction_policy`
default: `restriction_policy`
```
{
  "data": {
    "id": "dashboard:test-update",
    "type": "restriction_policy",
    "attributes": {
      "bindings": [
        {
          "relation": "editor",
          "principals": [
            "org:00000000-0000-beef-0000-000000000000"
          ]
        }
      ]
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/restriction-policies/#UpdateRestrictionPolicy-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/restriction-policies/#UpdateRestrictionPolicy-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/restriction-policies/#UpdateRestrictionPolicy-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/restriction-policies/#UpdateRestrictionPolicy-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


Response containing information about a single restriction policy.
Field
Type
Description
data [_required_]
object
Restriction policy object.
attributes [_required_]
object
Restriction policy attributes.
bindings [_required_]
[object]
An array of bindings.
principals [_required_]
[string]
An array of principals. A principal is a subject or group of subjects. Each principal is formatted as `type:id`. Supported types: `role`, `team`, `user`, and `org`. The org ID can be obtained through the api/v2/current_user API. The user principal type accepts service account IDs.
relation [_required_]
string
The role/level of access.
id [_required_]
string
The identifier, always equivalent to the value specified in the `resource_id` path parameter.
type [_required_]
enum
Restriction policy type. Allowed enum values: `restriction_policy`
default: `restriction_policy`
```
{
  "data": {
    "attributes": {
      "bindings": [
        {
          "principals": [
            "role:00000000-0000-1111-0000-000000000000"
          ],
          "relation": "editor"
        }
      ]
    },
    "id": "dashboard:abc-def-ghi",
    "type": "restriction_policy"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=typescript)


#####  Update a restriction policy returns "OK" response
Copy
```
                          # Path parameters  
export resource_id="dashboard:abc-def-ghi"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/restriction_policy/${resource_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "dashboard:test-update",
    "type": "restriction_policy",
    "attributes": {
      "bindings": [
        {
          "relation": "editor",
          "principals": [
            "org:00000000-0000-beef-0000-000000000000"
          ]
        }
      ]
    }
  }
}
EOF  

                        
```

#####  Update a restriction policy returns "OK" response
```
// Update a restriction policy returns "OK" response

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
	// there is a valid "user" in the system

	body := datadogV2.RestrictionPolicyUpdateRequest{
		Data: datadogV2.RestrictionPolicy{
			Id:   "dashboard:test-update",
			Type: datadogV2.RESTRICTIONPOLICYTYPE_RESTRICTION_POLICY,
			Attributes: datadogV2.RestrictionPolicyAttributes{
				Bindings: []datadogV2.RestrictionPolicyBinding{
					{
						Relation: "editor",
						Principals: []string{
							"org:00000000-0000-beef-0000-000000000000",
						},
					},
				},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRestrictionPoliciesApi(apiClient)
	resp, r, err := api.UpdateRestrictionPolicy(ctx, "dashboard:test-update", body, *datadogV2.NewUpdateRestrictionPolicyOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RestrictionPoliciesApi.UpdateRestrictionPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RestrictionPoliciesApi.UpdateRestrictionPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a restriction policy returns "OK" response
```
// Update a restriction policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RestrictionPoliciesApi;
import com.datadog.api.client.v2.model.RestrictionPolicy;
import com.datadog.api.client.v2.model.RestrictionPolicyAttributes;
import com.datadog.api.client.v2.model.RestrictionPolicyBinding;
import com.datadog.api.client.v2.model.RestrictionPolicyResponse;
import com.datadog.api.client.v2.model.RestrictionPolicyType;
import com.datadog.api.client.v2.model.RestrictionPolicyUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RestrictionPoliciesApi apiInstance = new RestrictionPoliciesApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_RELATIONSHIPS_ORG_DATA_ID =
        System.getenv("USER_DATA_RELATIONSHIPS_ORG_DATA_ID");

    RestrictionPolicyUpdateRequest body =
        new RestrictionPolicyUpdateRequest()
            .data(
                new RestrictionPolicy()
                    .id("dashboard:test-update")
                    .type(RestrictionPolicyType.RESTRICTION_POLICY)
                    .attributes(
                        new RestrictionPolicyAttributes()
                            .bindings(
                                Collections.singletonList(
                                    new RestrictionPolicyBinding()
                                        .relation("editor")
                                        .principals(
                                            Collections.singletonList(
                                                "org:00000000-0000-beef-0000-000000000000"))))));

    try {
      RestrictionPolicyResponse result =
          apiInstance.updateRestrictionPolicy("dashboard:test-update", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictionPoliciesApi#updateRestrictionPolicy");
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update a restriction policy returns "OK" response
```
"""
Update a restriction policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.restriction_policies_api import RestrictionPoliciesApi
from datadog_api_client.v2.model.restriction_policy import RestrictionPolicy
from datadog_api_client.v2.model.restriction_policy_attributes import RestrictionPolicyAttributes
from datadog_api_client.v2.model.restriction_policy_binding import RestrictionPolicyBinding
from datadog_api_client.v2.model.restriction_policy_type import RestrictionPolicyType
from datadog_api_client.v2.model.restriction_policy_update_request import RestrictionPolicyUpdateRequest

# there is a valid "user" in the system
USER_DATA_RELATIONSHIPS_ORG_DATA_ID = environ["USER_DATA_RELATIONSHIPS_ORG_DATA_ID"]

body = RestrictionPolicyUpdateRequest(
    data=RestrictionPolicy(
        id="dashboard:test-update",
        type=RestrictionPolicyType.RESTRICTION_POLICY,
        attributes=RestrictionPolicyAttributes(
            bindings=[
                RestrictionPolicyBinding(
                    relation="editor",
                    principals=[
                        "org:00000000-0000-beef-0000-000000000000",
                    ],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RestrictionPoliciesApi(api_client)
    response = api_instance.update_restriction_policy(resource_id="dashboard:test-update", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a restriction policy returns "OK" response
```
# Update a restriction policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RestrictionPoliciesAPI.new

# there is a valid "user" in the system
USER_DATA_RELATIONSHIPS_ORG_DATA_ID = ENV["USER_DATA_RELATIONSHIPS_ORG_DATA_ID"]

body = DatadogAPIClient::V2::RestrictionPolicyUpdateRequest.new({
  data: DatadogAPIClient::V2::RestrictionPolicy.new({
    id: "dashboard:test-update",
    type: DatadogAPIClient::V2::RestrictionPolicyType::RESTRICTION_POLICY,
    attributes: DatadogAPIClient::V2::RestrictionPolicyAttributes.new({
      bindings: [
        DatadogAPIClient::V2::RestrictionPolicyBinding.new({
          relation: "editor",
          principals: [
            "org:00000000-0000-beef-0000-000000000000",
          ],
        }),
      ],
    }),
  }),
})
p api_instance.update_restriction_policy("dashboard:test-update", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a restriction policy returns "OK" response
```
// Update a restriction policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_restriction_policies::RestrictionPoliciesAPI;
use datadog_api_client::datadogV2::api_restriction_policies::UpdateRestrictionPolicyOptionalParams;
use datadog_api_client::datadogV2::model::RestrictionPolicy;
use datadog_api_client::datadogV2::model::RestrictionPolicyAttributes;
use datadog_api_client::datadogV2::model::RestrictionPolicyBinding;
use datadog_api_client::datadogV2::model::RestrictionPolicyType;
use datadog_api_client::datadogV2::model::RestrictionPolicyUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let body = RestrictionPolicyUpdateRequest::new(RestrictionPolicy::new(
        RestrictionPolicyAttributes::new(vec![RestrictionPolicyBinding::new(
            vec!["org:00000000-0000-beef-0000-000000000000".to_string()],
            "editor".to_string(),
        )]),
        "dashboard:test-update".to_string(),
        RestrictionPolicyType::RESTRICTION_POLICY,
    ));
    let configuration = datadog::Configuration::new();
    let api = RestrictionPoliciesAPI::with_config(configuration);
    let resp = api
        .update_restriction_policy(
            "dashboard:test-update".to_string(),
            body,
            UpdateRestrictionPolicyOptionalParams::default(),
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update a restriction policy returns "OK" response
```
/**
 * Update a restriction policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RestrictionPoliciesApi(configuration);

// there is a valid "user" in the system

const params: v2.RestrictionPoliciesApiUpdateRestrictionPolicyRequest = {
  body: {
    data: {
      id: "dashboard:test-update",
      type: "restriction_policy",
      attributes: {
        bindings: [
          {
            relation: "editor",
            principals: ["org:00000000-0000-beef-0000-000000000000"],
          },
        ],
      },
    },
  },
  resourceId: "dashboard:test-update",
};

apiInstance
  .updateRestrictionPolicy(params)
  .then((data: v2.RestrictionPolicyResponse) => {
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a restriction policy](https://docs.datadoghq.com/api/latest/restriction-policies/#get-a-restriction-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/restriction-policies/#get-a-restriction-policy-v2)


GET https://api.ap1.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.ap2.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.datadoghq.eu/api/v2/restriction_policy/{resource_id}https://api.ddog-gov.com/api/v2/restriction_policy/{resource_id}https://api.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.us3.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.us5.datadoghq.com/api/v2/restriction_policy/{resource_id}
### Overview
Retrieves the restriction policy associated with a specified resource.
### Arguments
#### Path Parameters
Name
Type
Description
resource_id [_required_]
string
Identifier, formatted as `type:id`. Supported types: `dashboard`, `integration-service`, `integration-webhook`, `notebook`, `reference-table`, `security-rule`, `slo`, `workflow`, `app-builder-app`, `connection`, `connection-group`, `rum-application`, `cross-org-connection`, `spreadsheet`, `on-call-schedule`, `on-call-escalation-policy`, `on-call-team-routing-rules`, `logs-pipeline`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/restriction-policies/#GetRestrictionPolicy-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/restriction-policies/#GetRestrictionPolicy-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/restriction-policies/#GetRestrictionPolicy-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/restriction-policies/#GetRestrictionPolicy-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


Response containing information about a single restriction policy.
Field
Type
Description
data [_required_]
object
Restriction policy object.
attributes [_required_]
object
Restriction policy attributes.
bindings [_required_]
[object]
An array of bindings.
principals [_required_]
[string]
An array of principals. A principal is a subject or group of subjects. Each principal is formatted as `type:id`. Supported types: `role`, `team`, `user`, and `org`. The org ID can be obtained through the api/v2/current_user API. The user principal type accepts service account IDs.
relation [_required_]
string
The role/level of access.
id [_required_]
string
The identifier, always equivalent to the value specified in the `resource_id` path parameter.
type [_required_]
enum
Restriction policy type. Allowed enum values: `restriction_policy`
default: `restriction_policy`
```
{
  "data": {
    "attributes": {
      "bindings": [
        {
          "principals": [
            "role:00000000-0000-1111-0000-000000000000"
          ],
          "relation": "editor"
        }
      ]
    },
    "id": "dashboard:abc-def-ghi",
    "type": "restriction_policy"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=typescript)


#####  Get a restriction policy
Copy
```
                  # Path parameters  
export resource_id="dashboard:abc-def-ghi"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/restriction_policy/${resource_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a restriction policy
```
"""
Get a restriction policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.restriction_policies_api import RestrictionPoliciesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RestrictionPoliciesApi(api_client)
    response = api_instance.get_restriction_policy(
        resource_id="dashboard:test-get",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a restriction policy
```
# Get a restriction policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RestrictionPoliciesAPI.new
p api_instance.get_restriction_policy("dashboard:test-get")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a restriction policy
```
// Get a restriction policy returns "OK" response

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
	api := datadogV2.NewRestrictionPoliciesApi(apiClient)
	resp, r, err := api.GetRestrictionPolicy(ctx, "dashboard:test-get")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RestrictionPoliciesApi.GetRestrictionPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RestrictionPoliciesApi.GetRestrictionPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a restriction policy
```
// Get a restriction policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RestrictionPoliciesApi;
import com.datadog.api.client.v2.model.RestrictionPolicyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RestrictionPoliciesApi apiInstance = new RestrictionPoliciesApi(defaultClient);

    try {
      RestrictionPolicyResponse result = apiInstance.getRestrictionPolicy("dashboard:test-get");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictionPoliciesApi#getRestrictionPolicy");
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a restriction policy
```
// Get a restriction policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_restriction_policies::RestrictionPoliciesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RestrictionPoliciesAPI::with_config(configuration);
    let resp = api
        .get_restriction_policy("dashboard:test-get".to_string())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a restriction policy
```
/**
 * Get a restriction policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RestrictionPoliciesApi(configuration);

const params: v2.RestrictionPoliciesApiGetRestrictionPolicyRequest = {
  resourceId: "dashboard:test-get",
};

apiInstance
  .getRestrictionPolicy(params)
  .then((data: v2.RestrictionPolicyResponse) => {
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete a restriction policy](https://docs.datadoghq.com/api/latest/restriction-policies/#delete-a-restriction-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/restriction-policies/#delete-a-restriction-policy-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.ap2.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.datadoghq.eu/api/v2/restriction_policy/{resource_id}https://api.ddog-gov.com/api/v2/restriction_policy/{resource_id}https://api.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.us3.datadoghq.com/api/v2/restriction_policy/{resource_id}https://api.us5.datadoghq.com/api/v2/restriction_policy/{resource_id}
### Overview
Deletes the restriction policy associated with a specified resource.
### Arguments
#### Path Parameters
Name
Type
Description
resource_id [_required_]
string
Identifier, formatted as `type:id`. Supported types: `dashboard`, `integration-service`, `integration-webhook`, `notebook`, `reference-table`, `security-rule`, `slo`, `workflow`, `app-builder-app`, `connection`, `connection-group`, `rum-application`, `cross-org-connection`, `spreadsheet`, `on-call-schedule`, `on-call-escalation-policy`, `on-call-team-routing-rules`, `logs-pipeline`.
### Response
  * [204](https://docs.datadoghq.com/api/latest/restriction-policies/#DeleteRestrictionPolicy-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/restriction-policies/#DeleteRestrictionPolicy-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/restriction-policies/#DeleteRestrictionPolicy-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/restriction-policies/#DeleteRestrictionPolicy-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
Not Authorized
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
  * [Model](https://docs.datadoghq.com/api/latest/restriction-policies/)
  * [Example](https://docs.datadoghq.com/api/latest/restriction-policies/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/restriction-policies/?code-lang=typescript)


#####  Delete a restriction policy
Copy
```
                  # Path parameters  
export resource_id="dashboard:abc-def-ghi"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/restriction_policy/${resource_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a restriction policy
```
"""
Delete a restriction policy returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.restriction_policies_api import RestrictionPoliciesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RestrictionPoliciesApi(api_client)
    api_instance.delete_restriction_policy(
        resource_id="dashboard:test-delete",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a restriction policy
```
# Delete a restriction policy returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RestrictionPoliciesAPI.new
api_instance.delete_restriction_policy("dashboard:test-delete")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a restriction policy
```
// Delete a restriction policy returns "No Content" response

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
	api := datadogV2.NewRestrictionPoliciesApi(apiClient)
	r, err := api.DeleteRestrictionPolicy(ctx, "dashboard:test-delete")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RestrictionPoliciesApi.DeleteRestrictionPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete a restriction policy
```
// Delete a restriction policy returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RestrictionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RestrictionPoliciesApi apiInstance = new RestrictionPoliciesApi(defaultClient);

    try {
      apiInstance.deleteRestrictionPolicy("dashboard:test-delete");
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictionPoliciesApi#deleteRestrictionPolicy");
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete a restriction policy
```
// Delete a restriction policy returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_restriction_policies::RestrictionPoliciesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RestrictionPoliciesAPI::with_config(configuration);
    let resp = api
        .delete_restriction_policy("dashboard:test-delete".to_string())
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete a restriction policy
```
/**
 * Delete a restriction policy returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RestrictionPoliciesApi(configuration);

const params: v2.RestrictionPoliciesApiDeleteRestrictionPolicyRequest = {
  resourceId: "dashboard:test-delete",
};

apiInstance
  .deleteRestrictionPolicy(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d34e136f-a2af-415a-ac09-613930c075e5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b8fd4205-3e96-44d7-b811-e8960d258442&pt=Restriction%20Policies&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frestriction-policies%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d34e136f-a2af-415a-ac09-613930c075e5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=b8fd4205-3e96-44d7-b811-e8960d258442&pt=Restriction%20Policies&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frestriction-policies%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=2b470f19-2c7a-45cb-ab8e-24caffa7fe2c&bo=2&sid=b77a5fe0f0bf11f0bab0291dd4b5f9fd&vid=b77a7130f0bf11f0b69eb7008fe8e23b&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Restriction%20Policies&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frestriction-policies%2F&r=&lt=843&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=132577)
