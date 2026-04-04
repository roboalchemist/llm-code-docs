# Source: https://docs.datadoghq.com/api/latest/service-scorecards

# Service Scorecards
API to create and update scorecard rules and outcomes. See [Service Scorecards](https://docs.datadoghq.com/service_catalog/scorecards) for more information.
This feature is currently in BETA. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
## [Create a new rule](https://docs.datadoghq.com/api/latest/service-scorecards/#create-a-new-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-scorecards/#create-a-new-rule-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/scorecard/ruleshttps://api.ap2.datadoghq.com/api/v2/scorecard/ruleshttps://api.datadoghq.eu/api/v2/scorecard/ruleshttps://api.ddog-gov.com/api/v2/scorecard/ruleshttps://api.datadoghq.com/api/v2/scorecard/ruleshttps://api.us3.datadoghq.com/api/v2/scorecard/ruleshttps://api.us5.datadoghq.com/api/v2/scorecard/rules
### Overview
Creates a new rule.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-scorecards) to access this endpoint.
### Request
#### Body Data (required)
Rule attributes.
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Field
Type
Description
data
object
Scorecard create rule request data.
attributes
object
Details of a rule.
category
string
**DEPRECATED** : The scorecard name to which this rule must belong.
created_at
date-time
Creation time of the rule outcome.
custom
boolean
Defines if the rule is a custom rule.
description
string
Explanation of the rule.
enabled
boolean
If enabled, the rule is calculated as part of the score.
level
int32
The maturity level of the rule (1, 2, or 3).
modified_at
date-time
Time of the last rule outcome modification.
name
string
Name of the rule.
owner
string
Owner of the rule.
scorecard_name
string
The scorecard name to which this rule must belong.
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
```
{
  "data": {
    "attributes": {
      "enabled": true,
      "name": "Example-Service-Scorecard",
      "scorecard_name": "Observability Best Practices"
    },
    "type": "rule"
  }
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardRule-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardRule-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardRule-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardRule-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Created rule in response.
Field
Type
Description
data
object
Create rule response data.
attributes
object
Details of a rule.
category
string
**DEPRECATED** : The scorecard name to which this rule must belong.
created_at
date-time
Creation time of the rule outcome.
custom
boolean
Defines if the rule is a custom rule.
description
string
Explanation of the rule.
enabled
boolean
If enabled, the rule is calculated as part of the score.
level
int32
The maturity level of the rule (1, 2, or 3).
modified_at
date-time
Time of the last rule outcome modification.
name
string
Name of the rule.
owner
string
Owner of the rule.
scorecard_name
string
The scorecard name to which this rule must belong.
id
string
The unique ID for a scorecard rule.
relationships
object
Scorecard create rule response relationship.
scorecard
object
Relationship data for a rule.
data
object
Rule relationship data.
id
string
The unique ID for a scorecard.
type
enum
The JSON:API type for scorecard. Allowed enum values: `scorecard`
default: `scorecard`
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
```
{
  "data": {
    "attributes": {
      "category": "string",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom": false,
      "description": "string",
      "enabled": true,
      "level": 2,
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "Team Defined",
      "owner": "string",
      "scorecard_name": "Deployments automated via Deployment Trains"
    },
    "id": "q8MQxk8TCqrHnWkx",
    "relationships": {
      "scorecard": {
        "data": {
          "id": "q8MQxk8TCqrHnWkp",
          "type": "scorecard"
        }
      }
    },
    "type": "rule"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=typescript)


#####  Create a new rule returns "Created" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scorecard/rules" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": true,
      "name": "Example-Service-Scorecard",
      "scorecard_name": "Observability Best Practices"
    },
    "type": "rule"
  }
}
EOF  

                        
```

#####  Create a new rule returns "Created" response
```
// Create a new rule returns "Created" response

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
	body := datadogV2.CreateRuleRequest{
		Data: &datadogV2.CreateRuleRequestData{
			Attributes: &datadogV2.RuleAttributes{
				Enabled:       datadog.PtrBool(true),
				Name:          datadog.PtrString("Example-Service-Scorecard"),
				ScorecardName: datadog.PtrString("Observability Best Practices"),
			},
			Type: datadogV2.RULETYPE_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateScorecardRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceScorecardsApi(apiClient)
	resp, r, err := api.CreateScorecardRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceScorecardsApi.CreateScorecardRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceScorecardsApi.CreateScorecardRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a new rule returns "Created" response
```
// Create a new rule returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceScorecardsApi;
import com.datadog.api.client.v2.model.CreateRuleRequest;
import com.datadog.api.client.v2.model.CreateRuleRequestData;
import com.datadog.api.client.v2.model.CreateRuleResponse;
import com.datadog.api.client.v2.model.RuleAttributes;
import com.datadog.api.client.v2.model.RuleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createScorecardRule", true);
    ServiceScorecardsApi apiInstance = new ServiceScorecardsApi(defaultClient);

    CreateRuleRequest body =
        new CreateRuleRequest()
            .data(
                new CreateRuleRequestData()
                    .attributes(
                        new RuleAttributes()
                            .enabled(true)
                            .name("Example-Service-Scorecard")
                            .scorecardName("Observability Best Practices"))
                    .type(RuleType.RULE));

    try {
      CreateRuleResponse result = apiInstance.createScorecardRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceScorecardsApi#createScorecardRule");
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

#####  Create a new rule returns "Created" response
```
"""
Create a new rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.create_rule_request import CreateRuleRequest
from datadog_api_client.v2.model.create_rule_request_data import CreateRuleRequestData
from datadog_api_client.v2.model.rule_attributes import RuleAttributes
from datadog_api_client.v2.model.rule_type import RuleType

body = CreateRuleRequest(
    data=CreateRuleRequestData(
        attributes=RuleAttributes(
            enabled=True,
            name="Example-Service-Scorecard",
            scorecard_name="Observability Best Practices",
        ),
        type=RuleType.RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_scorecard_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.create_scorecard_rule(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a new rule returns "Created" response
```
# Create a new rule returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_scorecard_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceScorecardsAPI.new

body = DatadogAPIClient::V2::CreateRuleRequest.new({
  data: DatadogAPIClient::V2::CreateRuleRequestData.new({
    attributes: DatadogAPIClient::V2::RuleAttributes.new({
      enabled: true,
      name: "Example-Service-Scorecard",
      scorecard_name: "Observability Best Practices",
    }),
    type: DatadogAPIClient::V2::RuleType::RULE,
  }),
})
p api_instance.create_scorecard_rule(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a new rule returns "Created" response
```
// Create a new rule returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_scorecards::ServiceScorecardsAPI;
use datadog_api_client::datadogV2::model::CreateRuleRequest;
use datadog_api_client::datadogV2::model::CreateRuleRequestData;
use datadog_api_client::datadogV2::model::RuleAttributes;
use datadog_api_client::datadogV2::model::RuleType;

#[tokio::main]
async fn main() {
    let body = CreateRuleRequest::new().data(
        CreateRuleRequestData::new()
            .attributes(
                RuleAttributes::new()
                    .enabled(true)
                    .name("Example-Service-Scorecard".to_string())
                    .scorecard_name("Observability Best Practices".to_string()),
            )
            .type_(RuleType::RULE),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateScorecardRule", true);
    let api = ServiceScorecardsAPI::with_config(configuration);
    let resp = api.create_scorecard_rule(body).await;
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

#####  Create a new rule returns "Created" response
```
/**
 * Create a new rule returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createScorecardRule"] = true;
const apiInstance = new v2.ServiceScorecardsApi(configuration);

const params: v2.ServiceScorecardsApiCreateScorecardRuleRequest = {
  body: {
    data: {
      attributes: {
        enabled: true,
        name: "Example-Service-Scorecard",
        scorecardName: "Observability Best Practices",
      },
      type: "rule",
    },
  },
};

apiInstance
  .createScorecardRule(params)
  .then((data: v2.CreateRuleResponse) => {
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
## [Create outcomes batch](https://docs.datadoghq.com/api/latest/service-scorecards/#create-outcomes-batch)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-scorecards/#create-outcomes-batch-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/scorecard/outcomes/batchhttps://api.ap2.datadoghq.com/api/v2/scorecard/outcomes/batchhttps://api.datadoghq.eu/api/v2/scorecard/outcomes/batchhttps://api.ddog-gov.com/api/v2/scorecard/outcomes/batchhttps://api.datadoghq.com/api/v2/scorecard/outcomes/batchhttps://api.us3.datadoghq.com/api/v2/scorecard/outcomes/batchhttps://api.us5.datadoghq.com/api/v2/scorecard/outcomes/batch
### Overview
Sets multiple service-rule outcomes in a single batched request.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-scorecards) to access this endpoint.
### Request
#### Body Data (required)
Set of scorecard outcomes.
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Field
Type
Description
data
object
Scorecard outcomes batch request data.
attributes
object
The JSON:API attributes for a batched set of scorecard outcomes.
results
[object]
Set of scorecard outcomes to update.
remarks
string
Any remarks regarding the scorecard rule's evaluation, and supports HTML hyperlinks.
rule_id [_required_]
string
The unique ID for a scorecard rule.
service_name [_required_]
string
The unique name for a service in the catalog.
state [_required_]
enum
The state of the rule evaluation. Allowed enum values: `pass,fail,skip`
type
enum
The JSON:API type for scorecard outcomes. Allowed enum values: `batched-outcome`
default: `batched-outcome`
```
{
  "data": {
    "attributes": {
      "results": [
        {
          "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>",
          "rule_id": "q8MQxk8TCqrHnWkx",
          "service_name": "my-service",
          "state": "pass"
        }
      ]
    },
    "type": "batched-outcome"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardOutcomesBatch-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardOutcomesBatch-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardOutcomesBatch-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-scorecards/#CreateScorecardOutcomesBatch-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Scorecard outcomes batch response.
Field
Type
Description
data [_required_]
[object]
List of rule outcomes which were affected during the bulk operation.
attributes
object
The JSON:API attributes for an outcome.
created_at
date-time
Creation time of the rule outcome.
modified_at
date-time
Time of last rule outcome modification.
remarks
string
Any remarks regarding the scorecard rule's evaluation, and supports HTML hyperlinks.
service_name
string
The unique name for a service in the catalog.
state
enum
The state of the rule evaluation. Allowed enum values: `pass,fail,skip`
id
string
The unique ID for a rule outcome.
relationships
object
The JSON:API relationship to a scorecard rule.
rule
object
The JSON:API relationship to a scorecard outcome.
data
object
The JSON:API relationship to an outcome, which returns the related rule id.
id
string
The unique ID for a scorecard rule.
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
type
enum
The JSON:API type for an outcome. Allowed enum values: `outcome`
default: `outcome`
meta [_required_]
object
Metadata pertaining to the bulk operation.
total_received
int64
Total number of scorecard results received during the bulk operation.
total_updated
int64
Total number of scorecard results modified during the bulk operation.
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>",
        "service_name": "my-service",
        "state": "pass"
      },
      "id": "string",
      "relationships": {
        "rule": {
          "data": {
            "id": "q8MQxk8TCqrHnWkx",
            "type": "rule"
          }
        }
      },
      "type": "outcome"
    }
  ],
  "meta": {
    "total_received": "integer",
    "total_updated": "integer"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=typescript)


#####  Create outcomes batch returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scorecard/outcomes/batch" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "results": [
        {
          "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>",
          "rule_id": "q8MQxk8TCqrHnWkx",
          "service_name": "my-service",
          "state": "pass"
        }
      ]
    },
    "type": "batched-outcome"
  }
}
EOF  

                        
```

#####  Create outcomes batch returns "OK" response
```
// Create outcomes batch returns "OK" response

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
	// there is a valid "create_scorecard_rule" in the system
	CreateScorecardRuleDataID := os.Getenv("CREATE_SCORECARD_RULE_DATA_ID")

	body := datadogV2.OutcomesBatchRequest{
		Data: &datadogV2.OutcomesBatchRequestData{
			Attributes: &datadogV2.OutcomesBatchAttributes{
				Results: []datadogV2.OutcomesBatchRequestItem{
					{
						Remarks:     datadog.PtrString(`See: <a href="https://app.datadoghq.com/services">Services</a>`),
						RuleId:      CreateScorecardRuleDataID,
						ServiceName: "my-service",
						State:       datadogV2.STATE_PASS,
					},
				},
			},
			Type: datadogV2.OUTCOMESBATCHTYPE_BATCHED_OUTCOME.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateScorecardOutcomesBatch", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceScorecardsApi(apiClient)
	resp, r, err := api.CreateScorecardOutcomesBatch(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceScorecardsApi.CreateScorecardOutcomesBatch`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceScorecardsApi.CreateScorecardOutcomesBatch`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create outcomes batch returns "OK" response
```
// Create outcomes batch returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceScorecardsApi;
import com.datadog.api.client.v2.model.OutcomesBatchAttributes;
import com.datadog.api.client.v2.model.OutcomesBatchRequest;
import com.datadog.api.client.v2.model.OutcomesBatchRequestData;
import com.datadog.api.client.v2.model.OutcomesBatchRequestItem;
import com.datadog.api.client.v2.model.OutcomesBatchResponse;
import com.datadog.api.client.v2.model.OutcomesBatchType;
import com.datadog.api.client.v2.model.State;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createScorecardOutcomesBatch", true);
    ServiceScorecardsApi apiInstance = new ServiceScorecardsApi(defaultClient);

    // there is a valid "create_scorecard_rule" in the system
    String CREATE_SCORECARD_RULE_DATA_ID = System.getenv("CREATE_SCORECARD_RULE_DATA_ID");

    OutcomesBatchRequest body =
        new OutcomesBatchRequest()
            .data(
                new OutcomesBatchRequestData()
                    .attributes(
                        new OutcomesBatchAttributes()
                            .results(
                                Collections.singletonList(
                                    new OutcomesBatchRequestItem()
                                        .remarks(
                                            """
See: <a href="https://app.datadoghq.com/services">Services</a>
""")
                                        .ruleId(CREATE_SCORECARD_RULE_DATA_ID)
                                        .serviceName("my-service")
                                        .state(State.PASS))))
                    .type(OutcomesBatchType.BATCHED_OUTCOME));

    try {
      OutcomesBatchResponse result = apiInstance.createScorecardOutcomesBatch(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceScorecardsApi#createScorecardOutcomesBatch");
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

#####  Create outcomes batch returns "OK" response
```
"""
Create outcomes batch returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.outcomes_batch_attributes import OutcomesBatchAttributes
from datadog_api_client.v2.model.outcomes_batch_request import OutcomesBatchRequest
from datadog_api_client.v2.model.outcomes_batch_request_data import OutcomesBatchRequestData
from datadog_api_client.v2.model.outcomes_batch_request_item import OutcomesBatchRequestItem
from datadog_api_client.v2.model.outcomes_batch_type import OutcomesBatchType
from datadog_api_client.v2.model.state import State

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

body = OutcomesBatchRequest(
    data=OutcomesBatchRequestData(
        attributes=OutcomesBatchAttributes(
            results=[
                OutcomesBatchRequestItem(
                    remarks='See: <a href="https://app.datadoghq.com/services">Services</a>',
                    rule_id=CREATE_SCORECARD_RULE_DATA_ID,
                    service_name="my-service",
                    state=State.PASS,
                ),
            ],
        ),
        type=OutcomesBatchType.BATCHED_OUTCOME,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_scorecard_outcomes_batch"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.create_scorecard_outcomes_batch(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create outcomes batch returns "OK" response
```
# Create outcomes batch returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_scorecard_outcomes_batch".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceScorecardsAPI.new

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = ENV["CREATE_SCORECARD_RULE_DATA_ID"]

body = DatadogAPIClient::V2::OutcomesBatchRequest.new({
  data: DatadogAPIClient::V2::OutcomesBatchRequestData.new({
    attributes: DatadogAPIClient::V2::OutcomesBatchAttributes.new({
      results: [
        DatadogAPIClient::V2::OutcomesBatchRequestItem.new({
          remarks: 'See: <a href="https://app.datadoghq.com/services">Services</a>',
          rule_id: CREATE_SCORECARD_RULE_DATA_ID,
          service_name: "my-service",
          state: DatadogAPIClient::V2::State::PASS,
        }),
      ],
    }),
    type: DatadogAPIClient::V2::OutcomesBatchType::BATCHED_OUTCOME,
  }),
})
p api_instance.create_scorecard_outcomes_batch(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create outcomes batch returns "OK" response
```
// Create outcomes batch returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_scorecards::ServiceScorecardsAPI;
use datadog_api_client::datadogV2::model::OutcomesBatchAttributes;
use datadog_api_client::datadogV2::model::OutcomesBatchRequest;
use datadog_api_client::datadogV2::model::OutcomesBatchRequestData;
use datadog_api_client::datadogV2::model::OutcomesBatchRequestItem;
use datadog_api_client::datadogV2::model::OutcomesBatchType;
use datadog_api_client::datadogV2::model::State;

#[tokio::main]
async fn main() {
    // there is a valid "create_scorecard_rule" in the system
    let create_scorecard_rule_data_id = std::env::var("CREATE_SCORECARD_RULE_DATA_ID").unwrap();
    let body = OutcomesBatchRequest::new().data(
        OutcomesBatchRequestData::new()
            .attributes(
                OutcomesBatchAttributes::new().results(vec![OutcomesBatchRequestItem::new(
                    create_scorecard_rule_data_id.clone(),
                    "my-service".to_string(),
                    State::PASS,
                )
                .remarks(
                    r#"See: <a href="https://app.datadoghq.com/services">Services</a>"#.to_string(),
                )]),
            )
            .type_(OutcomesBatchType::BATCHED_OUTCOME),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateScorecardOutcomesBatch", true);
    let api = ServiceScorecardsAPI::with_config(configuration);
    let resp = api.create_scorecard_outcomes_batch(body).await;
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

#####  Create outcomes batch returns "OK" response
```
/**
 * Create outcomes batch returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createScorecardOutcomesBatch"] = true;
const apiInstance = new v2.ServiceScorecardsApi(configuration);

// there is a valid "create_scorecard_rule" in the system
const CREATE_SCORECARD_RULE_DATA_ID = process.env
  .CREATE_SCORECARD_RULE_DATA_ID as string;

const params: v2.ServiceScorecardsApiCreateScorecardOutcomesBatchRequest = {
  body: {
    data: {
      attributes: {
        results: [
          {
            remarks: `See: <a href="https://app.datadoghq.com/services">Services</a>`,
            ruleId: CREATE_SCORECARD_RULE_DATA_ID,
            serviceName: "my-service",
            state: "pass",
          },
        ],
      },
      type: "batched-outcome",
    },
  },
};

apiInstance
  .createScorecardOutcomesBatch(params)
  .then((data: v2.OutcomesBatchResponse) => {
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
## [Update Scorecard outcomes asynchronously](https://docs.datadoghq.com/api/latest/service-scorecards/#update-scorecard-outcomes-asynchronously)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-scorecards/#update-scorecard-outcomes-asynchronously-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/scorecard/outcomeshttps://api.ap2.datadoghq.com/api/v2/scorecard/outcomeshttps://api.datadoghq.eu/api/v2/scorecard/outcomeshttps://api.ddog-gov.com/api/v2/scorecard/outcomeshttps://api.datadoghq.com/api/v2/scorecard/outcomeshttps://api.us3.datadoghq.com/api/v2/scorecard/outcomeshttps://api.us5.datadoghq.com/api/v2/scorecard/outcomes
### Overview
Updates multiple scorecard rule outcomes in a single batched request.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-scorecards) to access this endpoint.
### Request
#### Body Data (required)
Set of scorecard outcomes.
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Field
Type
Description
data
object
Scorecard outcomes batch request data.
attributes
object
The JSON:API attributes for a batched set of scorecard outcomes.
results
[object]
Set of scorecard outcomes to update asynchronously.
entity_reference [_required_]
string
The unique reference for an IDP entity.
remarks
string
Any remarks regarding the scorecard rule's evaluation. Supports HTML hyperlinks.
rule_id [_required_]
string
The unique ID for a scorecard rule.
state [_required_]
enum
The state of the rule evaluation. Allowed enum values: `pass,fail,skip`
type
enum
The JSON:API type for scorecard outcomes. Allowed enum values: `batched-outcome`
default: `batched-outcome`
```
{
  "data": {
    "attributes": {
      "results": [
        {
          "rule_id": "q8MQxk8TCqrHnWkx",
          "entity_reference": "service:my-service",
          "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>",
          "state": "pass"
        }
      ]
    },
    "type": "batched-outcome"
  }
}
```

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardOutcomesAsync-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardOutcomesAsync-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardOutcomesAsync-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardOutcomesAsync-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardOutcomesAsync-429-v2)


Accepted
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=typescript)


#####  Update Scorecard outcomes asynchronously returns "Accepted" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scorecard/outcomes" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "results": [
        {
          "rule_id": "q8MQxk8TCqrHnWkx",
          "entity_reference": "service:my-service",
          "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>",
          "state": "pass"
        }
      ]
    },
    "type": "batched-outcome"
  }
}
EOF  

                        
```

#####  Update Scorecard outcomes asynchronously returns "Accepted" response
```
// Update Scorecard outcomes asynchronously returns "Accepted" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "create_scorecard_rule" in the system
	CreateScorecardRuleDataID := os.Getenv("CREATE_SCORECARD_RULE_DATA_ID")

	body := datadogV2.UpdateOutcomesAsyncRequest{
		Data: &datadogV2.UpdateOutcomesAsyncRequestData{
			Attributes: &datadogV2.UpdateOutcomesAsyncAttributes{
				Results: []datadogV2.UpdateOutcomesAsyncRequestItem{
					{
						RuleId:          CreateScorecardRuleDataID,
						EntityReference: "service:my-service",
						Remarks:         datadog.PtrString(`See: <a href="https://app.datadoghq.com/services">Services</a>`),
						State:           datadogV2.STATE_PASS,
					},
				},
			},
			Type: datadogV2.UPDATEOUTCOMESASYNCTYPE_BATCHED_OUTCOME.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateScorecardOutcomesAsync", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceScorecardsApi(apiClient)
	r, err := api.UpdateScorecardOutcomesAsync(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceScorecardsApi.UpdateScorecardOutcomesAsync`: %v\n", err)
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

#####  Update Scorecard outcomes asynchronously returns "Accepted" response
```
// Update Scorecard outcomes asynchronously returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceScorecardsApi;
import com.datadog.api.client.v2.model.State;
import com.datadog.api.client.v2.model.UpdateOutcomesAsyncAttributes;
import com.datadog.api.client.v2.model.UpdateOutcomesAsyncRequest;
import com.datadog.api.client.v2.model.UpdateOutcomesAsyncRequestData;
import com.datadog.api.client.v2.model.UpdateOutcomesAsyncRequestItem;
import com.datadog.api.client.v2.model.UpdateOutcomesAsyncType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateScorecardOutcomesAsync", true);
    ServiceScorecardsApi apiInstance = new ServiceScorecardsApi(defaultClient);

    // there is a valid "create_scorecard_rule" in the system
    String CREATE_SCORECARD_RULE_DATA_ID = System.getenv("CREATE_SCORECARD_RULE_DATA_ID");

    UpdateOutcomesAsyncRequest body =
        new UpdateOutcomesAsyncRequest()
            .data(
                new UpdateOutcomesAsyncRequestData()
                    .attributes(
                        new UpdateOutcomesAsyncAttributes()
                            .results(
                                Collections.singletonList(
                                    new UpdateOutcomesAsyncRequestItem()
                                        .ruleId(CREATE_SCORECARD_RULE_DATA_ID)
                                        .entityReference("service:my-service")
                                        .remarks(
                                            """
See: <a href="https://app.datadoghq.com/services">Services</a>
""")
                                        .state(State.PASS))))
                    .type(UpdateOutcomesAsyncType.BATCHED_OUTCOME));

    try {
      apiInstance.updateScorecardOutcomesAsync(body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceScorecardsApi#updateScorecardOutcomesAsync");
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

#####  Update Scorecard outcomes asynchronously returns "Accepted" response
```
"""
Update Scorecard outcomes asynchronously returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.state import State
from datadog_api_client.v2.model.update_outcomes_async_attributes import UpdateOutcomesAsyncAttributes
from datadog_api_client.v2.model.update_outcomes_async_request import UpdateOutcomesAsyncRequest
from datadog_api_client.v2.model.update_outcomes_async_request_data import UpdateOutcomesAsyncRequestData
from datadog_api_client.v2.model.update_outcomes_async_request_item import UpdateOutcomesAsyncRequestItem
from datadog_api_client.v2.model.update_outcomes_async_type import UpdateOutcomesAsyncType

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

body = UpdateOutcomesAsyncRequest(
    data=UpdateOutcomesAsyncRequestData(
        attributes=UpdateOutcomesAsyncAttributes(
            results=[
                UpdateOutcomesAsyncRequestItem(
                    rule_id=CREATE_SCORECARD_RULE_DATA_ID,
                    entity_reference="service:my-service",
                    remarks='See: <a href="https://app.datadoghq.com/services">Services</a>',
                    state=State.PASS,
                ),
            ],
        ),
        type=UpdateOutcomesAsyncType.BATCHED_OUTCOME,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_scorecard_outcomes_async"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.update_scorecard_outcomes_async(body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update Scorecard outcomes asynchronously returns "Accepted" response
```
# Update Scorecard outcomes asynchronously returns "Accepted" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_scorecard_outcomes_async".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceScorecardsAPI.new

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = ENV["CREATE_SCORECARD_RULE_DATA_ID"]

body = DatadogAPIClient::V2::UpdateOutcomesAsyncRequest.new({
  data: DatadogAPIClient::V2::UpdateOutcomesAsyncRequestData.new({
    attributes: DatadogAPIClient::V2::UpdateOutcomesAsyncAttributes.new({
      results: [
        DatadogAPIClient::V2::UpdateOutcomesAsyncRequestItem.new({
          rule_id: CREATE_SCORECARD_RULE_DATA_ID,
          entity_reference: "service:my-service",
          remarks: 'See: <a href="https://app.datadoghq.com/services">Services</a>',
          state: DatadogAPIClient::V2::State::PASS,
        }),
      ],
    }),
    type: DatadogAPIClient::V2::UpdateOutcomesAsyncType::BATCHED_OUTCOME,
  }),
})
p api_instance.update_scorecard_outcomes_async(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update Scorecard outcomes asynchronously returns "Accepted" response
```
// Update Scorecard outcomes asynchronously returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_scorecards::ServiceScorecardsAPI;
use datadog_api_client::datadogV2::model::State;
use datadog_api_client::datadogV2::model::UpdateOutcomesAsyncAttributes;
use datadog_api_client::datadogV2::model::UpdateOutcomesAsyncRequest;
use datadog_api_client::datadogV2::model::UpdateOutcomesAsyncRequestData;
use datadog_api_client::datadogV2::model::UpdateOutcomesAsyncRequestItem;
use datadog_api_client::datadogV2::model::UpdateOutcomesAsyncType;

#[tokio::main]
async fn main() {
    // there is a valid "create_scorecard_rule" in the system
    let create_scorecard_rule_data_id = std::env::var("CREATE_SCORECARD_RULE_DATA_ID").unwrap();
    let body = UpdateOutcomesAsyncRequest::new().data(
        UpdateOutcomesAsyncRequestData::new()
            .attributes(UpdateOutcomesAsyncAttributes::new().results(vec![
                    UpdateOutcomesAsyncRequestItem::new(
                        "service:my-service".to_string(),
                        create_scorecard_rule_data_id.clone(),
                        State::PASS,
                    )
                    .remarks(
                        r#"See: <a href="https://app.datadoghq.com/services">Services</a>"#
                            .to_string(),
                    ),
                ]))
            .type_(UpdateOutcomesAsyncType::BATCHED_OUTCOME),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateScorecardOutcomesAsync", true);
    let api = ServiceScorecardsAPI::with_config(configuration);
    let resp = api.update_scorecard_outcomes_async(body).await;
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

#####  Update Scorecard outcomes asynchronously returns "Accepted" response
```
/**
 * Update Scorecard outcomes asynchronously returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateScorecardOutcomesAsync"] = true;
const apiInstance = new v2.ServiceScorecardsApi(configuration);

// there is a valid "create_scorecard_rule" in the system
const CREATE_SCORECARD_RULE_DATA_ID = process.env
  .CREATE_SCORECARD_RULE_DATA_ID as string;

const params: v2.ServiceScorecardsApiUpdateScorecardOutcomesAsyncRequest = {
  body: {
    data: {
      attributes: {
        results: [
          {
            ruleId: CREATE_SCORECARD_RULE_DATA_ID,
            entityReference: "service:my-service",
            remarks: `See: <a href="https://app.datadoghq.com/services">Services</a>`,
            state: "pass",
          },
        ],
      },
      type: "batched-outcome",
    },
  },
};

apiInstance
  .updateScorecardOutcomesAsync(params)
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
## [List all rule outcomes](https://docs.datadoghq.com/api/latest/service-scorecards/#list-all-rule-outcomes)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-scorecards/#list-all-rule-outcomes-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/scorecard/outcomeshttps://api.ap2.datadoghq.com/api/v2/scorecard/outcomeshttps://api.datadoghq.eu/api/v2/scorecard/outcomeshttps://api.ddog-gov.com/api/v2/scorecard/outcomeshttps://api.datadoghq.com/api/v2/scorecard/outcomeshttps://api.us3.datadoghq.com/api/v2/scorecard/outcomeshttps://api.us5.datadoghq.com/api/v2/scorecard/outcomes
### Overview
Fetches all rule outcomes.
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-scorecards) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[offset]
integer
Specific offset to use as the beginning of the returned page.
include
string
Include related rule details in the response.
fields[outcome]
string
Return only specified values in the outcome attributes.
fields[rule]
string
Return only specified values in the included rule details.
filter[outcome][service_name]
string
Filter the outcomes on a specific service name.
filter[outcome][state]
string
Filter the outcomes by a specific state.
filter[rule][enabled]
boolean
Filter outcomes on whether a rule is enabled/disabled.
filter[rule][id]
string
Filter outcomes based on rule ID.
filter[rule][name]
string
Filter outcomes based on rule name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardOutcomes-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardOutcomes-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardOutcomes-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardOutcomes-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Scorecard outcomes - the result of a rule for a service.
Field
Type
Description
data
[object]
List of rule outcomes.
attributes
object
The JSON:API attributes for an outcome.
created_at
date-time
Creation time of the rule outcome.
modified_at
date-time
Time of last rule outcome modification.
remarks
string
Any remarks regarding the scorecard rule's evaluation, and supports HTML hyperlinks.
service_name
string
The unique name for a service in the catalog.
state
enum
The state of the rule evaluation. Allowed enum values: `pass,fail,skip`
id
string
The unique ID for a rule outcome.
relationships
object
The JSON:API relationship to a scorecard rule.
rule
object
The JSON:API relationship to a scorecard outcome.
data
object
The JSON:API relationship to an outcome, which returns the related rule id.
id
string
The unique ID for a scorecard rule.
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
type
enum
The JSON:API type for an outcome. Allowed enum values: `outcome`
default: `outcome`
included
[object]
Array of rule details.
attributes
object
Details of a rule.
name
string
Name of the rule.
scorecard_name
string
The scorecard name to which this rule must belong.
id
string
The unique ID for a scorecard rule.
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
links
object
Links attributes.
next
string
Link for the next set of results.
```
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>",
        "service_name": "my-service",
        "state": "pass"
      },
      "id": "string",
      "relationships": {
        "rule": {
          "data": {
            "id": "q8MQxk8TCqrHnWkx",
            "type": "rule"
          }
        }
      },
      "type": "outcome"
    }
  ],
  "included": [
    {
      "attributes": {
        "name": "Team Defined",
        "scorecard_name": "Observability Best Practices"
      },
      "id": "q8MQxk8TCqrHnWkx",
      "type": "rule"
    }
  ],
  "links": {
    "next": "/api/v2/scorecard/outcomes?include=rule\u0026page%5Blimit%5D=100\u0026page%5Boffset%5D=100"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=typescript)


#####  List all rule outcomes
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scorecard/outcomes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all rule outcomes
```
"""
List all rule outcomes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi

configuration = Configuration()
configuration.unstable_operations["list_scorecard_outcomes"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.list_scorecard_outcomes()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List all rule outcomes
```
# List all rule outcomes returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_scorecard_outcomes".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceScorecardsAPI.new
p api_instance.list_scorecard_outcomes()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List all rule outcomes
```
// List all rule outcomes returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListScorecardOutcomes", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceScorecardsApi(apiClient)
	resp, r, err := api.ListScorecardOutcomes(ctx, *datadogV2.NewListScorecardOutcomesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceScorecardsApi.ListScorecardOutcomes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceScorecardsApi.ListScorecardOutcomes`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List all rule outcomes
```
// List all rule outcomes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceScorecardsApi;
import com.datadog.api.client.v2.model.OutcomesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listScorecardOutcomes", true);
    ServiceScorecardsApi apiInstance = new ServiceScorecardsApi(defaultClient);

    try {
      OutcomesResponse result = apiInstance.listScorecardOutcomes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceScorecardsApi#listScorecardOutcomes");
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

#####  List all rule outcomes
```
// List all rule outcomes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_scorecards::ListScorecardOutcomesOptionalParams;
use datadog_api_client::datadogV2::api_service_scorecards::ServiceScorecardsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListScorecardOutcomes", true);
    let api = ServiceScorecardsAPI::with_config(configuration);
    let resp = api
        .list_scorecard_outcomes(ListScorecardOutcomesOptionalParams::default())
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

#####  List all rule outcomes
```
/**
 * List all rule outcomes returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listScorecardOutcomes"] = true;
const apiInstance = new v2.ServiceScorecardsApi(configuration);

apiInstance
  .listScorecardOutcomes()
  .then((data: v2.OutcomesResponse) => {
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
## [List all rules](https://docs.datadoghq.com/api/latest/service-scorecards/#list-all-rules)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-scorecards/#list-all-rules-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/scorecard/ruleshttps://api.ap2.datadoghq.com/api/v2/scorecard/ruleshttps://api.datadoghq.eu/api/v2/scorecard/ruleshttps://api.ddog-gov.com/api/v2/scorecard/ruleshttps://api.datadoghq.com/api/v2/scorecard/ruleshttps://api.us3.datadoghq.com/api/v2/scorecard/ruleshttps://api.us5.datadoghq.com/api/v2/scorecard/rules
### Overview
Fetch all rules.
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-scorecards) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[offset]
integer
Specific offset to use as the beginning of the returned page.
include
string
Include related scorecard details in the response.
filter[rule][id]
string
Filter the rules on a rule ID.
filter[rule][enabled]
boolean
Filter for enabled rules only.
filter[rule][custom]
boolean
Filter for custom rules only.
filter[rule][name]
string
Filter rules on the rule name.
filter[rule][description]
string
Filter rules on the rule description.
fields[rule]
string
Return only specific fields in the response for rule attributes.
fields[scorecard]
string
Return only specific fields in the included response for scorecard attributes.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardRules-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardRules-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardRules-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-scorecards/#ListScorecardRules-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Scorecard rules response.
Field
Type
Description
data
[object]
Array of rule details.
attributes
object
Details of a rule.
category
string
**DEPRECATED** : The scorecard name to which this rule must belong.
created_at
date-time
Creation time of the rule outcome.
custom
boolean
Defines if the rule is a custom rule.
description
string
Explanation of the rule.
enabled
boolean
If enabled, the rule is calculated as part of the score.
level
int32
The maturity level of the rule (1, 2, or 3).
modified_at
date-time
Time of the last rule outcome modification.
name
string
Name of the rule.
owner
string
Owner of the rule.
scorecard_name
string
The scorecard name to which this rule must belong.
id
string
The unique ID for a scorecard rule.
relationships
object
Scorecard create rule response relationship.
scorecard
object
Relationship data for a rule.
data
object
Rule relationship data.
id
string
The unique ID for a scorecard.
type
enum
The JSON:API type for scorecard. Allowed enum values: `scorecard`
default: `scorecard`
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
links
object
Links attributes.
next
string
Link for the next set of rules.
```
{
  "data": [
    {
      "attributes": {
        "category": "string",
        "created_at": "2019-09-19T10:00:00.000Z",
        "custom": false,
        "description": "string",
        "enabled": true,
        "level": 2,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "Team Defined",
        "owner": "string",
        "scorecard_name": "Deployments automated via Deployment Trains"
      },
      "id": "q8MQxk8TCqrHnWkx",
      "relationships": {
        "scorecard": {
          "data": {
            "id": "q8MQxk8TCqrHnWkp",
            "type": "scorecard"
          }
        }
      },
      "type": "rule"
    }
  ],
  "links": {
    "next": "/api/v2/scorecard/rules?page%5Blimit%5D=2\u0026page%5Boffset%5D=2\u0026page%5Bsize%5D=2"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=typescript)


#####  List all rules
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scorecard/rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List all rules
```
"""
List all rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi

configuration = Configuration()
configuration.unstable_operations["list_scorecard_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.list_scorecard_rules()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  List all rules
```
# List all rules returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_scorecard_rules".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceScorecardsAPI.new
p api_instance.list_scorecard_rules()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  List all rules
```
// List all rules returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListScorecardRules", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceScorecardsApi(apiClient)
	resp, r, err := api.ListScorecardRules(ctx, *datadogV2.NewListScorecardRulesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceScorecardsApi.ListScorecardRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceScorecardsApi.ListScorecardRules`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  List all rules
```
// List all rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceScorecardsApi;
import com.datadog.api.client.v2.model.ListRulesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listScorecardRules", true);
    ServiceScorecardsApi apiInstance = new ServiceScorecardsApi(defaultClient);

    try {
      ListRulesResponse result = apiInstance.listScorecardRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceScorecardsApi#listScorecardRules");
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

#####  List all rules
```
// List all rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_scorecards::ListScorecardRulesOptionalParams;
use datadog_api_client::datadogV2::api_service_scorecards::ServiceScorecardsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListScorecardRules", true);
    let api = ServiceScorecardsAPI::with_config(configuration);
    let resp = api
        .list_scorecard_rules(ListScorecardRulesOptionalParams::default())
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

#####  List all rules
```
/**
 * List all rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listScorecardRules"] = true;
const apiInstance = new v2.ServiceScorecardsApi(configuration);

apiInstance
  .listScorecardRules()
  .then((data: v2.ListRulesResponse) => {
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
## [Delete a rule](https://docs.datadoghq.com/api/latest/service-scorecards/#delete-a-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-scorecards/#delete-a-rule-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.datadoghq.eu/api/v2/scorecard/rules/{rule_id}https://api.ddog-gov.com/api/v2/scorecard/rules/{rule_id}https://api.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.us3.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.us5.datadoghq.com/api/v2/scorecard/rules/{rule_id}
### Overview
Deletes a single rule.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-scorecards) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
rule_id [_required_]
string
The ID of the rule.
### Response
  * [204](https://docs.datadoghq.com/api/latest/service-scorecards/#DeleteScorecardRule-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-scorecards/#DeleteScorecardRule-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-scorecards/#DeleteScorecardRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/service-scorecards/#DeleteScorecardRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-scorecards/#DeleteScorecardRule-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=typescript)


#####  Delete a rule
Copy
```
                  # Path parameters  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scorecard/rules/${rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a rule
```
"""
Delete a rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_scorecard_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.delete_scorecard_rule(
        rule_id=CREATE_SCORECARD_RULE_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a rule
```
# Delete a rule returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_scorecard_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceScorecardsAPI.new

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = ENV["CREATE_SCORECARD_RULE_DATA_ID"]
api_instance.delete_scorecard_rule(CREATE_SCORECARD_RULE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a rule
```
// Delete a rule returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "create_scorecard_rule" in the system
	CreateScorecardRuleDataID := os.Getenv("CREATE_SCORECARD_RULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteScorecardRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceScorecardsApi(apiClient)
	r, err := api.DeleteScorecardRule(ctx, CreateScorecardRuleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceScorecardsApi.DeleteScorecardRule`: %v\n", err)
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

#####  Delete a rule
```
// Delete a rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceScorecardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteScorecardRule", true);
    ServiceScorecardsApi apiInstance = new ServiceScorecardsApi(defaultClient);

    // there is a valid "create_scorecard_rule" in the system
    String CREATE_SCORECARD_RULE_DATA_ID = System.getenv("CREATE_SCORECARD_RULE_DATA_ID");

    try {
      apiInstance.deleteScorecardRule(CREATE_SCORECARD_RULE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceScorecardsApi#deleteScorecardRule");
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

#####  Delete a rule
```
// Delete a rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_scorecards::ServiceScorecardsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "create_scorecard_rule" in the system
    let create_scorecard_rule_data_id = std::env::var("CREATE_SCORECARD_RULE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteScorecardRule", true);
    let api = ServiceScorecardsAPI::with_config(configuration);
    let resp = api
        .delete_scorecard_rule(create_scorecard_rule_data_id.clone())
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

#####  Delete a rule
```
/**
 * Delete a rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteScorecardRule"] = true;
const apiInstance = new v2.ServiceScorecardsApi(configuration);

// there is a valid "create_scorecard_rule" in the system
const CREATE_SCORECARD_RULE_DATA_ID = process.env
  .CREATE_SCORECARD_RULE_DATA_ID as string;

const params: v2.ServiceScorecardsApiDeleteScorecardRuleRequest = {
  ruleId: CREATE_SCORECARD_RULE_DATA_ID,
};

apiInstance
  .deleteScorecardRule(params)
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
## [Update an existing rule](https://docs.datadoghq.com/api/latest/service-scorecards/#update-an-existing-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/service-scorecards/#update-an-existing-rule-v2)


**Note** : This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PUT https://api.ap1.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.ap2.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.datadoghq.eu/api/v2/scorecard/rules/{rule_id}https://api.ddog-gov.com/api/v2/scorecard/rules/{rule_id}https://api.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.us3.datadoghq.com/api/v2/scorecard/rules/{rule_id}https://api.us5.datadoghq.com/api/v2/scorecard/rules/{rule_id}
### Overview
Updates an existing rule.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-scorecards) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
rule_id [_required_]
string
The ID of the rule.
### Request
#### Body Data (required)
Rule attributes.
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


Field
Type
Description
data
object
Data for the request to update a scorecard rule.
attributes
object
Details of a rule.
category
string
**DEPRECATED** : The scorecard name to which this rule must belong.
created_at
date-time
Creation time of the rule outcome.
custom
boolean
Defines if the rule is a custom rule.
description
string
Explanation of the rule.
enabled
boolean
If enabled, the rule is calculated as part of the score.
level
int32
The maturity level of the rule (1, 2, or 3).
modified_at
date-time
Time of the last rule outcome modification.
name
string
Name of the rule.
owner
string
Owner of the rule.
scorecard_name
string
The scorecard name to which this rule must belong.
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
```
{
  "data": {
    "attributes": {
      "enabled": true,
      "name": "Team Defined",
      "scorecard_name": "Deployments automated via Deployment Trains",
      "description": "Updated description via test"
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardRule-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardRule-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/service-scorecards/#UpdateScorecardRule-429-v2)


Rule updated successfully
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


The response from a rule update request.
Field
Type
Description
data
object
The data for a rule update response.
attributes
object
Details of a rule.
category
string
**DEPRECATED** : The scorecard name to which this rule must belong.
created_at
date-time
Creation time of the rule outcome.
custom
boolean
Defines if the rule is a custom rule.
description
string
Explanation of the rule.
enabled
boolean
If enabled, the rule is calculated as part of the score.
level
int32
The maturity level of the rule (1, 2, or 3).
modified_at
date-time
Time of the last rule outcome modification.
name
string
Name of the rule.
owner
string
Owner of the rule.
scorecard_name
string
The scorecard name to which this rule must belong.
id
string
The unique ID for a scorecard rule.
relationships
object
Scorecard create rule response relationship.
scorecard
object
Relationship data for a rule.
data
object
Rule relationship data.
id
string
The unique ID for a scorecard.
type
enum
The JSON:API type for scorecard. Allowed enum values: `scorecard`
default: `scorecard`
type
enum
The JSON:API type for scorecard rules. Allowed enum values: `rule`
default: `rule`
```
{
  "data": {
    "attributes": {
      "category": "string",
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom": false,
      "description": "string",
      "enabled": true,
      "level": 2,
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "Team Defined",
      "owner": "string",
      "scorecard_name": "Deployments automated via Deployment Trains"
    },
    "id": "q8MQxk8TCqrHnWkx",
    "relationships": {
      "scorecard": {
        "data": {
          "id": "q8MQxk8TCqrHnWkp",
          "type": "scorecard"
        }
      }
    },
    "type": "rule"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-scorecards/)
  * [Example](https://docs.datadoghq.com/api/latest/service-scorecards/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-scorecards/?code-lang=typescript)


#####  Update an existing rule returns "Rule updated successfully" response
Copy
```
                          # Path parameters  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scorecard/rules/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": true,
      "name": "Team Defined",
      "scorecard_name": "Deployments automated via Deployment Trains",
      "description": "Updated description via test"
    }
  }
}
EOF  

                        
```

#####  Update an existing rule returns "Rule updated successfully" response
```
// Update an existing rule returns "Rule updated successfully" response

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
	// there is a valid "create_scorecard_rule" in the system
	CreateScorecardRuleDataAttributesName := os.Getenv("CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME")
	CreateScorecardRuleDataAttributesScorecardName := os.Getenv("CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME")
	CreateScorecardRuleDataID := os.Getenv("CREATE_SCORECARD_RULE_DATA_ID")

	body := datadogV2.UpdateRuleRequest{
		Data: &datadogV2.UpdateRuleRequestData{
			Attributes: &datadogV2.RuleAttributes{
				Enabled:       datadog.PtrBool(true),
				Name:          datadog.PtrString(CreateScorecardRuleDataAttributesName),
				ScorecardName: datadog.PtrString(CreateScorecardRuleDataAttributesScorecardName),
				Description:   datadog.PtrString("Updated description via test"),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateScorecardRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewServiceScorecardsApi(apiClient)
	resp, r, err := api.UpdateScorecardRule(ctx, CreateScorecardRuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceScorecardsApi.UpdateScorecardRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceScorecardsApi.UpdateScorecardRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update an existing rule returns "Rule updated successfully" response
```
// Update an existing rule returns "Rule updated successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceScorecardsApi;
import com.datadog.api.client.v2.model.RuleAttributes;
import com.datadog.api.client.v2.model.UpdateRuleRequest;
import com.datadog.api.client.v2.model.UpdateRuleRequestData;
import com.datadog.api.client.v2.model.UpdateRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateScorecardRule", true);
    ServiceScorecardsApi apiInstance = new ServiceScorecardsApi(defaultClient);

    // there is a valid "create_scorecard_rule" in the system
    String CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME =
        System.getenv("CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME");
    String CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME =
        System.getenv("CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME");
    String CREATE_SCORECARD_RULE_DATA_ID = System.getenv("CREATE_SCORECARD_RULE_DATA_ID");

    UpdateRuleRequest body =
        new UpdateRuleRequest()
            .data(
                new UpdateRuleRequestData()
                    .attributes(
                        new RuleAttributes()
                            .enabled(true)
                            .name(CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME)
                            .scorecardName(CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME)
                            .description("Updated description via test")));

    try {
      UpdateRuleResponse result =
          apiInstance.updateScorecardRule(CREATE_SCORECARD_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceScorecardsApi#updateScorecardRule");
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

#####  Update an existing rule returns "Rule updated successfully" response
```
"""
Update an existing rule returns "Rule updated successfully" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.rule_attributes import RuleAttributes
from datadog_api_client.v2.model.update_rule_request import UpdateRuleRequest
from datadog_api_client.v2.model.update_rule_request_data import UpdateRuleRequestData

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME = environ["CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME"]
CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME = environ["CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME"]
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

body = UpdateRuleRequest(
    data=UpdateRuleRequestData(
        attributes=RuleAttributes(
            enabled=True,
            name=CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME,
            scorecard_name=CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME,
            description="Updated description via test",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_scorecard_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.update_scorecard_rule(rule_id=CREATE_SCORECARD_RULE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update an existing rule returns "Rule updated successfully" response
```
# Update an existing rule returns "Rule updated successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_scorecard_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceScorecardsAPI.new

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME = ENV["CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME"]
CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME = ENV["CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME"]
CREATE_SCORECARD_RULE_DATA_ID = ENV["CREATE_SCORECARD_RULE_DATA_ID"]

body = DatadogAPIClient::V2::UpdateRuleRequest.new({
  data: DatadogAPIClient::V2::UpdateRuleRequestData.new({
    attributes: DatadogAPIClient::V2::RuleAttributes.new({
      enabled: true,
      name: CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME,
      scorecard_name: CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME,
      description: "Updated description via test",
    }),
  }),
})
p api_instance.update_scorecard_rule(CREATE_SCORECARD_RULE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update an existing rule returns "Rule updated successfully" response
```
// Update an existing rule returns "Rule updated successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_scorecards::ServiceScorecardsAPI;
use datadog_api_client::datadogV2::model::RuleAttributes;
use datadog_api_client::datadogV2::model::UpdateRuleRequest;
use datadog_api_client::datadogV2::model::UpdateRuleRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "create_scorecard_rule" in the system
    let create_scorecard_rule_data_attributes_name =
        std::env::var("CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME").unwrap();
    let create_scorecard_rule_data_attributes_scorecard_name =
        std::env::var("CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME").unwrap();
    let create_scorecard_rule_data_id = std::env::var("CREATE_SCORECARD_RULE_DATA_ID").unwrap();
    let body = UpdateRuleRequest::new().data(
        UpdateRuleRequestData::new().attributes(
            RuleAttributes::new()
                .description("Updated description via test".to_string())
                .enabled(true)
                .name(create_scorecard_rule_data_attributes_name.clone())
                .scorecard_name(create_scorecard_rule_data_attributes_scorecard_name.clone()),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateScorecardRule", true);
    let api = ServiceScorecardsAPI::with_config(configuration);
    let resp = api
        .update_scorecard_rule(create_scorecard_rule_data_id.clone(), body)
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

#####  Update an existing rule returns "Rule updated successfully" response
```
/**
 * Update an existing rule returns "Rule updated successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateScorecardRule"] = true;
const apiInstance = new v2.ServiceScorecardsApi(configuration);

// there is a valid "create_scorecard_rule" in the system
const CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME = process.env
  .CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME as string;
const CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME = process.env
  .CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME as string;
const CREATE_SCORECARD_RULE_DATA_ID = process.env
  .CREATE_SCORECARD_RULE_DATA_ID as string;

const params: v2.ServiceScorecardsApiUpdateScorecardRuleRequest = {
  body: {
    data: {
      attributes: {
        enabled: true,
        name: CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_NAME,
        scorecardName: CREATE_SCORECARD_RULE_DATA_ATTRIBUTES_SCORECARD_NAME,
        description: "Updated description via test",
      },
    },
  },
  ruleId: CREATE_SCORECARD_RULE_DATA_ID,
};

apiInstance
  .updateScorecardRule(params)
  .then((data: v2.UpdateRuleResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=9f45b900-10a3-4084-84e8-5e1a68095181&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=1bd04605-3149-4ca8-bce0-ddd1bce0c4d4&pt=Service%20Scorecards&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-scorecards%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=9f45b900-10a3-4084-84e8-5e1a68095181&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=1bd04605-3149-4ca8-bce0-ddd1bce0c4d4&pt=Service%20Scorecards&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-scorecards%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=de8206a9-eaf5-464e-81de-58cfcba6a0db&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Service%20Scorecards&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-scorecards%2F&r=&lt=11503&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=537830)
