# Source: https://docs.datadoghq.com/api/latest/code-coverage.md

---
title: Code Coverage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Code Coverage
---

# Code Coverage

Retrieve and analyze code coverage data from Code Coverage. See the [Code Coverage page](https://docs.datadoghq.com/code_coverage/) for more information.

## Get code coverage summary for a branch{% #get-code-coverage-summary-for-a-branch %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/code-coverage/branch/summary |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/code-coverage/branch/summary |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/code-coverage/branch/summary      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/code-coverage/branch/summary      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/code-coverage/branch/summary     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/code-coverage/branch/summary |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/code-coverage/branch/summary |

### Overview

Retrieve aggregated code coverage statistics for a specific branch in a repository. This endpoint provides overall coverage metrics as well as breakdowns by service and code owner. This endpoint requires the `code_coverage_read` permission.

OAuth apps require the `code_coverage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#code-coverage) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                           | Type   | Description                                                                                                                                                                         |
| ------------ | ------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]          | object | Data object for branch summary request.                                                                                                                                             |
| data         | attributes [*required*]    | object | Attributes for requesting code coverage summary for a branch.                                                                                                                       |
| attributes   | branch [*required*]        | string | The branch name.                                                                                                                                                                    |
| attributes   | repository_id [*required*] | string | The repository identifier.                                                                                                                                                          |
| data         | type [*required*]          | enum   | JSON:API type for branch coverage summary request. The value must always be `ci_app_coverage_branch_summary_request`. Allowed enum values: `ci_app_coverage_branch_summary_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "branch": "prod",
      "repository_id": "github.com/datadog/shopist"
    },
    "type": "ci_app_coverage_branch_summary_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing code coverage summary.

| Parent field         | Field                   | Type   | Description                                                                                                                                     |
| -------------------- | ----------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                    | object | Data object for coverage summary response.                                                                                                      |
| data                 | attributes              | object | Attributes object for code coverage summary response.                                                                                           |
| attributes           | codeowners              | object | Coverage statistics broken down by code owner.                                                                                                  |
| additionalProperties | <any-key>               | object | Coverage statistics for a specific code owner.                                                                                                  |
| <any-key>            | evaluated_flags_count   | int64  | Number of coverage flags evaluated for the code owner.                                                                                          |
| <any-key>            | evaluated_reports_count | int64  | Number of coverage reports evaluated for the code owner.                                                                                        |
| <any-key>            | patch_coverage          | double | Patch coverage percentage for the code owner.                                                                                                   |
| <any-key>            | total_coverage          | double | Total coverage percentage for the code owner.                                                                                                   |
| attributes           | evaluated_flags_count   | int64  | Total number of coverage flags evaluated.                                                                                                       |
| attributes           | evaluated_reports_count | int64  | Total number of coverage reports evaluated.                                                                                                     |
| attributes           | patch_coverage          | double | Overall patch coverage percentage.                                                                                                              |
| attributes           | services                | object | Coverage statistics broken down by service.                                                                                                     |
| additionalProperties | <any-key>               | object | Coverage statistics for a specific service.                                                                                                     |
| <any-key>            | evaluated_flags_count   | int64  | Number of coverage flags evaluated for the service.                                                                                             |
| <any-key>            | evaluated_reports_count | int64  | Number of coverage reports evaluated for the service.                                                                                           |
| <any-key>            | patch_coverage          | double | Patch coverage percentage for the service.                                                                                                      |
| <any-key>            | total_coverage          | double | Total coverage percentage for the service.                                                                                                      |
| attributes           | total_coverage          | double | Overall total coverage percentage.                                                                                                              |
| data                 | id                      | string | Unique identifier for the coverage summary (base64-hashed).                                                                                     |
| data                 | type                    | enum   | JSON:API type for coverage summary response. The value must always be `ci_app_coverage_summary`. Allowed enum values: `ci_app_coverage_summary` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "codeowners": {
        "<any-key>": {
          "evaluated_flags_count": 2,
          "evaluated_reports_count": 4,
          "patch_coverage": 75.2,
          "total_coverage": 88.7
        }
      },
      "evaluated_flags_count": 8,
      "evaluated_reports_count": 12,
      "patch_coverage": 70.1,
      "services": {
        "<any-key>": {
          "evaluated_flags_count": 3,
          "evaluated_reports_count": 5,
          "patch_coverage": 72.3,
          "total_coverage": 85.5
        }
      },
      "total_coverage": 82.4
    },
    "id": "ZGQxMjM0NV9tYWluXzE3MDk1NjQwMDA=",
    "type": "ci_app_coverage_summary"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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

{% tab title="500" %}
Internal server error
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/code-coverage/branch/summary" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "branch": "prod",
      "repository_id": "github.com/datadog/shopist"
    },
    "type": "ci_app_coverage_branch_summary_request"
  }
}
EOF
                
##### 

```python
"""
Get code coverage summary for a branch returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.code_coverage_api import CodeCoverageApi
from datadog_api_client.v2.model.branch_coverage_summary_request import BranchCoverageSummaryRequest
from datadog_api_client.v2.model.branch_coverage_summary_request_attributes import (
    BranchCoverageSummaryRequestAttributes,
)
from datadog_api_client.v2.model.branch_coverage_summary_request_data import BranchCoverageSummaryRequestData
from datadog_api_client.v2.model.branch_coverage_summary_request_type import BranchCoverageSummaryRequestType

body = BranchCoverageSummaryRequest(
    data=BranchCoverageSummaryRequestData(
        attributes=BranchCoverageSummaryRequestAttributes(
            branch="prod",
            repository_id="github.com/datadog/shopist",
        ),
        type=BranchCoverageSummaryRequestType.CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_code_coverage_branch_summary"] = True
with ApiClient(configuration) as api_client:
    api_instance = CodeCoverageApi(api_client)
    response = api_instance.get_code_coverage_branch_summary(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get code coverage summary for a branch returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_code_coverage_branch_summary".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CodeCoverageAPI.new

body = DatadogAPIClient::V2::BranchCoverageSummaryRequest.new({
  data: DatadogAPIClient::V2::BranchCoverageSummaryRequestData.new({
    attributes: DatadogAPIClient::V2::BranchCoverageSummaryRequestAttributes.new({
      branch: "prod",
      repository_id: "github.com/datadog/shopist",
    }),
    type: DatadogAPIClient::V2::BranchCoverageSummaryRequestType::CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST,
  }),
})
p api_instance.get_code_coverage_branch_summary(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get code coverage summary for a branch returns "OK" response

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
	body := datadogV2.BranchCoverageSummaryRequest{
		Data: datadogV2.BranchCoverageSummaryRequestData{
			Attributes: datadogV2.BranchCoverageSummaryRequestAttributes{
				Branch:       "prod",
				RepositoryId: "github.com/datadog/shopist",
			},
			Type: datadogV2.BRANCHCOVERAGESUMMARYREQUESTTYPE_CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetCodeCoverageBranchSummary", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCodeCoverageApi(apiClient)
	resp, r, err := api.GetCodeCoverageBranchSummary(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CodeCoverageApi.GetCodeCoverageBranchSummary`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CodeCoverageApi.GetCodeCoverageBranchSummary`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get code coverage summary for a branch returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CodeCoverageApi;
import com.datadog.api.client.v2.model.BranchCoverageSummaryRequest;
import com.datadog.api.client.v2.model.BranchCoverageSummaryRequestAttributes;
import com.datadog.api.client.v2.model.BranchCoverageSummaryRequestData;
import com.datadog.api.client.v2.model.BranchCoverageSummaryRequestType;
import com.datadog.api.client.v2.model.CoverageSummaryResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getCodeCoverageBranchSummary", true);
    CodeCoverageApi apiInstance = new CodeCoverageApi(defaultClient);

    BranchCoverageSummaryRequest body =
        new BranchCoverageSummaryRequest()
            .data(
                new BranchCoverageSummaryRequestData()
                    .attributes(
                        new BranchCoverageSummaryRequestAttributes()
                            .branch("prod")
                            .repositoryId("github.com/datadog/shopist"))
                    .type(BranchCoverageSummaryRequestType.CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST));

    try {
      CoverageSummaryResponse result = apiInstance.getCodeCoverageBranchSummary(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeCoverageApi#getCodeCoverageBranchSummary");
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
// Get code coverage summary for a branch returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_code_coverage::CodeCoverageAPI;
use datadog_api_client::datadogV2::model::BranchCoverageSummaryRequest;
use datadog_api_client::datadogV2::model::BranchCoverageSummaryRequestAttributes;
use datadog_api_client::datadogV2::model::BranchCoverageSummaryRequestData;
use datadog_api_client::datadogV2::model::BranchCoverageSummaryRequestType;

#[tokio::main]
async fn main() {
    let body = BranchCoverageSummaryRequest::new(BranchCoverageSummaryRequestData::new(
        BranchCoverageSummaryRequestAttributes::new(
            "prod".to_string(),
            "github.com/datadog/shopist".to_string(),
        ),
        BranchCoverageSummaryRequestType::CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetCodeCoverageBranchSummary", true);
    let api = CodeCoverageAPI::with_config(configuration);
    let resp = api.get_code_coverage_branch_summary(body).await;
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
 * Get code coverage summary for a branch returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getCodeCoverageBranchSummary"] = true;
const apiInstance = new v2.CodeCoverageApi(configuration);

const params: v2.CodeCoverageApiGetCodeCoverageBranchSummaryRequest = {
  body: {
    data: {
      attributes: {
        branch: "prod",
        repositoryId: "github.com/datadog/shopist",
      },
      type: "ci_app_coverage_branch_summary_request",
    },
  },
};

apiInstance
  .getCodeCoverageBranchSummary(params)
  .then((data: v2.CoverageSummaryResponse) => {
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

## Get code coverage summary for a commit{% #get-code-coverage-summary-for-a-commit %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/code-coverage/commit/summary |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/code-coverage/commit/summary |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/code-coverage/commit/summary      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/code-coverage/commit/summary      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/code-coverage/commit/summary     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/code-coverage/commit/summary |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/code-coverage/commit/summary |

### Overview



Retrieve aggregated code coverage statistics for a specific commit in a repository. This endpoint provides overall coverage metrics as well as breakdowns by service and code owner.

The commit SHA must be a 40-character hexadecimal string (SHA-1 hash).
This endpoint requires the `code_coverage_read` permission.
OAuth apps require the `code_coverage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#code-coverage) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                           | Type   | Description                                                                                                                                                                         |
| ------------ | ------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]          | object | Data object for commit summary request.                                                                                                                                             |
| data         | attributes [*required*]    | object | Attributes for requesting code coverage summary for a commit.                                                                                                                       |
| attributes   | commit_sha [*required*]    | string | The commit SHA (40-character hexadecimal string).                                                                                                                                   |
| attributes   | repository_id [*required*] | string | The repository identifier.                                                                                                                                                          |
| data         | type [*required*]          | enum   | JSON:API type for commit coverage summary request. The value must always be `ci_app_coverage_commit_summary_request`. Allowed enum values: `ci_app_coverage_commit_summary_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
      "repository_id": "github.com/datadog/shopist"
    },
    "type": "ci_app_coverage_commit_summary_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object containing code coverage summary.

| Parent field         | Field                   | Type   | Description                                                                                                                                     |
| -------------------- | ----------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                    | object | Data object for coverage summary response.                                                                                                      |
| data                 | attributes              | object | Attributes object for code coverage summary response.                                                                                           |
| attributes           | codeowners              | object | Coverage statistics broken down by code owner.                                                                                                  |
| additionalProperties | <any-key>               | object | Coverage statistics for a specific code owner.                                                                                                  |
| <any-key>            | evaluated_flags_count   | int64  | Number of coverage flags evaluated for the code owner.                                                                                          |
| <any-key>            | evaluated_reports_count | int64  | Number of coverage reports evaluated for the code owner.                                                                                        |
| <any-key>            | patch_coverage          | double | Patch coverage percentage for the code owner.                                                                                                   |
| <any-key>            | total_coverage          | double | Total coverage percentage for the code owner.                                                                                                   |
| attributes           | evaluated_flags_count   | int64  | Total number of coverage flags evaluated.                                                                                                       |
| attributes           | evaluated_reports_count | int64  | Total number of coverage reports evaluated.                                                                                                     |
| attributes           | patch_coverage          | double | Overall patch coverage percentage.                                                                                                              |
| attributes           | services                | object | Coverage statistics broken down by service.                                                                                                     |
| additionalProperties | <any-key>               | object | Coverage statistics for a specific service.                                                                                                     |
| <any-key>            | evaluated_flags_count   | int64  | Number of coverage flags evaluated for the service.                                                                                             |
| <any-key>            | evaluated_reports_count | int64  | Number of coverage reports evaluated for the service.                                                                                           |
| <any-key>            | patch_coverage          | double | Patch coverage percentage for the service.                                                                                                      |
| <any-key>            | total_coverage          | double | Total coverage percentage for the service.                                                                                                      |
| attributes           | total_coverage          | double | Overall total coverage percentage.                                                                                                              |
| data                 | id                      | string | Unique identifier for the coverage summary (base64-hashed).                                                                                     |
| data                 | type                    | enum   | JSON:API type for coverage summary response. The value must always be `ci_app_coverage_summary`. Allowed enum values: `ci_app_coverage_summary` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "codeowners": {
        "<any-key>": {
          "evaluated_flags_count": 2,
          "evaluated_reports_count": 4,
          "patch_coverage": 75.2,
          "total_coverage": 88.7
        }
      },
      "evaluated_flags_count": 8,
      "evaluated_reports_count": 12,
      "patch_coverage": 70.1,
      "services": {
        "<any-key>": {
          "evaluated_flags_count": 3,
          "evaluated_reports_count": 5,
          "patch_coverage": 72.3,
          "total_coverage": 85.5
        }
      },
      "total_coverage": 82.4
    },
    "id": "ZGQxMjM0NV9tYWluXzE3MDk1NjQwMDA=",
    "type": "ci_app_coverage_summary"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Not Authorized
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

{% tab title="404" %}
Not Found
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

{% tab title="500" %}
Internal server error
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/code-coverage/commit/summary" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588",
      "repository_id": "github.com/datadog/shopist"
    },
    "type": "ci_app_coverage_commit_summary_request"
  }
}
EOF
                
##### 

```python
"""
Get code coverage summary for a commit returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.code_coverage_api import CodeCoverageApi
from datadog_api_client.v2.model.commit_coverage_summary_request import CommitCoverageSummaryRequest
from datadog_api_client.v2.model.commit_coverage_summary_request_attributes import (
    CommitCoverageSummaryRequestAttributes,
)
from datadog_api_client.v2.model.commit_coverage_summary_request_data import CommitCoverageSummaryRequestData
from datadog_api_client.v2.model.commit_coverage_summary_request_type import CommitCoverageSummaryRequestType

body = CommitCoverageSummaryRequest(
    data=CommitCoverageSummaryRequestData(
        attributes=CommitCoverageSummaryRequestAttributes(
            commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
            repository_id="github.com/datadog/shopist",
        ),
        type=CommitCoverageSummaryRequestType.CI_APP_COVERAGE_COMMIT_SUMMARY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_code_coverage_commit_summary"] = True
with ApiClient(configuration) as api_client:
    api_instance = CodeCoverageApi(api_client)
    response = api_instance.get_code_coverage_commit_summary(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get code coverage summary for a commit returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_code_coverage_commit_summary".to_sym] = true
end
api_instance = DatadogAPIClient::V2::CodeCoverageAPI.new

body = DatadogAPIClient::V2::CommitCoverageSummaryRequest.new({
  data: DatadogAPIClient::V2::CommitCoverageSummaryRequestData.new({
    attributes: DatadogAPIClient::V2::CommitCoverageSummaryRequestAttributes.new({
      commit_sha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
      repository_id: "github.com/datadog/shopist",
    }),
    type: DatadogAPIClient::V2::CommitCoverageSummaryRequestType::CI_APP_COVERAGE_COMMIT_SUMMARY_REQUEST,
  }),
})
p api_instance.get_code_coverage_commit_summary(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get code coverage summary for a commit returns "OK" response

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
	body := datadogV2.CommitCoverageSummaryRequest{
		Data: datadogV2.CommitCoverageSummaryRequestData{
			Attributes: datadogV2.CommitCoverageSummaryRequestAttributes{
				CommitSha:    "66adc9350f2cc9b250b69abddab733dd55e1a588",
				RepositoryId: "github.com/datadog/shopist",
			},
			Type: datadogV2.COMMITCOVERAGESUMMARYREQUESTTYPE_CI_APP_COVERAGE_COMMIT_SUMMARY_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetCodeCoverageCommitSummary", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCodeCoverageApi(apiClient)
	resp, r, err := api.GetCodeCoverageCommitSummary(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CodeCoverageApi.GetCodeCoverageCommitSummary`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CodeCoverageApi.GetCodeCoverageCommitSummary`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get code coverage summary for a commit returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CodeCoverageApi;
import com.datadog.api.client.v2.model.CommitCoverageSummaryRequest;
import com.datadog.api.client.v2.model.CommitCoverageSummaryRequestAttributes;
import com.datadog.api.client.v2.model.CommitCoverageSummaryRequestData;
import com.datadog.api.client.v2.model.CommitCoverageSummaryRequestType;
import com.datadog.api.client.v2.model.CoverageSummaryResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getCodeCoverageCommitSummary", true);
    CodeCoverageApi apiInstance = new CodeCoverageApi(defaultClient);

    CommitCoverageSummaryRequest body =
        new CommitCoverageSummaryRequest()
            .data(
                new CommitCoverageSummaryRequestData()
                    .attributes(
                        new CommitCoverageSummaryRequestAttributes()
                            .commitSha("66adc9350f2cc9b250b69abddab733dd55e1a588")
                            .repositoryId("github.com/datadog/shopist"))
                    .type(CommitCoverageSummaryRequestType.CI_APP_COVERAGE_COMMIT_SUMMARY_REQUEST));

    try {
      CoverageSummaryResponse result = apiInstance.getCodeCoverageCommitSummary(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeCoverageApi#getCodeCoverageCommitSummary");
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
// Get code coverage summary for a commit returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_code_coverage::CodeCoverageAPI;
use datadog_api_client::datadogV2::model::CommitCoverageSummaryRequest;
use datadog_api_client::datadogV2::model::CommitCoverageSummaryRequestAttributes;
use datadog_api_client::datadogV2::model::CommitCoverageSummaryRequestData;
use datadog_api_client::datadogV2::model::CommitCoverageSummaryRequestType;

#[tokio::main]
async fn main() {
    let body = CommitCoverageSummaryRequest::new(CommitCoverageSummaryRequestData::new(
        CommitCoverageSummaryRequestAttributes::new(
            "66adc9350f2cc9b250b69abddab733dd55e1a588".to_string(),
            "github.com/datadog/shopist".to_string(),
        ),
        CommitCoverageSummaryRequestType::CI_APP_COVERAGE_COMMIT_SUMMARY_REQUEST,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetCodeCoverageCommitSummary", true);
    let api = CodeCoverageAPI::with_config(configuration);
    let resp = api.get_code_coverage_commit_summary(body).await;
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
 * Get code coverage summary for a commit returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getCodeCoverageCommitSummary"] = true;
const apiInstance = new v2.CodeCoverageApi(configuration);

const params: v2.CodeCoverageApiGetCodeCoverageCommitSummaryRequest = {
  body: {
    data: {
      attributes: {
        commitSha: "66adc9350f2cc9b250b69abddab733dd55e1a588",
        repositoryId: "github.com/datadog/shopist",
      },
      type: "ci_app_coverage_commit_summary_request",
    },
  },
};

apiInstance
  .getCodeCoverageCommitSummary(params)
  .then((data: v2.CoverageSummaryResponse) => {
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
