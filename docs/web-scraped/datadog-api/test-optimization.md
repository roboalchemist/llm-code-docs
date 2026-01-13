# Source: https://docs.datadoghq.com/api/latest/test-optimization

# Test Optimization
Search and manage flaky tests through Test Optimization. See the [Test Optimization page](https://docs.datadoghq.com/tests/) for more information.
## [Search flaky tests](https://docs.datadoghq.com/api/latest/test-optimization/#search-flaky-tests)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/test-optimization/#search-flaky-tests-v2)


**Note** : This endpoint is in preview and may be subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/test/flaky-test-management/testshttps://api.ap2.datadoghq.com/api/v2/test/flaky-test-management/testshttps://api.datadoghq.eu/api/v2/test/flaky-test-management/testshttps://api.ddog-gov.com/api/v2/test/flaky-test-management/testshttps://api.datadoghq.com/api/v2/test/flaky-test-management/testshttps://api.us3.datadoghq.com/api/v2/test/flaky-test-management/testshttps://api.us5.datadoghq.com/api/v2/test/flaky-test-management/tests
### Overview
List endpoint returning flaky tests from Flaky Test Management. Results are paginated. This endpoint requires the `test_optimization_read` permission.
OAuth apps require the `test_optimization_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#test-optimization) to access this endpoint.
### Request
#### Body Data 
  * [Model](https://docs.datadoghq.com/api/latest/test-optimization/)
  * [Example](https://docs.datadoghq.com/api/latest/test-optimization/)


Field
Type
Description
data
object
The JSON:API data for flaky tests search request.
attributes
object
Attributes for the flaky tests search request.
filter
object
Search filter settings.
query
string
Search query following log syntax used to filter flaky tests, same as on Flaky Tests Management UI. The supported search keys are:
  * `flaky_test_state`
  * `flaky_test_category`
  * `@test.name`
  * `@test.suite`
  * `@test.module`
  * `@test.service`
  * `@git.repository.id_v2`
  * `@git.branch`
  * `@test.codeowners`
  * `env`


default: `*`
page
object
Pagination attributes for listing flaky tests.
cursor
string
List following results with a cursor provided in the previous request.
limit
int64
Maximum number of flaky tests in the response.
default: `10`
sort
enum
Parameter for sorting flaky test results. The default sort is by ascending Fully Qualified Name (FQN). The FQN is the concatenation of the test module, suite, and name. Allowed enum values: `fqn,-fqn,first_flaked,-first_flaked,last_flaked,-last_flaked,failure_rate,-failure_rate,pipelines_failed,-pipelines_failed,pipelines_duration_lost,-pipelines_duration_lost`
type
enum
The definition of `FlakyTestsSearchRequestDataType` object. Allowed enum values: `search_flaky_tests_request`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/test-optimization/#SearchFlakyTests-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/test-optimization/#SearchFlakyTests-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/test-optimization/#SearchFlakyTests-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/test-optimization/#SearchFlakyTests-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/test-optimization/)
  * [Example](https://docs.datadoghq.com/api/latest/test-optimization/)


Response object with flaky tests matching the search request.
Field
Type
Description
data
[object]
Array of flaky tests matching the request.
attributes
object
Attributes of a flaky test.
attempt_to_fix_id
string
Unique identifier for the attempt to fix this flaky test. Use this ID in the Git commit message in order to trigger the attempt to fix workflow.
When the workflow is triggered the test is automatically retried by the tracer a certain number of configurable times. When all retries pass, the test is automatically marked as fixed in Flaky Test Management. Test runs are tagged with @test.test_management.attempt_to_fix_passed and @test.test_management.is_attempt_to_fix when the attempt to fix workflow is triggered.
codeowners
[string]
The name of the test's code owners as inferred from the repository configuration.
envs
[string]
List of environments where this test has been flaky.
first_flaked_branch
string
The branch name where the test exhibited flakiness for the first time.
first_flaked_sha
string
The commit SHA where the test exhibited flakiness for the first time.
first_flaked_ts
int64
Unix timestamp when the test exhibited flakiness for the first time.
flaky_category
string
The category of a flaky test.
flaky_state
enum
The current state of the flaky test. Allowed enum values: `active,fixed,quarantined,disabled`
last_flaked_branch
string
The branch name where the test exhibited flakiness for the last time.
last_flaked_sha
string
The commit SHA where the test exhibited flakiness for the last time.
last_flaked_ts
int64
Unix timestamp when the test exhibited flakiness for the last time.
module
string
The name of the test module. The definition of module changes slightly per language:
  * In .NET, a test module groups every test that is run under the same unit test project.
  * In Swift, a test module groups every test that is run for a given bundle.
  * In JavaScript, the test modules map one-to-one to test sessions.
  * In Java, a test module groups every test that is run by the same Maven Surefire/Failsafe or Gradle Test task execution.
  * In Python, a test module groups every test that is run under the same `.py` file as part of a test suite, which is typically managed by a framework like `unittest` or `pytest`.
  * In Ruby, a test module groups every test that is run within the same test file, which is typically managed by a framework like `RSpec` or `Minitest`.


name
string
The test name. A concise name for a test case. Defined in the test itself.
pipeline_stats
object
CI pipeline related statistics for the flaky test. This information is only available if test runs are associated with CI pipeline events from CI Visibility.
failed_pipelines
int64
The number of pipelines that failed due to this test for the past 7 days. This is computed as the sum of failed CI pipeline events associated with test runs where the flaky test failed.
total_lost_time_ms
int64
The total time lost by CI pipelines due to this flaky test in milliseconds. This is computed as the sum of the duration of failed CI pipeline events associated with test runs where the flaky test failed.
services
[string]
List of test service names where this test has been flaky.
A test service is a group of tests associated with a project or repository. It contains all the individual tests for your code, optionally organized into test suites, which are like folders for your tests.
suite
string
The name of the test suite. A group of tests exercising the same unit of code depending on your language and testing framework.
test_run_metadata
object
Metadata about the latest failed test run of the flaky test.
duration_ms
int64
The duration of the test run in milliseconds.
error_message
string
The error message from the test failure.
error_stack
string
The stack trace from the test failure.
source_end
int64
The line number where the test ends in the source file.
source_file
string
The source file where the test is defined.
source_start
int64
The line number where the test starts in the source file.
test_stats
object
Test statistics for the flaky test.
failure_rate_pct
double
The failure rate percentage of the test for the past 7 days. This is the number of failed test runs divided by the total number of test runs (excluding skipped test runs).
id
string
Test's ID. This ID is the hash of the test's Fully Qualified Name and Git repository ID. On the Test Runs UI it is the same as the `test_fingerprint_fqn` tag.
type
enum
The type of the flaky test from Flaky Test Management. Allowed enum values: `flaky_test`
meta
object
Metadata for the flaky tests search response.
pagination
object
Pagination metadata for flaky tests.
next_page
string
Cursor for the next page of results.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/test-optimization/)
  * [Example](https://docs.datadoghq.com/api/latest/test-optimization/)


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
  * [Model](https://docs.datadoghq.com/api/latest/test-optimization/)
  * [Example](https://docs.datadoghq.com/api/latest/test-optimization/)


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
  * [Model](https://docs.datadoghq.com/api/latest/test-optimization/)
  * [Example](https://docs.datadoghq.com/api/latest/test-optimization/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/test-optimization/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/test-optimization/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/test-optimization/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/test-optimization/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/test-optimization/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/test-optimization/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/test-optimization/?code-lang=typescript)


#####  Search flaky tests
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/test/flaky-test-management/tests" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Search flaky tests
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Search flaky tests
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Search flaky tests
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Search flaky tests
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Search flaky tests
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Search flaky tests
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=94a79573-6e05-4042-8842-fc6a9c976379&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8e522bda-345e-47a9-9548-a76f6ac45835&pt=Test%20Optimization&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ftest-optimization%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=94a79573-6e05-4042-8842-fc6a9c976379&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8e522bda-345e-47a9-9548-a76f6ac45835&pt=Test%20Optimization&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ftest-optimization%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=c78cfa63-4c91-4fa4-8fbe-47833a115105&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Test%20Optimization&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Ftest-optimization%2F&r=&lt=4979&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=257142)
