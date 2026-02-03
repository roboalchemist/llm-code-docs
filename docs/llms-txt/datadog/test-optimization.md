# Source: https://docs.datadoghq.com/api/latest/test-optimization.md

---
title: Test Optimization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Test Optimization
---

# Test Optimization

Search and manage flaky tests through Test Optimization. See the [Test Optimization page](https://docs.datadoghq.com/tests/) for more information.

## Search flaky tests{% #search-flaky-tests %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/test/flaky-test-management/tests |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/test/flaky-test-management/tests |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/test/flaky-test-management/tests      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/test/flaky-test-management/tests      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/test/flaky-test-management/tests     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/test/flaky-test-management/tests |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/test/flaky-test-management/tests |

### Overview

List endpoint returning flaky tests from Flaky Test Management. Results are paginated. This endpoint requires the `test_optimization_read` permission.

OAuth apps require the `test_optimization_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#test-optimization) to access this endpoint.



### Request

#### Body Data 



{% tab title="Model" %}

| Parent field | Field      | Type   | Description                                                                                                                                                                                                                                                                                                                                                                 |
| ------------ | ---------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | object | The JSON:API data for flaky tests search request.                                                                                                                                                                                                                                                                                                                           |
| data         | attributes | object | Attributes for the flaky tests search request.                                                                                                                                                                                                                                                                                                                              |
| attributes   | filter     | object | Search filter settings.                                                                                                                                                                                                                                                                                                                                                     |
| filter       | query      | string | Search query following log syntax used to filter flaky tests, same as on Flaky Tests Management UI. The supported search keys are:                                                                                                                                                                                                                                          |
| attributes   | page       | object | Pagination attributes for listing flaky tests.                                                                                                                                                                                                                                                                                                                              |
| page         | cursor     | string | List following results with a cursor provided in the previous request.                                                                                                                                                                                                                                                                                                      |
| page         | limit      | int64  | Maximum number of flaky tests in the response.                                                                                                                                                                                                                                                                                                                              |
| attributes   | sort       | enum   | Parameter for sorting flaky test results. The default sort is by ascending Fully Qualified Name (FQN). The FQN is the concatenation of the test module, suite, and name. Allowed enum values: `fqn,-fqn,first_flaked,-first_flaked,last_flaked,-last_flaked,failure_rate,-failure_rate,pipelines_failed,-pipelines_failed,pipelines_duration_lost,-pipelines_duration_lost` |
| data         | type       | enum   | The definition of `FlakyTestsSearchRequestDataType` object. Allowed enum values: `search_flaky_tests_request`                                                                                                                                                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "filter": {
        "query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""
      },
      "page": {
        "cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
        "limit": 25
      },
      "sort": "failure_rate"
    },
    "type": "string"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with flaky tests matching the search request.

| Parent field      | Field               | Type     | Description                                                                                                                                                                                                 |
| ----------------- | ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | data                | [object] | Array of flaky tests matching the request.                                                                                                                                                                  |
| data              | attributes          | object   | Attributes of a flaky test.                                                                                                                                                                                 |
| attributes        | attempt_to_fix_id   | string   | Unique identifier for the attempt to fix this flaky test. Use this ID in the Git commit message in order to trigger the attempt to fix workflow.                                                            | When the workflow is triggered the test is automatically retried by the tracer a certain number of configurable times. When all retries pass, the test is automatically marked as fixed in Flaky Test Management. Test runs are tagged with @test.test_management.attempt_to_fix_passed and @test.test_management.is_attempt_to_fix when the attempt to fix workflow is triggered. |
| attributes        | codeowners          | [string] | The name of the test's code owners as inferred from the repository configuration.                                                                                                                           |
| attributes        | envs                | [string] | List of environments where this test has been flaky.                                                                                                                                                        |
| attributes        | first_flaked_branch | string   | The branch name where the test exhibited flakiness for the first time.                                                                                                                                      |
| attributes        | first_flaked_sha    | string   | The commit SHA where the test exhibited flakiness for the first time.                                                                                                                                       |
| attributes        | first_flaked_ts     | int64    | Unix timestamp when the test exhibited flakiness for the first time.                                                                                                                                        |
| attributes        | flaky_category      | string   | The category of a flaky test.                                                                                                                                                                               |
| attributes        | flaky_state         | enum     | The current state of the flaky test. Allowed enum values: `active,fixed,quarantined,disabled`                                                                                                               |
| attributes        | last_flaked_branch  | string   | The branch name where the test exhibited flakiness for the last time.                                                                                                                                       |
| attributes        | last_flaked_sha     | string   | The commit SHA where the test exhibited flakiness for the last time.                                                                                                                                        |
| attributes        | last_flaked_ts      | int64    | Unix timestamp when the test exhibited flakiness for the last time.                                                                                                                                         |
| attributes        | module              | string   | The name of the test module. The definition of module changes slightly per language:                                                                                                                        |
| attributes        | name                | string   | The test name. A concise name for a test case. Defined in the test itself.                                                                                                                                  |
| attributes        | pipeline_stats      | object   | CI pipeline related statistics for the flaky test. This information is only available if test runs are associated with CI pipeline events from CI Visibility.                                               |
| pipeline_stats    | failed_pipelines    | int64    | The number of pipelines that failed due to this test for the past 7 days. This is computed as the sum of failed CI pipeline events associated with test runs where the flaky test failed.                   |
| pipeline_stats    | total_lost_time_ms  | int64    | The total time lost by CI pipelines due to this flaky test in milliseconds. This is computed as the sum of the duration of failed CI pipeline events associated with test runs where the flaky test failed. |
| attributes        | services            | [string] | List of test service names where this test has been flaky.                                                                                                                                                  | A test service is a group of tests associated with a project or repository. It contains all the individual tests for your code, optionally organized into test suites, which are like folders for your tests.                                                                                                                                                                      |
| attributes        | suite               | string   | The name of the test suite. A group of tests exercising the same unit of code depending on your language and testing framework.                                                                             |
| attributes        | test_run_metadata   | object   | Metadata about the latest failed test run of the flaky test.                                                                                                                                                |
| test_run_metadata | duration_ms         | int64    | The duration of the test run in milliseconds.                                                                                                                                                               |
| test_run_metadata | error_message       | string   | The error message from the test failure.                                                                                                                                                                    |
| test_run_metadata | error_stack         | string   | The stack trace from the test failure.                                                                                                                                                                      |
| test_run_metadata | source_end          | int64    | The line number where the test ends in the source file.                                                                                                                                                     |
| test_run_metadata | source_file         | string   | The source file where the test is defined.                                                                                                                                                                  |
| test_run_metadata | source_start        | int64    | The line number where the test starts in the source file.                                                                                                                                                   |
| attributes        | test_stats          | object   | Test statistics for the flaky test.                                                                                                                                                                         |
| test_stats        | failure_rate_pct    | double   | The failure rate percentage of the test for the past 7 days. This is the number of failed test runs divided by the total number of test runs (excluding skipped test runs).                                 |
| data              | id                  | string   | Test's ID. This ID is the hash of the test's Fully Qualified Name and Git repository ID. On the Test Runs UI it is the same as the `test_fingerprint_fqn` tag.                                              |
| data              | type                | enum     | The type of the flaky test from Flaky Test Management. Allowed enum values: `flaky_test`                                                                                                                    |
|                   | meta                | object   | Metadata for the flaky tests search response.                                                                                                                                                               |
| meta              | pagination          | object   | Pagination metadata for flaky tests.                                                                                                                                                                        |
| pagination        | next_page           | string   | Cursor for the next page of results.                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attempt_to_fix_id": "I42TEO",
        "codeowners": [
          "@foo",
          "@bar"
        ],
        "envs": "prod",
        "first_flaked_branch": "main",
        "first_flaked_sha": "0c6be03165b7f7ffe96e076ffb29afb2825616c3",
        "first_flaked_ts": 1757688149,
        "flaky_category": "Timeout",
        "flaky_state": "active",
        "last_flaked_branch": "main",
        "last_flaked_sha": "0c6be03165b7f7ffe96e076ffb29afb2825616c3",
        "last_flaked_ts": 1757688149,
        "module": "TestModule",
        "name": "TestName",
        "pipeline_stats": {
          "failed_pipelines": 319,
          "total_lost_time_ms": 1527550000
        },
        "services": [
          "foo",
          "bar"
        ],
        "suite": "TestSuite",
        "test_run_metadata": {
          "duration_ms": 27398,
          "error_message": "Expecting actual not to be empty",
          "error_stack": "Traceback (most recent call last):\n  File \"test_foo.py\", line 10, in test_foo\n    assert actual == expected\nAssertionError: Expecting actual not to be empty",
          "source_end": 20,
          "source_file": "test_foo.py",
          "source_start": 10
        },
        "test_stats": {
          "failure_rate_pct": 0.1
        }
      },
      "id": "string",
      "type": "string"
    }
  ],
  "meta": {
    "pagination": {
      "next_page": "string"
    }
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/test/flaky-test-management/tests" \
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
Search flaky tests returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.flaky_tests_search_filter import FlakyTestsSearchFilter
from datadog_api_client.v2.model.flaky_tests_search_page_options import FlakyTestsSearchPageOptions
from datadog_api_client.v2.model.flaky_tests_search_request import FlakyTestsSearchRequest
from datadog_api_client.v2.model.flaky_tests_search_request_attributes import FlakyTestsSearchRequestAttributes
from datadog_api_client.v2.model.flaky_tests_search_request_data import FlakyTestsSearchRequestData
from datadog_api_client.v2.model.flaky_tests_search_request_data_type import FlakyTestsSearchRequestDataType
from datadog_api_client.v2.model.flaky_tests_search_sort import FlakyTestsSearchSort

body = FlakyTestsSearchRequest(
    data=FlakyTestsSearchRequestData(
        attributes=FlakyTestsSearchRequestAttributes(
            filter=FlakyTestsSearchFilter(
                query='flaky_test_state:active @git.repository.id_v2:"github.com/datadog/shopist"',
            ),
            page=FlakyTestsSearchPageOptions(
                cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
                limit=25,
            ),
            sort=FlakyTestsSearchSort.FAILURE_RATE_ASCENDING,
        ),
        type=FlakyTestsSearchRequestDataType.SEARCH_FLAKY_TESTS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["search_flaky_tests"] = True
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    response = api_instance.search_flaky_tests(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Search flaky tests returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.search_flaky_tests".to_sym] = true
end
api_instance = DatadogAPIClient::V2::TestOptimizationAPI.new

body = DatadogAPIClient::V2::FlakyTestsSearchRequest.new({
  data: DatadogAPIClient::V2::FlakyTestsSearchRequestData.new({
    attributes: DatadogAPIClient::V2::FlakyTestsSearchRequestAttributes.new({
      filter: DatadogAPIClient::V2::FlakyTestsSearchFilter.new({
        query: 'flaky_test_state:active @git.repository.id_v2:"github.com/datadog/shopist"',
      }),
      page: DatadogAPIClient::V2::FlakyTestsSearchPageOptions.new({
        cursor: "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
        limit: 25,
      }),
      sort: DatadogAPIClient::V2::FlakyTestsSearchSort::FAILURE_RATE_ASCENDING,
    }),
    type: DatadogAPIClient::V2::FlakyTestsSearchRequestDataType::SEARCH_FLAKY_TESTS_REQUEST,
  }),
})
opts = {
  body: body,
}
p api_instance.search_flaky_tests(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Search flaky tests returns "OK" response

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
	body := datadogV2.FlakyTestsSearchRequest{
		Data: &datadogV2.FlakyTestsSearchRequestData{
			Attributes: &datadogV2.FlakyTestsSearchRequestAttributes{
				Filter: &datadogV2.FlakyTestsSearchFilter{
					Query: datadog.PtrString(`flaky_test_state:active @git.repository.id_v2:"github.com/datadog/shopist"`),
				},
				Page: &datadogV2.FlakyTestsSearchPageOptions{
					Cursor: datadog.PtrString("eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="),
					Limit:  datadog.PtrInt64(25),
				},
				Sort: datadogV2.FLAKYTESTSSEARCHSORT_FAILURE_RATE_ASCENDING.Ptr(),
			},
			Type: datadogV2.FLAKYTESTSSEARCHREQUESTDATATYPE_SEARCH_FLAKY_TESTS_REQUEST.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.SearchFlakyTests", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewTestOptimizationApi(apiClient)
	resp, r, err := api.SearchFlakyTests(ctx, *datadogV2.NewSearchFlakyTestsOptionalParameters().WithBody(body))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestOptimizationApi.SearchFlakyTests`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `TestOptimizationApi.SearchFlakyTests`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Search flaky tests returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.TestOptimizationApi;
import com.datadog.api.client.v2.api.TestOptimizationApi.SearchFlakyTestsOptionalParameters;
import com.datadog.api.client.v2.model.FlakyTestsSearchFilter;
import com.datadog.api.client.v2.model.FlakyTestsSearchPageOptions;
import com.datadog.api.client.v2.model.FlakyTestsSearchRequest;
import com.datadog.api.client.v2.model.FlakyTestsSearchRequestAttributes;
import com.datadog.api.client.v2.model.FlakyTestsSearchRequestData;
import com.datadog.api.client.v2.model.FlakyTestsSearchRequestDataType;
import com.datadog.api.client.v2.model.FlakyTestsSearchResponse;
import com.datadog.api.client.v2.model.FlakyTestsSearchSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.searchFlakyTests", true);
    TestOptimizationApi apiInstance = new TestOptimizationApi(defaultClient);

    FlakyTestsSearchRequest body =
        new FlakyTestsSearchRequest()
            .data(
                new FlakyTestsSearchRequestData()
                    .attributes(
                        new FlakyTestsSearchRequestAttributes()
                            .filter(
                                new FlakyTestsSearchFilter()
                                    .query(
                                        """
flaky_test_state:active @git.repository.id_v2:"github.com/datadog/shopist"
"""))
                            .page(
                                new FlakyTestsSearchPageOptions()
                                    .cursor(
                                        "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==")
                                    .limit(25L))
                            .sort(FlakyTestsSearchSort.FAILURE_RATE_ASCENDING))
                    .type(FlakyTestsSearchRequestDataType.SEARCH_FLAKY_TESTS_REQUEST));

    try {
      FlakyTestsSearchResponse result =
          apiInstance.searchFlakyTests(new SearchFlakyTestsOptionalParameters().body(body));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestOptimizationApi#searchFlakyTests");
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
// Search flaky tests returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_test_optimization::SearchFlakyTestsOptionalParams;
use datadog_api_client::datadogV2::api_test_optimization::TestOptimizationAPI;
use datadog_api_client::datadogV2::model::FlakyTestsSearchFilter;
use datadog_api_client::datadogV2::model::FlakyTestsSearchPageOptions;
use datadog_api_client::datadogV2::model::FlakyTestsSearchRequest;
use datadog_api_client::datadogV2::model::FlakyTestsSearchRequestAttributes;
use datadog_api_client::datadogV2::model::FlakyTestsSearchRequestData;
use datadog_api_client::datadogV2::model::FlakyTestsSearchRequestDataType;
use datadog_api_client::datadogV2::model::FlakyTestsSearchSort;

#[tokio::main]
async fn main() {
    let body =
        FlakyTestsSearchRequest
        ::new().data(
            FlakyTestsSearchRequestData::new()
                .attributes(
                    FlakyTestsSearchRequestAttributes::new()
                        .filter(
                            FlakyTestsSearchFilter
                            ::new().query(
                                r#"flaky_test_state:active @git.repository.id_v2:"github.com/datadog/shopist""#.to_string(),
                            ),
                        )
                        .page(
                            FlakyTestsSearchPageOptions::new()
                                .cursor(
                                    "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==".to_string(),
                                )
                                .limit(25),
                        )
                        .sort(FlakyTestsSearchSort::FAILURE_RATE_ASCENDING),
                )
                .type_(FlakyTestsSearchRequestDataType::SEARCH_FLAKY_TESTS_REQUEST),
        );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.SearchFlakyTests", true);
    let api = TestOptimizationAPI::with_config(configuration);
    let resp = api
        .search_flaky_tests(SearchFlakyTestsOptionalParams::default().body(body))
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Search flaky tests returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.searchFlakyTests"] = true;
const apiInstance = new v2.TestOptimizationApi(configuration);

const params: v2.TestOptimizationApiSearchFlakyTestsRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          query: `flaky_test_state:active @git.repository.id_v2:"github.com/datadog/shopist"`,
        },
        page: {
          cursor:
            "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
          limit: 25,
        },
        sort: "failure_rate",
      },
      type: "search_flaky_tests_request",
    },
  },
};

apiInstance
  .searchFlakyTests(params)
  .then((data: v2.FlakyTestsSearchResponse) => {
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

## Update flaky test states{% #update-flaky-test-states %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/test/flaky-test-management/tests |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/test/flaky-test-management/tests |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/test/flaky-test-management/tests      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/test/flaky-test-management/tests      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/test/flaky-test-management/tests     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/test/flaky-test-management/tests |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/test/flaky-test-management/tests |

### Overview

Update the state of multiple flaky tests in Flaky Test Management. This endpoint requires the `test_optimization_write` permission.

OAuth apps require the `test_optimization_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#test-optimization) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                                                     |
| ------------ | ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | The JSON:API data for updating flaky test states.                                                                                                               |
| data         | attributes [*required*] | object   | Attributes for updating flaky test states.                                                                                                                      |
| attributes   | tests [*required*]      | [object] | List of flaky tests to update.                                                                                                                                  |
| tests        | id [*required*]         | string   | The ID of the flaky test. This is the same ID returned by the Search flaky tests endpoint and corresponds to the test_fingerprint_fqn field in test run events. |
| tests        | new_state [*required*]  | enum     | The new state to set for the flaky test. Allowed enum values: `active,quarantined,disabled,fixed`                                                               |
| data         | type [*required*]       | enum     | The definition of `UpdateFlakyTestsRequestDataType` object. Allowed enum values: `update_flaky_test_state_request`                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "tests": [
        {
          "id": "4eb1887a8adb1847",
          "new_state": "active"
        }
      ]
    },
    "type": "update_flaky_test_state_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for updating flaky test states.

| Parent field | Field                        | Type     | Description                                                                                                                                                                      |
| ------------ | ---------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object   | Summary of the update operations. Tells whether a test succeeded or failed to be updated.                                                                                        |
| data         | attributes                   | object   | Attributes for the update flaky test state response.                                                                                                                             |
| attributes   | has_errors [*required*] | boolean  | `True` if any errors occurred during the update operations. `False` if all tests succeeded to be updated.                                                                        |
| attributes   | results [*required*]    | [object] | Results of the update operation for each test.                                                                                                                                   |
| results      | error                        | string   | Error message if the update failed.                                                                                                                                              |
| results      | id [*required*]         | string   | The ID of the flaky test from the request. This is the same ID returned by the Search flaky tests endpoint and corresponds to the test_fingerprint_fqn field in test run events. |
| results      | success [*required*]    | boolean  | `True` if the update was successful, `False` if there were any errors.                                                                                                           |
| data         | id                           | string   | The ID of the response.                                                                                                                                                          |
| data         | type                         | enum     | The definition of `UpdateFlakyTestsResponseDataType` object. Allowed enum values: `update_flaky_test_state_response`                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "has_errors": true,
      "results": [
        {
          "error": "string",
          "id": "4eb1887a8adb1847",
          "success": false
        }
      ]
    },
    "id": "string",
    "type": "string"
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
                  \# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/test/flaky-test-management/tests" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "tests": [
        {
          "id": "4eb1887a8adb1847",
          "new_state": "active"
        }
      ]
    },
    "type": "update_flaky_test_state_request"
  }
}
EOF
                
{% /tab %}
