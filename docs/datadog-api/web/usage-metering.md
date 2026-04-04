# Source: https://docs.datadoghq.com/api/latest/usage-metering

# Usage Metering
The usage metering API allows you to get hourly, daily, and monthly usage across multiple facets of Datadog. This API is available to all Pro and Enterprise customers.
**Note** : Usage data is delayed by up to 72 hours from when it was incurred. It is retained for 15 months.
You can retrieve up to 24 hours of hourly usage data for multiple organizations, and up to two months of hourly usage data for a single organization in one request. Learn more on the [usage details documentation](https://docs.datadoghq.com/account_management/billing/usage_details/).
## [Get billing dimension mapping for usage endpoints](https://docs.datadoghq.com/api/latest/usage-metering/#get-billing-dimension-mapping-for-usage-endpoints)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-billing-dimension-mapping-for-usage-endpoints-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/billing_dimension_mappinghttps://api.ap2.datadoghq.com/api/v2/usage/billing_dimension_mappinghttps://api.datadoghq.eu/api/v2/usage/billing_dimension_mappinghttps://api.ddog-gov.com/api/v2/usage/billing_dimension_mappinghttps://api.datadoghq.com/api/v2/usage/billing_dimension_mappinghttps://api.us3.datadoghq.com/api/v2/usage/billing_dimension_mappinghttps://api.us5.datadoghq.com/api/v2/usage/billing_dimension_mapping
### Overview
Get a mapping of billing dimensions to the corresponding keys for the supported usage metering public API endpoints. Mapping data is updated on a monthly cadence.
This endpoint is only accessible to [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/).
This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter[month]
string
Datetime in ISO-8601 format, UTC, and for mappings beginning this month. Defaults to the current month.
filter[view]
string
String to specify whether to retrieve active billing dimension mappings for the contract or for all available mappings. Allowed views have the string `active` or `all`. Defaults to `active`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetBillingDimensionMapping-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetBillingDimensionMapping-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetBillingDimensionMapping-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetBillingDimensionMapping-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Billing dimensions mapping response.
Field
Type
Description
data
[object]
Billing dimensions mapping data.
attributes
object
Mapping of billing dimensions to endpoint keys.
endpoints
[object]
List of supported endpoints with their keys mapped to the billing_dimension.
id
string
The URL for the endpoint.
keys
[string]
The billing dimension.
status
enum
Denotes whether mapping keys were available for this endpoint. Allowed enum values: `OK,NOT_FOUND`
in_app_label
string
Label used for the billing dimension in the Plan & Usage charts.
timestamp
date-time
Month in ISO-8601 format, UTC, and precise to the second: `[YYYY-MM-DDThh:mm:ss]`.
id
string
ID of the billing dimension.
type
enum
Type of active billing dimensions data. Allowed enum values: `billing_dimensions`
default: `billing_dimensions`
```
{
  "data": [
    {
      "attributes": {
        "endpoints": [
          {
            "id": "api/v1/usage/billable-summary",
            "keys": [
              "apm_host_top99p",
              "apm_host_sum"
            ],
            "status": "string"
          }
        ],
        "in_app_label": "APM Hosts",
        "timestamp": "2019-09-19T10:00:00.000Z"
      },
      "id": "string",
      "type": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get billing dimension mapping for usage endpoints
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/billing_dimension_mapping" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get billing dimension mapping for usage endpoints
```
"""
Get billing dimension mapping for usage endpoints returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_billing_dimension_mapping()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get billing dimension mapping for usage endpoints
```
# Get billing dimension mapping for usage endpoints returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
p api_instance.get_billing_dimension_mapping()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get billing dimension mapping for usage endpoints
```
// Get billing dimension mapping for usage endpoints returns "OK" response

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
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetBillingDimensionMapping(ctx, *datadogV2.NewGetBillingDimensionMappingOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetBillingDimensionMapping`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetBillingDimensionMapping`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get billing dimension mapping for usage endpoints
```
// Get billing dimension mapping for usage endpoints returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.model.BillingDimensionsMappingResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      BillingDimensionsMappingResponse result = apiInstance.getBillingDimensionMapping();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getBillingDimensionMapping");
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

#####  Get billing dimension mapping for usage endpoints
```
// Get billing dimension mapping for usage endpoints returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetBillingDimensionMappingOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_billing_dimension_mapping(GetBillingDimensionMappingOptionalParams::default())
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

#####  Get billing dimension mapping for usage endpoints
```
/**
 * Get billing dimension mapping for usage endpoints returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

apiInstance
  .getBillingDimensionMapping()
  .then((data: v2.BillingDimensionsMappingResponse) => {
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
## [Get hourly usage by product family](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/hourly_usagehttps://api.ap2.datadoghq.com/api/v2/usage/hourly_usagehttps://api.datadoghq.eu/api/v2/usage/hourly_usagehttps://api.ddog-gov.com/api/v2/usage/hourly_usagehttps://api.datadoghq.com/api/v2/usage/hourly_usagehttps://api.us3.datadoghq.com/api/v2/usage/hourly_usagehttps://api.us5.datadoghq.com/api/v2/usage/hourly_usage
### Overview
Get hourly usage by product family. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter[timestamp][start] [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
filter[timestamp][end]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
filter[product_families] [_required_]
string
Comma separated list of product families to retrieve. Available families are `all`, `analyzed_logs`, `application_security`, `audit_trail`, `bits_ai`, `serverless`, `ci_app`, `cloud_cost_management`, `cloud_siem`, `csm_container_enterprise`, `csm_host_enterprise`, `cspm`, `custom_events`, `cws`, `dbm`, `error_tracking`, `fargate`, `infra_hosts`, `incident_management`, `indexed_logs`, `indexed_spans`, `ingested_spans`, `iot`, `lambda_traced_invocations`, `llm_observability`, `logs`, `network_flows`, `network_hosts`, `network_monitoring`, `observability_pipelines`, `online_archive`, `profiling`, `product_analytics`, `rum`, `rum_browser_sessions`, `rum_mobile_sessions`, `sds`, `snmp`, `software_delivery`, `synthetics_api`, `synthetics_browser`, `synthetics_mobile`, `synthetics_parallel_testing`, `timeseries`, `vuln_management` and `workflow_executions`. The following product family has been **deprecated** : `audit_logs`.
filter[include_descendants]
boolean
Include child org usage in the response. Defaults to false.
filter[include_connected_accounts]
boolean
Boolean to specify whether to include accounts connected to the current account as partner customers in the Datadog partner network program. Defaults to false.
filter[include_breakdown]
boolean
Include breakdown of usage by subcategories where applicable (for product family logs only). Defaults to false.
filter[versions]
string
Comma separated list of product family versions to use in the format `product_family:version`. For example, `infra_hosts:1.0.0`. If this parameter is not used, the API will use the latest version of each requested product family. Currently all families have one version `1.0.0`.
page[limit]
integer
Maximum number of results to return (between 1 and 500) - defaults to 500 if limit not specified.
page[next_record_id]
string
List following results with a next_record_id provided in the previous query.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetHourlyUsage-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetHourlyUsage-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetHourlyUsage-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetHourlyUsage-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Hourly usage response.
Field
Type
Description
data
[object]
Response containing hourly usage.
attributes
object
Attributes of hourly usage for a product family for an org for a time period.
account_name
string
The account name.
account_public_id
string
The account public ID.
measurements
[object]
List of the measured usage values for the product family for the org for the time period.
usage_type
string
Type of usage.
value
int64
Contains the number measured for the given usage_type during the hour.
org_name
string
The organization name.
product_family
string
The product for which usage is being reported.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
timestamp
date-time
Datetime in ISO-8601 format, UTC. The hour for the usage.
id
string
Unique ID of the response.
type
enum
Type of usage data. Allowed enum values: `usage_timeseries`
default: `usage_timeseries`
meta
object
The object containing document metadata.
pagination
object
The metadata for the current pagination.
next_record_id
string
The cursor to get the next results (if any). To make the next request, use the same parameters and add `next_record_id`.
```
{
  "data": [
    {
      "attributes": {
        "account_name": "string",
        "account_public_id": "string",
        "measurements": [
          {
            "usage_type": "string",
            "value": "integer"
          }
        ],
        "org_name": "string",
        "product_family": "string",
        "public_id": "string",
        "region": "string",
        "timestamp": "2019-09-19T10:00:00.000Z"
      },
      "id": "string",
      "type": "usage_timeseries"
    }
  ],
  "meta": {
    "pagination": {
      "next_record_id": "string"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage by product family
Copy
```
                  # Required query arguments  
export filter[timestamp][start]="CHANGE_ME"  
export filter[product_families]="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/hourly_usage?filter[timestamp][start]=${filter[timestamp][start]}&filter[product_families]=${filter[product_families]}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage by product family
```
"""
Get hourly usage by product family returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_hourly_usage(
        filter_timestamp_start=(datetime.now() + relativedelta(days=-3)),
        filter_product_families="infra_hosts",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage by product family
```
# Get hourly usage by product family returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
p api_instance.get_hourly_usage((Time.now + -3 * 86400), "infra_hosts")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage by product family
```
// Get hourly usage by product family returns "OK" response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetHourlyUsage(ctx, time.Now().AddDate(0, 0, -3), "infra_hosts", *datadogV2.NewGetHourlyUsageOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetHourlyUsage`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetHourlyUsage`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage by product family
```
// Get hourly usage by product family returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.model.HourlyUsageResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      HourlyUsageResponse result =
          apiInstance.getHourlyUsage(OffsetDateTime.now().plusDays(-3), "infra_hosts");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getHourlyUsage");
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

#####  Get hourly usage by product family
```
// Get hourly usage by product family returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetHourlyUsageOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_hourly_usage(
            DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            "infra_hosts".to_string(),
            GetHourlyUsageOptionalParams::default(),
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

#####  Get hourly usage by product family
```
/**
 * Get hourly usage by product family returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetHourlyUsageRequest = {
  filterTimestampStart: new Date(new Date().getTime() + -3 * 86400 * 1000),
  filterProductFamilies: "infra_hosts",
};

apiInstance
  .getHourlyUsage(params)
  .then((data: v2.HourlyUsageResponse) => {
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
## [Get hourly usage attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-attribution)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-attribution-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/hourly-attributionhttps://api.ap2.datadoghq.com/api/v1/usage/hourly-attributionhttps://api.datadoghq.eu/api/v1/usage/hourly-attributionhttps://api.ddog-gov.com/api/v1/usage/hourly-attributionhttps://api.datadoghq.com/api/v1/usage/hourly-attributionhttps://api.us3.datadoghq.com/api/v1/usage/hourly-attributionhttps://api.us5.datadoghq.com/api/v1/usage/hourly-attribution
### Overview
Get hourly usage attribution. Multi-region data is available starting March 1, 2023.
This API endpoint is paginated. To make sure you receive all records, check if the value of `next_record_id` is set in the response. If it is, make another request and pass `next_record_id` as a parameter. Pseudo code example:
```
response := GetHourlyUsageAttribution(start_month)
cursor := response.metadata.pagination.next_record_id
WHILE cursor != null BEGIN
  sleep(5 seconds)  # Avoid running into rate limit
  response := GetHourlyUsageAttribution(start_month, next_record_id=cursor)
  cursor := response.metadata.pagination.next_record_id
END

```

The following values have been **deprecated** : `estimated_indexed_spans_usage`, `estimated_indexed_spans_percentage`, `estimated_ingested_spans_usage`, `estimated_ingested_spans_percentage`, `llm_observability_usage`, `llm_observability_percentage`.
This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
usage_type [_required_]
enum
Usage type to retrieve. The following values have been **deprecated** : `estimated_indexed_spans_usage`, `estimated_ingested_spans_usage`.  
Allowed enum values: `api_usage, apm_fargate_usage, apm_host_usage, apm_usm_usage, appsec_fargate_usage, appsec_usage, asm_serverless_traced_invocations_usage, asm_serverless_traced_invocations_percentage, bits_ai_investigations_usage, browser_usage, ci_pipeline_indexed_spans_usage, ci_test_indexed_spans_usage, ci_visibility_itr_usage, cloud_siem_usage, code_security_host_usage, container_excl_agent_usage, container_usage, cspm_containers_usage, cspm_hosts_usage, custom_event_usage, custom_ingested_timeseries_usage, custom_timeseries_usage, cws_containers_usage, cws_fargate_task_usage, cws_hosts_usage, data_jobs_monitoring_usage, data_stream_monitoring_usage, dbm_hosts_usage, dbm_queries_usage, error_tracking_usage, error_tracking_percentage, estimated_indexed_spans_usage, estimated_ingested_spans_usage, fargate_usage, flex_stored_logs, functions_usage, incident_management_monthly_active_users_usage, indexed_spans_usage, infra_host_usage, ingested_logs_bytes_usage, ingested_spans_bytes_usage, invocations_usage, lambda_traced_invocations_usage, llm_observability_usage, llm_spans_usage, logs_indexed_15day_usage, logs_indexed_180day_usage, logs_indexed_1day_usage, logs_indexed_30day_usage, logs_indexed_360day_usage, logs_indexed_3day_usage, logs_indexed_45day_usage, logs_indexed_60day_usage, logs_indexed_7day_usage, logs_indexed_90day_usage, logs_indexed_custom_retention_usage, mobile_app_testing_usage, ndm_netflow_usage, npm_host_usage, network_device_wireless_usage, obs_pipeline_bytes_usage, obs_pipelines_vcpu_usage, online_archive_usage, product_analytics_session_usage, profiled_container_usage, profiled_fargate_usage, profiled_host_usage, published_app, rum_browser_mobile_sessions_usage, rum_ingested_usage, rum_investigate_usage, rum_replay_sessions_usage, rum_session_replay_add_on_usage, sca_fargate_usage, sds_scanned_bytes_usage, serverless_apps_usage, siem_analyzed_logs_add_on_usage, siem_ingested_bytes_usage, snmp_usage, universal_service_monitoring_usage, vuln_management_hosts_usage, workflow_executions_usage`
next_record_id
string
List following results with a next_record_id provided in the previous query.
tag_breakdown_keys
string
Comma separated list of tags used to group usage. If no value is provided the usage will not be broken down by tags.
To see which tags are available, look for the value of `tag_config_source` in the API response.
include_descendants
boolean
Include child org usage in the response. Defaults to `true`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetHourlyUsageAttribution-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetHourlyUsageAttribution-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetHourlyUsageAttribution-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the hourly usage attribution by tag(s).
Field
Type
Description
metadata
object
The object containing document metadata.
pagination
object
The metadata for the current pagination.
next_record_id
string
The cursor to get the next results (if any). To make the next request, use the same parameters and add `next_record_id`.
usage
[object]
Get the hourly usage attribution by tag(s).
hour
date-time
The hour for the usage.
org_name
string
The name of the organization.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
tag_config_source
string
The source of the usage attribution tag configuration and the selected tags in the format of `<source_org_name>:::<selected tag 1>///<selected tag 2>///<selected tag 3>`.
tags
object
Tag keys and values.
A `null` value here means that the requested tag breakdown cannot be applied because it does not match the [tags configured for usage attribution](https://docs.datadoghq.com/account_management/billing/usage_attribution/#getting-started). In this scenario the API returns the total usage, not broken down by tags.
<any-key>
[string]
A list of values that are associated with each tag key.
  * An empty list means the resource use wasn't tagged with the respective tag.
  * Multiple values means the respective tag was applied multiple times on the resource.
  * An `<empty>` value means the resource was tagged with the respective tag but did not have a value.


total_usage_sum
double
Total product usage for the given tags within the hour.
updated_at
string
Shows the most recent hour in the current month for all organizations where usages are calculated.
usage_type
enum
Supported products for hourly usage attribution requests. The following values have been **deprecated** : `estimated_indexed_spans_usage`, `estimated_ingested_spans_usage`. Allowed enum values: `api_usage,apm_fargate_usage,apm_host_usage,apm_usm_usage,appsec_fargate_usage,appsec_usage,asm_serverless_traced_invocations_usage,asm_serverless_traced_invocations_percentage,bits_ai_investigations_usage,browser_usage,ci_pipeline_indexed_spans_usage,ci_test_indexed_spans_usage,ci_visibility_itr_usage,cloud_siem_usage,code_security_host_usage,container_excl_agent_usage,container_usage,cspm_containers_usage,cspm_hosts_usage,custom_event_usage,custom_ingested_timeseries_usage,custom_timeseries_usage,cws_containers_usage,cws_fargate_task_usage,cws_hosts_usage,data_jobs_monitoring_usage,data_stream_monitoring_usage,dbm_hosts_usage,dbm_queries_usage,error_tracking_usage,error_tracking_percentage,estimated_indexed_spans_usage,estimated_ingested_spans_usage,fargate_usage,flex_stored_logs,functions_usage,incident_management_monthly_active_users_usage,indexed_spans_usage,infra_host_usage,ingested_logs_bytes_usage,ingested_spans_bytes_usage,invocations_usage,lambda_traced_invocations_usage,llm_observability_usage,llm_spans_usage,logs_indexed_15day_usage,logs_indexed_180day_usage,logs_indexed_1day_usage,logs_indexed_30day_usage,logs_indexed_360day_usage,logs_indexed_3day_usage,logs_indexed_45day_usage,logs_indexed_60day_usage,logs_indexed_7day_usage,logs_indexed_90day_usage,logs_indexed_custom_retention_usage,mobile_app_testing_usage,ndm_netflow_usage,npm_host_usage,network_device_wireless_usage,obs_pipeline_bytes_usage,obs_pipelines_vcpu_usage,online_archive_usage,product_analytics_session_usage,profiled_container_usage,profiled_fargate_usage,profiled_host_usage,published_app,rum_browser_mobile_sessions_usage,rum_ingested_usage,rum_investigate_usage,rum_replay_sessions_usage,rum_session_replay_add_on_usage,sca_fargate_usage,sds_scanned_bytes_usage,serverless_apps_usage,siem_analyzed_logs_add_on_usage,siem_ingested_bytes_usage,snmp_usage,universal_service_monitoring_usage,vuln_management_hosts_usage,workflow_executions_usage`
```
{
  "metadata": {
    "pagination": {
      "next_record_id": "string"
    }
  },
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string",
      "region": "string",
      "tag_config_source": "string",
      "tags": {
        "<any-key>": [
          "datadog-integrations-lab"
        ]
      },
      "total_usage_sum": "number",
      "updated_at": "string",
      "usage_type": "string"
    }
  ]
}
```

Copy
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage attribution
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
export usage_type="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/hourly-attribution?start_hr=${start_hr}&usage_type=${usage_type}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage attribution
```
"""
Get hourly usage attribution returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v1.model.hourly_usage_attribution_usage_type import HourlyUsageAttributionUsageType

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_hourly_usage_attribution(
        start_hr=(datetime.now() + relativedelta(days=-3)),
        usage_type=HourlyUsageAttributionUsageType.INFRA_HOST_USAGE,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage attribution
```
# Get hourly usage attribution returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_hourly_usage_attribution((Time.now + -3 * 86400), HourlyUsageAttributionUsageType::INFRA_HOST_USAGE)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage attribution
```
// Get hourly usage attribution returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetHourlyUsageAttribution(ctx, time.Now().AddDate(0, 0, -3), datadogV1.HOURLYUSAGEATTRIBUTIONUSAGETYPE_INFRA_HOST_USAGE, *datadogV1.NewGetHourlyUsageAttributionOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetHourlyUsageAttribution`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetHourlyUsageAttribution`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage attribution
```
// Get hourly usage attribution returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.HourlyUsageAttributionResponse;
import com.datadog.api.client.v1.model.HourlyUsageAttributionUsageType;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      HourlyUsageAttributionResponse result =
          apiInstance.getHourlyUsageAttribution(
              OffsetDateTime.now().plusDays(-3), HourlyUsageAttributionUsageType.INFRA_HOST_USAGE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getHourlyUsageAttribution");
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

#####  Get hourly usage attribution
```
// Get hourly usage attribution returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetHourlyUsageAttributionOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;
use datadog_api_client::datadogV1::model::HourlyUsageAttributionUsageType;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_hourly_usage_attribution(
            DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            HourlyUsageAttributionUsageType::INFRA_HOST_USAGE,
            GetHourlyUsageAttributionOptionalParams::default(),
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

#####  Get hourly usage attribution
```
/**
 * Get hourly usage attribution returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetHourlyUsageAttributionRequest = {
  startHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
  usageType: "infra_host_usage",
};

apiInstance
  .getHourlyUsageAttribution(params)
  .then((data: v1.HourlyUsageAttributionResponse) => {
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
## [Get monthly usage attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-monthly-usage-attribution)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-monthly-usage-attribution-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/monthly-attributionhttps://api.ap2.datadoghq.com/api/v1/usage/monthly-attributionhttps://api.datadoghq.eu/api/v1/usage/monthly-attributionhttps://api.ddog-gov.com/api/v1/usage/monthly-attributionhttps://api.datadoghq.com/api/v1/usage/monthly-attributionhttps://api.us3.datadoghq.com/api/v1/usage/monthly-attributionhttps://api.us5.datadoghq.com/api/v1/usage/monthly-attribution
### Overview
Get monthly usage attribution. Multi-region data is available starting March 1, 2023.
This API endpoint is paginated. To make sure you receive all records, check if the value of `next_record_id` is set in the response. If it is, make another request and pass `next_record_id` as a parameter. Pseudo code example:
```
response := GetMonthlyUsageAttribution(start_month)
cursor := response.metadata.pagination.next_record_id
WHILE cursor != null BEGIN
  sleep(5 seconds)  # Avoid running into rate limit
  response := GetMonthlyUsageAttribution(start_month, next_record_id=cursor)
  cursor := response.metadata.pagination.next_record_id
END

```

This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_month [_required_]
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage beginning in this month. Maximum of 15 months ago.
end_month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage ending this month.
fields [_required_]
enum
Comma-separated list of usage types to return, or `*` for all usage types. The following values have been **deprecated** : `estimated_indexed_spans_usage`, `estimated_indexed_spans_percentage`, `estimated_ingested_spans_usage`, `estimated_ingested_spans_percentage`, `llm_observability_usage`, `llm_observability_percentage`.  
Allowed enum values: `api_usage, api_percentage, apm_fargate_usage, apm_fargate_percentage, appsec_fargate_usage, appsec_fargate_percentage, apm_host_usage, apm_host_percentage, apm_usm_usage, apm_usm_percentage, appsec_usage, appsec_percentage, asm_serverless_traced_invocations_usage, asm_serverless_traced_invocations_percentage, bits_ai_investigations_usage, bits_ai_investigations_percentage, browser_usage, browser_percentage, ci_visibility_itr_usage, ci_visibility_itr_percentage, cloud_siem_usage, cloud_siem_percentage, code_security_host_usage, code_security_host_percentage, container_excl_agent_usage, container_excl_agent_percentage, container_usage, container_percentage, cspm_containers_percentage, cspm_containers_usage, cspm_hosts_percentage, cspm_hosts_usage, custom_timeseries_usage, custom_timeseries_percentage, custom_ingested_timeseries_usage, custom_ingested_timeseries_percentage, cws_containers_percentage, cws_containers_usage, cws_fargate_task_percentage, cws_fargate_task_usage, cws_hosts_percentage, cws_hosts_usage, data_jobs_monitoring_usage, data_jobs_monitoring_percentage, data_stream_monitoring_usage, data_stream_monitoring_percentage, dbm_hosts_percentage, dbm_hosts_usage, dbm_queries_percentage, dbm_queries_usage, error_tracking_usage, error_tracking_percentage, estimated_indexed_spans_usage, estimated_indexed_spans_percentage, estimated_ingested_spans_usage, estimated_ingested_spans_percentage, fargate_usage, fargate_percentage, flex_stored_logs_usage, flex_stored_logs_percentage, functions_usage, functions_percentage, incident_management_monthly_active_users_usage, incident_management_monthly_active_users_percentage, infra_host_usage, infra_host_percentage, invocations_usage, invocations_percentage, lambda_traced_invocations_usage, lambda_traced_invocations_percentage, llm_observability_usage, llm_observability_percentage, llm_spans_usage, llm_spans_percentage, mobile_app_testing_percentage, mobile_app_testing_usage, ndm_netflow_usage, ndm_netflow_percentage, network_device_wireless_usage, network_device_wireless_percentage, npm_host_usage, npm_host_percentage, obs_pipeline_bytes_usage, obs_pipeline_bytes_percentage, obs_pipelines_vcpu_usage, obs_pipelines_vcpu_percentage, online_archive_usage, online_archive_percentage, product_analytics_session_usage, product_analytics_session_percentage, profiled_container_usage, profiled_container_percentage, profiled_fargate_usage, profiled_fargate_percentage, profiled_host_usage, profiled_host_percentage, published_app_usage, published_app_percentage, serverless_apps_usage, serverless_apps_percentage, snmp_usage, snmp_percentage, universal_service_monitoring_usage, universal_service_monitoring_percentage, vuln_management_hosts_usage, vuln_management_hosts_percentage, sds_scanned_bytes_usage, sds_scanned_bytes_percentage, ci_test_indexed_spans_usage, ci_test_indexed_spans_percentage, ingested_logs_bytes_usage, ingested_logs_bytes_percentage, ci_pipeline_indexed_spans_usage, ci_pipeline_indexed_spans_percentage, indexed_spans_usage, indexed_spans_percentage, custom_event_usage, custom_event_percentage, logs_indexed_custom_retention_usage, logs_indexed_custom_retention_percentage, logs_indexed_360day_usage, logs_indexed_360day_percentage, logs_indexed_180day_usage, logs_indexed_180day_percentage, logs_indexed_90day_usage, logs_indexed_90day_percentage, logs_indexed_60day_usage, logs_indexed_60day_percentage, logs_indexed_45day_usage, logs_indexed_45day_percentage, logs_indexed_30day_usage, logs_indexed_30day_percentage, logs_indexed_15day_usage, logs_indexed_15day_percentage, logs_indexed_7day_usage, logs_indexed_7day_percentage, logs_indexed_3day_usage, logs_indexed_3day_percentage, logs_indexed_1day_usage, logs_indexed_1day_percentage, rum_ingested_usage, rum_ingested_percentage, rum_investigate_usage, rum_investigate_percentage, rum_replay_sessions_usage, rum_replay_sessions_percentage, rum_session_replay_add_on_usage, rum_session_replay_add_on_percentage, rum_browser_mobile_sessions_usage, rum_browser_mobile_sessions_percentage, ingested_spans_bytes_usage, ingested_spans_bytes_percentage, siem_analyzed_logs_add_on_usage, siem_analyzed_logs_add_on_percentage, siem_ingested_bytes_usage, siem_ingested_bytes_percentage, workflow_executions_usage, workflow_executions_percentage, sca_fargate_usage, sca_fargate_percentage, *`
sort_direction
enum
The direction to sort by: `[desc, asc]`.  
Allowed enum values: `desc, asc`
sort_name
enum
The field to sort by. The following values have been **deprecated** : `estimated_indexed_spans_usage`, `estimated_indexed_spans_percentage`, `estimated_ingested_spans_usage`, `estimated_ingested_spans_percentage`.  
Allowed enum values: `api_usage, api_percentage, apm_fargate_usage, apm_fargate_percentage, appsec_fargate_usage, appsec_fargate_percentage, apm_host_usage, apm_host_percentage, apm_usm_usage, apm_usm_percentage, appsec_usage, appsec_percentage, asm_serverless_traced_invocations_usage, asm_serverless_traced_invocations_percentage, bits_ai_investigations_usage, bits_ai_investigations_percentage, browser_usage, browser_percentage, ci_visibility_itr_usage, ci_visibility_itr_percentage, cloud_siem_usage, cloud_siem_percentage, code_security_host_usage, code_security_host_percentage, container_excl_agent_usage, container_excl_agent_percentage, container_usage, container_percentage, cspm_containers_percentage, cspm_containers_usage, cspm_hosts_percentage, cspm_hosts_usage, custom_timeseries_usage, custom_timeseries_percentage, custom_ingested_timeseries_usage, custom_ingested_timeseries_percentage, cws_containers_percentage, cws_containers_usage, cws_fargate_task_percentage, cws_fargate_task_usage, cws_hosts_percentage, cws_hosts_usage, data_jobs_monitoring_usage, data_jobs_monitoring_percentage, data_stream_monitoring_usage, data_stream_monitoring_percentage, dbm_hosts_percentage, dbm_hosts_usage, dbm_queries_percentage, dbm_queries_usage, error_tracking_usage, error_tracking_percentage, estimated_indexed_spans_usage, estimated_indexed_spans_percentage, estimated_ingested_spans_usage, estimated_ingested_spans_percentage, fargate_usage, fargate_percentage, flex_stored_logs_usage, flex_stored_logs_percentage, functions_usage, functions_percentage, incident_management_monthly_active_users_usage, incident_management_monthly_active_users_percentage, infra_host_usage, infra_host_percentage, invocations_usage, invocations_percentage, lambda_traced_invocations_usage, lambda_traced_invocations_percentage, llm_observability_usage, llm_observability_percentage, llm_spans_usage, llm_spans_percentage, mobile_app_testing_percentage, mobile_app_testing_usage, ndm_netflow_usage, ndm_netflow_percentage, network_device_wireless_usage, network_device_wireless_percentage, npm_host_usage, npm_host_percentage, obs_pipeline_bytes_usage, obs_pipeline_bytes_percentage, obs_pipelines_vcpu_usage, obs_pipelines_vcpu_percentage, online_archive_usage, online_archive_percentage, product_analytics_session_usage, product_analytics_session_percentage, profiled_container_usage, profiled_container_percentage, profiled_fargate_usage, profiled_fargate_percentage, profiled_host_usage, profiled_host_percentage, published_app_usage, published_app_percentage, serverless_apps_usage, serverless_apps_percentage, snmp_usage, snmp_percentage, universal_service_monitoring_usage, universal_service_monitoring_percentage, vuln_management_hosts_usage, vuln_management_hosts_percentage, sds_scanned_bytes_usage, sds_scanned_bytes_percentage, ci_test_indexed_spans_usage, ci_test_indexed_spans_percentage, ingested_logs_bytes_usage, ingested_logs_bytes_percentage, ci_pipeline_indexed_spans_usage, ci_pipeline_indexed_spans_percentage, indexed_spans_usage, indexed_spans_percentage, custom_event_usage, custom_event_percentage, logs_indexed_custom_retention_usage, logs_indexed_custom_retention_percentage, logs_indexed_360day_usage, logs_indexed_360day_percentage, logs_indexed_180day_usage, logs_indexed_180day_percentage, logs_indexed_90day_usage, logs_indexed_90day_percentage, logs_indexed_60day_usage, logs_indexed_60day_percentage, logs_indexed_45day_usage, logs_indexed_45day_percentage, logs_indexed_30day_usage, logs_indexed_30day_percentage, logs_indexed_15day_usage, logs_indexed_15day_percentage, logs_indexed_7day_usage, logs_indexed_7day_percentage, logs_indexed_3day_usage, logs_indexed_3day_percentage, logs_indexed_1day_usage, logs_indexed_1day_percentage, rum_ingested_usage, rum_ingested_percentage, rum_investigate_usage, rum_investigate_percentage, rum_replay_sessions_usage, rum_replay_sessions_percentage, rum_session_replay_add_on_usage, rum_session_replay_add_on_percentage, rum_browser_mobile_sessions_usage, rum_browser_mobile_sessions_percentage, ingested_spans_bytes_usage, ingested_spans_bytes_percentage, siem_analyzed_logs_add_on_usage, siem_analyzed_logs_add_on_percentage, siem_ingested_bytes_usage, siem_ingested_bytes_percentage, workflow_executions_usage, workflow_executions_percentage, sca_fargate_usage, sca_fargate_percentage, *`
tag_breakdown_keys
string
Comma separated list of tag keys used to group usage. If no value is provided the usage will not be broken down by tags.
To see which tags are available, look for the value of `tag_config_source` in the API response.
next_record_id
string
List following results with a next_record_id provided in the previous query.
include_descendants
boolean
Include child org usage in the response. Defaults to `true`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyUsageAttribution-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyUsageAttribution-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyUsageAttribution-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the monthly Usage Summary by tag(s).
Field
Type
Description
metadata
object
The object containing document metadata.
aggregates
[object]
An array of available aggregates.
agg_type
string
The aggregate type.
field
string
The field.
value
double
The value for a given field.
pagination
object
The metadata for the current pagination.
next_record_id
string
The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `next_record_id`.
usage
[object]
Get usage summary by tag(s).
month
date-time
Datetime in ISO-8601 format, UTC, precise to month: [YYYY-MM].
org_name
string
The name of the organization.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
tag_config_source
string
The source of the usage attribution tag configuration and the selected tags in the format `<source_org_name>:::<selected tag 1>///<selected tag 2>///<selected tag 3>`.
tags
object
Tag keys and values.
A `null` value here means that the requested tag breakdown cannot be applied because it does not match the [tags configured for usage attribution](https://docs.datadoghq.com/account_management/billing/usage_attribution/#getting-started). In this scenario the API returns the total usage, not broken down by tags.
<any-key>
[string]
A list of values that are associated with each tag key.
  * An empty list means the resource use wasn't tagged with the respective tag.
  * Multiple values means the respective tag was applied multiple times on the resource.
  * An `<empty>` value means the resource was tagged with the respective tag but did not have a value.


updated_at
date-time
Datetime of the most recent update to the usage values.
values
object
Fields in Usage Summary by tag(s). The following values have been **deprecated** : `estimated_indexed_spans_usage`, `estimated_indexed_spans_percentage`, `estimated_ingested_spans_usage`, `estimated_ingested_spans_percentage`.
api_percentage
double
The percentage of synthetic API test usage by tag(s).
api_usage
double
The synthetic API test usage by tag(s).
apm_fargate_percentage
double
The percentage of APM ECS Fargate task usage by tag(s).
apm_fargate_usage
double
The APM ECS Fargate task usage by tag(s).
apm_host_percentage
double
The percentage of APM host usage by tag(s).
apm_host_usage
double
The APM host usage by tag(s).
apm_usm_percentage
double
The percentage of APM and Universal Service Monitoring host usage by tag(s).
apm_usm_usage
double
The APM and Universal Service Monitoring host usage by tag(s).
appsec_fargate_percentage
double
The percentage of Application Security Monitoring ECS Fargate task usage by tag(s).
appsec_fargate_usage
double
The Application Security Monitoring ECS Fargate task usage by tag(s).
appsec_percentage
double
The percentage of Application Security Monitoring host usage by tag(s).
appsec_usage
double
The Application Security Monitoring host usage by tag(s).
asm_serverless_traced_invocations_percentage
double
The percentage of Application Security Monitoring Serverless traced invocations usage by tag(s).
asm_serverless_traced_invocations_usage
double
The Application Security Monitoring Serverless traced invocations usage by tag(s).
bits_ai_investigations_percentage
double
The percentage of Bits AI `SRE` investigation usage by tag(s).
bits_ai_investigations_usage
double
The Bits AI `SRE` investigation usage by tag(s).
browser_percentage
double
The percentage of synthetic browser test usage by tag(s).
browser_usage
double
The synthetic browser test usage by tag(s).
ci_pipeline_indexed_spans_percentage
double
The percentage of CI Pipeline Indexed Spans usage by tag(s).
ci_pipeline_indexed_spans_usage
double
The total CI Pipeline Indexed Spans usage by tag(s).
ci_test_indexed_spans_percentage
double
The percentage of CI Test Indexed Spans usage by tag(s).
ci_test_indexed_spans_usage
double
The total CI Test Indexed Spans usage by tag(s).
ci_visibility_itr_percentage
double
The percentage of Git committers for Intelligent Test Runner usage by tag(s).
ci_visibility_itr_usage
double
The Git committers for Intelligent Test Runner usage by tag(s).
cloud_siem_percentage
double
The percentage of Cloud Security Information and Event Management usage by tag(s).
cloud_siem_usage
double
The Cloud Security Information and Event Management usage by tag(s).
code_security_host_percentage
double
The percentage of Code Security host usage by tags.
code_security_host_usage
double
The Code Security host usage by tags.
container_excl_agent_percentage
double
The percentage of container usage without the Datadog Agent by tag(s).
container_excl_agent_usage
double
The container usage without the Datadog Agent by tag(s).
container_percentage
double
The percentage of container usage by tag(s).
container_usage
double
The container usage by tag(s).
cspm_containers_percentage
double
The percentage of Cloud Security Management Pro container usage by tag(s).
cspm_containers_usage
double
The Cloud Security Management Pro container usage by tag(s).
cspm_hosts_percentage
double
The percentage of Cloud Security Management Pro host usage by tag(s).
cspm_hosts_usage
double
The Cloud Security Management Pro host usage by tag(s).
custom_event_percentage
double
The percentage of Custom Events usage by tag(s).
custom_event_usage
double
The total Custom Events usage by tag(s).
custom_ingested_timeseries_percentage
double
The percentage of ingested custom metrics usage by tag(s).
custom_ingested_timeseries_usage
double
The ingested custom metrics usage by tag(s).
custom_timeseries_percentage
double
The percentage of indexed custom metrics usage by tag(s).
custom_timeseries_usage
double
The indexed custom metrics usage by tag(s).
cws_containers_percentage
double
The percentage of Cloud Workload Security container usage by tag(s).
cws_containers_usage
double
The Cloud Workload Security container usage by tag(s).
cws_fargate_task_percentage
double
The percentage of Cloud Workload Security Fargate task usage by tag(s).
cws_fargate_task_usage
double
The Cloud Workload Security Fargate task usage by tag(s).
cws_hosts_percentage
double
The percentage of Cloud Workload Security host usage by tag(s).
cws_hosts_usage
double
The Cloud Workload Security host usage by tag(s).
data_jobs_monitoring_usage
double
The Data Jobs Monitoring usage by tag(s).
data_stream_monitoring_usage
double
The Data Stream Monitoring usage by tag(s).
dbm_hosts_percentage
double
The percentage of Database Monitoring host usage by tag(s).
dbm_hosts_usage
double
The Database Monitoring host usage by tag(s).
dbm_queries_percentage
double
The percentage of Database Monitoring queries usage by tag(s).
dbm_queries_usage
double
The Database Monitoring queries usage by tag(s).
error_tracking_percentage
double
The percentage of error tracking events usage by tag(s).
error_tracking_usage
double
The error tracking events usage by tag(s).
estimated_indexed_spans_percentage
double
The percentage of estimated indexed spans usage by tag(s).
estimated_indexed_spans_usage
double
The estimated indexed spans usage by tag(s).
estimated_ingested_spans_percentage
double
The percentage of estimated ingested spans usage by tag(s).
estimated_ingested_spans_usage
double
The estimated ingested spans usage by tag(s).
fargate_percentage
double
The percentage of Fargate usage by tags.
fargate_usage
double
The Fargate usage by tags.
flex_stored_logs_percentage
double
The percentage of Flex Stored Logs usage by tags.
flex_stored_logs_usage
double
The Flex Stored Logs usage by tags.
functions_percentage
double
The percentage of Lambda function usage by tag(s).
functions_usage
double
The Lambda function usage by tag(s).
incident_management_monthly_active_users_percentage
double
The percentage of Incident Management monthly active users usage by tag(s).
incident_management_monthly_active_users_usage
double
The Incident Management monthly active users usage by tag(s).
indexed_spans_percentage
double
The percentage of APM Indexed Spans usage by tag(s).
indexed_spans_usage
double
The total APM Indexed Spans usage by tag(s).
infra_host_percentage
double
The percentage of infrastructure host usage by tag(s).
infra_host_usage
double
The infrastructure host usage by tag(s).
ingested_logs_bytes_percentage
double
The percentage of Ingested Logs usage by tag(s).
ingested_logs_bytes_usage
double
The total Ingested Logs usage by tag(s).
ingested_spans_bytes_percentage
double
The percentage of APM Ingested Spans usage by tag(s).
ingested_spans_bytes_usage
double
The total APM Ingested Spans usage by tag(s).
invocations_percentage
double
The percentage of Lambda invocation usage by tag(s).
invocations_usage
double
The Lambda invocation usage by tag(s).
lambda_traced_invocations_percentage
double
The percentage of Serverless APM usage by tag(s).
lambda_traced_invocations_usage
double
The Serverless APM usage by tag(s).
llm_observability_percentage
double
The percentage of LLM Observability usage by tag(s).
llm_observability_usage
double
The LLM Observability usage by tag(s).
llm_spans_percentage
double
The percentage of LLM Spans usage by tag(s).
llm_spans_usage
double
The LLM Spans usage by tag(s).
logs_indexed_15day_percentage
double
The percentage of Indexed Logs (15-day Retention) usage by tag(s).
logs_indexed_15day_usage
double
The total Indexed Logs (15-day Retention) usage by tag(s).
logs_indexed_180day_percentage
double
The percentage of Indexed Logs (180-day Retention) usage by tag(s).
logs_indexed_180day_usage
double
The total Indexed Logs (180-day Retention) usage by tag(s).
logs_indexed_1day_percentage
double
The percentage of Indexed Logs (1-day Retention) usage by tag(s).
logs_indexed_1day_usage
double
The total Indexed Logs (1-day Retention) usage by tag(s).
logs_indexed_30day_percentage
double
The percentage of Indexed Logs (30-day Retention) usage by tag(s).
logs_indexed_30day_usage
double
The total Indexed Logs (30-day Retention) usage by tag(s).
logs_indexed_360day_percentage
double
The percentage of Indexed Logs (360-day Retention) usage by tag(s).
logs_indexed_360day_usage
double
The total Indexed Logs (360-day Retention) usage by tag(s).
logs_indexed_3day_percentage
double
The percentage of Indexed Logs (3-day Retention) usage by tag(s).
logs_indexed_3day_usage
double
The total Indexed Logs (3-day Retention) usage by tag(s).
logs_indexed_45day_percentage
double
The percentage of Indexed Logs (45-day Retention) usage by tag(s).
logs_indexed_45day_usage
double
The total Indexed Logs (45-day Retention) usage by tag(s).
logs_indexed_60day_percentage
double
The percentage of Indexed Logs (60-day Retention) usage by tag(s).
logs_indexed_60day_usage
double
The total Indexed Logs (60-day Retention) usage by tag(s).
logs_indexed_7day_percentage
double
The percentage of Indexed Logs (7-day Retention) usage by tag(s).
logs_indexed_7day_usage
double
The total Indexed Logs (7-day Retention) usage by tag(s).
logs_indexed_90day_percentage
double
The percentage of Indexed Logs (90-day Retention) usage by tag(s).
logs_indexed_90day_usage
double
The total Indexed Logs (90-day Retention) usage by tag(s).
logs_indexed_custom_retention_percentage
double
The percentage of Indexed Logs (Custom Retention) usage by tag(s).
logs_indexed_custom_retention_usage
double
The total Indexed Logs (Custom Retention) usage by tag(s).
mobile_app_testing_percentage
double
The percentage of Synthetic mobile application test usage by tag(s).
mobile_app_testing_usage
double
The Synthetic mobile application test usage by tag(s).
ndm_netflow_percentage
double
The percentage of Network Device Monitoring NetFlow usage by tag(s).
ndm_netflow_usage
double
The Network Device Monitoring NetFlow usage by tag(s).
network_device_wireless_percentage
double
The percentage of network device wireless usage by tag(s).
network_device_wireless_usage
double
The network device wireless usage by tag(s).
npm_host_percentage
double
The percentage of network host usage by tag(s).
npm_host_usage
double
The network host usage by tag(s).
obs_pipeline_bytes_percentage
double
The percentage of observability pipeline bytes usage by tag(s).
obs_pipeline_bytes_usage
double
The observability pipeline bytes usage by tag(s).
obs_pipelines_vcpu_percentage
double
The percentage of observability pipeline per core usage by tag(s).
obs_pipelines_vcpu_usage
double
The observability pipeline per core usage by tag(s).
online_archive_percentage
double
The percentage of online archive usage by tag(s).
online_archive_usage
double
The online archive usage by tag(s).
product_analytics_session_percentage
double
The percentage of Product Analytics session usage by tag(s).
product_analytics_session_usage
double
The Product Analytics session usage by tag(s).
profiled_container_percentage
double
The percentage of profiled container usage by tag(s).
profiled_container_usage
double
The profiled container usage by tag(s).
profiled_fargate_percentage
double
The percentage of profiled Fargate task usage by tag(s).
profiled_fargate_usage
double
The profiled Fargate task usage by tag(s).
profiled_host_percentage
double
The percentage of profiled hosts usage by tag(s).
profiled_host_usage
double
The profiled hosts usage by tag(s).
published_app_percentage
double
The percentage of published application usage by tag(s).
published_app_usage
double
The published application usage by tag(s).
rum_browser_mobile_sessions_percentage
double
The percentage of RUM Browser and Mobile usage by tag(s).
rum_browser_mobile_sessions_usage
double
The total RUM Browser and Mobile usage by tag(s).
rum_ingested_percentage
double
The percentage of RUM Ingested usage by tag(s).
rum_ingested_usage
double
The total RUM Ingested usage by tag(s).
rum_investigate_percentage
double
The percentage of RUM Investigate usage by tag(s).
rum_investigate_usage
double
The total RUM Investigate usage by tag(s).
rum_replay_sessions_percentage
double
The percentage of RUM Session Replay usage by tag(s).
rum_replay_sessions_usage
double
The total RUM Session Replay usage by tag(s).
rum_session_replay_add_on_percentage
double
The percentage of RUM Session Replay Add-On usage by tag(s).
rum_session_replay_add_on_usage
double
The total RUM Session Replay Add-On usage by tag(s).
sca_fargate_percentage
double
The percentage of Software Composition Analysis Fargate task usage by tag(s).
sca_fargate_usage
double
The total Software Composition Analysis Fargate task usage by tag(s).
sds_scanned_bytes_percentage
double
The percentage of Sensitive Data Scanner usage by tag(s).
sds_scanned_bytes_usage
double
The total Sensitive Data Scanner usage by tag(s).
serverless_apps_percentage
double
The percentage of Serverless Apps usage by tag(s).
serverless_apps_usage
double
The total Serverless Apps usage by tag(s).
siem_analyzed_logs_add_on_percentage
double
The percentage of log events analyzed by Cloud SIEM usage by tag(s).
siem_analyzed_logs_add_on_usage
double
The log events analyzed by Cloud SIEM usage by tag(s).
siem_ingested_bytes_percentage
double
The percentage of SIEM usage by tag(s).
siem_ingested_bytes_usage
double
The total SIEM usage by tag(s).
snmp_percentage
double
The percentage of network device usage by tag(s).
snmp_usage
double
The network device usage by tag(s).
universal_service_monitoring_percentage
double
The percentage of universal service monitoring usage by tag(s).
universal_service_monitoring_usage
double
The universal service monitoring usage by tag(s).
vuln_management_hosts_percentage
double
The percentage of Application Vulnerability Management usage by tag(s).
vuln_management_hosts_usage
double
The Application Vulnerability Management usage by tag(s).
workflow_executions_percentage
double
The percentage of workflow executions usage by tag(s).
workflow_executions_usage
double
The total workflow executions usage by tag(s).
```
{
  "metadata": {
    "aggregates": [
      {
        "agg_type": "sum",
        "field": "custom_timeseries_usage",
        "value": "number"
      }
    ],
    "pagination": {
      "next_record_id": "string"
    }
  },
  "usage": [
    {
      "month": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string",
      "region": "string",
      "tag_config_source": "string",
      "tags": {
        "<any-key>": [
          "datadog-integrations-lab"
        ]
      },
      "updated_at": "2019-09-19T10:00:00.000Z",
      "values": {
        "api_percentage": "number",
        "api_usage": "number",
        "apm_fargate_percentage": "number",
        "apm_fargate_usage": "number",
        "apm_host_percentage": "number",
        "apm_host_usage": "number",
        "apm_usm_percentage": "number",
        "apm_usm_usage": "number",
        "appsec_fargate_percentage": "number",
        "appsec_fargate_usage": "number",
        "appsec_percentage": "number",
        "appsec_usage": "number",
        "asm_serverless_traced_invocations_percentage": "number",
        "asm_serverless_traced_invocations_usage": "number",
        "bits_ai_investigations_percentage": "number",
        "bits_ai_investigations_usage": "number",
        "browser_percentage": "number",
        "browser_usage": "number",
        "ci_pipeline_indexed_spans_percentage": "number",
        "ci_pipeline_indexed_spans_usage": "number",
        "ci_test_indexed_spans_percentage": "number",
        "ci_test_indexed_spans_usage": "number",
        "ci_visibility_itr_percentage": "number",
        "ci_visibility_itr_usage": "number",
        "cloud_siem_percentage": "number",
        "cloud_siem_usage": "number",
        "code_security_host_percentage": "number",
        "code_security_host_usage": "number",
        "container_excl_agent_percentage": "number",
        "container_excl_agent_usage": "number",
        "container_percentage": "number",
        "container_usage": "number",
        "cspm_containers_percentage": "number",
        "cspm_containers_usage": "number",
        "cspm_hosts_percentage": "number",
        "cspm_hosts_usage": "number",
        "custom_event_percentage": "number",
        "custom_event_usage": "number",
        "custom_ingested_timeseries_percentage": "number",
        "custom_ingested_timeseries_usage": "number",
        "custom_timeseries_percentage": "number",
        "custom_timeseries_usage": "number",
        "cws_containers_percentage": "number",
        "cws_containers_usage": "number",
        "cws_fargate_task_percentage": "number",
        "cws_fargate_task_usage": "number",
        "cws_hosts_percentage": "number",
        "cws_hosts_usage": "number",
        "data_jobs_monitoring_usage": "number",
        "data_stream_monitoring_usage": "number",
        "dbm_hosts_percentage": "number",
        "dbm_hosts_usage": "number",
        "dbm_queries_percentage": "number",
        "dbm_queries_usage": "number",
        "error_tracking_percentage": "number",
        "error_tracking_usage": "number",
        "estimated_indexed_spans_percentage": "number",
        "estimated_indexed_spans_usage": "number",
        "estimated_ingested_spans_percentage": "number",
        "estimated_ingested_spans_usage": "number",
        "fargate_percentage": "number",
        "fargate_usage": "number",
        "flex_stored_logs_percentage": "number",
        "flex_stored_logs_usage": "number",
        "functions_percentage": "number",
        "functions_usage": "number",
        "incident_management_monthly_active_users_percentage": "number",
        "incident_management_monthly_active_users_usage": "number",
        "indexed_spans_percentage": "number",
        "indexed_spans_usage": "number",
        "infra_host_percentage": "number",
        "infra_host_usage": "number",
        "ingested_logs_bytes_percentage": "number",
        "ingested_logs_bytes_usage": "number",
        "ingested_spans_bytes_percentage": "number",
        "ingested_spans_bytes_usage": "number",
        "invocations_percentage": "number",
        "invocations_usage": "number",
        "lambda_traced_invocations_percentage": "number",
        "lambda_traced_invocations_usage": "number",
        "llm_observability_percentage": "number",
        "llm_observability_usage": "number",
        "llm_spans_percentage": "number",
        "llm_spans_usage": "number",
        "logs_indexed_15day_percentage": "number",
        "logs_indexed_15day_usage": "number",
        "logs_indexed_180day_percentage": "number",
        "logs_indexed_180day_usage": "number",
        "logs_indexed_1day_percentage": "number",
        "logs_indexed_1day_usage": "number",
        "logs_indexed_30day_percentage": "number",
        "logs_indexed_30day_usage": "number",
        "logs_indexed_360day_percentage": "number",
        "logs_indexed_360day_usage": "number",
        "logs_indexed_3day_percentage": "number",
        "logs_indexed_3day_usage": "number",
        "logs_indexed_45day_percentage": "number",
        "logs_indexed_45day_usage": "number",
        "logs_indexed_60day_percentage": "number",
        "logs_indexed_60day_usage": "number",
        "logs_indexed_7day_percentage": "number",
        "logs_indexed_7day_usage": "number",
        "logs_indexed_90day_percentage": "number",
        "logs_indexed_90day_usage": "number",
        "logs_indexed_custom_retention_percentage": "number",
        "logs_indexed_custom_retention_usage": "number",
        "mobile_app_testing_percentage": "number",
        "mobile_app_testing_usage": "number",
        "ndm_netflow_percentage": "number",
        "ndm_netflow_usage": "number",
        "network_device_wireless_percentage": "number",
        "network_device_wireless_usage": "number",
        "npm_host_percentage": "number",
        "npm_host_usage": "number",
        "obs_pipeline_bytes_percentage": "number",
        "obs_pipeline_bytes_usage": "number",
        "obs_pipelines_vcpu_percentage": "number",
        "obs_pipelines_vcpu_usage": "number",
        "online_archive_percentage": "number",
        "online_archive_usage": "number",
        "product_analytics_session_percentage": "number",
        "product_analytics_session_usage": "number",
        "profiled_container_percentage": "number",
        "profiled_container_usage": "number",
        "profiled_fargate_percentage": "number",
        "profiled_fargate_usage": "number",
        "profiled_host_percentage": "number",
        "profiled_host_usage": "number",
        "published_app_percentage": "number",
        "published_app_usage": "number",
        "rum_browser_mobile_sessions_percentage": "number",
        "rum_browser_mobile_sessions_usage": "number",
        "rum_ingested_percentage": "number",
        "rum_ingested_usage": "number",
        "rum_investigate_percentage": "number",
        "rum_investigate_usage": "number",
        "rum_replay_sessions_percentage": "number",
        "rum_replay_sessions_usage": "number",
        "rum_session_replay_add_on_percentage": "number",
        "rum_session_replay_add_on_usage": "number",
        "sca_fargate_percentage": "number",
        "sca_fargate_usage": "number",
        "sds_scanned_bytes_percentage": "number",
        "sds_scanned_bytes_usage": "number",
        "serverless_apps_percentage": "number",
        "serverless_apps_usage": "number",
        "siem_analyzed_logs_add_on_percentage": "number",
        "siem_analyzed_logs_add_on_usage": "number",
        "siem_ingested_bytes_percentage": "number",
        "siem_ingested_bytes_usage": "number",
        "snmp_percentage": "number",
        "snmp_usage": "number",
        "universal_service_monitoring_percentage": "number",
        "universal_service_monitoring_usage": "number",
        "vuln_management_hosts_percentage": "number",
        "vuln_management_hosts_usage": "number",
        "workflow_executions_percentage": "number",
        "workflow_executions_usage": "number"
      }
    }
  ]
}
```

Copy
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get monthly usage attribution
Copy
```
                  # Required query arguments  
export start_month="CHANGE_ME"  
export fields="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/monthly-attribution?start_month=${start_month}&fields=${fields}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get monthly usage attribution
```
"""
Get monthly usage attribution returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v1.model.monthly_usage_attribution_supported_metrics import (
    MonthlyUsageAttributionSupportedMetrics,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_monthly_usage_attribution(
        start_month=(datetime.now() + relativedelta(days=-3)),
        fields=MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_USAGE,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get monthly usage attribution
```
# Get monthly usage attribution returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_monthly_usage_attribution((Time.now + -3 * 86400), MonthlyUsageAttributionSupportedMetrics::INFRA_HOST_USAGE)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get monthly usage attribution
```
// Get monthly usage attribution returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetMonthlyUsageAttribution(ctx, time.Now().AddDate(0, 0, -3), datadogV1.MONTHLYUSAGEATTRIBUTIONSUPPORTEDMETRICS_INFRA_HOST_USAGE, *datadogV1.NewGetMonthlyUsageAttributionOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetMonthlyUsageAttribution`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetMonthlyUsageAttribution`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get monthly usage attribution
```
// Get monthly usage attribution returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.MonthlyUsageAttributionResponse;
import com.datadog.api.client.v1.model.MonthlyUsageAttributionSupportedMetrics;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      MonthlyUsageAttributionResponse result =
          apiInstance.getMonthlyUsageAttribution(
              OffsetDateTime.now().plusDays(-3),
              MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_USAGE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getMonthlyUsageAttribution");
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

#####  Get monthly usage attribution
```
// Get monthly usage attribution returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetMonthlyUsageAttributionOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;
use datadog_api_client::datadogV1::model::MonthlyUsageAttributionSupportedMetrics;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_monthly_usage_attribution(
            DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            MonthlyUsageAttributionSupportedMetrics::INFRA_HOST_USAGE,
            GetMonthlyUsageAttributionOptionalParams::default(),
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

#####  Get monthly usage attribution
```
/**
 * Get monthly usage attribution returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetMonthlyUsageAttributionRequest = {
  startMonth: new Date(new Date().getTime() + -3 * 86400 * 1000),
  fields: "infra_host_usage",
};

apiInstance
  .getMonthlyUsageAttribution(params)
  .then((data: v1.MonthlyUsageAttributionResponse) => {
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
## [Get active billing dimensions for cost attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-active-billing-dimensions-for-cost-attribution)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-active-billing-dimensions-for-cost-attribution-v2)


GET https://api.ap1.datadoghq.com/api/v2/cost_by_tag/active_billing_dimensionshttps://api.ap2.datadoghq.com/api/v2/cost_by_tag/active_billing_dimensionshttps://api.datadoghq.eu/api/v2/cost_by_tag/active_billing_dimensionshttps://api.ddog-gov.com/api/v2/cost_by_tag/active_billing_dimensionshttps://api.datadoghq.com/api/v2/cost_by_tag/active_billing_dimensionshttps://api.us3.datadoghq.com/api/v2/cost_by_tag/active_billing_dimensionshttps://api.us5.datadoghq.com/api/v2/cost_by_tag/active_billing_dimensions
### Overview
Get active billing dimensions for cost attribution. Cost data for a given month becomes available no later than the 19th of the following month. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetActiveBillingDimensions-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetActiveBillingDimensions-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetActiveBillingDimensions-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetActiveBillingDimensions-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Active billing dimensions response.
Field
Type
Description
data
object
Active billing dimensions data.
attributes
object
List of active billing dimensions.
month
date-time
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]`.
values
[string]
List of active billing dimensions. Example: `[infra_host, apm_host, serverless_infra]`.
id
string
Unique ID of the response.
type
enum
Type of active billing dimensions data. Allowed enum values: `billing_dimensions`
default: `billing_dimensions`
```
{
  "data": {
    "attributes": {
      "month": "2019-09-19T10:00:00.000Z",
      "values": [
        "infra_host"
      ]
    },
    "id": "string",
    "type": "string"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get active billing dimensions for cost attribution
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost_by_tag/active_billing_dimensions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get active billing dimensions for cost attribution
```
"""
Get active billing dimensions for cost attribution returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_active_billing_dimensions()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get active billing dimensions for cost attribution
```
# Get active billing dimensions for cost attribution returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
p api_instance.get_active_billing_dimensions()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get active billing dimensions for cost attribution
```
// Get active billing dimensions for cost attribution returns "OK" response

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
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetActiveBillingDimensions(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetActiveBillingDimensions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetActiveBillingDimensions`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get active billing dimensions for cost attribution
```
// Get active billing dimensions for cost attribution returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.model.ActiveBillingDimensionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      ActiveBillingDimensionsResponse result = apiInstance.getActiveBillingDimensions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getActiveBillingDimensions");
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

#####  Get active billing dimensions for cost attribution
```
// Get active billing dimensions for cost attribution returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api.get_active_billing_dimensions().await;
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

#####  Get active billing dimensions for cost attribution
```
/**
 * Get active billing dimensions for cost attribution returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

apiInstance
  .getActiveBillingDimensions()
  .then((data: v2.ActiveBillingDimensionsResponse) => {
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
## [Get billable usage across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-billable-usage-across-your-account)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-billable-usage-across-your-account-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/billable-summaryhttps://api.ap2.datadoghq.com/api/v1/usage/billable-summaryhttps://api.datadoghq.eu/api/v1/usage/billable-summaryhttps://api.ddog-gov.com/api/v1/usage/billable-summaryhttps://api.datadoghq.com/api/v1/usage/billable-summaryhttps://api.us3.datadoghq.com/api/v1/usage/billable-summaryhttps://api.us5.datadoghq.com/api/v1/usage/billable-summary
### Overview
Get billable usage across your account.
This endpoint is only accessible for [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/).
This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage starting this month.
include_connected_accounts
boolean
Boolean to specify whether to include accounts connected to the current account as partner customers in the Datadog partner network program. Defaults to `false`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageBillableSummary-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageBillableSummary-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageBillableSummary-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageBillableSummary-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response with monthly summary of data billed by Datadog.
Field
Type
Description
usage
[object]
An array of objects regarding usage of billable summary.
account_name
string
The account name.
account_public_id
string
The account public ID.
billing_plan
string
The billing plan.
end_date
date-time
Shows the last date of usage.
num_orgs
int64
The number of organizations.
org_name
string
The organization name.
public_id
string
The organization public ID.
ratio_in_month
double
Shows usage aggregation for a billing period.
region
string
The region of the organization.
start_date
date-time
Shows the first date of usage.
usage
object
Response with aggregated usage types.
apm_fargate_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
apm_fargate_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
apm_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
apm_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
apm_profiler_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
apm_profiler_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
apm_trace_search_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
application_security_fargate_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
application_security_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
application_security_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ci_pipeline_indexed_spans_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ci_pipeline_maximum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ci_pipeline_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ci_test_indexed_spans_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ci_testing_maximum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ci_testing_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cloud_cost_management_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cloud_cost_management_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cspm_container_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cspm_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cspm_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
custom_event_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cws_container_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cws_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
cws_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
dbm_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
dbm_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
dbm_normalized_queries_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
dbm_normalized_queries_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
fargate_container_apm_and_profiler_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
fargate_container_apm_and_profiler_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
fargate_container_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
fargate_container_profiler_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
fargate_container_profiler_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
fargate_container_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
incident_management_maximum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
incident_management_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
infra_and_apm_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
infra_and_apm_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
infra_container_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
infra_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
infra_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ingested_spans_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ingested_timeseries_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
ingested_timeseries_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
iot_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
iot_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
lambda_function_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
lambda_function_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_forwarding_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_15day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_180day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_1day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_30day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_360day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_3day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_45day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_60day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_7day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_90day_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_custom_retention_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_indexed_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
logs_ingested_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
network_device_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
network_device_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
npm_flow_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
npm_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
npm_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
observability_pipeline_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
online_archive_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
prof_container_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
prof_host_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
prof_host_top99p
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
rum_lite_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
rum_replay_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
rum_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
rum_units_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
sensitive_data_scanner_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
serverless_apm_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
serverless_infra_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
serverless_infra_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
serverless_invocation_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
siem_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
standard_timeseries_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
synthetics_api_tests_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
synthetics_app_testing_maximum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
synthetics_browser_checks_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
timeseries_average
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
timeseries_sum
object
Response with properties for each aggregated usage type.
account_billable_usage
int64
The total account usage.
account_committed_usage
int64
The total account committed usage.
account_on_demand_usage
int64
The total account on-demand usage.
elapsed_usage_hours
int64
Elapsed usage hours for some billable product.
first_billable_usage_hour
date-time
The first billable hour for the org.
last_billable_usage_hour
date-time
The last billable hour for the org.
org_billable_usage
int64
The number of units used within the billable timeframe.
percentage_in_account
double
The percentage of account usage the org represents.
usage_unit
string
Units pertaining to the usage.
```
{
  "usage": [
    {
      "account_name": "string",
      "account_public_id": "string",
      "billing_plan": "string",
      "end_date": "2019-09-19T10:00:00.000Z",
      "num_orgs": "integer",
      "org_name": "string",
      "public_id": "string",
      "ratio_in_month": "number",
      "region": "string",
      "start_date": "2019-09-19T10:00:00.000Z",
      "usage": {
        "apm_fargate_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "apm_fargate_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "apm_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "apm_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "apm_profiler_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "apm_profiler_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "apm_trace_search_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "application_security_fargate_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "application_security_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "application_security_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ci_pipeline_indexed_spans_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ci_pipeline_maximum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ci_pipeline_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ci_test_indexed_spans_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ci_testing_maximum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ci_testing_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cloud_cost_management_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cloud_cost_management_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cspm_container_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cspm_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cspm_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "custom_event_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cws_container_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cws_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "cws_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "dbm_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "dbm_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "dbm_normalized_queries_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "dbm_normalized_queries_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "fargate_container_apm_and_profiler_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "fargate_container_apm_and_profiler_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "fargate_container_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "fargate_container_profiler_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "fargate_container_profiler_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "fargate_container_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "incident_management_maximum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "incident_management_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "infra_and_apm_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "infra_and_apm_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "infra_container_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "infra_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "infra_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ingested_spans_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ingested_timeseries_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "ingested_timeseries_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "iot_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "iot_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "lambda_function_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "lambda_function_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_forwarding_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_15day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_180day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_1day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_30day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_360day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_3day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_45day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_60day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_7day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_90day_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_custom_retention_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_indexed_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "logs_ingested_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "network_device_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "network_device_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "npm_flow_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "npm_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "npm_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "observability_pipeline_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "online_archive_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "prof_container_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "prof_host_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "prof_host_top99p": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "rum_lite_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "rum_replay_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "rum_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "rum_units_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "sensitive_data_scanner_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "serverless_apm_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "serverless_infra_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "serverless_infra_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "serverless_invocation_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "siem_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "standard_timeseries_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "synthetics_api_tests_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "synthetics_app_testing_maximum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "synthetics_browser_checks_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "timeseries_average": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        },
        "timeseries_sum": {
          "account_billable_usage": "integer",
          "account_committed_usage": "integer",
          "account_on_demand_usage": "integer",
          "elapsed_usage_hours": "integer",
          "first_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "last_billable_usage_hour": "2019-09-19T10:00:00.000Z",
          "org_billable_usage": "integer",
          "percentage_in_account": "number",
          "usage_unit": "string"
        }
      }
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get billable usage across your account
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/billable-summary" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get billable usage across your account
```
"""
Get billable usage across your account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_billable_summary()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get billable usage across your account
```
# Get billable usage across your account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_billable_summary()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get billable usage across your account
```
// Get billable usage across your account returns "OK" response

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
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageBillableSummary(ctx, *datadogV1.NewGetUsageBillableSummaryOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageBillableSummary`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageBillableSummary`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get billable usage across your account
```
// Get billable usage across your account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageBillableSummaryResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageBillableSummaryResponse result = apiInstance.getUsageBillableSummary();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageBillableSummary");
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

#####  Get billable usage across your account
```
// Get billable usage across your account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageBillableSummaryOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_billable_summary(GetUsageBillableSummaryOptionalParams::default())
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

#####  Get billable usage across your account
```
/**
 * Get billable usage across your account returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

apiInstance
  .getUsageBillableSummary()
  .then((data: v1.UsageBillableSummaryResponse) => {
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
## [Get historical cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-historical-cost-across-your-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-historical-cost-across-your-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/historical_costhttps://api.ap2.datadoghq.com/api/v2/usage/historical_costhttps://api.datadoghq.eu/api/v2/usage/historical_costhttps://api.ddog-gov.com/api/v2/usage/historical_costhttps://api.datadoghq.com/api/v2/usage/historical_costhttps://api.us3.datadoghq.com/api/v2/usage/historical_costhttps://api.us5.datadoghq.com/api/v2/usage/historical_cost
### Overview
Get historical cost across multi-org and single root-org accounts. Cost data for a given month becomes available no later than the 16th of the following month.
This endpoint is only accessible for [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/).
This endpoint requires all of the following permissions:
* `usage_read`
* `billing_read`
  

OAuth apps require the `usage_read, billing_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_month [_required_]
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost beginning this month.
view
string
String to specify whether cost is broken down at a parent-org level or at the sub-org level. Available views are `summary` and `sub-org`. Defaults to `summary`.
end_month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost ending this month.
include_connected_accounts
boolean
Boolean to specify whether to include accounts connected to the current account as partner customers in the Datadog partner network program. Defaults to `false`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetHistoricalCostByOrg-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetHistoricalCostByOrg-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetHistoricalCostByOrg-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetHistoricalCostByOrg-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Chargeback Summary response.
Field
Type
Description
data
[object]
Response containing Chargeback Summary.
attributes
object
Cost attributes data.
account_name
string
The account name.
account_public_id
string
The account public ID.
charges
[object]
List of charges data reported for the requested month.
charge_type
string
The type of charge for a particular product.
cost
double
The cost for a particular product and charge type during a given month.
product_name
string
The product for which cost is being reported.
date
date-time
The month requested.
org_name
string
The organization name.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
total_cost
double
The total cost of products for the month.
id
string
Unique ID of the response.
type
enum
Type of cost data. Allowed enum values: `cost_by_org`
default: `cost_by_org`
```
{
  "data": [
    {
      "attributes": {
        "account_name": "string",
        "account_public_id": "string",
        "charges": [
          {
            "charge_type": "on_demand",
            "cost": "number",
            "product_name": "infra_host"
          }
        ],
        "date": "2019-09-19T10:00:00.000Z",
        "org_name": "string",
        "public_id": "string",
        "region": "string",
        "total_cost": "number"
      },
      "id": "string",
      "type": "cost_by_org"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get historical cost across your account
Copy
```
                  # Required query arguments  
export start_month="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/historical_cost?start_month=${start_month}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get historical cost across your account
```
"""
Get historical cost across your account returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_historical_cost_by_org(
        start_month=(datetime.now() + relativedelta(months=-2)),
        view="sub-org",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get historical cost across your account
```
# Get historical cost across your account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
opts = {
  view: "sub-org",
}
p api_instance.get_historical_cost_by_org((Time.now + -2 * 86400 * 30), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get historical cost across your account
```
// Get historical cost across your account returns "OK" response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetHistoricalCostByOrg(ctx, time.Now().AddDate(0, -2, 0), *datadogV2.NewGetHistoricalCostByOrgOptionalParameters().WithView("sub-org"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetHistoricalCostByOrg`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetHistoricalCostByOrg`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get historical cost across your account
```
// Get historical cost across your account returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.api.UsageMeteringApi.GetHistoricalCostByOrgOptionalParameters;
import com.datadog.api.client.v2.model.CostByOrgResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      CostByOrgResponse result =
          apiInstance.getHistoricalCostByOrg(
              OffsetDateTime.now().plusMonths(-2),
              new GetHistoricalCostByOrgOptionalParameters().view("sub-org"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getHistoricalCostByOrg");
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

#####  Get historical cost across your account
```
// Get historical cost across your account returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetHistoricalCostByOrgOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_historical_cost_by_org(
            DateTime::parse_from_rfc3339("2021-09-11T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetHistoricalCostByOrgOptionalParams::default().view("sub-org".to_string()),
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

#####  Get historical cost across your account
```
/**
 * Get historical cost across your account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetHistoricalCostByOrgRequest = {
  startMonth: new Date(new Date().getTime() + -2 * 86400 * 30 * 1000),
  view: "sub-org",
};

apiInstance
  .getHistoricalCostByOrg(params)
  .then((data: v2.CostByOrgResponse) => {
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
## [Get Monthly Cost Attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-monthly-cost-attribution)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-monthly-cost-attribution-v2)


GET https://api.ap1.datadoghq.com/api/v2/cost_by_tag/monthly_cost_attributionhttps://api.ap2.datadoghq.com/api/v2/cost_by_tag/monthly_cost_attributionhttps://api.datadoghq.eu/api/v2/cost_by_tag/monthly_cost_attributionhttps://api.ddog-gov.com/api/v2/cost_by_tag/monthly_cost_attributionhttps://api.datadoghq.com/api/v2/cost_by_tag/monthly_cost_attributionhttps://api.us3.datadoghq.com/api/v2/cost_by_tag/monthly_cost_attributionhttps://api.us5.datadoghq.com/api/v2/cost_by_tag/monthly_cost_attribution
### Overview
Get monthly cost attribution by tag across multi-org and single root-org accounts. Cost Attribution data for a given month becomes available no later than the 19th of the following month. This API endpoint is paginated. To make sure you receive all records, check if the value of `next_record_id` is set in the response. If it is, make another request and pass `next_record_id` as a parameter. Pseudo code example:
```
response := GetMonthlyCostAttribution(start_month, end_month)
cursor := response.metadata.pagination.next_record_id
WHILE cursor != null BEGIN
  sleep(5 seconds)  # Avoid running into rate limit
  response := GetMonthlyCostAttribution(start_month, end_month, next_record_id=cursor)
  cursor := response.metadata.pagination.next_record_id
END

```

This endpoint is only accessible for [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/). This endpoint is not available in the Government (US1-FED) site.
This endpoint requires all of the following permissions:
* `usage_read`
* `billing_read`
  

OAuth apps require the `usage_read, billing_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_month [_required_]
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost beginning in this month.
end_month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost ending this month.
fields [_required_]
string
Comma-separated list specifying cost types (e.g., `<billing_dimension>_on_demand_cost`, `<billing_dimension>_committed_cost`, `<billing_dimension>_total_cost`) and the proportions (`<billing_dimension>_percentage_in_org`, `<billing_dimension>_percentage_in_account`). Use `*` to retrieve all fields. Example: `infra_host_on_demand_cost,infra_host_percentage_in_account` To obtain the complete list of active billing dimensions that can be used to replace `<billing_dimension>` in the field names, make a request to the [Get active billing dimensions API](https://docs.datadoghq.com/api/latest/usage-metering/#get-active-billing-dimensions-for-cost-attribution).
sort_direction
enum
The direction to sort by: `[desc, asc]`.  
Allowed enum values: `desc, asc`
sort_name
string
The billing dimension to sort by. Always sorted by total cost. Example: `infra_host`.
tag_breakdown_keys
string
Comma separated list of tag keys used to group cost. If no value is provided the cost will not be broken down by tags. To see which tags are available, look for the value of `tag_config_source` in the API response.
next_record_id
string
List following results with a next_record_id provided in the previous query.
include_descendants
boolean
Include child org cost in the response. Defaults to `true`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyCostAttribution-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyCostAttribution-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyCostAttribution-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyCostAttribution-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the monthly cost attribution by tag(s).
Field
Type
Description
data
[object]
Response containing cost attribution.
attributes
object
Cost Attribution by Tag for a given organization.
month
date-time
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]`.
org_name
string
The name of the organization.
public_id
string
The organization public ID.
tag_config_source
string
The source of the cost attribution tag configuration and the selected tags in the format `<source_org_name>:::<selected tag 1>///<selected tag 2>///<selected tag 3>`.
tags
object
Tag keys and values. A `null` value here means that the requested tag breakdown cannot be applied because it does not match the [tags configured for usage attribution](https://docs.datadoghq.com/account_management/billing/usage_attribution/#getting-started). In this scenario the API returns the total cost, not broken down by tags.
<any-key>
[string]
A list of values that are associated with each tag key.
  * An empty list means the resource use wasn't tagged with the respective tag.
  * Multiple values means the respective tag was applied multiple times on the resource.
  * An `<empty>` value means the resource was tagged with the respective tag but did not have a value.


updated_at
string
Shows the most recent hour in the current months for all organizations for which all costs were calculated.
values
object
Fields in Cost Attribution by tag(s). Example: `infra_host_on_demand_cost`, `infra_host_committed_cost`, `infra_host_total_cost`, `infra_host_percentage_in_org`, `infra_host_percentage_in_account`.
id
string
Unique ID of the response.
type
enum
Type of cost attribution data. Allowed enum values: `cost_by_tag`
default: `cost_by_tag`
meta
object
The object containing document metadata.
aggregates
[object]
An array of available aggregates.
agg_type
string
The aggregate type.
field
string
The field.
value
double
The value for a given field.
pagination
object
The metadata for the current pagination.
next_record_id
string
The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `next_record_id`.
```
{
  "data": [
    {
      "attributes": {
        "month": "2019-09-19T10:00:00.000Z",
        "org_name": "string",
        "public_id": "string",
        "tag_config_source": "string",
        "tags": {
          "<any-key>": [
            "datadog-integrations-lab"
          ]
        },
        "updated_at": "string",
        "values": {}
      },
      "id": "string",
      "type": "cost_by_tag"
    }
  ],
  "meta": {
    "aggregates": [
      {
        "agg_type": "sum",
        "field": "infra_host_committed_cost",
        "value": "number"
      }
    ],
    "pagination": {
      "next_record_id": "string"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get Monthly Cost Attribution
Copy
```
                  # Required query arguments  
export start_month="CHANGE_ME"  
export fields="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost_by_tag/monthly_cost_attribution?start_month=${start_month}&fields=${fields}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Monthly Cost Attribution
```
"""
Get Monthly Cost Attribution returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_monthly_cost_attribution(
        start_month=(datetime.now() + relativedelta(days=-5)),
        end_month=(datetime.now() + relativedelta(days=-3)),
        fields="infra_host_total_cost",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get Monthly Cost Attribution
```
# Get Monthly Cost Attribution returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
opts = {
  end_month: (Time.now + -3 * 86400),
}
p api_instance.get_monthly_cost_attribution((Time.now + -5 * 86400), "infra_host_total_cost", opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get Monthly Cost Attribution
```
// Get Monthly Cost Attribution returns "OK" response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetMonthlyCostAttribution(ctx, time.Now().AddDate(0, 0, -5), "infra_host_total_cost", *datadogV2.NewGetMonthlyCostAttributionOptionalParameters().WithEndMonth(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetMonthlyCostAttribution`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetMonthlyCostAttribution`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get Monthly Cost Attribution
```
// Get Monthly Cost Attribution returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.api.UsageMeteringApi.GetMonthlyCostAttributionOptionalParameters;
import com.datadog.api.client.v2.model.MonthlyCostAttributionResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      MonthlyCostAttributionResponse result =
          apiInstance.getMonthlyCostAttribution(
              OffsetDateTime.now().plusDays(-5),
              "infra_host_total_cost",
              new GetMonthlyCostAttributionOptionalParameters()
                  .endMonth(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getMonthlyCostAttribution");
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

#####  Get Monthly Cost Attribution
```
// Get Monthly Cost Attribution returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetMonthlyCostAttributionOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_monthly_cost_attribution(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            "infra_host_total_cost".to_string(),
            GetMonthlyCostAttributionOptionalParams::default().end_month(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get Monthly Cost Attribution
```
/**
 * Get Monthly Cost Attribution returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetMonthlyCostAttributionRequest = {
  startMonth: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endMonth: new Date(new Date().getTime() + -3 * 86400 * 1000),
  fields: "infra_host_total_cost",
};

apiInstance
  .getMonthlyCostAttribution(params)
  .then((data: v2.MonthlyCostAttributionResponse) => {
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
## [Get estimated cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-estimated-cost-across-your-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-estimated-cost-across-your-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/estimated_costhttps://api.ap2.datadoghq.com/api/v2/usage/estimated_costhttps://api.datadoghq.eu/api/v2/usage/estimated_costhttps://api.ddog-gov.com/api/v2/usage/estimated_costhttps://api.datadoghq.com/api/v2/usage/estimated_costhttps://api.us3.datadoghq.com/api/v2/usage/estimated_costhttps://api.us5.datadoghq.com/api/v2/usage/estimated_cost
### Overview
Get estimated cost across multi-org and single root-org accounts. Estimated cost data is only available for the current month and previous month and is delayed by up to 72 hours from when it was incurred. To access historical costs prior to this, use the `/historical_cost` endpoint.
This endpoint is only accessible for [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/).
This endpoint requires all of the following permissions:
* `usage_read`
* `billing_read`
  

OAuth apps require the `usage_read, billing_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
view
string
String to specify whether cost is broken down at a parent-org level or at the sub-org level. Available views are `summary` and `sub-org`. Defaults to `summary`.
start_month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost beginning this month. **Either start_month or start_date should be specified, but not both.** (start_month cannot go beyond two months in the past). Provide an `end_month` to view month-over-month cost.
end_month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost ending this month.
start_date
string
Datetime in ISO-8601 format, UTC, precise to day: `[YYYY-MM-DD]` for cost beginning this day. **Either start_month or start_date should be specified, but not both.** (start_date cannot go beyond two months in the past). Provide an `end_date` to view day-over-day cumulative cost.
end_date
string
Datetime in ISO-8601 format, UTC, precise to day: `[YYYY-MM-DD]` for cost ending this day.
include_connected_accounts
boolean
Boolean to specify whether to include accounts connected to the current account as partner customers in the Datadog partner network program. Defaults to `false`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetEstimatedCostByOrg-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetEstimatedCostByOrg-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetEstimatedCostByOrg-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetEstimatedCostByOrg-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Chargeback Summary response.
Field
Type
Description
data
[object]
Response containing Chargeback Summary.
attributes
object
Cost attributes data.
account_name
string
The account name.
account_public_id
string
The account public ID.
charges
[object]
List of charges data reported for the requested month.
charge_type
string
The type of charge for a particular product.
cost
double
The cost for a particular product and charge type during a given month.
product_name
string
The product for which cost is being reported.
date
date-time
The month requested.
org_name
string
The organization name.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
total_cost
double
The total cost of products for the month.
id
string
Unique ID of the response.
type
enum
Type of cost data. Allowed enum values: `cost_by_org`
default: `cost_by_org`
```
{
  "data": [
    {
      "attributes": {
        "account_name": "string",
        "account_public_id": "string",
        "charges": [
          {
            "charge_type": "on_demand",
            "cost": "number",
            "product_name": "infra_host"
          }
        ],
        "date": "2019-09-19T10:00:00.000Z",
        "org_name": "string",
        "public_id": "string",
        "region": "string",
        "total_cost": "number"
      },
      "id": "string",
      "type": "cost_by_org"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get estimated cost across your account
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/estimated_cost" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get estimated cost across your account
```
"""
Get estimated cost across your account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_estimated_cost_by_org()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get estimated cost across your account
```
# Get estimated cost across your account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
p api_instance.get_estimated_cost_by_org()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get estimated cost across your account
```
// Get estimated cost across your account returns "OK" response

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
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetEstimatedCostByOrg(ctx, *datadogV2.NewGetEstimatedCostByOrgOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetEstimatedCostByOrg`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetEstimatedCostByOrg`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get estimated cost across your account
```
// Get estimated cost across your account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.model.CostByOrgResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      CostByOrgResponse result = apiInstance.getEstimatedCostByOrg();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getEstimatedCostByOrg");
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

#####  Get estimated cost across your account
```
// Get estimated cost across your account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetEstimatedCostByOrgOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_estimated_cost_by_org(GetEstimatedCostByOrgOptionalParams::default())
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

#####  Get estimated cost across your account
```
/**
 * Get estimated cost across your account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

apiInstance
  .getEstimatedCostByOrg()
  .then((data: v2.CostByOrgResponse) => {
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
## [Get all custom metrics by hourly average](https://docs.datadoghq.com/api/latest/usage-metering/#get-all-custom-metrics-by-hourly-average)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-all-custom-metrics-by-hourly-average-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/top_avg_metricshttps://api.ap2.datadoghq.com/api/v1/usage/top_avg_metricshttps://api.datadoghq.eu/api/v1/usage/top_avg_metricshttps://api.ddog-gov.com/api/v1/usage/top_avg_metricshttps://api.datadoghq.com/api/v1/usage/top_avg_metricshttps://api.us3.datadoghq.com/api/v1/usage/top_avg_metricshttps://api.us5.datadoghq.com/api/v1/usage/top_avg_metrics
### Overview
Get all [custom metrics](https://docs.datadoghq.com/developers/metrics/custom_metrics/) by hourly average. Use the month parameter to get a month-to-date data resolution or use the day parameter to get a daily resolution. One of the two is required, and only one of the two is allowed. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
month
string
Datetime in ISO-8601 format, UTC, precise to month: [YYYY-MM] for usage beginning at this hour. (Either month or day should be specified, but not both)
day
string
Datetime in ISO-8601 format, UTC, precise to day: [YYYY-MM-DD] for usage beginning at this hour. (Either month or day should be specified, but not both)
names
array
Comma-separated list of metric names.
limit
integer
Maximum number of results to return (between 1 and 5000) - defaults to 500 results if limit not specified.
next_record_id
string
List following results with a next_record_id provided in the previous query.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTopAvgMetrics-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTopAvgMetrics-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTopAvgMetrics-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTopAvgMetrics-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of hourly recorded custom metrics for a given organization.
Field
Type
Description
metadata
object
The object containing document metadata.
day
date-time
The day value from the user request that contains the returned usage data. (If day was used the request)
month
date-time
The month value from the user request that contains the returned usage data. (If month was used the request)
pagination
object
The metadata for the current pagination.
limit
int64
Maximum amount of records to be returned.
next_record_id
string
The cursor to get the next results (if any). To make the next request, use the same parameters and add `next_record_id`.
total_number_of_records
int64
Total number of records.
usage
[object]
Number of hourly recorded custom metrics for a given organization.
avg_metric_hour
int64
Average number of timeseries per hour in which the metric occurs.
max_metric_hour
int64
Maximum number of timeseries per hour in which the metric occurs.
metric_category
enum
Contains the metric category. Allowed enum values: `standard,custom`
metric_name
string
Contains the custom metric name.
```
{
  "metadata": {
    "day": "2019-09-19T10:00:00.000Z",
    "month": "2019-09-19T10:00:00.000Z",
    "pagination": {
      "limit": "integer",
      "next_record_id": "string",
      "total_number_of_records": "integer"
    }
  },
  "usage": [
    {
      "avg_metric_hour": "integer",
      "max_metric_hour": "integer",
      "metric_category": "string",
      "metric_name": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get all custom metrics by hourly average
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/top_avg_metrics" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all custom metrics by hourly average
```
"""
Get all custom metrics by hourly average returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_top_avg_metrics(
        day=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all custom metrics by hourly average
```
# Get all custom metrics by hourly average returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  day: (Time.now + -3 * 86400),
}
p api_instance.get_usage_top_avg_metrics(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all custom metrics by hourly average
```
// Get all custom metrics by hourly average returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageTopAvgMetrics(ctx, *datadogV1.NewGetUsageTopAvgMetricsOptionalParameters().WithDay(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageTopAvgMetrics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageTopAvgMetrics`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all custom metrics by hourly average
```
// Get all custom metrics by hourly average returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageTopAvgMetricsOptionalParameters;
import com.datadog.api.client.v1.model.UsageTopAvgMetricsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageTopAvgMetricsResponse result =
          apiInstance.getUsageTopAvgMetrics(
              new GetUsageTopAvgMetricsOptionalParameters().day(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageTopAvgMetrics");
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

#####  Get all custom metrics by hourly average
```
// Get all custom metrics by hourly average returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageTopAvgMetricsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_top_avg_metrics(
            GetUsageTopAvgMetricsOptionalParams::default().day(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get all custom metrics by hourly average
```
/**
 * Get all custom metrics by hourly average returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageTopAvgMetricsRequest = {
  day: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageTopAvgMetrics(params)
  .then((data: v1.UsageTopAvgMetricsResponse) => {
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
## [Get projected cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-projected-cost-across-your-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-projected-cost-across-your-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/projected_costhttps://api.ap2.datadoghq.com/api/v2/usage/projected_costhttps://api.datadoghq.eu/api/v2/usage/projected_costhttps://api.ddog-gov.com/api/v2/usage/projected_costhttps://api.datadoghq.com/api/v2/usage/projected_costhttps://api.us3.datadoghq.com/api/v2/usage/projected_costhttps://api.us5.datadoghq.com/api/v2/usage/projected_cost
### Overview
Get projected cost across multi-org and single root-org accounts. Projected cost data is only available for the current month and becomes available around the 12th of the month.
This endpoint is only accessible for [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/).
This endpoint requires all of the following permissions:
* `usage_read`
* `billing_read`
  

OAuth apps require the `usage_read, billing_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
view
string
String to specify whether cost is broken down at a parent-org level or at the sub-org level. Available views are `summary` and `sub-org`. Defaults to `summary`.
include_connected_accounts
boolean
Boolean to specify whether to include accounts connected to the current account as partner customers in the Datadog partner network program. Defaults to `false`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetProjectedCost-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetProjectedCost-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetProjectedCost-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetProjectedCost-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Projected Cost response.
Field
Type
Description
data
[object]
Response containing Projected Cost.
attributes
object
Projected Cost attributes data.
account_name
string
The account name.
account_public_id
string
The account public ID.
charges
[object]
List of charges data reported for the requested month.
charge_type
string
The type of charge for a particular product.
cost
double
The cost for a particular product and charge type during a given month.
product_name
string
The product for which cost is being reported.
date
date-time
The month requested.
org_name
string
The organization name.
projected_total_cost
double
The total projected cost of products for the month.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
id
string
Unique ID of the response.
type
enum
Type of cost data. Allowed enum values: `projected_cost`
default: `projected_cost`
```
{
  "data": [
    {
      "attributes": {
        "account_name": "string",
        "account_public_id": "string",
        "charges": [
          {
            "charge_type": "on_demand",
            "cost": "number",
            "product_name": "infra_host"
          }
        ],
        "date": "2019-09-19T10:00:00.000Z",
        "org_name": "string",
        "projected_total_cost": "number",
        "public_id": "string",
        "region": "string"
      },
      "id": "string",
      "type": "projected_cost"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get projected cost across your account
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/projected_cost" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get projected cost across your account
```
"""
Get projected cost across your account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_projected_cost(
        view="sub-org",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get projected cost across your account
```
# Get projected cost across your account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
opts = {
  view: "sub-org",
}
p api_instance.get_projected_cost(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get projected cost across your account
```
// Get projected cost across your account returns "OK" response

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
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetProjectedCost(ctx, *datadogV2.NewGetProjectedCostOptionalParameters().WithView("sub-org"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetProjectedCost`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetProjectedCost`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get projected cost across your account
```
// Get projected cost across your account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.api.UsageMeteringApi.GetProjectedCostOptionalParameters;
import com.datadog.api.client.v2.model.ProjectedCostResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      ProjectedCostResponse result =
          apiInstance.getProjectedCost(new GetProjectedCostOptionalParameters().view("sub-org"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getProjectedCost");
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

#####  Get projected cost across your account
```
// Get projected cost across your account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetProjectedCostOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_projected_cost(GetProjectedCostOptionalParams::default().view("sub-org".to_string()))
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

#####  Get projected cost across your account
```
/**
 * Get projected cost across your account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetProjectedCostRequest = {
  view: "sub-org",
};

apiInstance
  .getProjectedCost(params)
  .then((data: v2.ProjectedCostResponse) => {
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
## [Get usage across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-usage-across-your-account)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-usage-across-your-account-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/summaryhttps://api.ap2.datadoghq.com/api/v1/usage/summaryhttps://api.datadoghq.eu/api/v1/usage/summaryhttps://api.ddog-gov.com/api/v1/usage/summaryhttps://api.datadoghq.com/api/v1/usage/summaryhttps://api.us3.datadoghq.com/api/v1/usage/summaryhttps://api.us5.datadoghq.com/api/v1/usage/summary
### Overview
Get all usage across your account.
This endpoint is only accessible for [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/).
This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_month [_required_]
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage beginning in this month. Maximum of 15 months ago.
end_month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage ending this month.
include_org_details
boolean
Include usage summaries for each sub-org.
include_connected_accounts
boolean
Boolean to specify whether to include accounts connected to the current account as partner customers in the Datadog partner network program. Defaults to `false`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSummary-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSummary-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSummary-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSummary-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response summarizing all usage aggregated across the months in the request for all organizations, and broken down by month and by organization.
Field
Type
Description
agent_host_top99p_sum
int64
Shows the 99th percentile of all agent hosts over all hours in the current month for all organizations.
apm_azure_app_service_host_top99p_sum
int64
Shows the 99th percentile of all Azure app services using APM over all hours in the current month all organizations.
apm_devsecops_host_top99p_sum
int64
Shows the 99th percentile of all APM DevSecOps hosts over all hours in the current month for all organizations.
apm_enterprise_standalone_hosts_top99p_sum
int64
Shows the sum of the 99th percentile of all distinct standalone Enterprise hosts over all hours in the current month for all organizations.
apm_fargate_count_avg_sum
int64
Shows the average of all APM ECS Fargate tasks over all hours in the current month for all organizations.
apm_host_top99p_sum
int64
Shows the 99th percentile of all distinct APM hosts over all hours in the current month for all organizations.
apm_pro_standalone_hosts_top99p_sum
int64
Shows the sum of the 99th percentile of all distinct standalone Pro hosts over all hours in the current month for all organizations.
appsec_fargate_count_avg_sum
int64
Shows the average of all Application Security Monitoring ECS Fargate tasks over all hours in the current month for all organizations.
asm_serverless_agg_sum
int64
Shows the sum of all Application Security Monitoring Serverless invocations over all hours in the current months for all organizations.
audit_logs_lines_indexed_agg_sum
int64
**DEPRECATED** : Shows the sum of all audit logs lines indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
audit_trail_enabled_hwm_sum
int64
Shows the total number of organizations that had Audit Trail enabled over a specific number of months.
avg_profiled_fargate_tasks_sum
int64
The average total count for Fargate Container Profiler over all hours in the current month for all organizations.
aws_host_top99p_sum
int64
Shows the 99th percentile of all AWS hosts over all hours in the current month for all organizations.
aws_lambda_func_count
int64
Shows the average of the number of functions that executed 1 or more times each hour in the current month for all organizations.
aws_lambda_invocations_sum
int64
Shows the sum of all AWS Lambda invocations over all hours in the current month for all organizations.
azure_app_service_top99p_sum
int64
Shows the 99th percentile of all Azure app services over all hours in the current month for all organizations.
azure_host_top99p_sum
int64
Shows the 99th percentile of all Azure hosts over all hours in the current month for all organizations.
billable_ingested_bytes_agg_sum
int64
Shows the sum of all log bytes ingested over all hours in the current month for all organizations.
bits_ai_investigations_agg_sum
int64
Shows the sum of all Bits AI Investigations over all hours in the current month for all organizations.
browser_rum_lite_session_count_agg_sum
int64
**DEPRECATED** : Shows the sum of all browser lite sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
browser_rum_replay_session_count_agg_sum
int64
Shows the sum of all browser replay sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
browser_rum_units_agg_sum
int64
**DEPRECATED** : Shows the sum of all browser RUM units over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
ci_pipeline_indexed_spans_agg_sum
int64
Shows the sum of all CI pipeline indexed spans over all hours in the current month for all organizations.
ci_test_indexed_spans_agg_sum
int64
Shows the sum of all CI test indexed spans over all hours in the current month for all organizations.
ci_visibility_itr_committers_hwm_sum
int64
Shows the high-water mark of all CI visibility intelligent test runner committers over all hours in the current month for all organizations.
ci_visibility_pipeline_committers_hwm_sum
int64
Shows the high-water mark of all CI visibility pipeline committers over all hours in the current month for all organizations.
ci_visibility_test_committers_hwm_sum
int64
Shows the high-water mark of all CI visibility test committers over all hours in the current month for all organizations.
cloud_cost_management_aws_host_count_avg_sum
int64
Sum of the host count average for Cloud Cost Management for AWS.
cloud_cost_management_azure_host_count_avg_sum
int64
Sum of the host count average for Cloud Cost Management for Azure.
cloud_cost_management_gcp_host_count_avg_sum
int64
Sum of the host count average for Cloud Cost Management for GCP.
cloud_cost_management_host_count_avg_sum
int64
Sum of the host count average for Cloud Cost Management for all cloud providers.
cloud_cost_management_oci_host_count_avg_sum
int64
Sum of the average host counts for Cloud Cost Management on OCI.
cloud_siem_events_agg_sum
int64
Shows the sum of all Cloud Security Information and Event Management events over all hours in the current month for all organizations.
code_analysis_sa_committers_hwm_sum
int64
Shows the high-water mark of all Static Analysis committers over all hours in the current month for all organizations.
code_analysis_sca_committers_hwm_sum
int64
Shows the high-water mark of all static Software Composition Analysis committers over all hours in the current month for all organizations.
code_security_host_top99p_sum
int64
Shows the 99th percentile of all Code Security hosts over all hours in the current month for all organizations.
container_avg_sum
int64
Shows the average of all distinct containers over all hours in the current month for all organizations.
container_excl_agent_avg_sum
int64
Shows the average of the containers without the Datadog Agent over all hours in the current month for all organizations.
container_hwm_sum
int64
Shows the sum of the high-water marks of all distinct containers over all hours in the current month for all organizations.
csm_container_enterprise_compliance_count_agg_sum
int64
Shows the sum of all Cloud Security Management Enterprise compliance containers over all hours in the current month for all organizations.
csm_container_enterprise_cws_count_agg_sum
int64
Shows the sum of all Cloud Security Management Enterprise Cloud Workload Security containers over all hours in the current month for all organizations.
csm_container_enterprise_total_count_agg_sum
int64
Shows the sum of all Cloud Security Management Enterprise containers over all hours in the current month for all organizations.
csm_host_enterprise_aas_host_count_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Azure app services hosts over all hours in the current month for all organizations.
csm_host_enterprise_aws_host_count_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Enterprise AWS hosts over all hours in the current month for all organizations.
csm_host_enterprise_azure_host_count_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Azure hosts over all hours in the current month for all organizations.
csm_host_enterprise_compliance_host_count_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Enterprise compliance hosts over all hours in the current month for all organizations.
csm_host_enterprise_cws_host_count_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Cloud Workload Security hosts over all hours in the current month for all organizations.
csm_host_enterprise_gcp_host_count_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Enterprise GCP hosts over all hours in the current month for all organizations.
csm_host_enterprise_total_host_count_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Enterprise hosts over all hours in the current month for all organizations.
cspm_aas_host_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Pro Azure app services hosts over all hours in the current month for all organizations.
cspm_aws_host_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Pro AWS hosts over all hours in the current month for all organizations.
cspm_azure_host_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Pro Azure hosts over all hours in the current month for all organizations.
cspm_container_avg_sum
int64
Shows the average number of Cloud Security Management Pro containers over all hours in the current month for all organizations.
cspm_container_hwm_sum
int64
Shows the sum of the high-water marks of Cloud Security Management Pro containers over all hours in the current month for all organizations.
cspm_gcp_host_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Pro GCP hosts over all hours in the current month for all organizations.
cspm_host_top99p_sum
int64
Shows the 99th percentile of all Cloud Security Management Pro hosts over all hours in the current month for all organizations.
custom_historical_ts_sum
int64
Shows the average number of distinct historical custom metrics over all hours in the current month for all organizations.
custom_live_ts_sum
int64
Shows the average number of distinct live custom metrics over all hours in the current month for all organizations.
custom_ts_sum
int64
Shows the average number of distinct custom metrics over all hours in the current month for all organizations.
cws_container_avg_sum
int64
Shows the average of all distinct Cloud Workload Security containers over all hours in the current month for all organizations.
cws_fargate_task_avg_sum
int64
Shows the average of all distinct Cloud Workload Security Fargate tasks over all hours in the current month for all organizations.
cws_host_top99p_sum
int64
Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current month for all organizations.
data_jobs_monitoring_host_hr_agg_sum
int64
Shows the sum of Data Jobs Monitoring hosts over all hours in the current months for all organizations
dbm_host_top99p_sum
int64
Shows the 99th percentile of all Database Monitoring hosts over all hours in the current month for all organizations.
dbm_queries_avg_sum
int64
Shows the average of all distinct Database Monitoring Normalized Queries over all hours in the current month for all organizations.
end_date
date-time
Shows the last date of usage in the current month for all organizations.
eph_infra_host_agent_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts with the Datadog Agent over all hours in the current month for all organizations.
eph_infra_host_alibaba_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Alibaba over all hours in the current month for all organizations.
eph_infra_host_aws_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts on AWS over all hours in the current month for all organizations.
eph_infra_host_azure_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Azure over all hours in the current month for all organizations.
eph_infra_host_ent_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Enterprise over all hours in the current month for all organizations.
eph_infra_host_gcp_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts on GCP over all hours in the current month for all organizations.
eph_infra_host_heroku_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Heroku over all hours in the current month for all organizations.
eph_infra_host_only_aas_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts with only Azure App Services over all hours in the current month for all organizations.
eph_infra_host_only_vsphere_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts with only vSphere over all hours in the current month for all organizations.
eph_infra_host_opentelemetry_agg_sum
int64
Shows the sum of all ephemeral hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
eph_infra_host_opentelemetry_apm_agg_sum
int64
Shows the sum of all ephemeral APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
eph_infra_host_pro_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Pro over all hours in the current month for all organizations.
eph_infra_host_proplus_agg_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Pro Plus over all hours in the current month for all organizations.
eph_infra_host_proxmox_agg_sum
int64
Sum of all ephemeral infrastructure hosts for Proxmox over all hours in the current month for all organizations.
error_tracking_apm_error_events_agg_sum
int64
Shows the sum of all Error Tracking APM error events over all hours in the current month for all organizations.
error_tracking_error_events_agg_sum
int64
Shows the sum of all Error Tracking error events over all hours in the current month for all organizations.
error_tracking_events_agg_sum
int64
Shows the sum of all Error Tracking events over all hours in the current months for all organizations.
error_tracking_rum_error_events_agg_sum
int64
Shows the sum of all Error Tracking RUM error events over all hours in the current month for all organizations.
event_management_correlation_agg_sum
int64
Shows the sum of all Event Management correlations over all hours in the current month for all organizations.
event_management_correlation_correlated_events_agg_sum
int64
Shows the sum of all Event Management correlated events over all hours in the current month for all organizations.
event_management_correlation_correlated_related_events_agg_sum
int64
Shows the sum of all Event Management correlated related events over all hours in the current month for all organizations.
fargate_container_profiler_profiling_fargate_avg_sum
int64
The average number of Profiling Fargate tasks over all hours in the current month for all organizations.
fargate_container_profiler_profiling_fargate_eks_avg_sum
int64
The average number of Profiling Fargate Elastic Kubernetes Service tasks over all hours in the current month for all organizations.
fargate_tasks_count_avg_sum
int64
Shows the average of all Fargate tasks over all hours in the current month for all organizations.
fargate_tasks_count_hwm_sum
int64
Shows the sum of the high-water marks of all Fargate tasks over all hours in the current month for all organizations.
flex_logs_compute_large_avg_sum
int64
Shows the average number of Flex Logs Compute Large Instances over all hours in the current months for all organizations.
flex_logs_compute_medium_avg_sum
int64
Shows the average number of Flex Logs Compute Medium Instances over all hours in the current months for all organizations.
flex_logs_compute_small_avg_sum
int64
Shows the average number of Flex Logs Compute Small Instances over all hours in the current months for all organizations.
flex_logs_compute_xlarge_avg_sum
int64
Shows the average number of Flex Logs Compute Extra Large Instances over all hours in the current months for all organizations.
flex_logs_compute_xsmall_avg_sum
int64
Shows the average number of Flex Logs Compute Extra Small Instances over all hours in the current months for all organizations.
flex_logs_starter_avg_sum
int64
Shows the average number of Flex Logs Starter Instances over all hours in the current months for all organizations.
flex_logs_starter_storage_index_avg_sum
int64
Shows the average number of Flex Logs Starter Storage Index Instances over all hours in the current months for all organizations.
flex_logs_starter_storage_retention_adjustment_avg_sum
int64
Shows the average number of Flex Logs Starter Storage Retention Adjustment Instances over all hours in the current months for all organizations.
flex_stored_logs_avg_sum
int64
Shows the average of all Flex Stored Logs over all hours in the current months for all organizations.
forwarding_events_bytes_agg_sum
int64
Shows the sum of all logs forwarding bytes over all hours in the current month for all organizations (data available as of April 1, 2023)
gcp_host_top99p_sum
int64
Shows the 99th percentile of all GCP hosts over all hours in the current month for all organizations.
heroku_host_top99p_sum
int64
Shows the 99th percentile of all Heroku dynos over all hours in the current month for all organizations.
incident_management_monthly_active_users_hwm_sum
int64
Shows sum of the high-water marks of incident management monthly active users in the current month for all organizations.
incident_management_seats_hwm_sum
int64
Shows the sum of the high-water marks of Incident Management seats over all hours in the current month for all organizations.
indexed_events_count_agg_sum
int64
**DEPRECATED** : Shows the sum of all log events indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
infra_host_top99p_sum
int64
Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current month for all organizations.
ingested_events_bytes_agg_sum
int64
Shows the sum of all log bytes ingested over all hours in the current month for all organizations.
iot_device_agg_sum
int64
Shows the sum of all IoT devices over all hours in the current month for all organizations.
iot_device_top99p_sum
int64
Shows the 99th percentile of all IoT devices over all hours in the current month of all organizations.
last_updated
date-time
Shows the most recent hour in the current month for all organizations for which all usages were calculated.
live_indexed_events_agg_sum
int64
**DEPRECATED** : Shows the sum of all live logs indexed over all hours in the current month for all organization (To be deprecated on October 1st, 2024).
live_ingested_bytes_agg_sum
int64
Shows the sum of all live logs bytes ingested over all hours in the current month for all organizations (data available as of December 1, 2020).
llm_observability_agg_sum
int64
Sum of all LLM observability sessions for all hours in the current month for all organizations.
llm_observability_min_spend_agg_sum
int64
Minimum spend for LLM observability sessions for all hours in the current month for all organizations.
logs_by_retention
object
Object containing logs usage data broken down by retention period.
orgs
object
Indexed logs usage summary for each organization for each retention period with usage.
usage
[object]
Indexed logs usage summary for each organization.
usage
[object]
Indexed logs usage for each active retention for the organization.
logs_indexed_logs_usage_sum
int64
Total indexed logs for this retention period.
logs_live_indexed_logs_usage_sum
int64
Live indexed logs for this retention period.
logs_rehydrated_indexed_logs_usage_sum
int64
Rehydrated indexed logs for this retention period.
retention
string
The retention period in days or "custom" for all custom retention periods.
usage
[object]
Aggregated index logs usage for each retention period with usage.
logs_indexed_logs_usage_agg_sum
int64
Total indexed logs for this retention period.
logs_live_indexed_logs_usage_agg_sum
int64
Live indexed logs for this retention period.
logs_rehydrated_indexed_logs_usage_agg_sum
int64
Rehydrated indexed logs for this retention period.
retention
string
The retention period in days or "custom" for all custom retention periods.
usage_by_month
object
Object containing a summary of indexed logs usage by retention period for a single month.
date
date-time
The month for the usage.
usage
[object]
Indexed logs usage for each active retention for the month.
logs_indexed_logs_usage_sum
int64
Total indexed logs for this retention period.
logs_live_indexed_logs_usage_sum
int64
Live indexed logs for this retention period.
logs_rehydrated_indexed_logs_usage_sum
int64
Rehydrated indexed logs for this retention period.
retention
string
The retention period in days or "custom" for all custom retention periods.
mobile_rum_lite_session_count_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile lite sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_android_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Android over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_flutter_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Flutter over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_ios_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on iOS over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_reactnative_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on React Native over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_roku_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Roku over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_units_agg_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM units over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
ndm_netflow_events_agg_sum
int64
Shows the sum of all Network Device Monitoring NetFlow events over all hours in the current month for all organizations.
netflow_indexed_events_count_agg_sum
int64
**DEPRECATED** : Shows the sum of all Network flows indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
network_device_wireless_top99p_sum
int64
Shows the 99th percentile of all Network Device Monitoring wireless devices over all hours in the current month for all organizations.
npm_host_top99p_sum
int64
Shows the 99th percentile of all distinct Cloud Network Monitoring hosts (formerly known as Network hosts) over all hours in the current month for all organizations.
observability_pipelines_bytes_processed_agg_sum
int64
Sum of all observability pipelines bytes processed over all hours in the current month for all organizations.
oci_host_agg_sum
int64
Shows the sum of Oracle Cloud Infrastructure hosts over all hours in the current months for all organizations
oci_host_top99p_sum
int64
Shows the 99th percentile of Oracle Cloud Infrastructure hosts over all hours in the current months for all organizations
on_call_seat_hwm_sum
int64
Shows the sum of the high-water marks of On-Call seats over all hours in the current month for all organizations.
online_archive_events_count_agg_sum
int64
Sum of all online archived events over all hours in the current month for all organizations.
opentelemetry_apm_host_top99p_sum
int64
Shows the 99th percentile of APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
opentelemetry_host_top99p_sum
int64
Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
product_analytics_agg_sum
int64
Sum of all product analytics sessions for all hours in the current month for all organizations.
profiling_aas_count_top99p_sum
int64
Shows the 99th percentile of all profiled Azure app services over all hours in the current month for all organizations.
profiling_container_agent_count_avg
int64
Shows the average number of profiled containers over all hours in the current month for all organizations.
profiling_host_count_top99p_sum
int64
Shows the 99th percentile of all profiled hosts over all hours in the current month for all organizations.
proxmox_host_agg_sum
int64
Sum of all Proxmox hosts over all hours in the current month for all organizations.
proxmox_host_top99p_sum
int64
Sum of the 99th percentile of all Proxmox hosts over all hours in the current month for all organizations.
published_app_hwm_sum
int64
Shows the high-water mark of all published applications over all hours in the current month for all organizations.
rehydrated_indexed_events_agg_sum
int64
**DEPRECATED** : Shows the sum of all rehydrated logs indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
rehydrated_ingested_bytes_agg_sum
int64
Shows the sum of all rehydrated logs bytes ingested over all hours in the current month for all organizations (data available as of December 1, 2020).
rum_browser_and_mobile_session_count
int64
Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
rum_browser_legacy_session_count_agg_sum
int64
Shows the sum of all browser RUM legacy sessions over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_browser_lite_session_count_agg_sum
int64
Shows the sum of all browser RUM lite sessions over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_browser_replay_session_count_agg_sum
int64
Shows the sum of all browser RUM Session Replay counts over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_indexed_sessions_agg_sum
int64
Sum of all RUM indexed sessions for all hours in the current month for all organizations.
rum_ingested_sessions_agg_sum
int64
Sum of all RUM ingested sessions for all hours in the current month for all organizations.
rum_lite_session_count_agg_sum
int64
Shows the sum of all RUM lite sessions (browser and mobile) over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_android_agg_sum
int64
Shows the sum of all mobile RUM legacy sessions on Android over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_flutter_agg_sum
int64
Shows the sum of all mobile RUM legacy sessions on Flutter over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_ios_agg_sum
int64
Shows the sum of all mobile RUM legacy sessions on iOS over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_reactnative_agg_sum
int64
Shows the sum of all mobile RUM legacy sessions on React Native over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_roku_agg_sum
int64
Shows the sum of all mobile RUM legacy sessions on Roku over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_android_agg_sum
int64
Shows the sum of all mobile RUM lite sessions on Android over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_flutter_agg_sum
int64
Shows the sum of all mobile RUM lite sessions on Flutter over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_ios_agg_sum
int64
Shows the sum of all mobile RUM lite sessions on iOS over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum
int64
Shows the sum of all mobile RUM lite sessions on Kotlin Multiplatform over all hours within the current month for all organizations.
rum_mobile_lite_session_count_reactnative_agg_sum
int64
Shows the sum of all mobile RUM lite sessions on React Native over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_roku_agg_sum
int64
Shows the sum of all mobile RUM lite sessions on Roku over all hours within the current month for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_unity_agg_sum
int64
Shows the sum of all mobile RUM lite sessions on Unity over all hours within the current month for all organizations.
rum_mobile_replay_session_count_android_agg_sum
int64
Shows the sum of all mobile RUM replay sessions on Android over all hours within the current month for all organizations.
rum_mobile_replay_session_count_ios_agg_sum
int64
Shows the sum of all mobile RUM replay sessions on iOS over all hours within the current month for all organizations.
rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum
int64
Shows the sum of all mobile RUM replay sessions on Kotlin Multiplatform over all hours within the current month for all organizations.
rum_mobile_replay_session_count_reactnative_agg_sum
int64
Shows the sum of all mobile RUM replay sessions on React Native over all hours within the current month for all organizations.
rum_replay_session_count_agg_sum
int64
Shows the sum of all RUM Session Replay counts over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
rum_session_count_agg_sum
int64
**DEPRECATED** : Shows the sum of all browser RUM lite sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
rum_session_replay_add_on_agg_sum
int64
Sum of all RUM session replay add-on sessions for all hours in the current month for all organizations.
rum_total_session_count_agg_sum
int64
Shows the sum of RUM sessions (browser and mobile) over all hours in the current month for all organizations.
rum_units_agg_sum
int64
**DEPRECATED** : Shows the sum of all browser and mobile RUM units over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
sca_fargate_count_avg_sum
int64
Shows the average of all Software Composition Analysis Fargate tasks over all hours in the current months for all organizations.
sca_fargate_count_hwm_sum
int64
Shows the sum of the high-water marks of all Software Composition Analysis Fargate tasks over all hours in the current months for all organizations.
sds_apm_scanned_bytes_sum
int64
Sum of all APM bytes scanned with sensitive data scanner in the current month for all organizations.
sds_events_scanned_bytes_sum
int64
Sum of all event stream events bytes scanned with sensitive data scanner in the current month for all organizations.
sds_logs_scanned_bytes_sum
int64
Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for all organizations.
sds_rum_scanned_bytes_sum
int64
Sum of all RUM bytes scanned with sensitive data scanner in the current month for all organizations.
sds_total_scanned_bytes_sum
int64
Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for all organizations.
serverless_apps_apm_apm_azure_appservice_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring for Azure App Service instances in the current month for all organizations.
serverless_apps_apm_apm_azure_azurefunction_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring for Azure Function instances in the current month for all organizations.
serverless_apps_apm_apm_azure_containerapp_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring for Azure Container App instances in the current month for all organizations.
serverless_apps_apm_apm_fargate_ecs_tasks_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring for Fargate Elastic Container Service tasks in the current month for all organizations.
serverless_apps_apm_apm_gcp_cloudfunction_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring for Google Cloud Platform Cloud Function instances in the current month for all organizations.
serverless_apps_apm_apm_gcp_cloudrun_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring for Google Cloud Platform Cloud Run instances in the current month for all organizations.
serverless_apps_apm_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring in the current month for all organizations.
serverless_apps_apm_excl_fargate_apm_azure_appservice_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure App Service instances in the current month for all organizations.
serverless_apps_apm_excl_fargate_apm_azure_azurefunction_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure Function instances in the current month for all organizations.
serverless_apps_apm_excl_fargate_apm_azure_containerapp_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure Container App instances in the current month for all organizations.
serverless_apps_apm_excl_fargate_apm_gcp_cloudfunction_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Google Cloud Platform Cloud Function instances in the current month for all organizations.
serverless_apps_apm_excl_fargate_apm_gcp_cloudrun_instances_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Google Cloud Platform Cloud Run instances in the current month for all organizations.
serverless_apps_apm_excl_fargate_avg_sum
int64
Sum of the average number of Serverless Apps with Application Performance Monitoring excluding Fargate in the current month for all organizations.
serverless_apps_azure_container_app_instances_avg_sum
int64
Sum of the average number of Serverless Apps for Azure Container App instances in the current month for all organizations.
serverless_apps_azure_count_avg_sum
int64
Sum of the average number of Serverless Apps for Azure in the current month for all organizations.
serverless_apps_azure_function_app_instances_avg_sum
int64
Sum of the average number of Serverless Apps for Azure Function App instances in the current month for all organizations.
serverless_apps_azure_web_app_instances_avg_sum
int64
Sum of the average number of Serverless Apps for Azure Web App instances in the current month for all organizations.
serverless_apps_ecs_avg_sum
int64
Sum of the average number of Serverless Apps for Elastic Container Service in the current month for all organizations.
serverless_apps_eks_avg_sum
int64
Sum of the average number of Serverless Apps for Elastic Kubernetes Service in the current month for all organizations.
serverless_apps_excl_fargate_avg_sum
int64
Sum of the average number of Serverless Apps excluding Fargate in the current month for all organizations.
serverless_apps_excl_fargate_azure_container_app_instances_avg_sum
int64
Sum of the average number of Serverless Apps excluding Fargate for Azure Container App instances in the current month for all organizations.
serverless_apps_excl_fargate_azure_function_app_instances_avg_sum
int64
Sum of the average number of Serverless Apps excluding Fargate for Azure Function App instances in the current month for all organizations.
serverless_apps_excl_fargate_azure_web_app_instances_avg_sum
int64
Sum of the average number of Serverless Apps excluding Fargate for Azure Web App instances in the current month for all organizations.
serverless_apps_excl_fargate_google_cloud_functions_instances_avg_sum
int64
Sum of the average number of Serverless Apps excluding Fargate for Google Cloud Platform Cloud Functions instances in the current month for all organizations.
serverless_apps_excl_fargate_google_cloud_run_instances_avg_sum
int64
Sum of the average number of Serverless Apps excluding Fargate for Google Cloud Platform Cloud Run instances in the current month for all organizations.
serverless_apps_google_cloud_functions_instances_avg_sum
int64
Sum of the average number of Serverless Apps for Google Cloud Platform Cloud Functions instances in the current month for all organizations.
serverless_apps_google_cloud_run_instances_avg_sum
int64
Sum of the average number of Serverless Apps for Google Cloud Platform Cloud Run instances in the current month for all organizations.
serverless_apps_google_count_avg_sum
int64
Sum of the average number of Serverless Apps for Google Cloud in the current month for all organizations.
serverless_apps_total_count_avg_sum
int64
Sum of the average number of Serverless Apps for Azure and Google Cloud in the current month for all organizations.
siem_analyzed_logs_add_on_count_agg_sum
int64
Shows the sum of all log events analyzed by Cloud SIEM over all hours in the current month for all organizations.
start_date
date-time
Shows the first date of usage in the current month for all organizations.
synthetics_browser_check_calls_count_agg_sum
int64
Shows the sum of all Synthetic browser tests over all hours in the current month for all organizations.
synthetics_check_calls_count_agg_sum
int64
Shows the sum of all Synthetic API tests over all hours in the current month for all organizations.
synthetics_mobile_test_runs_agg_sum
int64
Shows the sum of Synthetic mobile application tests over all hours in the current month for all organizations.
synthetics_parallel_testing_max_slots_hwm_sum
int64
Shows the sum of the high-water marks of used synthetics parallel testing slots over all hours in the current month for all organizations.
trace_search_indexed_events_count_agg_sum
int64
Shows the sum of all Indexed Spans indexed over all hours in the current month for all organizations.
twol_ingested_events_bytes_agg_sum
int64
Shows the sum of all ingested APM span bytes over all hours in the current month for all organizations.
universal_service_monitoring_host_top99p_sum
int64
Shows the 99th percentile of all Universal Service Monitoring hosts over all hours in the current month for all organizations.
usage
[object]
An array of objects regarding hourly usage.
agent_host_top99p
int64
Shows the 99th percentile of all agent hosts over all hours in the current date for all organizations.
apm_azure_app_service_host_top99p
int64
Shows the 99th percentile of all Azure app services using APM over all hours in the current date all organizations.
apm_devsecops_host_top99p
int64
Shows the 99th percentile of all APM DevSecOps hosts over all hours in the current date for the given org.
apm_enterprise_standalone_hosts_top99p
int64
Shows the 99th percentile of all distinct standalone Enterprise hosts over all hours in the current date for all organizations.
apm_fargate_count_avg
int64
Shows the average of all APM ECS Fargate tasks over all hours in the current date for all organizations.
apm_host_top99p
int64
Shows the 99th percentile of all distinct APM hosts over all hours in the current date for all organizations.
apm_pro_standalone_hosts_top99p
int64
Shows the 99th percentile of all distinct standalone Pro hosts over all hours in the current date for all organizations.
appsec_fargate_count_avg
int64
Shows the average of all Application Security Monitoring ECS Fargate tasks over all hours in the current date for all organizations.
asm_serverless_sum
int64
Shows the sum of all Application Security Monitoring Serverless invocations over all hours in the current date for all organizations.
audit_logs_lines_indexed_sum
int64
**DEPRECATED** : Shows the sum of audit logs lines indexed over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
audit_trail_enabled_hwm
int64
Shows the number of organizations that had Audit Trail enabled in the current date.
avg_profiled_fargate_tasks
int64
The average total count for Fargate Container Profiler over all hours in the current date for all organizations.
aws_host_top99p
int64
Shows the 99th percentile of all AWS hosts over all hours in the current date for all organizations.
aws_lambda_func_count
int64
Shows the average of the number of functions that executed 1 or more times each hour in the current date for all organizations.
aws_lambda_invocations_sum
int64
Shows the sum of all AWS Lambda invocations over all hours in the current date for all organizations.
azure_app_service_top99p
int64
Shows the 99th percentile of all Azure app services over all hours in the current date for all organizations.
billable_ingested_bytes_sum
int64
Shows the sum of all log bytes ingested over all hours in the current date for all organizations.
bits_ai_investigations_sum
int64
Shows the sum of all Bits AI Investigations over all hours in the current date for all organizations.
browser_rum_lite_session_count_sum
int64
**DEPRECATED** : Shows the sum of all browser lite sessions over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
browser_rum_replay_session_count_sum
int64
Shows the sum of all browser replay sessions over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
browser_rum_units_sum
int64
**DEPRECATED** : Shows the sum of all browser RUM units over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
ci_pipeline_indexed_spans_sum
int64
Shows the sum of all CI pipeline indexed spans over all hours in the current month for all organizations.
ci_test_indexed_spans_sum
int64
Shows the sum of all CI test indexed spans over all hours in the current month for all organizations.
ci_visibility_itr_committers_hwm
int64
Shows the high-water mark of all CI visibility intelligent test runner committers over all hours in the current month for all organizations.
ci_visibility_pipeline_committers_hwm
int64
Shows the high-water mark of all CI visibility pipeline committers over all hours in the current month for all organizations.
ci_visibility_test_committers_hwm
int64
Shows the high-water mark of all CI visibility test committers over all hours in the current month for all organizations.
cloud_cost_management_aws_host_count_avg
int64
Host count average of Cloud Cost Management for AWS for the given date and given organization.
cloud_cost_management_azure_host_count_avg
int64
Host count average of Cloud Cost Management for Azure for the given date and given organization.
cloud_cost_management_gcp_host_count_avg
int64
Host count average of Cloud Cost Management for GCP for the given date and given organization.
cloud_cost_management_host_count_avg
int64
Host count average of Cloud Cost Management for all cloud providers for the given date and given organization.
cloud_cost_management_oci_host_count_avg
int64
Average host count for Cloud Cost Management on OCI for the given date and organization.
cloud_siem_events_sum
int64
Shows the sum of all Cloud Security Information and Event Management events over all hours in the current date for the given org.
code_analysis_sa_committers_hwm
int64
Shows the high-water mark of all Static Analysis committers over all hours in the current date for the given org.
code_analysis_sca_committers_hwm
int64
Shows the high-water mark of all static Software Composition Analysis committers over all hours in the current date for the given org.
code_security_host_top99p
int64
Shows the 99th percentile of all Code Security hosts over all hours in the current date for the given org.
container_avg
int64
Shows the average of all distinct containers over all hours in the current date for all organizations.
container_excl_agent_avg
int64
Shows the average of containers without the Datadog Agent over all hours in the current date for all organizations.
container_hwm
int64
Shows the high-water mark of all distinct containers over all hours in the current date for all organizations.
csm_container_enterprise_compliance_count_sum
int64
Shows the sum of all Cloud Security Management Enterprise compliance containers over all hours in the current date for the given org.
csm_container_enterprise_cws_count_sum
int64
Shows the sum of all Cloud Security Management Enterprise Cloud Workload Security containers over all hours in the current date for the given org.
csm_container_enterprise_total_count_sum
int64
Shows the sum of all Cloud Security Management Enterprise containers over all hours in the current date for the given org.
csm_host_enterprise_aas_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Azure app services hosts over all hours in the current date for the given org.
csm_host_enterprise_aws_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise AWS hosts over all hours in the current date for the given org.
csm_host_enterprise_azure_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Azure hosts over all hours in the current date for the given org.
csm_host_enterprise_compliance_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise compliance hosts over all hours in the current date for the given org.
csm_host_enterprise_cws_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Cloud Workload Security hosts over all hours in the current date for the given org.
csm_host_enterprise_gcp_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise GCP hosts over all hours in the current date for the given org.
csm_host_enterprise_total_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise hosts over all hours in the current date for the given org.
cspm_aas_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro Azure app services hosts over all hours in the current date for all organizations.
cspm_aws_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro AWS hosts over all hours in the current date for all organizations.
cspm_azure_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro Azure hosts over all hours in the current date for all organizations.
cspm_container_avg
int64
Shows the average number of Cloud Security Management Pro containers over all hours in the current date for all organizations.
cspm_container_hwm
int64
Shows the high-water mark of Cloud Security Management Pro containers over all hours in the current date for all organizations.
cspm_gcp_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro GCP hosts over all hours in the current date for all organizations.
cspm_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro hosts over all hours in the current date for all organizations.
custom_ts_avg
int64
Shows the average number of distinct custom metrics over all hours in the current date for all organizations.
cws_container_count_avg
int64
Shows the average of all distinct Cloud Workload Security containers over all hours in the current date for all organizations.
cws_fargate_task_avg
int64
Shows the average of all distinct Cloud Workload Security Fargate tasks over all hours in the current date for all organizations.
cws_host_top99p
int64
Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current date for all organizations.
data_jobs_monitoring_host_hr_sum
int64
Shows the sum of all Data Jobs Monitoring hosts over all hours in the current date for the given org.
date
date-time
The date for the usage.
dbm_host_top99p
int64
Shows the 99th percentile of all Database Monitoring hosts over all hours in the current date for all organizations.
dbm_queries_count_avg
int64
Shows the average of all normalized Database Monitoring queries over all hours in the current date for all organizations.
eph_infra_host_agent_sum
int64
Shows the sum of all ephemeral infrastructure hosts with the Datadog Agent over all hours in the current date for the given org.
eph_infra_host_alibaba_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Alibaba over all hours in the current date for the given org.
eph_infra_host_aws_sum
int64
Shows the sum of all ephemeral infrastructure hosts on AWS over all hours in the current date for the given org.
eph_infra_host_azure_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Azure over all hours in the current date for the given org.
eph_infra_host_ent_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Enterprise over all hours in the current date for the given org.
eph_infra_host_gcp_sum
int64
Shows the sum of all ephemeral infrastructure hosts on GCP over all hours in the current date for the given org.
eph_infra_host_heroku_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Heroku over all hours in the current date for the given org.
eph_infra_host_only_aas_sum
int64
Shows the sum of all ephemeral infrastructure hosts with only Azure App Services over all hours in the current date for the given org.
eph_infra_host_only_vsphere_sum
int64
Shows the sum of all ephemeral infrastructure hosts with only vSphere over all hours in the current date for the given org.
eph_infra_host_opentelemetry_apm_sum
int64
Shows the sum of all ephemeral APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
eph_infra_host_opentelemetry_sum
int64
Shows the sum of all ephemeral hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
eph_infra_host_pro_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Pro over all hours in the current date for the given org.
eph_infra_host_proplus_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Pro Plus over all hours in the current date for the given org.
eph_infra_host_proxmox_sum
int64
Sum of all ephemeral infrastructure hosts for Proxmox over all hours in the current date for all organizations.
error_tracking_apm_error_events_sum
int64
Shows the sum of all Error Tracking APM error events over all hours in the current date for the given org.
error_tracking_error_events_sum
int64
Shows the sum of all Error Tracking error events over all hours in the current date for the given org.
error_tracking_events_sum
int64
Shows the sum of all Error Tracking events over all hours in the current date for the given org.
error_tracking_rum_error_events_sum
int64
Shows the sum of all Error Tracking RUM error events over all hours in the current date for the given org.
event_management_correlation_correlated_events_sum
int64
Shows the sum of all Event Management correlated events over all hours in the current date for all organizations.
event_management_correlation_correlated_related_events_sum
int64
Shows the sum of all Event Management correlated related events over all hours in the current date for all organizations.
event_management_correlation_sum
int64
Shows the sum of all Event Management correlations over all hours in the current date for all organizations.
fargate_container_profiler_profiling_fargate_avg
int64
The average number of Profiling Fargate tasks over all hours in the current date for all organizations.
fargate_container_profiler_profiling_fargate_eks_avg
int64
The average number of Profiling Fargate Elastic Kubernetes Service tasks over all hours in the current date for all organizations.
fargate_tasks_count_avg
int64
Shows the high-watermark of all Fargate tasks over all hours in the current date for all organizations.
fargate_tasks_count_hwm
int64
Shows the average of all Fargate tasks over all hours in the current date for all organizations.
flex_logs_compute_large_avg
int64
Shows the average number of Flex Logs Compute Large Instances over all hours in the current date for the given org.
flex_logs_compute_medium_avg
int64
Shows the average number of Flex Logs Compute Medium Instances over all hours in the current date for the given org.
flex_logs_compute_small_avg
int64
Shows the average number of Flex Logs Compute Small Instances over all hours in the current date for the given org.
flex_logs_compute_xlarge_avg
int64
Shows the average number of Flex Logs Compute Extra Large Instances over all hours in the current date for the given org.
flex_logs_compute_xsmall_avg
int64
Shows the average number of Flex Logs Compute Extra Small Instances over all hours in the current date for the given org.
flex_logs_starter_avg
int64
Shows the average number of Flex Logs Starter Instances over all hours in the current date for the given org.
flex_logs_starter_storage_index_avg
int64
Shows the average number of Flex Logs Starter Storage Index Instances over all hours in the current date for the given org.
flex_logs_starter_storage_retention_adjustment_avg
int64
Shows the average number of Flex Logs Starter Storage Retention Adjustment Instances over all hours in the current date for the given org.
flex_stored_logs_avg
int64
Shows the average of all Flex Stored Logs over all hours in the current date for the given org.
forwarding_events_bytes_sum
int64
Shows the sum of all log bytes forwarded over all hours in the current date for all organizations.
gcp_host_top99p
int64
Shows the 99th percentile of all GCP hosts over all hours in the current date for all organizations.
heroku_host_top99p
int64
Shows the 99th percentile of all Heroku dynos over all hours in the current date for all organizations.
incident_management_monthly_active_users_hwm
int64
Shows the high-water mark of incident management monthly active users over all hours in the current date for all organizations.
incident_management_seats_hwm
int64
Shows the high-water mark of Incident Management seats over all hours on the current date for all organizations.
indexed_events_count_sum
int64
Shows the sum of all log events indexed over all hours in the current date for all organizations.
infra_host_top99p
int64
Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for all organizations.
ingested_events_bytes_sum
int64
Shows the sum of all log bytes ingested over all hours in the current date for all organizations.
iot_device_sum
int64
Shows the sum of all IoT devices over all hours in the current date for all organizations.
iot_device_top99p
int64
Shows the 99th percentile of all IoT devices over all hours in the current date all organizations.
llm_observability_min_spend_sum
int64
Sum of all LLM observability minimum spend over all hours in the current date for all organizations.
llm_observability_sum
int64
Sum of all LLM observability sessions over all hours in the current date for all organizations.
mobile_rum_lite_session_count_sum
int64
**DEPRECATED** : Shows the sum of all mobile lite sessions over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_android_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Android over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_flutter_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Flutter over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_ios_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on iOS over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_reactnative_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on React Native over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_roku_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Roku over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_session_count_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
mobile_rum_units_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM units over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
ndm_netflow_events_sum
int64
Shows the sum of all Network Device Monitoring NetFlow events over all hours in the current date for the given org.
netflow_indexed_events_count_sum
int64
**DEPRECATED** : Shows the sum of all Network flows indexed over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
network_device_wireless_top99p
int64
Shows the 99th percentile of all Network Device Monitoring wireless devices over all hours in the current date for all organizations.
npm_host_top99p
int64
Shows the 99th percentile of all distinct Cloud Network Monitoring hosts (formerly known as Network hosts) over all hours in the current date for all organizations.
observability_pipelines_bytes_processed_sum
int64
Sum of all observability pipelines bytes processed over all hours in the current date for the given org.
oci_host_sum
int64
Shows the sum of all Oracle Cloud Infrastructure hosts over all hours in the current date for the given org.
oci_host_top99p
int64
Shows the 99th percentile of all Oracle Cloud Infrastructure hosts over all hours in the current date for the given org.
on_call_seat_hwm
int64
Shows the high-water mark of On-Call seats over all hours in the current date for all organizations.
online_archive_events_count_sum
int64
Sum of all online archived events over all hours in the current date for all organizations.
opentelemetry_apm_host_top99p
int64
Shows the 99th percentile of APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for all organizations.
opentelemetry_host_top99p
int64
Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for all organizations.
orgs
[object]
Organizations associated with a user.
account_name
string
The account name.
account_public_id
string
The account public id.
agent_host_top99p
int64
Shows the 99th percentile of all agent hosts over all hours in the current date for the given org.
apm_azure_app_service_host_top99p
int64
Shows the 99th percentile of all Azure app services using APM over all hours in the current date for the given org.
apm_devsecops_host_top99p
int64
Shows the 99th percentile of all APM DevSecOps hosts over all hours in the current date for the given org.
apm_enterprise_standalone_hosts_top99p
int64
Shows the 99th percentile of all distinct standalone Enterprise hosts over all hours in the current date for the given org.
apm_fargate_count_avg
int64
Shows the average of all APM ECS Fargate tasks over all hours in the current month for the given org.
apm_host_top99p
int64
Shows the 99th percentile of all distinct APM hosts over all hours in the current date for the given org.
apm_pro_standalone_hosts_top99p
int64
Shows the 99th percentile of all distinct standalone Pro hosts over all hours in the current date for the given org.
appsec_fargate_count_avg
int64
Shows the average of all Application Security Monitoring ECS Fargate tasks over all hours in the current month for the given org.
asm_serverless_sum
int64
Shows the sum of all Application Security Monitoring Serverless invocations over all hours in the current month for the given org.
audit_logs_lines_indexed_sum
int64
**DEPRECATED** : Shows the sum of all audit logs lines indexed over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
audit_trail_enabled_hwm
int64
Shows whether Audit Trail is enabled for the current date for the given org.
avg_profiled_fargate_tasks
int64
The average total count for Fargate Container Profiler over all hours in the current month for the given org.
aws_host_top99p
int64
Shows the 99th percentile of all AWS hosts over all hours in the current date for the given org.
aws_lambda_func_count
int64
Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org.
aws_lambda_invocations_sum
int64
Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org.
azure_app_service_top99p
int64
Shows the 99th percentile of all Azure app services over all hours in the current date for the given org.
billable_ingested_bytes_sum
int64
Shows the sum of all log bytes ingested over all hours in the current date for the given org.
bits_ai_investigations_sum
int64
Shows the sum of all Bits AI Investigations over all hours in the current date for the given org.
browser_rum_lite_session_count_sum
int64
**DEPRECATED** : Shows the sum of all browser lite sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
browser_rum_replay_session_count_sum
int64
Shows the sum of all browser replay sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
browser_rum_units_sum
int64
**DEPRECATED** : Shows the sum of all browser RUM units over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
ci_pipeline_indexed_spans_sum
int64
Shows the sum of all CI pipeline indexed spans over all hours in the current date for the given org.
ci_test_indexed_spans_sum
int64
Shows the sum of all CI test indexed spans over all hours in the current date for the given org.
ci_visibility_itr_committers_hwm
int64
Shows the high-water mark of all CI visibility intelligent test runner committers over all hours in the current date for the given org.
ci_visibility_pipeline_committers_hwm
int64
Shows the high-water mark of all CI visibility pipeline committers over all hours in the current date for the given org.
ci_visibility_test_committers_hwm
int64
Shows the high-water mark of all CI visibility test committers over all hours in the current date for the given org.
cloud_cost_management_aws_host_count_avg
int64
Host count average of Cloud Cost Management for AWS for the given date and given org.
cloud_cost_management_azure_host_count_avg
int64
Host count average of Cloud Cost Management for Azure for the given date and given org.
cloud_cost_management_gcp_host_count_avg
int64
Host count average of Cloud Cost Management for GCP for the given date and given org.
cloud_cost_management_host_count_avg
int64
Host count average of Cloud Cost Management for all cloud providers for the given date and given org.
cloud_cost_management_oci_host_count_avg
int64
Average host count for Cloud Cost Management on OCI for the given date and organization.
cloud_siem_events_sum
int64
Shows the sum of all Cloud Security Information and Event Management events over all hours in the current date for the given org.
code_analysis_sa_committers_hwm
int64
Shows the high-water mark of all Static Analysis committers over all hours in the current date for the given org.
code_analysis_sca_committers_hwm
int64
Shows the high-water mark of all static Software Composition Analysis committers over all hours in the current date for the given org.
code_security_host_top99p
int64
Shows the 99th percentile of all Code Security hosts over all hours in the current date for the given org.
container_avg
int64
Shows the average of all distinct containers over all hours in the current date for the given org.
container_excl_agent_avg
int64
Shows the average of containers without the Datadog Agent over all hours in the current date for the given organization.
container_hwm
int64
Shows the high-water mark of all distinct containers over all hours in the current date for the given org.
csm_container_enterprise_compliance_count_sum
int64
Shows the sum of all Cloud Security Management Enterprise compliance containers over all hours in the current date for the given org.
csm_container_enterprise_cws_count_sum
int64
Shows the sum of all Cloud Security Management Enterprise Cloud Workload Security containers over all hours in the current date for the given org.
csm_container_enterprise_total_count_sum
int64
Shows the sum of all Cloud Security Management Enterprise containers over all hours in the current date for the given org.
csm_host_enterprise_aas_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Azure app services hosts over all hours in the current date for the given org.
csm_host_enterprise_aws_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise AWS hosts over all hours in the current date for the given org.
csm_host_enterprise_azure_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Azure hosts over all hours in the current date for the given org.
csm_host_enterprise_compliance_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise compliance hosts over all hours in the current date for the given org.
csm_host_enterprise_cws_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise Cloud Workload Security hosts over all hours in the current date for the given org.
csm_host_enterprise_gcp_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise GCP hosts over all hours in the current date for the given org.
csm_host_enterprise_total_host_count_top99p
int64
Shows the 99th percentile of all Cloud Security Management Enterprise hosts over all hours in the current date for the given org.
cspm_aas_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro Azure app services hosts over all hours in the current date for the given org.
cspm_aws_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro AWS hosts over all hours in the current date for the given org.
cspm_azure_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro Azure hosts over all hours in the current date for the given org.
cspm_container_avg
int64
Shows the average number of Cloud Security Management Pro containers over all hours in the current date for the given org.
cspm_container_hwm
int64
Shows the high-water mark of Cloud Security Management Pro containers over all hours in the current date for the given org.
cspm_gcp_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro GCP hosts over all hours in the current date for the given org.
cspm_host_top99p
int64
Shows the 99th percentile of all Cloud Security Management Pro hosts over all hours in the current date for the given org.
custom_historical_ts_avg
int64
Shows the average number of distinct historical custom metrics over all hours in the current date for the given org.
custom_live_ts_avg
int64
Shows the average number of distinct live custom metrics over all hours in the current date for the given org.
custom_ts_avg
int64
Shows the average number of distinct custom metrics over all hours in the current date for the given org.
cws_container_count_avg
int64
Shows the average of all distinct Cloud Workload Security containers over all hours in the current date for the given org.
cws_fargate_task_avg
int64
Shows the average of all distinct Cloud Workload Security Fargate tasks over all hours in the current date for the given org.
cws_host_top99p
int64
Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current date for the given org.
data_jobs_monitoring_host_hr_sum
int64
Shows the sum of all Data Jobs Monitoring hosts over all hours in the current date for the given org.
dbm_host_top99p_sum
int64
Shows the 99th percentile of all Database Monitoring hosts over all hours in the current month for the given org.
dbm_queries_avg_sum
int64
Shows the average of all distinct Database Monitoring normalized queries over all hours in the current month for the given org.
eph_infra_host_agent_sum
int64
Shows the sum of all ephemeral infrastructure hosts with the Datadog Agent over all hours in the current date for the given org.
eph_infra_host_alibaba_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Alibaba over all hours in the current date for the given org.
eph_infra_host_aws_sum
int64
Shows the sum of all ephemeral infrastructure hosts on AWS over all hours in the current date for the given org.
eph_infra_host_azure_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Azure over all hours in the current date for the given org.
eph_infra_host_ent_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Enterprise over all hours in the current date for the given org.
eph_infra_host_gcp_sum
int64
Shows the sum of all ephemeral infrastructure hosts on GCP over all hours in the current date for the given org.
eph_infra_host_heroku_sum
int64
Shows the sum of all ephemeral infrastructure hosts on Heroku over all hours in the current date for the given org.
eph_infra_host_only_aas_sum
int64
Shows the sum of all ephemeral infrastructure hosts with only Azure App Services over all hours in the current date for the given org.
eph_infra_host_only_vsphere_sum
int64
Shows the sum of all ephemeral infrastructure hosts with only vSphere over all hours in the current date for the given org.
eph_infra_host_opentelemetry_apm_sum
int64
Shows the sum of all ephemeral APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
eph_infra_host_opentelemetry_sum
int64
Shows the sum of all ephemeral hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
eph_infra_host_pro_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Pro over all hours in the current date for the given org.
eph_infra_host_proplus_sum
int64
Shows the sum of all ephemeral infrastructure hosts for Pro Plus over all hours in the current date for the given org.
eph_infra_host_proxmox_sum
int64
Sum of all ephemeral infrastructure hosts for Proxmox over all hours in the current date for the given organization.
error_tracking_apm_error_events_sum
int64
Shows the sum of all Error Tracking APM error events over all hours in the current date for the given org.
error_tracking_error_events_sum
int64
Shows the sum of all Error Tracking error events over all hours in the current date for the given org.
error_tracking_events_sum
int64
Shows the sum of all Error Tracking events over all hours in the current date for the given org.
error_tracking_rum_error_events_sum
int64
Shows the sum of all Error Tracking RUM error events over all hours in the current date for the given org.
event_management_correlation_correlated_events_sum
int64
Shows the sum of all Event Management correlated events over all hours in the current date for the given org.
event_management_correlation_correlated_related_events_sum
int64
Shows the sum of all Event Management correlated related events over all hours in the current date for the given org.
event_management_correlation_sum
int64
Shows the sum of all Event Management correlations over all hours in the current date for the given org.
fargate_container_profiler_profiling_fargate_avg
int64
The average number of Profiling Fargate tasks over all hours in the current month for the given org.
fargate_container_profiler_profiling_fargate_eks_avg
int64
The average number of Profiling Fargate Elastic Kubernetes Service tasks over all hours in the current month for the given org.
fargate_tasks_count_avg
int64
The average task count for Fargate.
fargate_tasks_count_hwm
int64
Shows the high-water mark of all Fargate tasks over all hours in the current date for the given org.
flex_logs_compute_large_avg
int64
Shows the average number of Flex Logs Compute Large Instances over all hours in the current date for the given org.
flex_logs_compute_medium_avg
int64
Shows the average number of Flex Logs Compute Medium Instances over all hours in the current date for the given org.
flex_logs_compute_small_avg
int64
Shows the average number of Flex Logs Compute Small Instances over all hours in the current date for the given org.
flex_logs_compute_xlarge_avg
int64
Shows the average number of Flex Logs Compute Extra Large Instances over all hours in the current date for the given org.
flex_logs_compute_xsmall_avg
int64
Shows the average number of Flex Logs Compute Extra Small Instances over all hours in the current date for the given org.
flex_logs_starter_avg
int64
Shows the average number of Flex Logs Starter Instances over all hours in the current date for the given org.
flex_logs_starter_storage_index_avg
int64
Shows the average number of Flex Logs Starter Storage Index Instances over all hours in the current date for the given org.
flex_logs_starter_storage_retention_adjustment_avg
int64
Shows the average number of Flex Logs Starter Storage Retention Adjustment Instances over all hours in the current date for the given org.
flex_stored_logs_avg
int64
Shows the average of all Flex Stored Logs over all hours in the current date for the given org.
forwarding_events_bytes_sum
int64
Shows the sum of all log bytes forwarded over all hours in the current date for the given org.
gcp_host_top99p
int64
Shows the 99th percentile of all GCP hosts over all hours in the current date for the given org.
heroku_host_top99p
int64
Shows the 99th percentile of all Heroku dynos over all hours in the current date for the given org.
id
string
The organization id.
incident_management_monthly_active_users_hwm
int64
Shows the high-water mark of incident management monthly active users over all hours in the current date for the given org.
incident_management_seats_hwm
int64
Shows the high-water mark of Incident Management seats over all hours on the current date for the given organization.
indexed_events_count_sum
int64
**DEPRECATED** : Shows the sum of all log events indexed over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
infra_host_top99p
int64
Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for the given org.
ingested_events_bytes_sum
int64
Shows the sum of all log bytes ingested over all hours in the current date for the given org.
iot_device_agg_sum
int64
Shows the sum of all IoT devices over all hours in the current date for the given org.
iot_device_top99p_sum
int64
Shows the 99th percentile of all IoT devices over all hours in the current date for the given org.
llm_observability_min_spend_sum
int64
Shows the sum of all LLM Observability minimum spend over all hours in the current date for the given org.
llm_observability_sum
int64
Shows the sum of all LLM observability sessions over all hours in the current date for the given org.
mobile_rum_lite_session_count_sum
int64
**DEPRECATED** : Shows the sum of all mobile lite sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
mobile_rum_session_count_android_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Android over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
mobile_rum_session_count_flutter_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Flutter over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
mobile_rum_session_count_ios_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on iOS over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
mobile_rum_session_count_reactnative_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on React Native over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
mobile_rum_session_count_roku_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions on Roku over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
mobile_rum_session_count_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
mobile_rum_units_sum
int64
**DEPRECATED** : Shows the sum of all mobile RUM units over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
name
string
The organization name.
ndm_netflow_events_sum
int64
Shows the sum of all Network Device Monitoring NetFlow events over all hours in the current date for the given org.
netflow_indexed_events_count_sum
int64
**DEPRECATED** : Shows the sum of all Network flows indexed over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
network_device_wireless_top99p
int64
Shows the 99th percentile of all Network Device Monitoring wireless devices over all hours in the current date for the given org.
npm_host_top99p
int64
Shows the 99th percentile of all distinct Cloud Network Monitoring hosts (formerly known as Network hosts) over all hours in the current date for the given org.
observability_pipelines_bytes_processed_sum
int64
Sum of all observability pipelines bytes processed over all hours in the current date for the given org.
oci_host_sum
int64
Shows the sum of all Oracle Cloud Infrastructure hosts over all hours in the current date for the given org.
oci_host_top99p
int64
Shows the 99th percentile of all Oracle Cloud Infrastructure hosts over all hours in the current date for the given org.
on_call_seat_hwm
int64
Shows the high-water mark of On-Call seats over all hours in the current date for the given org.
online_archive_events_count_sum
int64
Sum of all online archived events over all hours in the current date for the given org.
opentelemetry_apm_host_top99p
int64
Shows the 99th percentile of APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
opentelemetry_host_top99p
int64
Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
product_analytics_sum
int64
Shows the sum of all product analytics sessions over all hours in the current date for the given org.
profiling_aas_count_top99p
int64
Shows the 99th percentile of all profiled Azure app services over all hours in the current date for all organizations.
profiling_host_top99p
int64
Shows the 99th percentile of all profiled hosts over all hours within the current date for the given org.
proxmox_host_sum
int64
Sum of all Proxmox hosts over all hours in the current date for the given organization.
proxmox_host_top99p
int64
99th percentile of all Proxmox hosts over all hours in the current date for the given organization.
public_id
string
The organization public id.
published_app_hwm
int64
Shows the high-water mark of all published applications over all hours in the current date for the given org.
region
string
The region of the organization.
rum_browser_and_mobile_session_count
int64
Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
rum_browser_legacy_session_count_sum
int64
Shows the sum of all browser RUM legacy sessions over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_browser_lite_session_count_sum
int64
Shows the sum of all browser RUM lite sessions over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_browser_replay_session_count_sum
int64
Shows the sum of all browser RUM Session Replay counts over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_indexed_sessions_sum
int64
Shows the sum of all RUM indexed sessions over all hours in the current date for the given org.
rum_ingested_sessions_sum
int64
Shows the sum of all RUM ingested sessions over all hours in the current date for the given org.
rum_lite_session_count_sum
int64
Shows the sum of all RUM lite sessions (browser and mobile) over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_android_sum
int64
Shows the sum of all mobile RUM legacy sessions on Android over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_flutter_sum
int64
Shows the sum of all mobile RUM legacy sessions on Flutter over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_ios_sum
int64
Shows the sum of all mobile RUM legacy sessions on iOS over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_reactnative_sum
int64
Shows the sum of all mobile RUM legacy sessions on React Native over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_roku_sum
int64
Shows the sum of all mobile RUM legacy sessions on Roku over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_android_sum
int64
Shows the sum of all mobile RUM lite sessions on Android over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_flutter_sum
int64
Shows the sum of all mobile RUM lite sessions on Flutter over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_ios_sum
int64
Shows the sum of all mobile RUM lite sessions on iOS over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_kotlinmultiplatform_sum
int64
Shows the sum of all mobile RUM lite sessions on Kotlin Multiplatform over all hours within the current date for the given org.
rum_mobile_lite_session_count_reactnative_sum
int64
Shows the sum of all mobile RUM lite sessions on React Native over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_roku_sum
int64
Shows the sum of all mobile RUM lite sessions on Roku over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_unity_sum
int64
Shows the sum of all mobile RUM lite sessions on Unity over all hours within the current date for the given org.
rum_mobile_replay_session_count_android_sum
int64
Shows the sum of all mobile RUM replay sessions on Android over all hours within the current date for the given org.
rum_mobile_replay_session_count_ios_sum
int64
Shows the sum of all mobile RUM replay sessions on iOS over all hours within the current date for the given org.
rum_mobile_replay_session_count_kotlinmultiplatform_sum
int64
Shows the sum of all mobile RUM replay sessions on Kotlin Multiplatform over all hours within the current date for the given org.
rum_mobile_replay_session_count_reactnative_sum
int64
Shows the sum of all mobile RUM replay sessions on React Native over all hours within the current date for the given org.
rum_replay_session_count_sum
int64
Shows the sum of all RUM Session Replay counts over all hours in the current date for the given org (To be introduced on October 1st, 2024).
rum_session_count_sum
int64
**DEPRECATED** : Shows the sum of all browser RUM lite sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
rum_session_replay_add_on_sum
int64
Shows the sum of all RUM session replay add-on sessions over all hours in the current date for the given org.
rum_total_session_count_sum
int64
Shows the sum of RUM sessions (browser and mobile) over all hours in the current date for the given org.
rum_units_sum
int64
**DEPRECATED** : Shows the sum of all browser and mobile RUM units over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
sca_fargate_count_avg
int64
Shows the average of all Software Composition Analysis Fargate tasks over all hours in the current date for the given org.
sca_fargate_count_hwm
int64
Shows the sum of the high-water marks of all Software Composition Analysis Fargate tasks over all hours in the current date for the given org.
sds_apm_scanned_bytes_sum
int64
Sum of all APM bytes scanned with sensitive data scanner over all hours in the current date for the given org.
sds_events_scanned_bytes_sum
int64
Sum of all event stream events bytes scanned with sensitive data scanner over all hours in the current date for the given org.
sds_logs_scanned_bytes_sum
int64
Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for the given org.
sds_rum_scanned_bytes_sum
int64
Sum of all RUM bytes scanned with sensitive data scanner over all hours in the current date for the given org.
sds_total_scanned_bytes_sum
int64
Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for the given org.
serverless_apps_apm_apm_azure_appservice_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Azure App Service instances for the given date and given org.
serverless_apps_apm_apm_azure_azurefunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Azure Function instances for the given date and given org.
serverless_apps_apm_apm_azure_containerapp_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Azure Container App instances for the given date and given org.
serverless_apps_apm_apm_fargate_ecs_tasks_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Fargate Elastic Container Service tasks for the given date and given org.
serverless_apps_apm_apm_gcp_cloudfunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Google Cloud Platform Cloud Function instances for the given date and given org.
serverless_apps_apm_apm_gcp_cloudrun_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Google Cloud Platform Cloud Run instances for the given date and given org.
serverless_apps_apm_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for the given date and given org.
serverless_apps_apm_excl_fargate_apm_azure_appservice_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure App Service instances for the given date and given org.
serverless_apps_apm_excl_fargate_apm_azure_azurefunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure Function instances for the given date and given org.
serverless_apps_apm_excl_fargate_apm_azure_containerapp_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure Container App instances for the given date and given org.
serverless_apps_apm_excl_fargate_apm_gcp_cloudfunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Google Cloud Platform Cloud Function instances for the given date and given org.
serverless_apps_apm_excl_fargate_apm_gcp_cloudrun_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Google Cloud Platform Cloud Run instances for the given date and given org.
serverless_apps_apm_excl_fargate_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for the given date and given org.
serverless_apps_azure_container_app_instances_avg
int64
Shows the average number of Serverless Apps for Azure Container App instances for the given date and given org.
serverless_apps_azure_count_avg
int64
Shows the average number of Serverless Apps for Azure for the given date and given org.
serverless_apps_azure_function_app_instances_avg
int64
Shows the average number of Serverless Apps for Azure Function App instances for the given date and given org.
serverless_apps_azure_web_app_instances_avg
int64
Shows the average number of Serverless Apps for Azure Web App instances for the given date and given org.
serverless_apps_ecs_avg
int64
Shows the average number of Serverless Apps for Elastic Container Service for the given date and given org.
serverless_apps_eks_avg
int64
Shows the average number of Serverless Apps for Elastic Kubernetes Service for the given date and given org.
serverless_apps_excl_fargate_avg
int64
Shows the average number of Serverless Apps excluding Fargate for the given date and given org.
serverless_apps_excl_fargate_azure_container_app_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Azure Container App instances for the given date and given org.
serverless_apps_excl_fargate_azure_function_app_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Azure Function App instances for the given date and given org.
serverless_apps_excl_fargate_azure_web_app_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Azure Web App instances for the given date and given org.
serverless_apps_excl_fargate_google_cloud_functions_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Google Cloud Platform Cloud Functions instances for the given date and given org.
serverless_apps_excl_fargate_google_cloud_run_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Google Cloud Platform Cloud Run instances for the given date and given org.
serverless_apps_google_cloud_functions_instances_avg
int64
Shows the average number of Serverless Apps for Google Cloud Platform Cloud Functions instances for the given date and given org.
serverless_apps_google_cloud_run_instances_avg
int64
Shows the average number of Serverless Apps for Google Cloud Platform Cloud Run instances for the given date and given org.
serverless_apps_google_count_avg
int64
Shows the average number of Serverless Apps for Google Cloud for the given date and given org.
serverless_apps_total_count_avg
int64
Shows the average number of Serverless Apps for Azure and Google Cloud for the given date and given org.
siem_analyzed_logs_add_on_count_sum
int64
Shows the sum of all log events analyzed by Cloud SIEM over all hours in the current date for the given org.
synthetics_browser_check_calls_count_sum
int64
Shows the sum of all Synthetic browser tests over all hours in the current date for the given org.
synthetics_check_calls_count_sum
int64
Shows the sum of all Synthetic API tests over all hours in the current date for the given org.
synthetics_mobile_test_runs_sum
int64
Shows the sum of all Synthetic mobile application tests over all hours in the current date for the given org.
synthetics_parallel_testing_max_slots_hwm
int64
Shows the high-water mark of used synthetics parallel testing slots over all hours in the current date for the given org.
trace_search_indexed_events_count_sum
int64
Shows the sum of all Indexed Spans indexed over all hours in the current date for the given org.
twol_ingested_events_bytes_sum
int64
Shows the sum of all ingested APM span bytes over all hours in the current date for the given org.
universal_service_monitoring_host_top99p
int64
Shows the 99th percentile of all Universal Service Monitoring hosts over all hours in the current date for the given org.
vsphere_host_top99p
int64
Shows the 99th percentile of all vSphere hosts over all hours in the current date for the given org.
vuln_management_host_count_top99p
int64
Shows the 99th percentile of all Application Vulnerability Management hosts over all hours in the current date for the given org.
workflow_executions_usage_sum
int64
Sum of all workflows executed over all hours in the current date for the given org.
product_analytics_sum
int64
Sum of all product analytics sessions over all hours in the current date for all organizations.
profiling_aas_count_top99p
int64
Shows the 99th percentile of all profiled Azure app services over all hours in the current date for all organizations.
profiling_host_top99p
int64
Shows the 99th percentile of all profiled hosts over all hours within the current date for all organizations.
proxmox_host_sum
int64
Sum of all Proxmox hosts over all hours in the current date for all organizations.
proxmox_host_top99p
int64
99th percentile of all Proxmox hosts over all hours in the current date for all organizations.
published_app_hwm
int64
Shows the high-water mark of all published applications over all hours in the current date for all organizations.
rum_browser_and_mobile_session_count
int64
Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
rum_browser_legacy_session_count_sum
int64
Shows the sum of all browser RUM legacy sessions over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_browser_lite_session_count_sum
int64
Shows the sum of all browser RUM lite sessions over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_browser_replay_session_count_sum
int64
Shows the sum of all browser RUM Session Replay counts over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_indexed_sessions_sum
int64
Sum of all RUM indexed sessions over all hours in the current date for all organizations.
rum_ingested_sessions_sum
int64
Sum of all RUM ingested sessions over all hours in the current date for all organizations.
rum_lite_session_count_sum
int64
Shows the sum of all RUM lite sessions (browser and mobile) over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_android_sum
int64
Shows the sum of all mobile RUM legacy sessions on Android over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_flutter_sum
int64
Shows the sum of all mobile RUM legacy Sessions on Flutter over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_ios_sum
int64
Shows the sum of all mobile RUM legacy sessions on iOS over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_reactnative_sum
int64
Shows the sum of all mobile RUM legacy sessions on React Native over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_legacy_session_count_roku_sum
int64
Shows the sum of all mobile RUM legacy sessions on Roku over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_android_sum
int64
Shows the sum of all mobile RUM lite sessions on Android over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_flutter_sum
int64
Shows the sum of all mobile RUM lite sessions on Flutter over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_ios_sum
int64
Shows the sum of all mobile RUM lite sessions on iOS over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_kotlinmultiplatform_sum
int64
Shows the sum of all mobile RUM lite sessions on Kotlin Multiplatform over all hours within the current date for all organizations.
rum_mobile_lite_session_count_reactnative_sum
int64
Shows the sum of all mobile RUM lite sessions on React Native over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_roku_sum
int64
Shows the sum of all mobile RUM lite sessions on Roku over all hours within the current date for all organizations (To be introduced on October 1st, 2024).
rum_mobile_lite_session_count_unity_sum
int64
Shows the sum of all mobile RUM lite sessions on Unity over all hours within the current date for all organizations.
rum_mobile_replay_session_count_android_sum
int64
Shows the sum of all mobile RUM replay sessions on Android over all hours within the current date for the given org.
rum_mobile_replay_session_count_ios_sum
int64
Shows the sum of all mobile RUM replay sessions on iOS over all hours within the current date for the given org.
rum_mobile_replay_session_count_kotlinmultiplatform_sum
int64
Shows the sum of all mobile RUM replay sessions on Kotlin Multiplatform over all hours within the current date for all organizations.
rum_mobile_replay_session_count_reactnative_sum
int64
Shows the sum of all mobile RUM replay sessions on React Native over all hours within the current date for the given org.
rum_replay_session_count_sum
int64
Shows the sum of all RUM Session Replay counts over all hours in the current date for all organizations (To be introduced on October 1st, 2024).
rum_session_count_sum
int64
**DEPRECATED** : Shows the sum of all browser RUM lite sessions over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
rum_session_replay_add_on_sum
int64
Sum of all RUM session replay add-on sessions over all hours in the current date for all organizations.
rum_total_session_count_sum
int64
Shows the sum of RUM sessions (browser and mobile) over all hours in the current date for all organizations.
rum_units_sum
int64
**DEPRECATED** : Shows the sum of all browser and mobile RUM units over all hours in the current date for all organizations (To be deprecated on October 1st, 2024).
sca_fargate_count_avg
int64
Shows the average of all Software Composition Analysis Fargate tasks over all hours in the current date for the given org.
sca_fargate_count_hwm
int64
Shows the sum of the high-water marks of all Software Composition Analysis Fargate tasks over all hours in the current date for the given org.
sds_apm_scanned_bytes_sum
int64
Sum of all APM bytes scanned with sensitive data scanner over all hours in the current date for all organizations.
sds_events_scanned_bytes_sum
int64
Sum of all event stream events bytes scanned with sensitive data scanner over all hours in the current date for all organizations.
sds_logs_scanned_bytes_sum
int64
Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for all organizations.
sds_rum_scanned_bytes_sum
int64
Sum of all RUM bytes scanned with sensitive data scanner over all hours in the current date for all organizations.
sds_total_scanned_bytes_sum
int64
Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for all organizations.
serverless_apps_apm_apm_azure_appservice_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Azure App Service instances for the current date for all organizations.
serverless_apps_apm_apm_azure_azurefunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Azure Function instances for the current date for all organizations.
serverless_apps_apm_apm_azure_containerapp_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Azure Container App instances for the current date for all organizations.
serverless_apps_apm_apm_fargate_ecs_tasks_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Fargate Elastic Container Service tasks for the current date for all organizations.
serverless_apps_apm_apm_gcp_cloudfunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Google Cloud Platform Cloud Function instances for the current date for all organizations.
serverless_apps_apm_apm_gcp_cloudrun_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for Google Cloud Platform Cloud Run instances for the current date for all organizations.
serverless_apps_apm_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring for the current date for all organizations.
serverless_apps_apm_excl_fargate_apm_azure_appservice_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure App Service instances for the current date for all organizations.
serverless_apps_apm_excl_fargate_apm_azure_azurefunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure Function instances for the current date for all organizations.
serverless_apps_apm_excl_fargate_apm_azure_containerapp_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Azure Container App instances for the current date for all organizations.
serverless_apps_apm_excl_fargate_apm_gcp_cloudfunction_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Google Cloud Platform Cloud Function instances for the current date for all organizations.
serverless_apps_apm_excl_fargate_apm_gcp_cloudrun_instances_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for Google Cloud Platform Cloud Run instances for the current date for all organizations.
serverless_apps_apm_excl_fargate_avg
int64
Shows the average number of Serverless Apps with Application Performance Monitoring excluding Fargate for the current date for all organizations.
serverless_apps_azure_container_app_instances_avg
int64
Shows the average number of Serverless Apps for Azure Container App instances for the current date for all organizations.
serverless_apps_azure_count_avg
int64
Shows the average number of Serverless Apps for Azure for the given date and given org.
serverless_apps_azure_function_app_instances_avg
int64
Shows the average number of Serverless Apps for Azure Function App instances for the current date for all organizations.
serverless_apps_azure_web_app_instances_avg
int64
Shows the average number of Serverless Apps for Azure Web App instances for the current date for all organizations.
serverless_apps_ecs_avg
int64
Shows the average number of Serverless Apps for Elastic Container Service for the current date for all organizations.
serverless_apps_eks_avg
int64
Shows the average number of Serverless Apps for Elastic Kubernetes Service for the current date for all organizations.
serverless_apps_excl_fargate_avg
int64
Shows the average number of Serverless Apps excluding Fargate for the current date for all organizations.
serverless_apps_excl_fargate_azure_container_app_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Azure Container App instances for the current date for all organizations.
serverless_apps_excl_fargate_azure_function_app_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Azure Function App instances for the current date for all organizations.
serverless_apps_excl_fargate_azure_web_app_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Azure Web App instances for the current date for all organizations.
serverless_apps_excl_fargate_google_cloud_functions_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Google Cloud Platform Cloud Functions instances for the current date for all organizations.
serverless_apps_excl_fargate_google_cloud_run_instances_avg
int64
Shows the average number of Serverless Apps excluding Fargate for Google Cloud Platform Cloud Run instances for the current date for all organizations.
serverless_apps_google_cloud_functions_instances_avg
int64
Shows the average number of Serverless Apps for Google Cloud Platform Cloud Functions instances for the current date for all organizations.
serverless_apps_google_cloud_run_instances_avg
int64
Shows the average number of Serverless Apps for Google Cloud Platform Cloud Run instances for the current date for all organizations.
serverless_apps_google_count_avg
int64
Shows the average number of Serverless Apps for Google Cloud for the given date and given org.
serverless_apps_total_count_avg
int64
Shows the average number of Serverless Apps for Azure and Google Cloud for the given date and given org.
siem_analyzed_logs_add_on_count_sum
int64
Shows the sum of all log events analyzed by Cloud SIEM over all hours in the current date for the given org.
synthetics_browser_check_calls_count_sum
int64
Shows the sum of all Synthetic browser tests over all hours in the current date for all organizations.
synthetics_check_calls_count_sum
int64
Shows the sum of all Synthetic API tests over all hours in the current date for all organizations.
synthetics_mobile_test_runs_sum
int64
Shows the sum of all Synthetic mobile application tests over all hours in the current date for all organizations.
synthetics_parallel_testing_max_slots_hwm
int64
Shows the high-water mark of used synthetics parallel testing slots over all hours in the current date for all organizations.
trace_search_indexed_events_count_sum
int64
Shows the sum of all Indexed Spans indexed over all hours in the current date for all organizations.
twol_ingested_events_bytes_sum
int64
Shows the sum of all ingested APM span bytes over all hours in the current date for all organizations.
universal_service_monitoring_host_top99p
int64
Shows the 99th percentile of all universal service management hosts over all hours in the current date for the given org.
vsphere_host_top99p
int64
Shows the 99th percentile of all vSphere hosts over all hours in the current date for all organizations.
vuln_management_host_count_top99p
int64
Shows the 99th percentile of all Application Vulnerability Management hosts over all hours in the current date for the given org.
workflow_executions_usage_sum
int64
Sum of all workflows executed over all hours in the current date for all organizations.
vsphere_host_top99p_sum
int64
Shows the 99th percentile of all vSphere hosts over all hours in the current month for all organizations.
vuln_management_host_count_top99p_sum
int64
Shows the 99th percentile of all Application Vulnerability Management hosts over all hours in the current month for all organizations.
workflow_executions_usage_agg_sum
int64
Sum of all workflows executed over all hours in the current month for all organizations.
```
{
  "agent_host_top99p_sum": "integer",
  "apm_azure_app_service_host_top99p_sum": "integer",
  "apm_devsecops_host_top99p_sum": "integer",
  "apm_enterprise_standalone_hosts_top99p_sum": "integer",
  "apm_fargate_count_avg_sum": "integer",
  "apm_host_top99p_sum": "integer",
  "apm_pro_standalone_hosts_top99p_sum": "integer",
  "appsec_fargate_count_avg_sum": "integer",
  "asm_serverless_agg_sum": "integer",
  "audit_logs_lines_indexed_agg_sum": "integer",
  "audit_trail_enabled_hwm_sum": "integer",
  "avg_profiled_fargate_tasks_sum": "integer",
  "aws_host_top99p_sum": "integer",
  "aws_lambda_func_count": "integer",
  "aws_lambda_invocations_sum": "integer",
  "azure_app_service_top99p_sum": "integer",
  "azure_host_top99p_sum": "integer",
  "billable_ingested_bytes_agg_sum": "integer",
  "bits_ai_investigations_agg_sum": "integer",
  "browser_rum_lite_session_count_agg_sum": "integer",
  "browser_rum_replay_session_count_agg_sum": "integer",
  "browser_rum_units_agg_sum": "integer",
  "ci_pipeline_indexed_spans_agg_sum": "integer",
  "ci_test_indexed_spans_agg_sum": "integer",
  "ci_visibility_itr_committers_hwm_sum": "integer",
  "ci_visibility_pipeline_committers_hwm_sum": "integer",
  "ci_visibility_test_committers_hwm_sum": "integer",
  "cloud_cost_management_aws_host_count_avg_sum": "integer",
  "cloud_cost_management_azure_host_count_avg_sum": "integer",
  "cloud_cost_management_gcp_host_count_avg_sum": "integer",
  "cloud_cost_management_host_count_avg_sum": "integer",
  "cloud_cost_management_oci_host_count_avg_sum": "integer",
  "cloud_siem_events_agg_sum": "integer",
  "code_analysis_sa_committers_hwm_sum": "integer",
  "code_analysis_sca_committers_hwm_sum": "integer",
  "code_security_host_top99p_sum": "integer",
  "container_avg_sum": "integer",
  "container_excl_agent_avg_sum": "integer",
  "container_hwm_sum": "integer",
  "csm_container_enterprise_compliance_count_agg_sum": "integer",
  "csm_container_enterprise_cws_count_agg_sum": "integer",
  "csm_container_enterprise_total_count_agg_sum": "integer",
  "csm_host_enterprise_aas_host_count_top99p_sum": "integer",
  "csm_host_enterprise_aws_host_count_top99p_sum": "integer",
  "csm_host_enterprise_azure_host_count_top99p_sum": "integer",
  "csm_host_enterprise_compliance_host_count_top99p_sum": "integer",
  "csm_host_enterprise_cws_host_count_top99p_sum": "integer",
  "csm_host_enterprise_gcp_host_count_top99p_sum": "integer",
  "csm_host_enterprise_total_host_count_top99p_sum": "integer",
  "cspm_aas_host_top99p_sum": "integer",
  "cspm_aws_host_top99p_sum": "integer",
  "cspm_azure_host_top99p_sum": "integer",
  "cspm_container_avg_sum": "integer",
  "cspm_container_hwm_sum": "integer",
  "cspm_gcp_host_top99p_sum": "integer",
  "cspm_host_top99p_sum": "integer",
  "custom_historical_ts_sum": "integer",
  "custom_live_ts_sum": "integer",
  "custom_ts_sum": "integer",
  "cws_container_avg_sum": "integer",
  "cws_fargate_task_avg_sum": "integer",
  "cws_host_top99p_sum": "integer",
  "data_jobs_monitoring_host_hr_agg_sum": "integer",
  "dbm_host_top99p_sum": "integer",
  "dbm_queries_avg_sum": "integer",
  "end_date": "2019-09-19T10:00:00.000Z",
  "eph_infra_host_agent_agg_sum": "integer",
  "eph_infra_host_alibaba_agg_sum": "integer",
  "eph_infra_host_aws_agg_sum": "integer",
  "eph_infra_host_azure_agg_sum": "integer",
  "eph_infra_host_ent_agg_sum": "integer",
  "eph_infra_host_gcp_agg_sum": "integer",
  "eph_infra_host_heroku_agg_sum": "integer",
  "eph_infra_host_only_aas_agg_sum": "integer",
  "eph_infra_host_only_vsphere_agg_sum": "integer",
  "eph_infra_host_opentelemetry_agg_sum": "integer",
  "eph_infra_host_opentelemetry_apm_agg_sum": "integer",
  "eph_infra_host_pro_agg_sum": "integer",
  "eph_infra_host_proplus_agg_sum": "integer",
  "eph_infra_host_proxmox_agg_sum": "integer",
  "error_tracking_apm_error_events_agg_sum": "integer",
  "error_tracking_error_events_agg_sum": "integer",
  "error_tracking_events_agg_sum": "integer",
  "error_tracking_rum_error_events_agg_sum": "integer",
  "event_management_correlation_agg_sum": "integer",
  "event_management_correlation_correlated_events_agg_sum": "integer",
  "event_management_correlation_correlated_related_events_agg_sum": "integer",
  "fargate_container_profiler_profiling_fargate_avg_sum": "integer",
  "fargate_container_profiler_profiling_fargate_eks_avg_sum": "integer",
  "fargate_tasks_count_avg_sum": "integer",
  "fargate_tasks_count_hwm_sum": "integer",
  "flex_logs_compute_large_avg_sum": "integer",
  "flex_logs_compute_medium_avg_sum": "integer",
  "flex_logs_compute_small_avg_sum": "integer",
  "flex_logs_compute_xlarge_avg_sum": "integer",
  "flex_logs_compute_xsmall_avg_sum": "integer",
  "flex_logs_starter_avg_sum": "integer",
  "flex_logs_starter_storage_index_avg_sum": "integer",
  "flex_logs_starter_storage_retention_adjustment_avg_sum": "integer",
  "flex_stored_logs_avg_sum": "integer",
  "forwarding_events_bytes_agg_sum": "integer",
  "gcp_host_top99p_sum": "integer",
  "heroku_host_top99p_sum": "integer",
  "incident_management_monthly_active_users_hwm_sum": "integer",
  "incident_management_seats_hwm_sum": "integer",
  "indexed_events_count_agg_sum": "integer",
  "infra_host_top99p_sum": "integer",
  "ingested_events_bytes_agg_sum": "integer",
  "iot_device_agg_sum": "integer",
  "iot_device_top99p_sum": "integer",
  "last_updated": "2019-09-19T10:00:00.000Z",
  "live_indexed_events_agg_sum": "integer",
  "live_ingested_bytes_agg_sum": "integer",
  "llm_observability_agg_sum": "integer",
  "llm_observability_min_spend_agg_sum": "integer",
  "logs_by_retention": {
    "orgs": {
      "usage": [
        {
          "usage": [
            {
              "logs_indexed_logs_usage_sum": "integer",
              "logs_live_indexed_logs_usage_sum": "integer",
              "logs_rehydrated_indexed_logs_usage_sum": "integer",
              "retention": "string"
            }
          ]
        }
      ]
    },
    "usage": [
      {
        "logs_indexed_logs_usage_agg_sum": "integer",
        "logs_live_indexed_logs_usage_agg_sum": "integer",
        "logs_rehydrated_indexed_logs_usage_agg_sum": "integer",
        "retention": "string"
      }
    ],
    "usage_by_month": {
      "date": "2019-09-19T10:00:00.000Z",
      "usage": [
        {
          "logs_indexed_logs_usage_sum": "integer",
          "logs_live_indexed_logs_usage_sum": "integer",
          "logs_rehydrated_indexed_logs_usage_sum": "integer",
          "retention": "string"
        }
      ]
    }
  },
  "mobile_rum_lite_session_count_agg_sum": "integer",
  "mobile_rum_session_count_agg_sum": "integer",
  "mobile_rum_session_count_android_agg_sum": "integer",
  "mobile_rum_session_count_flutter_agg_sum": "integer",
  "mobile_rum_session_count_ios_agg_sum": "integer",
  "mobile_rum_session_count_reactnative_agg_sum": "integer",
  "mobile_rum_session_count_roku_agg_sum": "integer",
  "mobile_rum_units_agg_sum": "integer",
  "ndm_netflow_events_agg_sum": "integer",
  "netflow_indexed_events_count_agg_sum": "integer",
  "network_device_wireless_top99p_sum": "integer",
  "npm_host_top99p_sum": "integer",
  "observability_pipelines_bytes_processed_agg_sum": "integer",
  "oci_host_agg_sum": "integer",
  "oci_host_top99p_sum": "integer",
  "on_call_seat_hwm_sum": "integer",
  "online_archive_events_count_agg_sum": "integer",
  "opentelemetry_apm_host_top99p_sum": "integer",
  "opentelemetry_host_top99p_sum": "integer",
  "product_analytics_agg_sum": "integer",
  "profiling_aas_count_top99p_sum": "integer",
  "profiling_container_agent_count_avg": "integer",
  "profiling_host_count_top99p_sum": "integer",
  "proxmox_host_agg_sum": "integer",
  "proxmox_host_top99p_sum": "integer",
  "published_app_hwm_sum": "integer",
  "rehydrated_indexed_events_agg_sum": "integer",
  "rehydrated_ingested_bytes_agg_sum": "integer",
  "rum_browser_and_mobile_session_count": "integer",
  "rum_browser_legacy_session_count_agg_sum": "integer",
  "rum_browser_lite_session_count_agg_sum": "integer",
  "rum_browser_replay_session_count_agg_sum": "integer",
  "rum_indexed_sessions_agg_sum": "integer",
  "rum_ingested_sessions_agg_sum": "integer",
  "rum_lite_session_count_agg_sum": "integer",
  "rum_mobile_legacy_session_count_android_agg_sum": "integer",
  "rum_mobile_legacy_session_count_flutter_agg_sum": "integer",
  "rum_mobile_legacy_session_count_ios_agg_sum": "integer",
  "rum_mobile_legacy_session_count_reactnative_agg_sum": "integer",
  "rum_mobile_legacy_session_count_roku_agg_sum": "integer",
  "rum_mobile_lite_session_count_android_agg_sum": "integer",
  "rum_mobile_lite_session_count_flutter_agg_sum": "integer",
  "rum_mobile_lite_session_count_ios_agg_sum": "integer",
  "rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum": "integer",
  "rum_mobile_lite_session_count_reactnative_agg_sum": "integer",
  "rum_mobile_lite_session_count_roku_agg_sum": "integer",
  "rum_mobile_lite_session_count_unity_agg_sum": "integer",
  "rum_mobile_replay_session_count_android_agg_sum": "integer",
  "rum_mobile_replay_session_count_ios_agg_sum": "integer",
  "rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum": "integer",
  "rum_mobile_replay_session_count_reactnative_agg_sum": "integer",
  "rum_replay_session_count_agg_sum": "integer",
  "rum_session_count_agg_sum": "integer",
  "rum_session_replay_add_on_agg_sum": "integer",
  "rum_total_session_count_agg_sum": "integer",
  "rum_units_agg_sum": "integer",
  "sca_fargate_count_avg_sum": "integer",
  "sca_fargate_count_hwm_sum": "integer",
  "sds_apm_scanned_bytes_sum": "integer",
  "sds_events_scanned_bytes_sum": "integer",
  "sds_logs_scanned_bytes_sum": "integer",
  "sds_rum_scanned_bytes_sum": "integer",
  "sds_total_scanned_bytes_sum": "integer",
  "serverless_apps_apm_apm_azure_appservice_instances_avg_sum": "integer",
  "serverless_apps_apm_apm_azure_azurefunction_instances_avg_sum": "integer",
  "serverless_apps_apm_apm_azure_containerapp_instances_avg_sum": "integer",
  "serverless_apps_apm_apm_fargate_ecs_tasks_avg_sum": "integer",
  "serverless_apps_apm_apm_gcp_cloudfunction_instances_avg_sum": "integer",
  "serverless_apps_apm_apm_gcp_cloudrun_instances_avg_sum": "integer",
  "serverless_apps_apm_avg_sum": "integer",
  "serverless_apps_apm_excl_fargate_apm_azure_appservice_instances_avg_sum": "integer",
  "serverless_apps_apm_excl_fargate_apm_azure_azurefunction_instances_avg_sum": "integer",
  "serverless_apps_apm_excl_fargate_apm_azure_containerapp_instances_avg_sum": "integer",
  "serverless_apps_apm_excl_fargate_apm_gcp_cloudfunction_instances_avg_sum": "integer",
  "serverless_apps_apm_excl_fargate_apm_gcp_cloudrun_instances_avg_sum": "integer",
  "serverless_apps_apm_excl_fargate_avg_sum": "integer",
  "serverless_apps_azure_container_app_instances_avg_sum": "integer",
  "serverless_apps_azure_count_avg_sum": "integer",
  "serverless_apps_azure_function_app_instances_avg_sum": "integer",
  "serverless_apps_azure_web_app_instances_avg_sum": "integer",
  "serverless_apps_ecs_avg_sum": "integer",
  "serverless_apps_eks_avg_sum": "integer",
  "serverless_apps_excl_fargate_avg_sum": "integer",
  "serverless_apps_excl_fargate_azure_container_app_instances_avg_sum": "integer",
  "serverless_apps_excl_fargate_azure_function_app_instances_avg_sum": "integer",
  "serverless_apps_excl_fargate_azure_web_app_instances_avg_sum": "integer",
  "serverless_apps_excl_fargate_google_cloud_functions_instances_avg_sum": "integer",
  "serverless_apps_excl_fargate_google_cloud_run_instances_avg_sum": "integer",
  "serverless_apps_google_cloud_functions_instances_avg_sum": "integer",
  "serverless_apps_google_cloud_run_instances_avg_sum": "integer",
  "serverless_apps_google_count_avg_sum": "integer",
  "serverless_apps_total_count_avg_sum": "integer",
  "siem_analyzed_logs_add_on_count_agg_sum": "integer",
  "start_date": "2019-09-19T10:00:00.000Z",
  "synthetics_browser_check_calls_count_agg_sum": "integer",
  "synthetics_check_calls_count_agg_sum": "integer",
  "synthetics_mobile_test_runs_agg_sum": "integer",
  "synthetics_parallel_testing_max_slots_hwm_sum": "integer",
  "trace_search_indexed_events_count_agg_sum": "integer",
  "twol_ingested_events_bytes_agg_sum": "integer",
  "universal_service_monitoring_host_top99p_sum": "integer",
  "usage": [
    {
      "agent_host_top99p": "integer",
      "apm_azure_app_service_host_top99p": "integer",
      "apm_devsecops_host_top99p": "integer",
      "apm_enterprise_standalone_hosts_top99p": "integer",
      "apm_fargate_count_avg": "integer",
      "apm_host_top99p": "integer",
      "apm_pro_standalone_hosts_top99p": "integer",
      "appsec_fargate_count_avg": "integer",
      "asm_serverless_sum": "integer",
      "audit_logs_lines_indexed_sum": "integer",
      "audit_trail_enabled_hwm": "integer",
      "avg_profiled_fargate_tasks": "integer",
      "aws_host_top99p": "integer",
      "aws_lambda_func_count": "integer",
      "aws_lambda_invocations_sum": "integer",
      "azure_app_service_top99p": "integer",
      "billable_ingested_bytes_sum": "integer",
      "bits_ai_investigations_sum": "integer",
      "browser_rum_lite_session_count_sum": "integer",
      "browser_rum_replay_session_count_sum": "integer",
      "browser_rum_units_sum": "integer",
      "ci_pipeline_indexed_spans_sum": "integer",
      "ci_test_indexed_spans_sum": "integer",
      "ci_visibility_itr_committers_hwm": "integer",
      "ci_visibility_pipeline_committers_hwm": "integer",
      "ci_visibility_test_committers_hwm": "integer",
      "cloud_cost_management_aws_host_count_avg": "integer",
      "cloud_cost_management_azure_host_count_avg": "integer",
      "cloud_cost_management_gcp_host_count_avg": "integer",
      "cloud_cost_management_host_count_avg": "integer",
      "cloud_cost_management_oci_host_count_avg": "integer",
      "cloud_siem_events_sum": "integer",
      "code_analysis_sa_committers_hwm": "integer",
      "code_analysis_sca_committers_hwm": "integer",
      "code_security_host_top99p": "integer",
      "container_avg": "integer",
      "container_excl_agent_avg": "integer",
      "container_hwm": "integer",
      "csm_container_enterprise_compliance_count_sum": "integer",
      "csm_container_enterprise_cws_count_sum": "integer",
      "csm_container_enterprise_total_count_sum": "integer",
      "csm_host_enterprise_aas_host_count_top99p": "integer",
      "csm_host_enterprise_aws_host_count_top99p": "integer",
      "csm_host_enterprise_azure_host_count_top99p": "integer",
      "csm_host_enterprise_compliance_host_count_top99p": "integer",
      "csm_host_enterprise_cws_host_count_top99p": "integer",
      "csm_host_enterprise_gcp_host_count_top99p": "integer",
      "csm_host_enterprise_total_host_count_top99p": "integer",
      "cspm_aas_host_top99p": "integer",
      "cspm_aws_host_top99p": "integer",
      "cspm_azure_host_top99p": "integer",
      "cspm_container_avg": "integer",
      "cspm_container_hwm": "integer",
      "cspm_gcp_host_top99p": "integer",
      "cspm_host_top99p": "integer",
      "custom_ts_avg": "integer",
      "cws_container_count_avg": "integer",
      "cws_fargate_task_avg": "integer",
      "cws_host_top99p": "integer",
      "data_jobs_monitoring_host_hr_sum": "integer",
      "date": "2019-09-19T10:00:00.000Z",
      "dbm_host_top99p": "integer",
      "dbm_queries_count_avg": "integer",
      "eph_infra_host_agent_sum": "integer",
      "eph_infra_host_alibaba_sum": "integer",
      "eph_infra_host_aws_sum": "integer",
      "eph_infra_host_azure_sum": "integer",
      "eph_infra_host_ent_sum": "integer",
      "eph_infra_host_gcp_sum": "integer",
      "eph_infra_host_heroku_sum": "integer",
      "eph_infra_host_only_aas_sum": "integer",
      "eph_infra_host_only_vsphere_sum": "integer",
      "eph_infra_host_opentelemetry_apm_sum": "integer",
      "eph_infra_host_opentelemetry_sum": "integer",
      "eph_infra_host_pro_sum": "integer",
      "eph_infra_host_proplus_sum": "integer",
      "eph_infra_host_proxmox_sum": "integer",
      "error_tracking_apm_error_events_sum": "integer",
      "error_tracking_error_events_sum": "integer",
      "error_tracking_events_sum": "integer",
      "error_tracking_rum_error_events_sum": "integer",
      "event_management_correlation_correlated_events_sum": "integer",
      "event_management_correlation_correlated_related_events_sum": "integer",
      "event_management_correlation_sum": "integer",
      "fargate_container_profiler_profiling_fargate_avg": "integer",
      "fargate_container_profiler_profiling_fargate_eks_avg": "integer",
      "fargate_tasks_count_avg": "integer",
      "fargate_tasks_count_hwm": "integer",
      "flex_logs_compute_large_avg": "integer",
      "flex_logs_compute_medium_avg": "integer",
      "flex_logs_compute_small_avg": "integer",
      "flex_logs_compute_xlarge_avg": "integer",
      "flex_logs_compute_xsmall_avg": "integer",
      "flex_logs_starter_avg": "integer",
      "flex_logs_starter_storage_index_avg": "integer",
      "flex_logs_starter_storage_retention_adjustment_avg": "integer",
      "flex_stored_logs_avg": "integer",
      "forwarding_events_bytes_sum": "integer",
      "gcp_host_top99p": "integer",
      "heroku_host_top99p": "integer",
      "incident_management_monthly_active_users_hwm": "integer",
      "incident_management_seats_hwm": "integer",
      "indexed_events_count_sum": "integer",
      "infra_host_top99p": "integer",
      "ingested_events_bytes_sum": "integer",
      "iot_device_sum": "integer",
      "iot_device_top99p": "integer",
      "llm_observability_min_spend_sum": "integer",
      "llm_observability_sum": "integer",
      "mobile_rum_lite_session_count_sum": "integer",
      "mobile_rum_session_count_android_sum": "integer",
      "mobile_rum_session_count_flutter_sum": "integer",
      "mobile_rum_session_count_ios_sum": "integer",
      "mobile_rum_session_count_reactnative_sum": "integer",
      "mobile_rum_session_count_roku_sum": "integer",
      "mobile_rum_session_count_sum": "integer",
      "mobile_rum_units_sum": "integer",
      "ndm_netflow_events_sum": "integer",
      "netflow_indexed_events_count_sum": "integer",
      "network_device_wireless_top99p": "integer",
      "npm_host_top99p": "integer",
      "observability_pipelines_bytes_processed_sum": "integer",
      "oci_host_sum": "integer",
      "oci_host_top99p": "integer",
      "on_call_seat_hwm": "integer",
      "online_archive_events_count_sum": "integer",
      "opentelemetry_apm_host_top99p": "integer",
      "opentelemetry_host_top99p": "integer",
      "orgs": [
        {
          "account_name": "string",
          "account_public_id": "string",
          "agent_host_top99p": "integer",
          "apm_azure_app_service_host_top99p": "integer",
          "apm_devsecops_host_top99p": "integer",
          "apm_enterprise_standalone_hosts_top99p": "integer",
          "apm_fargate_count_avg": "integer",
          "apm_host_top99p": "integer",
          "apm_pro_standalone_hosts_top99p": "integer",
          "appsec_fargate_count_avg": "integer",
          "asm_serverless_sum": "integer",
          "audit_logs_lines_indexed_sum": "integer",
          "audit_trail_enabled_hwm": "integer",
          "avg_profiled_fargate_tasks": "integer",
          "aws_host_top99p": "integer",
          "aws_lambda_func_count": "integer",
          "aws_lambda_invocations_sum": "integer",
          "azure_app_service_top99p": "integer",
          "billable_ingested_bytes_sum": "integer",
          "bits_ai_investigations_sum": "integer",
          "browser_rum_lite_session_count_sum": "integer",
          "browser_rum_replay_session_count_sum": "integer",
          "browser_rum_units_sum": "integer",
          "ci_pipeline_indexed_spans_sum": "integer",
          "ci_test_indexed_spans_sum": "integer",
          "ci_visibility_itr_committers_hwm": "integer",
          "ci_visibility_pipeline_committers_hwm": "integer",
          "ci_visibility_test_committers_hwm": "integer",
          "cloud_cost_management_aws_host_count_avg": "integer",
          "cloud_cost_management_azure_host_count_avg": "integer",
          "cloud_cost_management_gcp_host_count_avg": "integer",
          "cloud_cost_management_host_count_avg": "integer",
          "cloud_cost_management_oci_host_count_avg": "integer",
          "cloud_siem_events_sum": "integer",
          "code_analysis_sa_committers_hwm": "integer",
          "code_analysis_sca_committers_hwm": "integer",
          "code_security_host_top99p": "integer",
          "container_avg": "integer",
          "container_excl_agent_avg": "integer",
          "container_hwm": "integer",
          "csm_container_enterprise_compliance_count_sum": "integer",
          "csm_container_enterprise_cws_count_sum": "integer",
          "csm_container_enterprise_total_count_sum": "integer",
          "csm_host_enterprise_aas_host_count_top99p": "integer",
          "csm_host_enterprise_aws_host_count_top99p": "integer",
          "csm_host_enterprise_azure_host_count_top99p": "integer",
          "csm_host_enterprise_compliance_host_count_top99p": "integer",
          "csm_host_enterprise_cws_host_count_top99p": "integer",
          "csm_host_enterprise_gcp_host_count_top99p": "integer",
          "csm_host_enterprise_total_host_count_top99p": "integer",
          "cspm_aas_host_top99p": "integer",
          "cspm_aws_host_top99p": "integer",
          "cspm_azure_host_top99p": "integer",
          "cspm_container_avg": "integer",
          "cspm_container_hwm": "integer",
          "cspm_gcp_host_top99p": "integer",
          "cspm_host_top99p": "integer",
          "custom_historical_ts_avg": "integer",
          "custom_live_ts_avg": "integer",
          "custom_ts_avg": "integer",
          "cws_container_count_avg": "integer",
          "cws_fargate_task_avg": "integer",
          "cws_host_top99p": "integer",
          "data_jobs_monitoring_host_hr_sum": "integer",
          "dbm_host_top99p_sum": "integer",
          "dbm_queries_avg_sum": "integer",
          "eph_infra_host_agent_sum": "integer",
          "eph_infra_host_alibaba_sum": "integer",
          "eph_infra_host_aws_sum": "integer",
          "eph_infra_host_azure_sum": "integer",
          "eph_infra_host_ent_sum": "integer",
          "eph_infra_host_gcp_sum": "integer",
          "eph_infra_host_heroku_sum": "integer",
          "eph_infra_host_only_aas_sum": "integer",
          "eph_infra_host_only_vsphere_sum": "integer",
          "eph_infra_host_opentelemetry_apm_sum": "integer",
          "eph_infra_host_opentelemetry_sum": "integer",
          "eph_infra_host_pro_sum": "integer",
          "eph_infra_host_proplus_sum": "integer",
          "eph_infra_host_proxmox_sum": "integer",
          "error_tracking_apm_error_events_sum": "integer",
          "error_tracking_error_events_sum": "integer",
          "error_tracking_events_sum": "integer",
          "error_tracking_rum_error_events_sum": "integer",
          "event_management_correlation_correlated_events_sum": "integer",
          "event_management_correlation_correlated_related_events_sum": "integer",
          "event_management_correlation_sum": "integer",
          "fargate_container_profiler_profiling_fargate_avg": "integer",
          "fargate_container_profiler_profiling_fargate_eks_avg": "integer",
          "fargate_tasks_count_avg": "integer",
          "fargate_tasks_count_hwm": "integer",
          "flex_logs_compute_large_avg": "integer",
          "flex_logs_compute_medium_avg": "integer",
          "flex_logs_compute_small_avg": "integer",
          "flex_logs_compute_xlarge_avg": "integer",
          "flex_logs_compute_xsmall_avg": "integer",
          "flex_logs_starter_avg": "integer",
          "flex_logs_starter_storage_index_avg": "integer",
          "flex_logs_starter_storage_retention_adjustment_avg": "integer",
          "flex_stored_logs_avg": "integer",
          "forwarding_events_bytes_sum": "integer",
          "gcp_host_top99p": "integer",
          "heroku_host_top99p": "integer",
          "id": "string",
          "incident_management_monthly_active_users_hwm": "integer",
          "incident_management_seats_hwm": "integer",
          "indexed_events_count_sum": "integer",
          "infra_host_top99p": "integer",
          "ingested_events_bytes_sum": "integer",
          "iot_device_agg_sum": "integer",
          "iot_device_top99p_sum": "integer",
          "llm_observability_min_spend_sum": "integer",
          "llm_observability_sum": "integer",
          "mobile_rum_lite_session_count_sum": "integer",
          "mobile_rum_session_count_android_sum": "integer",
          "mobile_rum_session_count_flutter_sum": "integer",
          "mobile_rum_session_count_ios_sum": "integer",
          "mobile_rum_session_count_reactnative_sum": "integer",
          "mobile_rum_session_count_roku_sum": "integer",
          "mobile_rum_session_count_sum": "integer",
          "mobile_rum_units_sum": "integer",
          "name": "string",
          "ndm_netflow_events_sum": "integer",
          "netflow_indexed_events_count_sum": "integer",
          "network_device_wireless_top99p": "integer",
          "npm_host_top99p": "integer",
          "observability_pipelines_bytes_processed_sum": "integer",
          "oci_host_sum": "integer",
          "oci_host_top99p": "integer",
          "on_call_seat_hwm": "integer",
          "online_archive_events_count_sum": "integer",
          "opentelemetry_apm_host_top99p": "integer",
          "opentelemetry_host_top99p": "integer",
          "product_analytics_sum": "integer",
          "profiling_aas_count_top99p": "integer",
          "profiling_host_top99p": "integer",
          "proxmox_host_sum": "integer",
          "proxmox_host_top99p": "integer",
          "public_id": "string",
          "published_app_hwm": "integer",
          "region": "string",
          "rum_browser_and_mobile_session_count": "integer",
          "rum_browser_legacy_session_count_sum": "integer",
          "rum_browser_lite_session_count_sum": "integer",
          "rum_browser_replay_session_count_sum": "integer",
          "rum_indexed_sessions_sum": "integer",
          "rum_ingested_sessions_sum": "integer",
          "rum_lite_session_count_sum": "integer",
          "rum_mobile_legacy_session_count_android_sum": "integer",
          "rum_mobile_legacy_session_count_flutter_sum": "integer",
          "rum_mobile_legacy_session_count_ios_sum": "integer",
          "rum_mobile_legacy_session_count_reactnative_sum": "integer",
          "rum_mobile_legacy_session_count_roku_sum": "integer",
          "rum_mobile_lite_session_count_android_sum": "integer",
          "rum_mobile_lite_session_count_flutter_sum": "integer",
          "rum_mobile_lite_session_count_ios_sum": "integer",
          "rum_mobile_lite_session_count_kotlinmultiplatform_sum": "integer",
          "rum_mobile_lite_session_count_reactnative_sum": "integer",
          "rum_mobile_lite_session_count_roku_sum": "integer",
          "rum_mobile_lite_session_count_unity_sum": "integer",
          "rum_mobile_replay_session_count_android_sum": "integer",
          "rum_mobile_replay_session_count_ios_sum": "integer",
          "rum_mobile_replay_session_count_kotlinmultiplatform_sum": "integer",
          "rum_mobile_replay_session_count_reactnative_sum": "integer",
          "rum_replay_session_count_sum": "integer",
          "rum_session_count_sum": "integer",
          "rum_session_replay_add_on_sum": "integer",
          "rum_total_session_count_sum": "integer",
          "rum_units_sum": "integer",
          "sca_fargate_count_avg": "integer",
          "sca_fargate_count_hwm": "integer",
          "sds_apm_scanned_bytes_sum": "integer",
          "sds_events_scanned_bytes_sum": "integer",
          "sds_logs_scanned_bytes_sum": "integer",
          "sds_rum_scanned_bytes_sum": "integer",
          "sds_total_scanned_bytes_sum": "integer",
          "serverless_apps_apm_apm_azure_appservice_instances_avg": "integer",
          "serverless_apps_apm_apm_azure_azurefunction_instances_avg": "integer",
          "serverless_apps_apm_apm_azure_containerapp_instances_avg": "integer",
          "serverless_apps_apm_apm_fargate_ecs_tasks_avg": "integer",
          "serverless_apps_apm_apm_gcp_cloudfunction_instances_avg": "integer",
          "serverless_apps_apm_apm_gcp_cloudrun_instances_avg": "integer",
          "serverless_apps_apm_avg": "integer",
          "serverless_apps_apm_excl_fargate_apm_azure_appservice_instances_avg": "integer",
          "serverless_apps_apm_excl_fargate_apm_azure_azurefunction_instances_avg": "integer",
          "serverless_apps_apm_excl_fargate_apm_azure_containerapp_instances_avg": "integer",
          "serverless_apps_apm_excl_fargate_apm_gcp_cloudfunction_instances_avg": "integer",
          "serverless_apps_apm_excl_fargate_apm_gcp_cloudrun_instances_avg": "integer",
          "serverless_apps_apm_excl_fargate_avg": "integer",
          "serverless_apps_azure_container_app_instances_avg": "integer",
          "serverless_apps_azure_count_avg": "integer",
          "serverless_apps_azure_function_app_instances_avg": "integer",
          "serverless_apps_azure_web_app_instances_avg": "integer",
          "serverless_apps_ecs_avg": "integer",
          "serverless_apps_eks_avg": "integer",
          "serverless_apps_excl_fargate_avg": "integer",
          "serverless_apps_excl_fargate_azure_container_app_instances_avg": "integer",
          "serverless_apps_excl_fargate_azure_function_app_instances_avg": "integer",
          "serverless_apps_excl_fargate_azure_web_app_instances_avg": "integer",
          "serverless_apps_excl_fargate_google_cloud_functions_instances_avg": "integer",
          "serverless_apps_excl_fargate_google_cloud_run_instances_avg": "integer",
          "serverless_apps_google_cloud_functions_instances_avg": "integer",
          "serverless_apps_google_cloud_run_instances_avg": "integer",
          "serverless_apps_google_count_avg": "integer",
          "serverless_apps_total_count_avg": "integer",
          "siem_analyzed_logs_add_on_count_sum": "integer",
          "synthetics_browser_check_calls_count_sum": "integer",
          "synthetics_check_calls_count_sum": "integer",
          "synthetics_mobile_test_runs_sum": "integer",
          "synthetics_parallel_testing_max_slots_hwm": "integer",
          "trace_search_indexed_events_count_sum": "integer",
          "twol_ingested_events_bytes_sum": "integer",
          "universal_service_monitoring_host_top99p": "integer",
          "vsphere_host_top99p": "integer",
          "vuln_management_host_count_top99p": "integer",
          "workflow_executions_usage_sum": "integer"
        }
      ],
      "product_analytics_sum": "integer",
      "profiling_aas_count_top99p": "integer",
      "profiling_host_top99p": "integer",
      "proxmox_host_sum": "integer",
      "proxmox_host_top99p": "integer",
      "published_app_hwm": "integer",
      "rum_browser_and_mobile_session_count": "integer",
      "rum_browser_legacy_session_count_sum": "integer",
      "rum_browser_lite_session_count_sum": "integer",
      "rum_browser_replay_session_count_sum": "integer",
      "rum_indexed_sessions_sum": "integer",
      "rum_ingested_sessions_sum": "integer",
      "rum_lite_session_count_sum": "integer",
      "rum_mobile_legacy_session_count_android_sum": "integer",
      "rum_mobile_legacy_session_count_flutter_sum": "integer",
      "rum_mobile_legacy_session_count_ios_sum": "integer",
      "rum_mobile_legacy_session_count_reactnative_sum": "integer",
      "rum_mobile_legacy_session_count_roku_sum": "integer",
      "rum_mobile_lite_session_count_android_sum": "integer",
      "rum_mobile_lite_session_count_flutter_sum": "integer",
      "rum_mobile_lite_session_count_ios_sum": "integer",
      "rum_mobile_lite_session_count_kotlinmultiplatform_sum": "integer",
      "rum_mobile_lite_session_count_reactnative_sum": "integer",
      "rum_mobile_lite_session_count_roku_sum": "integer",
      "rum_mobile_lite_session_count_unity_sum": "integer",
      "rum_mobile_replay_session_count_android_sum": "integer",
      "rum_mobile_replay_session_count_ios_sum": "integer",
      "rum_mobile_replay_session_count_kotlinmultiplatform_sum": "integer",
      "rum_mobile_replay_session_count_reactnative_sum": "integer",
      "rum_replay_session_count_sum": "integer",
      "rum_session_count_sum": "integer",
      "rum_session_replay_add_on_sum": "integer",
      "rum_total_session_count_sum": "integer",
      "rum_units_sum": "integer",
      "sca_fargate_count_avg": "integer",
      "sca_fargate_count_hwm": "integer",
      "sds_apm_scanned_bytes_sum": "integer",
      "sds_events_scanned_bytes_sum": "integer",
      "sds_logs_scanned_bytes_sum": "integer",
      "sds_rum_scanned_bytes_sum": "integer",
      "sds_total_scanned_bytes_sum": "integer",
      "serverless_apps_apm_apm_azure_appservice_instances_avg": "integer",
      "serverless_apps_apm_apm_azure_azurefunction_instances_avg": "integer",
      "serverless_apps_apm_apm_azure_containerapp_instances_avg": "integer",
      "serverless_apps_apm_apm_fargate_ecs_tasks_avg": "integer",
      "serverless_apps_apm_apm_gcp_cloudfunction_instances_avg": "integer",
      "serverless_apps_apm_apm_gcp_cloudrun_instances_avg": "integer",
      "serverless_apps_apm_avg": "integer",
      "serverless_apps_apm_excl_fargate_apm_azure_appservice_instances_avg": "integer",
      "serverless_apps_apm_excl_fargate_apm_azure_azurefunction_instances_avg": "integer",
      "serverless_apps_apm_excl_fargate_apm_azure_containerapp_instances_avg": "integer",
      "serverless_apps_apm_excl_fargate_apm_gcp_cloudfunction_instances_avg": "integer",
      "serverless_apps_apm_excl_fargate_apm_gcp_cloudrun_instances_avg": "integer",
      "serverless_apps_apm_excl_fargate_avg": "integer",
      "serverless_apps_azure_container_app_instances_avg": "integer",
      "serverless_apps_azure_count_avg": "integer",
      "serverless_apps_azure_function_app_instances_avg": "integer",
      "serverless_apps_azure_web_app_instances_avg": "integer",
      "serverless_apps_ecs_avg": "integer",
      "serverless_apps_eks_avg": "integer",
      "serverless_apps_excl_fargate_avg": "integer",
      "serverless_apps_excl_fargate_azure_container_app_instances_avg": "integer",
      "serverless_apps_excl_fargate_azure_function_app_instances_avg": "integer",
      "serverless_apps_excl_fargate_azure_web_app_instances_avg": "integer",
      "serverless_apps_excl_fargate_google_cloud_functions_instances_avg": "integer",
      "serverless_apps_excl_fargate_google_cloud_run_instances_avg": "integer",
      "serverless_apps_google_cloud_functions_instances_avg": "integer",
      "serverless_apps_google_cloud_run_instances_avg": "integer",
      "serverless_apps_google_count_avg": "integer",
      "serverless_apps_total_count_avg": "integer",
      "siem_analyzed_logs_add_on_count_sum": "integer",
      "synthetics_browser_check_calls_count_sum": "integer",
      "synthetics_check_calls_count_sum": "integer",
      "synthetics_mobile_test_runs_sum": "integer",
      "synthetics_parallel_testing_max_slots_hwm": "integer",
      "trace_search_indexed_events_count_sum": "integer",
      "twol_ingested_events_bytes_sum": "integer",
      "universal_service_monitoring_host_top99p": "integer",
      "vsphere_host_top99p": "integer",
      "vuln_management_host_count_top99p": "integer",
      "workflow_executions_usage_sum": "integer"
    }
  ],
  "vsphere_host_top99p_sum": "integer",
  "vuln_management_host_count_top99p_sum": "integer",
  "workflow_executions_usage_agg_sum": "integer"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get usage across your account
Copy
```
                  # Required query arguments  
export start_month="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/summary?start_month=${start_month}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get usage across your account
```
"""
Get usage across your account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_summary(
        start_month=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get usage across your account
```
# Get usage across your account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_summary("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get usage across your account
```
// Get usage across your account returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageSummary(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageSummaryOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageSummary`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageSummary`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get usage across your account
```
// Get usage across your account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageSummaryResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSummaryResponse result =
          apiInstance.getUsageSummary(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageSummary");
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

#####  Get usage across your account
```
// Get usage across your account returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageSummaryOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_summary(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageSummaryOptionalParams::default(),
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

#####  Get usage across your account
```
/**
 * Get usage across your account returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageSummaryRequest = {
  startMonth: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageSummary(params)
  .then((data: v1.UsageSummaryResponse) => {
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
## [Get hourly usage for logs by index](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-logs-by-index)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-logs-by-index-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/logs_by_indexhttps://api.ap2.datadoghq.com/api/v1/usage/logs_by_indexhttps://api.datadoghq.eu/api/v1/usage/logs_by_indexhttps://api.ddog-gov.com/api/v1/usage/logs_by_indexhttps://api.datadoghq.com/api/v1/usage/logs_by_indexhttps://api.us3.datadoghq.com/api/v1/usage/logs_by_indexhttps://api.us5.datadoghq.com/api/v1/usage/logs_by_index
### Overview
Get hourly usage for logs by index. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
index_name
array
Comma-separated list of log index names.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByIndex-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByIndex-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByIndex-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByIndex-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of indexed logs for each hour and index for a given organization.
Field
Type
Description
usage
[object]
An array of objects regarding hourly usage of logs by index response.
event_count
int64
The total number of indexed logs for the queried hour.
hour
date-time
The hour for the usage.
index_id
string
The index ID for this usage.
index_name
string
The user specified name for this index ID.
org_name
string
The organization name.
public_id
string
The organization public ID.
retention
int64
The retention period (in days) for this index ID.
```
{
  "usage": [
    {
      "event_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "index_id": "string",
      "index_name": "string",
      "org_name": "string",
      "public_id": "string",
      "retention": "integer"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python-legacy)


#####  Get hourly usage for logs by index
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/logs_by_index?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for logs by index
```
"""
Get hourly usage for logs by index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_logs_by_index(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for logs by index
```
# Get hourly usage for logs by index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_logs_by_index("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for logs by index
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2020-01-01T00'
end_date='2019-01-01T02'
index_name='main, marketing'

dog.get_logs_by_index_usage(start_date, end_date, index_name)
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for logs by index
```
// Get hourly usage for logs by index returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageLogsByIndex(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageLogsByIndexOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageLogsByIndex`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageLogsByIndex`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for logs by index
```
// Get hourly usage for logs by index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageLogsByIndexResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageLogsByIndexResponse result =
          apiInstance.getUsageLogsByIndex(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageLogsByIndex");
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

#####  Get hourly usage for logs by index
```
# Consult the ruby example
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get hourly usage for logs by index
```
// Get hourly usage for logs by index returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageLogsByIndexOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_logs_by_index(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageLogsByIndexOptionalParams::default(),
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

#####  Get hourly usage for logs by index
```
/**
 * Get hourly usage for logs by index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageLogsByIndexRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageLogsByIndex(params)
  .then((data: v1.UsageLogsByIndexResponse) => {
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
## [Get hourly logs usage by retention](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-logs-usage-by-retention)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-logs-usage-by-retention-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/logs-by-retentionhttps://api.ap2.datadoghq.com/api/v1/usage/logs-by-retentionhttps://api.datadoghq.eu/api/v1/usage/logs-by-retentionhttps://api.ddog-gov.com/api/v1/usage/logs-by-retentionhttps://api.datadoghq.com/api/v1/usage/logs-by-retentionhttps://api.us3.datadoghq.com/api/v1/usage/logs-by-retentionhttps://api.us5.datadoghq.com/api/v1/usage/logs-by-retention
### Overview
Get hourly usage for indexed logs by retention period. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByRetention-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByRetention-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByRetention-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogsByRetention-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the indexed logs usage broken down by retention period for an organization during a given hour.
Field
Type
Description
usage
[object]
Get hourly usage for indexed logs by retention period.
indexed_events_count
int64
Total logs indexed with this retention period during a given hour.
live_indexed_events_count
int64
Live logs indexed with this retention period during a given hour.
org_name
string
The organization name.
public_id
string
The organization public ID.
rehydrated_indexed_events_count
int64
Rehydrated logs indexed with this retention period during a given hour.
retention
string
The retention period in days or "custom" for all custom retention usage.
```
{
  "usage": [
    {
      "indexed_events_count": "integer",
      "live_indexed_events_count": "integer",
      "org_name": "string",
      "public_id": "string",
      "rehydrated_indexed_events_count": "integer",
      "retention": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly logs usage by retention
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/logs-by-retention?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly logs usage by retention
```
"""
Get hourly logs usage by retention returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_logs_by_retention(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly logs usage by retention
```
# Get hourly logs usage by retention returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_logs_by_retention((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly logs usage by retention
```
// Get hourly logs usage by retention returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageLogsByRetention(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageLogsByRetentionOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageLogsByRetention`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageLogsByRetention`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly logs usage by retention
```
// Get hourly logs usage by retention returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageLogsByRetentionOptionalParameters;
import com.datadog.api.client.v1.model.UsageLogsByRetentionResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageLogsByRetentionResponse result =
          apiInstance.getUsageLogsByRetention(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageLogsByRetentionOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageLogsByRetention");
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

#####  Get hourly logs usage by retention
```
// Get hourly logs usage by retention returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageLogsByRetentionOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_logs_by_retention(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageLogsByRetentionOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly logs usage by retention
```
/**
 * Get hourly logs usage by retention returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageLogsByRetentionRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageLogsByRetention(params)
  .then((data: v1.UsageLogsByRetentionResponse) => {
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
## [Get hourly usage for hosts and containers](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-hosts-and-containers)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-hosts-and-containers-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/hostshttps://api.ap2.datadoghq.com/api/v1/usage/hostshttps://api.datadoghq.eu/api/v1/usage/hostshttps://api.ddog-gov.com/api/v1/usage/hostshttps://api.datadoghq.com/api/v1/usage/hostshttps://api.us3.datadoghq.com/api/v1/usage/hostshttps://api.us5.datadoghq.com/api/v1/usage/hosts
### Overview
Get hourly usage for hosts and containers. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageHosts-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageHosts-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageHosts-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageHosts-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Host usage response.
Field
Type
Description
usage
[object]
An array of objects related to host usage.
agent_host_count
int64
Contains the total number of infrastructure hosts reporting during a given hour that were running the Datadog Agent.
alibaba_host_count
int64
Contains the total number of hosts that reported through Alibaba integration (and were NOT running the Datadog Agent).
apm_azure_app_service_host_count
int64
Contains the total number of Azure App Services hosts using APM.
apm_host_count
int64
Shows the total number of hosts using APM during the hour, these are counted as billable (except during trial periods).
aws_host_count
int64
Contains the total number of hosts that reported through the AWS integration (and were NOT running the Datadog Agent).
azure_host_count
int64
Contains the total number of hosts that reported through Azure integration (and were NOT running the Datadog Agent).
container_count
int64
Shows the total number of containers reported by the Docker integration during the hour.
gcp_host_count
int64
Contains the total number of hosts that reported through the Google Cloud integration (and were NOT running the Datadog Agent).
heroku_host_count
int64
Contains the total number of Heroku dynos reported by the Datadog Agent.
host_count
int64
Contains the total number of billable infrastructure hosts reporting during a given hour. This is the sum of `agent_host_count`, `aws_host_count`, and `gcp_host_count`.
hour
date-time
The hour for the usage.
infra_azure_app_service
int64
Contains the total number of hosts that reported through the Azure App Services integration (and were NOT running the Datadog Agent).
opentelemetry_apm_host_count
int64
Contains the total number of hosts using APM reported by Datadog exporter for the OpenTelemetry Collector.
opentelemetry_host_count
int64
Contains the total number of hosts reported by Datadog exporter for the OpenTelemetry Collector.
org_name
string
The organization name.
public_id
string
The organization public ID.
vsphere_host_count
int64
Contains the total number of hosts that reported through vSphere integration (and were NOT running the Datadog Agent).
```
{
  "usage": [
    {
      "agent_host_count": "integer",
      "alibaba_host_count": "integer",
      "apm_azure_app_service_host_count": "integer",
      "apm_host_count": "integer",
      "aws_host_count": "integer",
      "azure_host_count": "integer",
      "container_count": "integer",
      "gcp_host_count": "integer",
      "heroku_host_count": "integer",
      "host_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "infra_azure_app_service": "integer",
      "opentelemetry_apm_host_count": "integer",
      "opentelemetry_host_count": "integer",
      "org_name": "string",
      "public_id": "string",
      "vsphere_host_count": "integer"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for hosts and containers
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/hosts?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for hosts and containers
```
"""
Get hourly usage for hosts and containers returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_hosts(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for hosts and containers
```
# Get hourly usage for hosts and containers returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_hosts((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for hosts and containers
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_hosts_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for hosts and containers
```
// Get hourly usage for hosts and containers returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageHosts(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageHostsOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageHosts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageHosts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for hosts and containers
```
// Get hourly usage for hosts and containers returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageHostsOptionalParameters;
import com.datadog.api.client.v1.model.UsageHostsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageHostsResponse result =
          apiInstance.getUsageHosts(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageHostsOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageHosts");
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

#####  Get hourly usage for hosts and containers
```
// Get hourly usage for hosts and containers returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageHostsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_hosts(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageHostsOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for hosts and containers
```
/**
 * Get hourly usage for hosts and containers returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageHostsRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageHosts(params)
  .then((data: v1.UsageHostsResponse) => {
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
## [Get hourly usage for logs](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-logs)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-logs-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/logshttps://api.ap2.datadoghq.com/api/v1/usage/logshttps://api.datadoghq.eu/api/v1/usage/logshttps://api.ddog-gov.com/api/v1/usage/logshttps://api.datadoghq.com/api/v1/usage/logshttps://api.us3.datadoghq.com/api/v1/usage/logshttps://api.us5.datadoghq.com/api/v1/usage/logs
### Overview
Get hourly usage for logs. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogs-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogs-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogs-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLogs-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of logs for each hour.
Field
Type
Description
usage
[object]
An array of objects regarding hourly usage of logs.
billable_ingested_bytes
int64
Contains the number of billable log bytes ingested.
hour
date-time
The hour for the usage.
indexed_events_count
int64
Contains the number of log events indexed.
ingested_events_bytes
int64
Contains the number of log bytes ingested.
logs_forwarding_events_bytes
int64
Contains the number of logs forwarded bytes (data available as of April 1st 2023)
logs_live_indexed_count
int64
Contains the number of live log events indexed (data available as of December 1, 2020).
logs_live_ingested_bytes
int64
Contains the number of live log bytes ingested (data available as of December 1, 2020).
logs_rehydrated_indexed_count
int64
Contains the number of rehydrated log events indexed (data available as of December 1, 2020).
logs_rehydrated_ingested_bytes
int64
Contains the number of rehydrated log bytes ingested (data available as of December 1, 2020).
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "billable_ingested_bytes": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "indexed_events_count": "integer",
      "ingested_events_bytes": "integer",
      "logs_forwarding_events_bytes": "integer",
      "logs_live_indexed_count": "integer",
      "logs_live_ingested_bytes": "integer",
      "logs_rehydrated_indexed_count": "integer",
      "logs_rehydrated_ingested_bytes": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for logs
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/logs?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for logs
```
"""
Get hourly usage for logs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_logs(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for logs
```
# Get hourly usage for logs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_logs("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for logs
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_logs_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for logs
```
// Get hourly usage for logs returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageLogs(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageLogsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageLogs`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for logs
```
// Get hourly usage for logs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageLogsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageLogsResponse result =
          apiInstance.getUsageLogs(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageLogs");
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

#####  Get hourly usage for logs
```
// Get hourly usage for logs returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageLogsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_logs(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageLogsOptionalParams::default(),
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

#####  Get hourly usage for logs
```
/**
 * Get hourly usage for logs returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageLogsRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageLogs(params)
  .then((data: v1.UsageLogsResponse) => {
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
## [Get hourly usage for custom metrics](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-custom-metrics)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-custom-metrics-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/timeserieshttps://api.ap2.datadoghq.com/api/v1/usage/timeserieshttps://api.datadoghq.eu/api/v1/usage/timeserieshttps://api.ddog-gov.com/api/v1/usage/timeserieshttps://api.datadoghq.com/api/v1/usage/timeserieshttps://api.us3.datadoghq.com/api/v1/usage/timeserieshttps://api.us5.datadoghq.com/api/v1/usage/timeseries
### Overview
Get hourly usage for [custom metrics](https://docs.datadoghq.com/developers/metrics/custom_metrics/). **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTimeseries-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTimeseries-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTimeseries-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageTimeseries-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing hourly usage of timeseries.
Field
Type
Description
usage
[object]
An array of objects regarding hourly usage of timeseries.
hour
date-time
The hour for the usage.
num_custom_input_timeseries
int64
Contains the number of custom metrics that are inputs for aggregations (metric configured is custom).
num_custom_output_timeseries
int64
Contains the number of custom metrics that are outputs for aggregations (metric configured is custom).
num_custom_timeseries
int64
Contains sum of non-aggregation custom metrics and custom metrics that are outputs for aggregations.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "num_custom_input_timeseries": "integer",
      "num_custom_output_timeseries": "integer",
      "num_custom_timeseries": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for custom metrics
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/timeseries?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for custom metrics
```
"""
Get hourly usage for custom metrics returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_timeseries(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for custom metrics
```
# Get hourly usage for custom metrics returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_timeseries((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for custom metrics
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_custom_metrics_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for custom metrics
```
// Get hourly usage for custom metrics returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageTimeseries(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageTimeseriesOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageTimeseries`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageTimeseries`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for custom metrics
```
// Get hourly usage for custom metrics returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageTimeseriesOptionalParameters;
import com.datadog.api.client.v1.model.UsageTimeseriesResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageTimeseriesResponse result =
          apiInstance.getUsageTimeseries(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageTimeseriesOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageTimeseries");
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

#####  Get hourly usage for custom metrics
```
// Get hourly usage for custom metrics returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageTimeseriesOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_timeseries(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageTimeseriesOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for custom metrics
```
/**
 * Get hourly usage for custom metrics returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageTimeseriesRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageTimeseries(params)
  .then((data: v1.UsageTimeseriesResponse) => {
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
## [Get hourly usage for indexed spans](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-indexed-spans)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-indexed-spans-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/indexed-spanshttps://api.ap2.datadoghq.com/api/v1/usage/indexed-spanshttps://api.datadoghq.eu/api/v1/usage/indexed-spanshttps://api.ddog-gov.com/api/v1/usage/indexed-spanshttps://api.datadoghq.com/api/v1/usage/indexed-spanshttps://api.us3.datadoghq.com/api/v1/usage/indexed-spanshttps://api.us5.datadoghq.com/api/v1/usage/indexed-spans
### Overview
Get hourly usage for indexed spans. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageIndexedSpans-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageIndexedSpans-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageIndexedSpans-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageIndexedSpans-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


A response containing indexed spans usage.
Field
Type
Description
usage
[object]
Array with the number of hourly traces indexed for a given organization.
hour
date-time
The hour for the usage.
indexed_events_count
int64
Contains the number of spans indexed.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "indexed_events_count": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for indexed spans
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/indexed-spans?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for indexed spans
```
"""
Get hourly usage for indexed spans returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_indexed_spans(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for indexed spans
```
# Get hourly usage for indexed spans returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_indexed_spans((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for indexed spans
```
// Get hourly usage for indexed spans returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageIndexedSpans(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageIndexedSpansOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageIndexedSpans`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageIndexedSpans`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for indexed spans
```
// Get hourly usage for indexed spans returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageIndexedSpansOptionalParameters;
import com.datadog.api.client.v1.model.UsageIndexedSpansResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageIndexedSpansResponse result =
          apiInstance.getUsageIndexedSpans(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageIndexedSpansOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageIndexedSpans");
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

#####  Get hourly usage for indexed spans
```
// Get hourly usage for indexed spans returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageIndexedSpansOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_indexed_spans(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageIndexedSpansOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for indexed spans
```
/**
 * Get hourly usage for indexed spans returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageIndexedSpansRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageIndexedSpans(params)
  .then((data: v1.UsageIndexedSpansResponse) => {
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
## [Get hourly usage for synthetics checks](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-checks)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-checks-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/syntheticshttps://api.ap2.datadoghq.com/api/v1/usage/syntheticshttps://api.datadoghq.eu/api/v1/usage/syntheticshttps://api.ddog-gov.com/api/v1/usage/syntheticshttps://api.datadoghq.com/api/v1/usage/syntheticshttps://api.us3.datadoghq.com/api/v1/usage/syntheticshttps://api.us5.datadoghq.com/api/v1/usage/synthetics
### Overview
Get hourly usage for [synthetics checks](https://docs.datadoghq.com/synthetics/). **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSynthetics-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSynthetics-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSynthetics-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSynthetics-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of Synthetics API tests run for each hour for a given organization.
Field
Type
Description
usage
[object]
Array with the number of hourly Synthetics test run for a given organization.
check_calls_count
int64
Contains the number of Synthetics API tests run.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "check_calls_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for synthetics checks
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/synthetics?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for synthetics checks
```
"""
Get hourly usage for synthetics checks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_synthetics(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for synthetics checks
```
# Get hourly usage for synthetics checks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_synthetics("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for synthetics checks
```
// Get hourly usage for synthetics checks returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageSynthetics(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageSyntheticsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageSynthetics`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageSynthetics`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for synthetics checks
```
// Get hourly usage for synthetics checks returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageSyntheticsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSyntheticsResponse result =
          apiInstance.getUsageSynthetics(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageSynthetics");
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

#####  Get hourly usage for synthetics checks
```
// Get hourly usage for synthetics checks returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageSyntheticsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_synthetics(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageSyntheticsOptionalParams::default(),
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

#####  Get hourly usage for synthetics checks
```
/**
 * Get hourly usage for synthetics checks returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageSyntheticsRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageSynthetics(params)
  .then((data: v1.UsageSyntheticsResponse) => {
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
## [Get hourly usage for synthetics API checks](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-api-checks)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-api-checks-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/synthetics_apihttps://api.ap2.datadoghq.com/api/v1/usage/synthetics_apihttps://api.datadoghq.eu/api/v1/usage/synthetics_apihttps://api.ddog-gov.com/api/v1/usage/synthetics_apihttps://api.datadoghq.com/api/v1/usage/synthetics_apihttps://api.us3.datadoghq.com/api/v1/usage/synthetics_apihttps://api.us5.datadoghq.com/api/v1/usage/synthetics_api
### Overview
Get hourly usage for [synthetics API checks](https://docs.datadoghq.com/synthetics/). **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsAPI-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsAPI-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsAPI-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsAPI-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of Synthetics API tests run for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Synthetics API tests.
check_calls_count
int64
Contains the number of Synthetics API tests run.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "check_calls_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for synthetics API checks
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/synthetics_api?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for synthetics API checks
```
"""
Get hourly usage for synthetics API checks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_synthetics_api(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for synthetics API checks
```
# Get hourly usage for synthetics API checks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_synthetics_api("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for synthetics API checks
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_synthetics_api_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for synthetics API checks
```
// Get hourly usage for synthetics API checks returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageSyntheticsAPI(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageSyntheticsAPIOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageSyntheticsAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageSyntheticsAPI`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for synthetics API checks
```
// Get hourly usage for synthetics API checks returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageSyntheticsAPIResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSyntheticsAPIResponse result =
          apiInstance.getUsageSyntheticsAPI(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageSyntheticsAPI");
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

#####  Get hourly usage for synthetics API checks
```
// Get hourly usage for synthetics API checks returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageSyntheticsAPIOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_synthetics_api(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageSyntheticsAPIOptionalParams::default(),
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

#####  Get hourly usage for synthetics API checks
```
/**
 * Get hourly usage for synthetics API checks returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageSyntheticsAPIRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageSyntheticsAPI(params)
  .then((data: v1.UsageSyntheticsAPIResponse) => {
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
## [Get hourly usage for synthetics browser checks](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-browser-checks)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-browser-checks-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/synthetics_browserhttps://api.ap2.datadoghq.com/api/v1/usage/synthetics_browserhttps://api.datadoghq.eu/api/v1/usage/synthetics_browserhttps://api.ddog-gov.com/api/v1/usage/synthetics_browserhttps://api.datadoghq.com/api/v1/usage/synthetics_browserhttps://api.us3.datadoghq.com/api/v1/usage/synthetics_browserhttps://api.us5.datadoghq.com/api/v1/usage/synthetics_browser
### Overview
Get hourly usage for synthetics browser checks. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsBrowser-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsBrowser-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsBrowser-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSyntheticsBrowser-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of Synthetics Browser tests run for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Synthetics Browser tests.
browser_check_calls_count
int64
Contains the number of Synthetics Browser tests run.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "browser_check_calls_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for synthetics browser checks
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/synthetics_browser?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for synthetics browser checks
```
"""
Get hourly usage for synthetics browser checks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_synthetics_browser(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for synthetics browser checks
```
# Get hourly usage for synthetics browser checks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_synthetics_browser("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for synthetics browser checks
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_synthetics_browser_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for synthetics browser checks
```
// Get hourly usage for synthetics browser checks returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageSyntheticsBrowser(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageSyntheticsBrowserOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageSyntheticsBrowser`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageSyntheticsBrowser`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for synthetics browser checks
```
// Get hourly usage for synthetics browser checks returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageSyntheticsBrowserResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSyntheticsBrowserResponse result =
          apiInstance.getUsageSyntheticsBrowser(
              OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageSyntheticsBrowser");
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

#####  Get hourly usage for synthetics browser checks
```
// Get hourly usage for synthetics browser checks returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageSyntheticsBrowserOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_synthetics_browser(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageSyntheticsBrowserOptionalParams::default(),
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

#####  Get hourly usage for synthetics browser checks
```
/**
 * Get hourly usage for synthetics browser checks returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageSyntheticsBrowserRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageSyntheticsBrowser(params)
  .then((data: v1.UsageSyntheticsBrowserResponse) => {
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
## [Get hourly usage for Fargate](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-fargate)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-fargate-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/fargatehttps://api.ap2.datadoghq.com/api/v1/usage/fargatehttps://api.datadoghq.eu/api/v1/usage/fargatehttps://api.ddog-gov.com/api/v1/usage/fargatehttps://api.datadoghq.com/api/v1/usage/fargatehttps://api.us3.datadoghq.com/api/v1/usage/fargatehttps://api.us5.datadoghq.com/api/v1/usage/fargate
### Overview
Get hourly usage for [Fargate](https://docs.datadoghq.com/integrations/ecs_fargate/). **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageFargate-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageFargate-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageFargate-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageFargate-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of Fargate tasks run and hourly usage.
Field
Type
Description
usage
[object]
Array with the number of hourly Fargate tasks recorded for a given organization.
apm_fargate_count
int64
The high-water mark of APM ECS Fargate tasks during the given hour.
appsec_fargate_count
int64
The Application Security Monitoring ECS Fargate tasks during the given hour.
avg_profiled_fargate_tasks
int64
The average profiled task count for Fargate Profiling.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
tasks_count
int64
The number of Fargate tasks run.
```
{
  "usage": [
    {
      "apm_fargate_count": "integer",
      "appsec_fargate_count": "integer",
      "avg_profiled_fargate_tasks": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string",
      "tasks_count": "integer"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for Fargate
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/fargate?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for Fargate
```
"""
Get hourly usage for Fargate returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_fargate(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for Fargate
```
# Get hourly usage for Fargate returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_fargate((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for Fargate
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_fargate_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for Fargate
```
// Get hourly usage for Fargate returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageFargate(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageFargateOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageFargate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageFargate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for Fargate
```
// Get hourly usage for Fargate returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageFargateOptionalParameters;
import com.datadog.api.client.v1.model.UsageFargateResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageFargateResponse result =
          apiInstance.getUsageFargate(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageFargateOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageFargate");
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

#####  Get hourly usage for Fargate
```
// Get hourly usage for Fargate returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageFargateOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_fargate(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageFargateOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for Fargate
```
/**
 * Get hourly usage for Fargate returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageFargateRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageFargate(params)
  .then((data: v1.UsageFargateResponse) => {
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
## [Get hourly usage for Lambda](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-lambda)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-lambda-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/aws_lambdahttps://api.ap2.datadoghq.com/api/v1/usage/aws_lambdahttps://api.datadoghq.eu/api/v1/usage/aws_lambdahttps://api.ddog-gov.com/api/v1/usage/aws_lambdahttps://api.datadoghq.com/api/v1/usage/aws_lambdahttps://api.us3.datadoghq.com/api/v1/usage/aws_lambdahttps://api.us5.datadoghq.com/api/v1/usage/aws_lambda
### Overview
Get hourly usage for Lambda. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambda-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambda-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambda-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambda-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of Lambda functions and sum of the invocations of all Lambda functions for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Lambda.
func_count
int64
Contains the number of different functions for each region and AWS account.
hour
date-time
The hour for the usage.
invocations_sum
int64
Contains the sum of invocations of all functions.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "func_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "invocations_sum": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for Lambda
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/aws_lambda?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for Lambda
```
"""
Get hourly usage for Lambda returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_lambda(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for Lambda
```
# Get hourly usage for Lambda returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_lambda((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for Lambda
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_aws_lambda_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for Lambda
```
// Get hourly usage for Lambda returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageLambda(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageLambdaOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageLambda`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageLambda`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for Lambda
```
// Get hourly usage for Lambda returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageLambdaOptionalParameters;
import com.datadog.api.client.v1.model.UsageLambdaResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageLambdaResponse result =
          apiInstance.getUsageLambda(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageLambdaOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageLambda");
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

#####  Get hourly usage for Lambda
```
// Get hourly usage for Lambda returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageLambdaOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_lambda(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageLambdaOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for Lambda
```
/**
 * Get hourly usage for Lambda returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageLambdaRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageLambda(params)
  .then((data: v1.UsageLambdaResponse) => {
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
## [Get hourly usage for RUM sessions](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-rum-sessions)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-rum-sessions-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/rum_sessionshttps://api.ap2.datadoghq.com/api/v1/usage/rum_sessionshttps://api.datadoghq.eu/api/v1/usage/rum_sessionshttps://api.ddog-gov.com/api/v1/usage/rum_sessionshttps://api.datadoghq.com/api/v1/usage/rum_sessionshttps://api.us3.datadoghq.com/api/v1/usage/rum_sessionshttps://api.us5.datadoghq.com/api/v1/usage/rum_sessions
### Overview
Get hourly usage for [RUM](https://docs.datadoghq.com/real_user_monitoring/) Sessions. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
type
string
RUM type: `[browser, mobile]`. Defaults to `browser`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumSessions-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumSessions-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumSessions-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumSessions-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of RUM sessions for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for RUM sessions.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
replay_session_count
int64
Contains the number of RUM Session Replay counts (data available beginning November 1, 2021).
session_count
int64
Contains the number of browser RUM lite Sessions.
session_count_android
int64
Contains the number of mobile RUM sessions on Android (data available beginning December 1, 2020).
session_count_flutter
int64
Contains the number of mobile RUM sessions on Flutter (data available beginning March 1, 2023).
session_count_ios
int64
Contains the number of mobile RUM sessions on iOS (data available beginning December 1, 2020).
session_count_reactnative
int64
Contains the number of mobile RUM sessions on React Native (data available beginning May 1, 2022).
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string",
      "replay_session_count": "integer",
      "session_count": "integer",
      "session_count_android": "integer",
      "session_count_flutter": "integer",
      "session_count_ios": "integer",
      "session_count_reactnative": "integer"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for RUM sessions
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/rum_sessions?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for RUM sessions
```
"""
Get hourly usage for RUM sessions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_rum_sessions(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for RUM sessions
```
# Get hourly usage for RUM sessions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_rum_sessions("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for RUM sessions
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_rum_sessions_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for RUM sessions
```
// Get hourly usage for RUM sessions returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageRumSessions(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageRumSessionsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageRumSessions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageRumSessions`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for RUM sessions
```
// Get hourly usage for RUM sessions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageRumSessionsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageRumSessionsResponse result =
          apiInstance.getUsageRumSessions(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageRumSessions");
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

#####  Get hourly usage for RUM sessions
```
// Get hourly usage for RUM sessions returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageRumSessionsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_rum_sessions(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageRumSessionsOptionalParams::default(),
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

#####  Get hourly usage for RUM sessions
```
/**
 * Get hourly usage for RUM sessions returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageRumSessionsRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageRumSessions(params)
  .then((data: v1.UsageRumSessionsResponse) => {
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
## [Get hourly usage for network hosts](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-network-hosts)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-network-hosts-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/network_hostshttps://api.ap2.datadoghq.com/api/v1/usage/network_hostshttps://api.datadoghq.eu/api/v1/usage/network_hostshttps://api.ddog-gov.com/api/v1/usage/network_hostshttps://api.datadoghq.com/api/v1/usage/network_hostshttps://api.us3.datadoghq.com/api/v1/usage/network_hostshttps://api.us5.datadoghq.com/api/v1/usage/network_hosts
### Overview
Get hourly usage for network hosts. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkHosts-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkHosts-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkHosts-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkHosts-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of active NPM hosts for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for NPM hosts.
host_count
int64
Contains the number of active NPM hosts.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "host_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  Get hourly usage for network hosts
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/network_hosts?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for network hosts
```
"""
Get hourly usage for network hosts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_network_hosts(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for network hosts
```
# Get hourly usage for network hosts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_network_hosts("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for network hosts
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_network_hosts_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for network hosts
```
// Get hourly usage for network hosts returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageNetworkHosts(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageNetworkHostsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageNetworkHosts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageNetworkHosts`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for network hosts
```
// Get hourly usage for network hosts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageNetworkHostsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageNetworkHostsResponse result =
          apiInstance.getUsageNetworkHosts(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageNetworkHosts");
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

#####  Get hourly usage for network hosts
```
// Get hourly usage for network hosts returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageNetworkHostsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_network_hosts(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageNetworkHostsOptionalParams::default(),
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

#####  Get hourly usage for network hosts
```
/**
 * Get hourly usage for network hosts returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageNetworkHostsRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageNetworkHosts(params)
  .then((data: v1.UsageNetworkHostsResponse) => {
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
## [get hourly usage for network flows](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-network-flows)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-network-flows-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/network_flowshttps://api.ap2.datadoghq.com/api/v1/usage/network_flowshttps://api.datadoghq.eu/api/v1/usage/network_flowshttps://api.ddog-gov.com/api/v1/usage/network_flowshttps://api.datadoghq.com/api/v1/usage/network_flowshttps://api.us3.datadoghq.com/api/v1/usage/network_flowshttps://api.us5.datadoghq.com/api/v1/usage/network_flows
### Overview
Get hourly usage for network flows. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkFlows-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkFlows-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkFlows-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageNetworkFlows-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of netflow events indexed for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Network Flows.
hour
date-time
The hour for the usage.
indexed_events_count
int64
Contains the number of netflow events indexed.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "indexed_events_count": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby-legacy)


#####  get hourly usage for network flows
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/network_flows?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  get hourly usage for network flows
```
"""
get hourly usage for network flows returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_network_flows(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  get hourly usage for network flows
```
# get hourly usage for network flows returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_network_flows("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  get hourly usage for network flows
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

start_date= '2019-10-07T00'
end_date='2019-10-07T02'

dog.get_network_flows_usage(start_date, end_date)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  get hourly usage for network flows
```
// get hourly usage for network flows returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageNetworkFlows(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageNetworkFlowsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageNetworkFlows`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageNetworkFlows`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  get hourly usage for network flows
```
// get hourly usage for network flows returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageNetworkFlowsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageNetworkFlowsResponse result =
          apiInstance.getUsageNetworkFlows(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageNetworkFlows");
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

#####  get hourly usage for network flows
```
// get hourly usage for network flows returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageNetworkFlowsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_network_flows(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageNetworkFlowsOptionalParams::default(),
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

#####  get hourly usage for network flows
```
/**
 * get hourly usage for network flows returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageNetworkFlowsRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageNetworkFlows(params)
  .then((data: v1.UsageNetworkFlowsResponse) => {
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
## [Get hourly usage for analyzed logs](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-analyzed-logs)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-analyzed-logs-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/analyzed_logshttps://api.ap2.datadoghq.com/api/v1/usage/analyzed_logshttps://api.datadoghq.eu/api/v1/usage/analyzed_logshttps://api.ddog-gov.com/api/v1/usage/analyzed_logshttps://api.datadoghq.com/api/v1/usage/analyzed_logshttps://api.us3.datadoghq.com/api/v1/usage/analyzed_logshttps://api.us5.datadoghq.com/api/v1/usage/analyzed_logs
### Overview
Get hourly usage for analyzed logs (Security Monitoring). **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAnalyzedLogs-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAnalyzedLogs-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAnalyzedLogs-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAnalyzedLogs-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


A response containing the number of analyzed logs for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for analyzed logs.
analyzed_logs
int64
Contains the number of analyzed logs.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "analyzed_logs": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for analyzed logs
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/analyzed_logs?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for analyzed logs
```
"""
Get hourly usage for analyzed logs returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_analyzed_logs(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for analyzed logs
```
# Get hourly usage for analyzed logs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_analyzed_logs((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for analyzed logs
```
// Get hourly usage for analyzed logs returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageAnalyzedLogs(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageAnalyzedLogsOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageAnalyzedLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageAnalyzedLogs`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for analyzed logs
```
// Get hourly usage for analyzed logs returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageAnalyzedLogsOptionalParameters;
import com.datadog.api.client.v1.model.UsageAnalyzedLogsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageAnalyzedLogsResponse result =
          apiInstance.getUsageAnalyzedLogs(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageAnalyzedLogsOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageAnalyzedLogs");
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

#####  Get hourly usage for analyzed logs
```
// Get hourly usage for analyzed logs returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageAnalyzedLogsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_analyzed_logs(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageAnalyzedLogsOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for analyzed logs
```
/**
 * Get hourly usage for analyzed logs returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageAnalyzedLogsRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageAnalyzedLogs(params)
  .then((data: v1.UsageAnalyzedLogsResponse) => {
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
## [Get hourly usage for SNMP devices](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-snmp-devices)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-snmp-devices-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/snmphttps://api.ap2.datadoghq.com/api/v1/usage/snmphttps://api.datadoghq.eu/api/v1/usage/snmphttps://api.ddog-gov.com/api/v1/usage/snmphttps://api.datadoghq.com/api/v1/usage/snmphttps://api.us3.datadoghq.com/api/v1/usage/snmphttps://api.us5.datadoghq.com/api/v1/usage/snmp
### Overview
Get hourly usage for SNMP devices. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSNMP-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSNMP-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSNMP-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSNMP-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of SNMP devices for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for SNMP devices.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
snmp_devices
int64
Contains the number of SNMP devices.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string",
      "snmp_devices": "integer"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for SNMP devices
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/snmp?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for SNMP devices
```
"""
Get hourly usage for SNMP devices returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_snmp(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for SNMP devices
```
# Get hourly usage for SNMP devices returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_snmp((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for SNMP devices
```
// Get hourly usage for SNMP devices returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageSNMP(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageSNMPOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageSNMP`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageSNMP`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for SNMP devices
```
// Get hourly usage for SNMP devices returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageSNMPOptionalParameters;
import com.datadog.api.client.v1.model.UsageSNMPResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSNMPResponse result =
          apiInstance.getUsageSNMP(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageSNMPOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageSNMP");
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

#####  Get hourly usage for SNMP devices
```
// Get hourly usage for SNMP devices returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageSNMPOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_snmp(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageSNMPOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for SNMP devices
```
/**
 * Get hourly usage for SNMP devices returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageSNMPRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageSNMP(params)
  .then((data: v1.UsageSNMPResponse) => {
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
## [Get hourly usage for ingested spans](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-ingested-spans)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-ingested-spans-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/ingested-spanshttps://api.ap2.datadoghq.com/api/v1/usage/ingested-spanshttps://api.datadoghq.eu/api/v1/usage/ingested-spanshttps://api.ddog-gov.com/api/v1/usage/ingested-spanshttps://api.datadoghq.com/api/v1/usage/ingested-spanshttps://api.us3.datadoghq.com/api/v1/usage/ingested-spanshttps://api.us5.datadoghq.com/api/v1/usage/ingested-spans
### Overview
Get hourly usage for ingested spans. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetIngestedSpans-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetIngestedSpans-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetIngestedSpans-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetIngestedSpans-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the ingested spans usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for ingested spans.
hour
date-time
The hour for the usage.
ingested_events_bytes
int64
Contains the total number of bytes ingested for APM spans during a given hour.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "ingested_events_bytes": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for ingested spans
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/ingested-spans?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for ingested spans
```
"""
Get hourly usage for ingested spans returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_ingested_spans(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for ingested spans
```
# Get hourly usage for ingested spans returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_ingested_spans((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for ingested spans
```
// Get hourly usage for ingested spans returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetIngestedSpans(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetIngestedSpansOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetIngestedSpans`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetIngestedSpans`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for ingested spans
```
// Get hourly usage for ingested spans returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetIngestedSpansOptionalParameters;
import com.datadog.api.client.v1.model.UsageIngestedSpansResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageIngestedSpansResponse result =
          apiInstance.getIngestedSpans(
              OffsetDateTime.now().plusDays(-5),
              new GetIngestedSpansOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getIngestedSpans");
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

#####  Get hourly usage for ingested spans
```
// Get hourly usage for ingested spans returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetIngestedSpansOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_ingested_spans(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetIngestedSpansOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for ingested spans
```
/**
 * Get hourly usage for ingested spans returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetIngestedSpansRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getIngestedSpans(params)
  .then((data: v1.UsageIngestedSpansResponse) => {
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
## [Get hourly usage for incident management](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-incident-management)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-incident-management-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/incident-managementhttps://api.ap2.datadoghq.com/api/v1/usage/incident-managementhttps://api.datadoghq.eu/api/v1/usage/incident-managementhttps://api.ddog-gov.com/api/v1/usage/incident-managementhttps://api.datadoghq.com/api/v1/usage/incident-managementhttps://api.us3.datadoghq.com/api/v1/usage/incident-managementhttps://api.us5.datadoghq.com/api/v1/usage/incident-management
### Overview
Get hourly usage for incident management. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetIncidentManagement-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetIncidentManagement-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetIncidentManagement-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetIncidentManagement-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the incident management usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for incident management.
hour
date-time
The hour for the usage.
monthly_active_users
int64
Contains the total number monthly active users from the start of the given hour's month until the given hour.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "monthly_active_users": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for incident management
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/incident-management?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for incident management
```
"""
Get hourly usage for incident management returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_incident_management(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for incident management
```
# Get hourly usage for incident management returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_incident_management((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for incident management
```
// Get hourly usage for incident management returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetIncidentManagement(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetIncidentManagementOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetIncidentManagement`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetIncidentManagement`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for incident management
```
// Get hourly usage for incident management returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetIncidentManagementOptionalParameters;
import com.datadog.api.client.v1.model.UsageIncidentManagementResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageIncidentManagementResponse result =
          apiInstance.getIncidentManagement(
              OffsetDateTime.now().plusDays(-5),
              new GetIncidentManagementOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getIncidentManagement");
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

#####  Get hourly usage for incident management
```
// Get hourly usage for incident management returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetIncidentManagementOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_incident_management(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetIncidentManagementOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for incident management
```
/**
 * Get hourly usage for incident management returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetIncidentManagementRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getIncidentManagement(params)
  .then((data: v1.UsageIncidentManagementResponse) => {
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
## [Get hourly usage for IoT](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-iot)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-iot-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/iothttps://api.ap2.datadoghq.com/api/v1/usage/iothttps://api.datadoghq.eu/api/v1/usage/iothttps://api.ddog-gov.com/api/v1/usage/iothttps://api.datadoghq.com/api/v1/usage/iothttps://api.us3.datadoghq.com/api/v1/usage/iothttps://api.us5.datadoghq.com/api/v1/usage/iot
### Overview
Get hourly usage for IoT. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageInternetOfThings-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageInternetOfThings-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageInternetOfThings-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageInternetOfThings-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the IoT usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for IoT.
hour
date-time
The hour for the usage.
iot_device_count
int64
The total number of IoT devices during a given hour.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "iot_device_count": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for IoT
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/iot?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for IoT
```
"""
Get hourly usage for IoT returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_internet_of_things(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for IoT
```
# Get hourly usage for IoT returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_internet_of_things((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for IoT
```
// Get hourly usage for IoT returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageInternetOfThings(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageInternetOfThingsOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageInternetOfThings`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageInternetOfThings`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for IoT
```
// Get hourly usage for IoT returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageInternetOfThingsOptionalParameters;
import com.datadog.api.client.v1.model.UsageIoTResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageIoTResponse result =
          apiInstance.getUsageInternetOfThings(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageInternetOfThingsOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageInternetOfThings");
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

#####  Get hourly usage for IoT
```
// Get hourly usage for IoT returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageInternetOfThingsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_internet_of_things(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageInternetOfThingsOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for IoT
```
/**
 * Get hourly usage for IoT returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageInternetOfThingsRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageInternetOfThings(params)
  .then((data: v1.UsageIoTResponse) => {
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
## [Get hourly usage for CSM Pro](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-csm-pro)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-csm-pro-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/cspmhttps://api.ap2.datadoghq.com/api/v1/usage/cspmhttps://api.datadoghq.eu/api/v1/usage/cspmhttps://api.ddog-gov.com/api/v1/usage/cspmhttps://api.datadoghq.com/api/v1/usage/cspmhttps://api.us3.datadoghq.com/api/v1/usage/cspmhttps://api.us5.datadoghq.com/api/v1/usage/cspm
### Overview
Get hourly usage for cloud security management (CSM) pro. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCloudSecurityPostureManagement-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCloudSecurityPostureManagement-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCloudSecurityPostureManagement-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCloudSecurityPostureManagement-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


The response containing the Cloud Security Management Pro usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Cloud Security Management Pro.
aas_host_count
double
The number of Cloud Security Management Pro Azure app services hosts during a given hour.
aws_host_count
double
The number of Cloud Security Management Pro AWS hosts during a given hour.
azure_host_count
double
The number of Cloud Security Management Pro Azure hosts during a given hour.
compliance_host_count
double
The number of Cloud Security Management Pro hosts during a given hour.
container_count
double
The total number of Cloud Security Management Pro containers during a given hour.
gcp_host_count
double
The number of Cloud Security Management Pro GCP hosts during a given hour.
host_count
double
The total number of Cloud Security Management Pro hosts during a given hour.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "aas_host_count": "number",
      "aws_host_count": "number",
      "azure_host_count": "number",
      "compliance_host_count": "number",
      "container_count": "number",
      "gcp_host_count": "number",
      "host_count": "number",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for CSM Pro
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/cspm?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for CSM Pro
```
"""
Get hourly usage for CSM Pro returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_cloud_security_posture_management(
        start_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for CSM Pro
```
# Get hourly usage for CSM Pro returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_cloud_security_posture_management((Time.now + -3 * 86400))

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for CSM Pro
```
// Get hourly usage for CSM Pro returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageCloudSecurityPostureManagement(ctx, time.Now().AddDate(0, 0, -3), *datadogV1.NewGetUsageCloudSecurityPostureManagementOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageCloudSecurityPostureManagement`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageCloudSecurityPostureManagement`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for CSM Pro
```
// Get hourly usage for CSM Pro returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageCloudSecurityPostureManagementResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageCloudSecurityPostureManagementResponse result =
          apiInstance.getUsageCloudSecurityPostureManagement(OffsetDateTime.now().plusDays(-3));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling UsageMeteringApi#getUsageCloudSecurityPostureManagement");
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

#####  Get hourly usage for CSM Pro
```
// Get hourly usage for CSM Pro returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageCloudSecurityPostureManagementOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_cloud_security_posture_management(
            DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageCloudSecurityPostureManagementOptionalParams::default(),
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

#####  Get hourly usage for CSM Pro
```
/**
 * Get hourly usage for CSM Pro returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageCloudSecurityPostureManagementRequest =
  {
    startHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
  };

apiInstance
  .getUsageCloudSecurityPostureManagement(params)
  .then((data: v1.UsageCloudSecurityPostureManagementResponse) => {
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
## [Get hourly usage for cloud workload security](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-cloud-workload-security)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-cloud-workload-security-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/cwshttps://api.ap2.datadoghq.com/api/v1/usage/cwshttps://api.datadoghq.eu/api/v1/usage/cwshttps://api.ddog-gov.com/api/v1/usage/cwshttps://api.datadoghq.com/api/v1/usage/cwshttps://api.us3.datadoghq.com/api/v1/usage/cwshttps://api.us5.datadoghq.com/api/v1/usage/cws
### Overview
Get hourly usage for cloud workload security. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCWS-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCWS-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCWS-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCWS-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the Cloud Workload Security usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Cloud Workload Security.
cws_container_count
int64
The total number of Cloud Workload Security container hours from the start of the given hour’s month until the given hour.
cws_host_count
int64
The total number of Cloud Workload Security host hours from the start of the given hour’s month until the given hour.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "cws_container_count": "integer",
      "cws_host_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for cloud workload security
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/cws?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for cloud workload security
```
"""
Get hourly usage for cloud workload security returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_cws(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for cloud workload security
```
# Get hourly usage for cloud workload security returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_cws((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for cloud workload security
```
// Get hourly usage for cloud workload security returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageCWS(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageCWSOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageCWS`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageCWS`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for cloud workload security
```
// Get hourly usage for cloud workload security returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageCWSOptionalParameters;
import com.datadog.api.client.v1.model.UsageCWSResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageCWSResponse result =
          apiInstance.getUsageCWS(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageCWSOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageCWS");
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

#####  Get hourly usage for cloud workload security
```
// Get hourly usage for cloud workload security returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageCWSOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_cws(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageCWSOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for cloud workload security
```
/**
 * Get hourly usage for cloud workload security returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageCWSRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageCWS(params)
  .then((data: v1.UsageCWSResponse) => {
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
## [Get hourly usage for database monitoring](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-database-monitoring)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-database-monitoring-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/dbmhttps://api.ap2.datadoghq.com/api/v1/usage/dbmhttps://api.datadoghq.eu/api/v1/usage/dbmhttps://api.ddog-gov.com/api/v1/usage/dbmhttps://api.datadoghq.com/api/v1/usage/dbmhttps://api.us3.datadoghq.com/api/v1/usage/dbmhttps://api.us5.datadoghq.com/api/v1/usage/dbm
### Overview
Get hourly usage for database monitoring **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageDBM-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageDBM-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageDBM-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageDBM-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the Database Monitoring usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Database Monitoring
dbm_host_count
int64
The total number of Database Monitoring host hours from the start of the given hour’s month until the given hour.
dbm_queries_count
int64
The total number of normalized Database Monitoring queries from the start of the given hour’s month until the given hour.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "dbm_host_count": "integer",
      "dbm_queries_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for database monitoring
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/dbm?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for database monitoring
```
"""
Get hourly usage for database monitoring returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_dbm(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for database monitoring
```
# Get hourly usage for database monitoring returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_dbm("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for database monitoring
```
// Get hourly usage for database monitoring returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageDBM(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageDBMOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageDBM`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageDBM`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for database monitoring
```
// Get hourly usage for database monitoring returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageDBMResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageDBMResponse result =
          apiInstance.getUsageDBM(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageDBM");
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

#####  Get hourly usage for database monitoring
```
// Get hourly usage for database monitoring returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageDBMOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_dbm(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageDBMOptionalParams::default(),
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

#####  Get hourly usage for database monitoring
```
/**
 * Get hourly usage for database monitoring returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageDBMRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageDBM(params)
  .then((data: v1.UsageDBMResponse) => {
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
## [Get hourly usage for sensitive data scanner](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-sensitive-data-scanner)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-sensitive-data-scanner-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/sdshttps://api.ap2.datadoghq.com/api/v1/usage/sdshttps://api.datadoghq.eu/api/v1/usage/sdshttps://api.ddog-gov.com/api/v1/usage/sdshttps://api.datadoghq.com/api/v1/usage/sdshttps://api.us3.datadoghq.com/api/v1/usage/sdshttps://api.us5.datadoghq.com/api/v1/usage/sds
### Overview
Get hourly usage for sensitive data scanner. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSDS-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSDS-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSDS-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageSDS-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the Sensitive Data Scanner usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for Sensitive Data Scanner.
apm_scanned_bytes
int64
The total number of bytes scanned of APM usage across all usage types by the Sensitive Data Scanner from the start of the given hour’s month until the given hour.
events_scanned_bytes
int64
The total number of bytes scanned of Events usage across all usage types by the Sensitive Data Scanner from the start of the given hour’s month until the given hour.
hour
date-time
The hour for the usage.
logs_scanned_bytes
int64
The total number of bytes scanned of logs usage by the Sensitive Data Scanner from the start of the given hour’s month until the given hour.
org_name
string
The organization name.
public_id
string
The organization public ID.
rum_scanned_bytes
int64
The total number of bytes scanned of RUM usage across all usage types by the Sensitive Data Scanner from the start of the given hour’s month until the given hour.
total_scanned_bytes
int64
The total number of bytes scanned across all usage types by the Sensitive Data Scanner from the start of the given hour’s month until the given hour.
```
{
  "usage": [
    {
      "apm_scanned_bytes": "integer",
      "events_scanned_bytes": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "logs_scanned_bytes": "integer",
      "org_name": "string",
      "public_id": "string",
      "rum_scanned_bytes": "integer",
      "total_scanned_bytes": "integer"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for sensitive data scanner
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/sds?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for sensitive data scanner
```
"""
Get hourly usage for sensitive data scanner returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_sds(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for sensitive data scanner
```
# Get hourly usage for sensitive data scanner returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_sds("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for sensitive data scanner
```
// Get hourly usage for sensitive data scanner returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageSDS(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageSDSOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageSDS`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageSDS`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for sensitive data scanner
```
// Get hourly usage for sensitive data scanner returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageSDSResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSDSResponse result =
          apiInstance.getUsageSDS(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageSDS");
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

#####  Get hourly usage for sensitive data scanner
```
// Get hourly usage for sensitive data scanner returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageSDSOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_sds(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageSDSOptionalParams::default(),
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

#####  Get hourly usage for sensitive data scanner
```
/**
 * Get hourly usage for sensitive data scanner returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageSDSRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageSDS(params)
  .then((data: v1.UsageSDSResponse) => {
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
## [Get hourly usage for RUM units](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-rum-units)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-rum-units-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/rumhttps://api.ap2.datadoghq.com/api/v1/usage/rumhttps://api.datadoghq.eu/api/v1/usage/rumhttps://api.ddog-gov.com/api/v1/usage/rumhttps://api.datadoghq.com/api/v1/usage/rumhttps://api.us3.datadoghq.com/api/v1/usage/rumhttps://api.us5.datadoghq.com/api/v1/usage/rum
### Overview
Get hourly usage for [RUM](https://docs.datadoghq.com/real_user_monitoring/) Units. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumUnits-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumUnits-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumUnits-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageRumUnits-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of RUM Units for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for RUM Units.
browser_rum_units
int64
The number of browser RUM units.
mobile_rum_units
int64
The number of mobile RUM units.
org_name
string
The organization name.
public_id
string
The organization public ID.
rum_units
int64
Total RUM units across mobile and browser RUM.
```
{
  "usage": [
    {
      "browser_rum_units": "integer",
      "mobile_rum_units": "integer",
      "org_name": "string",
      "public_id": "string",
      "rum_units": "integer"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for RUM units
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/rum?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for RUM units
```
"""
Get hourly usage for RUM units returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_rum_units(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for RUM units
```
# Get hourly usage for RUM units returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_rum_units("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for RUM units
```
// Get hourly usage for RUM units returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageRumUnits(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageRumUnitsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageRumUnits`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageRumUnits`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for RUM units
```
// Get hourly usage for RUM units returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageRumUnitsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageRumUnitsResponse result =
          apiInstance.getUsageRumUnits(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageRumUnits");
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

#####  Get hourly usage for RUM units
```
// Get hourly usage for RUM units returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageRumUnitsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_rum_units(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageRumUnitsOptionalParams::default(),
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

#####  Get hourly usage for RUM units
```
/**
 * Get hourly usage for RUM units returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageRumUnitsRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageRumUnits(params)
  .then((data: v1.UsageRumUnitsResponse) => {
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
## [Get hourly usage for profiled hosts](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-profiled-hosts)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-profiled-hosts-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/profilinghttps://api.ap2.datadoghq.com/api/v1/usage/profilinghttps://api.datadoghq.eu/api/v1/usage/profilinghttps://api.ddog-gov.com/api/v1/usage/profilinghttps://api.datadoghq.com/api/v1/usage/profilinghttps://api.us3.datadoghq.com/api/v1/usage/profilinghttps://api.us5.datadoghq.com/api/v1/usage/profiling
### Overview
Get hourly usage for profiled hosts. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageProfiling-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageProfiling-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageProfiling-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageProfiling-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the number of profiled hosts for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for profiled hosts.
aas_count
int64
Contains the total number of profiled Azure app services reporting during a given hour.
avg_container_agent_count
int64
Get average number of container agents for that hour.
host_count
int64
Contains the total number of profiled hosts reporting during a given hour.
hour
date-time
The hour for the usage.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "aas_count": "integer",
      "avg_container_agent_count": "integer",
      "host_count": "integer",
      "hour": "2019-09-19T10:00:00.000Z",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for profiled hosts
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/profiling?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for profiled hosts
```
"""
Get hourly usage for profiled hosts returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_profiling(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for profiled hosts
```
# Get hourly usage for profiled hosts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_profiling((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for profiled hosts
```
// Get hourly usage for profiled hosts returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageProfiling(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageProfilingOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageProfiling`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageProfiling`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for profiled hosts
```
// Get hourly usage for profiled hosts returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageProfilingOptionalParameters;
import com.datadog.api.client.v1.model.UsageProfilingResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageProfilingResponse result =
          apiInstance.getUsageProfiling(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageProfilingOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageProfiling");
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

#####  Get hourly usage for profiled hosts
```
// Get hourly usage for profiled hosts returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageProfilingOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_profiling(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageProfilingOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for profiled hosts
```
/**
 * Get hourly usage for profiled hosts returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageProfilingRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageProfiling(params)
  .then((data: v1.UsageProfilingResponse) => {
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
## [Get hourly usage for CI visibility](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-ci-visibility)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-ci-visibility-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/ci-apphttps://api.ap2.datadoghq.com/api/v1/usage/ci-apphttps://api.datadoghq.eu/api/v1/usage/ci-apphttps://api.ddog-gov.com/api/v1/usage/ci-apphttps://api.datadoghq.com/api/v1/usage/ci-apphttps://api.us3.datadoghq.com/api/v1/usage/ci-apphttps://api.us5.datadoghq.com/api/v1/usage/ci-app
### Overview
Get hourly usage for CI visibility (tests, pipeline, and spans). **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCIApp-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCIApp-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCIApp-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageCIApp-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


CI visibility usage response
Field
Type
Description
usage
[object]
Response containing CI visibility usage.
ci_pipeline_indexed_spans
int64
The number of spans for pipelines in the queried hour.
ci_test_indexed_spans
int64
The number of spans for tests in the queried hour.
ci_visibility_itr_committers
int64
Shows the total count of all active Git committers for Intelligent Test Runner in the current month. A committer is active if they commit at least 3 times in a given month.
ci_visibility_pipeline_committers
int64
Shows the total count of all active Git committers for Pipelines in the current month. A committer is active if they commit at least 3 times in a given month.
ci_visibility_test_committers
int64
The total count of all active Git committers for tests in the current month. A committer is active if they commit at least 3 times in a given month.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "ci_pipeline_indexed_spans": "integer",
      "ci_test_indexed_spans": "integer",
      "ci_visibility_itr_committers": "integer",
      "ci_visibility_pipeline_committers": "integer",
      "ci_visibility_test_committers": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for CI visibility
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/ci-app?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for CI visibility
```
"""
Get hourly usage for CI visibility returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_ci_app(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for CI visibility
```
# Get hourly usage for CI visibility returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_ci_app((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for CI visibility
```
// Get hourly usage for CI visibility returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageCIApp(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageCIAppOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageCIApp`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageCIApp`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for CI visibility
```
// Get hourly usage for CI visibility returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageCIAppOptionalParameters;
import com.datadog.api.client.v1.model.UsageCIVisibilityResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageCIVisibilityResponse result =
          apiInstance.getUsageCIApp(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageCIAppOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageCIApp");
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

#####  Get hourly usage for CI visibility
```
// Get hourly usage for CI visibility returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageCIAppOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_ci_app(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageCIAppOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for CI visibility
```
/**
 * Get hourly usage for CI visibility returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageCIAppRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageCIApp(params)
  .then((data: v1.UsageCIVisibilityResponse) => {
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
## [Get hourly usage for online archive](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-online-archive)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-online-archive-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/online-archivehttps://api.ap2.datadoghq.com/api/v1/usage/online-archivehttps://api.datadoghq.eu/api/v1/usage/online-archivehttps://api.ddog-gov.com/api/v1/usage/online-archivehttps://api.datadoghq.com/api/v1/usage/online-archivehttps://api.us3.datadoghq.com/api/v1/usage/online-archivehttps://api.us5.datadoghq.com/api/v1/usage/online-archive
### Overview
Get hourly usage for online archive. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family). Refer to [Migrating from the V1 Hourly Usage APIs to V2](https://docs.datadoghq.com/account_management/guide/hourly-usage-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageOnlineArchive-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageOnlineArchive-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageOnlineArchive-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageOnlineArchive-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Online Archive usage response.
Field
Type
Description
usage
[object]
Response containing Online Archive usage.
hour
date-time
The hour for the usage.
online_archive_events_count
int64
Total count of online archived events within the hour.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "online_archive_events_count": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for online archive
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/online-archive?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for online archive
```
"""
Get hourly usage for online archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_online_archive(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for online archive
```
# Get hourly usage for online archive returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_usage_online_archive("2021-11-11T11:11:11.111+00:00")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for online archive
```
// Get hourly usage for online archive returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageOnlineArchive(ctx, time.Date(2021, 11, 11, 11, 11, 11, 111000, time.UTC), *datadogV1.NewGetUsageOnlineArchiveOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageOnlineArchive`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageOnlineArchive`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for online archive
```
// Get hourly usage for online archive returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageOnlineArchiveResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageOnlineArchiveResponse result =
          apiInstance.getUsageOnlineArchive(OffsetDateTime.parse("2021-11-11T11:11:11.111+00:00"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageOnlineArchive");
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

#####  Get hourly usage for online archive
```
// Get hourly usage for online archive returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageOnlineArchiveOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_online_archive(
            DateTime::parse_from_rfc3339("2021-11-11T11:11:11.111000+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageOnlineArchiveOptionalParams::default(),
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

#####  Get hourly usage for online archive
```
/**
 * Get hourly usage for online archive returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageOnlineArchiveRequest = {
  startHr: new Date(2021, 11, 11, 11, 11, 11, 111000),
};

apiInstance
  .getUsageOnlineArchive(params)
  .then((data: v1.UsageOnlineArchiveResponse) => {
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
## [Get hourly usage for Lambda traced invocations](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-lambda-traced-invocations)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-lambda-traced-invocations-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/lambda_traced_invocationshttps://api.ap2.datadoghq.com/api/v2/usage/lambda_traced_invocationshttps://api.datadoghq.eu/api/v2/usage/lambda_traced_invocationshttps://api.ddog-gov.com/api/v2/usage/lambda_traced_invocationshttps://api.datadoghq.com/api/v2/usage/lambda_traced_invocationshttps://api.us3.datadoghq.com/api/v2/usage/lambda_traced_invocationshttps://api.us5.datadoghq.com/api/v2/usage/lambda_traced_invocations
### Overview
Get hourly usage for Lambda traced invocations. **Note:** This endpoint has been deprecated.. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family) This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambdaTracedInvocations-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambdaTracedInvocations-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambdaTracedInvocations-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageLambdaTracedInvocations-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Lambda Traced Invocations usage response.
Field
Type
Description
data
[object]
Response containing Lambda Traced Invocations usage.
attributes
object
Usage attributes data.
org_name
string
The organization name.
product_family
string
The product for which usage is being reported.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
timeseries
[object]
List of usage data reported for each requested hour.
timestamp
date-time
Datetime in ISO-8601 format, UTC. The hour for the usage.
value
int64
Contains the number measured for the given usage_type during the hour.
usage_type
enum
Usage type that is being measured. Allowed enum values: `app_sec_host_count,observability_pipelines_bytes_processed,lambda_traced_invocations_count`
id
string
Unique ID of the response.
type
enum
Type of usage data. Allowed enum values: `usage_timeseries`
default: `usage_timeseries`
```
{
  "data": [
    {
      "attributes": {
        "org_name": "string",
        "product_family": "string",
        "public_id": "string",
        "region": "string",
        "timeseries": [
          {
            "timestamp": "2019-09-19T10:00:00.000Z",
            "value": "integer"
          }
        ],
        "usage_type": "observability_pipelines_bytes_processed"
      },
      "id": "string",
      "type": "usage_timeseries"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for Lambda traced invocations
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/lambda_traced_invocations?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for Lambda traced invocations
```
"""
Get hourly usage for Lambda traced invocations returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_lambda_traced_invocations(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for Lambda traced invocations
```
# Get hourly usage for Lambda traced invocations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_lambda_traced_invocations((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for Lambda traced invocations
```
// Get hourly usage for Lambda traced invocations returns "OK" response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageLambdaTracedInvocations(ctx, time.Now().AddDate(0, 0, -5), *datadogV2.NewGetUsageLambdaTracedInvocationsOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageLambdaTracedInvocations`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageLambdaTracedInvocations`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for Lambda traced invocations
```
// Get hourly usage for Lambda traced invocations returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.api.UsageMeteringApi.GetUsageLambdaTracedInvocationsOptionalParameters;
import com.datadog.api.client.v2.model.UsageLambdaTracedInvocationsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageLambdaTracedInvocationsResponse result =
          apiInstance.getUsageLambdaTracedInvocations(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageLambdaTracedInvocationsOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageLambdaTracedInvocations");
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

#####  Get hourly usage for Lambda traced invocations
```
// Get hourly usage for Lambda traced invocations returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetUsageLambdaTracedInvocationsOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_lambda_traced_invocations(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageLambdaTracedInvocationsOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for Lambda traced invocations
```
/**
 * Get hourly usage for Lambda traced invocations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetUsageLambdaTracedInvocationsRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageLambdaTracedInvocations(params)
  .then((data: v2.UsageLambdaTracedInvocationsResponse) => {
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
## [Get hourly usage for application security](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-application-security)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-application-security-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/application_securityhttps://api.ap2.datadoghq.com/api/v2/usage/application_securityhttps://api.datadoghq.eu/api/v2/usage/application_securityhttps://api.ddog-gov.com/api/v2/usage/application_securityhttps://api.datadoghq.com/api/v2/usage/application_securityhttps://api.us3.datadoghq.com/api/v2/usage/application_securityhttps://api.us5.datadoghq.com/api/v2/usage/application_security
### Overview
Get hourly usage for application security . **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family) This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageApplicationSecurityMonitoring-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageApplicationSecurityMonitoring-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageApplicationSecurityMonitoring-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageApplicationSecurityMonitoring-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Application Security Monitoring usage response.
Field
Type
Description
data
[object]
Response containing Application Security Monitoring usage.
attributes
object
Usage attributes data.
org_name
string
The organization name.
product_family
string
The product for which usage is being reported.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
timeseries
[object]
List of usage data reported for each requested hour.
timestamp
date-time
Datetime in ISO-8601 format, UTC. The hour for the usage.
value
int64
Contains the number measured for the given usage_type during the hour.
usage_type
enum
Usage type that is being measured. Allowed enum values: `app_sec_host_count,observability_pipelines_bytes_processed,lambda_traced_invocations_count`
id
string
Unique ID of the response.
type
enum
Type of usage data. Allowed enum values: `usage_timeseries`
default: `usage_timeseries`
```
{
  "data": [
    {
      "attributes": {
        "org_name": "string",
        "product_family": "string",
        "public_id": "string",
        "region": "string",
        "timeseries": [
          {
            "timestamp": "2019-09-19T10:00:00.000Z",
            "value": "integer"
          }
        ],
        "usage_type": "observability_pipelines_bytes_processed"
      },
      "id": "string",
      "type": "usage_timeseries"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for application security
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/application_security?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for application security
```
"""
Get hourly usage for application security returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_application_security_monitoring(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for application security
```
# Get hourly usage for application security returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_application_security_monitoring((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for application security
```
// Get hourly usage for application security returns "OK" response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageApplicationSecurityMonitoring(ctx, time.Now().AddDate(0, 0, -5), *datadogV2.NewGetUsageApplicationSecurityMonitoringOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageApplicationSecurityMonitoring`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageApplicationSecurityMonitoring`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for application security
```
// Get hourly usage for application security returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.api.UsageMeteringApi.GetUsageApplicationSecurityMonitoringOptionalParameters;
import com.datadog.api.client.v2.model.UsageApplicationSecurityMonitoringResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageApplicationSecurityMonitoringResponse result =
          apiInstance.getUsageApplicationSecurityMonitoring(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageApplicationSecurityMonitoringOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling UsageMeteringApi#getUsageApplicationSecurityMonitoring");
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

#####  Get hourly usage for application security
```
// Get hourly usage for application security returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetUsageApplicationSecurityMonitoringOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_application_security_monitoring(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageApplicationSecurityMonitoringOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for application security
```
/**
 * Get hourly usage for application security returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetUsageApplicationSecurityMonitoringRequest =
  {
    startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
    endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
  };

apiInstance
  .getUsageApplicationSecurityMonitoring(params)
  .then((data: v2.UsageApplicationSecurityMonitoringResponse) => {
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
## [Get hourly usage for observability pipelines](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-observability-pipelines)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-observability-pipelines-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/observability_pipelineshttps://api.ap2.datadoghq.com/api/v2/usage/observability_pipelineshttps://api.datadoghq.eu/api/v2/usage/observability_pipelineshttps://api.ddog-gov.com/api/v2/usage/observability_pipelineshttps://api.datadoghq.com/api/v2/usage/observability_pipelineshttps://api.us3.datadoghq.com/api/v2/usage/observability_pipelineshttps://api.us5.datadoghq.com/api/v2/usage/observability_pipelines
### Overview
Get hourly usage for observability pipelines. **Note:** This endpoint has been deprecated. Hourly usage data for all products is now available in the [Get hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family) This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageObservabilityPipelines-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageObservabilityPipelines-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageObservabilityPipelines-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageObservabilityPipelines-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Observability Pipelines usage response.
Field
Type
Description
data
[object]
Response containing Observability Pipelines usage.
attributes
object
Usage attributes data.
org_name
string
The organization name.
product_family
string
The product for which usage is being reported.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
timeseries
[object]
List of usage data reported for each requested hour.
timestamp
date-time
Datetime in ISO-8601 format, UTC. The hour for the usage.
value
int64
Contains the number measured for the given usage_type during the hour.
usage_type
enum
Usage type that is being measured. Allowed enum values: `app_sec_host_count,observability_pipelines_bytes_processed,lambda_traced_invocations_count`
id
string
Unique ID of the response.
type
enum
Type of usage data. Allowed enum values: `usage_timeseries`
default: `usage_timeseries`
```
{
  "data": [
    {
      "attributes": {
        "org_name": "string",
        "product_family": "string",
        "public_id": "string",
        "region": "string",
        "timeseries": [
          {
            "timestamp": "2019-09-19T10:00:00.000Z",
            "value": "integer"
          }
        ],
        "usage_type": "observability_pipelines_bytes_processed"
      },
      "id": "string",
      "type": "usage_timeseries"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for observability pipelines
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/observability_pipelines?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for observability pipelines
```
"""
Get hourly usage for observability pipelines returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_observability_pipelines(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for observability pipelines
```
# Get hourly usage for observability pipelines returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_observability_pipelines((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for observability pipelines
```
// Get hourly usage for observability pipelines returns "OK" response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageObservabilityPipelines(ctx, time.Now().AddDate(0, 0, -5), *datadogV2.NewGetUsageObservabilityPipelinesOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageObservabilityPipelines`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageObservabilityPipelines`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for observability pipelines
```
// Get hourly usage for observability pipelines returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.api.UsageMeteringApi.GetUsageObservabilityPipelinesOptionalParameters;
import com.datadog.api.client.v2.model.UsageObservabilityPipelinesResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageObservabilityPipelinesResponse result =
          apiInstance.getUsageObservabilityPipelines(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageObservabilityPipelinesOptionalParameters()
                  .endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageObservabilityPipelines");
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

#####  Get hourly usage for observability pipelines
```
// Get hourly usage for observability pipelines returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetUsageObservabilityPipelinesOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_observability_pipelines(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageObservabilityPipelinesOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for observability pipelines
```
/**
 * Get hourly usage for observability pipelines returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetUsageObservabilityPipelinesRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageObservabilityPipelines(params)
  .then((data: v2.UsageObservabilityPipelinesResponse) => {
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
## [Get hourly usage for audit logs](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-audit-logs)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-audit-logs-v1)


GET https://api.ap1.datadoghq.com/api/v1/usage/audit_logshttps://api.ap2.datadoghq.com/api/v1/usage/audit_logshttps://api.datadoghq.eu/api/v1/usage/audit_logshttps://api.ddog-gov.com/api/v1/usage/audit_logshttps://api.datadoghq.com/api/v1/usage/audit_logshttps://api.us3.datadoghq.com/api/v1/usage/audit_logshttps://api.us5.datadoghq.com/api/v1/usage/audit_logs
### Overview
Get hourly usage for audit logs. **Note:** This endpoint has been deprecated. This endpoint requires the `usage_read` permission.
OAuth apps require the `usage_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_hr [_required_]
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
end_hr
string
Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAuditLogs-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAuditLogs-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAuditLogs-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetUsageAuditLogs-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing the audit logs usage for each hour for a given organization.
Field
Type
Description
usage
[object]
Get hourly usage for audit logs.
hour
date-time
The hour for the usage.
lines_indexed
int64
The total number of audit logs lines indexed during a given hour.
org_name
string
The organization name.
public_id
string
The organization public ID.
```
{
  "usage": [
    {
      "hour": "2019-09-19T10:00:00.000Z",
      "lines_indexed": "integer",
      "org_name": "string",
      "public_id": "string"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get hourly usage for audit logs
Copy
```
                  # Required query arguments  
export start_hr="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/usage/audit_logs?start_hr=${start_hr}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get hourly usage for audit logs
```
"""
Get hourly usage for audit logs returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_audit_logs(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get hourly usage for audit logs
```
# Get hourly usage for audit logs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
opts = {
  end_hr: (Time.now + -3 * 86400),
}
p api_instance.get_usage_audit_logs((Time.now + -5 * 86400), opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get hourly usage for audit logs
```
// Get hourly usage for audit logs returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetUsageAuditLogs(ctx, time.Now().AddDate(0, 0, -5), *datadogV1.NewGetUsageAuditLogsOptionalParameters().WithEndHr(time.Now().AddDate(0, 0, -3)))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetUsageAuditLogs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetUsageAuditLogs`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get hourly usage for audit logs
```
// Get hourly usage for audit logs returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.api.UsageMeteringApi.GetUsageAuditLogsOptionalParameters;
import com.datadog.api.client.v1.model.UsageAuditLogsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageAuditLogsResponse result =
          apiInstance.getUsageAuditLogs(
              OffsetDateTime.now().plusDays(-5),
              new GetUsageAuditLogsOptionalParameters().endHr(OffsetDateTime.now().plusDays(-3)));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getUsageAuditLogs");
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

#####  Get hourly usage for audit logs
```
// Get hourly usage for audit logs returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetUsageAuditLogsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_usage_audit_logs(
            DateTime::parse_from_rfc3339("2021-11-06T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetUsageAuditLogsOptionalParams::default().end_hr(
                DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                    .expect("Failed to parse datetime")
                    .with_timezone(&Utc),
            ),
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

#####  Get hourly usage for audit logs
```
/**
 * Get hourly usage for audit logs returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetUsageAuditLogsRequest = {
  startHr: new Date(new Date().getTime() + -5 * 86400 * 1000),
  endHr: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getUsageAuditLogs(params)
  .then((data: v1.UsageAuditLogsResponse) => {
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
## [Get the list of available daily custom reports](https://docs.datadoghq.com/api/latest/usage-metering/#get-the-list-of-available-daily-custom-reports)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-the-list-of-available-daily-custom-reports-v1)


GET https://api.ap1.datadoghq.com/api/v1/daily_custom_reportshttps://api.ap2.datadoghq.com/api/v1/daily_custom_reportshttps://api.datadoghq.eu/api/v1/daily_custom_reportshttps://api.ddog-gov.com/api/v1/daily_custom_reportshttps://api.datadoghq.com/api/v1/daily_custom_reportshttps://api.us3.datadoghq.com/api/v1/daily_custom_reportshttps://api.us5.datadoghq.com/api/v1/daily_custom_reports
### Overview
Get daily custom reports. **Note:** This endpoint will be fully deprecated on December 1, 2022. Refer to [Migrating from v1 to v2 of the Usage Attribution API](https://docs.datadoghq.com/account_management/guide/usage-attribution-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
The number of files to return in the response. `[default=60]`.
page[number]
integer
The identifier of the first page to return. This parameter is used for the pagination feature `[default=0]`.
sort_dir
enum
The direction to sort by: `[desc, asc]`.  
Allowed enum values: `desc, asc`
sort
enum
The field to sort by: `[computed_on, size, start_date, end_date]`.  
Allowed enum values: `computed_on, size, start_date, end_date`
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetDailyCustomReports-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetDailyCustomReports-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetDailyCustomReports-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing available custom reports.
Field
Type
Description
data
[object]
An array of available custom reports.
attributes
object
The response containing attributes for custom reports.
computed_on
string
The date the specified custom report was computed.
end_date
string
The ending date of custom report.
size
int64
size
start_date
string
The starting date of custom report.
tags
[string]
A list of tags to apply to custom reports.
id
string
The date for specified custom reports.
type
enum
The type of reports. Allowed enum values: `reports`
default: `reports`
meta
object
The object containing document metadata.
page
object
The object containing page total count.
total_count
int64
Total page count.
```
{
  "data": [
    {
      "attributes": {
        "computed_on": "string",
        "end_date": "string",
        "size": "integer",
        "start_date": "string",
        "tags": [
          "env"
        ]
      },
      "id": "string",
      "type": "reports"
    }
  ],
  "meta": {
    "page": {
      "total_count": "integer"
    }
  }
}
```

Copy
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get the list of available daily custom reports
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/daily_custom_reports" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the list of available daily custom reports
```
"""
Get the list of available daily custom reports returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_daily_custom_reports()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the list of available daily custom reports
```
# Get the list of available daily custom reports returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_daily_custom_reports()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the list of available daily custom reports
```
// Get the list of available daily custom reports returns "OK" response

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
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetDailyCustomReports(ctx, *datadogV1.NewGetDailyCustomReportsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetDailyCustomReports`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetDailyCustomReports`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the list of available daily custom reports
```
// Get the list of available daily custom reports returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageCustomReportsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageCustomReportsResponse result = apiInstance.getDailyCustomReports();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getDailyCustomReports");
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

#####  Get the list of available daily custom reports
```
// Get the list of available daily custom reports returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetDailyCustomReportsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_daily_custom_reports(GetDailyCustomReportsOptionalParams::default())
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

#####  Get the list of available daily custom reports
```
/**
 * Get the list of available daily custom reports returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

apiInstance
  .getDailyCustomReports()
  .then((data: v1.UsageCustomReportsResponse) => {
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
## [Get specified daily custom reports](https://docs.datadoghq.com/api/latest/usage-metering/#get-specified-daily-custom-reports)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-specified-daily-custom-reports-v1)


GET https://api.ap1.datadoghq.com/api/v1/daily_custom_reports/{report_id}https://api.ap2.datadoghq.com/api/v1/daily_custom_reports/{report_id}https://api.datadoghq.eu/api/v1/daily_custom_reports/{report_id}https://api.ddog-gov.com/api/v1/daily_custom_reports/{report_id}https://api.datadoghq.com/api/v1/daily_custom_reports/{report_id}https://api.us3.datadoghq.com/api/v1/daily_custom_reports/{report_id}https://api.us5.datadoghq.com/api/v1/daily_custom_reports/{report_id}
### Overview
Get specified daily custom reports. **Note:** This endpoint will be fully deprecated on December 1, 2022. Refer to [Migrating from v1 to v2 of the Usage Attribution API](https://docs.datadoghq.com/account_management/guide/usage-attribution-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
report_id [_required_]
string
Date of the report in the format `YYYY-MM-DD`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedDailyCustomReports-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedDailyCustomReports-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedDailyCustomReports-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedDailyCustomReports-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Returns available specified custom reports.
Field
Type
Description
data
object
Response containing date and type for specified custom reports.
attributes
object
The response containing attributes for specified custom reports.
computed_on
string
The date the specified custom report was computed.
end_date
string
The ending date of specified custom report.
location
string
A downloadable file for the specified custom reporting file.
size
int64
size
start_date
string
The starting date of specified custom report.
tags
[string]
A list of tags to apply to specified custom reports.
id
string
The date for specified custom reports.
type
enum
The type of reports. Allowed enum values: `reports`
default: `reports`
meta
object
The object containing document metadata.
page
object
The object containing page total count for specified ID.
total_count
int64
Total page count.
```
{
  "data": {
    "attributes": {
      "computed_on": "string",
      "end_date": "string",
      "location": "https://an-s3-or-gs-bucket.s3.amazonaws.com",
      "size": "integer",
      "start_date": "string",
      "tags": [
        "env"
      ]
    },
    "id": "string",
    "type": "reports"
  },
  "meta": {
    "page": {
      "total_count": "integer"
    }
  }
}
```

Copy
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get specified daily custom reports
Copy
```
                  # Path parameters  
export report_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/daily_custom_reports/${report_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get specified daily custom reports
```
"""
Get specified daily custom reports returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_specified_daily_custom_reports(
        report_id="2022-03-20",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get specified daily custom reports
```
# Get specified daily custom reports returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_specified_daily_custom_reports("2022-03-20")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get specified daily custom reports
```
// Get specified daily custom reports returns "OK" response

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
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetSpecifiedDailyCustomReports(ctx, "2022-03-20")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetSpecifiedDailyCustomReports`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetSpecifiedDailyCustomReports`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get specified daily custom reports
```
// Get specified daily custom reports returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageSpecifiedCustomReportsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSpecifiedCustomReportsResponse result =
          apiInstance.getSpecifiedDailyCustomReports("2022-03-20");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getSpecifiedDailyCustomReports");
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

#####  Get specified daily custom reports
```
// Get specified daily custom reports returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_specified_daily_custom_reports("2022-03-20".to_string())
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

#####  Get specified daily custom reports
```
/**
 * Get specified daily custom reports returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetSpecifiedDailyCustomReportsRequest = {
  reportId: "2022-03-20",
};

apiInstance
  .getSpecifiedDailyCustomReports(params)
  .then((data: v1.UsageSpecifiedCustomReportsResponse) => {
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
## [Get the list of available monthly custom reports](https://docs.datadoghq.com/api/latest/usage-metering/#get-the-list-of-available-monthly-custom-reports)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-the-list-of-available-monthly-custom-reports-v1)


GET https://api.ap1.datadoghq.com/api/v1/monthly_custom_reportshttps://api.ap2.datadoghq.com/api/v1/monthly_custom_reportshttps://api.datadoghq.eu/api/v1/monthly_custom_reportshttps://api.ddog-gov.com/api/v1/monthly_custom_reportshttps://api.datadoghq.com/api/v1/monthly_custom_reportshttps://api.us3.datadoghq.com/api/v1/monthly_custom_reportshttps://api.us5.datadoghq.com/api/v1/monthly_custom_reports
### Overview
Get monthly custom reports. **Note:** This endpoint will be fully deprecated on December 1, 2022. Refer to [Migrating from v1 to v2 of the Usage Attribution API](https://docs.datadoghq.com/account_management/guide/usage-attribution-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
The number of files to return in the response `[default=60].`
page[number]
integer
The identifier of the first page to return. This parameter is used for the pagination feature `[default=0]`.
sort_dir
enum
The direction to sort by: `[desc, asc]`.  
Allowed enum values: `desc, asc`
sort
enum
The field to sort by: `[computed_on, size, start_date, end_date]`.  
Allowed enum values: `computed_on, size, start_date, end_date`
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyCustomReports-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyCustomReports-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetMonthlyCustomReports-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Response containing available custom reports.
Field
Type
Description
data
[object]
An array of available custom reports.
attributes
object
The response containing attributes for custom reports.
computed_on
string
The date the specified custom report was computed.
end_date
string
The ending date of custom report.
size
int64
size
start_date
string
The starting date of custom report.
tags
[string]
A list of tags to apply to custom reports.
id
string
The date for specified custom reports.
type
enum
The type of reports. Allowed enum values: `reports`
default: `reports`
meta
object
The object containing document metadata.
page
object
The object containing page total count.
total_count
int64
Total page count.
```
{
  "data": [
    {
      "attributes": {
        "computed_on": "string",
        "end_date": "string",
        "size": "integer",
        "start_date": "string",
        "tags": [
          "env"
        ]
      },
      "id": "string",
      "type": "reports"
    }
  ],
  "meta": {
    "page": {
      "total_count": "integer"
    }
  }
}
```

Copy
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get the list of available monthly custom reports
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monthly_custom_reports" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the list of available monthly custom reports
```
"""
Get the list of available monthly custom reports returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_monthly_custom_reports()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the list of available monthly custom reports
```
# Get the list of available monthly custom reports returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_monthly_custom_reports()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the list of available monthly custom reports
```
// Get the list of available monthly custom reports returns "OK" response

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
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetMonthlyCustomReports(ctx, *datadogV1.NewGetMonthlyCustomReportsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetMonthlyCustomReports`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetMonthlyCustomReports`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the list of available monthly custom reports
```
// Get the list of available monthly custom reports returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageCustomReportsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageCustomReportsResponse result = apiInstance.getMonthlyCustomReports();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getMonthlyCustomReports");
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

#####  Get the list of available monthly custom reports
```
// Get the list of available monthly custom reports returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::GetMonthlyCustomReportsOptionalParams;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_monthly_custom_reports(GetMonthlyCustomReportsOptionalParams::default())
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

#####  Get the list of available monthly custom reports
```
/**
 * Get the list of available monthly custom reports returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

apiInstance
  .getMonthlyCustomReports()
  .then((data: v1.UsageCustomReportsResponse) => {
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
## [Get specified monthly custom reports](https://docs.datadoghq.com/api/latest/usage-metering/#get-specified-monthly-custom-reports)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-specified-monthly-custom-reports-v1)


GET https://api.ap1.datadoghq.com/api/v1/monthly_custom_reports/{report_id}https://api.ap2.datadoghq.com/api/v1/monthly_custom_reports/{report_id}https://api.datadoghq.eu/api/v1/monthly_custom_reports/{report_id}https://api.ddog-gov.com/api/v1/monthly_custom_reports/{report_id}https://api.datadoghq.com/api/v1/monthly_custom_reports/{report_id}https://api.us3.datadoghq.com/api/v1/monthly_custom_reports/{report_id}https://api.us5.datadoghq.com/api/v1/monthly_custom_reports/{report_id}
### Overview
Get specified monthly custom reports. **Note:** This endpoint will be fully deprecated on December 1, 2022. Refer to [Migrating from v1 to v2 of the Usage Attribution API](https://docs.datadoghq.com/account_management/guide/usage-attribution-migration/) for the associated migration guide. This endpoint requires the `usage_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
report_id [_required_]
string
Date of the report in the format `YYYY-MM-DD`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedMonthlyCustomReports-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedMonthlyCustomReports-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedMonthlyCustomReports-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedMonthlyCustomReports-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetSpecifiedMonthlyCustomReports-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Returns available specified custom reports.
Field
Type
Description
data
object
Response containing date and type for specified custom reports.
attributes
object
The response containing attributes for specified custom reports.
computed_on
string
The date the specified custom report was computed.
end_date
string
The ending date of specified custom report.
location
string
A downloadable file for the specified custom reporting file.
size
int64
size
start_date
string
The starting date of specified custom report.
tags
[string]
A list of tags to apply to specified custom reports.
id
string
The date for specified custom reports.
type
enum
The type of reports. Allowed enum values: `reports`
default: `reports`
meta
object
The object containing document metadata.
page
object
The object containing page total count for specified ID.
total_count
int64
Total page count.
```
{
  "data": {
    "attributes": {
      "computed_on": "string",
      "end_date": "string",
      "location": "https://an-s3-or-gs-bucket.s3.amazonaws.com",
      "size": "integer",
      "start_date": "string",
      "tags": [
        "env"
      ]
    },
    "id": "string",
    "type": "reports"
  },
  "meta": {
    "page": {
      "total_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get specified monthly custom reports
Copy
```
                  # Path parameters  
export report_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monthly_custom_reports/${report_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get specified monthly custom reports
```
"""
Get specified monthly custom reports returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_specified_monthly_custom_reports(
        report_id="2021-05-01",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get specified monthly custom reports
```
# Get specified monthly custom reports returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::UsageMeteringAPI.new
p api_instance.get_specified_monthly_custom_reports("2021-05-01")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get specified monthly custom reports
```
// Get specified monthly custom reports returns "OK" response

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
	api := datadogV1.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetSpecifiedMonthlyCustomReports(ctx, "2021-05-01")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetSpecifiedMonthlyCustomReports`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetSpecifiedMonthlyCustomReports`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get specified monthly custom reports
```
// Get specified monthly custom reports returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.UsageMeteringApi;
import com.datadog.api.client.v1.model.UsageSpecifiedCustomReportsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      UsageSpecifiedCustomReportsResponse result =
          apiInstance.getSpecifiedMonthlyCustomReports("2021-05-01");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling UsageMeteringApi#getSpecifiedMonthlyCustomReports");
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

#####  Get specified monthly custom reports
```
// Get specified monthly custom reports returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_specified_monthly_custom_reports("2021-05-01".to_string())
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

#####  Get specified monthly custom reports
```
/**
 * Get specified monthly custom reports returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.UsageMeteringApi(configuration);

const params: v1.UsageMeteringApiGetSpecifiedMonthlyCustomReportsRequest = {
  reportId: "2021-05-01",
};

apiInstance
  .getSpecifiedMonthlyCustomReports(params)
  .then((data: v1.UsageSpecifiedCustomReportsResponse) => {
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
## [Get cost across multi-org account](https://docs.datadoghq.com/api/latest/usage-metering/#get-cost-across-multi-org-account)
  * [v2 (deprecated)](https://docs.datadoghq.com/api/latest/usage-metering/#get-cost-across-multi-org-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/usage/cost_by_orghttps://api.ap2.datadoghq.com/api/v2/usage/cost_by_orghttps://api.datadoghq.eu/api/v2/usage/cost_by_orghttps://api.ddog-gov.com/api/v2/usage/cost_by_orghttps://api.datadoghq.com/api/v2/usage/cost_by_orghttps://api.us3.datadoghq.com/api/v2/usage/cost_by_orghttps://api.us5.datadoghq.com/api/v2/usage/cost_by_org
### Overview
Get cost across multi-org account. Cost by org data for a given month becomes available no later than the 16th of the following month. **Note:** This endpoint has been deprecated. Please use the new endpoint [`/historical_cost`](https://docs.datadoghq.com/api/latest/usage-metering/#get-historical-cost-across-your-account) instead.
This endpoint is only accessible for [parent-level organizations](https://docs.datadoghq.com/account_management/multi_organization/).
This endpoint requires all of the following permissions:
* `usage_read`
* `billing_read`
  

OAuth apps require the `usage_read, billing_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#usage-metering) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
start_month [_required_]
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost beginning this month.
end_month
string
Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost ending this month.
### Response
  * [200](https://docs.datadoghq.com/api/latest/usage-metering/#GetCostByOrg-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/usage-metering/#GetCostByOrg-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/usage-metering/#GetCostByOrg-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/usage-metering/#GetCostByOrg-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


Chargeback Summary response.
Field
Type
Description
data
[object]
Response containing Chargeback Summary.
attributes
object
Cost attributes data.
account_name
string
The account name.
account_public_id
string
The account public ID.
charges
[object]
List of charges data reported for the requested month.
charge_type
string
The type of charge for a particular product.
cost
double
The cost for a particular product and charge type during a given month.
product_name
string
The product for which cost is being reported.
date
date-time
The month requested.
org_name
string
The organization name.
public_id
string
The organization public ID.
region
string
The region of the Datadog instance that the organization belongs to.
total_cost
double
The total cost of products for the month.
id
string
Unique ID of the response.
type
enum
Type of cost data. Allowed enum values: `cost_by_org`
default: `cost_by_org`
```
{
  "data": [
    {
      "attributes": {
        "account_name": "string",
        "account_public_id": "string",
        "charges": [
          {
            "charge_type": "on_demand",
            "cost": "number",
            "product_name": "infra_host"
          }
        ],
        "date": "2019-09-19T10:00:00.000Z",
        "org_name": "string",
        "public_id": "string",
        "region": "string",
        "total_cost": "number"
      },
      "id": "string",
      "type": "cost_by_org"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
Forbidden - User is not authorized
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Model](https://docs.datadoghq.com/api/latest/usage-metering/)
  * [Example](https://docs.datadoghq.com/api/latest/usage-metering/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/usage-metering/?code-lang=typescript)


#####  Get cost across multi-org account
Copy
```
                  # Required query arguments  
export start_month="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/usage/cost_by_org?start_month=${start_month}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get cost across multi-org account
```
"""
Get cost across multi-org account returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_cost_by_org(
        start_month=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get cost across multi-org account
```
# Get cost across multi-org account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::UsageMeteringAPI.new
p api_instance.get_cost_by_org((Time.now + -3 * 86400))

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get cost across multi-org account
```
// Get cost across multi-org account returns "OK" response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewUsageMeteringApi(apiClient)
	resp, r, err := api.GetCostByOrg(ctx, time.Now().AddDate(0, 0, -3), *datadogV2.NewGetCostByOrgOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageMeteringApi.GetCostByOrg`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `UsageMeteringApi.GetCostByOrg`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get cost across multi-org account
```
// Get cost across multi-org account returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.UsageMeteringApi;
import com.datadog.api.client.v2.model.CostByOrgResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    UsageMeteringApi apiInstance = new UsageMeteringApi(defaultClient);

    try {
      CostByOrgResponse result = apiInstance.getCostByOrg(OffsetDateTime.now().plusDays(-3));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageMeteringApi#getCostByOrg");
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

#####  Get cost across multi-org account
```
// Get cost across multi-org account returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_usage_metering::GetCostByOrgOptionalParams;
use datadog_api_client::datadogV2::api_usage_metering::UsageMeteringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = UsageMeteringAPI::with_config(configuration);
    let resp = api
        .get_cost_by_org(
            DateTime::parse_from_rfc3339("2021-11-08T11:11:11+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
            GetCostByOrgOptionalParams::default(),
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

#####  Get cost across multi-org account
```
/**
 * Get cost across multi-org account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.UsageMeteringApi(configuration);

const params: v2.UsageMeteringApiGetCostByOrgRequest = {
  startMonth: new Date(new Date().getTime() + -3 * 86400 * 1000),
};

apiInstance
  .getCostByOrg(params)
  .then((data: v2.CostByOrgResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ae94b021-7bc7-455c-ba1c-e020d8593c45&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=0d8d2689-303a-4218-8102-5b687e57895f&pt=Usage%20Metering&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusage-metering%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ae94b021-7bc7-455c-ba1c-e020d8593c45&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=0d8d2689-303a-4218-8102-5b687e57895f&pt=Usage%20Metering&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusage-metering%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=8c4dc355-8d8f-4a5c-831f-fd0ae98f2e54&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Usage%20Metering&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusage-metering%2F&r=&lt=18819&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=60740)
