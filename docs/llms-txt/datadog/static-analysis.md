# Source: https://docs.datadoghq.com/api/latest/static-analysis.md

---
title: Static Analysis
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Static Analysis
---

# Static Analysis

API for static analysis

## POST request to resolve vulnerable symbols{% #post-request-to-resolve-vulnerable-symbols %}

{% tab title="v2" %}
**Note**: This endpoint may be subject to changes.
| Datadog site      | API endpoint                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols |

### Overview



OAuth apps require the `code_analysis_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#static-analysis) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description |
| ------------ | ---------------------- | -------- | ----------- |
|              | data                   | object   |
| data         | attributes             | object   |
| attributes   | purls                  | [string] |
| data         | id                     | string   |
| data         | type [*required*] | enum     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "purls": []
    },
    "id": "string",
    "type": "resolve-vulnerable-symbols-request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field       | Field                  | Type     | Description |
| ------------------ | ---------------------- | -------- | ----------- |
|                    | data                   | object   |
| data               | attributes             | object   |
| attributes         | results                | [object] |
| results            | purl                   | string   |
| results            | vulnerable_symbols     | [object] |
| vulnerable_symbols | advisory_id            | string   |
| vulnerable_symbols | symbols                | [object] |
| symbols            | name                   | string   |
| symbols            | type                   | string   |
| symbols            | value                  | string   |
| data               | id                     | string   |
| data               | type [*required*] | enum     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "results": [
        {
          "purl": "string",
          "vulnerable_symbols": [
            {
              "advisory_id": "string",
              "symbols": [
                {
                  "name": "string",
                  "type": "string",
                  "value": "string"
                }
              ]
            }
          ]
        }
      ]
    },
    "id": "string",
    "type": "resolve-vulnerable-symbols-response"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "resolve-vulnerable-symbols-request"
  }
}
EOF
                
##### 

```python
"""
POST request to resolve vulnerable symbols returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request import ResolveVulnerableSymbolsRequest
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data import ResolveVulnerableSymbolsRequestData
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_attributes import (
    ResolveVulnerableSymbolsRequestDataAttributes,
)
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_type import (
    ResolveVulnerableSymbolsRequestDataType,
)

body = ResolveVulnerableSymbolsRequest(
    data=ResolveVulnerableSymbolsRequestData(
        attributes=ResolveVulnerableSymbolsRequestDataAttributes(
            purls=[],
        ),
        type=ResolveVulnerableSymbolsRequestDataType.RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sca_resolve_vulnerable_symbols"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_sca_resolve_vulnerable_symbols(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# POST request to resolve vulnerable symbols returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_sca_resolve_vulnerable_symbols".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::ResolveVulnerableSymbolsRequest.new({
  data: DatadogAPIClient::V2::ResolveVulnerableSymbolsRequestData.new({
    attributes: DatadogAPIClient::V2::ResolveVulnerableSymbolsRequestDataAttributes.new({
      purls: [],
    }),
    type: DatadogAPIClient::V2::ResolveVulnerableSymbolsRequestDataType::RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
  }),
})
p api_instance.create_sca_resolve_vulnerable_symbols(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// POST request to resolve vulnerable symbols returns "OK" response

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
	body := datadogV2.ResolveVulnerableSymbolsRequest{
		Data: &datadogV2.ResolveVulnerableSymbolsRequestData{
			Attributes: &datadogV2.ResolveVulnerableSymbolsRequestDataAttributes{
				Purls: []string{},
			},
			Type: datadogV2.RESOLVEVULNERABLESYMBOLSREQUESTDATATYPE_RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateSCAResolveVulnerableSymbols", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.CreateSCAResolveVulnerableSymbols(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.CreateSCAResolveVulnerableSymbols`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.CreateSCAResolveVulnerableSymbols`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// POST request to resolve vulnerable symbols returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequest;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequestData;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequestDataAttributes;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsRequestDataType;
import com.datadog.api.client.v2.model.ResolveVulnerableSymbolsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createSCAResolveVulnerableSymbols", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    ResolveVulnerableSymbolsRequest body =
        new ResolveVulnerableSymbolsRequest()
            .data(
                new ResolveVulnerableSymbolsRequestData()
                    .attributes(new ResolveVulnerableSymbolsRequestDataAttributes())
                    .type(
                        ResolveVulnerableSymbolsRequestDataType
                            .RESOLVE_VULNERABLE_SYMBOLS_REQUEST));

    try {
      ResolveVulnerableSymbolsResponse result = apiInstance.createSCAResolveVulnerableSymbols(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling StaticAnalysisApi#createSCAResolveVulnerableSymbols");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// POST request to resolve vulnerable symbols returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequest;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequestData;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequestDataAttributes;
use datadog_api_client::datadogV2::model::ResolveVulnerableSymbolsRequestDataType;

#[tokio::main]
async fn main() {
    let body = ResolveVulnerableSymbolsRequest::new().data(
        ResolveVulnerableSymbolsRequestData::new(
            ResolveVulnerableSymbolsRequestDataType::RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
        )
        .attributes(ResolveVulnerableSymbolsRequestDataAttributes::new().purls(vec![])),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateSCAResolveVulnerableSymbols", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api.create_sca_resolve_vulnerable_symbols(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * POST request to resolve vulnerable symbols returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createSCAResolveVulnerableSymbols"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiCreateSCAResolveVulnerableSymbolsRequest = {
  body: {
    data: {
      attributes: {
        purls: [],
      },
      type: "resolve-vulnerable-symbols-request",
    },
  },
};

apiInstance
  .createSCAResolveVulnerableSymbols(params)
  .then((data: v2.ResolveVulnerableSymbolsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Revert Custom Rule Revision{% #revert-custom-rule-revision %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert |

### Overview

Revert a custom rule to a previous revision

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |
| rule_name [*required*]    | string | The rule name    |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field            | Type   | Description                                                             |
| ------------ | ---------------- | ------ | ----------------------------------------------------------------------- |
|              | data             | object |
| data         | attributes       | object |
| attributes   | currentRevision  | string | Current revision ID                                                     |
| attributes   | revertToRevision | string | Target revision ID to revert to                                         |
| data         | id               | string | Request identifier                                                      |
| data         | type             | enum   | Request type Allowed enum values: `revert_custom_rule_revision_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "currentRevision": "string",
      "revertToRevision": "string"
    },
    "id": "string",
    "type": "string"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Successfully reverted
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"export rule_name="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}/rules/${rule_name}/revisions/revert" \
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
Revert Custom Rule Revision returns "Successfully reverted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.revert_custom_rule_revision_data_type import RevertCustomRuleRevisionDataType
from datadog_api_client.v2.model.revert_custom_rule_revision_request import RevertCustomRuleRevisionRequest
from datadog_api_client.v2.model.revert_custom_rule_revision_request_data import RevertCustomRuleRevisionRequestData
from datadog_api_client.v2.model.revert_custom_rule_revision_request_data_attributes import (
    RevertCustomRuleRevisionRequestDataAttributes,
)

body = RevertCustomRuleRevisionRequest(
    data=RevertCustomRuleRevisionRequestData(
        attributes=RevertCustomRuleRevisionRequestDataAttributes(),
        type=RevertCustomRuleRevisionDataType.REVERT_CUSTOM_RULE_REVISION_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["revert_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.revert_custom_rule_revision(ruleset_name="ruleset_name", rule_name="rule_name", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Revert Custom Rule Revision returns "Successfully reverted" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.revert_custom_rule_revision".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::RevertCustomRuleRevisionRequest.new({
  data: DatadogAPIClient::V2::RevertCustomRuleRevisionRequestData.new({
    attributes: DatadogAPIClient::V2::RevertCustomRuleRevisionRequestDataAttributes.new({}),
    type: DatadogAPIClient::V2::RevertCustomRuleRevisionDataType::REVERT_CUSTOM_RULE_REVISION_REQUEST,
  }),
})
p api_instance.revert_custom_rule_revision("ruleset_name", "rule_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Revert Custom Rule Revision returns "Successfully reverted" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.RevertCustomRuleRevisionRequest{
		Data: &datadogV2.RevertCustomRuleRevisionRequestData{
			Attributes: &datadogV2.RevertCustomRuleRevisionRequestDataAttributes{},
			Type:       datadogV2.REVERTCUSTOMRULEREVISIONDATATYPE_REVERT_CUSTOM_RULE_REVISION_REQUEST.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.RevertCustomRuleRevision", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	r, err := api.RevertCustomRuleRevision(ctx, "ruleset_name", "rule_name", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.RevertCustomRuleRevision`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Revert Custom Rule Revision returns "Successfully reverted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.RevertCustomRuleRevisionDataType;
import com.datadog.api.client.v2.model.RevertCustomRuleRevisionRequest;
import com.datadog.api.client.v2.model.RevertCustomRuleRevisionRequestData;
import com.datadog.api.client.v2.model.RevertCustomRuleRevisionRequestDataAttributes;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.revertCustomRuleRevision", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    RevertCustomRuleRevisionRequest body =
        new RevertCustomRuleRevisionRequest()
            .data(
                new RevertCustomRuleRevisionRequestData()
                    .attributes(new RevertCustomRuleRevisionRequestDataAttributes())
                    .type(RevertCustomRuleRevisionDataType.REVERT_CUSTOM_RULE_REVISION_REQUEST));

    try {
      apiInstance.revertCustomRuleRevision("ruleset_name", "rule_name", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#revertCustomRuleRevision");
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
// Revert Custom Rule Revision returns "Successfully reverted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::RevertCustomRuleRevisionDataType;
use datadog_api_client::datadogV2::model::RevertCustomRuleRevisionRequest;
use datadog_api_client::datadogV2::model::RevertCustomRuleRevisionRequestData;
use datadog_api_client::datadogV2::model::RevertCustomRuleRevisionRequestDataAttributes;

#[tokio::main]
async fn main() {
    let body = RevertCustomRuleRevisionRequest::new().data(
        RevertCustomRuleRevisionRequestData::new()
            .attributes(RevertCustomRuleRevisionRequestDataAttributes::new())
            .type_(RevertCustomRuleRevisionDataType::REVERT_CUSTOM_RULE_REVISION_REQUEST),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.RevertCustomRuleRevision", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .revert_custom_rule_revision("ruleset_name".to_string(), "rule_name".to_string(), body)
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
 * Revert Custom Rule Revision returns "Successfully reverted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.revertCustomRuleRevision"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiRevertCustomRuleRevisionRequest = {
  body: {
    data: {
      attributes: {},
      type: "revert_custom_rule_revision_request",
    },
  },
  rulesetName: "ruleset_name",
  ruleName: "rule_name",
};

apiInstance
  .revertCustomRuleRevision(params)
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

## Post dependencies for analysis{% #post-dependencies-for-analysis %}

{% tab title="v2" %}
**Note**: This endpoint may be subject to changes.
| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/static-analysis-sca/dependencies |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/static-analysis-sca/dependencies |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/static-analysis-sca/dependencies      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/static-analysis-sca/dependencies      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/static-analysis-sca/dependencies     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/static-analysis-sca/dependencies |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/static-analysis-sca/dependencies |

### Overview



OAuth apps require the `code_analysis_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#static-analysis) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field                | Field                       | Type     | Description |
| --------------------------- | --------------------------- | -------- | ----------- |
|                             | data                        | object   |
| data                        | attributes                  | object   |
| attributes                  | commit                      | object   |
| commit                      | author_date                 | string   |
| commit                      | author_email                | string   |
| commit                      | author_name                 | string   |
| commit                      | branch                      | string   |
| commit                      | committer_email             | string   |
| commit                      | committer_name              | string   |
| commit                      | sha                         | string   |
| attributes                  | dependencies                | [object] |
| dependencies                | exclusions                  | [string] |
| dependencies                | group                       | string   |
| dependencies                | is_dev                      | boolean  |
| dependencies                | is_direct                   | boolean  |
| dependencies                | language                    | string   |
| dependencies                | locations                   | [object] |
| locations                   | block                       | object   |
| block                       | end                         | object   |
| end                         | col                         | int32    |
| end                         | line                        | int32    |
| block                       | file_name                   | string   |
| block                       | start                       | object   |
| start                       | col                         | int32    |
| start                       | line                        | int32    |
| locations                   | name                        | object   |
| name                        | end                         | object   |
| end                         | col                         | int32    |
| end                         | line                        | int32    |
| name                        | file_name                   | string   |
| name                        | start                       | object   |
| start                       | col                         | int32    |
| start                       | line                        | int32    |
| locations                   | namespace                   | object   |
| namespace                   | end                         | object   |
| end                         | col                         | int32    |
| end                         | line                        | int32    |
| namespace                   | file_name                   | string   |
| namespace                   | start                       | object   |
| start                       | col                         | int32    |
| start                       | line                        | int32    |
| locations                   | version                     | object   |
| version                     | end                         | object   |
| end                         | col                         | int32    |
| end                         | line                        | int32    |
| version                     | file_name                   | string   |
| version                     | start                       | object   |
| start                       | col                         | int32    |
| start                       | line                        | int32    |
| dependencies                | name                        | string   |
| dependencies                | package_manager             | string   |
| dependencies                | purl                        | string   |
| dependencies                | reachable_symbol_properties | [object] |
| reachable_symbol_properties | name                        | string   |
| reachable_symbol_properties | value                       | string   |
| dependencies                | version                     | string   |
| attributes                  | env                         | string   |
| attributes                  | files                       | [object] |
| files                       | name                        | string   |
| files                       | purl                        | string   |
| attributes                  | relations                   | [object] |
| relations                   | depends_on                  | [string] |
| relations                   | ref                         | string   |
| attributes                  | repository                  | object   |
| repository                  | url                         | string   |
| attributes                  | service                     | string   |
| attributes                  | tags                        | object   |
| additionalProperties        | <any-key>                   | string   |
| attributes                  | vulnerabilities             | [object] |
| vulnerabilities             | affects                     | [object] |
| affects                     | ref                         | string   |
| vulnerabilities             | bom_ref                     | string   |
| vulnerabilities             | id                          | string   |
| data                        | id                          | string   |
| data                        | type [*required*]      | enum     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "commit": {
        "author_date": "string",
        "author_email": "string",
        "author_name": "string",
        "branch": "string",
        "committer_email": "string",
        "committer_name": "string",
        "sha": "string"
      },
      "dependencies": [
        {
          "exclusions": [],
          "group": "string",
          "is_dev": false,
          "is_direct": false,
          "language": "string",
          "locations": [
            {
              "block": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              },
              "name": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              },
              "namespace": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              },
              "version": {
                "end": {
                  "col": "integer",
                  "line": "integer"
                },
                "file_name": "string",
                "start": {
                  "col": "integer",
                  "line": "integer"
                }
              }
            }
          ],
          "name": "string",
          "package_manager": "string",
          "purl": "string",
          "reachable_symbol_properties": [
            {
              "name": "string",
              "value": "string"
            }
          ],
          "version": "string"
        }
      ],
      "env": "string",
      "files": [
        {
          "name": "string",
          "purl": "string"
        }
      ],
      "relations": [
        {
          "depends_on": [],
          "ref": "string"
        }
      ],
      "repository": {
        "url": "string"
      },
      "service": "string",
      "tags": {
        "<any-key>": "string"
      },
      "vulnerabilities": [
        {
          "affects": [
            {
              "ref": "string"
            }
          ],
          "bom_ref": "string",
          "id": "string"
        }
      ]
    },
    "id": "string",
    "type": "scarequests"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis-sca/dependencies" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "scarequests"
  }
}
EOF
                
##### 

```python
"""
Post dependencies for analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.sca_request import ScaRequest
from datadog_api_client.v2.model.sca_request_data import ScaRequestData
from datadog_api_client.v2.model.sca_request_data_attributes import ScaRequestDataAttributes
from datadog_api_client.v2.model.sca_request_data_attributes_commit import ScaRequestDataAttributesCommit
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items import (
    ScaRequestDataAttributesDependenciesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items import (
    ScaRequestDataAttributesDependenciesItemsLocationsItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_file_position import (
    ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_position import (
    ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_reachable_symbol_properties_items import (
    ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_files_items import ScaRequestDataAttributesFilesItems
from datadog_api_client.v2.model.sca_request_data_attributes_relations_items import (
    ScaRequestDataAttributesRelationsItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_repository import ScaRequestDataAttributesRepository
from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items import (
    ScaRequestDataAttributesVulnerabilitiesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items_affects_items import (
    ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems,
)
from datadog_api_client.v2.model.sca_request_data_type import ScaRequestDataType

body = ScaRequest(
    data=ScaRequestData(
        attributes=ScaRequestDataAttributes(
            commit=ScaRequestDataAttributesCommit(),
            dependencies=[
                ScaRequestDataAttributesDependenciesItems(
                    exclusions=[],
                    locations=[
                        ScaRequestDataAttributesDependenciesItemsLocationsItems(
                            block=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            name=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            namespace=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            version=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                        ),
                    ],
                    reachable_symbol_properties=[
                        ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems(),
                    ],
                ),
            ],
            files=[
                ScaRequestDataAttributesFilesItems(),
            ],
            relations=[
                ScaRequestDataAttributesRelationsItems(
                    depends_on=[],
                ),
            ],
            repository=ScaRequestDataAttributesRepository(),
            vulnerabilities=[
                ScaRequestDataAttributesVulnerabilitiesItems(
                    affects=[
                        ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems(),
                    ],
                ),
            ],
        ),
        type=ScaRequestDataType.SCAREQUESTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sca_result"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.create_sca_result(body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Post dependencies for analysis returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_sca_result".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::ScaRequest.new({
  data: DatadogAPIClient::V2::ScaRequestData.new({
    attributes: DatadogAPIClient::V2::ScaRequestDataAttributes.new({
      commit: DatadogAPIClient::V2::ScaRequestDataAttributesCommit.new({}),
      dependencies: [
        DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItems.new({
          exclusions: [],
          locations: [
            DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItems.new({
              block: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
              name: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
              namespace: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
              version: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition.new({
                _end: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
                start: DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition.new({}),
              }),
            }),
          ],
          reachable_symbol_properties: [
            DatadogAPIClient::V2::ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems.new({}),
          ],
        }),
      ],
      files: [
        DatadogAPIClient::V2::ScaRequestDataAttributesFilesItems.new({}),
      ],
      relations: [
        DatadogAPIClient::V2::ScaRequestDataAttributesRelationsItems.new({
          depends_on: [],
        }),
      ],
      repository: DatadogAPIClient::V2::ScaRequestDataAttributesRepository.new({}),
      vulnerabilities: [
        DatadogAPIClient::V2::ScaRequestDataAttributesVulnerabilitiesItems.new({
          affects: [
            DatadogAPIClient::V2::ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems.new({}),
          ],
        }),
      ],
    }),
    type: DatadogAPIClient::V2::ScaRequestDataType::SCAREQUESTS,
  }),
})
p api_instance.create_sca_result(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Post dependencies for analysis returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.ScaRequest{
		Data: &datadogV2.ScaRequestData{
			Attributes: &datadogV2.ScaRequestDataAttributes{
				Commit: &datadogV2.ScaRequestDataAttributesCommit{},
				Dependencies: []datadogV2.ScaRequestDataAttributesDependenciesItems{
					{
						Exclusions: []string{},
						Locations: []datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItems{
							{
								Block: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
								Name: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
								Namespace: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
								Version: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition{
									End:   &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
									Start: &datadogV2.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition{},
								},
							},
						},
						ReachableSymbolProperties: []datadogV2.ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems{
							{},
						},
					},
				},
				Files: []datadogV2.ScaRequestDataAttributesFilesItems{
					{},
				},
				Relations: []datadogV2.ScaRequestDataAttributesRelationsItems{
					{
						DependsOn: []string{},
					},
				},
				Repository: &datadogV2.ScaRequestDataAttributesRepository{},
				Vulnerabilities: []datadogV2.ScaRequestDataAttributesVulnerabilitiesItems{
					{
						Affects: []datadogV2.ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems{
							{},
						},
					},
				},
			},
			Type: datadogV2.SCAREQUESTDATATYPE_SCAREQUESTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateSCAResult", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	r, err := api.CreateSCAResult(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.CreateSCAResult`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Post dependencies for analysis returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.ScaRequest;
import com.datadog.api.client.v2.model.ScaRequestData;
import com.datadog.api.client.v2.model.ScaRequestDataAttributes;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesCommit;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsLocationsItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesFilesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesRelationsItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesRepository;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesVulnerabilitiesItems;
import com.datadog.api.client.v2.model.ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems;
import com.datadog.api.client.v2.model.ScaRequestDataType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createSCAResult", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    ScaRequest body =
        new ScaRequest()
            .data(
                new ScaRequestData()
                    .attributes(
                        new ScaRequestDataAttributes()
                            .commit(new ScaRequestDataAttributesCommit())
                            .dependencies(
                                Collections.singletonList(
                                    new ScaRequestDataAttributesDependenciesItems()
                                        .locations(
                                            Collections.singletonList(
                                                new ScaRequestDataAttributesDependenciesItemsLocationsItems()
                                                    .block(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))
                                                    .name(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))
                                                    .namespace(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))
                                                    .version(
                                                        new ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition()
                                                            .end(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition())
                                                            .start(
                                                                new ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition()))))
                                        .reachableSymbolProperties(
                                            Collections.singletonList(
                                                new ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems()))))
                            .files(
                                Collections.singletonList(new ScaRequestDataAttributesFilesItems()))
                            .relations(
                                Collections.singletonList(
                                    new ScaRequestDataAttributesRelationsItems()))
                            .repository(new ScaRequestDataAttributesRepository())
                            .vulnerabilities(
                                Collections.singletonList(
                                    new ScaRequestDataAttributesVulnerabilitiesItems()
                                        .affects(
                                            Collections.singletonList(
                                                new ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems())))))
                    .type(ScaRequestDataType.SCAREQUESTS));

    try {
      apiInstance.createSCAResult(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#createSCAResult");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Post dependencies for analysis returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::ScaRequest;
use datadog_api_client::datadogV2::model::ScaRequestData;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributes;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesCommit;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsLocationsItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesFilesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesRelationsItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesRepository;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesVulnerabilitiesItems;
use datadog_api_client::datadogV2::model::ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems;
use datadog_api_client::datadogV2::model::ScaRequestDataType;

#[tokio::main]
async fn main() {
    let body =
        ScaRequest
        ::new().data(
            ScaRequestData::new(
                ScaRequestDataType::SCAREQUESTS,
            ).attributes(
                ScaRequestDataAttributes::new()
                    .commit(ScaRequestDataAttributesCommit::new())
                    .dependencies(
                        vec![
                            ScaRequestDataAttributesDependenciesItems::new()
                                .exclusions(vec![])
                                .locations(
                                    vec![
                                        ScaRequestDataAttributesDependenciesItemsLocationsItems::new()
                                            .block(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                            .name(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                            .namespace(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                            .version(
                                                ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition
                                                ::new()
                                                    .end(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    )
                                                    .start(
                                                        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition
                                                        ::new(),
                                                    ),
                                            )
                                    ],
                                )
                                .reachable_symbol_properties(
                                    vec![
                                        ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems::new()
                                    ],
                                )
                        ],
                    )
                    .files(vec![ScaRequestDataAttributesFilesItems::new()])
                    .relations(vec![ScaRequestDataAttributesRelationsItems::new().depends_on(vec![])])
                    .repository(ScaRequestDataAttributesRepository::new())
                    .vulnerabilities(
                        vec![
                            ScaRequestDataAttributesVulnerabilitiesItems
                            ::new().affects(vec![ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems::new()])
                        ],
                    ),
            ),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateSCAResult", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api.create_sca_result(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Post dependencies for analysis returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createSCAResult"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiCreateSCAResultRequest = {
  body: {
    data: {
      attributes: {
        commit: {},
        dependencies: [
          {
            exclusions: [],
            locations: [
              {
                block: {
                  end: {},
                  start: {},
                },
                name: {
                  end: {},
                  start: {},
                },
                namespace: {
                  end: {},
                  start: {},
                },
                version: {
                  end: {},
                  start: {},
                },
              },
            ],
            reachableSymbolProperties: [{}],
          },
        ],
        files: [{}],
        relations: [
          {
            dependsOn: [],
          },
        ],
        repository: {},
        vulnerabilities: [
          {
            affects: [{}],
          },
        ],
      },
      type: "scarequests",
    },
  },
};

apiInstance
  .createSCAResult(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Show Custom Rule Revision{% #show-custom-rule-revision %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id} |

### Overview

Get a specific revision of a custom rule

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |
| rule_name [*required*]    | string | The rule name    |
| id [*required*]           | string | The revision ID  |

### Response

{% tab title="200" %}
Successful response
{% tab title="Model" %}

| Parent field | Field                               | Type      | Description                                                                                                        |
| ------------ | ----------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]              | object    |
| data         | attributes [*required*]        | object    |
| attributes   | arguments [*required*]         | [object]  | Rule arguments                                                                                                     |
| arguments    | description [*required*]       | string    | Base64-encoded argument description                                                                                |
| arguments    | name [*required*]              | string    | Base64-encoded argument name                                                                                       |
| attributes   | category [*required*]          | enum      | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes   | checksum [*required*]          | string    | Code checksum                                                                                                      |
| attributes   | code [*required*]              | string    | Rule code                                                                                                          |
| attributes   | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes   | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes   | creation_message [*required*]  | string    | Revision creation message                                                                                          |
| attributes   | cve [*required*]               | string    | Associated CVE                                                                                                     |
| attributes   | cwe [*required*]               | string    | Associated CWE                                                                                                     |
| attributes   | description [*required*]       | string    | Full description                                                                                                   |
| attributes   | documentation_url [*required*] | string    | Documentation URL                                                                                                  |
| attributes   | is_published [*required*]      | boolean   | Whether the revision is published                                                                                  |
| attributes   | is_testing [*required*]        | boolean   | Whether this is a testing revision                                                                                 |
| attributes   | language [*required*]          | enum      | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes   | severity [*required*]          | enum      | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes   | short_description [*required*] | string    | Short description                                                                                                  |
| attributes   | should_use_ai_fix [*required*] | boolean   | Whether to use AI for fixes                                                                                        |
| attributes   | tags [*required*]              | [string]  | Rule tags                                                                                                          |
| attributes   | tests [*required*]             | [object]  | Rule tests                                                                                                         |
| tests        | annotation_count [*required*]  | int64     | Expected violation count                                                                                           |
| tests        | code [*required*]              | string    | Test code                                                                                                          |
| tests        | filename [*required*]          | string    | Test filename                                                                                                      |
| attributes   | tree_sitter_query [*required*] | string    | Tree-sitter query                                                                                                  |
| data         | id [*required*]                | string    | Revision identifier                                                                                                |
| data         | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule_revision`                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "arguments": [
        {
          "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
          "name": "YXJndW1lbnRfbmFtZQ=="
        }
      ],
      "category": "SECURITY",
      "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
      "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
      "created_at": "2026-01-09T13:00:57.473141Z",
      "created_by": "foobarbaz",
      "creation_message": "Initial revision",
      "cve": "CVE-2024-1234",
      "cwe": "CWE-79",
      "description": "bG9uZyBkZXNjcmlwdGlvbg==",
      "documentation_url": "https://docs.example.com/rules/my-rule",
      "is_published": false,
      "is_testing": false,
      "language": "PYTHON",
      "severity": "ERROR",
      "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
      "should_use_ai_fix": false,
      "tags": [
        "security",
        "custom"
      ],
      "tests": [
        {
          "annotation_count": 1,
          "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
          "filename": "test.yaml"
        }
      ],
      "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
    },
    "id": "revision-123",
    "type": "custom_rule_revision"
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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
Revision not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"export rule_name="CHANGE_ME"export id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}/rules/${rule_name}/revisions/${id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Show Custom Rule Revision returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_custom_rule_revision(
        ruleset_name="ruleset_name",
        rule_name="rule_name",
        id="id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Show Custom Rule Revision returns "Successful response" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_custom_rule_revision".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new
p api_instance.get_custom_rule_revision("ruleset_name", "rule_name", "id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Show Custom Rule Revision returns "Successful response" response

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
	configuration.SetUnstableOperationEnabled("v2.GetCustomRuleRevision", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.GetCustomRuleRevision(ctx, "ruleset_name", "rule_name", "id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.GetCustomRuleRevision`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.GetCustomRuleRevision`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Show Custom Rule Revision returns "Successful response" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.CustomRuleRevisionResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getCustomRuleRevision", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    try {
      CustomRuleRevisionResponse result =
          apiInstance.getCustomRuleRevision("ruleset_name", "rule_name", "id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#getCustomRuleRevision");
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
// Show Custom Rule Revision returns "Successful response" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetCustomRuleRevision", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .get_custom_rule_revision(
            "ruleset_name".to_string(),
            "rule_name".to_string(),
            "id".to_string(),
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
 * Show Custom Rule Revision returns "Successful response" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getCustomRuleRevision"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiGetCustomRuleRevisionRequest = {
  rulesetName: "ruleset_name",
  ruleName: "rule_name",
  id: "id",
};

apiInstance
  .getCustomRuleRevision(params)
  .then((data: v2.CustomRuleRevisionResponse) => {
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

## Create Custom Rule Revision{% #create-custom-rule-revision %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |

### Overview

Create a new revision for a custom rule

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |
| rule_name [*required*]    | string | The rule name    |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                               | Type     | Description                                                                                                        |
| ------------ | ----------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
|              | data                                | object   |
| data         | attributes                          | object   |
| attributes   | arguments [*required*]         | [object] | Rule arguments                                                                                                     |
| arguments    | description [*required*]       | string   | Base64-encoded argument description                                                                                |
| arguments    | name [*required*]              | string   | Base64-encoded argument name                                                                                       |
| attributes   | category [*required*]          | enum     | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes   | code [*required*]              | string   | Rule code                                                                                                          |
| attributes   | creation_message [*required*]  | string   | Revision creation message                                                                                          |
| attributes   | cve [*required*]               | string   | Associated CVE                                                                                                     |
| attributes   | cwe [*required*]               | string   | Associated CWE                                                                                                     |
| attributes   | description [*required*]       | string   | Full description                                                                                                   |
| attributes   | documentation_url [*required*] | string   | Documentation URL                                                                                                  |
| attributes   | is_published [*required*]      | boolean  | Whether the revision is published                                                                                  |
| attributes   | is_testing [*required*]        | boolean  | Whether this is a testing revision                                                                                 |
| attributes   | language [*required*]          | enum     | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes   | severity [*required*]          | enum     | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes   | short_description [*required*] | string   | Short description                                                                                                  |
| attributes   | should_use_ai_fix [*required*] | boolean  | Whether to use AI for fixes                                                                                        |
| attributes   | tags [*required*]              | [string] | Rule tags                                                                                                          |
| attributes   | tests [*required*]             | [object] | Rule tests                                                                                                         |
| tests        | annotation_count [*required*]  | int64    | Expected violation count                                                                                           |
| tests        | code [*required*]              | string   | Test code                                                                                                          |
| tests        | filename [*required*]          | string   | Test filename                                                                                                      |
| attributes   | tree_sitter_query [*required*] | string   | Tree-sitter query                                                                                                  |
| data         | id                                  | string   | Revision identifier                                                                                                |
| data         | type                                | enum     | Resource type Allowed enum values: `custom_rule_revision`                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "arguments": [
        {
          "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
          "name": "YXJndW1lbnRfbmFtZQ=="
        }
      ],
      "category": "SECURITY",
      "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
      "creation_message": "Initial revision",
      "cve": "CVE-2024-1234",
      "cwe": "CWE-79",
      "description": "bG9uZyBkZXNjcmlwdGlvbg==",
      "documentation_url": "https://docs.example.com/rules/my-rule",
      "is_published": false,
      "is_testing": false,
      "language": "PYTHON",
      "severity": "ERROR",
      "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
      "should_use_ai_fix": false,
      "tags": [
        "security",
        "custom"
      ],
      "tests": [
        {
          "annotation_count": 1,
          "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
          "filename": "test.yaml"
        }
      ],
      "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
    },
    "id": "string",
    "type": "custom_rule_revision"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Successfully created
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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
Rule not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"export rule_name="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}/rules/${rule_name}/revisions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "arguments": [
        {
          "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
          "name": "YXJndW1lbnRfbmFtZQ=="
        }
      ],
      "category": "SECURITY",
      "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
      "creation_message": "Initial revision",
      "cve": "CVE-2024-1234",
      "cwe": "CWE-79",
      "description": "bG9uZyBkZXNjcmlwdGlvbg==",
      "documentation_url": "https://docs.example.com/rules/my-rule",
      "is_published": false,
      "is_testing": false,
      "language": "PYTHON",
      "severity": "ERROR",
      "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
      "should_use_ai_fix": false,
      "tags": [
        "security",
        "custom"
      ],
      "tests": [
        {
          "annotation_count": 1,
          "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
          "filename": "test.yaml"
        }
      ],
      "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
    }
  }
}
EOF
                
##### 

```python
"""
Create Custom Rule Revision returns "Successfully created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.argument import Argument
from datadog_api_client.v2.model.custom_rule_revision_attributes_category import CustomRuleRevisionAttributesCategory
from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import CustomRuleRevisionAttributesSeverity
from datadog_api_client.v2.model.custom_rule_revision_data_type import CustomRuleRevisionDataType
from datadog_api_client.v2.model.custom_rule_revision_input_attributes import CustomRuleRevisionInputAttributes
from datadog_api_client.v2.model.custom_rule_revision_request import CustomRuleRevisionRequest
from datadog_api_client.v2.model.custom_rule_revision_request_data import CustomRuleRevisionRequestData
from datadog_api_client.v2.model.custom_rule_revision_test import CustomRuleRevisionTest
from datadog_api_client.v2.model.language import Language

body = CustomRuleRevisionRequest(
    data=CustomRuleRevisionRequestData(
        attributes=CustomRuleRevisionInputAttributes(
            arguments=[
                Argument(
                    description="YXJndW1lbnQgZGVzY3JpcHRpb24=",
                    name="YXJndW1lbnRfbmFtZQ==",
                ),
            ],
            category=CustomRuleRevisionAttributesCategory.SECURITY,
            code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
            creation_message="Initial revision",
            cve="CVE-2024-1234",
            cwe="CWE-79",
            description="bG9uZyBkZXNjcmlwdGlvbg==",
            documentation_url="https://docs.example.com/rules/my-rule",
            is_published=False,
            is_testing=False,
            language=Language.PYTHON,
            severity=CustomRuleRevisionAttributesSeverity.ERROR,
            short_description="c2hvcnQgZGVzY3JpcHRpb24=",
            should_use_ai_fix=False,
            tags=[
                "security",
                "custom",
            ],
            tests=[
                CustomRuleRevisionTest(
                    annotation_count=1,
                    code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                    filename="test.yaml",
                ),
            ],
            tree_sitter_query="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
        ),
        type=CustomRuleRevisionDataType.CUSTOM_RULE_REVISION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.create_custom_rule_revision(ruleset_name="ruleset_name", rule_name="rule_name", body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create Custom Rule Revision returns "Successfully created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_custom_rule_revision".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::CustomRuleRevisionRequest.new({
  data: DatadogAPIClient::V2::CustomRuleRevisionRequestData.new({
    attributes: DatadogAPIClient::V2::CustomRuleRevisionInputAttributes.new({
      arguments: [
        DatadogAPIClient::V2::Argument.new({
          description: "YXJndW1lbnQgZGVzY3JpcHRpb24=",
          name: "YXJndW1lbnRfbmFtZQ==",
        }),
      ],
      category: DatadogAPIClient::V2::CustomRuleRevisionAttributesCategory::SECURITY,
      code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
      creation_message: "Initial revision",
      cve: "CVE-2024-1234",
      cwe: "CWE-79",
      description: "bG9uZyBkZXNjcmlwdGlvbg==",
      documentation_url: "https://docs.example.com/rules/my-rule",
      is_published: false,
      is_testing: false,
      language: DatadogAPIClient::V2::Language::PYTHON,
      severity: DatadogAPIClient::V2::CustomRuleRevisionAttributesSeverity::ERROR,
      short_description: "c2hvcnQgZGVzY3JpcHRpb24=",
      should_use_ai_fix: false,
      tags: [
        "security",
        "custom",
      ],
      tests: [
        DatadogAPIClient::V2::CustomRuleRevisionTest.new({
          annotation_count: 1,
          code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
          filename: "test.yaml",
        }),
      ],
      tree_sitter_query: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
    }),
    type: DatadogAPIClient::V2::CustomRuleRevisionDataType::CUSTOM_RULE_REVISION,
  }),
})
p api_instance.create_custom_rule_revision("ruleset_name", "rule_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Create Custom Rule Revision returns "Successfully created" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CustomRuleRevisionRequest{
		Data: &datadogV2.CustomRuleRevisionRequestData{
			Attributes: &datadogV2.CustomRuleRevisionInputAttributes{
				Arguments: []datadogV2.Argument{
					{
						Description: "YXJndW1lbnQgZGVzY3JpcHRpb24=",
						Name:        "YXJndW1lbnRfbmFtZQ==",
					},
				},
				Category:         datadogV2.CUSTOMRULEREVISIONATTRIBUTESCATEGORY_SECURITY,
				Code:             "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
				CreationMessage:  "Initial revision",
				Cve:              *datadog.NewNullableString(datadog.PtrString("CVE-2024-1234")),
				Cwe:              *datadog.NewNullableString(datadog.PtrString("CWE-79")),
				Description:      "bG9uZyBkZXNjcmlwdGlvbg==",
				DocumentationUrl: *datadog.NewNullableString(datadog.PtrString("https://docs.example.com/rules/my-rule")),
				IsPublished:      false,
				IsTesting:        false,
				Language:         datadogV2.LANGUAGE_PYTHON,
				Severity:         datadogV2.CUSTOMRULEREVISIONATTRIBUTESSEVERITY_ERROR,
				ShortDescription: "c2hvcnQgZGVzY3JpcHRpb24=",
				ShouldUseAiFix:   false,
				Tags: []string{
					"security",
					"custom",
				},
				Tests: []datadogV2.CustomRuleRevisionTest{
					{
						AnnotationCount: 1,
						Code:            "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
						Filename:        "test.yaml",
					},
				},
				TreeSitterQuery: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
			},
			Type: datadogV2.CUSTOMRULEREVISIONDATATYPE_CUSTOM_RULE_REVISION.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateCustomRuleRevision", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	r, err := api.CreateCustomRuleRevision(ctx, "ruleset_name", "rule_name", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.CreateCustomRuleRevision`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create Custom Rule Revision returns "Successfully created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.Argument;
import com.datadog.api.client.v2.model.CustomRuleRevisionAttributesCategory;
import com.datadog.api.client.v2.model.CustomRuleRevisionAttributesSeverity;
import com.datadog.api.client.v2.model.CustomRuleRevisionDataType;
import com.datadog.api.client.v2.model.CustomRuleRevisionInputAttributes;
import com.datadog.api.client.v2.model.CustomRuleRevisionRequest;
import com.datadog.api.client.v2.model.CustomRuleRevisionRequestData;
import com.datadog.api.client.v2.model.CustomRuleRevisionTest;
import com.datadog.api.client.v2.model.Language;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createCustomRuleRevision", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    CustomRuleRevisionRequest body =
        new CustomRuleRevisionRequest()
            .data(
                new CustomRuleRevisionRequestData()
                    .attributes(
                        new CustomRuleRevisionInputAttributes()
                            .arguments(
                                Collections.singletonList(
                                    new Argument()
                                        .description("YXJndW1lbnQgZGVzY3JpcHRpb24=")
                                        .name("YXJndW1lbnRfbmFtZQ==")))
                            .category(CustomRuleRevisionAttributesCategory.SECURITY)
                            .code("Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==")
                            .creationMessage("Initial revision")
                            .cve("CVE-2024-1234")
                            .cwe("CWE-79")
                            .description("bG9uZyBkZXNjcmlwdGlvbg==")
                            .documentationUrl("https://docs.example.com/rules/my-rule")
                            .isPublished(false)
                            .isTesting(false)
                            .language(Language.PYTHON)
                            .severity(CustomRuleRevisionAttributesSeverity.ERROR)
                            .shortDescription("c2hvcnQgZGVzY3JpcHRpb24=")
                            .shouldUseAiFix(false)
                            .tags(Arrays.asList("security", "custom"))
                            .tests(
                                Collections.singletonList(
                                    new CustomRuleRevisionTest()
                                        .annotationCount(1L)
                                        .code("Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==")
                                        .filename("test.yaml")))
                            .treeSitterQuery("Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="))
                    .type(CustomRuleRevisionDataType.CUSTOM_RULE_REVISION));

    try {
      apiInstance.createCustomRuleRevision("ruleset_name", "rule_name", body);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#createCustomRuleRevision");
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
// Create Custom Rule Revision returns "Successfully created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::Argument;
use datadog_api_client::datadogV2::model::CustomRuleRevisionAttributesCategory;
use datadog_api_client::datadogV2::model::CustomRuleRevisionAttributesSeverity;
use datadog_api_client::datadogV2::model::CustomRuleRevisionDataType;
use datadog_api_client::datadogV2::model::CustomRuleRevisionInputAttributes;
use datadog_api_client::datadogV2::model::CustomRuleRevisionRequest;
use datadog_api_client::datadogV2::model::CustomRuleRevisionRequestData;
use datadog_api_client::datadogV2::model::CustomRuleRevisionTest;
use datadog_api_client::datadogV2::model::Language;

#[tokio::main]
async fn main() {
    let body = CustomRuleRevisionRequest::new().data(
        CustomRuleRevisionRequestData::new()
            .attributes(CustomRuleRevisionInputAttributes::new(
                vec![Argument::new(
                    "YXJndW1lbnQgZGVzY3JpcHRpb24=".to_string(),
                    "YXJndW1lbnRfbmFtZQ==".to_string(),
                )],
                CustomRuleRevisionAttributesCategory::SECURITY,
                "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==".to_string(),
                "Initial revision".to_string(),
                Some("CVE-2024-1234".to_string()),
                Some("CWE-79".to_string()),
                "bG9uZyBkZXNjcmlwdGlvbg==".to_string(),
                Some("https://docs.example.com/rules/my-rule".to_string()),
                false,
                false,
                Language::PYTHON,
                CustomRuleRevisionAttributesSeverity::ERROR,
                "c2hvcnQgZGVzY3JpcHRpb24=".to_string(),
                false,
                vec!["security".to_string(), "custom".to_string()],
                vec![CustomRuleRevisionTest::new(
                    1,
                    "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==".to_string(),
                    "test.yaml".to_string(),
                )],
                "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==".to_string(),
            ))
            .type_(CustomRuleRevisionDataType::CUSTOM_RULE_REVISION),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateCustomRuleRevision", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .create_custom_rule_revision("ruleset_name".to_string(), "rule_name".to_string(), body)
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
 * Create Custom Rule Revision returns "Successfully created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createCustomRuleRevision"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiCreateCustomRuleRevisionRequest = {
  body: {
    data: {
      attributes: {
        arguments: [
          {
            description: "YXJndW1lbnQgZGVzY3JpcHRpb24=",
            name: "YXJndW1lbnRfbmFtZQ==",
          },
        ],
        category: "SECURITY",
        code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
        creationMessage: "Initial revision",
        cve: "CVE-2024-1234",
        cwe: "CWE-79",
        description: "bG9uZyBkZXNjcmlwdGlvbg==",
        documentationUrl: "https://docs.example.com/rules/my-rule",
        isPublished: false,
        isTesting: false,
        language: "PYTHON",
        severity: "ERROR",
        shortDescription: "c2hvcnQgZGVzY3JpcHRpb24=",
        shouldUseAiFix: false,
        tags: ["security", "custom"],
        tests: [
          {
            annotationCount: 1,
            code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
            filename: "test.yaml",
          },
        ],
        treeSitterQuery: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
      },
      type: "custom_rule_revision",
    },
  },
  rulesetName: "ruleset_name",
  ruleName: "rule_name",
};

apiInstance
  .createCustomRuleRevision(params)
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

## List Custom Rule Revisions{% #list-custom-rule-revisions %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions |

### Overview

Get all revisions for a custom rule

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |
| rule_name [*required*]    | string | The rule name    |

#### Query Strings

| Name         | Type    | Description       |
| ------------ | ------- | ----------------- |
| page[offset] | integer | Pagination offset |
| page[limit]  | integer | Pagination limit  |

### Response

{% tab title="200" %}
Successful response
{% tab title="Model" %}

| Parent field | Field                               | Type      | Description                                                                                                        |
| ------------ | ----------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
|              | data                                | [object]  |
| data         | attributes [*required*]        | object    |
| attributes   | arguments [*required*]         | [object]  | Rule arguments                                                                                                     |
| arguments    | description [*required*]       | string    | Base64-encoded argument description                                                                                |
| arguments    | name [*required*]              | string    | Base64-encoded argument name                                                                                       |
| attributes   | category [*required*]          | enum      | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes   | checksum [*required*]          | string    | Code checksum                                                                                                      |
| attributes   | code [*required*]              | string    | Rule code                                                                                                          |
| attributes   | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes   | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes   | creation_message [*required*]  | string    | Revision creation message                                                                                          |
| attributes   | cve [*required*]               | string    | Associated CVE                                                                                                     |
| attributes   | cwe [*required*]               | string    | Associated CWE                                                                                                     |
| attributes   | description [*required*]       | string    | Full description                                                                                                   |
| attributes   | documentation_url [*required*] | string    | Documentation URL                                                                                                  |
| attributes   | is_published [*required*]      | boolean   | Whether the revision is published                                                                                  |
| attributes   | is_testing [*required*]        | boolean   | Whether this is a testing revision                                                                                 |
| attributes   | language [*required*]          | enum      | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes   | severity [*required*]          | enum      | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes   | short_description [*required*] | string    | Short description                                                                                                  |
| attributes   | should_use_ai_fix [*required*] | boolean   | Whether to use AI for fixes                                                                                        |
| attributes   | tags [*required*]              | [string]  | Rule tags                                                                                                          |
| attributes   | tests [*required*]             | [object]  | Rule tests                                                                                                         |
| tests        | annotation_count [*required*]  | int64     | Expected violation count                                                                                           |
| tests        | code [*required*]              | string    | Test code                                                                                                          |
| tests        | filename [*required*]          | string    | Test filename                                                                                                      |
| attributes   | tree_sitter_query [*required*] | string    | Tree-sitter query                                                                                                  |
| data         | id [*required*]                | string    | Revision identifier                                                                                                |
| data         | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule_revision`                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "arguments": [
          {
            "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
            "name": "YXJndW1lbnRfbmFtZQ=="
          }
        ],
        "category": "SECURITY",
        "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
        "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
        "created_at": "2026-01-09T13:00:57.473141Z",
        "created_by": "foobarbaz",
        "creation_message": "Initial revision",
        "cve": "CVE-2024-1234",
        "cwe": "CWE-79",
        "description": "bG9uZyBkZXNjcmlwdGlvbg==",
        "documentation_url": "https://docs.example.com/rules/my-rule",
        "is_published": false,
        "is_testing": false,
        "language": "PYTHON",
        "severity": "ERROR",
        "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
        "should_use_ai_fix": false,
        "tags": [
          "security",
          "custom"
        ],
        "tests": [
          {
            "annotation_count": 1,
            "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
            "filename": "test.yaml"
          }
        ],
        "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
      },
      "id": "revision-123",
      "type": "custom_rule_revision"
    }
  ]
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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
Rule not found
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
                  \# Path parametersexport ruleset_name="CHANGE_ME"export rule_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}/rules/${rule_name}/revisions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Custom Rule Revisions returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["list_custom_rule_revisions"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.list_custom_rule_revisions(
        ruleset_name="ruleset_name",
        rule_name="rule_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Custom Rule Revisions returns "Successful response" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_custom_rule_revisions".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new
p api_instance.list_custom_rule_revisions("ruleset_name", "rule_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List Custom Rule Revisions returns "Successful response" response

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
	configuration.SetUnstableOperationEnabled("v2.ListCustomRuleRevisions", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.ListCustomRuleRevisions(ctx, "ruleset_name", "rule_name", *datadogV2.NewListCustomRuleRevisionsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.ListCustomRuleRevisions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.ListCustomRuleRevisions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List Custom Rule Revisions returns "Successful response" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.CustomRuleRevisionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listCustomRuleRevisions", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    try {
      CustomRuleRevisionsResponse result =
          apiInstance.listCustomRuleRevisions("ruleset_name", "rule_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#listCustomRuleRevisions");
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
// List Custom Rule Revisions returns "Successful response" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::ListCustomRuleRevisionsOptionalParams;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListCustomRuleRevisions", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .list_custom_rule_revisions(
            "ruleset_name".to_string(),
            "rule_name".to_string(),
            ListCustomRuleRevisionsOptionalParams::default(),
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
 * List Custom Rule Revisions returns "Successful response" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listCustomRuleRevisions"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiListCustomRuleRevisionsRequest = {
  rulesetName: "ruleset_name",
  ruleName: "rule_name",
};

apiInstance
  .listCustomRuleRevisions(params)
  .then((data: v2.CustomRuleRevisionsResponse) => {
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

## Delete Custom Rule{% #delete-custom-rule %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |

### Overview

Delete a custom rule

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |
| rule_name [*required*]    | string | The rule name    |

### Response

{% tab title="200" %}
Successfully deleted
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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
Rule not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"export rule_name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}/rules/${rule_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Custom Rule returns "Successfully deleted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["delete_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.delete_custom_rule(
        ruleset_name="ruleset_name",
        rule_name="rule_name",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Custom Rule returns "Successfully deleted" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_custom_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new
p api_instance.delete_custom_rule("ruleset_name", "rule_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete Custom Rule returns "Successfully deleted" response

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
	configuration.SetUnstableOperationEnabled("v2.DeleteCustomRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	r, err := api.DeleteCustomRule(ctx, "ruleset_name", "rule_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.DeleteCustomRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Custom Rule returns "Successfully deleted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteCustomRule", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    try {
      apiInstance.deleteCustomRule("ruleset_name", "rule_name");
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#deleteCustomRule");
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
// Delete Custom Rule returns "Successfully deleted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteCustomRule", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .delete_custom_rule("ruleset_name".to_string(), "rule_name".to_string())
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
 * Delete Custom Rule returns "Successfully deleted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteCustomRule"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiDeleteCustomRuleRequest = {
  rulesetName: "ruleset_name",
  ruleName: "rule_name",
};

apiInstance
  .deleteCustomRule(params)
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

## Show Custom Rule{% #show-custom-rule %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                              |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name} |

### Overview

Get a custom rule by name

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |
| rule_name [*required*]    | string | The rule name    |

### Response

{% tab title="200" %}
Successful response
{% tab title="Model" %}

| Parent field  | Field                               | Type      | Description                                                                                                        |
| ------------- | ----------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
|               | data [*required*]              | object    |
| data          | attributes [*required*]        | object    |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | last_revision [*required*]     | object    | Most recent revision                                                                                               |
| last_revision | attributes [*required*]        | object    |
| attributes    | arguments [*required*]         | [object]  | Rule arguments                                                                                                     |
| arguments     | description [*required*]       | string    | Base64-encoded argument description                                                                                |
| arguments     | name [*required*]              | string    | Base64-encoded argument name                                                                                       |
| attributes    | category [*required*]          | enum      | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes    | checksum [*required*]          | string    | Code checksum                                                                                                      |
| attributes    | code [*required*]              | string    | Rule code                                                                                                          |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | creation_message [*required*]  | string    | Revision creation message                                                                                          |
| attributes    | cve [*required*]               | string    | Associated CVE                                                                                                     |
| attributes    | cwe [*required*]               | string    | Associated CWE                                                                                                     |
| attributes    | description [*required*]       | string    | Full description                                                                                                   |
| attributes    | documentation_url [*required*] | string    | Documentation URL                                                                                                  |
| attributes    | is_published [*required*]      | boolean   | Whether the revision is published                                                                                  |
| attributes    | is_testing [*required*]        | boolean   | Whether this is a testing revision                                                                                 |
| attributes    | language [*required*]          | enum      | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes    | severity [*required*]          | enum      | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes    | short_description [*required*] | string    | Short description                                                                                                  |
| attributes    | should_use_ai_fix [*required*] | boolean   | Whether to use AI for fixes                                                                                        |
| attributes    | tags [*required*]              | [string]  | Rule tags                                                                                                          |
| attributes    | tests [*required*]             | [object]  | Rule tests                                                                                                         |
| tests         | annotation_count [*required*]  | int64     | Expected violation count                                                                                           |
| tests         | code [*required*]              | string    | Test code                                                                                                          |
| tests         | filename [*required*]          | string    | Test filename                                                                                                      |
| attributes    | tree_sitter_query [*required*] | string    | Tree-sitter query                                                                                                  |
| last_revision | id [*required*]                | string    | Revision identifier                                                                                                |
| last_revision | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule_revision`                                                          |
| attributes    | name [*required*]              | string    | Rule name                                                                                                          |
| data          | id [*required*]                | string    | Rule identifier                                                                                                    |
| data          | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule`                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2026-01-09T13:00:57.473141Z",
      "created_by": "foobarbaz",
      "last_revision": {
        "attributes": {
          "arguments": [
            {
              "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
              "name": "YXJndW1lbnRfbmFtZQ=="
            }
          ],
          "category": "SECURITY",
          "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
          "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
          "created_at": "2026-01-09T13:00:57.473141Z",
          "created_by": "foobarbaz",
          "creation_message": "Initial revision",
          "cve": "CVE-2024-1234",
          "cwe": "CWE-79",
          "description": "bG9uZyBkZXNjcmlwdGlvbg==",
          "documentation_url": "https://docs.example.com/rules/my-rule",
          "is_published": false,
          "is_testing": false,
          "language": "PYTHON",
          "severity": "ERROR",
          "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
          "should_use_ai_fix": false,
          "tags": [
            "security",
            "custom"
          ],
          "tests": [
            {
              "annotation_count": 1,
              "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              "filename": "test.yaml"
            }
          ],
          "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
        },
        "id": "revision-123",
        "type": "custom_rule_revision"
      },
      "name": "my-rule"
    },
    "id": "my-rule",
    "type": "custom_rule"
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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
Rule not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"export rule_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}/rules/${rule_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Show Custom Rule returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_custom_rule(
        ruleset_name="ruleset_name",
        rule_name="rule_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Show Custom Rule returns "Successful response" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_custom_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new
p api_instance.get_custom_rule("ruleset_name", "rule_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Show Custom Rule returns "Successful response" response

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
	configuration.SetUnstableOperationEnabled("v2.GetCustomRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.GetCustomRule(ctx, "ruleset_name", "rule_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.GetCustomRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.GetCustomRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Show Custom Rule returns "Successful response" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.CustomRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getCustomRule", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    try {
      CustomRuleResponse result = apiInstance.getCustomRule("ruleset_name", "rule_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#getCustomRule");
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
// Show Custom Rule returns "Successful response" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetCustomRule", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .get_custom_rule("ruleset_name".to_string(), "rule_name".to_string())
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
 * Show Custom Rule returns "Successful response" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getCustomRule"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiGetCustomRuleRequest = {
  rulesetName: "ruleset_name",
  ruleName: "rule_name",
};

apiInstance
  .getCustomRule(params)
  .then((data: v2.CustomRuleResponse) => {
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

## Create Custom Rule{% #create-custom-rule %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules |

### Overview

Create a new custom rule within a ruleset

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field      | Type   | Description                                      |
| ------------ | ---------- | ------ | ------------------------------------------------ |
|              | data       | object |
| data         | attributes | object |
| attributes   | name       | string | Rule name                                        |
| data         | id         | string | Rule identifier                                  |
| data         | type       | enum   | Resource type Allowed enum values: `custom_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "string"
    },
    "id": "string",
    "type": "custom_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Successfully created
{% tab title="Model" %}

| Parent field  | Field                               | Type      | Description                                                                                                        |
| ------------- | ----------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
|               | data [*required*]              | object    |
| data          | attributes [*required*]        | object    |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | last_revision [*required*]     | object    | Most recent revision                                                                                               |
| last_revision | attributes [*required*]        | object    |
| attributes    | arguments [*required*]         | [object]  | Rule arguments                                                                                                     |
| arguments     | description [*required*]       | string    | Base64-encoded argument description                                                                                |
| arguments     | name [*required*]              | string    | Base64-encoded argument name                                                                                       |
| attributes    | category [*required*]          | enum      | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes    | checksum [*required*]          | string    | Code checksum                                                                                                      |
| attributes    | code [*required*]              | string    | Rule code                                                                                                          |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | creation_message [*required*]  | string    | Revision creation message                                                                                          |
| attributes    | cve [*required*]               | string    | Associated CVE                                                                                                     |
| attributes    | cwe [*required*]               | string    | Associated CWE                                                                                                     |
| attributes    | description [*required*]       | string    | Full description                                                                                                   |
| attributes    | documentation_url [*required*] | string    | Documentation URL                                                                                                  |
| attributes    | is_published [*required*]      | boolean   | Whether the revision is published                                                                                  |
| attributes    | is_testing [*required*]        | boolean   | Whether this is a testing revision                                                                                 |
| attributes    | language [*required*]          | enum      | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes    | severity [*required*]          | enum      | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes    | short_description [*required*] | string    | Short description                                                                                                  |
| attributes    | should_use_ai_fix [*required*] | boolean   | Whether to use AI for fixes                                                                                        |
| attributes    | tags [*required*]              | [string]  | Rule tags                                                                                                          |
| attributes    | tests [*required*]             | [object]  | Rule tests                                                                                                         |
| tests         | annotation_count [*required*]  | int64     | Expected violation count                                                                                           |
| tests         | code [*required*]              | string    | Test code                                                                                                          |
| tests         | filename [*required*]          | string    | Test filename                                                                                                      |
| attributes    | tree_sitter_query [*required*] | string    | Tree-sitter query                                                                                                  |
| last_revision | id [*required*]                | string    | Revision identifier                                                                                                |
| last_revision | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule_revision`                                                          |
| attributes    | name [*required*]              | string    | Rule name                                                                                                          |
| data          | id [*required*]                | string    | Rule identifier                                                                                                    |
| data          | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule`                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2026-01-09T13:00:57.473141Z",
      "created_by": "foobarbaz",
      "last_revision": {
        "attributes": {
          "arguments": [
            {
              "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
              "name": "YXJndW1lbnRfbmFtZQ=="
            }
          ],
          "category": "SECURITY",
          "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
          "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
          "created_at": "2026-01-09T13:00:57.473141Z",
          "created_by": "foobarbaz",
          "creation_message": "Initial revision",
          "cve": "CVE-2024-1234",
          "cwe": "CWE-79",
          "description": "bG9uZyBkZXNjcmlwdGlvbg==",
          "documentation_url": "https://docs.example.com/rules/my-rule",
          "is_published": false,
          "is_testing": false,
          "language": "PYTHON",
          "severity": "ERROR",
          "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
          "should_use_ai_fix": false,
          "tags": [
            "security",
            "custom"
          ],
          "tests": [
            {
              "annotation_count": 1,
              "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              "filename": "test.yaml"
            }
          ],
          "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
        },
        "id": "revision-123",
        "type": "custom_rule_revision"
      },
      "name": "my-rule"
    },
    "id": "my-rule",
    "type": "custom_rule"
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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

{% tab title="409" %}
Conflict - rule already exists
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

{% tab title="412" %}
Precondition failed - validation error or ruleset not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}/rules" \
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
Create Custom Rule returns "Successfully created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.custom_rule_data_type import CustomRuleDataType
from datadog_api_client.v2.model.custom_rule_request import CustomRuleRequest
from datadog_api_client.v2.model.custom_rule_request_data import CustomRuleRequestData
from datadog_api_client.v2.model.custom_rule_request_data_attributes import CustomRuleRequestDataAttributes

body = CustomRuleRequest(
    data=CustomRuleRequestData(
        attributes=CustomRuleRequestDataAttributes(),
        type=CustomRuleDataType.CUSTOM_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_custom_rule(ruleset_name="ruleset_name", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create Custom Rule returns "Successfully created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_custom_rule".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::CustomRuleRequest.new({
  data: DatadogAPIClient::V2::CustomRuleRequestData.new({
    attributes: DatadogAPIClient::V2::CustomRuleRequestDataAttributes.new({}),
    type: DatadogAPIClient::V2::CustomRuleDataType::CUSTOM_RULE,
  }),
})
p api_instance.create_custom_rule("ruleset_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Create Custom Rule returns "Successfully created" response

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
	body := datadogV2.CustomRuleRequest{
		Data: &datadogV2.CustomRuleRequestData{
			Attributes: &datadogV2.CustomRuleRequestDataAttributes{},
			Type:       datadogV2.CUSTOMRULEDATATYPE_CUSTOM_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateCustomRule", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.CreateCustomRule(ctx, "ruleset_name", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.CreateCustomRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.CreateCustomRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create Custom Rule returns "Successfully created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.CustomRuleDataType;
import com.datadog.api.client.v2.model.CustomRuleRequest;
import com.datadog.api.client.v2.model.CustomRuleRequestData;
import com.datadog.api.client.v2.model.CustomRuleRequestDataAttributes;
import com.datadog.api.client.v2.model.CustomRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createCustomRule", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    CustomRuleRequest body =
        new CustomRuleRequest()
            .data(
                new CustomRuleRequestData()
                    .attributes(new CustomRuleRequestDataAttributes())
                    .type(CustomRuleDataType.CUSTOM_RULE));

    try {
      CustomRuleResponse result = apiInstance.createCustomRule("ruleset_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#createCustomRule");
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
// Create Custom Rule returns "Successfully created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::CustomRuleDataType;
use datadog_api_client::datadogV2::model::CustomRuleRequest;
use datadog_api_client::datadogV2::model::CustomRuleRequestData;
use datadog_api_client::datadogV2::model::CustomRuleRequestDataAttributes;

#[tokio::main]
async fn main() {
    let body = CustomRuleRequest::new().data(
        CustomRuleRequestData::new()
            .attributes(CustomRuleRequestDataAttributes::new())
            .type_(CustomRuleDataType::CUSTOM_RULE),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateCustomRule", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .create_custom_rule("ruleset_name".to_string(), body)
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
 * Create Custom Rule returns "Successfully created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createCustomRule"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiCreateCustomRuleRequest = {
  body: {
    data: {
      attributes: {},
      type: "custom_rule",
    },
  },
  rulesetName: "ruleset_name",
};

apiInstance
  .createCustomRule(params)
  .then((data: v2.CustomRuleResponse) => {
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

## Delete Custom Ruleset{% #delete-custom-ruleset %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |

### Overview

Delete a custom ruleset

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |

### Response

{% tab title="200" %}
Successfully deleted
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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
Ruleset not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Custom Ruleset returns "Successfully deleted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["delete_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.delete_custom_ruleset(
        ruleset_name="ruleset_name",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Custom Ruleset returns "Successfully deleted" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_custom_ruleset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new
p api_instance.delete_custom_ruleset("ruleset_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete Custom Ruleset returns "Successfully deleted" response

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
	configuration.SetUnstableOperationEnabled("v2.DeleteCustomRuleset", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	r, err := api.DeleteCustomRuleset(ctx, "ruleset_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.DeleteCustomRuleset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Custom Ruleset returns "Successfully deleted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteCustomRuleset", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    try {
      apiInstance.deleteCustomRuleset("ruleset_name");
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#deleteCustomRuleset");
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
// Delete Custom Ruleset returns "Successfully deleted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteCustomRuleset", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api.delete_custom_ruleset("ruleset_name".to_string()).await;
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
 * Delete Custom Ruleset returns "Successfully deleted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteCustomRuleset"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiDeleteCustomRulesetRequest = {
  rulesetName: "ruleset_name",
};

apiInstance
  .deleteCustomRuleset(params)
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

## Update Custom Ruleset{% #update-custom-ruleset %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |

### Overview

Update an existing custom ruleset

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                               | Type      | Description                                                                                                        |
| ------------- | ----------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
|               | data                                | object    |
| data          | attributes                          | object    |
| attributes    | description                         | string    | Base64-encoded full description                                                                                    |
| attributes    | name                                | string    | Ruleset name                                                                                                       |
| attributes    | rules                               | [object]  | Rules in the ruleset                                                                                               |
| rules         | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| rules         | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| rules         | last_revision [*required*]     | object    | Most recent revision                                                                                               |
| last_revision | attributes [*required*]        | object    |
| attributes    | arguments [*required*]         | [object]  | Rule arguments                                                                                                     |
| arguments     | description [*required*]       | string    | Base64-encoded argument description                                                                                |
| arguments     | name [*required*]              | string    | Base64-encoded argument name                                                                                       |
| attributes    | category [*required*]          | enum      | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes    | checksum [*required*]          | string    | Code checksum                                                                                                      |
| attributes    | code [*required*]              | string    | Rule code                                                                                                          |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | creation_message [*required*]  | string    | Revision creation message                                                                                          |
| attributes    | cve [*required*]               | string    | Associated CVE                                                                                                     |
| attributes    | cwe [*required*]               | string    | Associated CWE                                                                                                     |
| attributes    | description [*required*]       | string    | Full description                                                                                                   |
| attributes    | documentation_url [*required*] | string    | Documentation URL                                                                                                  |
| attributes    | is_published [*required*]      | boolean   | Whether the revision is published                                                                                  |
| attributes    | is_testing [*required*]        | boolean   | Whether this is a testing revision                                                                                 |
| attributes    | language [*required*]          | enum      | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes    | severity [*required*]          | enum      | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes    | short_description [*required*] | string    | Short description                                                                                                  |
| attributes    | should_use_ai_fix [*required*] | boolean   | Whether to use AI for fixes                                                                                        |
| attributes    | tags [*required*]              | [string]  | Rule tags                                                                                                          |
| attributes    | tests [*required*]             | [object]  | Rule tests                                                                                                         |
| tests         | annotation_count [*required*]  | int64     | Expected violation count                                                                                           |
| tests         | code [*required*]              | string    | Test code                                                                                                          |
| tests         | filename [*required*]          | string    | Test filename                                                                                                      |
| attributes    | tree_sitter_query [*required*] | string    | Tree-sitter query                                                                                                  |
| last_revision | id [*required*]                | string    | Revision identifier                                                                                                |
| last_revision | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule_revision`                                                          |
| rules         | name [*required*]              | string    | Rule name                                                                                                          |
| attributes    | short_description                   | string    | Base64-encoded short description                                                                                   |
| data          | id                                  | string    | Ruleset identifier                                                                                                 |
| data          | type                                | enum      | Resource type Allowed enum values: `custom_ruleset`                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "string",
      "name": "string",
      "rules": [
        {
          "created_at": "2026-01-09T13:00:57.473141Z",
          "created_by": "foobarbaz",
          "last_revision": {
            "attributes": {
              "arguments": [
                {
                  "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
                  "name": "YXJndW1lbnRfbmFtZQ=="
                }
              ],
              "category": "SECURITY",
              "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
              "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              "created_at": "2026-01-09T13:00:57.473141Z",
              "created_by": "foobarbaz",
              "creation_message": "Initial revision",
              "cve": "CVE-2024-1234",
              "cwe": "CWE-79",
              "description": "bG9uZyBkZXNjcmlwdGlvbg==",
              "documentation_url": "https://docs.example.com/rules/my-rule",
              "is_published": false,
              "is_testing": false,
              "language": "PYTHON",
              "severity": "ERROR",
              "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
              "should_use_ai_fix": false,
              "tags": [
                "security",
                "custom"
              ],
              "tests": [
                {
                  "annotation_count": 1,
                  "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                  "filename": "test.yaml"
                }
              ],
              "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
            },
            "id": "revision-123",
            "type": "custom_rule_revision"
          },
          "name": "my-rule"
        }
      ],
      "short_description": "string"
    },
    "id": "string",
    "type": "custom_ruleset"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Successfully updated
{% tab title="Model" %}

| Parent field  | Field                               | Type      | Description                                                                                                        |
| ------------- | ----------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
|               | data [*required*]              | object    |
| data          | attributes [*required*]        | object    |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | description [*required*]       | string    | Base64-encoded full description                                                                                    |
| attributes    | name [*required*]              | string    | Ruleset name                                                                                                       |
| attributes    | rules [*required*]             | [object]  | Rules in the ruleset                                                                                               |
| rules         | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| rules         | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| rules         | last_revision [*required*]     | object    | Most recent revision                                                                                               |
| last_revision | attributes [*required*]        | object    |
| attributes    | arguments [*required*]         | [object]  | Rule arguments                                                                                                     |
| arguments     | description [*required*]       | string    | Base64-encoded argument description                                                                                |
| arguments     | name [*required*]              | string    | Base64-encoded argument name                                                                                       |
| attributes    | category [*required*]          | enum      | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes    | checksum [*required*]          | string    | Code checksum                                                                                                      |
| attributes    | code [*required*]              | string    | Rule code                                                                                                          |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | creation_message [*required*]  | string    | Revision creation message                                                                                          |
| attributes    | cve [*required*]               | string    | Associated CVE                                                                                                     |
| attributes    | cwe [*required*]               | string    | Associated CWE                                                                                                     |
| attributes    | description [*required*]       | string    | Full description                                                                                                   |
| attributes    | documentation_url [*required*] | string    | Documentation URL                                                                                                  |
| attributes    | is_published [*required*]      | boolean   | Whether the revision is published                                                                                  |
| attributes    | is_testing [*required*]        | boolean   | Whether this is a testing revision                                                                                 |
| attributes    | language [*required*]          | enum      | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes    | severity [*required*]          | enum      | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes    | short_description [*required*] | string    | Short description                                                                                                  |
| attributes    | should_use_ai_fix [*required*] | boolean   | Whether to use AI for fixes                                                                                        |
| attributes    | tags [*required*]              | [string]  | Rule tags                                                                                                          |
| attributes    | tests [*required*]             | [object]  | Rule tests                                                                                                         |
| tests         | annotation_count [*required*]  | int64     | Expected violation count                                                                                           |
| tests         | code [*required*]              | string    | Test code                                                                                                          |
| tests         | filename [*required*]          | string    | Test filename                                                                                                      |
| attributes    | tree_sitter_query [*required*] | string    | Tree-sitter query                                                                                                  |
| last_revision | id [*required*]                | string    | Revision identifier                                                                                                |
| last_revision | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule_revision`                                                          |
| rules         | name [*required*]              | string    | Rule name                                                                                                          |
| attributes    | short_description [*required*] | string    | Base64-encoded short description                                                                                   |
| data          | id [*required*]                | string    | Ruleset identifier                                                                                                 |
| data          | type [*required*]              | enum      | Resource type Allowed enum values: `custom_ruleset`                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2026-01-09T13:00:57.473141Z",
      "created_by": "foobarbaz",
      "description": "bG9uZyBkZXNjcmlwdGlvbg==",
      "name": "my-ruleset",
      "rules": [
        {
          "created_at": "2026-01-09T13:00:57.473141Z",
          "created_by": "foobarbaz",
          "last_revision": {
            "attributes": {
              "arguments": [
                {
                  "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
                  "name": "YXJndW1lbnRfbmFtZQ=="
                }
              ],
              "category": "SECURITY",
              "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
              "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              "created_at": "2026-01-09T13:00:57.473141Z",
              "created_by": "foobarbaz",
              "creation_message": "Initial revision",
              "cve": "CVE-2024-1234",
              "cwe": "CWE-79",
              "description": "bG9uZyBkZXNjcmlwdGlvbg==",
              "documentation_url": "https://docs.example.com/rules/my-rule",
              "is_published": false,
              "is_testing": false,
              "language": "PYTHON",
              "severity": "ERROR",
              "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
              "should_use_ai_fix": false,
              "tags": [
                "security",
                "custom"
              ],
              "tests": [
                {
                  "annotation_count": 1,
                  "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                  "filename": "test.yaml"
                }
              ],
              "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
            },
            "id": "revision-123",
            "type": "custom_rule_revision"
          },
          "name": "my-rule"
        }
      ],
      "short_description": "c2hvcnQgZGVzY3JpcHRpb24="
    },
    "id": "my-ruleset",
    "type": "custom_ruleset"
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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

{% tab title="412" %}
Precondition failed - validation error or ruleset not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "rules": [
        {
          "created_at": "2026-01-09T13:00:57.473141Z",
          "created_by": "foobarbaz",
          "last_revision": {
            "attributes": {
              "arguments": [
                {
                  "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
                  "name": "YXJndW1lbnRfbmFtZQ=="
                }
              ],
              "category": "SECURITY",
              "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
              "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              "created_at": "2026-01-09T13:00:57.473141Z",
              "created_by": "foobarbaz",
              "creation_message": "Initial revision",
              "cve": "CVE-2024-1234",
              "cwe": "CWE-79",
              "description": "bG9uZyBkZXNjcmlwdGlvbg==",
              "documentation_url": "https://docs.example.com/rules/my-rule",
              "is_published": false,
              "is_testing": false,
              "language": "PYTHON",
              "severity": "ERROR",
              "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
              "should_use_ai_fix": false,
              "tags": [
                "security",
                "custom"
              ],
              "tests": [
                {
                  "annotation_count": 1,
                  "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                  "filename": "test.yaml"
                }
              ],
              "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
            },
            "id": "revision-123",
            "type": "custom_rule_revision"
          },
          "name": "my-rule"
        }
      ]
    }
  }
}
EOF
                
##### 

```python
"""
Update Custom Ruleset returns "Successfully updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.argument import Argument
from datadog_api_client.v2.model.custom_rule import CustomRule
from datadog_api_client.v2.model.custom_rule_revision import CustomRuleRevision
from datadog_api_client.v2.model.custom_rule_revision_attributes import CustomRuleRevisionAttributes
from datadog_api_client.v2.model.custom_rule_revision_attributes_category import CustomRuleRevisionAttributesCategory
from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import CustomRuleRevisionAttributesSeverity
from datadog_api_client.v2.model.custom_rule_revision_data_type import CustomRuleRevisionDataType
from datadog_api_client.v2.model.custom_rule_revision_test import CustomRuleRevisionTest
from datadog_api_client.v2.model.custom_ruleset_data_type import CustomRulesetDataType
from datadog_api_client.v2.model.custom_ruleset_request import CustomRulesetRequest
from datadog_api_client.v2.model.custom_ruleset_request_data import CustomRulesetRequestData
from datadog_api_client.v2.model.custom_ruleset_request_data_attributes import CustomRulesetRequestDataAttributes
from datadog_api_client.v2.model.language import Language
from datetime import datetime
from dateutil.tz import tzutc

body = CustomRulesetRequest(
    data=CustomRulesetRequestData(
        attributes=CustomRulesetRequestDataAttributes(
            rules=[
                CustomRule(
                    created_at=datetime(2026, 1, 9, 13, 0, 57, 473141, tzinfo=tzutc()),
                    created_by="foobarbaz",
                    last_revision=CustomRuleRevision(
                        attributes=CustomRuleRevisionAttributes(
                            arguments=[
                                Argument(
                                    description="YXJndW1lbnQgZGVzY3JpcHRpb24=",
                                    name="YXJndW1lbnRfbmFtZQ==",
                                ),
                            ],
                            category=CustomRuleRevisionAttributesCategory.SECURITY,
                            checksum="8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
                            code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                            created_at=datetime(2026, 1, 9, 13, 0, 57, 473141, tzinfo=tzutc()),
                            created_by="foobarbaz",
                            creation_message="Initial revision",
                            cve="CVE-2024-1234",
                            cwe="CWE-79",
                            description="bG9uZyBkZXNjcmlwdGlvbg==",
                            documentation_url="https://docs.example.com/rules/my-rule",
                            is_published=False,
                            is_testing=False,
                            language=Language.PYTHON,
                            severity=CustomRuleRevisionAttributesSeverity.ERROR,
                            short_description="c2hvcnQgZGVzY3JpcHRpb24=",
                            should_use_ai_fix=False,
                            tags=[
                                "security",
                                "custom",
                            ],
                            tests=[
                                CustomRuleRevisionTest(
                                    annotation_count=1,
                                    code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                                    filename="test.yaml",
                                ),
                            ],
                            tree_sitter_query="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                        ),
                        id="revision-123",
                        type=CustomRuleRevisionDataType.CUSTOM_RULE_REVISION,
                    ),
                    name="my-rule",
                ),
            ],
        ),
        type=CustomRulesetDataType.CUSTOM_RULESET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.update_custom_ruleset(ruleset_name="ruleset_name", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update Custom Ruleset returns "Successfully updated" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_custom_ruleset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new

body = DatadogAPIClient::V2::CustomRulesetRequest.new({
  data: DatadogAPIClient::V2::CustomRulesetRequestData.new({
    attributes: DatadogAPIClient::V2::CustomRulesetRequestDataAttributes.new({
      rules: [
        DatadogAPIClient::V2::CustomRule.new({
          created_at: "2026-01-09T13:00:57.473141Z",
          created_by: "foobarbaz",
          last_revision: DatadogAPIClient::V2::CustomRuleRevision.new({
            attributes: DatadogAPIClient::V2::CustomRuleRevisionAttributes.new({
              arguments: [
                DatadogAPIClient::V2::Argument.new({
                  description: "YXJndW1lbnQgZGVzY3JpcHRpb24=",
                  name: "YXJndW1lbnRfbmFtZQ==",
                }),
              ],
              category: DatadogAPIClient::V2::CustomRuleRevisionAttributesCategory::SECURITY,
              checksum: "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
              code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              created_at: "2026-01-09T13:00:57.473141Z",
              created_by: "foobarbaz",
              creation_message: "Initial revision",
              cve: "CVE-2024-1234",
              cwe: "CWE-79",
              description: "bG9uZyBkZXNjcmlwdGlvbg==",
              documentation_url: "https://docs.example.com/rules/my-rule",
              is_published: false,
              is_testing: false,
              language: DatadogAPIClient::V2::Language::PYTHON,
              severity: DatadogAPIClient::V2::CustomRuleRevisionAttributesSeverity::ERROR,
              short_description: "c2hvcnQgZGVzY3JpcHRpb24=",
              should_use_ai_fix: false,
              tags: [
                "security",
                "custom",
              ],
              tests: [
                DatadogAPIClient::V2::CustomRuleRevisionTest.new({
                  annotation_count: 1,
                  code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                  filename: "test.yaml",
                }),
              ],
              tree_sitter_query: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
            }),
            id: "revision-123",
            type: DatadogAPIClient::V2::CustomRuleRevisionDataType::CUSTOM_RULE_REVISION,
          }),
          name: "my-rule",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::CustomRulesetDataType::CUSTOM_RULESET,
  }),
})
p api_instance.update_custom_ruleset("ruleset_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Update Custom Ruleset returns "Successfully updated" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CustomRulesetRequest{
		Data: &datadogV2.CustomRulesetRequestData{
			Attributes: &datadogV2.CustomRulesetRequestDataAttributes{
				Rules: []datadogV2.CustomRule{
					{
						CreatedAt: time.Date(2026, 1, 9, 13, 0, 57, 473141, time.UTC),
						CreatedBy: "foobarbaz",
						LastRevision: datadogV2.CustomRuleRevision{
							Attributes: datadogV2.CustomRuleRevisionAttributes{
								Arguments: []datadogV2.Argument{
									{
										Description: "YXJndW1lbnQgZGVzY3JpcHRpb24=",
										Name:        "YXJndW1lbnRfbmFtZQ==",
									},
								},
								Category:         datadogV2.CUSTOMRULEREVISIONATTRIBUTESCATEGORY_SECURITY,
								Checksum:         "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
								Code:             "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
								CreatedAt:        time.Date(2026, 1, 9, 13, 0, 57, 473141, time.UTC),
								CreatedBy:        "foobarbaz",
								CreationMessage:  "Initial revision",
								Cve:              *datadog.NewNullableString(datadog.PtrString("CVE-2024-1234")),
								Cwe:              *datadog.NewNullableString(datadog.PtrString("CWE-79")),
								Description:      "bG9uZyBkZXNjcmlwdGlvbg==",
								DocumentationUrl: *datadog.NewNullableString(datadog.PtrString("https://docs.example.com/rules/my-rule")),
								IsPublished:      false,
								IsTesting:        false,
								Language:         datadogV2.LANGUAGE_PYTHON,
								Severity:         datadogV2.CUSTOMRULEREVISIONATTRIBUTESSEVERITY_ERROR,
								ShortDescription: "c2hvcnQgZGVzY3JpcHRpb24=",
								ShouldUseAiFix:   false,
								Tags: []string{
									"security",
									"custom",
								},
								Tests: []datadogV2.CustomRuleRevisionTest{
									{
										AnnotationCount: 1,
										Code:            "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
										Filename:        "test.yaml",
									},
								},
								TreeSitterQuery: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
							},
							Id:   "revision-123",
							Type: datadogV2.CUSTOMRULEREVISIONDATATYPE_CUSTOM_RULE_REVISION,
						},
						Name: "my-rule",
					},
				},
			},
			Type: datadogV2.CUSTOMRULESETDATATYPE_CUSTOM_RULESET.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateCustomRuleset", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.UpdateCustomRuleset(ctx, "ruleset_name", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.UpdateCustomRuleset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.UpdateCustomRuleset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update Custom Ruleset returns "Successfully updated" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.Argument;
import com.datadog.api.client.v2.model.CustomRule;
import com.datadog.api.client.v2.model.CustomRuleRevision;
import com.datadog.api.client.v2.model.CustomRuleRevisionAttributes;
import com.datadog.api.client.v2.model.CustomRuleRevisionAttributesCategory;
import com.datadog.api.client.v2.model.CustomRuleRevisionAttributesSeverity;
import com.datadog.api.client.v2.model.CustomRuleRevisionDataType;
import com.datadog.api.client.v2.model.CustomRuleRevisionTest;
import com.datadog.api.client.v2.model.CustomRulesetDataType;
import com.datadog.api.client.v2.model.CustomRulesetRequest;
import com.datadog.api.client.v2.model.CustomRulesetRequestData;
import com.datadog.api.client.v2.model.CustomRulesetRequestDataAttributes;
import com.datadog.api.client.v2.model.CustomRulesetResponse;
import com.datadog.api.client.v2.model.Language;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateCustomRuleset", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    CustomRulesetRequest body =
        new CustomRulesetRequest()
            .data(
                new CustomRulesetRequestData()
                    .attributes(
                        new CustomRulesetRequestDataAttributes()
                            .rules(
                                Collections.singletonList(
                                    new CustomRule()
                                        .createdAt(
                                            OffsetDateTime.parse("2026-01-09T13:00:57.473141Z"))
                                        .createdBy("foobarbaz")
                                        .lastRevision(
                                            new CustomRuleRevision()
                                                .attributes(
                                                    new CustomRuleRevisionAttributes()
                                                        .arguments(
                                                            Collections.singletonList(
                                                                new Argument()
                                                                    .description(
                                                                        "YXJndW1lbnQgZGVzY3JpcHRpb24=")
                                                                    .name("YXJndW1lbnRfbmFtZQ==")))
                                                        .category(
                                                            CustomRuleRevisionAttributesCategory
                                                                .SECURITY)
                                                        .checksum(
                                                            "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99")
                                                        .code(
                                                            "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==")
                                                        .createdAt(
                                                            OffsetDateTime.parse(
                                                                "2026-01-09T13:00:57.473141Z"))
                                                        .createdBy("foobarbaz")
                                                        .creationMessage("Initial revision")
                                                        .cve("CVE-2024-1234")
                                                        .cwe("CWE-79")
                                                        .description("bG9uZyBkZXNjcmlwdGlvbg==")
                                                        .documentationUrl(
                                                            "https://docs.example.com/rules/my-rule")
                                                        .isPublished(false)
                                                        .isTesting(false)
                                                        .language(Language.PYTHON)
                                                        .severity(
                                                            CustomRuleRevisionAttributesSeverity
                                                                .ERROR)
                                                        .shortDescription(
                                                            "c2hvcnQgZGVzY3JpcHRpb24=")
                                                        .shouldUseAiFix(false)
                                                        .tags(Arrays.asList("security", "custom"))
                                                        .tests(
                                                            Collections.singletonList(
                                                                new CustomRuleRevisionTest()
                                                                    .annotationCount(1L)
                                                                    .code(
                                                                        "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==")
                                                                    .filename("test.yaml")))
                                                        .treeSitterQuery(
                                                            "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="))
                                                .id("revision-123")
                                                .type(
                                                    CustomRuleRevisionDataType
                                                        .CUSTOM_RULE_REVISION))
                                        .name("my-rule"))))
                    .type(CustomRulesetDataType.CUSTOM_RULESET));

    try {
      CustomRulesetResponse result = apiInstance.updateCustomRuleset("ruleset_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#updateCustomRuleset");
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
// Update Custom Ruleset returns "Successfully updated" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;
use datadog_api_client::datadogV2::model::Argument;
use datadog_api_client::datadogV2::model::CustomRule;
use datadog_api_client::datadogV2::model::CustomRuleRevision;
use datadog_api_client::datadogV2::model::CustomRuleRevisionAttributes;
use datadog_api_client::datadogV2::model::CustomRuleRevisionAttributesCategory;
use datadog_api_client::datadogV2::model::CustomRuleRevisionAttributesSeverity;
use datadog_api_client::datadogV2::model::CustomRuleRevisionDataType;
use datadog_api_client::datadogV2::model::CustomRuleRevisionTest;
use datadog_api_client::datadogV2::model::CustomRulesetDataType;
use datadog_api_client::datadogV2::model::CustomRulesetRequest;
use datadog_api_client::datadogV2::model::CustomRulesetRequestData;
use datadog_api_client::datadogV2::model::CustomRulesetRequestDataAttributes;
use datadog_api_client::datadogV2::model::Language;

#[tokio::main]
async fn main() {
    let body = CustomRulesetRequest::new().data(
        CustomRulesetRequestData::new()
            .attributes(CustomRulesetRequestDataAttributes::new().rules(Some(
                vec![CustomRule::new(
                    DateTime::parse_from_rfc3339("2026-01-09T13:00:57.473141+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                    "foobarbaz".to_string(),
                    CustomRuleRevision::new(
                        CustomRuleRevisionAttributes::new(
                            vec![Argument::new(
                                "YXJndW1lbnQgZGVzY3JpcHRpb24=".to_string(),
                                "YXJndW1lbnRfbmFtZQ==".to_string(),
                            )],
                            CustomRuleRevisionAttributesCategory::SECURITY,
                            "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99"
                                .to_string(),
                            "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==".to_string(),
                            DateTime::parse_from_rfc3339("2026-01-09T13:00:57.473141+00:00")
                                .expect("Failed to parse datetime")
                                .with_timezone(&Utc),
                            "foobarbaz".to_string(),
                            "Initial revision".to_string(),
                            Some("CVE-2024-1234".to_string()),
                            Some("CWE-79".to_string()),
                            "bG9uZyBkZXNjcmlwdGlvbg==".to_string(),
                            Some("https://docs.example.com/rules/my-rule".to_string()),
                            false,
                            false,
                            Language::PYTHON,
                            CustomRuleRevisionAttributesSeverity::ERROR,
                            "c2hvcnQgZGVzY3JpcHRpb24=".to_string(),
                            false,
                            vec!["security".to_string(), "custom".to_string()],
                            vec![CustomRuleRevisionTest::new(
                                1,
                                "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==".to_string(),
                                "test.yaml".to_string(),
                            )],
                            "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==".to_string(),
                        ),
                        "revision-123".to_string(),
                        CustomRuleRevisionDataType::CUSTOM_RULE_REVISION,
                    ),
                    "my-rule".to_string(),
                )],
            )))
            .type_(CustomRulesetDataType::CUSTOM_RULESET),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateCustomRuleset", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api
        .update_custom_ruleset("ruleset_name".to_string(), body)
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
 * Update Custom Ruleset returns "Successfully updated" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateCustomRuleset"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiUpdateCustomRulesetRequest = {
  body: {
    data: {
      attributes: {
        rules: [
          {
            createdAt: new Date(2026, 1, 9, 13, 0, 57, 473141),
            createdBy: "foobarbaz",
            lastRevision: {
              attributes: {
                arguments: [
                  {
                    description: "YXJndW1lbnQgZGVzY3JpcHRpb24=",
                    name: "YXJndW1lbnRfbmFtZQ==",
                  },
                ],
                category: "SECURITY",
                checksum:
                  "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
                code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                createdAt: new Date(2026, 1, 9, 13, 0, 57, 473141),
                createdBy: "foobarbaz",
                creationMessage: "Initial revision",
                cve: "CVE-2024-1234",
                cwe: "CWE-79",
                description: "bG9uZyBkZXNjcmlwdGlvbg==",
                documentationUrl: "https://docs.example.com/rules/my-rule",
                isPublished: false,
                isTesting: false,
                language: "PYTHON",
                severity: "ERROR",
                shortDescription: "c2hvcnQgZGVzY3JpcHRpb24=",
                shouldUseAiFix: false,
                tags: ["security", "custom"],
                tests: [
                  {
                    annotationCount: 1,
                    code: "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                    filename: "test.yaml",
                  },
                ],
                treeSitterQuery:
                  "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              },
              id: "revision-123",
              type: "custom_rule_revision",
            },
            name: "my-rule",
          },
        ],
      },
      type: "custom_ruleset",
    },
  },
  rulesetName: "ruleset_name",
};

apiInstance
  .updateCustomRuleset(params)
  .then((data: v2.CustomRulesetResponse) => {
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

## Show Custom Ruleset{% #show-custom-ruleset %}

{% tab title="v2" %}
This endpoint is in Preview and may introduce breaking changes. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/static-analysis/custom/rulesets/{ruleset_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/{ruleset_name} |

### Overview

Get a custom ruleset by name

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| ruleset_name [*required*] | string | The ruleset name |

### Response

{% tab title="200" %}
Successful response
{% tab title="Model" %}

| Parent field  | Field                               | Type      | Description                                                                                                        |
| ------------- | ----------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
|               | data [*required*]              | object    |
| data          | attributes [*required*]        | object    |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | description [*required*]       | string    | Base64-encoded full description                                                                                    |
| attributes    | name [*required*]              | string    | Ruleset name                                                                                                       |
| attributes    | rules [*required*]             | [object]  | Rules in the ruleset                                                                                               |
| rules         | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| rules         | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| rules         | last_revision [*required*]     | object    | Most recent revision                                                                                               |
| last_revision | attributes [*required*]        | object    |
| attributes    | arguments [*required*]         | [object]  | Rule arguments                                                                                                     |
| arguments     | description [*required*]       | string    | Base64-encoded argument description                                                                                |
| arguments     | name [*required*]              | string    | Base64-encoded argument name                                                                                       |
| attributes    | category [*required*]          | enum      | Rule category Allowed enum values: `SECURITY,BEST_PRACTICES,CODE_STYLE,ERROR_PRONE,PERFORMANCE`                    |
| attributes    | checksum [*required*]          | string    | Code checksum                                                                                                      |
| attributes    | code [*required*]              | string    | Rule code                                                                                                          |
| attributes    | created_at [*required*]        | date-time | Creation timestamp                                                                                                 |
| attributes    | created_by [*required*]        | string    | Creator identifier                                                                                                 |
| attributes    | creation_message [*required*]  | string    | Revision creation message                                                                                          |
| attributes    | cve [*required*]               | string    | Associated CVE                                                                                                     |
| attributes    | cwe [*required*]               | string    | Associated CWE                                                                                                     |
| attributes    | description [*required*]       | string    | Full description                                                                                                   |
| attributes    | documentation_url [*required*] | string    | Documentation URL                                                                                                  |
| attributes    | is_published [*required*]      | boolean   | Whether the revision is published                                                                                  |
| attributes    | is_testing [*required*]        | boolean   | Whether this is a testing revision                                                                                 |
| attributes    | language [*required*]          | enum      | Programming language Allowed enum values: `PYTHON,JAVASCRIPT,TYPESCRIPT,JAVA,GO,YAML,RUBY,CSHARP,PHP,KOTLIN,SWIFT` |
| attributes    | severity [*required*]          | enum      | Rule severity Allowed enum values: `ERROR,WARNING,NOTICE`                                                          |
| attributes    | short_description [*required*] | string    | Short description                                                                                                  |
| attributes    | should_use_ai_fix [*required*] | boolean   | Whether to use AI for fixes                                                                                        |
| attributes    | tags [*required*]              | [string]  | Rule tags                                                                                                          |
| attributes    | tests [*required*]             | [object]  | Rule tests                                                                                                         |
| tests         | annotation_count [*required*]  | int64     | Expected violation count                                                                                           |
| tests         | code [*required*]              | string    | Test code                                                                                                          |
| tests         | filename [*required*]          | string    | Test filename                                                                                                      |
| attributes    | tree_sitter_query [*required*] | string    | Tree-sitter query                                                                                                  |
| last_revision | id [*required*]                | string    | Revision identifier                                                                                                |
| last_revision | type [*required*]              | enum      | Resource type Allowed enum values: `custom_rule_revision`                                                          |
| rules         | name [*required*]              | string    | Rule name                                                                                                          |
| attributes    | short_description [*required*] | string    | Base64-encoded short description                                                                                   |
| data          | id [*required*]                | string    | Ruleset identifier                                                                                                 |
| data          | type [*required*]              | enum      | Resource type Allowed enum values: `custom_ruleset`                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2026-01-09T13:00:57.473141Z",
      "created_by": "foobarbaz",
      "description": "bG9uZyBkZXNjcmlwdGlvbg==",
      "name": "my-ruleset",
      "rules": [
        {
          "created_at": "2026-01-09T13:00:57.473141Z",
          "created_by": "foobarbaz",
          "last_revision": {
            "attributes": {
              "arguments": [
                {
                  "description": "YXJndW1lbnQgZGVzY3JpcHRpb24=",
                  "name": "YXJndW1lbnRfbmFtZQ=="
                }
              ],
              "category": "SECURITY",
              "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
              "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
              "created_at": "2026-01-09T13:00:57.473141Z",
              "created_by": "foobarbaz",
              "creation_message": "Initial revision",
              "cve": "CVE-2024-1234",
              "cwe": "CWE-79",
              "description": "bG9uZyBkZXNjcmlwdGlvbg==",
              "documentation_url": "https://docs.example.com/rules/my-rule",
              "is_published": false,
              "is_testing": false,
              "language": "PYTHON",
              "severity": "ERROR",
              "short_description": "c2hvcnQgZGVzY3JpcHRpb24=",
              "should_use_ai_fix": false,
              "tags": [
                "security",
                "custom"
              ],
              "tests": [
                {
                  "annotation_count": 1,
                  "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                  "filename": "test.yaml"
                }
              ],
              "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="
            },
            "id": "revision-123",
            "type": "custom_rule_revision"
          },
          "name": "my-rule"
        }
      ],
      "short_description": "c2hvcnQgZGVzY3JpcHRpb24="
    },
    "id": "my-ruleset",
    "type": "custom_ruleset"
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

{% tab title="401" %}
Unauthorized - custom rules not enabled
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
Ruleset not found
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

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

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
                  \# Path parametersexport ruleset_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/static-analysis/custom/rulesets/${ruleset_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Show Custom Ruleset returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_custom_ruleset(
        ruleset_name="ruleset_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Show Custom Ruleset returns "Successful response" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_custom_ruleset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::StaticAnalysisAPI.new
p api_instance.get_custom_ruleset("ruleset_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Show Custom Ruleset returns "Successful response" response

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
	configuration.SetUnstableOperationEnabled("v2.GetCustomRuleset", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewStaticAnalysisApi(apiClient)
	resp, r, err := api.GetCustomRuleset(ctx, "ruleset_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StaticAnalysisApi.GetCustomRuleset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `StaticAnalysisApi.GetCustomRuleset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Show Custom Ruleset returns "Successful response" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StaticAnalysisApi;
import com.datadog.api.client.v2.model.CustomRulesetResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getCustomRuleset", true);
    StaticAnalysisApi apiInstance = new StaticAnalysisApi(defaultClient);

    try {
      CustomRulesetResponse result = apiInstance.getCustomRuleset("ruleset_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticAnalysisApi#getCustomRuleset");
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
// Show Custom Ruleset returns "Successful response" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_static_analysis::StaticAnalysisAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetCustomRuleset", true);
    let api = StaticAnalysisAPI::with_config(configuration);
    let resp = api.get_custom_ruleset("ruleset_name".to_string()).await;
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
 * Show Custom Ruleset returns "Successful response" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getCustomRuleset"] = true;
const apiInstance = new v2.StaticAnalysisApi(configuration);

const params: v2.StaticAnalysisApiGetCustomRulesetRequest = {
  rulesetName: "ruleset_name",
};

apiInstance
  .getCustomRuleset(params)
  .then((data: v2.CustomRulesetResponse) => {
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
