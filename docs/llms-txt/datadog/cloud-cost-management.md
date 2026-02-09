# Source: https://docs.datadoghq.com/api/latest/cloud-cost-management.md

---
title: Cloud Cost Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Cloud Cost Management
---

# Cloud Cost Management

The Cloud Cost Management API allows you to set up, edit, and delete Cloud Cost Management accounts for AWS, Azure, and Google Cloud. You can query your cost data by using the [Metrics endpoint](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products) and the `cloud_cost` data source. For more information, see the [Cloud Cost Management documentation](https://docs.datadoghq.com/cloud_cost_management/).

## List Cloud Cost Management AWS CUR configs{% #list-cloud-cost-management-aws-cur-configs %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/aws_cur_config |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/aws_cur_config |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/aws_cur_config      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/aws_cur_config      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/aws_cur_config     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/aws_cur_config |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config |

### Overview

List the AWS CUR configs. This endpoint requires the `cloud_cost_management_read` permission.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of AWS CUR configs.

| Parent field    | Field                           | Type     | Description                                                                                                             |
| --------------- | ------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
|                 | data [*required*]          | [object] | An AWS CUR config.                                                                                                      |
| data            | attributes [*required*]    | object   | Attributes for An AWS CUR config.                                                                                       |
| attributes      | account_filters                 | object   | The account filtering configuration.                                                                                    |
| account_filters | excluded_accounts               | [string] | The AWS account IDs to be excluded from your billing dataset. This field is used when `include_new_accounts` is `true`. |
| account_filters | include_new_accounts            | boolean  | Whether or not to automatically include new member accounts by default in your billing dataset.                         |
| account_filters | included_accounts               | [string] | The AWS account IDs to be included in your billing dataset. This field is used when `include_new_accounts` is `false`.  |
| attributes      | account_id [*required*]    | string   | The AWS account ID.                                                                                                     |
| attributes      | bucket_name [*required*]   | string   | The AWS bucket name used to store the Cost and Usage Report.                                                            |
| attributes      | bucket_region [*required*] | string   | The region the bucket is located in.                                                                                    |
| attributes      | created_at                      | string   | The timestamp when the AWS CUR config was created.                                                                      |
| attributes      | error_messages                  | [string] | The error messages for the AWS CUR config.                                                                              |
| attributes      | months                          | int32    | **DEPRECATED**: The number of months the report has been backfilled.                                                    |
| attributes      | report_name [*required*]   | string   | The name of the Cost and Usage Report.                                                                                  |
| attributes      | report_prefix [*required*] | string   | The report prefix used for the Cost and Usage Report.                                                                   |
| attributes      | status [*required*]        | string   | The status of the AWS CUR.                                                                                              |
| attributes      | status_updated_at               | string   | The timestamp when the AWS CUR config status was updated.                                                               |
| attributes      | updated_at                      | string   | The timestamp when the AWS CUR config status was updated.                                                               |
| data            | id                              | string   | The ID of the AWS CUR config.                                                                                           |
| data            | type [*required*]          | enum     | Type of AWS CUR config. Allowed enum values: `aws_cur_config`                                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "account_filters": {
          "excluded_accounts": [
            "123456789123",
            "123456789143"
          ],
          "include_new_accounts": true,
          "included_accounts": [
            "123456789123",
            "123456789143"
          ]
        },
        "account_id": "123456789123",
        "bucket_name": "dd-cost-bucket",
        "bucket_region": "us-east-1",
        "created_at": "string",
        "error_messages": [],
        "months": "integer",
        "report_name": "dd-report-name",
        "report_prefix": "dd-report-prefix",
        "status": "active",
        "status_updated_at": "string",
        "updated_at": "string"
      },
      "id": "string",
      "type": "aws_cur_config"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Cloud Cost Management AWS CUR configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_cost_awscur_configs()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List Cloud Cost Management AWS CUR configs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.list_cost_awscur_configs()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List Cloud Cost Management AWS CUR configs returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ListCostAWSCURConfigs(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ListCostAWSCURConfigs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ListCostAWSCURConfigs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List Cloud Cost Management AWS CUR configs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.AwsCURConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      AwsCURConfigsResponse result = apiInstance.listCostAWSCURConfigs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#listCostAWSCURConfigs");
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
// List Cloud Cost Management AWS CUR configs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.list_cost_awscur_configs().await;
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
 * List Cloud Cost Management AWS CUR configs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

apiInstance
  .listCostAWSCURConfigs()
  .then((data: v2.AwsCURConfigsResponse) => {
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

## Create Cloud Cost Management AWS CUR config{% #create-cloud-cost-management-aws-cur-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cost/aws_cur_config |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cost/aws_cur_config |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cost/aws_cur_config      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cost/aws_cur_config      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cost/aws_cur_config     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cost/aws_cur_config |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config |

### Overview

Create a Cloud Cost Management account for an AWS CUR config. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field    | Field                           | Type     | Description                                                                                                             |
| --------------- | ------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
|                 | data [*required*]          | object   | AWS CUR config Post data.                                                                                               |
| data            | attributes                      | object   | Attributes for AWS CUR config Post Request.                                                                             |
| attributes      | account_filters                 | object   | The account filtering configuration.                                                                                    |
| account_filters | excluded_accounts               | [string] | The AWS account IDs to be excluded from your billing dataset. This field is used when `include_new_accounts` is `true`. |
| account_filters | include_new_accounts            | boolean  | Whether or not to automatically include new member accounts by default in your billing dataset.                         |
| account_filters | included_accounts               | [string] | The AWS account IDs to be included in your billing dataset. This field is used when `include_new_accounts` is `false`.  |
| attributes      | account_id [*required*]    | string   | The AWS account ID.                                                                                                     |
| attributes      | bucket_name [*required*]   | string   | The AWS bucket name used to store the Cost and Usage Report.                                                            |
| attributes      | bucket_region                   | string   | The region the bucket is located in.                                                                                    |
| attributes      | months                          | int32    | The month of the report.                                                                                                |
| attributes      | report_name [*required*]   | string   | The name of the Cost and Usage Report.                                                                                  |
| attributes      | report_prefix [*required*] | string   | The report prefix used for the Cost and Usage Report.                                                                   |
| data            | type [*required*]          | enum     | Type of AWS CUR config Post Request. Allowed enum values: `aws_cur_config_post_request`                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_id": "123456789123",
      "bucket_name": "dd-cost-bucket",
      "bucket_region": "us-east-1",
      "report_name": "dd-report-name",
      "report_prefix": "dd-report-prefix"
    },
    "type": "aws_cur_config_post_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `AwsCurConfigResponse` object.

| Parent field    | Field                  | Type     | Description                                                                  |
| --------------- | ---------------------- | -------- | ---------------------------------------------------------------------------- |
|                 | data                   | object   | The definition of `AwsCurConfigResponseData` object.                         |
| data            | attributes             | object   | The definition of `AwsCurConfigResponseDataAttributes` object.               |
| attributes      | account_filters        | object   | The definition of `AwsCurConfigResponseDataAttributesAccountFilters` object. |
| account_filters | excluded_accounts      | [string] | The `account_filters` `excluded_accounts`.                                   |
| account_filters | include_new_accounts   | boolean  | The `account_filters` `include_new_accounts`.                                |
| account_filters | included_accounts      | [string] | The `account_filters` `included_accounts`.                                   |
| attributes      | account_id             | string   | The `attributes` `account_id`.                                               |
| attributes      | bucket_name            | string   | The `attributes` `bucket_name`.                                              |
| attributes      | bucket_region          | string   | The `attributes` `bucket_region`.                                            |
| attributes      | created_at             | string   | The `attributes` `created_at`.                                               |
| attributes      | error_messages         | [string] | The `attributes` `error_messages`.                                           |
| attributes      | months                 | int64    | The `attributes` `months`.                                                   |
| attributes      | report_name            | string   | The `attributes` `report_name`.                                              |
| attributes      | report_prefix          | string   | The `attributes` `report_prefix`.                                            |
| attributes      | status                 | string   | The `attributes` `status`.                                                   |
| attributes      | status_updated_at      | string   | The `attributes` `status_updated_at`.                                        |
| attributes      | updated_at             | string   | The `attributes` `updated_at`.                                               |
| data            | id                     | string   | The `AwsCurConfigResponseData` `id`.                                         |
| data            | type [*required*] | enum     | AWS CUR config resource type. Allowed enum values: `aws_cur_config`          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_filters": {
        "excluded_accounts": [
          "123456789124",
          "123456789125"
        ],
        "include_new_accounts": true
      },
      "account_id": "123456789123",
      "bucket_name": "dd-cost-bucket",
      "bucket_region": "us-east-1",
      "created_at": "2023-01-01T12:00:00.000Z",
      "error_messages": [],
      "months": 36,
      "report_name": "dd-report-name",
      "report_prefix": "dd-report-prefix",
      "status": "active",
      "status_updated_at": "2023-01-01T12:00:00.000Z",
      "updated_at": "2023-01-01T12:00:00.000Z"
    },
    "id": "123456789123",
    "type": "aws_cur_config"
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
Forbidden
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_id": "123456789123",
      "bucket_name": "dd-cost-bucket",
      "bucket_region": "us-east-1",
      "report_name": "dd-report-name",
      "report_prefix": "dd-report-prefix"
    },
    "type": "aws_cur_config_post_request"
  }
}
EOF
                        
##### 

```go
// Create Cloud Cost Management AWS CUR config returns "OK" response

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
	body := datadogV2.AwsCURConfigPostRequest{
		Data: datadogV2.AwsCURConfigPostData{
			Attributes: &datadogV2.AwsCURConfigPostRequestAttributes{
				AccountId:    "123456789123",
				BucketName:   "dd-cost-bucket",
				BucketRegion: datadog.PtrString("us-east-1"),
				ReportName:   "dd-report-name",
				ReportPrefix: "dd-report-prefix",
			},
			Type: datadogV2.AWSCURCONFIGPOSTREQUESTTYPE_AWS_CUR_CONFIG_POST_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.CreateCostAWSCURConfig(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.CreateCostAWSCURConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.CreateCostAWSCURConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create Cloud Cost Management AWS CUR config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.AwsCURConfigPostData;
import com.datadog.api.client.v2.model.AwsCURConfigPostRequest;
import com.datadog.api.client.v2.model.AwsCURConfigPostRequestAttributes;
import com.datadog.api.client.v2.model.AwsCURConfigPostRequestType;
import com.datadog.api.client.v2.model.AwsCurConfigResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    AwsCURConfigPostRequest body =
        new AwsCURConfigPostRequest()
            .data(
                new AwsCURConfigPostData()
                    .attributes(
                        new AwsCURConfigPostRequestAttributes()
                            .accountId("123456789123")
                            .bucketName("dd-cost-bucket")
                            .bucketRegion("us-east-1")
                            .reportName("dd-report-name")
                            .reportPrefix("dd-report-prefix"))
                    .type(AwsCURConfigPostRequestType.AWS_CUR_CONFIG_POST_REQUEST));

    try {
      AwsCurConfigResponse result = apiInstance.createCostAWSCURConfig(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#createCostAWSCURConfig");
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

```python
"""
Create Cloud Cost Management AWS CUR config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.aws_cur_config_post_data import AwsCURConfigPostData
from datadog_api_client.v2.model.aws_cur_config_post_request import AwsCURConfigPostRequest
from datadog_api_client.v2.model.aws_cur_config_post_request_attributes import AwsCURConfigPostRequestAttributes
from datadog_api_client.v2.model.aws_cur_config_post_request_type import AwsCURConfigPostRequestType

body = AwsCURConfigPostRequest(
    data=AwsCURConfigPostData(
        attributes=AwsCURConfigPostRequestAttributes(
            account_id="123456789123",
            bucket_name="dd-cost-bucket",
            bucket_region="us-east-1",
            report_name="dd-report-name",
            report_prefix="dd-report-prefix",
        ),
        type=AwsCURConfigPostRequestType.AWS_CUR_CONFIG_POST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_cost_awscur_config(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create Cloud Cost Management AWS CUR config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::AwsCURConfigPostRequest.new({
  data: DatadogAPIClient::V2::AwsCURConfigPostData.new({
    attributes: DatadogAPIClient::V2::AwsCURConfigPostRequestAttributes.new({
      account_id: "123456789123",
      bucket_name: "dd-cost-bucket",
      bucket_region: "us-east-1",
      report_name: "dd-report-name",
      report_prefix: "dd-report-prefix",
    }),
    type: DatadogAPIClient::V2::AwsCURConfigPostRequestType::AWS_CUR_CONFIG_POST_REQUEST,
  }),
})
p api_instance.create_cost_awscur_config(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create Cloud Cost Management AWS CUR config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::AwsCURConfigPostData;
use datadog_api_client::datadogV2::model::AwsCURConfigPostRequest;
use datadog_api_client::datadogV2::model::AwsCURConfigPostRequestAttributes;
use datadog_api_client::datadogV2::model::AwsCURConfigPostRequestType;

#[tokio::main]
async fn main() {
    let body = AwsCURConfigPostRequest::new(
        AwsCURConfigPostData::new(AwsCURConfigPostRequestType::AWS_CUR_CONFIG_POST_REQUEST)
            .attributes(
                AwsCURConfigPostRequestAttributes::new(
                    "123456789123".to_string(),
                    "dd-cost-bucket".to_string(),
                    "dd-report-name".to_string(),
                    "dd-report-prefix".to_string(),
                )
                .bucket_region("us-east-1".to_string()),
            ),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.create_cost_awscur_config(body).await;
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
 * Create Cloud Cost Management AWS CUR config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiCreateCostAWSCURConfigRequest = {
  body: {
    data: {
      attributes: {
        accountId: "123456789123",
        bucketName: "dd-cost-bucket",
        bucketRegion: "us-east-1",
        reportName: "dd-report-name",
        reportPrefix: "dd-report-prefix",
      },
      type: "aws_cur_config_post_request",
    },
  },
};

apiInstance
  .createCostAWSCURConfig(params)
  .then((data: v2.AwsCurConfigResponse) => {
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

## Update Cloud Cost Management AWS CUR config{% #update-cloud-cost-management-aws-cur-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/cost/aws_cur_config/{cloud_account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/cost/aws_cur_config/{cloud_account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |

### Overview

Update the status (active/archived) and/or account filtering configuration of an AWS CUR config. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description       |
| ---------------------------------- | ------- | ----------------- |
| cloud_account_id [*required*] | integer | Cloud Account id. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field    | Field                        | Type     | Description                                                                                                             |
| --------------- | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
|                 | data [*required*]       | object   | AWS CUR config Patch data.                                                                                              |
| data            | attributes [*required*] | object   | Attributes for AWS CUR config Patch Request.                                                                            |
| attributes      | account_filters              | object   | The account filtering configuration.                                                                                    |
| account_filters | excluded_accounts            | [string] | The AWS account IDs to be excluded from your billing dataset. This field is used when `include_new_accounts` is `true`. |
| account_filters | include_new_accounts         | boolean  | Whether or not to automatically include new member accounts by default in your billing dataset.                         |
| account_filters | included_accounts            | [string] | The AWS account IDs to be included in your billing dataset. This field is used when `include_new_accounts` is `false`.  |
| attributes      | is_enabled                   | boolean  | Whether or not the Cloud Cost Management account is enabled.                                                            |
| data            | type [*required*]       | enum     | Type of AWS CUR config Patch Request. Allowed enum values: `aws_cur_config_patch_request`                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "is_enabled": true
    },
    "type": "aws_cur_config_patch_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of AWS CUR configs.

| Parent field    | Field                           | Type     | Description                                                                                                             |
| --------------- | ------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
|                 | data [*required*]          | [object] | An AWS CUR config.                                                                                                      |
| data            | attributes [*required*]    | object   | Attributes for An AWS CUR config.                                                                                       |
| attributes      | account_filters                 | object   | The account filtering configuration.                                                                                    |
| account_filters | excluded_accounts               | [string] | The AWS account IDs to be excluded from your billing dataset. This field is used when `include_new_accounts` is `true`. |
| account_filters | include_new_accounts            | boolean  | Whether or not to automatically include new member accounts by default in your billing dataset.                         |
| account_filters | included_accounts               | [string] | The AWS account IDs to be included in your billing dataset. This field is used when `include_new_accounts` is `false`.  |
| attributes      | account_id [*required*]    | string   | The AWS account ID.                                                                                                     |
| attributes      | bucket_name [*required*]   | string   | The AWS bucket name used to store the Cost and Usage Report.                                                            |
| attributes      | bucket_region [*required*] | string   | The region the bucket is located in.                                                                                    |
| attributes      | created_at                      | string   | The timestamp when the AWS CUR config was created.                                                                      |
| attributes      | error_messages                  | [string] | The error messages for the AWS CUR config.                                                                              |
| attributes      | months                          | int32    | **DEPRECATED**: The number of months the report has been backfilled.                                                    |
| attributes      | report_name [*required*]   | string   | The name of the Cost and Usage Report.                                                                                  |
| attributes      | report_prefix [*required*] | string   | The report prefix used for the Cost and Usage Report.                                                                   |
| attributes      | status [*required*]        | string   | The status of the AWS CUR.                                                                                              |
| attributes      | status_updated_at               | string   | The timestamp when the AWS CUR config status was updated.                                                               |
| attributes      | updated_at                      | string   | The timestamp when the AWS CUR config status was updated.                                                               |
| data            | id                              | string   | The ID of the AWS CUR config.                                                                                           |
| data            | type [*required*]          | enum     | Type of AWS CUR config. Allowed enum values: `aws_cur_config`                                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "account_filters": {
          "excluded_accounts": [
            "123456789123",
            "123456789143"
          ],
          "include_new_accounts": true,
          "included_accounts": [
            "123456789123",
            "123456789143"
          ]
        },
        "account_id": "123456789123",
        "bucket_name": "dd-cost-bucket",
        "bucket_region": "us-east-1",
        "created_at": "string",
        "error_messages": [],
        "months": "integer",
        "report_name": "dd-report-name",
        "report_prefix": "dd-report-prefix",
        "status": "active",
        "status_updated_at": "string",
        "updated_at": "string"
      },
      "id": "string",
      "type": "aws_cur_config"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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

### Code Example

##### 
                          \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config/${cloud_account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "is_enabled": true
    },
    "type": "aws_cur_config_patch_request"
  }
}
EOF
                        
##### 

```go
// Update Cloud Cost Management AWS CUR config returns "OK" response

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
	body := datadogV2.AwsCURConfigPatchRequest{
		Data: datadogV2.AwsCURConfigPatchData{
			Attributes: datadogV2.AwsCURConfigPatchRequestAttributes{
				IsEnabled: datadog.PtrBool(true),
			},
			Type: datadogV2.AWSCURCONFIGPATCHREQUESTTYPE_AWS_CUR_CONFIG_PATCH_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.UpdateCostAWSCURConfig(ctx, 100, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.UpdateCostAWSCURConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.UpdateCostAWSCURConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update Cloud Cost Management AWS CUR config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.AwsCURConfigPatchData;
import com.datadog.api.client.v2.model.AwsCURConfigPatchRequest;
import com.datadog.api.client.v2.model.AwsCURConfigPatchRequestAttributes;
import com.datadog.api.client.v2.model.AwsCURConfigPatchRequestType;
import com.datadog.api.client.v2.model.AwsCURConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    AwsCURConfigPatchRequest body =
        new AwsCURConfigPatchRequest()
            .data(
                new AwsCURConfigPatchData()
                    .attributes(new AwsCURConfigPatchRequestAttributes().isEnabled(true))
                    .type(AwsCURConfigPatchRequestType.AWS_CUR_CONFIG_PATCH_REQUEST));

    try {
      AwsCURConfigsResponse result = apiInstance.updateCostAWSCURConfig(100L, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#updateCostAWSCURConfig");
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

```python
"""
Update Cloud Cost Management AWS CUR config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.aws_cur_config_patch_data import AwsCURConfigPatchData
from datadog_api_client.v2.model.aws_cur_config_patch_request import AwsCURConfigPatchRequest
from datadog_api_client.v2.model.aws_cur_config_patch_request_attributes import AwsCURConfigPatchRequestAttributes
from datadog_api_client.v2.model.aws_cur_config_patch_request_type import AwsCURConfigPatchRequestType

body = AwsCURConfigPatchRequest(
    data=AwsCURConfigPatchData(
        attributes=AwsCURConfigPatchRequestAttributes(
            is_enabled=True,
        ),
        type=AwsCURConfigPatchRequestType.AWS_CUR_CONFIG_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_awscur_config(cloud_account_id=100, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update Cloud Cost Management AWS CUR config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::AwsCURConfigPatchRequest.new({
  data: DatadogAPIClient::V2::AwsCURConfigPatchData.new({
    attributes: DatadogAPIClient::V2::AwsCURConfigPatchRequestAttributes.new({
      is_enabled: true,
    }),
    type: DatadogAPIClient::V2::AwsCURConfigPatchRequestType::AWS_CUR_CONFIG_PATCH_REQUEST,
  }),
})
p api_instance.update_cost_awscur_config(100, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update Cloud Cost Management AWS CUR config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::AwsCURConfigPatchData;
use datadog_api_client::datadogV2::model::AwsCURConfigPatchRequest;
use datadog_api_client::datadogV2::model::AwsCURConfigPatchRequestAttributes;
use datadog_api_client::datadogV2::model::AwsCURConfigPatchRequestType;

#[tokio::main]
async fn main() {
    let body = AwsCURConfigPatchRequest::new(AwsCURConfigPatchData::new(
        AwsCURConfigPatchRequestAttributes::new().is_enabled(true),
        AwsCURConfigPatchRequestType::AWS_CUR_CONFIG_PATCH_REQUEST,
    ));
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.update_cost_awscur_config(100, body).await;
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
 * Update Cloud Cost Management AWS CUR config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiUpdateCostAWSCURConfigRequest = {
  body: {
    data: {
      attributes: {
        isEnabled: true,
      },
      type: "aws_cur_config_patch_request",
    },
  },
  cloudAccountId: 100,
};

apiInstance
  .updateCostAWSCURConfig(params)
  .then((data: v2.AwsCURConfigsResponse) => {
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

## Delete Cloud Cost Management AWS CUR config{% #delete-cloud-cost-management-aws-cur-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cost/aws_cur_config/{cloud_account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cost/aws_cur_config/{cloud_account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |

### Overview

Archive a Cloud Cost Management Account. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description       |
| ---------------------------------- | ------- | ----------------- |
| cloud_account_id [*required*] | integer | Cloud Account id. |

### Response

{% tab title="204" %}
No Content
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

### Code Example

##### 
                  \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config/${cloud_account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Cloud Cost Management AWS CUR config returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_cost_awscur_config(
        cloud_account_id=100,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete Cloud Cost Management AWS CUR config returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
api_instance.delete_cost_awscur_config(100)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete Cloud Cost Management AWS CUR config returns "No Content" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.DeleteCostAWSCURConfig(ctx, 100)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.DeleteCostAWSCURConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete Cloud Cost Management AWS CUR config returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      apiInstance.deleteCostAWSCURConfig(100L);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#deleteCostAWSCURConfig");
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
// Delete Cloud Cost Management AWS CUR config returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.delete_cost_awscur_config(100).await;
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
 * Delete Cloud Cost Management AWS CUR config returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiDeleteCostAWSCURConfigRequest = {
  cloudAccountId: 100,
};

apiInstance
  .deleteCostAWSCURConfig(params)
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

## Get cost AWS CUR config{% #get-cost-aws-cur-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/aws_cur_config/{cloud_account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/aws_cur_config/{cloud_account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config/{cloud_account_id} |

### Overview

Get a specific AWS CUR config.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description                                |
| ---------------------------------- | ------- | ------------------------------------------ |
| cloud_account_id [*required*] | integer | The unique identifier of the cloud account |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `AwsCurConfigResponse` object.

| Parent field    | Field                  | Type     | Description                                                                  |
| --------------- | ---------------------- | -------- | ---------------------------------------------------------------------------- |
|                 | data                   | object   | The definition of `AwsCurConfigResponseData` object.                         |
| data            | attributes             | object   | The definition of `AwsCurConfigResponseDataAttributes` object.               |
| attributes      | account_filters        | object   | The definition of `AwsCurConfigResponseDataAttributesAccountFilters` object. |
| account_filters | excluded_accounts      | [string] | The `account_filters` `excluded_accounts`.                                   |
| account_filters | include_new_accounts   | boolean  | The `account_filters` `include_new_accounts`.                                |
| account_filters | included_accounts      | [string] | The `account_filters` `included_accounts`.                                   |
| attributes      | account_id             | string   | The `attributes` `account_id`.                                               |
| attributes      | bucket_name            | string   | The `attributes` `bucket_name`.                                              |
| attributes      | bucket_region          | string   | The `attributes` `bucket_region`.                                            |
| attributes      | created_at             | string   | The `attributes` `created_at`.                                               |
| attributes      | error_messages         | [string] | The `attributes` `error_messages`.                                           |
| attributes      | months                 | int64    | The `attributes` `months`.                                                   |
| attributes      | report_name            | string   | The `attributes` `report_name`.                                              |
| attributes      | report_prefix          | string   | The `attributes` `report_prefix`.                                            |
| attributes      | status                 | string   | The `attributes` `status`.                                                   |
| attributes      | status_updated_at      | string   | The `attributes` `status_updated_at`.                                        |
| attributes      | updated_at             | string   | The `attributes` `updated_at`.                                               |
| data            | id                     | string   | The `AwsCurConfigResponseData` `id`.                                         |
| data            | type [*required*] | enum     | AWS CUR config resource type. Allowed enum values: `aws_cur_config`          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_filters": {
        "excluded_accounts": [
          "123456789124",
          "123456789125"
        ],
        "include_new_accounts": true
      },
      "account_id": "123456789123",
      "bucket_name": "dd-cost-bucket",
      "bucket_region": "us-east-1",
      "created_at": "2023-01-01T12:00:00.000Z",
      "error_messages": [],
      "months": 36,
      "report_name": "dd-report-name",
      "report_prefix": "dd-report-prefix",
      "status": "active",
      "status_updated_at": "2023-01-01T12:00:00.000Z",
      "updated_at": "2023-01-01T12:00:00.000Z"
    },
    "id": "123456789123",
    "type": "aws_cur_config"
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
                  \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/aws_cur_config/${cloud_account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get cost AWS CUR config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_cost_awscur_config(
        cloud_account_id=123456,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get cost AWS CUR config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.get_cost_awscur_config(123456)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get cost AWS CUR config returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.GetCostAWSCURConfig(ctx, 123456)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.GetCostAWSCURConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.GetCostAWSCURConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get cost AWS CUR config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.AwsCurConfigResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      AwsCurConfigResponse result = apiInstance.getCostAWSCURConfig(123456L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#getCostAWSCURConfig");
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
// Get cost AWS CUR config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.get_cost_awscur_config(123456).await;
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
 * Get cost AWS CUR config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiGetCostAWSCURConfigRequest = {
  cloudAccountId: 123456,
};

apiInstance
  .getCostAWSCURConfig(params)
  .then((data: v2.AwsCurConfigResponse) => {
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

## List Cloud Cost Management Azure configs{% #list-cloud-cost-management-azure-configs %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/azure_uc_config |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/azure_uc_config |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/azure_uc_config      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/azure_uc_config      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/azure_uc_config     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/azure_uc_config |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config |

### Overview

List the Azure configs. This endpoint requires the `cloud_cost_management_read` permission.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of Azure accounts with configs.

| Parent field | Field                               | Type     | Description                                                          |
| ------------ | ----------------------------------- | -------- | -------------------------------------------------------------------- |
|              | data [*required*]              | [object] | An Azure config pair.                                                |
| data         | attributes [*required*]        | object   | Attributes for Azure config pair.                                    |
| attributes   | configs [*required*]           | [object] | An Azure config.                                                     |
| configs      | account_id [*required*]        | string   | The tenant ID of the Azure account.                                  |
| configs      | client_id [*required*]         | string   | The client ID of the Azure account.                                  |
| configs      | created_at                          | string   | The timestamp when the Azure config was created.                     |
| configs      | dataset_type [*required*]      | string   | The dataset type of the Azure config.                                |
| configs      | error_messages                      | [string] | The error messages for the Azure config.                             |
| configs      | export_name [*required*]       | string   | The name of the configured Azure Export.                             |
| configs      | export_path [*required*]       | string   | The path where the Azure Export is saved.                            |
| configs      | id                                  | string   | The ID of the Azure config.                                          |
| configs      | months                              | int32    | **DEPRECATED**: The number of months the report has been backfilled. |
| configs      | scope [*required*]             | string   | The scope of your observed subscription.                             |
| configs      | status [*required*]            | string   | The status of the Azure config.                                      |
| configs      | status_updated_at                   | string   | The timestamp when the Azure config status was last updated.         |
| configs      | storage_account [*required*]   | string   | The name of the storage account where the Azure Export is saved.     |
| configs      | storage_container [*required*] | string   | The name of the storage container where the Azure Export is saved.   |
| configs      | updated_at                          | string   | The timestamp when the Azure config was last updated.                |
| attributes   | id                                  | string   | The ID of the Azure config pair.                                     |
| data         | id                                  | string   | The ID of Cloud Cost Management account.                             |
| data         | type [*required*]              | enum     | Type of Azure config pair. Allowed enum values: `azure_uc_configs`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "configs": [
          {
            "account_id": "1234abcd-1234-abcd-1234-1234abcd1234",
            "client_id": "1234abcd-1234-abcd-1234-1234abcd1234",
            "created_at": "string",
            "dataset_type": "actual",
            "error_messages": [],
            "export_name": "dd-actual-export",
            "export_path": "dd-export-path",
            "id": "string",
            "months": "integer",
            "scope": "/subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
            "status": "active",
            "status_updated_at": "string",
            "storage_account": "dd-storage-account",
            "storage_container": "dd-storage-container",
            "updated_at": "string"
          }
        ],
        "id": "string"
      },
      "id": "string",
      "type": "azure_uc_configs"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Cloud Cost Management Azure configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_cost_azure_uc_configs()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List Cloud Cost Management Azure configs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.list_cost_azure_uc_configs()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List Cloud Cost Management Azure configs returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ListCostAzureUCConfigs(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ListCostAzureUCConfigs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ListCostAzureUCConfigs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List Cloud Cost Management Azure configs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.AzureUCConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      AzureUCConfigsResponse result = apiInstance.listCostAzureUCConfigs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#listCostAzureUCConfigs");
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
// List Cloud Cost Management Azure configs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.list_cost_azure_uc_configs().await;
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
 * List Cloud Cost Management Azure configs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

apiInstance
  .listCostAzureUCConfigs()
  .then((data: v2.AzureUCConfigsResponse) => {
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

## Create Cloud Cost Management Azure configs{% #create-cloud-cost-management-azure-configs %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cost/azure_uc_config |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cost/azure_uc_config |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cost/azure_uc_config      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cost/azure_uc_config      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cost/azure_uc_config     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cost/azure_uc_config |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config |

### Overview

Create a Cloud Cost Management account for an Azure config. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field          | Field                                   | Type   | Description                                                                            |
| --------------------- | --------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
|                       | data [*required*]                  | object | Azure config Post data.                                                                |
| data                  | attributes                              | object | Attributes for Azure config Post Request.                                              |
| attributes            | account_id [*required*]            | string | The tenant ID of the Azure account.                                                    |
| attributes            | actual_bill_config [*required*]    | object | Bill config.                                                                           |
| actual_bill_config    | export_name [*required*]           | string | The name of the configured Azure Export.                                               |
| actual_bill_config    | export_path [*required*]           | string | The path where the Azure Export is saved.                                              |
| actual_bill_config    | storage_account [*required*]       | string | The name of the storage account where the Azure Export is saved.                       |
| actual_bill_config    | storage_container [*required*]     | string | The name of the storage container where the Azure Export is saved.                     |
| attributes            | amortized_bill_config [*required*] | object | Bill config.                                                                           |
| amortized_bill_config | export_name [*required*]           | string | The name of the configured Azure Export.                                               |
| amortized_bill_config | export_path [*required*]           | string | The path where the Azure Export is saved.                                              |
| amortized_bill_config | storage_account [*required*]       | string | The name of the storage account where the Azure Export is saved.                       |
| amortized_bill_config | storage_container [*required*]     | string | The name of the storage container where the Azure Export is saved.                     |
| attributes            | client_id [*required*]             | string | The client ID of the Azure account.                                                    |
| attributes            | scope [*required*]                 | string | The scope of your observed subscription.                                               |
| data                  | type [*required*]                  | enum   | Type of Azure config Post Request. Allowed enum values: `azure_uc_config_post_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_id": "1234abcd-1234-abcd-1234-1234abcd1234",
      "actual_bill_config": {
        "export_name": "dd-actual-export",
        "export_path": "dd-export-path",
        "storage_account": "dd-storage-account",
        "storage_container": "dd-storage-container"
      },
      "amortized_bill_config": {
        "export_name": "dd-actual-export",
        "export_path": "dd-export-path",
        "storage_account": "dd-storage-account",
        "storage_container": "dd-storage-container"
      },
      "client_id": "1234abcd-1234-abcd-1234-1234abcd1234",
      "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"
    },
    "type": "azure_uc_config_post_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of Azure config pair.

| Parent field | Field                               | Type     | Description                                                          |
| ------------ | ----------------------------------- | -------- | -------------------------------------------------------------------- |
|              | data                                | object   | Azure config pair.                                                   |
| data         | attributes [*required*]        | object   | Attributes for Azure config pair.                                    |
| attributes   | configs [*required*]           | [object] | An Azure config.                                                     |
| configs      | account_id [*required*]        | string   | The tenant ID of the Azure account.                                  |
| configs      | client_id [*required*]         | string   | The client ID of the Azure account.                                  |
| configs      | created_at                          | string   | The timestamp when the Azure config was created.                     |
| configs      | dataset_type [*required*]      | string   | The dataset type of the Azure config.                                |
| configs      | error_messages                      | [string] | The error messages for the Azure config.                             |
| configs      | export_name [*required*]       | string   | The name of the configured Azure Export.                             |
| configs      | export_path [*required*]       | string   | The path where the Azure Export is saved.                            |
| configs      | id                                  | string   | The ID of the Azure config.                                          |
| configs      | months                              | int32    | **DEPRECATED**: The number of months the report has been backfilled. |
| configs      | scope [*required*]             | string   | The scope of your observed subscription.                             |
| configs      | status [*required*]            | string   | The status of the Azure config.                                      |
| configs      | status_updated_at                   | string   | The timestamp when the Azure config status was last updated.         |
| configs      | storage_account [*required*]   | string   | The name of the storage account where the Azure Export is saved.     |
| configs      | storage_container [*required*] | string   | The name of the storage container where the Azure Export is saved.   |
| configs      | updated_at                          | string   | The timestamp when the Azure config was last updated.                |
| attributes   | id                                  | string   | The ID of the Azure config pair.                                     |
| data         | id                                  | string   | The ID of Cloud Cost Management account.                             |
| data         | type [*required*]              | enum     | Type of Azure config pair. Allowed enum values: `azure_uc_configs`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "configs": [
        {
          "account_id": "1234abcd-1234-abcd-1234-1234abcd1234",
          "client_id": "1234abcd-1234-abcd-1234-1234abcd1234",
          "created_at": "string",
          "dataset_type": "actual",
          "error_messages": [],
          "export_name": "dd-actual-export",
          "export_path": "dd-export-path",
          "id": "string",
          "months": "integer",
          "scope": "/subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
          "status": "active",
          "status_updated_at": "string",
          "storage_account": "dd-storage-account",
          "storage_container": "dd-storage-container",
          "updated_at": "string"
        }
      ],
      "id": "string"
    },
    "id": "string",
    "type": "azure_uc_configs"
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
Forbidden
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_id": "1234abcd-1234-abcd-1234-1234abcd1234",
      "actual_bill_config": {
        "export_name": "dd-actual-export",
        "export_path": "dd-export-path",
        "storage_account": "dd-storage-account",
        "storage_container": "dd-storage-container"
      },
      "amortized_bill_config": {
        "export_name": "dd-actual-export",
        "export_path": "dd-export-path",
        "storage_account": "dd-storage-account",
        "storage_container": "dd-storage-container"
      },
      "client_id": "1234abcd-1234-abcd-1234-1234abcd1234",
      "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"
    },
    "type": "azure_uc_config_post_request"
  }
}
EOF
                        
##### 

```go
// Create Cloud Cost Management Azure configs returns "OK" response

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
	body := datadogV2.AzureUCConfigPostRequest{
		Data: datadogV2.AzureUCConfigPostData{
			Attributes: &datadogV2.AzureUCConfigPostRequestAttributes{
				AccountId: "1234abcd-1234-abcd-1234-1234abcd1234",
				ActualBillConfig: datadogV2.BillConfig{
					ExportName:       "dd-actual-export",
					ExportPath:       "dd-export-path",
					StorageAccount:   "dd-storage-account",
					StorageContainer: "dd-storage-container",
				},
				AmortizedBillConfig: datadogV2.BillConfig{
					ExportName:       "dd-actual-export",
					ExportPath:       "dd-export-path",
					StorageAccount:   "dd-storage-account",
					StorageContainer: "dd-storage-container",
				},
				ClientId: "1234abcd-1234-abcd-1234-1234abcd1234",
				Scope:    "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
			},
			Type: datadogV2.AZUREUCCONFIGPOSTREQUESTTYPE_AZURE_UC_CONFIG_POST_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.CreateCostAzureUCConfigs(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.CreateCostAzureUCConfigs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.CreateCostAzureUCConfigs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create Cloud Cost Management Azure configs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.AzureUCConfigPairsResponse;
import com.datadog.api.client.v2.model.AzureUCConfigPostData;
import com.datadog.api.client.v2.model.AzureUCConfigPostRequest;
import com.datadog.api.client.v2.model.AzureUCConfigPostRequestAttributes;
import com.datadog.api.client.v2.model.AzureUCConfigPostRequestType;
import com.datadog.api.client.v2.model.BillConfig;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    AzureUCConfigPostRequest body =
        new AzureUCConfigPostRequest()
            .data(
                new AzureUCConfigPostData()
                    .attributes(
                        new AzureUCConfigPostRequestAttributes()
                            .accountId("1234abcd-1234-abcd-1234-1234abcd1234")
                            .actualBillConfig(
                                new BillConfig()
                                    .exportName("dd-actual-export")
                                    .exportPath("dd-export-path")
                                    .storageAccount("dd-storage-account")
                                    .storageContainer("dd-storage-container"))
                            .amortizedBillConfig(
                                new BillConfig()
                                    .exportName("dd-actual-export")
                                    .exportPath("dd-export-path")
                                    .storageAccount("dd-storage-account")
                                    .storageContainer("dd-storage-container"))
                            .clientId("1234abcd-1234-abcd-1234-1234abcd1234")
                            .scope("subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"))
                    .type(AzureUCConfigPostRequestType.AZURE_UC_CONFIG_POST_REQUEST));

    try {
      AzureUCConfigPairsResponse result = apiInstance.createCostAzureUCConfigs(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#createCostAzureUCConfigs");
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

```python
"""
Create Cloud Cost Management Azure configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.azure_uc_config_post_data import AzureUCConfigPostData
from datadog_api_client.v2.model.azure_uc_config_post_request import AzureUCConfigPostRequest
from datadog_api_client.v2.model.azure_uc_config_post_request_attributes import AzureUCConfigPostRequestAttributes
from datadog_api_client.v2.model.azure_uc_config_post_request_type import AzureUCConfigPostRequestType
from datadog_api_client.v2.model.bill_config import BillConfig

body = AzureUCConfigPostRequest(
    data=AzureUCConfigPostData(
        attributes=AzureUCConfigPostRequestAttributes(
            account_id="1234abcd-1234-abcd-1234-1234abcd1234",
            actual_bill_config=BillConfig(
                export_name="dd-actual-export",
                export_path="dd-export-path",
                storage_account="dd-storage-account",
                storage_container="dd-storage-container",
            ),
            amortized_bill_config=BillConfig(
                export_name="dd-actual-export",
                export_path="dd-export-path",
                storage_account="dd-storage-account",
                storage_container="dd-storage-container",
            ),
            client_id="1234abcd-1234-abcd-1234-1234abcd1234",
            scope="subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
        ),
        type=AzureUCConfigPostRequestType.AZURE_UC_CONFIG_POST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_cost_azure_uc_configs(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create Cloud Cost Management Azure configs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::AzureUCConfigPostRequest.new({
  data: DatadogAPIClient::V2::AzureUCConfigPostData.new({
    attributes: DatadogAPIClient::V2::AzureUCConfigPostRequestAttributes.new({
      account_id: "1234abcd-1234-abcd-1234-1234abcd1234",
      actual_bill_config: DatadogAPIClient::V2::BillConfig.new({
        export_name: "dd-actual-export",
        export_path: "dd-export-path",
        storage_account: "dd-storage-account",
        storage_container: "dd-storage-container",
      }),
      amortized_bill_config: DatadogAPIClient::V2::BillConfig.new({
        export_name: "dd-actual-export",
        export_path: "dd-export-path",
        storage_account: "dd-storage-account",
        storage_container: "dd-storage-container",
      }),
      client_id: "1234abcd-1234-abcd-1234-1234abcd1234",
      scope: "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
    }),
    type: DatadogAPIClient::V2::AzureUCConfigPostRequestType::AZURE_UC_CONFIG_POST_REQUEST,
  }),
})
p api_instance.create_cost_azure_uc_configs(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create Cloud Cost Management Azure configs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::AzureUCConfigPostData;
use datadog_api_client::datadogV2::model::AzureUCConfigPostRequest;
use datadog_api_client::datadogV2::model::AzureUCConfigPostRequestAttributes;
use datadog_api_client::datadogV2::model::AzureUCConfigPostRequestType;
use datadog_api_client::datadogV2::model::BillConfig;

#[tokio::main]
async fn main() {
    let body = AzureUCConfigPostRequest::new(
        AzureUCConfigPostData::new(AzureUCConfigPostRequestType::AZURE_UC_CONFIG_POST_REQUEST)
            .attributes(AzureUCConfigPostRequestAttributes::new(
                "1234abcd-1234-abcd-1234-1234abcd1234".to_string(),
                BillConfig::new(
                    "dd-actual-export".to_string(),
                    "dd-export-path".to_string(),
                    "dd-storage-account".to_string(),
                    "dd-storage-container".to_string(),
                ),
                BillConfig::new(
                    "dd-actual-export".to_string(),
                    "dd-export-path".to_string(),
                    "dd-storage-account".to_string(),
                    "dd-storage-container".to_string(),
                ),
                "1234abcd-1234-abcd-1234-1234abcd1234".to_string(),
                "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234".to_string(),
            )),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.create_cost_azure_uc_configs(body).await;
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
 * Create Cloud Cost Management Azure configs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiCreateCostAzureUCConfigsRequest = {
  body: {
    data: {
      attributes: {
        accountId: "1234abcd-1234-abcd-1234-1234abcd1234",
        actualBillConfig: {
          exportName: "dd-actual-export",
          exportPath: "dd-export-path",
          storageAccount: "dd-storage-account",
          storageContainer: "dd-storage-container",
        },
        amortizedBillConfig: {
          exportName: "dd-actual-export",
          exportPath: "dd-export-path",
          storageAccount: "dd-storage-account",
          storageContainer: "dd-storage-container",
        },
        clientId: "1234abcd-1234-abcd-1234-1234abcd1234",
        scope: "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
      },
      type: "azure_uc_config_post_request",
    },
  },
};

apiInstance
  .createCostAzureUCConfigs(params)
  .then((data: v2.AzureUCConfigPairsResponse) => {
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

## Update Cloud Cost Management Azure config{% #update-cloud-cost-management-azure-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/cost/azure_uc_config/{cloud_account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/cost/azure_uc_config/{cloud_account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |

### Overview

Update the status of an Azure config (active/archived). This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description       |
| ---------------------------------- | ------- | ----------------- |
| cloud_account_id [*required*] | integer | Cloud Account id. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                              |
| ------------ | ---------------------------- | ------- | ---------------------------------------------------------------------------------------- |
|              | data [*required*]       | object  | Azure config Patch data.                                                                 |
| data         | attributes                   | object  | Attributes for Azure config Patch Request.                                               |
| attributes   | is_enabled [*required*] | boolean | Whether or not the Cloud Cost Management account is enabled.                             |
| data         | type [*required*]       | enum    | Type of Azure config Patch Request. Allowed enum values: `azure_uc_config_patch_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "is_enabled": true
    },
    "type": "azure_uc_config_patch_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of Azure config pair.

| Parent field | Field                               | Type     | Description                                                          |
| ------------ | ----------------------------------- | -------- | -------------------------------------------------------------------- |
|              | data                                | object   | Azure config pair.                                                   |
| data         | attributes [*required*]        | object   | Attributes for Azure config pair.                                    |
| attributes   | configs [*required*]           | [object] | An Azure config.                                                     |
| configs      | account_id [*required*]        | string   | The tenant ID of the Azure account.                                  |
| configs      | client_id [*required*]         | string   | The client ID of the Azure account.                                  |
| configs      | created_at                          | string   | The timestamp when the Azure config was created.                     |
| configs      | dataset_type [*required*]      | string   | The dataset type of the Azure config.                                |
| configs      | error_messages                      | [string] | The error messages for the Azure config.                             |
| configs      | export_name [*required*]       | string   | The name of the configured Azure Export.                             |
| configs      | export_path [*required*]       | string   | The path where the Azure Export is saved.                            |
| configs      | id                                  | string   | The ID of the Azure config.                                          |
| configs      | months                              | int32    | **DEPRECATED**: The number of months the report has been backfilled. |
| configs      | scope [*required*]             | string   | The scope of your observed subscription.                             |
| configs      | status [*required*]            | string   | The status of the Azure config.                                      |
| configs      | status_updated_at                   | string   | The timestamp when the Azure config status was last updated.         |
| configs      | storage_account [*required*]   | string   | The name of the storage account where the Azure Export is saved.     |
| configs      | storage_container [*required*] | string   | The name of the storage container where the Azure Export is saved.   |
| configs      | updated_at                          | string   | The timestamp when the Azure config was last updated.                |
| attributes   | id                                  | string   | The ID of the Azure config pair.                                     |
| data         | id                                  | string   | The ID of Cloud Cost Management account.                             |
| data         | type [*required*]              | enum     | Type of Azure config pair. Allowed enum values: `azure_uc_configs`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "configs": [
        {
          "account_id": "1234abcd-1234-abcd-1234-1234abcd1234",
          "client_id": "1234abcd-1234-abcd-1234-1234abcd1234",
          "created_at": "string",
          "dataset_type": "actual",
          "error_messages": [],
          "export_name": "dd-actual-export",
          "export_path": "dd-export-path",
          "id": "string",
          "months": "integer",
          "scope": "/subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
          "status": "active",
          "status_updated_at": "string",
          "storage_account": "dd-storage-account",
          "storage_container": "dd-storage-container",
          "updated_at": "string"
        }
      ],
      "id": "string"
    },
    "id": "string",
    "type": "azure_uc_configs"
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
Forbidden
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

### Code Example

##### 
                          \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config/${cloud_account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "is_enabled": true
    },
    "type": "azure_uc_config_patch_request"
  }
}
EOF
                        
##### 

```go
// Update Cloud Cost Management Azure config returns "OK" response

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
	body := datadogV2.AzureUCConfigPatchRequest{
		Data: datadogV2.AzureUCConfigPatchData{
			Attributes: &datadogV2.AzureUCConfigPatchRequestAttributes{
				IsEnabled: true,
			},
			Type: datadogV2.AZUREUCCONFIGPATCHREQUESTTYPE_AZURE_UC_CONFIG_PATCH_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.UpdateCostAzureUCConfigs(ctx, 100, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.UpdateCostAzureUCConfigs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.UpdateCostAzureUCConfigs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update Cloud Cost Management Azure config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.AzureUCConfigPairsResponse;
import com.datadog.api.client.v2.model.AzureUCConfigPatchData;
import com.datadog.api.client.v2.model.AzureUCConfigPatchRequest;
import com.datadog.api.client.v2.model.AzureUCConfigPatchRequestAttributes;
import com.datadog.api.client.v2.model.AzureUCConfigPatchRequestType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    AzureUCConfigPatchRequest body =
        new AzureUCConfigPatchRequest()
            .data(
                new AzureUCConfigPatchData()
                    .attributes(new AzureUCConfigPatchRequestAttributes().isEnabled(true))
                    .type(AzureUCConfigPatchRequestType.AZURE_UC_CONFIG_PATCH_REQUEST));

    try {
      AzureUCConfigPairsResponse result = apiInstance.updateCostAzureUCConfigs(100L, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#updateCostAzureUCConfigs");
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

```python
"""
Update Cloud Cost Management Azure config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.azure_uc_config_patch_data import AzureUCConfigPatchData
from datadog_api_client.v2.model.azure_uc_config_patch_request import AzureUCConfigPatchRequest
from datadog_api_client.v2.model.azure_uc_config_patch_request_attributes import AzureUCConfigPatchRequestAttributes
from datadog_api_client.v2.model.azure_uc_config_patch_request_type import AzureUCConfigPatchRequestType

body = AzureUCConfigPatchRequest(
    data=AzureUCConfigPatchData(
        attributes=AzureUCConfigPatchRequestAttributes(
            is_enabled=True,
        ),
        type=AzureUCConfigPatchRequestType.AZURE_UC_CONFIG_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_azure_uc_configs(cloud_account_id=100, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update Cloud Cost Management Azure config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::AzureUCConfigPatchRequest.new({
  data: DatadogAPIClient::V2::AzureUCConfigPatchData.new({
    attributes: DatadogAPIClient::V2::AzureUCConfigPatchRequestAttributes.new({
      is_enabled: true,
    }),
    type: DatadogAPIClient::V2::AzureUCConfigPatchRequestType::AZURE_UC_CONFIG_PATCH_REQUEST,
  }),
})
p api_instance.update_cost_azure_uc_configs(100, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update Cloud Cost Management Azure config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::AzureUCConfigPatchData;
use datadog_api_client::datadogV2::model::AzureUCConfigPatchRequest;
use datadog_api_client::datadogV2::model::AzureUCConfigPatchRequestAttributes;
use datadog_api_client::datadogV2::model::AzureUCConfigPatchRequestType;

#[tokio::main]
async fn main() {
    let body = AzureUCConfigPatchRequest::new(
        AzureUCConfigPatchData::new(AzureUCConfigPatchRequestType::AZURE_UC_CONFIG_PATCH_REQUEST)
            .attributes(AzureUCConfigPatchRequestAttributes::new(true)),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.update_cost_azure_uc_configs(100, body).await;
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
 * Update Cloud Cost Management Azure config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiUpdateCostAzureUCConfigsRequest = {
  body: {
    data: {
      attributes: {
        isEnabled: true,
      },
      type: "azure_uc_config_patch_request",
    },
  },
  cloudAccountId: 100,
};

apiInstance
  .updateCostAzureUCConfigs(params)
  .then((data: v2.AzureUCConfigPairsResponse) => {
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

## Delete Cloud Cost Management Azure config{% #delete-cloud-cost-management-azure-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cost/azure_uc_config/{cloud_account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cost/azure_uc_config/{cloud_account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |

### Overview

Archive a Cloud Cost Management Account. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description       |
| ---------------------------------- | ------- | ----------------- |
| cloud_account_id [*required*] | integer | Cloud Account id. |

### Response

{% tab title="204" %}
No Content
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

### Code Example

##### 
                  \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config/${cloud_account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Cloud Cost Management Azure config returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_cost_azure_uc_config(
        cloud_account_id=100,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete Cloud Cost Management Azure config returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
api_instance.delete_cost_azure_uc_config(100)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete Cloud Cost Management Azure config returns "No Content" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.DeleteCostAzureUCConfig(ctx, 100)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.DeleteCostAzureUCConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete Cloud Cost Management Azure config returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      apiInstance.deleteCostAzureUCConfig(100L);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#deleteCostAzureUCConfig");
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
// Delete Cloud Cost Management Azure config returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.delete_cost_azure_uc_config(100).await;
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
 * Delete Cloud Cost Management Azure config returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiDeleteCostAzureUCConfigRequest = {
  cloudAccountId: 100,
};

apiInstance
  .deleteCostAzureUCConfig(params)
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

## Get cost Azure UC config{% #get-cost-azure-uc-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/azure_uc_config/{cloud_account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/azure_uc_config/{cloud_account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config/{cloud_account_id} |

### Overview

Get a specific Azure config.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description                                |
| ---------------------------------- | ------- | ------------------------------------------ |
| cloud_account_id [*required*] | integer | The unique identifier of the cloud account |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `UCConfigPair` object.

| Parent field | Field                  | Type     | Description                                                             |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------- |
|              | data                   | object   | The definition of `UCConfigPairData` object.                            |
| data         | attributes             | object   | The definition of `UCConfigPairDataAttributes` object.                  |
| attributes   | configs                | [object] | The `attributes` `configs`.                                             |
| configs      | account_id             | string   | The `items` `account_id`.                                               |
| configs      | client_id              | string   | The `items` `client_id`.                                                |
| configs      | created_at             | string   | The `items` `created_at`.                                               |
| configs      | dataset_type           | string   | The `items` `dataset_type`.                                             |
| configs      | error_messages         | [string] | The `items` `error_messages`.                                           |
| configs      | export_name            | string   | The `items` `export_name`.                                              |
| configs      | export_path            | string   | The `items` `export_path`.                                              |
| configs      | id                     | string   | The `items` `id`.                                                       |
| configs      | months                 | int64    | The `items` `months`.                                                   |
| configs      | scope                  | string   | The `items` `scope`.                                                    |
| configs      | status                 | string   | The `items` `status`.                                                   |
| configs      | status_updated_at      | string   | The `items` `status_updated_at`.                                        |
| configs      | storage_account        | string   | The `items` `storage_account`.                                          |
| configs      | storage_container      | string   | The `items` `storage_container`.                                        |
| configs      | updated_at             | string   | The `items` `updated_at`.                                               |
| data         | id                     | string   | The `UCConfigPairData` `id`.                                            |
| data         | type [*required*] | enum     | Azure UC configs resource type. Allowed enum values: `azure_uc_configs` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "configs": [
        {
          "account_id": "1234abcd-1234-abcd-1234-1234abcd1234",
          "client_id": "1234abcd-1234-abcd-1234-1234abcd1234",
          "created_at": "2023-01-01T12:00:00.000Z",
          "dataset_type": "actual",
          "error_messages": [],
          "export_name": "dd-actual-export",
          "export_path": "dd-export-path",
          "id": "123456789123",
          "months": 36,
          "scope": "/subscriptions/1234abcd-1234-abcd-1234-1234abcd1234",
          "status": "active",
          "status_updated_at": "2023-01-01T12:00:00.000Z",
          "storage_account": "dd-storage-account",
          "storage_container": "dd-storage-container",
          "updated_at": "2023-01-01T12:00:00.000Z"
        }
      ]
    },
    "id": "123456789123",
    "type": "azure_uc_configs"
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
                  \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/azure_uc_config/${cloud_account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get cost Azure UC config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_cost_azure_uc_config(
        cloud_account_id=123456,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get cost Azure UC config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.get_cost_azure_uc_config(123456)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get cost Azure UC config returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.GetCostAzureUCConfig(ctx, 123456)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.GetCostAzureUCConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.GetCostAzureUCConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get cost Azure UC config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.UCConfigPair;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      UCConfigPair result = apiInstance.getCostAzureUCConfig(123456L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#getCostAzureUCConfig");
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
// Get cost Azure UC config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.get_cost_azure_uc_config(123456).await;
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
 * Get cost Azure UC config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiGetCostAzureUCConfigRequest = {
  cloudAccountId: 123456,
};

apiInstance
  .getCostAzureUCConfig(params)
  .then((data: v2.UCConfigPair) => {
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

## List Google Cloud Usage Cost configs{% #list-google-cloud-usage-cost-configs %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/gcp_uc_config |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/gcp_uc_config |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/gcp_uc_config      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/gcp_uc_config      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/gcp_uc_config     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/gcp_uc_config |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config |

### Overview

List the Google Cloud Usage Cost configs. This endpoint requires the `cloud_cost_management_read` permission.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of Google Cloud Usage Cost configs.

| Parent field | Field                                 | Type     | Description                                                                  |
| ------------ | ------------------------------------- | -------- | ---------------------------------------------------------------------------- |
|              | data [*required*]                | [object] | A Google Cloud Usage Cost config.                                            |
| data         | attributes [*required*]          | object   | Attributes for a Google Cloud Usage Cost config.                             |
| attributes   | account_id [*required*]          | string   | The Google Cloud account ID.                                                 |
| attributes   | bucket_name [*required*]         | string   | The Google Cloud bucket name used to store the Usage Cost export.            |
| attributes   | created_at                            | string   | The timestamp when the Google Cloud Usage Cost config was created.           |
| attributes   | dataset [*required*]             | string   | The export dataset name used for the Google Cloud Usage Cost Report.         |
| attributes   | error_messages                        | [string] | The error messages for the Google Cloud Usage Cost config.                   |
| attributes   | export_prefix [*required*]       | string   | The export prefix used for the Google Cloud Usage Cost Report.               |
| attributes   | export_project_name [*required*] | string   | The name of the Google Cloud Usage Cost Report.                              |
| attributes   | months                                | int32    | **DEPRECATED**: The number of months the report has been backfilled.         |
| attributes   | project_id                            | string   | The `project_id` of the Google Cloud Usage Cost report.                      |
| attributes   | service_account [*required*]     | string   | The unique Google Cloud service account email.                               |
| attributes   | status [*required*]              | string   | The status of the Google Cloud Usage Cost config.                            |
| attributes   | status_updated_at                     | string   | The timestamp when the Google Cloud Usage Cost config status was updated.    |
| attributes   | updated_at                            | string   | The timestamp when the Google Cloud Usage Cost config status was updated.    |
| data         | id                                    | string   | The ID of the Google Cloud Usage Cost config.                                |
| data         | type [*required*]                | enum     | Type of Google Cloud Usage Cost config. Allowed enum values: `gcp_uc_config` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "account_id": "123456_A123BC_12AB34",
        "bucket_name": "dd-cost-bucket",
        "created_at": "string",
        "dataset": "billing",
        "error_messages": [],
        "export_prefix": "datadog_cloud_cost_usage_export",
        "export_project_name": "dd-cloud-cost-report",
        "months": "integer",
        "project_id": "my-project-123",
        "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
        "status": "active",
        "status_updated_at": "string",
        "updated_at": "string"
      },
      "id": "string",
      "type": "gcp_uc_config"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Google Cloud Usage Cost configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_cost_gcp_usage_cost_configs()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List Google Cloud Usage Cost configs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.list_cost_gcp_usage_cost_configs()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List Google Cloud Usage Cost configs returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ListCostGCPUsageCostConfigs(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ListCostGCPUsageCostConfigs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ListCostGCPUsageCostConfigs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List Google Cloud Usage Cost configs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.GCPUsageCostConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      GCPUsageCostConfigsResponse result = apiInstance.listCostGCPUsageCostConfigs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#listCostGCPUsageCostConfigs");
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
// List Google Cloud Usage Cost configs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.list_cost_gcp_usage_cost_configs().await;
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
 * List Google Cloud Usage Cost configs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

apiInstance
  .listCostGCPUsageCostConfigs()
  .then((data: v2.GCPUsageCostConfigsResponse) => {
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

## Create Google Cloud Usage Cost config{% #create-google-cloud-usage-cost-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cost/gcp_uc_config |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cost/gcp_uc_config |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cost/gcp_uc_config      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cost/gcp_uc_config      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cost/gcp_uc_config     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cost/gcp_uc_config |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config |

### Overview

Create a Cloud Cost Management account for an Google Cloud Usage Cost config. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                                 | Type   | Description                                                                                            |
| ------------ | ------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------ |
|              | data [*required*]                | object | Google Cloud Usage Cost config post data.                                                              |
| data         | attributes                            | object | Attributes for Google Cloud Usage Cost config post request.                                            |
| attributes   | billing_account_id [*required*]  | string | The Google Cloud account ID.                                                                           |
| attributes   | bucket_name [*required*]         | string | The Google Cloud bucket name used to store the Usage Cost export.                                      |
| attributes   | export_dataset_name [*required*] | string | The export dataset name used for the Google Cloud Usage Cost report.                                   |
| attributes   | export_prefix                         | string | The export prefix used for the Google Cloud Usage Cost report.                                         |
| attributes   | export_project_name [*required*] | string | The name of the Google Cloud Usage Cost report.                                                        |
| attributes   | service_account [*required*]     | string | The unique Google Cloud service account email.                                                         |
| data         | type [*required*]                | enum   | Type of Google Cloud Usage Cost config post request. Allowed enum values: `gcp_uc_config_post_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "billing_account_id": "123456_A123BC_12AB34",
      "bucket_name": "dd-cost-bucket",
      "export_dataset_name": "billing",
      "export_prefix": "datadog_cloud_cost_usage_export",
      "export_project_name": "dd-cloud-cost-report",
      "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com"
    },
    "type": "gcp_uc_config_post_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of Google Cloud Usage Cost config.

| Parent field | Field                                 | Type     | Description                                                                  |
| ------------ | ------------------------------------- | -------- | ---------------------------------------------------------------------------- |
|              | data                                  | object   | Google Cloud Usage Cost config.                                              |
| data         | attributes [*required*]          | object   | Attributes for a Google Cloud Usage Cost config.                             |
| attributes   | account_id [*required*]          | string   | The Google Cloud account ID.                                                 |
| attributes   | bucket_name [*required*]         | string   | The Google Cloud bucket name used to store the Usage Cost export.            |
| attributes   | created_at                            | string   | The timestamp when the Google Cloud Usage Cost config was created.           |
| attributes   | dataset [*required*]             | string   | The export dataset name used for the Google Cloud Usage Cost Report.         |
| attributes   | error_messages                        | [string] | The error messages for the Google Cloud Usage Cost config.                   |
| attributes   | export_prefix [*required*]       | string   | The export prefix used for the Google Cloud Usage Cost Report.               |
| attributes   | export_project_name [*required*] | string   | The name of the Google Cloud Usage Cost Report.                              |
| attributes   | months                                | int32    | **DEPRECATED**: The number of months the report has been backfilled.         |
| attributes   | project_id                            | string   | The `project_id` of the Google Cloud Usage Cost report.                      |
| attributes   | service_account [*required*]     | string   | The unique Google Cloud service account email.                               |
| attributes   | status [*required*]              | string   | The status of the Google Cloud Usage Cost config.                            |
| attributes   | status_updated_at                     | string   | The timestamp when the Google Cloud Usage Cost config status was updated.    |
| attributes   | updated_at                            | string   | The timestamp when the Google Cloud Usage Cost config status was updated.    |
| data         | id                                    | string   | The ID of the Google Cloud Usage Cost config.                                |
| data         | type [*required*]                | enum     | Type of Google Cloud Usage Cost config. Allowed enum values: `gcp_uc_config` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_id": "123456_A123BC_12AB34",
      "bucket_name": "dd-cost-bucket",
      "created_at": "string",
      "dataset": "billing",
      "error_messages": [],
      "export_prefix": "datadog_cloud_cost_usage_export",
      "export_project_name": "dd-cloud-cost-report",
      "months": "integer",
      "project_id": "my-project-123",
      "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
      "status": "active",
      "status_updated_at": "string",
      "updated_at": "string"
    },
    "id": "string",
    "type": "gcp_uc_config"
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
Forbidden
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "billing_account_id": "123456_A123BC_12AB34",
      "bucket_name": "dd-cost-bucket",
      "export_dataset_name": "billing",
      "export_prefix": "datadog_cloud_cost_usage_export",
      "export_project_name": "dd-cloud-cost-report",
      "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com"
    },
    "type": "gcp_uc_config_post_request"
  }
}
EOF
                        
##### 

```go
// Create Google Cloud Usage Cost config returns "OK" response

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
	body := datadogV2.GCPUsageCostConfigPostRequest{
		Data: datadogV2.GCPUsageCostConfigPostData{
			Attributes: &datadogV2.GCPUsageCostConfigPostRequestAttributes{
				BillingAccountId:  "123456_A123BC_12AB34",
				BucketName:        "dd-cost-bucket",
				ExportDatasetName: "billing",
				ExportPrefix:      datadog.PtrString("datadog_cloud_cost_usage_export"),
				ExportProjectName: "dd-cloud-cost-report",
				ServiceAccount:    "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
			},
			Type: datadogV2.GCPUSAGECOSTCONFIGPOSTREQUESTTYPE_GCP_USAGE_COST_CONFIG_POST_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.CreateCostGCPUsageCostConfig(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.CreateCostGCPUsageCostConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.CreateCostGCPUsageCostConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create Google Cloud Usage Cost config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPostData;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPostRequest;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPostRequestAttributes;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPostRequestType;
import com.datadog.api.client.v2.model.GCPUsageCostConfigResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    GCPUsageCostConfigPostRequest body =
        new GCPUsageCostConfigPostRequest()
            .data(
                new GCPUsageCostConfigPostData()
                    .attributes(
                        new GCPUsageCostConfigPostRequestAttributes()
                            .billingAccountId("123456_A123BC_12AB34")
                            .bucketName("dd-cost-bucket")
                            .exportDatasetName("billing")
                            .exportPrefix("datadog_cloud_cost_usage_export")
                            .exportProjectName("dd-cloud-cost-report")
                            .serviceAccount(
                                "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com"))
                    .type(GCPUsageCostConfigPostRequestType.GCP_USAGE_COST_CONFIG_POST_REQUEST));

    try {
      GCPUsageCostConfigResponse result = apiInstance.createCostGCPUsageCostConfig(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#createCostGCPUsageCostConfig");
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

```python
"""
Create Google Cloud Usage Cost config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.gcp_usage_cost_config_post_data import GCPUsageCostConfigPostData
from datadog_api_client.v2.model.gcp_usage_cost_config_post_request import GCPUsageCostConfigPostRequest
from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_attributes import (
    GCPUsageCostConfigPostRequestAttributes,
)
from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_type import GCPUsageCostConfigPostRequestType

body = GCPUsageCostConfigPostRequest(
    data=GCPUsageCostConfigPostData(
        attributes=GCPUsageCostConfigPostRequestAttributes(
            billing_account_id="123456_A123BC_12AB34",
            bucket_name="dd-cost-bucket",
            export_dataset_name="billing",
            export_prefix="datadog_cloud_cost_usage_export",
            export_project_name="dd-cloud-cost-report",
            service_account="dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
        ),
        type=GCPUsageCostConfigPostRequestType.GCP_USAGE_COST_CONFIG_POST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_cost_gcp_usage_cost_config(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create Google Cloud Usage Cost config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::GCPUsageCostConfigPostRequest.new({
  data: DatadogAPIClient::V2::GCPUsageCostConfigPostData.new({
    attributes: DatadogAPIClient::V2::GCPUsageCostConfigPostRequestAttributes.new({
      billing_account_id: "123456_A123BC_12AB34",
      bucket_name: "dd-cost-bucket",
      export_dataset_name: "billing",
      export_prefix: "datadog_cloud_cost_usage_export",
      export_project_name: "dd-cloud-cost-report",
      service_account: "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
    }),
    type: DatadogAPIClient::V2::GCPUsageCostConfigPostRequestType::GCP_USAGE_COST_CONFIG_POST_REQUEST,
  }),
})
p api_instance.create_cost_gcp_usage_cost_config(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create Google Cloud Usage Cost config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPostData;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPostRequest;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPostRequestAttributes;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPostRequestType;

#[tokio::main]
async fn main() {
    let body = GCPUsageCostConfigPostRequest::new(
        GCPUsageCostConfigPostData::new(
            GCPUsageCostConfigPostRequestType::GCP_USAGE_COST_CONFIG_POST_REQUEST,
        )
        .attributes(
            GCPUsageCostConfigPostRequestAttributes::new(
                "123456_A123BC_12AB34".to_string(),
                "dd-cost-bucket".to_string(),
                "billing".to_string(),
                "dd-cloud-cost-report".to_string(),
                "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com".to_string(),
            )
            .export_prefix("datadog_cloud_cost_usage_export".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.create_cost_gcp_usage_cost_config(body).await;
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
 * Create Google Cloud Usage Cost config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiCreateCostGCPUsageCostConfigRequest = {
  body: {
    data: {
      attributes: {
        billingAccountId: "123456_A123BC_12AB34",
        bucketName: "dd-cost-bucket",
        exportDatasetName: "billing",
        exportPrefix: "datadog_cloud_cost_usage_export",
        exportProjectName: "dd-cloud-cost-report",
        serviceAccount:
          "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
      },
      type: "gcp_uc_config_post_request",
    },
  },
};

apiInstance
  .createCostGCPUsageCostConfig(params)
  .then((data: v2.GCPUsageCostConfigResponse) => {
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

## Update Google Cloud Usage Cost config{% #update-google-cloud-usage-cost-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/cost/gcp_uc_config/{cloud_account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/cost/gcp_uc_config/{cloud_account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |

### Overview

Update the status of an Google Cloud Usage Cost config (active/archived). This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description       |
| ---------------------------------- | ------- | ----------------- |
| cloud_account_id [*required*] | integer | Cloud Account id. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                                              |
| ------------ | ---------------------------- | ------- | -------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object  | Google Cloud Usage Cost config patch data.                                                               |
| data         | attributes [*required*] | object  | Attributes for Google Cloud Usage Cost config patch request.                                             |
| attributes   | is_enabled [*required*] | boolean | Whether or not the Cloud Cost Management account is enabled.                                             |
| data         | type [*required*]       | enum    | Type of Google Cloud Usage Cost config patch request. Allowed enum values: `gcp_uc_config_patch_request` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "is_enabled": true
    },
    "type": "gcp_uc_config_patch_request"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of Google Cloud Usage Cost config.

| Parent field | Field                                 | Type     | Description                                                                  |
| ------------ | ------------------------------------- | -------- | ---------------------------------------------------------------------------- |
|              | data                                  | object   | Google Cloud Usage Cost config.                                              |
| data         | attributes [*required*]          | object   | Attributes for a Google Cloud Usage Cost config.                             |
| attributes   | account_id [*required*]          | string   | The Google Cloud account ID.                                                 |
| attributes   | bucket_name [*required*]         | string   | The Google Cloud bucket name used to store the Usage Cost export.            |
| attributes   | created_at                            | string   | The timestamp when the Google Cloud Usage Cost config was created.           |
| attributes   | dataset [*required*]             | string   | The export dataset name used for the Google Cloud Usage Cost Report.         |
| attributes   | error_messages                        | [string] | The error messages for the Google Cloud Usage Cost config.                   |
| attributes   | export_prefix [*required*]       | string   | The export prefix used for the Google Cloud Usage Cost Report.               |
| attributes   | export_project_name [*required*] | string   | The name of the Google Cloud Usage Cost Report.                              |
| attributes   | months                                | int32    | **DEPRECATED**: The number of months the report has been backfilled.         |
| attributes   | project_id                            | string   | The `project_id` of the Google Cloud Usage Cost report.                      |
| attributes   | service_account [*required*]     | string   | The unique Google Cloud service account email.                               |
| attributes   | status [*required*]              | string   | The status of the Google Cloud Usage Cost config.                            |
| attributes   | status_updated_at                     | string   | The timestamp when the Google Cloud Usage Cost config status was updated.    |
| attributes   | updated_at                            | string   | The timestamp when the Google Cloud Usage Cost config status was updated.    |
| data         | id                                    | string   | The ID of the Google Cloud Usage Cost config.                                |
| data         | type [*required*]                | enum     | Type of Google Cloud Usage Cost config. Allowed enum values: `gcp_uc_config` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_id": "123456_A123BC_12AB34",
      "bucket_name": "dd-cost-bucket",
      "created_at": "string",
      "dataset": "billing",
      "error_messages": [],
      "export_prefix": "datadog_cloud_cost_usage_export",
      "export_project_name": "dd-cloud-cost-report",
      "months": "integer",
      "project_id": "my-project-123",
      "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
      "status": "active",
      "status_updated_at": "string",
      "updated_at": "string"
    },
    "id": "string",
    "type": "gcp_uc_config"
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
Forbidden
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

### Code Example

##### 
                          \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config/${cloud_account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "is_enabled": true
    },
    "type": "gcp_uc_config_patch_request"
  }
}
EOF
                        
##### 

```go
// Update Google Cloud Usage Cost config returns "OK" response

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
	body := datadogV2.GCPUsageCostConfigPatchRequest{
		Data: datadogV2.GCPUsageCostConfigPatchData{
			Attributes: datadogV2.GCPUsageCostConfigPatchRequestAttributes{
				IsEnabled: true,
			},
			Type: datadogV2.GCPUSAGECOSTCONFIGPATCHREQUESTTYPE_GCP_USAGE_COST_CONFIG_PATCH_REQUEST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.UpdateCostGCPUsageCostConfig(ctx, 100, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.UpdateCostGCPUsageCostConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.UpdateCostGCPUsageCostConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update Google Cloud Usage Cost config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPatchData;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPatchRequest;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPatchRequestAttributes;
import com.datadog.api.client.v2.model.GCPUsageCostConfigPatchRequestType;
import com.datadog.api.client.v2.model.GCPUsageCostConfigResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    GCPUsageCostConfigPatchRequest body =
        new GCPUsageCostConfigPatchRequest()
            .data(
                new GCPUsageCostConfigPatchData()
                    .attributes(new GCPUsageCostConfigPatchRequestAttributes().isEnabled(true))
                    .type(GCPUsageCostConfigPatchRequestType.GCP_USAGE_COST_CONFIG_PATCH_REQUEST));

    try {
      GCPUsageCostConfigResponse result = apiInstance.updateCostGCPUsageCostConfig(100L, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#updateCostGCPUsageCostConfig");
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

```python
"""
Update Google Cloud Usage Cost config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_data import GCPUsageCostConfigPatchData
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_request import GCPUsageCostConfigPatchRequest
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_request_attributes import (
    GCPUsageCostConfigPatchRequestAttributes,
)
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_request_type import GCPUsageCostConfigPatchRequestType

body = GCPUsageCostConfigPatchRequest(
    data=GCPUsageCostConfigPatchData(
        attributes=GCPUsageCostConfigPatchRequestAttributes(
            is_enabled=True,
        ),
        type=GCPUsageCostConfigPatchRequestType.GCP_USAGE_COST_CONFIG_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_gcp_usage_cost_config(cloud_account_id=100, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update Google Cloud Usage Cost config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::GCPUsageCostConfigPatchRequest.new({
  data: DatadogAPIClient::V2::GCPUsageCostConfigPatchData.new({
    attributes: DatadogAPIClient::V2::GCPUsageCostConfigPatchRequestAttributes.new({
      is_enabled: true,
    }),
    type: DatadogAPIClient::V2::GCPUsageCostConfigPatchRequestType::GCP_USAGE_COST_CONFIG_PATCH_REQUEST,
  }),
})
p api_instance.update_cost_gcp_usage_cost_config(100, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update Google Cloud Usage Cost config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPatchData;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPatchRequest;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPatchRequestAttributes;
use datadog_api_client::datadogV2::model::GCPUsageCostConfigPatchRequestType;

#[tokio::main]
async fn main() {
    let body = GCPUsageCostConfigPatchRequest::new(GCPUsageCostConfigPatchData::new(
        GCPUsageCostConfigPatchRequestAttributes::new(true),
        GCPUsageCostConfigPatchRequestType::GCP_USAGE_COST_CONFIG_PATCH_REQUEST,
    ));
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.update_cost_gcp_usage_cost_config(100, body).await;
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
 * Update Google Cloud Usage Cost config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiUpdateCostGCPUsageCostConfigRequest = {
  body: {
    data: {
      attributes: {
        isEnabled: true,
      },
      type: "gcp_uc_config_patch_request",
    },
  },
  cloudAccountId: 100,
};

apiInstance
  .updateCostGCPUsageCostConfig(params)
  .then((data: v2.GCPUsageCostConfigResponse) => {
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

## Delete Google Cloud Usage Cost config{% #delete-google-cloud-usage-cost-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cost/gcp_uc_config/{cloud_account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cost/gcp_uc_config/{cloud_account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |

### Overview

Archive a Cloud Cost Management account. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description       |
| ---------------------------------- | ------- | ----------------- |
| cloud_account_id [*required*] | integer | Cloud Account id. |

### Response

{% tab title="204" %}
No Content
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

### Code Example

##### 
                  \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config/${cloud_account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Google Cloud Usage Cost config returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_cost_gcp_usage_cost_config(
        cloud_account_id=100,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete Google Cloud Usage Cost config returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
api_instance.delete_cost_gcp_usage_cost_config(100)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete Google Cloud Usage Cost config returns "No Content" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.DeleteCostGCPUsageCostConfig(ctx, 100)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.DeleteCostGCPUsageCostConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete Google Cloud Usage Cost config returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      apiInstance.deleteCostGCPUsageCostConfig(100L);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#deleteCostGCPUsageCostConfig");
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
// Delete Google Cloud Usage Cost config returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.delete_cost_gcp_usage_cost_config(100).await;
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
 * Delete Google Cloud Usage Cost config returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiDeleteCostGCPUsageCostConfigRequest = {
  cloudAccountId: 100,
};

apiInstance
  .deleteCostGCPUsageCostConfig(params)
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

## Get Google Cloud Usage Cost config{% #get-google-cloud-usage-cost-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/gcp_uc_config/{cloud_account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/gcp_uc_config/{cloud_account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config/{cloud_account_id} |

### Overview

Get a specific Google Cloud Usage Cost config.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                               | Type    | Description                                |
| ---------------------------------- | ------- | ------------------------------------------ |
| cloud_account_id [*required*] | integer | The unique identifier of the cloud account |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `GcpUcConfigResponse` object.

| Parent field | Field                  | Type     | Description                                                                        |
| ------------ | ---------------------- | -------- | ---------------------------------------------------------------------------------- |
|              | data                   | object   | The definition of `GcpUcConfigResponseData` object.                                |
| data         | attributes             | object   | The definition of `GcpUcConfigResponseDataAttributes` object.                      |
| attributes   | account_id             | string   | The `attributes` `account_id`.                                                     |
| attributes   | bucket_name            | string   | The `attributes` `bucket_name`.                                                    |
| attributes   | created_at             | string   | The `attributes` `created_at`.                                                     |
| attributes   | dataset                | string   | The `attributes` `dataset`.                                                        |
| attributes   | error_messages         | [string] | The `attributes` `error_messages`.                                                 |
| attributes   | export_prefix          | string   | The `attributes` `export_prefix`.                                                  |
| attributes   | export_project_name    | string   | The `attributes` `export_project_name`.                                            |
| attributes   | months                 | int64    | The `attributes` `months`.                                                         |
| attributes   | project_id             | string   | The `attributes` `project_id`.                                                     |
| attributes   | service_account        | string   | The `attributes` `service_account`.                                                |
| attributes   | status                 | string   | The `attributes` `status`.                                                         |
| attributes   | status_updated_at      | string   | The `attributes` `status_updated_at`.                                              |
| attributes   | updated_at             | string   | The `attributes` `updated_at`.                                                     |
| data         | id                     | string   | The `GcpUcConfigResponseData` `id`.                                                |
| data         | type [*required*] | enum     | Google Cloud Usage Cost config resource type. Allowed enum values: `gcp_uc_config` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_id": "123456_A123BC_12AB34",
      "bucket_name": "dd-cost-bucket",
      "created_at": "2023-01-01T12:00:00.000Z",
      "dataset": "billing",
      "error_messages": [],
      "export_prefix": "datadog_cloud_cost_usage_export",
      "export_project_name": "dd-cloud-cost-report",
      "months": 36,
      "project_id": "my-project-123",
      "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com",
      "status": "active",
      "status_updated_at": "2023-01-01T12:00:00.000Z",
      "updated_at": "2023-01-01T12:00:00.000Z"
    },
    "id": "123456789123",
    "type": "gcp_uc_config"
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
                  \# Path parametersexport cloud_account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/gcp_uc_config/${cloud_account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get Google Cloud Usage Cost config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_cost_gcp_usage_cost_config(
        cloud_account_id=123456,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get Google Cloud Usage Cost config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.get_cost_gcp_usage_cost_config(123456)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get Google Cloud Usage Cost config returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.GetCostGCPUsageCostConfig(ctx, 123456)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.GetCostGCPUsageCostConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.GetCostGCPUsageCostConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get Google Cloud Usage Cost config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.GcpUcConfigResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      GcpUcConfigResponse result = apiInstance.getCostGCPUsageCostConfig(123456L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#getCostGCPUsageCostConfig");
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
// Get Google Cloud Usage Cost config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.get_cost_gcp_usage_cost_config(123456).await;
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
 * Get Google Cloud Usage Cost config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiGetCostGCPUsageCostConfigRequest = {
  cloudAccountId: 123456,
};

apiInstance
  .getCostGCPUsageCostConfig(params)
  .then((data: v2.GcpUcConfigResponse) => {
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

## List tag pipeline rulesets{% #list-tag-pipeline-rulesets %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/tags/enrichment |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/tags/enrichment |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/tags/enrichment      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/tags/enrichment      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/tags/enrichment     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/tags/enrichment |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/tags/enrichment |

### Overview

List all tag pipeline rulesets - Retrieve a list of all tag pipeline rulesets for the organization

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `RulesetRespArray` object.

| Parent field         | Field                                     | Type     | Description                                                                   |
| -------------------- | ----------------------------------------- | -------- | ----------------------------------------------------------------------------- |
|                      | data [*required*]                    | [object] | The `RulesetRespArray` `data`.                                                |
| data                 | attributes                                | object   | The definition of `RulesetRespDataAttributes` object.                         |
| attributes           | created [*required*]                 | object   | The definition of `RulesetRespDataAttributesCreated` object.                  |
| created              | nanos                                     | int32    | The `created` `nanos`.                                                        |
| created              | seconds                                   | int64    | The `created` `seconds`.                                                      |
| attributes           | enabled [*required*]                 | boolean  | The `attributes` `enabled`.                                                   |
| attributes           | last_modified_user_uuid [*required*] | string   | The `attributes` `last_modified_user_uuid`.                                   |
| attributes           | modified [*required*]                | object   | The definition of `RulesetRespDataAttributesModified` object.                 |
| modified             | nanos                                     | int32    | The `modified` `nanos`.                                                       |
| modified             | seconds                                   | int64    | The `modified` `seconds`.                                                     |
| attributes           | name [*required*]                    | string   | The `attributes` `name`.                                                      |
| attributes           | position [*required*]                | int32    | The `attributes` `position`.                                                  |
| attributes           | processing_status                         | string   | The `attributes` `processing_status`.                                         |
| attributes           | rules [*required*]                   | [object] | The `attributes` `rules`.                                                     |
| rules                | enabled [*required*]                 | boolean  | The `items` `enabled`.                                                        |
| rules                | mapping                                   | object   | The definition of `RulesetRespDataAttributesRulesItemsMapping` object.        |
| mapping              | destination_key [*required*]         | string   | The `mapping` `destination_key`.                                              |
| mapping              | if_not_exists [*required*]           | boolean  | The `mapping` `if_not_exists`.                                                |
| mapping              | source_keys [*required*]             | [string] | The `mapping` `source_keys`.                                                  |
| rules                | metadata                                  | object   | The `items` `metadata`.                                                       |
| additionalProperties | <any-key>                                 | string   |
| rules                | name [*required*]                    | string   | The `items` `name`.                                                           |
| rules                | query                                     | object   | The definition of `RulesetRespDataAttributesRulesItemsQuery` object.          |
| query                | addition [*required*]                | object   | The definition of `RulesetRespDataAttributesRulesItemsQueryAddition` object.  |
| addition             | key [*required*]                     | string   | The `addition` `key`.                                                         |
| addition             | value [*required*]                   | string   | The `addition` `value`.                                                       |
| query                | case_insensitivity                        | boolean  | The `query` `case_insensitivity`.                                             |
| query                | if_not_exists [*required*]           | boolean  | The `query` `if_not_exists`.                                                  |
| query                | query [*required*]                   | string   | The `query` `query`.                                                          |
| rules                | reference_table                           | object   | The definition of `RulesetRespDataAttributesRulesItemsReferenceTable` object. |
| reference_table      | case_insensitivity                        | boolean  | The `reference_table` `case_insensitivity`.                                   |
| reference_table      | field_pairs [*required*]             | [object] | The `reference_table` `field_pairs`.                                          |
| field_pairs          | input_column [*required*]            | string   | The `items` `input_column`.                                                   |
| field_pairs          | output_key [*required*]              | string   | The `items` `output_key`.                                                     |
| reference_table      | if_not_exists                             | boolean  | The `reference_table` `if_not_exists`.                                        |
| reference_table      | source_keys [*required*]             | [string] | The `reference_table` `source_keys`.                                          |
| reference_table      | table_name [*required*]              | string   | The `reference_table` `table_name`.                                           |
| attributes           | version [*required*]                 | int64    | The `attributes` `version`.                                                   |
| data                 | id                                        | string   | The `RulesetRespData` `id`.                                                   |
| data                 | type [*required*]                    | enum     | Ruleset resource type. Allowed enum values: `ruleset`                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created": null,
        "enabled": true,
        "last_modified_user_uuid": "",
        "modified": null,
        "name": "Production Cost Allocation Rules",
        "position": 0,
        "rules": [
          {
            "enabled": true,
            "mapping": null,
            "metadata": null,
            "name": "AWS Production Account Tagging",
            "query": {
              "addition": {
                "key": "environment",
                "value": "production"
              },
              "case_insensitivity": false,
              "if_not_exists": true,
              "query": "billingcurrency:\"USD\" AND account_name:\"prod-account\""
            },
            "reference_table": null
          },
          {
            "enabled": true,
            "mapping": {
              "destination_key": "team_owner",
              "if_not_exists": true,
              "source_keys": [
                "account_name",
                "service"
              ]
            },
            "metadata": null,
            "name": "Team Mapping Rule",
            "query": null,
            "reference_table": null
          },
          {
            "enabled": true,
            "mapping": null,
            "metadata": null,
            "name": "New table rule with new UI",
            "query": null,
            "reference_table": {
              "case_insensitivity": true,
              "field_pairs": [
                {
                  "input_column": "status_type",
                  "output_key": "status"
                },
                {
                  "input_column": "status_description",
                  "output_key": "dess"
                }
              ],
              "if_not_exists": false,
              "source_keys": [
                "http_status",
                "status_description"
              ],
              "table_name": "http_status_codes"
            }
          }
        ],
        "version": 2
      },
      "id": "55ef2385-9ae1-4410-90c4-5ac1b60fec10",
      "type": "ruleset"
    },
    {
      "attributes": {
        "created": null,
        "enabled": true,
        "last_modified_user_uuid": "",
        "modified": null,
        "name": "Development Environment Rules",
        "position": 0,
        "rules": [
          {
            "enabled": true,
            "mapping": null,
            "metadata": null,
            "name": "Dev Account Cost Center",
            "query": {
              "addition": {
                "key": "cost_center",
                "value": "engineering"
              },
              "case_insensitivity": true,
              "if_not_exists": true,
              "query": "account_name:\"dev-*\""
            },
            "reference_table": null
          }
        ],
        "version": 1
      },
      "id": "a7b8c9d0-1234-5678-9abc-def012345678",
      "type": "ruleset"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/tags/enrichment" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List tag pipeline rulesets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_tag_pipelines_rulesets()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List tag pipeline rulesets returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.list_tag_pipelines_rulesets()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List tag pipeline rulesets returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ListTagPipelinesRulesets(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ListTagPipelinesRulesets`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ListTagPipelinesRulesets`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List tag pipeline rulesets returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.RulesetRespArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      RulesetRespArray result = apiInstance.listTagPipelinesRulesets();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#listTagPipelinesRulesets");
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
// List tag pipeline rulesets returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.list_tag_pipelines_rulesets().await;
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
 * List tag pipeline rulesets returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

apiInstance
  .listTagPipelinesRulesets()
  .then((data: v2.RulesetRespArray) => {
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

## Create tag pipeline ruleset{% #create-tag-pipeline-ruleset %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/tags/enrichment |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/tags/enrichment |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/tags/enrichment      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/tags/enrichment      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/tags/enrichment     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/tags/enrichment |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/tags/enrichment |

### Overview

Create a new tag pipeline ruleset with the specified rules and configuration

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field         | Field                             | Type     | Description                                                                            |
| -------------------- | --------------------------------- | -------- | -------------------------------------------------------------------------------------- |
|                      | data                              | object   | The definition of `CreateRulesetRequestData` object.                                   |
| data                 | attributes                        | object   | The definition of `CreateRulesetRequestDataAttributes` object.                         |
| attributes           | enabled                           | boolean  | The `attributes` `enabled`.                                                            |
| attributes           | rules [*required*]           | [object] | The `attributes` `rules`.                                                              |
| rules                | enabled [*required*]         | boolean  | The `items` `enabled`.                                                                 |
| rules                | mapping                           | object   | The definition of `CreateRulesetRequestDataAttributesRulesItemsMapping` object.        |
| mapping              | destination_key [*required*] | string   | The `mapping` `destination_key`.                                                       |
| mapping              | if_not_exists [*required*]   | boolean  | The `mapping` `if_not_exists`.                                                         |
| mapping              | source_keys [*required*]     | [string] | The `mapping` `source_keys`.                                                           |
| rules                | metadata                          | object   | The `items` `metadata`.                                                                |
| additionalProperties | <any-key>                         | string   |
| rules                | name [*required*]            | string   | The `items` `name`.                                                                    |
| rules                | query                             | object   | The definition of `CreateRulesetRequestDataAttributesRulesItemsQuery` object.          |
| query                | addition [*required*]        | object   | The definition of `CreateRulesetRequestDataAttributesRulesItemsQueryAddition` object.  |
| addition             | key [*required*]             | string   | The `addition` `key`.                                                                  |
| addition             | value [*required*]           | string   | The `addition` `value`.                                                                |
| query                | case_insensitivity                | boolean  | The `query` `case_insensitivity`.                                                      |
| query                | if_not_exists [*required*]   | boolean  | The `query` `if_not_exists`.                                                           |
| query                | query [*required*]           | string   | The `query` `query`.                                                                   |
| rules                | reference_table                   | object   | The definition of `CreateRulesetRequestDataAttributesRulesItemsReferenceTable` object. |
| reference_table      | case_insensitivity                | boolean  | The `reference_table` `case_insensitivity`.                                            |
| reference_table      | field_pairs [*required*]     | [object] | The `reference_table` `field_pairs`.                                                   |
| field_pairs          | input_column [*required*]    | string   | The `items` `input_column`.                                                            |
| field_pairs          | output_key [*required*]      | string   | The `items` `output_key`.                                                              |
| reference_table      | if_not_exists                     | boolean  | The `reference_table` `if_not_exists`.                                                 |
| reference_table      | source_keys [*required*]     | [string] | The `reference_table` `source_keys`.                                                   |
| reference_table      | table_name [*required*]      | string   | The `reference_table` `table_name`.                                                    |
| data                 | id                                | string   | The `CreateRulesetRequestData` `id`.                                                   |
| data                 | type [*required*]            | enum     | Create ruleset resource type. Allowed enum values: `create_ruleset`                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "rules": [
        {
          "enabled": true,
          "mapping": null,
          "name": "Add Cost Center Tag",
          "query": {
            "addition": {
              "key": "cost_center",
              "value": "engineering"
            },
            "case_insensitivity": false,
            "if_not_exists": true,
            "query": "account_id:\"123456789\" AND service:\"web-api\""
          },
          "reference_table": null
        }
      ]
    },
    "id": "New Ruleset",
    "type": "create_ruleset"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `RulesetResp` object.

| Parent field         | Field                                     | Type     | Description                                                                   |
| -------------------- | ----------------------------------------- | -------- | ----------------------------------------------------------------------------- |
|                      | data                                      | object   | The definition of `RulesetRespData` object.                                   |
| data                 | attributes                                | object   | The definition of `RulesetRespDataAttributes` object.                         |
| attributes           | created [*required*]                 | object   | The definition of `RulesetRespDataAttributesCreated` object.                  |
| created              | nanos                                     | int32    | The `created` `nanos`.                                                        |
| created              | seconds                                   | int64    | The `created` `seconds`.                                                      |
| attributes           | enabled [*required*]                 | boolean  | The `attributes` `enabled`.                                                   |
| attributes           | last_modified_user_uuid [*required*] | string   | The `attributes` `last_modified_user_uuid`.                                   |
| attributes           | modified [*required*]                | object   | The definition of `RulesetRespDataAttributesModified` object.                 |
| modified             | nanos                                     | int32    | The `modified` `nanos`.                                                       |
| modified             | seconds                                   | int64    | The `modified` `seconds`.                                                     |
| attributes           | name [*required*]                    | string   | The `attributes` `name`.                                                      |
| attributes           | position [*required*]                | int32    | The `attributes` `position`.                                                  |
| attributes           | processing_status                         | string   | The `attributes` `processing_status`.                                         |
| attributes           | rules [*required*]                   | [object] | The `attributes` `rules`.                                                     |
| rules                | enabled [*required*]                 | boolean  | The `items` `enabled`.                                                        |
| rules                | mapping                                   | object   | The definition of `RulesetRespDataAttributesRulesItemsMapping` object.        |
| mapping              | destination_key [*required*]         | string   | The `mapping` `destination_key`.                                              |
| mapping              | if_not_exists [*required*]           | boolean  | The `mapping` `if_not_exists`.                                                |
| mapping              | source_keys [*required*]             | [string] | The `mapping` `source_keys`.                                                  |
| rules                | metadata                                  | object   | The `items` `metadata`.                                                       |
| additionalProperties | <any-key>                                 | string   |
| rules                | name [*required*]                    | string   | The `items` `name`.                                                           |
| rules                | query                                     | object   | The definition of `RulesetRespDataAttributesRulesItemsQuery` object.          |
| query                | addition [*required*]                | object   | The definition of `RulesetRespDataAttributesRulesItemsQueryAddition` object.  |
| addition             | key [*required*]                     | string   | The `addition` `key`.                                                         |
| addition             | value [*required*]                   | string   | The `addition` `value`.                                                       |
| query                | case_insensitivity                        | boolean  | The `query` `case_insensitivity`.                                             |
| query                | if_not_exists [*required*]           | boolean  | The `query` `if_not_exists`.                                                  |
| query                | query [*required*]                   | string   | The `query` `query`.                                                          |
| rules                | reference_table                           | object   | The definition of `RulesetRespDataAttributesRulesItemsReferenceTable` object. |
| reference_table      | case_insensitivity                        | boolean  | The `reference_table` `case_insensitivity`.                                   |
| reference_table      | field_pairs [*required*]             | [object] | The `reference_table` `field_pairs`.                                          |
| field_pairs          | input_column [*required*]            | string   | The `items` `input_column`.                                                   |
| field_pairs          | output_key [*required*]              | string   | The `items` `output_key`.                                                     |
| reference_table      | if_not_exists                             | boolean  | The `reference_table` `if_not_exists`.                                        |
| reference_table      | source_keys [*required*]             | [string] | The `reference_table` `source_keys`.                                          |
| reference_table      | table_name [*required*]              | string   | The `reference_table` `table_name`.                                           |
| attributes           | version [*required*]                 | int64    | The `attributes` `version`.                                                   |
| data                 | id                                        | string   | The `RulesetRespData` `id`.                                                   |
| data                 | type [*required*]                    | enum     | Ruleset resource type. Allowed enum values: `ruleset`                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created": null,
      "enabled": true,
      "last_modified_user_uuid": "",
      "modified": null,
      "name": "Example Ruleset",
      "position": 0,
      "rules": [
        {
          "enabled": false,
          "mapping": null,
          "metadata": null,
          "name": "RC test rule edited1",
          "query": {
            "addition": {
              "key": "abc",
              "value": "ww"
            },
            "case_insensitivity": false,
            "if_not_exists": true,
            "query": "billingcurrency:\"USD\" AND account_name:\"SZA96462\" AND billingcurrency:\"USD\""
          },
          "reference_table": null
        },
        {
          "enabled": true,
          "mapping": {
            "destination_key": "h",
            "if_not_exists": true,
            "source_keys": [
              "accountname",
              "accountownerid"
            ]
          },
          "metadata": null,
          "name": "rule with empty source key",
          "query": null,
          "reference_table": null
        },
        {
          "enabled": true,
          "mapping": null,
          "metadata": null,
          "name": "New table rule with new UI",
          "query": null,
          "reference_table": {
            "case_insensitivity": true,
            "field_pairs": [
              {
                "input_column": "status_type",
                "output_key": "status"
              },
              {
                "input_column": "status_description",
                "output_key": "dess"
              }
            ],
            "if_not_exists": false,
            "source_keys": [
              "http_status",
              "status_description"
            ],
            "table_name": "http_status_codes"
          }
        }
      ],
      "version": 1
    },
    "id": "12345",
    "type": "ruleset"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/tags/enrichment" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": true,
      "rules": [
        {
          "enabled": true,
          "mapping": null,
          "name": "Add Cost Center Tag",
          "query": {
            "addition": {
              "key": "cost_center",
              "value": "engineering"
            },
            "case_insensitivity": false,
            "if_not_exists": true,
            "query": "account_id:\"123456789\" AND service:\"web-api\""
          },
          "reference_table": null
        }
      ]
    },
    "id": "New Ruleset",
    "type": "create_ruleset"
  }
}
EOF
                        
##### 

```go
// Create tag pipeline ruleset returns "OK" response

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
	body := datadogV2.CreateRulesetRequest{
		Data: &datadogV2.CreateRulesetRequestData{
			Attributes: &datadogV2.CreateRulesetRequestDataAttributes{
				Enabled: datadog.PtrBool(true),
				Rules: []datadogV2.CreateRulesetRequestDataAttributesRulesItems{
					{
						Enabled: true,
						Mapping: *datadogV2.NewNullableCreateRulesetRequestDataAttributesRulesItemsMapping(nil),
						Name:    "Add Cost Center Tag",
						Query: *datadogV2.NewNullableCreateRulesetRequestDataAttributesRulesItemsQuery(&datadogV2.CreateRulesetRequestDataAttributesRulesItemsQuery{
							Addition: *datadogV2.NewNullableCreateRulesetRequestDataAttributesRulesItemsQueryAddition(&datadogV2.CreateRulesetRequestDataAttributesRulesItemsQueryAddition{
								Key:   "cost_center",
								Value: "engineering",
							}),
							CaseInsensitivity: datadog.PtrBool(false),
							IfNotExists:       true,
							Query:             `account_id:"123456789" AND service:"web-api"`,
						}),
						ReferenceTable: *datadogV2.NewNullableCreateRulesetRequestDataAttributesRulesItemsReferenceTable(nil),
					},
				},
			},
			Id:   datadog.PtrString("New Ruleset"),
			Type: datadogV2.CREATERULESETREQUESTDATATYPE_CREATE_RULESET,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.CreateTagPipelinesRuleset(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.CreateTagPipelinesRuleset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.CreateTagPipelinesRuleset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create tag pipeline ruleset returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.CreateRulesetRequest;
import com.datadog.api.client.v2.model.CreateRulesetRequestData;
import com.datadog.api.client.v2.model.CreateRulesetRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateRulesetRequestDataAttributesRulesItems;
import com.datadog.api.client.v2.model.CreateRulesetRequestDataAttributesRulesItemsQuery;
import com.datadog.api.client.v2.model.CreateRulesetRequestDataAttributesRulesItemsQueryAddition;
import com.datadog.api.client.v2.model.CreateRulesetRequestDataType;
import com.datadog.api.client.v2.model.RulesetResp;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    CreateRulesetRequest body =
        new CreateRulesetRequest()
            .data(
                new CreateRulesetRequestData()
                    .attributes(
                        new CreateRulesetRequestDataAttributes()
                            .enabled(true)
                            .rules(
                                Collections.singletonList(
                                    new CreateRulesetRequestDataAttributesRulesItems()
                                        .enabled(true)
                                        .mapping(null)
                                        .name("Add Cost Center Tag")
                                        .query(
                                            new CreateRulesetRequestDataAttributesRulesItemsQuery()
                                                .addition(
                                                    new CreateRulesetRequestDataAttributesRulesItemsQueryAddition()
                                                        .key("cost_center")
                                                        .value("engineering"))
                                                .caseInsensitivity(false)
                                                .ifNotExists(true)
                                                .query(
                                                    """
account_id:"123456789" AND service:"web-api"
"""))
                                        .referenceTable(null))))
                    .id("New Ruleset")
                    .type(CreateRulesetRequestDataType.CREATE_RULESET));

    try {
      RulesetResp result = apiInstance.createTagPipelinesRuleset(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#createTagPipelinesRuleset");
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

```python
"""
Create tag pipeline ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.create_ruleset_request import CreateRulesetRequest
from datadog_api_client.v2.model.create_ruleset_request_data import CreateRulesetRequestData
from datadog_api_client.v2.model.create_ruleset_request_data_attributes import CreateRulesetRequestDataAttributes
from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items import (
    CreateRulesetRequestDataAttributesRulesItems,
)
from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query import (
    CreateRulesetRequestDataAttributesRulesItemsQuery,
)
from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query_addition import (
    CreateRulesetRequestDataAttributesRulesItemsQueryAddition,
)
from datadog_api_client.v2.model.create_ruleset_request_data_type import CreateRulesetRequestDataType

body = CreateRulesetRequest(
    data=CreateRulesetRequestData(
        attributes=CreateRulesetRequestDataAttributes(
            enabled=True,
            rules=[
                CreateRulesetRequestDataAttributesRulesItems(
                    enabled=True,
                    mapping=None,
                    name="Add Cost Center Tag",
                    query=CreateRulesetRequestDataAttributesRulesItemsQuery(
                        addition=CreateRulesetRequestDataAttributesRulesItemsQueryAddition(
                            key="cost_center",
                            value="engineering",
                        ),
                        case_insensitivity=False,
                        if_not_exists=True,
                        query='account_id:"123456789" AND service:"web-api"',
                    ),
                    reference_table=None,
                ),
            ],
        ),
        id="New Ruleset",
        type=CreateRulesetRequestDataType.CREATE_RULESET,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_tag_pipelines_ruleset(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create tag pipeline ruleset returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::CreateRulesetRequest.new({
  data: DatadogAPIClient::V2::CreateRulesetRequestData.new({
    attributes: DatadogAPIClient::V2::CreateRulesetRequestDataAttributes.new({
      enabled: true,
      rules: [
        DatadogAPIClient::V2::CreateRulesetRequestDataAttributesRulesItems.new({
          enabled: true,
          mapping: nil,
          name: "Add Cost Center Tag",
          query: DatadogAPIClient::V2::CreateRulesetRequestDataAttributesRulesItemsQuery.new({
            addition: DatadogAPIClient::V2::CreateRulesetRequestDataAttributesRulesItemsQueryAddition.new({
              key: "cost_center",
              value: "engineering",
            }),
            case_insensitivity: false,
            if_not_exists: true,
            query: 'account_id:"123456789" AND service:"web-api"',
          }),
          reference_table: nil,
        }),
      ],
    }),
    id: "New Ruleset",
    type: DatadogAPIClient::V2::CreateRulesetRequestDataType::CREATE_RULESET,
  }),
})
p api_instance.create_tag_pipelines_ruleset(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create tag pipeline ruleset returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::CreateRulesetRequest;
use datadog_api_client::datadogV2::model::CreateRulesetRequestData;
use datadog_api_client::datadogV2::model::CreateRulesetRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreateRulesetRequestDataAttributesRulesItems;
use datadog_api_client::datadogV2::model::CreateRulesetRequestDataAttributesRulesItemsQuery;
use datadog_api_client::datadogV2::model::CreateRulesetRequestDataAttributesRulesItemsQueryAddition;
use datadog_api_client::datadogV2::model::CreateRulesetRequestDataType;

#[tokio::main]
async fn main() {
    let body = CreateRulesetRequest::new().data(
        CreateRulesetRequestData::new(CreateRulesetRequestDataType::CREATE_RULESET)
            .attributes(
                CreateRulesetRequestDataAttributes::new(vec![
                    CreateRulesetRequestDataAttributesRulesItems::new(
                        true,
                        "Add Cost Center Tag".to_string(),
                    )
                    .mapping(None)
                    .query(Some(
                        CreateRulesetRequestDataAttributesRulesItemsQuery::new(
                            Some(
                                CreateRulesetRequestDataAttributesRulesItemsQueryAddition::new(
                                    "cost_center".to_string(),
                                    "engineering".to_string(),
                                ),
                            ),
                            true,
                            r#"account_id:"123456789" AND service:"web-api""#.to_string(),
                        )
                        .case_insensitivity(false),
                    ))
                    .reference_table(None),
                ])
                .enabled(true),
            )
            .id("New Ruleset".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.create_tag_pipelines_ruleset(body).await;
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
 * Create tag pipeline ruleset returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiCreateTagPipelinesRulesetRequest = {
  body: {
    data: {
      attributes: {
        enabled: true,
        rules: [
          {
            enabled: true,
            mapping: undefined,
            name: "Add Cost Center Tag",
            query: {
              addition: {
                key: "cost_center",
                value: "engineering",
              },
              caseInsensitivity: false,
              ifNotExists: true,
              query: `account_id:"123456789" AND service:"web-api"`,
            },
            referenceTable: undefined,
          },
        ],
      },
      id: "New Ruleset",
      type: "create_ruleset",
    },
  },
};

apiInstance
  .createTagPipelinesRuleset(params)
  .then((data: v2.RulesetResp) => {
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

## Update tag pipeline ruleset{% #update-tag-pipeline-ruleset %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/tags/enrichment/{ruleset_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/tags/enrichment/{ruleset_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/tags/enrichment/{ruleset_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |

### Overview

Update a tag pipeline ruleset - Update an existing tag pipeline ruleset with new rules and configuration

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                          |
| ---------------------------- | ------ | ------------------------------------ |
| ruleset_id [*required*] | string | The unique identifier of the ruleset |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field         | Field                             | Type     | Description                                                                            |
| -------------------- | --------------------------------- | -------- | -------------------------------------------------------------------------------------- |
|                      | data                              | object   | The definition of `UpdateRulesetRequestData` object.                                   |
| data                 | attributes                        | object   | The definition of `UpdateRulesetRequestDataAttributes` object.                         |
| attributes           | enabled [*required*]         | boolean  | The `attributes` `enabled`.                                                            |
| attributes           | last_version                      | int64    | The `attributes` `last_version`.                                                       |
| attributes           | rules [*required*]           | [object] | The `attributes` `rules`.                                                              |
| rules                | enabled [*required*]         | boolean  | The `items` `enabled`.                                                                 |
| rules                | mapping                           | object   | The definition of `UpdateRulesetRequestDataAttributesRulesItemsMapping` object.        |
| mapping              | destination_key [*required*] | string   | The `mapping` `destination_key`.                                                       |
| mapping              | if_not_exists [*required*]   | boolean  | The `mapping` `if_not_exists`.                                                         |
| mapping              | source_keys [*required*]     | [string] | The `mapping` `source_keys`.                                                           |
| rules                | metadata                          | object   | The `items` `metadata`.                                                                |
| additionalProperties | <any-key>                         | string   |
| rules                | name [*required*]            | string   | The `items` `name`.                                                                    |
| rules                | query                             | object   | The definition of `UpdateRulesetRequestDataAttributesRulesItemsQuery` object.          |
| query                | addition [*required*]        | object   | The definition of `UpdateRulesetRequestDataAttributesRulesItemsQueryAddition` object.  |
| addition             | key [*required*]             | string   | The `addition` `key`.                                                                  |
| addition             | value [*required*]           | string   | The `addition` `value`.                                                                |
| query                | case_insensitivity                | boolean  | The `query` `case_insensitivity`.                                                      |
| query                | if_not_exists [*required*]   | boolean  | The `query` `if_not_exists`.                                                           |
| query                | query [*required*]           | string   | The `query` `query`.                                                                   |
| rules                | reference_table                   | object   | The definition of `UpdateRulesetRequestDataAttributesRulesItemsReferenceTable` object. |
| reference_table      | case_insensitivity                | boolean  | The `reference_table` `case_insensitivity`.                                            |
| reference_table      | field_pairs [*required*]     | [object] | The `reference_table` `field_pairs`.                                                   |
| field_pairs          | input_column [*required*]    | string   | The `items` `input_column`.                                                            |
| field_pairs          | output_key [*required*]      | string   | The `items` `output_key`.                                                              |
| reference_table      | if_not_exists                     | boolean  | The `reference_table` `if_not_exists`.                                                 |
| reference_table      | source_keys [*required*]     | [string] | The `reference_table` `source_keys`.                                                   |
| reference_table      | table_name [*required*]      | string   | The `reference_table` `table_name`.                                                    |
| data                 | id                                | string   | The `UpdateRulesetRequestData` `id`.                                                   |
| data                 | type [*required*]            | enum     | Update ruleset resource type. Allowed enum values: `update_ruleset`                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "last_version": 3611102,
      "rules": [
        {
          "enabled": true,
          "mapping": {
            "destination_key": "team_owner",
            "if_not_exists": true,
            "source_keys": [
              "account_name",
              "account_id"
            ]
          },
          "name": "Account Name Mapping",
          "query": null,
          "reference_table": null
        }
      ]
    },
    "id": "New Ruleset",
    "type": "update_ruleset"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `RulesetResp` object.

| Parent field         | Field                                     | Type     | Description                                                                   |
| -------------------- | ----------------------------------------- | -------- | ----------------------------------------------------------------------------- |
|                      | data                                      | object   | The definition of `RulesetRespData` object.                                   |
| data                 | attributes                                | object   | The definition of `RulesetRespDataAttributes` object.                         |
| attributes           | created [*required*]                 | object   | The definition of `RulesetRespDataAttributesCreated` object.                  |
| created              | nanos                                     | int32    | The `created` `nanos`.                                                        |
| created              | seconds                                   | int64    | The `created` `seconds`.                                                      |
| attributes           | enabled [*required*]                 | boolean  | The `attributes` `enabled`.                                                   |
| attributes           | last_modified_user_uuid [*required*] | string   | The `attributes` `last_modified_user_uuid`.                                   |
| attributes           | modified [*required*]                | object   | The definition of `RulesetRespDataAttributesModified` object.                 |
| modified             | nanos                                     | int32    | The `modified` `nanos`.                                                       |
| modified             | seconds                                   | int64    | The `modified` `seconds`.                                                     |
| attributes           | name [*required*]                    | string   | The `attributes` `name`.                                                      |
| attributes           | position [*required*]                | int32    | The `attributes` `position`.                                                  |
| attributes           | processing_status                         | string   | The `attributes` `processing_status`.                                         |
| attributes           | rules [*required*]                   | [object] | The `attributes` `rules`.                                                     |
| rules                | enabled [*required*]                 | boolean  | The `items` `enabled`.                                                        |
| rules                | mapping                                   | object   | The definition of `RulesetRespDataAttributesRulesItemsMapping` object.        |
| mapping              | destination_key [*required*]         | string   | The `mapping` `destination_key`.                                              |
| mapping              | if_not_exists [*required*]           | boolean  | The `mapping` `if_not_exists`.                                                |
| mapping              | source_keys [*required*]             | [string] | The `mapping` `source_keys`.                                                  |
| rules                | metadata                                  | object   | The `items` `metadata`.                                                       |
| additionalProperties | <any-key>                                 | string   |
| rules                | name [*required*]                    | string   | The `items` `name`.                                                           |
| rules                | query                                     | object   | The definition of `RulesetRespDataAttributesRulesItemsQuery` object.          |
| query                | addition [*required*]                | object   | The definition of `RulesetRespDataAttributesRulesItemsQueryAddition` object.  |
| addition             | key [*required*]                     | string   | The `addition` `key`.                                                         |
| addition             | value [*required*]                   | string   | The `addition` `value`.                                                       |
| query                | case_insensitivity                        | boolean  | The `query` `case_insensitivity`.                                             |
| query                | if_not_exists [*required*]           | boolean  | The `query` `if_not_exists`.                                                  |
| query                | query [*required*]                   | string   | The `query` `query`.                                                          |
| rules                | reference_table                           | object   | The definition of `RulesetRespDataAttributesRulesItemsReferenceTable` object. |
| reference_table      | case_insensitivity                        | boolean  | The `reference_table` `case_insensitivity`.                                   |
| reference_table      | field_pairs [*required*]             | [object] | The `reference_table` `field_pairs`.                                          |
| field_pairs          | input_column [*required*]            | string   | The `items` `input_column`.                                                   |
| field_pairs          | output_key [*required*]              | string   | The `items` `output_key`.                                                     |
| reference_table      | if_not_exists                             | boolean  | The `reference_table` `if_not_exists`.                                        |
| reference_table      | source_keys [*required*]             | [string] | The `reference_table` `source_keys`.                                          |
| reference_table      | table_name [*required*]              | string   | The `reference_table` `table_name`.                                           |
| attributes           | version [*required*]                 | int64    | The `attributes` `version`.                                                   |
| data                 | id                                        | string   | The `RulesetRespData` `id`.                                                   |
| data                 | type [*required*]                    | enum     | Ruleset resource type. Allowed enum values: `ruleset`                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created": null,
      "enabled": true,
      "last_modified_user_uuid": "",
      "modified": null,
      "name": "Example Ruleset",
      "position": 0,
      "rules": [
        {
          "enabled": false,
          "mapping": null,
          "metadata": null,
          "name": "RC test rule edited1",
          "query": {
            "addition": {
              "key": "abc",
              "value": "ww"
            },
            "case_insensitivity": false,
            "if_not_exists": true,
            "query": "billingcurrency:\"USD\" AND account_name:\"SZA96462\" AND billingcurrency:\"USD\""
          },
          "reference_table": null
        },
        {
          "enabled": true,
          "mapping": {
            "destination_key": "h",
            "if_not_exists": true,
            "source_keys": [
              "accountname",
              "accountownerid"
            ]
          },
          "metadata": null,
          "name": "rule with empty source key",
          "query": null,
          "reference_table": null
        },
        {
          "enabled": true,
          "mapping": null,
          "metadata": null,
          "name": "New table rule with new UI",
          "query": null,
          "reference_table": {
            "case_insensitivity": true,
            "field_pairs": [
              {
                "input_column": "status_type",
                "output_key": "status"
              },
              {
                "input_column": "status_description",
                "output_key": "dess"
              }
            ],
            "if_not_exists": false,
            "source_keys": [
              "http_status",
              "status_description"
            ],
            "table_name": "http_status_codes"
          }
        }
      ],
      "version": 1
    },
    "id": "12345",
    "type": "ruleset"
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
                          \# Path parametersexport ruleset_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/tags/enrichment/${ruleset_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": true,
      "last_version": 3611102,
      "rules": [
        {
          "enabled": true,
          "mapping": {
            "destination_key": "team_owner",
            "if_not_exists": true,
            "source_keys": [
              "account_name",
              "account_id"
            ]
          },
          "name": "Account Name Mapping",
          "query": null,
          "reference_table": null
        }
      ]
    },
    "id": "New Ruleset",
    "type": "update_ruleset"
  }
}
EOF
                        
##### 

```go
// Update tag pipeline ruleset returns "OK" response

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
	body := datadogV2.UpdateRulesetRequest{
		Data: &datadogV2.UpdateRulesetRequestData{
			Attributes: &datadogV2.UpdateRulesetRequestDataAttributes{
				Enabled:     true,
				LastVersion: datadog.PtrInt64(3611102),
				Rules: []datadogV2.UpdateRulesetRequestDataAttributesRulesItems{
					{
						Enabled: true,
						Mapping: *datadogV2.NewNullableUpdateRulesetRequestDataAttributesRulesItemsMapping(&datadogV2.UpdateRulesetRequestDataAttributesRulesItemsMapping{
							DestinationKey: "team_owner",
							IfNotExists:    true,
							SourceKeys: []string{
								"account_name",
								"account_id",
							},
						}),
						Name:           "Account Name Mapping",
						Query:          *datadogV2.NewNullableUpdateRulesetRequestDataAttributesRulesItemsQuery(nil),
						ReferenceTable: *datadogV2.NewNullableUpdateRulesetRequestDataAttributesRulesItemsReferenceTable(nil),
					},
				},
			},
			Id:   datadog.PtrString("New Ruleset"),
			Type: datadogV2.UPDATERULESETREQUESTDATATYPE_UPDATE_RULESET,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.UpdateTagPipelinesRuleset(ctx, "ee10c3ff-312f-464c-b4f6-46adaa6d00a1", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.UpdateTagPipelinesRuleset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.UpdateTagPipelinesRuleset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update tag pipeline ruleset returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.RulesetResp;
import com.datadog.api.client.v2.model.UpdateRulesetRequest;
import com.datadog.api.client.v2.model.UpdateRulesetRequestData;
import com.datadog.api.client.v2.model.UpdateRulesetRequestDataAttributes;
import com.datadog.api.client.v2.model.UpdateRulesetRequestDataAttributesRulesItems;
import com.datadog.api.client.v2.model.UpdateRulesetRequestDataAttributesRulesItemsMapping;
import com.datadog.api.client.v2.model.UpdateRulesetRequestDataType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    UpdateRulesetRequest body =
        new UpdateRulesetRequest()
            .data(
                new UpdateRulesetRequestData()
                    .attributes(
                        new UpdateRulesetRequestDataAttributes()
                            .enabled(true)
                            .lastVersion(3611102L)
                            .rules(
                                Collections.singletonList(
                                    new UpdateRulesetRequestDataAttributesRulesItems()
                                        .enabled(true)
                                        .mapping(
                                            new UpdateRulesetRequestDataAttributesRulesItemsMapping()
                                                .destinationKey("team_owner")
                                                .ifNotExists(true)
                                                .sourceKeys(
                                                    Arrays.asList("account_name", "account_id")))
                                        .name("Account Name Mapping")
                                        .query(null)
                                        .referenceTable(null))))
                    .id("New Ruleset")
                    .type(UpdateRulesetRequestDataType.UPDATE_RULESET));

    try {
      RulesetResp result =
          apiInstance.updateTagPipelinesRuleset("ee10c3ff-312f-464c-b4f6-46adaa6d00a1", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#updateTagPipelinesRuleset");
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

```python
"""
Update tag pipeline ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.update_ruleset_request import UpdateRulesetRequest
from datadog_api_client.v2.model.update_ruleset_request_data import UpdateRulesetRequestData
from datadog_api_client.v2.model.update_ruleset_request_data_attributes import UpdateRulesetRequestDataAttributes
from datadog_api_client.v2.model.update_ruleset_request_data_attributes_rules_items import (
    UpdateRulesetRequestDataAttributesRulesItems,
)
from datadog_api_client.v2.model.update_ruleset_request_data_attributes_rules_items_mapping import (
    UpdateRulesetRequestDataAttributesRulesItemsMapping,
)
from datadog_api_client.v2.model.update_ruleset_request_data_type import UpdateRulesetRequestDataType

body = UpdateRulesetRequest(
    data=UpdateRulesetRequestData(
        attributes=UpdateRulesetRequestDataAttributes(
            enabled=True,
            last_version=3611102,
            rules=[
                UpdateRulesetRequestDataAttributesRulesItems(
                    enabled=True,
                    mapping=UpdateRulesetRequestDataAttributesRulesItemsMapping(
                        destination_key="team_owner",
                        if_not_exists=True,
                        source_keys=[
                            "account_name",
                            "account_id",
                        ],
                    ),
                    name="Account Name Mapping",
                    query=None,
                    reference_table=None,
                ),
            ],
        ),
        id="New Ruleset",
        type=UpdateRulesetRequestDataType.UPDATE_RULESET,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_tag_pipelines_ruleset(ruleset_id="ee10c3ff-312f-464c-b4f6-46adaa6d00a1", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update tag pipeline ruleset returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::UpdateRulesetRequest.new({
  data: DatadogAPIClient::V2::UpdateRulesetRequestData.new({
    attributes: DatadogAPIClient::V2::UpdateRulesetRequestDataAttributes.new({
      enabled: true,
      last_version: 3611102,
      rules: [
        DatadogAPIClient::V2::UpdateRulesetRequestDataAttributesRulesItems.new({
          enabled: true,
          mapping: DatadogAPIClient::V2::UpdateRulesetRequestDataAttributesRulesItemsMapping.new({
            destination_key: "team_owner",
            if_not_exists: true,
            source_keys: [
              "account_name",
              "account_id",
            ],
          }),
          name: "Account Name Mapping",
          query: nil,
          reference_table: nil,
        }),
      ],
    }),
    id: "New Ruleset",
    type: DatadogAPIClient::V2::UpdateRulesetRequestDataType::UPDATE_RULESET,
  }),
})
p api_instance.update_tag_pipelines_ruleset("ee10c3ff-312f-464c-b4f6-46adaa6d00a1", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update tag pipeline ruleset returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::UpdateRulesetRequest;
use datadog_api_client::datadogV2::model::UpdateRulesetRequestData;
use datadog_api_client::datadogV2::model::UpdateRulesetRequestDataAttributes;
use datadog_api_client::datadogV2::model::UpdateRulesetRequestDataAttributesRulesItems;
use datadog_api_client::datadogV2::model::UpdateRulesetRequestDataAttributesRulesItemsMapping;
use datadog_api_client::datadogV2::model::UpdateRulesetRequestDataType;

#[tokio::main]
async fn main() {
    let body = UpdateRulesetRequest::new().data(
        UpdateRulesetRequestData::new(UpdateRulesetRequestDataType::UPDATE_RULESET)
            .attributes(
                UpdateRulesetRequestDataAttributes::new(
                    true,
                    vec![UpdateRulesetRequestDataAttributesRulesItems::new(
                        true,
                        "Account Name Mapping".to_string(),
                    )
                    .mapping(Some(
                        UpdateRulesetRequestDataAttributesRulesItemsMapping::new(
                            "team_owner".to_string(),
                            true,
                            vec!["account_name".to_string(), "account_id".to_string()],
                        ),
                    ))
                    .query(None)
                    .reference_table(None)],
                )
                .last_version(3611102),
            )
            .id("New Ruleset".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api
        .update_tag_pipelines_ruleset("ee10c3ff-312f-464c-b4f6-46adaa6d00a1".to_string(), body)
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
 * Update tag pipeline ruleset returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiUpdateTagPipelinesRulesetRequest = {
  body: {
    data: {
      attributes: {
        enabled: true,
        lastVersion: 3611102,
        rules: [
          {
            enabled: true,
            mapping: {
              destinationKey: "team_owner",
              ifNotExists: true,
              sourceKeys: ["account_name", "account_id"],
            },
            name: "Account Name Mapping",
            query: undefined,
            referenceTable: undefined,
          },
        ],
      },
      id: "New Ruleset",
      type: "update_ruleset",
    },
  },
  rulesetId: "ee10c3ff-312f-464c-b4f6-46adaa6d00a1",
};

apiInstance
  .updateTagPipelinesRuleset(params)
  .then((data: v2.RulesetResp) => {
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

## Delete tag pipeline ruleset{% #delete-tag-pipeline-ruleset %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/tags/enrichment/{ruleset_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/tags/enrichment/{ruleset_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/tags/enrichment/{ruleset_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |

### Overview

Delete a tag pipeline ruleset - Delete an existing tag pipeline ruleset by its ID

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                          |
| ---------------------------- | ------ | ------------------------------------ |
| ruleset_id [*required*] | string | The unique identifier of the ruleset |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport ruleset_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/tags/enrichment/${ruleset_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete tag pipeline ruleset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_tag_pipelines_ruleset(
        ruleset_id="ee10c3ff-312f-464c-b4f6-46adaa6d00a1",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete tag pipeline ruleset returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
api_instance.delete_tag_pipelines_ruleset("ee10c3ff-312f-464c-b4f6-46adaa6d00a1")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete tag pipeline ruleset returns "No Content" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.DeleteTagPipelinesRuleset(ctx, "ee10c3ff-312f-464c-b4f6-46adaa6d00a1")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.DeleteTagPipelinesRuleset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete tag pipeline ruleset returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      apiInstance.deleteTagPipelinesRuleset("ee10c3ff-312f-464c-b4f6-46adaa6d00a1");
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#deleteTagPipelinesRuleset");
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
// Delete tag pipeline ruleset returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api
        .delete_tag_pipelines_ruleset("ee10c3ff-312f-464c-b4f6-46adaa6d00a1".to_string())
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
 * Delete tag pipeline ruleset returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiDeleteTagPipelinesRulesetRequest = {
  rulesetId: "ee10c3ff-312f-464c-b4f6-46adaa6d00a1",
};

apiInstance
  .deleteTagPipelinesRuleset(params)
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

## Get a tag pipeline ruleset{% #get-a-tag-pipeline-ruleset %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/tags/enrichment/{ruleset_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/tags/enrichment/{ruleset_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/tags/enrichment/{ruleset_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/tags/enrichment/{ruleset_id} |

### Overview

Get a specific tag pipeline ruleset - Retrieve a specific tag pipeline ruleset by its ID

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                          |
| ---------------------------- | ------ | ------------------------------------ |
| ruleset_id [*required*] | string | The unique identifier of the ruleset |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `RulesetResp` object.

| Parent field         | Field                                     | Type     | Description                                                                   |
| -------------------- | ----------------------------------------- | -------- | ----------------------------------------------------------------------------- |
|                      | data                                      | object   | The definition of `RulesetRespData` object.                                   |
| data                 | attributes                                | object   | The definition of `RulesetRespDataAttributes` object.                         |
| attributes           | created [*required*]                 | object   | The definition of `RulesetRespDataAttributesCreated` object.                  |
| created              | nanos                                     | int32    | The `created` `nanos`.                                                        |
| created              | seconds                                   | int64    | The `created` `seconds`.                                                      |
| attributes           | enabled [*required*]                 | boolean  | The `attributes` `enabled`.                                                   |
| attributes           | last_modified_user_uuid [*required*] | string   | The `attributes` `last_modified_user_uuid`.                                   |
| attributes           | modified [*required*]                | object   | The definition of `RulesetRespDataAttributesModified` object.                 |
| modified             | nanos                                     | int32    | The `modified` `nanos`.                                                       |
| modified             | seconds                                   | int64    | The `modified` `seconds`.                                                     |
| attributes           | name [*required*]                    | string   | The `attributes` `name`.                                                      |
| attributes           | position [*required*]                | int32    | The `attributes` `position`.                                                  |
| attributes           | processing_status                         | string   | The `attributes` `processing_status`.                                         |
| attributes           | rules [*required*]                   | [object] | The `attributes` `rules`.                                                     |
| rules                | enabled [*required*]                 | boolean  | The `items` `enabled`.                                                        |
| rules                | mapping                                   | object   | The definition of `RulesetRespDataAttributesRulesItemsMapping` object.        |
| mapping              | destination_key [*required*]         | string   | The `mapping` `destination_key`.                                              |
| mapping              | if_not_exists [*required*]           | boolean  | The `mapping` `if_not_exists`.                                                |
| mapping              | source_keys [*required*]             | [string] | The `mapping` `source_keys`.                                                  |
| rules                | metadata                                  | object   | The `items` `metadata`.                                                       |
| additionalProperties | <any-key>                                 | string   |
| rules                | name [*required*]                    | string   | The `items` `name`.                                                           |
| rules                | query                                     | object   | The definition of `RulesetRespDataAttributesRulesItemsQuery` object.          |
| query                | addition [*required*]                | object   | The definition of `RulesetRespDataAttributesRulesItemsQueryAddition` object.  |
| addition             | key [*required*]                     | string   | The `addition` `key`.                                                         |
| addition             | value [*required*]                   | string   | The `addition` `value`.                                                       |
| query                | case_insensitivity                        | boolean  | The `query` `case_insensitivity`.                                             |
| query                | if_not_exists [*required*]           | boolean  | The `query` `if_not_exists`.                                                  |
| query                | query [*required*]                   | string   | The `query` `query`.                                                          |
| rules                | reference_table                           | object   | The definition of `RulesetRespDataAttributesRulesItemsReferenceTable` object. |
| reference_table      | case_insensitivity                        | boolean  | The `reference_table` `case_insensitivity`.                                   |
| reference_table      | field_pairs [*required*]             | [object] | The `reference_table` `field_pairs`.                                          |
| field_pairs          | input_column [*required*]            | string   | The `items` `input_column`.                                                   |
| field_pairs          | output_key [*required*]              | string   | The `items` `output_key`.                                                     |
| reference_table      | if_not_exists                             | boolean  | The `reference_table` `if_not_exists`.                                        |
| reference_table      | source_keys [*required*]             | [string] | The `reference_table` `source_keys`.                                          |
| reference_table      | table_name [*required*]              | string   | The `reference_table` `table_name`.                                           |
| attributes           | version [*required*]                 | int64    | The `attributes` `version`.                                                   |
| data                 | id                                        | string   | The `RulesetRespData` `id`.                                                   |
| data                 | type [*required*]                    | enum     | Ruleset resource type. Allowed enum values: `ruleset`                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created": null,
      "enabled": true,
      "last_modified_user_uuid": "",
      "modified": null,
      "name": "Example Ruleset",
      "position": 0,
      "rules": [
        {
          "enabled": false,
          "mapping": null,
          "metadata": null,
          "name": "RC test rule edited1",
          "query": {
            "addition": {
              "key": "abc",
              "value": "ww"
            },
            "case_insensitivity": false,
            "if_not_exists": true,
            "query": "billingcurrency:\"USD\" AND account_name:\"SZA96462\" AND billingcurrency:\"USD\""
          },
          "reference_table": null
        },
        {
          "enabled": true,
          "mapping": {
            "destination_key": "h",
            "if_not_exists": true,
            "source_keys": [
              "accountname",
              "accountownerid"
            ]
          },
          "metadata": null,
          "name": "rule with empty source key",
          "query": null,
          "reference_table": null
        },
        {
          "enabled": true,
          "mapping": null,
          "metadata": null,
          "name": "New table rule with new UI",
          "query": null,
          "reference_table": {
            "case_insensitivity": true,
            "field_pairs": [
              {
                "input_column": "status_type",
                "output_key": "status"
              },
              {
                "input_column": "status_description",
                "output_key": "dess"
              }
            ],
            "if_not_exists": false,
            "source_keys": [
              "http_status",
              "status_description"
            ],
            "table_name": "http_status_codes"
          }
        }
      ],
      "version": 1
    },
    "id": "12345",
    "type": "ruleset"
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
                  \# Path parametersexport ruleset_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/tags/enrichment/${ruleset_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a tag pipeline ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_tag_pipelines_ruleset(
        ruleset_id="a1e9de9b-b88e-41c6-a0cd-cc0ebd7092de",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a tag pipeline ruleset returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.get_tag_pipelines_ruleset("a1e9de9b-b88e-41c6-a0cd-cc0ebd7092de")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a tag pipeline ruleset returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.GetTagPipelinesRuleset(ctx, "a1e9de9b-b88e-41c6-a0cd-cc0ebd7092de")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.GetTagPipelinesRuleset`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.GetTagPipelinesRuleset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a tag pipeline ruleset returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.RulesetResp;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      RulesetResp result =
          apiInstance.getTagPipelinesRuleset("a1e9de9b-b88e-41c6-a0cd-cc0ebd7092de");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#getTagPipelinesRuleset");
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
// Get a tag pipeline ruleset returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api
        .get_tag_pipelines_ruleset("a1e9de9b-b88e-41c6-a0cd-cc0ebd7092de".to_string())
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
 * Get a tag pipeline ruleset returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiGetTagPipelinesRulesetRequest = {
  rulesetId: "a1e9de9b-b88e-41c6-a0cd-cc0ebd7092de",
};

apiInstance
  .getTagPipelinesRuleset(params)
  .then((data: v2.RulesetResp) => {
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

## Reorder tag pipeline rulesets{% #reorder-tag-pipeline-rulesets %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/tags/enrichment/reorder |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/tags/enrichment/reorder |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/tags/enrichment/reorder      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/tags/enrichment/reorder      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/tags/enrichment/reorder     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/tags/enrichment/reorder |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/tags/enrichment/reorder |

### Overview

Reorder tag pipeline rulesets - Change the execution order of tag pipeline rulesets

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                           |
| ------------ | ---------------------- | -------- | ----------------------------------------------------- |
|              | data [*required*] | [object] | The `ReorderRulesetResourceArray` `data`.             |
| data         | id                     | string   | The `ReorderRulesetResourceData` `id`.                |
| data         | type [*required*] | enum     | Ruleset resource type. Allowed enum values: `ruleset` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "string",
      "type": "ruleset"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="204" %}
Successfully reordered rulesets
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/tags/enrichment/reorder" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "type": "ruleset"
    }
  ]
}
EOF
                
##### 

```python
"""
Reorder tag pipeline rulesets returns "Successfully reordered rulesets" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.reorder_ruleset_resource_array import ReorderRulesetResourceArray
from datadog_api_client.v2.model.reorder_ruleset_resource_data import ReorderRulesetResourceData
from datadog_api_client.v2.model.reorder_ruleset_resource_data_type import ReorderRulesetResourceDataType

body = ReorderRulesetResourceArray(
    data=[
        ReorderRulesetResourceData(
            id="55ef2385-9ae1-4410-90c4-5ac1b60fec10",
            type=ReorderRulesetResourceDataType.RULESET,
        ),
        ReorderRulesetResourceData(
            id="a7b8c9d0-1234-5678-9abc-def012345678",
            type=ReorderRulesetResourceDataType.RULESET,
        ),
        ReorderRulesetResourceData(
            id="f1e2d3c4-b5a6-9780-1234-567890abcdef",
            type=ReorderRulesetResourceDataType.RULESET,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.reorder_tag_pipelines_rulesets(body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Reorder tag pipeline rulesets returns "Successfully reordered rulesets" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::ReorderRulesetResourceArray.new({
  data: [
    DatadogAPIClient::V2::ReorderRulesetResourceData.new({
      id: "55ef2385-9ae1-4410-90c4-5ac1b60fec10",
      type: DatadogAPIClient::V2::ReorderRulesetResourceDataType::RULESET,
    }),
    DatadogAPIClient::V2::ReorderRulesetResourceData.new({
      id: "a7b8c9d0-1234-5678-9abc-def012345678",
      type: DatadogAPIClient::V2::ReorderRulesetResourceDataType::RULESET,
    }),
    DatadogAPIClient::V2::ReorderRulesetResourceData.new({
      id: "f1e2d3c4-b5a6-9780-1234-567890abcdef",
      type: DatadogAPIClient::V2::ReorderRulesetResourceDataType::RULESET,
    }),
  ],
})
api_instance.reorder_tag_pipelines_rulesets(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Reorder tag pipeline rulesets returns "Successfully reordered rulesets" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.ReorderRulesetResourceArray{
		Data: []datadogV2.ReorderRulesetResourceData{
			{
				Id:   datadog.PtrString("55ef2385-9ae1-4410-90c4-5ac1b60fec10"),
				Type: datadogV2.REORDERRULESETRESOURCEDATATYPE_RULESET,
			},
			{
				Id:   datadog.PtrString("a7b8c9d0-1234-5678-9abc-def012345678"),
				Type: datadogV2.REORDERRULESETRESOURCEDATATYPE_RULESET,
			},
			{
				Id:   datadog.PtrString("f1e2d3c4-b5a6-9780-1234-567890abcdef"),
				Type: datadogV2.REORDERRULESETRESOURCEDATATYPE_RULESET,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.ReorderTagPipelinesRulesets(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ReorderTagPipelinesRulesets`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Reorder tag pipeline rulesets returns "Successfully reordered rulesets" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.ReorderRulesetResourceArray;
import com.datadog.api.client.v2.model.ReorderRulesetResourceData;
import com.datadog.api.client.v2.model.ReorderRulesetResourceDataType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    ReorderRulesetResourceArray body =
        new ReorderRulesetResourceArray()
            .data(
                Arrays.asList(
                    new ReorderRulesetResourceData()
                        .id("55ef2385-9ae1-4410-90c4-5ac1b60fec10")
                        .type(ReorderRulesetResourceDataType.RULESET),
                    new ReorderRulesetResourceData()
                        .id("a7b8c9d0-1234-5678-9abc-def012345678")
                        .type(ReorderRulesetResourceDataType.RULESET),
                    new ReorderRulesetResourceData()
                        .id("f1e2d3c4-b5a6-9780-1234-567890abcdef")
                        .type(ReorderRulesetResourceDataType.RULESET)));

    try {
      apiInstance.reorderTagPipelinesRulesets(body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#reorderTagPipelinesRulesets");
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
// Reorder tag pipeline rulesets returns "Successfully reordered rulesets" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::ReorderRulesetResourceArray;
use datadog_api_client::datadogV2::model::ReorderRulesetResourceData;
use datadog_api_client::datadogV2::model::ReorderRulesetResourceDataType;

#[tokio::main]
async fn main() {
    let body = ReorderRulesetResourceArray::new(vec![
        ReorderRulesetResourceData::new(ReorderRulesetResourceDataType::RULESET)
            .id("55ef2385-9ae1-4410-90c4-5ac1b60fec10".to_string()),
        ReorderRulesetResourceData::new(ReorderRulesetResourceDataType::RULESET)
            .id("a7b8c9d0-1234-5678-9abc-def012345678".to_string()),
        ReorderRulesetResourceData::new(ReorderRulesetResourceDataType::RULESET)
            .id("f1e2d3c4-b5a6-9780-1234-567890abcdef".to_string()),
    ]);
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.reorder_tag_pipelines_rulesets(body).await;
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
 * Reorder tag pipeline rulesets returns "Successfully reordered rulesets" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiReorderTagPipelinesRulesetsRequest = {
  body: {
    data: [
      {
        id: "55ef2385-9ae1-4410-90c4-5ac1b60fec10",
        type: "ruleset",
      },
      {
        id: "a7b8c9d0-1234-5678-9abc-def012345678",
        type: "ruleset",
      },
      {
        id: "f1e2d3c4-b5a6-9780-1234-567890abcdef",
        type: "ruleset",
      },
    ],
  },
};

apiInstance
  .reorderTagPipelinesRulesets(params)
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

## Validate query{% #validate-query %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/tags/enrichment/validate-query |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/tags/enrichment/validate-query |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/tags/enrichment/validate-query      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/tags/enrichment/validate-query      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/tags/enrichment/validate-query     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/tags/enrichment/validate-query |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/tags/enrichment/validate-query |

### Overview

Validate a tag pipeline query - Validate the syntax and structure of a tag pipeline query

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                   | Type   | Description                                                         |
| ------------ | ----------------------- | ------ | ------------------------------------------------------------------- |
|              | data                    | object | The definition of `RulesValidateQueryRequestData` object.           |
| data         | attributes              | object | The definition of `RulesValidateQueryRequestDataAttributes` object. |
| attributes   | Query [*required*] | string | The `attributes` `Query`.                                           |
| data         | id                      | string | The `RulesValidateQueryRequestData` `id`.                           |
| data         | type [*required*]  | enum   | Validate query resource type. Allowed enum values: `validate_query` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "Query": "example:query AND test:true"
    },
    "type": "validate_query"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `RulesValidateQueryResponse` object.

| Parent field | Field                       | Type   | Description                                                               |
| ------------ | --------------------------- | ------ | ------------------------------------------------------------------------- |
|              | data                        | object | The definition of `RulesValidateQueryResponseData` object.                |
| data         | attributes                  | object | The definition of `RulesValidateQueryResponseDataAttributes` object.      |
| attributes   | Canonical [*required*] | string | The `attributes` `Canonical`.                                             |
| data         | id                          | string | The `RulesValidateQueryResponseData` `id`.                                |
| data         | type [*required*]      | enum   | Validate response resource type. Allowed enum values: `validate_response` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "Canonical": "canonical query representation"
    },
    "type": "validate_response"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/tags/enrichment/validate-query" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "Query": "example:query AND test:true"
    },
    "type": "validate_query"
  }
}
EOF
                        
##### 

```go
// Validate query returns "OK" response

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
	body := datadogV2.RulesValidateQueryRequest{
		Data: &datadogV2.RulesValidateQueryRequestData{
			Attributes: &datadogV2.RulesValidateQueryRequestDataAttributes{
				Query: "example:query AND test:true",
			},
			Type: datadogV2.RULESVALIDATEQUERYREQUESTDATATYPE_VALIDATE_QUERY,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ValidateQuery(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ValidateQuery`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ValidateQuery`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Validate query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.RulesValidateQueryRequest;
import com.datadog.api.client.v2.model.RulesValidateQueryRequestData;
import com.datadog.api.client.v2.model.RulesValidateQueryRequestDataAttributes;
import com.datadog.api.client.v2.model.RulesValidateQueryRequestDataType;
import com.datadog.api.client.v2.model.RulesValidateQueryResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    RulesValidateQueryRequest body =
        new RulesValidateQueryRequest()
            .data(
                new RulesValidateQueryRequestData()
                    .attributes(
                        new RulesValidateQueryRequestDataAttributes()
                            .query("example:query AND test:true"))
                    .type(RulesValidateQueryRequestDataType.VALIDATE_QUERY));

    try {
      RulesValidateQueryResponse result = apiInstance.validateQuery(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#validateQuery");
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

```python
"""
Validate query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.rules_validate_query_request import RulesValidateQueryRequest
from datadog_api_client.v2.model.rules_validate_query_request_data import RulesValidateQueryRequestData
from datadog_api_client.v2.model.rules_validate_query_request_data_attributes import (
    RulesValidateQueryRequestDataAttributes,
)
from datadog_api_client.v2.model.rules_validate_query_request_data_type import RulesValidateQueryRequestDataType

body = RulesValidateQueryRequest(
    data=RulesValidateQueryRequestData(
        attributes=RulesValidateQueryRequestDataAttributes(
            query="example:query AND test:true",
        ),
        type=RulesValidateQueryRequestDataType.VALIDATE_QUERY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.validate_query(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Validate query returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::RulesValidateQueryRequest.new({
  data: DatadogAPIClient::V2::RulesValidateQueryRequestData.new({
    attributes: DatadogAPIClient::V2::RulesValidateQueryRequestDataAttributes.new({
      query: "example:query AND test:true",
    }),
    type: DatadogAPIClient::V2::RulesValidateQueryRequestDataType::VALIDATE_QUERY,
  }),
})
p api_instance.validate_query(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Validate query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::RulesValidateQueryRequest;
use datadog_api_client::datadogV2::model::RulesValidateQueryRequestData;
use datadog_api_client::datadogV2::model::RulesValidateQueryRequestDataAttributes;
use datadog_api_client::datadogV2::model::RulesValidateQueryRequestDataType;

#[tokio::main]
async fn main() {
    let body = RulesValidateQueryRequest::new().data(
        RulesValidateQueryRequestData::new(RulesValidateQueryRequestDataType::VALIDATE_QUERY)
            .attributes(RulesValidateQueryRequestDataAttributes::new(
                "example:query AND test:true".to_string(),
            )),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.validate_query(body).await;
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
 * Validate query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiValidateQueryRequest = {
  body: {
    data: {
      attributes: {
        query: "example:query AND test:true",
      },
      type: "validate_query",
    },
  },
};

apiInstance
  .validateQuery(params)
  .then((data: v2.RulesValidateQueryResponse) => {
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

## List custom allocation rules{% #list-custom-allocation-rules %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/arbitrary_rule |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/arbitrary_rule |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/arbitrary_rule      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/arbitrary_rule      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/arbitrary_rule     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/arbitrary_rule |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule |

### Overview

List all custom allocation rules - Retrieve a list of all custom allocation rules for the organization

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `ArbitraryRuleResponseArray` object.

| Parent field                | Field                                     | Type      | Description                                                                       |
| --------------------------- | ----------------------------------------- | --------- | --------------------------------------------------------------------------------- |
|                             | data [*required*]                    | [object]  | The `ArbitraryRuleResponseArray` `data`.                                          |
| data                        | attributes                                | object    | The definition of `ArbitraryRuleResponseDataAttributes` object.                   |
| attributes                  | costs_to_allocate [*required*]       | [object]  | The `attributes` `costs_to_allocate`.                                             |
| costs_to_allocate           | condition [*required*]               | string    | The `items` `condition`.                                                          |
| costs_to_allocate           | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| costs_to_allocate           | value                                     | string    | The `items` `value`.                                                              |
| costs_to_allocate           | values                                    | [string]  | The `items` `values`.                                                             |
| attributes                  | created [*required*]                 | date-time | The `attributes` `created`.                                                       |
| attributes                  | enabled [*required*]                 | boolean   | The `attributes` `enabled`.                                                       |
| attributes                  | last_modified_user_uuid [*required*] | string    | The `attributes` `last_modified_user_uuid`.                                       |
| attributes                  | order_id [*required*]                | int64     | The `attributes` `order_id`.                                                      |
| attributes                  | processing_status                         | string    | The `attributes` `processing_status`.                                             |
| attributes                  | provider [*required*]                | [string]  | The `attributes` `provider`.                                                      |
| attributes                  | rejected                                  | boolean   | The `attributes` `rejected`.                                                      |
| attributes                  | rule_name [*required*]               | string    | The `attributes` `rule_name`.                                                     |
| attributes                  | strategy [*required*]                | object    | The definition of `ArbitraryRuleResponseDataAttributesStrategy` object.           |
| strategy                    | allocated_by                              | [object]  | The `strategy` `allocated_by`.                                                    |
| allocated_by                | allocated_tags [*required*]          | [object]  | The `items` `allocated_tags`.                                                     |
| allocated_tags              | key [*required*]                     | string    | The `items` `key`.                                                                |
| allocated_tags              | value [*required*]                   | string    | The `items` `value`.                                                              |
| allocated_by                | percentage [*required*]              | double    | The `items` `percentage`. The numeric value format should be a 32bit float value. |
| strategy                    | allocated_by_filters                      | [object]  | The `strategy` `allocated_by_filters`.                                            |
| allocated_by_filters        | condition [*required*]               | string    | The `items` `condition`.                                                          |
| allocated_by_filters        | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| allocated_by_filters        | value                                     | string    | The `items` `value`.                                                              |
| allocated_by_filters        | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | allocated_by_tag_keys                     | [string]  | The `strategy` `allocated_by_tag_keys`.                                           |
| strategy                    | based_on_costs                            | [object]  | The `strategy` `based_on_costs`.                                                  |
| based_on_costs              | condition [*required*]               | string    | The `items` `condition`.                                                          |
| based_on_costs              | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| based_on_costs              | value                                     | string    | The `items` `value`.                                                              |
| based_on_costs              | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | based_on_timeseries                       | object    | The rule `strategy` `based_on_timeseries`.                                        |
| strategy                    | evaluate_grouped_by_filters               | [object]  | The `strategy` `evaluate_grouped_by_filters`.                                     |
| evaluate_grouped_by_filters | condition [*required*]               | string    | The `items` `condition`.                                                          |
| evaluate_grouped_by_filters | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| evaluate_grouped_by_filters | value                                     | string    | The `items` `value`.                                                              |
| evaluate_grouped_by_filters | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | evaluate_grouped_by_tag_keys              | [string]  | The `strategy` `evaluate_grouped_by_tag_keys`.                                    |
| strategy                    | granularity                               | string    | The `strategy` `granularity`.                                                     |
| strategy                    | method [*required*]                  | string    | The `strategy` `method`.                                                          |
| attributes                  | type [*required*]                    | string    | The `attributes` `type`.                                                          |
| attributes                  | updated [*required*]                 | date-time | The `attributes` `updated`.                                                       |
| attributes                  | version [*required*]                 | int32     | The `attributes` `version`.                                                       |
| data                        | id                                        | string    | The `ArbitraryRuleResponseData` `id`.                                             |
| data                        | type [*required*]                    | enum      | Arbitrary rule resource type. Allowed enum values: `arbitrary_rule`               |
|                             | meta                                      | object    | The `ArbitraryRuleResponseArray` `meta`.                                          |
| meta                        | total_count                               | int64     | The `meta` `total_count`.                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "costs_to_allocate": [
          {
            "condition": "like",
            "tag": "service",
            "value": "orgstore-csm*",
            "values": null
          }
        ],
        "created": "2024-11-20T03:44:37Z",
        "enabled": true,
        "last_modified_user_uuid": "user-example-uuid",
        "order_id": 1,
        "processing_status": "done",
        "provider": [
          "gcp"
        ],
        "rule_name": "gcp-orgstore-csm-team-allocation",
        "strategy": {
          "allocated_by": [
            {
              "allocated_tags": [
                {
                  "key": "team",
                  "value": "csm-activation"
                }
              ],
              "percentage": 0.34
            },
            {
              "allocated_tags": [
                {
                  "key": "team",
                  "value": "csm-agentless"
                }
              ],
              "percentage": 0.66
            }
          ],
          "method": "percent"
        },
        "type": "shared",
        "updated": "2025-09-02T21:28:32Z",
        "version": 1
      },
      "id": "19",
      "type": "arbitrary_rule"
    },
    {
      "attributes": {
        "costs_to_allocate": [
          {
            "condition": "is",
            "tag": "env",
            "value": "staging",
            "values": null
          }
        ],
        "created": "2025-05-27T18:48:05Z",
        "enabled": true,
        "last_modified_user_uuid": "user-example-uuid-2",
        "order_id": 2,
        "processing_status": "done",
        "provider": [
          "aws"
        ],
        "rule_name": "test-even-2",
        "strategy": {
          "allocated_by_tag_keys": [
            "team"
          ],
          "based_on_costs": [
            {
              "condition": "is",
              "tag": "aws_product",
              "value": "s3",
              "values": null
            }
          ],
          "granularity": "daily",
          "method": "even"
        },
        "type": "shared",
        "updated": "2025-09-03T21:00:49Z",
        "version": 1
      },
      "id": "311",
      "type": "arbitrary_rule"
    },
    {
      "attributes": {
        "costs_to_allocate": [
          {
            "condition": "is",
            "tag": "servicename",
            "value": "s3",
            "values": null
          }
        ],
        "created": "2025-03-21T20:42:40Z",
        "enabled": false,
        "last_modified_user_uuid": "user-example-uuid-3",
        "order_id": 3,
        "processing_status": "done",
        "provider": [
          "aws"
        ],
        "rule_name": "test-s3-timeseries",
        "strategy": {
          "granularity": "daily",
          "method": "proportional_timeseries"
        },
        "type": "shared",
        "updated": "2025-09-02T21:16:50Z",
        "version": 1
      },
      "id": "289",
      "type": "arbitrary_rule"
    },
    {
      "attributes": {
        "costs_to_allocate": [
          {
            "condition": "=",
            "tag": "aws_product",
            "value": "msk",
            "values": null
          },
          {
            "condition": "is",
            "tag": "product",
            "value": "null",
            "values": null
          }
        ],
        "created": "2025-08-27T14:39:31Z",
        "enabled": true,
        "last_modified_user_uuid": "user-example-uuid-4",
        "order_id": 4,
        "processing_status": "done",
        "provider": [
          "aws"
        ],
        "rule_name": "azure-unallocated-by-product-2",
        "strategy": {
          "allocated_by_tag_keys": [
            "aws_product"
          ],
          "based_on_costs": [
            {
              "condition": "=",
              "tag": "aws_product",
              "value": "msk",
              "values": null
            },
            {
              "condition": "is not",
              "tag": "product",
              "value": "null",
              "values": null
            }
          ],
          "granularity": "daily",
          "method": "proportional"
        },
        "type": "shared",
        "updated": "2025-09-02T21:28:32Z",
        "version": 1
      },
      "id": "523",
      "type": "arbitrary_rule"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List custom allocation rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_custom_allocation_rules()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List custom allocation rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.list_custom_allocation_rules()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List custom allocation rules returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ListCustomAllocationRules(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ListCustomAllocationRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ListCustomAllocationRules`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List custom allocation rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.ArbitraryRuleResponseArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      ArbitraryRuleResponseArray result = apiInstance.listCustomAllocationRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#listCustomAllocationRules");
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
// List custom allocation rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.list_custom_allocation_rules().await;
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
 * List custom allocation rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

apiInstance
  .listCustomAllocationRules()
  .then((data: v2.ArbitraryRuleResponseArray) => {
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

## Create custom allocation rule{% #create-custom-allocation-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cost/arbitrary_rule |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cost/arbitrary_rule |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cost/arbitrary_rule      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cost/arbitrary_rule      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cost/arbitrary_rule     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cost/arbitrary_rule |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule |

### Overview



Create a new custom allocation rule with the specified filters and allocation strategy.

**Strategy Methods:**

- **PROPORTIONAL/EVEN**: Allocates costs proportionally/evenly based on existing costs. Requires: granularity, allocated_by_tag_keys. Optional: based_on_costs, allocated_by_filters, evaluate_grouped_by_tag_keys, evaluate_grouped_by_filters.
- **PROPORTIONAL\_TIMESERIES/EVEN\_TIMESERIES**: Allocates based on timeseries data. Requires: granularity, based_on_timeseries. Optional: evaluate_grouped_by_tag_keys.
- **PERCENT**: Allocates fixed percentages to specific tags. Requires: allocated_by (array of percentage allocations).

**Filter Conditions:**

- Use **value** for single-value conditions: "is", "is not", "contains", "does not contain", "=", "!=", "like", "not like", "is all values", "is untagged"
- Use **values** for multi-value conditions: "in", "not in"
- Cannot use both value and values simultaneously.

**Supported operators**: is, is not, is all values, is untagged, contains, does not contain, in, not in, =, !=, like, not like

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field                | Field                               | Type     | Description                                                                       |
| --------------------------- | ----------------------------------- | -------- | --------------------------------------------------------------------------------- |
|                             | data                                | object   | The definition of `ArbitraryCostUpsertRequestData` object.                        |
| data                        | attributes                          | object   | The definition of `ArbitraryCostUpsertRequestDataAttributes` object.              |
| attributes                  | costs_to_allocate [*required*] | [object] | The `attributes` `costs_to_allocate`.                                             |
| costs_to_allocate           | condition [*required*]         | string   | The `items` `condition`.                                                          |
| costs_to_allocate           | tag [*required*]               | string   | The `items` `tag`.                                                                |
| costs_to_allocate           | value                               | string   | The `items` `value`.                                                              |
| costs_to_allocate           | values                              | [string] | The `items` `values`.                                                             |
| attributes                  | enabled                             | boolean  | The `attributes` `enabled`.                                                       |
| attributes                  | order_id                            | int64    | The `attributes` `order_id`.                                                      |
| attributes                  | provider [*required*]          | [string] | The `attributes` `provider`.                                                      |
| attributes                  | rejected                            | boolean  | The `attributes` `rejected`.                                                      |
| attributes                  | rule_name [*required*]         | string   | The `attributes` `rule_name`.                                                     |
| attributes                  | strategy [*required*]          | object   | The definition of `ArbitraryCostUpsertRequestDataAttributesStrategy` object.      |
| strategy                    | allocated_by                        | [object] | The `strategy` `allocated_by`.                                                    |
| allocated_by                | allocated_tags [*required*]    | [object] | The `items` `allocated_tags`.                                                     |
| allocated_tags              | key [*required*]               | string   | The `items` `key`.                                                                |
| allocated_tags              | value [*required*]             | string   | The `items` `value`.                                                              |
| allocated_by                | percentage [*required*]        | double   | The `items` `percentage`. The numeric value format should be a 32bit float value. |
| strategy                    | allocated_by_filters                | [object] | The `strategy` `allocated_by_filters`.                                            |
| allocated_by_filters        | condition [*required*]         | string   | The `items` `condition`.                                                          |
| allocated_by_filters        | tag [*required*]               | string   | The `items` `tag`.                                                                |
| allocated_by_filters        | value                               | string   | The `items` `value`.                                                              |
| allocated_by_filters        | values                              | [string] | The `items` `values`.                                                             |
| strategy                    | allocated_by_tag_keys               | [string] | The `strategy` `allocated_by_tag_keys`.                                           |
| strategy                    | based_on_costs                      | [object] | The `strategy` `based_on_costs`.                                                  |
| based_on_costs              | condition [*required*]         | string   | The `items` `condition`.                                                          |
| based_on_costs              | tag [*required*]               | string   | The `items` `tag`.                                                                |
| based_on_costs              | value                               | string   | The `items` `value`.                                                              |
| based_on_costs              | values                              | [string] | The `items` `values`.                                                             |
| strategy                    | based_on_timeseries                 | object   | The `strategy` `based_on_timeseries`.                                             |
| strategy                    | evaluate_grouped_by_filters         | [object] | The `strategy` `evaluate_grouped_by_filters`.                                     |
| evaluate_grouped_by_filters | condition [*required*]         | string   | The `items` `condition`.                                                          |
| evaluate_grouped_by_filters | tag [*required*]               | string   | The `items` `tag`.                                                                |
| evaluate_grouped_by_filters | value                               | string   | The `items` `value`.                                                              |
| evaluate_grouped_by_filters | values                              | [string] | The `items` `values`.                                                             |
| strategy                    | evaluate_grouped_by_tag_keys        | [string] | The `strategy` `evaluate_grouped_by_tag_keys`.                                    |
| strategy                    | granularity                         | string   | The `strategy` `granularity`.                                                     |
| strategy                    | method [*required*]            | string   | The `strategy` `method`.                                                          |
| attributes                  | type [*required*]              | string   | The `attributes` `type`.                                                          |
| data                        | id                                  | string   | The `ArbitraryCostUpsertRequestData` `id`.                                        |
| data                        | type [*required*]              | enum     | Upsert arbitrary rule resource type. Allowed enum values: `upsert_arbitrary_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "costs_to_allocate": [
        {
          "condition": "is",
          "tag": "account_id",
          "value": "123456789"
        },
        {
          "condition": "in",
          "tag": "environment",
          "value": "",
          "values": [
            "production",
            "staging"
          ]
        }
      ],
      "enabled": true,
      "order_id": 1,
      "provider": [
        "aws",
        "gcp"
      ],
      "rule_name": "example-arbitrary-cost-rule",
      "strategy": {
        "allocated_by_tag_keys": [
          "team",
          "environment"
        ],
        "based_on_costs": [
          {
            "condition": "is",
            "tag": "service",
            "value": "web-api"
          },
          {
            "condition": "not in",
            "tag": "team",
            "value": "",
            "values": [
              "legacy",
              "deprecated"
            ]
          }
        ],
        "granularity": "daily",
        "method": "proportional"
      },
      "type": "shared"
    },
    "type": "upsert_arbitrary_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `ArbitraryRuleResponse` object.

| Parent field                | Field                                     | Type      | Description                                                                       |
| --------------------------- | ----------------------------------------- | --------- | --------------------------------------------------------------------------------- |
|                             | data                                      | object    | The definition of `ArbitraryRuleResponseData` object.                             |
| data                        | attributes                                | object    | The definition of `ArbitraryRuleResponseDataAttributes` object.                   |
| attributes                  | costs_to_allocate [*required*]       | [object]  | The `attributes` `costs_to_allocate`.                                             |
| costs_to_allocate           | condition [*required*]               | string    | The `items` `condition`.                                                          |
| costs_to_allocate           | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| costs_to_allocate           | value                                     | string    | The `items` `value`.                                                              |
| costs_to_allocate           | values                                    | [string]  | The `items` `values`.                                                             |
| attributes                  | created [*required*]                 | date-time | The `attributes` `created`.                                                       |
| attributes                  | enabled [*required*]                 | boolean   | The `attributes` `enabled`.                                                       |
| attributes                  | last_modified_user_uuid [*required*] | string    | The `attributes` `last_modified_user_uuid`.                                       |
| attributes                  | order_id [*required*]                | int64     | The `attributes` `order_id`.                                                      |
| attributes                  | processing_status                         | string    | The `attributes` `processing_status`.                                             |
| attributes                  | provider [*required*]                | [string]  | The `attributes` `provider`.                                                      |
| attributes                  | rejected                                  | boolean   | The `attributes` `rejected`.                                                      |
| attributes                  | rule_name [*required*]               | string    | The `attributes` `rule_name`.                                                     |
| attributes                  | strategy [*required*]                | object    | The definition of `ArbitraryRuleResponseDataAttributesStrategy` object.           |
| strategy                    | allocated_by                              | [object]  | The `strategy` `allocated_by`.                                                    |
| allocated_by                | allocated_tags [*required*]          | [object]  | The `items` `allocated_tags`.                                                     |
| allocated_tags              | key [*required*]                     | string    | The `items` `key`.                                                                |
| allocated_tags              | value [*required*]                   | string    | The `items` `value`.                                                              |
| allocated_by                | percentage [*required*]              | double    | The `items` `percentage`. The numeric value format should be a 32bit float value. |
| strategy                    | allocated_by_filters                      | [object]  | The `strategy` `allocated_by_filters`.                                            |
| allocated_by_filters        | condition [*required*]               | string    | The `items` `condition`.                                                          |
| allocated_by_filters        | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| allocated_by_filters        | value                                     | string    | The `items` `value`.                                                              |
| allocated_by_filters        | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | allocated_by_tag_keys                     | [string]  | The `strategy` `allocated_by_tag_keys`.                                           |
| strategy                    | based_on_costs                            | [object]  | The `strategy` `based_on_costs`.                                                  |
| based_on_costs              | condition [*required*]               | string    | The `items` `condition`.                                                          |
| based_on_costs              | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| based_on_costs              | value                                     | string    | The `items` `value`.                                                              |
| based_on_costs              | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | based_on_timeseries                       | object    | The rule `strategy` `based_on_timeseries`.                                        |
| strategy                    | evaluate_grouped_by_filters               | [object]  | The `strategy` `evaluate_grouped_by_filters`.                                     |
| evaluate_grouped_by_filters | condition [*required*]               | string    | The `items` `condition`.                                                          |
| evaluate_grouped_by_filters | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| evaluate_grouped_by_filters | value                                     | string    | The `items` `value`.                                                              |
| evaluate_grouped_by_filters | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | evaluate_grouped_by_tag_keys              | [string]  | The `strategy` `evaluate_grouped_by_tag_keys`.                                    |
| strategy                    | granularity                               | string    | The `strategy` `granularity`.                                                     |
| strategy                    | method [*required*]                  | string    | The `strategy` `method`.                                                          |
| attributes                  | type [*required*]                    | string    | The `attributes` `type`.                                                          |
| attributes                  | updated [*required*]                 | date-time | The `attributes` `updated`.                                                       |
| attributes                  | version [*required*]                 | int32     | The `attributes` `version`.                                                       |
| data                        | id                                        | string    | The `ArbitraryRuleResponseData` `id`.                                             |
| data                        | type [*required*]                    | enum      | Arbitrary rule resource type. Allowed enum values: `arbitrary_rule`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "costs_to_allocate": [
        {
          "condition": "is",
          "tag": "account_id",
          "value": "123456789",
          "values": null
        },
        {
          "condition": "in",
          "tag": "environment",
          "value": "",
          "values": [
            "production",
            "staging"
          ]
        }
      ],
      "created": "2023-01-01T12:00:00Z",
      "enabled": true,
      "last_modified_user_uuid": "user-123-uuid",
      "order_id": 1,
      "provider": [
        "aws",
        "gcp"
      ],
      "rule_name": "Example custom allocation rule",
      "strategy": {
        "allocated_by_tag_keys": [
          "team",
          "environment"
        ],
        "based_on_costs": [
          {
            "condition": "is",
            "tag": "service",
            "value": "web-api",
            "values": null
          },
          {
            "condition": "not in",
            "tag": "team",
            "value": "",
            "values": [
              "legacy",
              "deprecated"
            ]
          }
        ],
        "granularity": "daily",
        "method": "proportional"
      },
      "type": "shared",
      "updated": "2023-01-01T12:00:00Z",
      "version": 1
    },
    "id": "123",
    "type": "arbitrary_rule"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "costs_to_allocate": [
        {
          "condition": "is",
          "tag": "account_id",
          "value": "123456789"
        },
        {
          "condition": "in",
          "tag": "environment",
          "value": "",
          "values": [
            "production",
            "staging"
          ]
        }
      ],
      "enabled": true,
      "order_id": 1,
      "provider": [
        "aws",
        "gcp"
      ],
      "rule_name": "example-arbitrary-cost-rule",
      "strategy": {
        "allocated_by_tag_keys": [
          "team",
          "environment"
        ],
        "based_on_costs": [
          {
            "condition": "is",
            "tag": "service",
            "value": "web-api"
          },
          {
            "condition": "not in",
            "tag": "team",
            "value": "",
            "values": [
              "legacy",
              "deprecated"
            ]
          }
        ],
        "granularity": "daily",
        "method": "proportional"
      },
      "type": "shared"
    },
    "type": "upsert_arbitrary_rule"
  }
}
EOF
                        
##### 

```go
// Create custom allocation rule returns "OK" response

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
	body := datadogV2.ArbitraryCostUpsertRequest{
		Data: &datadogV2.ArbitraryCostUpsertRequestData{
			Attributes: &datadogV2.ArbitraryCostUpsertRequestDataAttributes{
				CostsToAllocate: []datadogV2.ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems{
					{
						Condition: "is",
						Tag:       "account_id",
						Value:     datadog.PtrString("123456789"),
					},
					{
						Condition: "in",
						Tag:       "environment",
						Value:     datadog.PtrString(""),
						Values: *datadog.NewNullableList(&[]string{
							"production",
							"staging",
						}),
					},
				},
				Enabled: datadog.PtrBool(true),
				OrderId: datadog.PtrInt64(1),
				Provider: []string{
					"aws",
					"gcp",
				},
				RuleName: "example-arbitrary-cost-rule",
				Strategy: datadogV2.ArbitraryCostUpsertRequestDataAttributesStrategy{
					AllocatedByTagKeys: []string{
						"team",
						"environment",
					},
					BasedOnCosts: []datadogV2.ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems{
						{
							Condition: "is",
							Tag:       "service",
							Value:     datadog.PtrString("web-api"),
						},
						{
							Condition: "not in",
							Tag:       "team",
							Value:     datadog.PtrString(""),
							Values: *datadog.NewNullableList(&[]string{
								"legacy",
								"deprecated",
							}),
						},
					},
					Granularity: datadog.PtrString("daily"),
					Method:      "proportional",
				},
				Type: "shared",
			},
			Type: datadogV2.ARBITRARYCOSTUPSERTREQUESTDATATYPE_UPSERT_ARBITRARY_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.CreateCustomAllocationRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.CreateCustomAllocationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.CreateCustomAllocationRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create custom allocation rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequest;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestData;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributes;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributesStrategy;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataType;
import com.datadog.api.client.v2.model.ArbitraryRuleResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    ArbitraryCostUpsertRequest body =
        new ArbitraryCostUpsertRequest()
            .data(
                new ArbitraryCostUpsertRequestData()
                    .attributes(
                        new ArbitraryCostUpsertRequestDataAttributes()
                            .costsToAllocate(
                                Arrays.asList(
                                    new ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems()
                                        .condition("is")
                                        .tag("account_id")
                                        .value("123456789"),
                                    new ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems()
                                        .condition("in")
                                        .tag("environment")
                                        .value("")
                                        .values(Arrays.asList("production", "staging"))))
                            .enabled(true)
                            .orderId(1L)
                            .provider(Arrays.asList("aws", "gcp"))
                            .ruleName("example-arbitrary-cost-rule")
                            .strategy(
                                new ArbitraryCostUpsertRequestDataAttributesStrategy()
                                    .allocatedByTagKeys(Arrays.asList("team", "environment"))
                                    .basedOnCosts(
                                        Arrays.asList(
                                            new ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems()
                                                .condition("is")
                                                .tag("service")
                                                .value("web-api"),
                                            new ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems()
                                                .condition("not in")
                                                .tag("team")
                                                .value("")
                                                .values(Arrays.asList("legacy", "deprecated"))))
                                    .granularity("daily")
                                    .method("proportional"))
                            .type("shared"))
                    .type(ArbitraryCostUpsertRequestDataType.UPSERT_ARBITRARY_RULE));

    try {
      ArbitraryRuleResponse result = apiInstance.createCustomAllocationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#createCustomAllocationRule");
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

```python
"""
Create custom allocation rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.arbitrary_cost_upsert_request import ArbitraryCostUpsertRequest
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data import ArbitraryCostUpsertRequestData
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes import (
    ArbitraryCostUpsertRequestDataAttributes,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_costs_to_allocate_items import (
    ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy import (
    ArbitraryCostUpsertRequestDataAttributesStrategy,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy_based_on_costs_items import (
    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_type import ArbitraryCostUpsertRequestDataType

body = ArbitraryCostUpsertRequest(
    data=ArbitraryCostUpsertRequestData(
        attributes=ArbitraryCostUpsertRequestDataAttributes(
            costs_to_allocate=[
                ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems(
                    condition="is",
                    tag="account_id",
                    value="123456789",
                ),
                ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems(
                    condition="in",
                    tag="environment",
                    value="",
                    values=[
                        "production",
                        "staging",
                    ],
                ),
            ],
            enabled=True,
            order_id=1,
            provider=[
                "aws",
                "gcp",
            ],
            rule_name="example-arbitrary-cost-rule",
            strategy=ArbitraryCostUpsertRequestDataAttributesStrategy(
                allocated_by_tag_keys=[
                    "team",
                    "environment",
                ],
                based_on_costs=[
                    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems(
                        condition="is",
                        tag="service",
                        value="web-api",
                    ),
                    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems(
                        condition="not in",
                        tag="team",
                        value="",
                        values=[
                            "legacy",
                            "deprecated",
                        ],
                    ),
                ],
                granularity="daily",
                method="proportional",
            ),
            type="shared",
        ),
        type=ArbitraryCostUpsertRequestDataType.UPSERT_ARBITRARY_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_custom_allocation_rule(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create custom allocation rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::ArbitraryCostUpsertRequest.new({
  data: DatadogAPIClient::V2::ArbitraryCostUpsertRequestData.new({
    attributes: DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributes.new({
      costs_to_allocate: [
        DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems.new({
          condition: "is",
          tag: "account_id",
          value: "123456789",
        }),
        DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems.new({
          condition: "in",
          tag: "environment",
          value: "",
          values: [
            "production",
            "staging",
          ],
        }),
      ],
      enabled: true,
      order_id: 1,
      provider: [
        "aws",
        "gcp",
      ],
      rule_name: "example-arbitrary-cost-rule",
      strategy: DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesStrategy.new({
        allocated_by_tag_keys: [
          "team",
          "environment",
        ],
        based_on_costs: [
          DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems.new({
            condition: "is",
            tag: "service",
            value: "web-api",
          }),
          DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems.new({
            condition: "not in",
            tag: "team",
            value: "",
            values: [
              "legacy",
              "deprecated",
            ],
          }),
        ],
        granularity: "daily",
        method: "proportional",
      }),
      type: "shared",
    }),
    type: DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataType::UPSERT_ARBITRARY_RULE,
  }),
})
p api_instance.create_custom_allocation_rule(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create custom allocation rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequest;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestData;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributes;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributesStrategy;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataType;

#[tokio::main]
async fn main() {
    let body = ArbitraryCostUpsertRequest::new().data(
        ArbitraryCostUpsertRequestData::new(
            ArbitraryCostUpsertRequestDataType::UPSERT_ARBITRARY_RULE,
        )
        .attributes(
            ArbitraryCostUpsertRequestDataAttributes::new(
                vec![
                    ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems::new(
                        "is".to_string(),
                        "account_id".to_string(),
                    )
                    .value("123456789".to_string()),
                    ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems::new(
                        "in".to_string(),
                        "environment".to_string(),
                    )
                    .value("".to_string())
                    .values(Some(vec!["production".to_string(), "staging".to_string()])),
                ],
                vec!["aws".to_string(), "gcp".to_string()],
                "example-arbitrary-cost-rule".to_string(),
                ArbitraryCostUpsertRequestDataAttributesStrategy::new("proportional".to_string())
                    .allocated_by_tag_keys(vec!["team".to_string(), "environment".to_string()])
                    .based_on_costs(vec![
                        ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems::new(
                            "is".to_string(),
                            "service".to_string(),
                        )
                        .value("web-api".to_string()),
                        ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems::new(
                            "not in".to_string(),
                            "team".to_string(),
                        )
                        .value("".to_string())
                        .values(Some(vec!["legacy".to_string(), "deprecated".to_string()])),
                    ])
                    .granularity("daily".to_string()),
                "shared".to_string(),
            )
            .enabled(true)
            .order_id(1),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.create_custom_allocation_rule(body).await;
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
 * Create custom allocation rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiCreateCustomAllocationRuleRequest = {
  body: {
    data: {
      attributes: {
        costsToAllocate: [
          {
            condition: "is",
            tag: "account_id",
            value: "123456789",
          },
          {
            condition: "in",
            tag: "environment",
            value: "",
            values: ["production", "staging"],
          },
        ],
        enabled: true,
        orderId: 1,
        provider: ["aws", "gcp"],
        ruleName: "example-arbitrary-cost-rule",
        strategy: {
          allocatedByTagKeys: ["team", "environment"],
          basedOnCosts: [
            {
              condition: "is",
              tag: "service",
              value: "web-api",
            },
            {
              condition: "not in",
              tag: "team",
              value: "",
              values: ["legacy", "deprecated"],
            },
          ],
          granularity: "daily",
          method: "proportional",
        },
        type: "shared",
      },
      type: "upsert_arbitrary_rule",
    },
  },
};

apiInstance
  .createCustomAllocationRule(params)
  .then((data: v2.ArbitraryRuleResponse) => {
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

## Update custom allocation rule{% #update-custom-allocation-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/cost/arbitrary_rule/{rule_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/cost/arbitrary_rule/{rule_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |

### Overview



Update an existing custom allocation rule with new filters and allocation strategy.

**Strategy Methods:**

- **PROPORTIONAL/EVEN**: Allocates costs proportionally/evenly based on existing costs. Requires: granularity, allocated_by_tag_keys. Optional: based_on_costs, allocated_by_filters, evaluate_grouped_by_tag_keys, evaluate_grouped_by_filters.
- **PROPORTIONAL\_TIMESERIES/EVEN\_TIMESERIES**: Allocates based on timeseries data. Requires: granularity, based_on_timeseries. Optional: evaluate_grouped_by_tag_keys.
- **PERCENT**: Allocates fixed percentages to specific tags. Requires: allocated_by (array of percentage allocations).
- **USAGE\_METRIC**: Allocates based on usage metrics (implementation varies).

**Filter Conditions:**

- Use **value** for single-value conditions: "is", "is not", "contains", "does not contain", "=", "!=", "like", "not like", "is all values", "is untagged"
- Use **values** for multi-value conditions: "in", "not in"
- Cannot use both value and values simultaneously.

**Supported operators**: is, is not, is all values, is untagged, contains, does not contain, in, not in, =, !=, like, not like

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type    | Description                                         |
| ------------------------- | ------- | --------------------------------------------------- |
| rule_id [*required*] | integer | The unique identifier of the custom allocation rule |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field                | Field                               | Type     | Description                                                                       |
| --------------------------- | ----------------------------------- | -------- | --------------------------------------------------------------------------------- |
|                             | data                                | object   | The definition of `ArbitraryCostUpsertRequestData` object.                        |
| data                        | attributes                          | object   | The definition of `ArbitraryCostUpsertRequestDataAttributes` object.              |
| attributes                  | costs_to_allocate [*required*] | [object] | The `attributes` `costs_to_allocate`.                                             |
| costs_to_allocate           | condition [*required*]         | string   | The `items` `condition`.                                                          |
| costs_to_allocate           | tag [*required*]               | string   | The `items` `tag`.                                                                |
| costs_to_allocate           | value                               | string   | The `items` `value`.                                                              |
| costs_to_allocate           | values                              | [string] | The `items` `values`.                                                             |
| attributes                  | enabled                             | boolean  | The `attributes` `enabled`.                                                       |
| attributes                  | order_id                            | int64    | The `attributes` `order_id`.                                                      |
| attributes                  | provider [*required*]          | [string] | The `attributes` `provider`.                                                      |
| attributes                  | rejected                            | boolean  | The `attributes` `rejected`.                                                      |
| attributes                  | rule_name [*required*]         | string   | The `attributes` `rule_name`.                                                     |
| attributes                  | strategy [*required*]          | object   | The definition of `ArbitraryCostUpsertRequestDataAttributesStrategy` object.      |
| strategy                    | allocated_by                        | [object] | The `strategy` `allocated_by`.                                                    |
| allocated_by                | allocated_tags [*required*]    | [object] | The `items` `allocated_tags`.                                                     |
| allocated_tags              | key [*required*]               | string   | The `items` `key`.                                                                |
| allocated_tags              | value [*required*]             | string   | The `items` `value`.                                                              |
| allocated_by                | percentage [*required*]        | double   | The `items` `percentage`. The numeric value format should be a 32bit float value. |
| strategy                    | allocated_by_filters                | [object] | The `strategy` `allocated_by_filters`.                                            |
| allocated_by_filters        | condition [*required*]         | string   | The `items` `condition`.                                                          |
| allocated_by_filters        | tag [*required*]               | string   | The `items` `tag`.                                                                |
| allocated_by_filters        | value                               | string   | The `items` `value`.                                                              |
| allocated_by_filters        | values                              | [string] | The `items` `values`.                                                             |
| strategy                    | allocated_by_tag_keys               | [string] | The `strategy` `allocated_by_tag_keys`.                                           |
| strategy                    | based_on_costs                      | [object] | The `strategy` `based_on_costs`.                                                  |
| based_on_costs              | condition [*required*]         | string   | The `items` `condition`.                                                          |
| based_on_costs              | tag [*required*]               | string   | The `items` `tag`.                                                                |
| based_on_costs              | value                               | string   | The `items` `value`.                                                              |
| based_on_costs              | values                              | [string] | The `items` `values`.                                                             |
| strategy                    | based_on_timeseries                 | object   | The `strategy` `based_on_timeseries`.                                             |
| strategy                    | evaluate_grouped_by_filters         | [object] | The `strategy` `evaluate_grouped_by_filters`.                                     |
| evaluate_grouped_by_filters | condition [*required*]         | string   | The `items` `condition`.                                                          |
| evaluate_grouped_by_filters | tag [*required*]               | string   | The `items` `tag`.                                                                |
| evaluate_grouped_by_filters | value                               | string   | The `items` `value`.                                                              |
| evaluate_grouped_by_filters | values                              | [string] | The `items` `values`.                                                             |
| strategy                    | evaluate_grouped_by_tag_keys        | [string] | The `strategy` `evaluate_grouped_by_tag_keys`.                                    |
| strategy                    | granularity                         | string   | The `strategy` `granularity`.                                                     |
| strategy                    | method [*required*]            | string   | The `strategy` `method`.                                                          |
| attributes                  | type [*required*]              | string   | The `attributes` `type`.                                                          |
| data                        | id                                  | string   | The `ArbitraryCostUpsertRequestData` `id`.                                        |
| data                        | type [*required*]              | enum     | Upsert arbitrary rule resource type. Allowed enum values: `upsert_arbitrary_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "costs_to_allocate": [
        {
          "condition": "is",
          "tag": "account_id",
          "value": "123456789",
          "values": []
        },
        {
          "condition": "in",
          "tag": "environment",
          "value": "",
          "values": [
            "production",
            "staging"
          ]
        }
      ],
      "enabled": true,
      "order_id": 1,
      "provider": [
        "aws",
        "gcp"
      ],
      "rule_name": "example-arbitrary-cost-rule",
      "strategy": {
        "allocated_by_tag_keys": [
          "team",
          "environment"
        ],
        "based_on_costs": [
          {
            "condition": "is",
            "tag": "service",
            "value": "web-api",
            "values": []
          },
          {
            "condition": "not in",
            "tag": "team",
            "value": "",
            "values": [
              "legacy",
              "deprecated"
            ]
          }
        ],
        "granularity": "daily",
        "method": "proportional"
      },
      "type": "shared"
    },
    "type": "upsert_arbitrary_rule"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `ArbitraryRuleResponse` object.

| Parent field                | Field                                     | Type      | Description                                                                       |
| --------------------------- | ----------------------------------------- | --------- | --------------------------------------------------------------------------------- |
|                             | data                                      | object    | The definition of `ArbitraryRuleResponseData` object.                             |
| data                        | attributes                                | object    | The definition of `ArbitraryRuleResponseDataAttributes` object.                   |
| attributes                  | costs_to_allocate [*required*]       | [object]  | The `attributes` `costs_to_allocate`.                                             |
| costs_to_allocate           | condition [*required*]               | string    | The `items` `condition`.                                                          |
| costs_to_allocate           | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| costs_to_allocate           | value                                     | string    | The `items` `value`.                                                              |
| costs_to_allocate           | values                                    | [string]  | The `items` `values`.                                                             |
| attributes                  | created [*required*]                 | date-time | The `attributes` `created`.                                                       |
| attributes                  | enabled [*required*]                 | boolean   | The `attributes` `enabled`.                                                       |
| attributes                  | last_modified_user_uuid [*required*] | string    | The `attributes` `last_modified_user_uuid`.                                       |
| attributes                  | order_id [*required*]                | int64     | The `attributes` `order_id`.                                                      |
| attributes                  | processing_status                         | string    | The `attributes` `processing_status`.                                             |
| attributes                  | provider [*required*]                | [string]  | The `attributes` `provider`.                                                      |
| attributes                  | rejected                                  | boolean   | The `attributes` `rejected`.                                                      |
| attributes                  | rule_name [*required*]               | string    | The `attributes` `rule_name`.                                                     |
| attributes                  | strategy [*required*]                | object    | The definition of `ArbitraryRuleResponseDataAttributesStrategy` object.           |
| strategy                    | allocated_by                              | [object]  | The `strategy` `allocated_by`.                                                    |
| allocated_by                | allocated_tags [*required*]          | [object]  | The `items` `allocated_tags`.                                                     |
| allocated_tags              | key [*required*]                     | string    | The `items` `key`.                                                                |
| allocated_tags              | value [*required*]                   | string    | The `items` `value`.                                                              |
| allocated_by                | percentage [*required*]              | double    | The `items` `percentage`. The numeric value format should be a 32bit float value. |
| strategy                    | allocated_by_filters                      | [object]  | The `strategy` `allocated_by_filters`.                                            |
| allocated_by_filters        | condition [*required*]               | string    | The `items` `condition`.                                                          |
| allocated_by_filters        | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| allocated_by_filters        | value                                     | string    | The `items` `value`.                                                              |
| allocated_by_filters        | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | allocated_by_tag_keys                     | [string]  | The `strategy` `allocated_by_tag_keys`.                                           |
| strategy                    | based_on_costs                            | [object]  | The `strategy` `based_on_costs`.                                                  |
| based_on_costs              | condition [*required*]               | string    | The `items` `condition`.                                                          |
| based_on_costs              | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| based_on_costs              | value                                     | string    | The `items` `value`.                                                              |
| based_on_costs              | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | based_on_timeseries                       | object    | The rule `strategy` `based_on_timeseries`.                                        |
| strategy                    | evaluate_grouped_by_filters               | [object]  | The `strategy` `evaluate_grouped_by_filters`.                                     |
| evaluate_grouped_by_filters | condition [*required*]               | string    | The `items` `condition`.                                                          |
| evaluate_grouped_by_filters | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| evaluate_grouped_by_filters | value                                     | string    | The `items` `value`.                                                              |
| evaluate_grouped_by_filters | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | evaluate_grouped_by_tag_keys              | [string]  | The `strategy` `evaluate_grouped_by_tag_keys`.                                    |
| strategy                    | granularity                               | string    | The `strategy` `granularity`.                                                     |
| strategy                    | method [*required*]                  | string    | The `strategy` `method`.                                                          |
| attributes                  | type [*required*]                    | string    | The `attributes` `type`.                                                          |
| attributes                  | updated [*required*]                 | date-time | The `attributes` `updated`.                                                       |
| attributes                  | version [*required*]                 | int32     | The `attributes` `version`.                                                       |
| data                        | id                                        | string    | The `ArbitraryRuleResponseData` `id`.                                             |
| data                        | type [*required*]                    | enum      | Arbitrary rule resource type. Allowed enum values: `arbitrary_rule`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "costs_to_allocate": [
        {
          "condition": "is",
          "tag": "account_id",
          "value": "123456789",
          "values": null
        },
        {
          "condition": "in",
          "tag": "environment",
          "value": "",
          "values": [
            "production",
            "staging"
          ]
        }
      ],
      "created": "2023-01-01T12:00:00Z",
      "enabled": true,
      "last_modified_user_uuid": "user-123-uuid",
      "order_id": 1,
      "provider": [
        "aws",
        "gcp"
      ],
      "rule_name": "Example custom allocation rule",
      "strategy": {
        "allocated_by_tag_keys": [
          "team",
          "environment"
        ],
        "based_on_costs": [
          {
            "condition": "is",
            "tag": "service",
            "value": "web-api",
            "values": null
          },
          {
            "condition": "not in",
            "tag": "team",
            "value": "",
            "values": [
              "legacy",
              "deprecated"
            ]
          }
        ],
        "granularity": "daily",
        "method": "proportional"
      },
      "type": "shared",
      "updated": "2023-01-01T12:00:00Z",
      "version": 1
    },
    "id": "123",
    "type": "arbitrary_rule"
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
                          \# Path parametersexport rule_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "costs_to_allocate": [
        {
          "condition": "is",
          "tag": "account_id",
          "value": "123456789",
          "values": []
        },
        {
          "condition": "in",
          "tag": "environment",
          "value": "",
          "values": [
            "production",
            "staging"
          ]
        }
      ],
      "enabled": true,
      "order_id": 1,
      "provider": [
        "aws",
        "gcp"
      ],
      "rule_name": "example-arbitrary-cost-rule",
      "strategy": {
        "allocated_by_tag_keys": [
          "team",
          "environment"
        ],
        "based_on_costs": [
          {
            "condition": "is",
            "tag": "service",
            "value": "web-api",
            "values": []
          },
          {
            "condition": "not in",
            "tag": "team",
            "value": "",
            "values": [
              "legacy",
              "deprecated"
            ]
          }
        ],
        "granularity": "daily",
        "method": "proportional"
      },
      "type": "shared"
    },
    "type": "upsert_arbitrary_rule"
  }
}
EOF
                        
##### 

```go
// Update custom allocation rule returns "OK" response

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
	body := datadogV2.ArbitraryCostUpsertRequest{
		Data: &datadogV2.ArbitraryCostUpsertRequestData{
			Attributes: &datadogV2.ArbitraryCostUpsertRequestDataAttributes{
				CostsToAllocate: []datadogV2.ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems{
					{
						Condition: "is",
						Tag:       "account_id",
						Value:     datadog.PtrString("123456789"),
						Values:    *datadog.NewNullableList(&[]string{}),
					},
					{
						Condition: "in",
						Tag:       "environment",
						Value:     datadog.PtrString(""),
						Values: *datadog.NewNullableList(&[]string{
							"production",
							"staging",
						}),
					},
				},
				Enabled: datadog.PtrBool(true),
				OrderId: datadog.PtrInt64(1),
				Provider: []string{
					"aws",
					"gcp",
				},
				RuleName: "example-arbitrary-cost-rule",
				Strategy: datadogV2.ArbitraryCostUpsertRequestDataAttributesStrategy{
					AllocatedByTagKeys: []string{
						"team",
						"environment",
					},
					BasedOnCosts: []datadogV2.ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems{
						{
							Condition: "is",
							Tag:       "service",
							Value:     datadog.PtrString("web-api"),
							Values:    *datadog.NewNullableList(&[]string{}),
						},
						{
							Condition: "not in",
							Tag:       "team",
							Value:     datadog.PtrString(""),
							Values: *datadog.NewNullableList(&[]string{
								"legacy",
								"deprecated",
							}),
						},
					},
					Granularity: datadog.PtrString("daily"),
					Method:      "proportional",
				},
				Type: "shared",
			},
			Type: datadogV2.ARBITRARYCOSTUPSERTREQUESTDATATYPE_UPSERT_ARBITRARY_RULE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.UpdateCustomAllocationRule(ctx, 683, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.UpdateCustomAllocationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.UpdateCustomAllocationRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update custom allocation rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequest;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestData;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributes;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributesStrategy;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems;
import com.datadog.api.client.v2.model.ArbitraryCostUpsertRequestDataType;
import com.datadog.api.client.v2.model.ArbitraryRuleResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    ArbitraryCostUpsertRequest body =
        new ArbitraryCostUpsertRequest()
            .data(
                new ArbitraryCostUpsertRequestData()
                    .attributes(
                        new ArbitraryCostUpsertRequestDataAttributes()
                            .costsToAllocate(
                                Arrays.asList(
                                    new ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems()
                                        .condition("is")
                                        .tag("account_id")
                                        .value("123456789"),
                                    new ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems()
                                        .condition("in")
                                        .tag("environment")
                                        .value("")
                                        .values(Arrays.asList("production", "staging"))))
                            .enabled(true)
                            .orderId(1L)
                            .provider(Arrays.asList("aws", "gcp"))
                            .ruleName("example-arbitrary-cost-rule")
                            .strategy(
                                new ArbitraryCostUpsertRequestDataAttributesStrategy()
                                    .allocatedByTagKeys(Arrays.asList("team", "environment"))
                                    .basedOnCosts(
                                        Arrays.asList(
                                            new ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems()
                                                .condition("is")
                                                .tag("service")
                                                .value("web-api"),
                                            new ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems()
                                                .condition("not in")
                                                .tag("team")
                                                .value("")
                                                .values(Arrays.asList("legacy", "deprecated"))))
                                    .granularity("daily")
                                    .method("proportional"))
                            .type("shared"))
                    .type(ArbitraryCostUpsertRequestDataType.UPSERT_ARBITRARY_RULE));

    try {
      ArbitraryRuleResponse result = apiInstance.updateCustomAllocationRule(683L, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#updateCustomAllocationRule");
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

```python
"""
Update custom allocation rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.arbitrary_cost_upsert_request import ArbitraryCostUpsertRequest
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data import ArbitraryCostUpsertRequestData
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes import (
    ArbitraryCostUpsertRequestDataAttributes,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_costs_to_allocate_items import (
    ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy import (
    ArbitraryCostUpsertRequestDataAttributesStrategy,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy_based_on_costs_items import (
    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_type import ArbitraryCostUpsertRequestDataType

body = ArbitraryCostUpsertRequest(
    data=ArbitraryCostUpsertRequestData(
        attributes=ArbitraryCostUpsertRequestDataAttributes(
            costs_to_allocate=[
                ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems(
                    condition="is",
                    tag="account_id",
                    value="123456789",
                    values=[],
                ),
                ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems(
                    condition="in",
                    tag="environment",
                    value="",
                    values=[
                        "production",
                        "staging",
                    ],
                ),
            ],
            enabled=True,
            order_id=1,
            provider=[
                "aws",
                "gcp",
            ],
            rule_name="example-arbitrary-cost-rule",
            strategy=ArbitraryCostUpsertRequestDataAttributesStrategy(
                allocated_by_tag_keys=[
                    "team",
                    "environment",
                ],
                based_on_costs=[
                    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems(
                        condition="is",
                        tag="service",
                        value="web-api",
                        values=[],
                    ),
                    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems(
                        condition="not in",
                        tag="team",
                        value="",
                        values=[
                            "legacy",
                            "deprecated",
                        ],
                    ),
                ],
                granularity="daily",
                method="proportional",
            ),
            type="shared",
        ),
        type=ArbitraryCostUpsertRequestDataType.UPSERT_ARBITRARY_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_custom_allocation_rule(rule_id=683, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update custom allocation rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::ArbitraryCostUpsertRequest.new({
  data: DatadogAPIClient::V2::ArbitraryCostUpsertRequestData.new({
    attributes: DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributes.new({
      costs_to_allocate: [
        DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems.new({
          condition: "is",
          tag: "account_id",
          value: "123456789",
          values: [],
        }),
        DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems.new({
          condition: "in",
          tag: "environment",
          value: "",
          values: [
            "production",
            "staging",
          ],
        }),
      ],
      enabled: true,
      order_id: 1,
      provider: [
        "aws",
        "gcp",
      ],
      rule_name: "example-arbitrary-cost-rule",
      strategy: DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesStrategy.new({
        allocated_by_tag_keys: [
          "team",
          "environment",
        ],
        based_on_costs: [
          DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems.new({
            condition: "is",
            tag: "service",
            value: "web-api",
            values: [],
          }),
          DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems.new({
            condition: "not in",
            tag: "team",
            value: "",
            values: [
              "legacy",
              "deprecated",
            ],
          }),
        ],
        granularity: "daily",
        method: "proportional",
      }),
      type: "shared",
    }),
    type: DatadogAPIClient::V2::ArbitraryCostUpsertRequestDataType::UPSERT_ARBITRARY_RULE,
  }),
})
p api_instance.update_custom_allocation_rule(683, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update custom allocation rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequest;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestData;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributes;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributesStrategy;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems;
use datadog_api_client::datadogV2::model::ArbitraryCostUpsertRequestDataType;

#[tokio::main]
async fn main() {
    let body = ArbitraryCostUpsertRequest::new().data(
        ArbitraryCostUpsertRequestData::new(
            ArbitraryCostUpsertRequestDataType::UPSERT_ARBITRARY_RULE,
        )
        .attributes(
            ArbitraryCostUpsertRequestDataAttributes::new(
                vec![
                    ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems::new(
                        "is".to_string(),
                        "account_id".to_string(),
                    )
                    .value("123456789".to_string())
                    .values(Some(vec![])),
                    ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems::new(
                        "in".to_string(),
                        "environment".to_string(),
                    )
                    .value("".to_string())
                    .values(Some(vec!["production".to_string(), "staging".to_string()])),
                ],
                vec!["aws".to_string(), "gcp".to_string()],
                "example-arbitrary-cost-rule".to_string(),
                ArbitraryCostUpsertRequestDataAttributesStrategy::new("proportional".to_string())
                    .allocated_by_tag_keys(vec!["team".to_string(), "environment".to_string()])
                    .based_on_costs(vec![
                        ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems::new(
                            "is".to_string(),
                            "service".to_string(),
                        )
                        .value("web-api".to_string())
                        .values(Some(vec![])),
                        ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems::new(
                            "not in".to_string(),
                            "team".to_string(),
                        )
                        .value("".to_string())
                        .values(Some(vec!["legacy".to_string(), "deprecated".to_string()])),
                    ])
                    .granularity("daily".to_string()),
                "shared".to_string(),
            )
            .enabled(true)
            .order_id(1),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.update_custom_allocation_rule(683, body).await;
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
 * Update custom allocation rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiUpdateCustomAllocationRuleRequest = {
  body: {
    data: {
      attributes: {
        costsToAllocate: [
          {
            condition: "is",
            tag: "account_id",
            value: "123456789",
            values: [],
          },
          {
            condition: "in",
            tag: "environment",
            value: "",
            values: ["production", "staging"],
          },
        ],
        enabled: true,
        orderId: 1,
        provider: ["aws", "gcp"],
        ruleName: "example-arbitrary-cost-rule",
        strategy: {
          allocatedByTagKeys: ["team", "environment"],
          basedOnCosts: [
            {
              condition: "is",
              tag: "service",
              value: "web-api",
              values: [],
            },
            {
              condition: "not in",
              tag: "team",
              value: "",
              values: ["legacy", "deprecated"],
            },
          ],
          granularity: "daily",
          method: "proportional",
        },
        type: "shared",
      },
      type: "upsert_arbitrary_rule",
    },
  },
  ruleId: 683,
};

apiInstance
  .updateCustomAllocationRule(params)
  .then((data: v2.ArbitraryRuleResponse) => {
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

## Delete custom allocation rule{% #delete-custom-allocation-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cost/arbitrary_rule/{rule_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cost/arbitrary_rule/{rule_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |

### Overview

Delete a custom allocation rule - Delete an existing custom allocation rule by its ID

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type    | Description                                         |
| ------------------------- | ------- | --------------------------------------------------- |
| rule_id [*required*] | integer | The unique identifier of the custom allocation rule |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport rule_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/${rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete custom allocation rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_custom_allocation_rule(
        rule_id=683,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete custom allocation rule returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
api_instance.delete_custom_allocation_rule(683)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete custom allocation rule returns "No Content" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.DeleteCustomAllocationRule(ctx, 683)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.DeleteCustomAllocationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete custom allocation rule returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      apiInstance.deleteCustomAllocationRule(683L);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#deleteCustomAllocationRule");
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
// Delete custom allocation rule returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.delete_custom_allocation_rule(683).await;
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
 * Delete custom allocation rule returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiDeleteCustomAllocationRuleRequest = {
  ruleId: 683,
};

apiInstance
  .deleteCustomAllocationRule(params)
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

## Get custom allocation rule{% #get-custom-allocation-rule %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/arbitrary_rule/{rule_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/arbitrary_rule/{rule_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/{rule_id} |

### Overview

Get a specific custom allocation rule - Retrieve a specific custom allocation rule by its ID

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type    | Description                                         |
| ------------------------- | ------- | --------------------------------------------------- |
| rule_id [*required*] | integer | The unique identifier of the custom allocation rule |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of `ArbitraryRuleResponse` object.

| Parent field                | Field                                     | Type      | Description                                                                       |
| --------------------------- | ----------------------------------------- | --------- | --------------------------------------------------------------------------------- |
|                             | data                                      | object    | The definition of `ArbitraryRuleResponseData` object.                             |
| data                        | attributes                                | object    | The definition of `ArbitraryRuleResponseDataAttributes` object.                   |
| attributes                  | costs_to_allocate [*required*]       | [object]  | The `attributes` `costs_to_allocate`.                                             |
| costs_to_allocate           | condition [*required*]               | string    | The `items` `condition`.                                                          |
| costs_to_allocate           | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| costs_to_allocate           | value                                     | string    | The `items` `value`.                                                              |
| costs_to_allocate           | values                                    | [string]  | The `items` `values`.                                                             |
| attributes                  | created [*required*]                 | date-time | The `attributes` `created`.                                                       |
| attributes                  | enabled [*required*]                 | boolean   | The `attributes` `enabled`.                                                       |
| attributes                  | last_modified_user_uuid [*required*] | string    | The `attributes` `last_modified_user_uuid`.                                       |
| attributes                  | order_id [*required*]                | int64     | The `attributes` `order_id`.                                                      |
| attributes                  | processing_status                         | string    | The `attributes` `processing_status`.                                             |
| attributes                  | provider [*required*]                | [string]  | The `attributes` `provider`.                                                      |
| attributes                  | rejected                                  | boolean   | The `attributes` `rejected`.                                                      |
| attributes                  | rule_name [*required*]               | string    | The `attributes` `rule_name`.                                                     |
| attributes                  | strategy [*required*]                | object    | The definition of `ArbitraryRuleResponseDataAttributesStrategy` object.           |
| strategy                    | allocated_by                              | [object]  | The `strategy` `allocated_by`.                                                    |
| allocated_by                | allocated_tags [*required*]          | [object]  | The `items` `allocated_tags`.                                                     |
| allocated_tags              | key [*required*]                     | string    | The `items` `key`.                                                                |
| allocated_tags              | value [*required*]                   | string    | The `items` `value`.                                                              |
| allocated_by                | percentage [*required*]              | double    | The `items` `percentage`. The numeric value format should be a 32bit float value. |
| strategy                    | allocated_by_filters                      | [object]  | The `strategy` `allocated_by_filters`.                                            |
| allocated_by_filters        | condition [*required*]               | string    | The `items` `condition`.                                                          |
| allocated_by_filters        | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| allocated_by_filters        | value                                     | string    | The `items` `value`.                                                              |
| allocated_by_filters        | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | allocated_by_tag_keys                     | [string]  | The `strategy` `allocated_by_tag_keys`.                                           |
| strategy                    | based_on_costs                            | [object]  | The `strategy` `based_on_costs`.                                                  |
| based_on_costs              | condition [*required*]               | string    | The `items` `condition`.                                                          |
| based_on_costs              | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| based_on_costs              | value                                     | string    | The `items` `value`.                                                              |
| based_on_costs              | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | based_on_timeseries                       | object    | The rule `strategy` `based_on_timeseries`.                                        |
| strategy                    | evaluate_grouped_by_filters               | [object]  | The `strategy` `evaluate_grouped_by_filters`.                                     |
| evaluate_grouped_by_filters | condition [*required*]               | string    | The `items` `condition`.                                                          |
| evaluate_grouped_by_filters | tag [*required*]                     | string    | The `items` `tag`.                                                                |
| evaluate_grouped_by_filters | value                                     | string    | The `items` `value`.                                                              |
| evaluate_grouped_by_filters | values                                    | [string]  | The `items` `values`.                                                             |
| strategy                    | evaluate_grouped_by_tag_keys              | [string]  | The `strategy` `evaluate_grouped_by_tag_keys`.                                    |
| strategy                    | granularity                               | string    | The `strategy` `granularity`.                                                     |
| strategy                    | method [*required*]                  | string    | The `strategy` `method`.                                                          |
| attributes                  | type [*required*]                    | string    | The `attributes` `type`.                                                          |
| attributes                  | updated [*required*]                 | date-time | The `attributes` `updated`.                                                       |
| attributes                  | version [*required*]                 | int32     | The `attributes` `version`.                                                       |
| data                        | id                                        | string    | The `ArbitraryRuleResponseData` `id`.                                             |
| data                        | type [*required*]                    | enum      | Arbitrary rule resource type. Allowed enum values: `arbitrary_rule`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "costs_to_allocate": [
        {
          "condition": "is",
          "tag": "account_id",
          "value": "123456789",
          "values": null
        },
        {
          "condition": "in",
          "tag": "environment",
          "value": "",
          "values": [
            "production",
            "staging"
          ]
        }
      ],
      "created": "2023-01-01T12:00:00Z",
      "enabled": true,
      "last_modified_user_uuid": "user-123-uuid",
      "order_id": 1,
      "provider": [
        "aws",
        "gcp"
      ],
      "rule_name": "Example custom allocation rule",
      "strategy": {
        "allocated_by_tag_keys": [
          "team",
          "environment"
        ],
        "based_on_costs": [
          {
            "condition": "is",
            "tag": "service",
            "value": "web-api",
            "values": null
          },
          {
            "condition": "not in",
            "tag": "team",
            "value": "",
            "values": [
              "legacy",
              "deprecated"
            ]
          }
        ],
        "granularity": "daily",
        "method": "proportional"
      },
      "type": "shared",
      "updated": "2023-01-01T12:00:00Z",
      "version": 1
    },
    "id": "123",
    "type": "arbitrary_rule"
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
                  \# Path parametersexport rule_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/${rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get custom allocation rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_custom_allocation_rule(
        rule_id=683,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get custom allocation rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.get_custom_allocation_rule(683)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get custom allocation rule returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.GetCustomAllocationRule(ctx, 683)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.GetCustomAllocationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.GetCustomAllocationRule`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get custom allocation rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.ArbitraryRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      ArbitraryRuleResponse result = apiInstance.getCustomAllocationRule(683L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#getCustomAllocationRule");
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
// Get custom allocation rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.get_custom_allocation_rule(683).await;
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
 * Get custom allocation rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiGetCustomAllocationRuleRequest = {
  ruleId: 683,
};

apiInstance
  .getCustomAllocationRule(params)
  .then((data: v2.ArbitraryRuleResponse) => {
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

## Reorder custom allocation rules{% #reorder-custom-allocation-rules %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cost/arbitrary_rule/reorder |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cost/arbitrary_rule/reorder |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cost/arbitrary_rule/reorder      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cost/arbitrary_rule/reorder      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cost/arbitrary_rule/reorder     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cost/arbitrary_rule/reorder |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/reorder |

### Overview



Reorder custom allocation rules - Change the execution order of custom allocation rules.

**Important**: You must provide the **complete list** of all rule IDs in the desired execution order. The API will reorder ALL rules according to the provided sequence.

Rules are executed in the order specified, with lower indices (earlier in the array) having higher priority.

**Example**: If you have rules with IDs [123, 456, 789] and want to change order from 123â456â789 to 456â123â789, send: [{"id": "456"}, {"id": "123"}, {"id": "789"}]

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                         |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------- |
|              | data [*required*] | [object] | The `ReorderRuleResourceArray` `data`.                              |
| data         | id                     | string   | The `ReorderRuleResourceData` `id`.                                 |
| data         | type [*required*] | enum     | Arbitrary rule resource type. Allowed enum values: `arbitrary_rule` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "string",
      "type": "arbitrary_rule"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="204" %}
Successfully reordered rules
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/arbitrary_rule/reorder" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "type": "arbitrary_rule"
    }
  ]
}
EOF
                
##### 

```python
"""
Reorder custom allocation rules returns "Successfully reordered rules" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.reorder_rule_resource_array import ReorderRuleResourceArray
from datadog_api_client.v2.model.reorder_rule_resource_data import ReorderRuleResourceData
from datadog_api_client.v2.model.reorder_rule_resource_data_type import ReorderRuleResourceDataType

body = ReorderRuleResourceArray(
    data=[
        ReorderRuleResourceData(
            id="456",
            type=ReorderRuleResourceDataType.ARBITRARY_RULE,
        ),
        ReorderRuleResourceData(
            id="123",
            type=ReorderRuleResourceDataType.ARBITRARY_RULE,
        ),
        ReorderRuleResourceData(
            id="789",
            type=ReorderRuleResourceDataType.ARBITRARY_RULE,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.reorder_custom_allocation_rules(body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Reorder custom allocation rules returns "Successfully reordered rules" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::ReorderRuleResourceArray.new({
  data: [
    DatadogAPIClient::V2::ReorderRuleResourceData.new({
      id: "456",
      type: DatadogAPIClient::V2::ReorderRuleResourceDataType::ARBITRARY_RULE,
    }),
    DatadogAPIClient::V2::ReorderRuleResourceData.new({
      id: "123",
      type: DatadogAPIClient::V2::ReorderRuleResourceDataType::ARBITRARY_RULE,
    }),
    DatadogAPIClient::V2::ReorderRuleResourceData.new({
      id: "789",
      type: DatadogAPIClient::V2::ReorderRuleResourceDataType::ARBITRARY_RULE,
    }),
  ],
})
api_instance.reorder_custom_allocation_rules(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Reorder custom allocation rules returns "Successfully reordered rules" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.ReorderRuleResourceArray{
		Data: []datadogV2.ReorderRuleResourceData{
			{
				Id:   datadog.PtrString("456"),
				Type: datadogV2.REORDERRULERESOURCEDATATYPE_ARBITRARY_RULE,
			},
			{
				Id:   datadog.PtrString("123"),
				Type: datadogV2.REORDERRULERESOURCEDATATYPE_ARBITRARY_RULE,
			},
			{
				Id:   datadog.PtrString("789"),
				Type: datadogV2.REORDERRULERESOURCEDATATYPE_ARBITRARY_RULE,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.ReorderCustomAllocationRules(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ReorderCustomAllocationRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Reorder custom allocation rules returns "Successfully reordered rules" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.ReorderRuleResourceArray;
import com.datadog.api.client.v2.model.ReorderRuleResourceData;
import com.datadog.api.client.v2.model.ReorderRuleResourceDataType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    ReorderRuleResourceArray body =
        new ReorderRuleResourceArray()
            .data(
                Arrays.asList(
                    new ReorderRuleResourceData()
                        .id("456")
                        .type(ReorderRuleResourceDataType.ARBITRARY_RULE),
                    new ReorderRuleResourceData()
                        .id("123")
                        .type(ReorderRuleResourceDataType.ARBITRARY_RULE),
                    new ReorderRuleResourceData()
                        .id("789")
                        .type(ReorderRuleResourceDataType.ARBITRARY_RULE)));

    try {
      apiInstance.reorderCustomAllocationRules(body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudCostManagementApi#reorderCustomAllocationRules");
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
// Reorder custom allocation rules returns "Successfully reordered rules" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::ReorderRuleResourceArray;
use datadog_api_client::datadogV2::model::ReorderRuleResourceData;
use datadog_api_client::datadogV2::model::ReorderRuleResourceDataType;

#[tokio::main]
async fn main() {
    let body = ReorderRuleResourceArray::new(vec![
        ReorderRuleResourceData::new(ReorderRuleResourceDataType::ARBITRARY_RULE)
            .id("456".to_string()),
        ReorderRuleResourceData::new(ReorderRuleResourceDataType::ARBITRARY_RULE)
            .id("123".to_string()),
        ReorderRuleResourceData::new(ReorderRuleResourceDataType::ARBITRARY_RULE)
            .id("789".to_string()),
    ]);
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.reorder_custom_allocation_rules(body).await;
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
 * Reorder custom allocation rules returns "Successfully reordered rules" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiReorderCustomAllocationRulesRequest = {
  body: {
    data: [
      {
        id: "456",
        type: "arbitrary_rule",
      },
      {
        id: "123",
        type: "arbitrary_rule",
      },
      {
        id: "789",
        type: "arbitrary_rule",
      },
    ],
  },
};

apiInstance
  .reorderCustomAllocationRules(params)
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

## List Custom Costs files{% #list-custom-costs-files %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/custom_costs |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/custom_costs |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/custom_costs      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/custom_costs      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/custom_costs     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/custom_costs |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/custom_costs |

### Overview

List the Custom Costs files. This endpoint requires the `cloud_cost_management_read` permission.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Query Strings

| Name           | Type    | Description                              |
| -------------- | ------- | ---------------------------------------- |
| page[number]   | integer | Page number for pagination               |
| page[size]     | integer | Page size for pagination                 |
| filter[status] | string  | Filter by file status                    |
| sort           | string  | Sort key with optional descending prefix |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for List Custom Costs files.

| Parent field  | Field                | Type     | Description                                                             |
| ------------- | -------------------- | -------- | ----------------------------------------------------------------------- |
|               | data                 | [object] | List of Custom Costs files.                                             |
| data          | attributes           | object   | Schema of a Custom Costs metadata.                                      |
| attributes    | billed_cost          | double   | Total cost in the cost file.                                            |
| attributes    | billing_currency     | string   | Currency used in the Custom Costs file.                                 |
| attributes    | charge_period        | object   | Usage charge period of a Custom Costs file.                             |
| charge_period | end                  | double   | End of the usage of the Custom Costs file.                              |
| charge_period | start                | double   | Start of the usage of the Custom Costs file.                            |
| attributes    | name                 | string   | Name of the Custom Costs file.                                          |
| attributes    | provider_names       | [string] | Providers contained in the Custom Costs file.                           |
| attributes    | status               | string   | Status of the Custom Costs file.                                        |
| attributes    | uploaded_at          | double   | Timestamp, in millisecond, of the upload time of the Custom Costs file. |
| attributes    | uploaded_by          | object   | Metadata of the user that has uploaded the Custom Costs file.           |
| uploaded_by   | email                | string   | The name of the Custom Costs file.                                      |
| uploaded_by   | icon                 | string   | The name of the Custom Costs file.                                      |
| uploaded_by   | name                 | string   | Name of the user.                                                       |
| data          | id                   | string   | ID of the Custom Costs metadata.                                        |
| data          | type                 | string   | Type of the Custom Costs file metadata.                                 |
|               | meta                 | object   | Meta for the response from the List Custom Costs endpoints.             |
| meta          | total_filtered_count | int64    | Number of Custom Costs files returned by the List Custom Costs endpoint |
| meta          | version              | string   | Version of Custom Costs file                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "billed_cost": 100.5,
        "billing_currency": "USD",
        "charge_period": {
          "end": 1706745600000,
          "start": 1704067200000
        },
        "name": "my_file.json",
        "provider_names": [
          "my_provider"
        ],
        "status": "active",
        "uploaded_at": 1704067200000,
        "uploaded_by": {
          "email": "email.test@datadohq.com",
          "icon": "icon.png",
          "name": "Test User"
        }
      },
      "id": "string",
      "type": "string"
    }
  ],
  "meta": {
    "total_filtered_count": "integer",
    "version": "string"
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
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/custom_costs" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Custom Costs files returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_custom_costs_files()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List Custom Costs files returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.list_custom_costs_files()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List Custom Costs files returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ListCustomCostsFiles(ctx, *datadogV2.NewListCustomCostsFilesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ListCustomCostsFiles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ListCustomCostsFiles`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List Custom Costs files returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.CustomCostsFileListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      CustomCostsFileListResponse result = apiInstance.listCustomCostsFiles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#listCustomCostsFiles");
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
// List Custom Costs files returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::api_cloud_cost_management::ListCustomCostsFilesOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api
        .list_custom_costs_files(ListCustomCostsFilesOptionalParams::default())
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
 * List Custom Costs files returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

apiInstance
  .listCustomCostsFiles()
  .then((data: v2.CustomCostsFileListResponse) => {
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

## Upload Custom Costs file{% #upload-custom-costs-file %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/cost/custom_costs |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/cost/custom_costs |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/cost/custom_costs      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/cost/custom_costs      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/cost/custom_costs     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/cost/custom_costs |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/cost/custom_costs |

### Overview

Upload a Custom Costs file. This endpoint requires the `cloud_cost_management_write` permission.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field         | Field             | Type   | Description                             |
| -------------------- | ----------------- | ------ | --------------------------------------- |
|                      | BilledCost        | double | Total cost in the cost file.            |
|                      | BillingCurrency   | string | Currency used in the Custom Costs file. |
|                      | ChargeDescription | string | Description for the line item cost.     |
|                      | ChargePeriodEnd   | string | End date of the usage charge.           |
|                      | ChargePeriodStart | string | Start date of the usage charge.         |
|                      | ProviderName      | string | Name of the provider for the line item. |
|                      | Tags              | object | Additional tags for the line item.      |
| additionalProperties | <any-key>         | string |

{% /tab %}

{% tab title="Example" %}

```json
[
  {
    "ProviderName": "my_provider",
    "ChargePeriodStart": "2023-05-06",
    "ChargePeriodEnd": "2023-06-06",
    "ChargeDescription": "my_description",
    "BilledCost": 250,
    "BillingCurrency": "USD",
    "Tags": {
      "key": "value"
    }
  }
]
```

{% /tab %}

### Response

{% tab title="202" %}
Accepted
{% tab title="Model" %}
Response for Uploaded Custom Costs files.

| Parent field  | Field            | Type     | Description                                                             |
| ------------- | ---------------- | -------- | ----------------------------------------------------------------------- |
|               | data             | object   | JSON API format for a Custom Costs file.                                |
| data          | attributes       | object   | Schema of a Custom Costs metadata.                                      |
| attributes    | billed_cost      | double   | Total cost in the cost file.                                            |
| attributes    | billing_currency | string   | Currency used in the Custom Costs file.                                 |
| attributes    | charge_period    | object   | Usage charge period of a Custom Costs file.                             |
| charge_period | end              | double   | End of the usage of the Custom Costs file.                              |
| charge_period | start            | double   | Start of the usage of the Custom Costs file.                            |
| attributes    | name             | string   | Name of the Custom Costs file.                                          |
| attributes    | provider_names   | [string] | Providers contained in the Custom Costs file.                           |
| attributes    | status           | string   | Status of the Custom Costs file.                                        |
| attributes    | uploaded_at      | double   | Timestamp, in millisecond, of the upload time of the Custom Costs file. |
| attributes    | uploaded_by      | object   | Metadata of the user that has uploaded the Custom Costs file.           |
| uploaded_by   | email            | string   | The name of the Custom Costs file.                                      |
| uploaded_by   | icon             | string   | The name of the Custom Costs file.                                      |
| uploaded_by   | name             | string   | Name of the user.                                                       |
| data          | id               | string   | ID of the Custom Costs metadata.                                        |
| data          | type             | string   | Type of the Custom Costs file metadata.                                 |
|               | meta             | object   | Meta for the response from the Upload Custom Costs endpoints.           |
| meta          | version          | string   | Version of Custom Costs file                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "billed_cost": 100.5,
      "billing_currency": "USD",
      "charge_period": {
        "end": 1706745600000,
        "start": 1704067200000
      },
      "name": "my_file.json",
      "provider_names": [
        "my_provider"
      ],
      "status": "active",
      "uploaded_at": 1704067200000,
      "uploaded_by": {
        "email": "email.test@datadohq.com",
        "icon": "icon.png",
        "name": "Test User"
      }
    },
    "id": "string",
    "type": "string"
  },
  "meta": {
    "version": "string"
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
Forbidden
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
                          \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/custom_costs" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
[
  {
    "ProviderName": "my_provider",
    "ChargePeriodStart": "2023-05-06",
    "ChargePeriodEnd": "2023-06-06",
    "ChargeDescription": "my_description",
    "BilledCost": 250,
    "BillingCurrency": "USD",
    "Tags": {
      "key": "value"
    }
  }
]
EOF
                        
##### 

```go
// Upload Custom Costs File returns "Accepted" response

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
	body := []datadogV2.CustomCostsFileLineItem{
		{
			ProviderName:      datadog.PtrString("my_provider"),
			ChargePeriodStart: datadog.PtrString("2023-05-06"),
			ChargePeriodEnd:   datadog.PtrString("2023-06-06"),
			ChargeDescription: datadog.PtrString("my_description"),
			BilledCost:        datadog.PtrFloat64(250),
			BillingCurrency:   datadog.PtrString("USD"),
			Tags: map[string]string{
				"key": "value",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.UploadCustomCostsFile(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.UploadCustomCostsFile`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.UploadCustomCostsFile`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Upload Custom Costs File returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.CustomCostsFileLineItem;
import com.datadog.api.client.v2.model.CustomCostsFileUploadResponse;
import java.util.Collections;
import java.util.List;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    List<CustomCostsFileLineItem> body =
        Collections.singletonList(
            new CustomCostsFileLineItem()
                .providerName("my_provider")
                .chargePeriodStart("2023-05-06")
                .chargePeriodEnd("2023-06-06")
                .chargeDescription("my_description")
                .billedCost(250.0)
                .billingCurrency("USD")
                .tags(Map.ofEntries(Map.entry("key", "value"))));

    try {
      CustomCostsFileUploadResponse result = apiInstance.uploadCustomCostsFile(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#uploadCustomCostsFile");
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

```python
"""
Upload Custom Costs File returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.custom_costs_file_line_item import CustomCostsFileLineItem

body = [
    CustomCostsFileLineItem(
        provider_name="my_provider",
        charge_period_start="2023-05-06",
        charge_period_end="2023-06-06",
        charge_description="my_description",
        billed_cost=250.0,
        billing_currency="USD",
        tags=dict(
            key="value",
        ),
    ),
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.upload_custom_costs_file(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Upload Custom Costs File returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = [
  DatadogAPIClient::V2::CustomCostsFileLineItem.new({
    provider_name: "my_provider",
    charge_period_start: "2023-05-06",
    charge_period_end: "2023-06-06",
    charge_description: "my_description",
    billed_cost: 250,
    billing_currency: "USD",
    tags: {
      key: "value",
    },
  }),
]
p api_instance.upload_custom_costs_file(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Upload Custom Costs File returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::CustomCostsFileLineItem;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = vec![CustomCostsFileLineItem::new()
        .billed_cost(250.0 as f64)
        .billing_currency("USD".to_string())
        .charge_description("my_description".to_string())
        .charge_period_end("2023-06-06".to_string())
        .charge_period_start("2023-05-06".to_string())
        .provider_name("my_provider".to_string())
        .tags(BTreeMap::from([("key".to_string(), "value".to_string())]))];
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.upload_custom_costs_file(body).await;
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
 * Upload Custom Costs File returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiUploadCustomCostsFileRequest = {
  body: [
    {
      providerName: "my_provider",
      chargePeriodStart: "2023-05-06",
      chargePeriodEnd: "2023-06-06",
      chargeDescription: "my_description",
      billedCost: 250,
      billingCurrency: "USD",
      tags: {
        key: "value",
      },
    },
  ],
};

apiInstance
  .uploadCustomCostsFile(params)
  .then((data: v2.CustomCostsFileUploadResponse) => {
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

## Delete Custom Costs file{% #delete-custom-costs-file %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cost/custom_costs/{file_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cost/custom_costs/{file_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cost/custom_costs/{file_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cost/custom_costs/{file_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cost/custom_costs/{file_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cost/custom_costs/{file_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cost/custom_costs/{file_id} |

### Overview

Delete the specified Custom Costs file.

OAuth apps require the `cloud_cost_management_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| file_id [*required*] | string | File ID.    |

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="403" %}
Forbidden
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

### Code Example

##### 
                  \# Path parametersexport file_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/custom_costs/${file_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Custom Costs file returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_custom_costs_file(
        file_id="file_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete Custom Costs file returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
api_instance.delete_custom_costs_file("file_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete Custom Costs file returns "No Content" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.DeleteCustomCostsFile(ctx, "file_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.DeleteCustomCostsFile`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete Custom Costs file returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      apiInstance.deleteCustomCostsFile("file_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#deleteCustomCostsFile");
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
// Delete Custom Costs file returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.delete_custom_costs_file("file_id".to_string()).await;
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
 * Delete Custom Costs file returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiDeleteCustomCostsFileRequest = {
  fileId: "file_id",
};

apiInstance
  .deleteCustomCostsFile(params)
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

## Get Custom Costs file{% #get-custom-costs-file %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/custom_costs/{file_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/custom_costs/{file_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/custom_costs/{file_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/custom_costs/{file_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/custom_costs/{file_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/custom_costs/{file_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/custom_costs/{file_id} |

### Overview

Fetch the specified Custom Costs file.

OAuth apps require the `cloud_cost_management_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#cloud-cost-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description |
| ------------------------- | ------ | ----------- |
| file_id [*required*] | string | File ID.    |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for Get Custom Costs files.

| Parent field         | Field             | Type     | Description                                                           |
| -------------------- | ----------------- | -------- | --------------------------------------------------------------------- |
|                      | data              | object   | JSON API format of for a Custom Costs file with content.              |
| data                 | attributes        | object   | Schema of a cost file's metadata.                                     |
| attributes           | billed_cost       | double   | Total cost in the cost file.                                          |
| attributes           | billing_currency  | string   | Currency used in the Custom Costs file.                               |
| attributes           | charge_period     | object   | Usage charge period of a Custom Costs file.                           |
| charge_period        | end               | double   | End of the usage of the Custom Costs file.                            |
| charge_period        | start             | double   | Start of the usage of the Custom Costs file.                          |
| attributes           | content           | [object] | Detail of the line items from the Custom Costs file.                  |
| content              | BilledCost        | double   | Total cost in the cost file.                                          |
| content              | BillingCurrency   | string   | Currency used in the Custom Costs file.                               |
| content              | ChargeDescription | string   | Description for the line item cost.                                   |
| content              | ChargePeriodEnd   | string   | End date of the usage charge.                                         |
| content              | ChargePeriodStart | string   | Start date of the usage charge.                                       |
| content              | ProviderName      | string   | Name of the provider for the line item.                               |
| content              | Tags              | object   | Additional tags for the line item.                                    |
| additionalProperties | <any-key>         | string   |
| attributes           | name              | string   | Name of the Custom Costs file.                                        |
| attributes           | provider_names    | [string] | Providers contained in the Custom Costs file.                         |
| attributes           | status            | string   | Status of the Custom Costs file.                                      |
| attributes           | uploaded_at       | double   | Timestamp in millisecond of the upload time of the Custom Costs file. |
| attributes           | uploaded_by       | object   | Metadata of the user that has uploaded the Custom Costs file.         |
| uploaded_by          | email             | string   | The name of the Custom Costs file.                                    |
| uploaded_by          | icon              | string   | The name of the Custom Costs file.                                    |
| uploaded_by          | name              | string   | Name of the user.                                                     |
| data                 | id                | string   | ID of the Custom Costs metadata.                                      |
| data                 | type              | string   | Type of the Custom Costs file metadata.                               |
|                      | meta              | object   | Meta for the response from the Get Custom Costs endpoints.            |
| meta                 | version           | string   | Version of Custom Costs file                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "billed_cost": 100.5,
      "billing_currency": "USD",
      "charge_period": {
        "end": 1706745600000,
        "start": 1704067200000
      },
      "content": [
        {
          "BilledCost": 100.5,
          "BillingCurrency": "USD",
          "ChargeDescription": "Monthly usage charge for my service",
          "ChargePeriodEnd": "2023-02-28",
          "ChargePeriodStart": "2023-02-01",
          "ProviderName": "string",
          "Tags": {
            "<any-key>": "string"
          }
        }
      ],
      "name": "my_file.json",
      "provider_names": [
        "my_provider"
      ],
      "status": "active",
      "uploaded_at": 1704067200000,
      "uploaded_by": {
        "email": "email.test@datadohq.com",
        "icon": "icon.png",
        "name": "Test User"
      }
    },
    "id": "string",
    "type": "string"
  },
  "meta": {
    "version": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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

### Code Example

##### 
                  \# Path parametersexport file_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/custom_costs/${file_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get Custom Costs file returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_custom_costs_file(
        file_id="file_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get Custom Costs file returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.get_custom_costs_file("file_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get Custom Costs file returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.GetCustomCostsFile(ctx, "file_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.GetCustomCostsFile`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.GetCustomCostsFile`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get Custom Costs file returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.CustomCostsFileGetResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      CustomCostsFileGetResponse result = apiInstance.getCustomCostsFile("file_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#getCustomCostsFile");
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
// Get Custom Costs file returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.get_custom_costs_file("file_id".to_string()).await;
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
 * Get Custom Costs file returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiGetCustomCostsFileRequest = {
  fileId: "file_id",
};

apiInstance
  .getCustomCostsFile(params)
  .then((data: v2.CustomCostsFileGetResponse) => {
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

## List budgets{% #list-budgets %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/budgets |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/budgets |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/budgets      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/budgets      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/budgets     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/budgets |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/budgets |

### Overview

List budgets.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An array of budgets.

| Parent field | Field                  | Type     | Description                                      |
| ------------ | ---------------------- | -------- | ------------------------------------------------ |
|              | data [*required*] | [object] | The `BudgetArray` `data`.                        |
| data         | attributes             | object   | The attributes of a budget.                      |
| attributes   | created_at             | int64    | The timestamp when the budget was created.       |
| attributes   | created_by             | string   | The id of the user that created the budget.      |
| attributes   | end_month              | int64    | The month when the budget ends.                  |
| attributes   | entries                | [object] |
| entries      | amount                 | double   |
| entries      | month                  | int64    |
| entries      | tag_filters            | [object] |
| tag_filters  | tag_key                | string   |
| tag_filters  | tag_value              | string   |
| attributes   | metrics_query          | string   | The cost query used to track against the budget. |
| attributes   | name                   | string   | The name of the budget.                          |
| attributes   | org_id                 | int64    | The id of the org the budget belongs to.         |
| attributes   | start_month            | int64    | The month when the budget starts.                |
| attributes   | total_amount           | double   | The sum of all budget entries' amounts.          |
| attributes   | updated_at             | int64    | The timestamp when the budget was last updated.  |
| attributes   | updated_by             | string   | The id of the user that created the budget.      |
| data         | id                     | string   | The id of the budget.                            |
| data         | type [*required*] | string   | The type of the object, must be `budget`.        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": 1741011342772,
        "created_by": "user1",
        "end_month": 202502,
        "metrics_query": "aws.cost.amortized{service:ec2} by {service}",
        "name": "my budget",
        "org_id": 123,
        "start_month": 202501,
        "total_amount": 1000,
        "updated_at": 1741011342772,
        "updated_by": "user2"
      },
      "id": "00000000-0a0a-0a0a-aaa0-00000000000a",
      "type": "budget"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/budgets" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List budgets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.list_budgets()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List budgets returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.list_budgets()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List budgets returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.ListBudgets(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.ListBudgets`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.ListBudgets`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List budgets returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.BudgetArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      BudgetArray result = apiInstance.listBudgets();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#listBudgets");
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
// List budgets returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.list_budgets().await;
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
 * List budgets returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

apiInstance
  .listBudgets()
  .then((data: v2.BudgetArray) => {
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

## Create or update a budget{% #create-or-update-a-budget %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/cost/budget |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/cost/budget |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/cost/budget      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/cost/budget      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/cost/budget     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/cost/budget |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/cost/budget |

### Overview

Create a new budget or update an existing one.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field         | Type     | Description                                      |
| ------------ | ------------- | -------- | ------------------------------------------------ |
|              | data          | object   | A budget and all its entries.                    |
| data         | attributes    | object   | The attributes of a budget.                      |
| attributes   | created_at    | int64    | The timestamp when the budget was created.       |
| attributes   | created_by    | string   | The id of the user that created the budget.      |
| attributes   | end_month     | int64    | The month when the budget ends.                  |
| attributes   | entries       | [object] |
| entries      | amount        | double   |
| entries      | month         | int64    |
| entries      | tag_filters   | [object] |
| tag_filters  | tag_key       | string   |
| tag_filters  | tag_value     | string   |
| attributes   | metrics_query | string   | The cost query used to track against the budget. |
| attributes   | name          | string   | The name of the budget.                          |
| attributes   | org_id        | int64    | The id of the org the budget belongs to.         |
| attributes   | start_month   | int64    | The month when the budget starts.                |
| attributes   | total_amount  | double   | The sum of all budget entries' amounts.          |
| attributes   | updated_at    | int64    | The timestamp when the budget was last updated.  |
| attributes   | updated_by    | string   | The id of the user that created the budget.      |
| data         | id            | string   | The `BudgetWithEntriesData` `id`.                |
| data         | type          | string   | The type of the object, must be `budget`.        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": 1738258683590,
      "created_by": "00000000-0a0a-0a0a-aaa0-00000000000a",
      "end_month": 202502,
      "entries": [
        {
          "amount": "number",
          "month": "integer",
          "tag_filters": [
            {
              "tag_key": "string",
              "tag_value": "string"
            }
          ]
        }
      ],
      "metrics_query": "aws.cost.amortized{service:ec2} by {service}",
      "name": "my budget",
      "org_id": 123,
      "start_month": 202501,
      "total_amount": 1000,
      "updated_at": 1738258683590,
      "updated_by": "00000000-0a0a-0a0a-aaa0-00000000000a"
    },
    "id": "00000000-0a0a-0a0a-aaa0-00000000000a",
    "type": ""
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of the `BudgetWithEntries` object.

| Parent field | Field         | Type     | Description                                      |
| ------------ | ------------- | -------- | ------------------------------------------------ |
|              | data          | object   | A budget and all its entries.                    |
| data         | attributes    | object   | The attributes of a budget.                      |
| attributes   | created_at    | int64    | The timestamp when the budget was created.       |
| attributes   | created_by    | string   | The id of the user that created the budget.      |
| attributes   | end_month     | int64    | The month when the budget ends.                  |
| attributes   | entries       | [object] |
| entries      | amount        | double   |
| entries      | month         | int64    |
| entries      | tag_filters   | [object] |
| tag_filters  | tag_key       | string   |
| tag_filters  | tag_value     | string   |
| attributes   | metrics_query | string   | The cost query used to track against the budget. |
| attributes   | name          | string   | The name of the budget.                          |
| attributes   | org_id        | int64    | The id of the org the budget belongs to.         |
| attributes   | start_month   | int64    | The month when the budget starts.                |
| attributes   | total_amount  | double   | The sum of all budget entries' amounts.          |
| attributes   | updated_at    | int64    | The timestamp when the budget was last updated.  |
| attributes   | updated_by    | string   | The id of the user that created the budget.      |
| data         | id            | string   | The `BudgetWithEntriesData` `id`.                |
| data         | type          | string   | The type of the object, must be `budget`.        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": 1738258683590,
      "created_by": "00000000-0a0a-0a0a-aaa0-00000000000a",
      "end_month": 202502,
      "entries": [
        {
          "amount": "number",
          "month": "integer",
          "tag_filters": [
            {
              "tag_key": "string",
              "tag_value": "string"
            }
          ]
        }
      ],
      "metrics_query": "aws.cost.amortized{service:ec2} by {service}",
      "name": "my budget",
      "org_id": 123,
      "start_month": 202501,
      "total_amount": 1000,
      "updated_at": 1738258683590,
      "updated_by": "00000000-0a0a-0a0a-aaa0-00000000000a"
    },
    "id": "00000000-0a0a-0a0a-aaa0-00000000000a",
    "type": ""
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

### Code Example

##### 
                  \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/budget" \
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
Create or update a budget returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.budget_attributes import BudgetAttributes
from datadog_api_client.v2.model.budget_entry import BudgetEntry
from datadog_api_client.v2.model.budget_with_entries import BudgetWithEntries
from datadog_api_client.v2.model.budget_with_entries_data import BudgetWithEntriesData
from datadog_api_client.v2.model.tag_filter import TagFilter

body = BudgetWithEntries(
    data=BudgetWithEntriesData(
        attributes=BudgetAttributes(
            created_at=1738258683590,
            created_by="00000000-0a0a-0a0a-aaa0-00000000000a",
            end_month=202502,
            entries=[
                BudgetEntry(
                    amount=500.0,
                    month=202501,
                    tag_filters=[
                        TagFilter(
                            tag_key="service",
                            tag_value="ec2",
                        ),
                    ],
                ),
            ],
            metrics_query="aws.cost.amortized{service:ec2} by {service}",
            name="my budget",
            org_id=123,
            start_month=202501,
            total_amount=1000.0,
            updated_at=1738258683590,
            updated_by="00000000-0a0a-0a0a-aaa0-00000000000a",
        ),
        id="00000000-0a0a-0a0a-aaa0-00000000000a",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.upsert_budget(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create or update a budget returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new

body = DatadogAPIClient::V2::BudgetWithEntries.new({
  data: DatadogAPIClient::V2::BudgetWithEntriesData.new({
    attributes: DatadogAPIClient::V2::BudgetAttributes.new({
      created_at: 1738258683590,
      created_by: "00000000-0a0a-0a0a-aaa0-00000000000a",
      end_month: 202502,
      entries: [
        DatadogAPIClient::V2::BudgetEntry.new({
          amount: 500,
          month: 202501,
          tag_filters: [
            DatadogAPIClient::V2::TagFilter.new({
              tag_key: "service",
              tag_value: "ec2",
            }),
          ],
        }),
      ],
      metrics_query: "aws.cost.amortized{service:ec2} by {service}",
      name: "my budget",
      org_id: 123,
      start_month: 202501,
      total_amount: 1000,
      updated_at: 1738258683590,
      updated_by: "00000000-0a0a-0a0a-aaa0-00000000000a",
    }),
    id: "00000000-0a0a-0a0a-aaa0-00000000000a",
  }),
})
p api_instance.upsert_budget(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create or update a budget returns "OK" response

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
	body := datadogV2.BudgetWithEntries{
		Data: &datadogV2.BudgetWithEntriesData{
			Attributes: &datadogV2.BudgetAttributes{
				CreatedAt: datadog.PtrInt64(1738258683590),
				CreatedBy: datadog.PtrString("00000000-0a0a-0a0a-aaa0-00000000000a"),
				EndMonth:  datadog.PtrInt64(202502),
				Entries: []datadogV2.BudgetEntry{
					{
						Amount: datadog.PtrFloat64(500),
						Month:  datadog.PtrInt64(202501),
						TagFilters: []datadogV2.TagFilter{
							{
								TagKey:   datadog.PtrString("service"),
								TagValue: datadog.PtrString("ec2"),
							},
						},
					},
				},
				MetricsQuery: datadog.PtrString("aws.cost.amortized{service:ec2} by {service}"),
				Name:         datadog.PtrString("my budget"),
				OrgId:        datadog.PtrInt64(123),
				StartMonth:   datadog.PtrInt64(202501),
				TotalAmount:  datadog.PtrFloat64(1000),
				UpdatedAt:    datadog.PtrInt64(1738258683590),
				UpdatedBy:    datadog.PtrString("00000000-0a0a-0a0a-aaa0-00000000000a"),
			},
			Id: datadog.PtrString("00000000-0a0a-0a0a-aaa0-00000000000a"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.UpsertBudget(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.UpsertBudget`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.UpsertBudget`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create or update a budget returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.BudgetAttributes;
import com.datadog.api.client.v2.model.BudgetEntry;
import com.datadog.api.client.v2.model.BudgetWithEntries;
import com.datadog.api.client.v2.model.BudgetWithEntriesData;
import com.datadog.api.client.v2.model.TagFilter;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    BudgetWithEntries body =
        new BudgetWithEntries()
            .data(
                new BudgetWithEntriesData()
                    .attributes(
                        new BudgetAttributes()
                            .createdAt(1738258683590L)
                            .createdBy("00000000-0a0a-0a0a-aaa0-00000000000a")
                            .endMonth(202502L)
                            .entries(
                                Collections.singletonList(
                                    new BudgetEntry()
                                        .amount(500.0)
                                        .month(202501L)
                                        .tagFilters(
                                            Collections.singletonList(
                                                new TagFilter()
                                                    .tagKey("service")
                                                    .tagValue("ec2")))))
                            .metricsQuery("aws.cost.amortized{service:ec2} by {service}")
                            .name("my budget")
                            .orgId(123L)
                            .startMonth(202501L)
                            .totalAmount(1000.0)
                            .updatedAt(1738258683590L)
                            .updatedBy("00000000-0a0a-0a0a-aaa0-00000000000a"))
                    .id("00000000-0a0a-0a0a-aaa0-00000000000a"));

    try {
      BudgetWithEntries result = apiInstance.upsertBudget(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#upsertBudget");
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
// Create or update a budget returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;
use datadog_api_client::datadogV2::model::BudgetAttributes;
use datadog_api_client::datadogV2::model::BudgetEntry;
use datadog_api_client::datadogV2::model::BudgetWithEntries;
use datadog_api_client::datadogV2::model::BudgetWithEntriesData;
use datadog_api_client::datadogV2::model::TagFilter;

#[tokio::main]
async fn main() {
    let body = BudgetWithEntries::new().data(
        BudgetWithEntriesData::new()
            .attributes(
                BudgetAttributes::new()
                    .created_at(1738258683590)
                    .created_by("00000000-0a0a-0a0a-aaa0-00000000000a".to_string())
                    .end_month(202502)
                    .entries(vec![BudgetEntry::new()
                        .amount(500.0 as f64)
                        .month(202501)
                        .tag_filters(vec![TagFilter::new()
                            .tag_key("service".to_string())
                            .tag_value("ec2".to_string())])])
                    .metrics_query("aws.cost.amortized{service:ec2} by {service}".to_string())
                    .name("my budget".to_string())
                    .org_id(123)
                    .start_month(202501)
                    .total_amount(1000.0 as f64)
                    .updated_at(1738258683590)
                    .updated_by("00000000-0a0a-0a0a-aaa0-00000000000a".to_string()),
            )
            .id("00000000-0a0a-0a0a-aaa0-00000000000a".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.upsert_budget(body).await;
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
 * Create or update a budget returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiUpsertBudgetRequest = {
  body: {
    data: {
      attributes: {
        createdAt: 1738258683590,
        createdBy: "00000000-0a0a-0a0a-aaa0-00000000000a",
        endMonth: 202502,
        entries: [
          {
            amount: 500,
            month: 202501,
            tagFilters: [
              {
                tagKey: "service",
                tagValue: "ec2",
              },
            ],
          },
        ],
        metricsQuery: "aws.cost.amortized{service:ec2} by {service}",
        name: "my budget",
        orgId: 123,
        startMonth: 202501,
        totalAmount: 1000,
        updatedAt: 1738258683590,
        updatedBy: "00000000-0a0a-0a0a-aaa0-00000000000a",
      },
      id: "00000000-0a0a-0a0a-aaa0-00000000000a",
    },
  },
};

apiInstance
  .upsertBudget(params)
  .then((data: v2.BudgetWithEntries) => {
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

## Validate budget{% #validate-budget %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cost/budget/validate |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cost/budget/validate |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cost/budget/validate      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cost/budget/validate      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cost/budget/validate     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cost/budget/validate |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cost/budget/validate |

### Overview

Validate a budget configuration without creating or modifying it

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                         |
| ------------ | ---------------------- | -------- | --------------------------------------------------- |
|              | data                   | object   |
| data         | attributes             | object   |
| attributes   | created_at             | int64    |
| attributes   | created_by             | string   |
| attributes   | end_month              | int64    |
| attributes   | entries                | [object] |
| entries      | amount                 | double   |
| entries      | month                  | int64    |
| entries      | tag_filters            | [object] |
| tag_filters  | tag_key                | string   |
| tag_filters  | tag_value              | string   |
| attributes   | metrics_query          | string   |
| attributes   | name                   | string   |
| attributes   | org_id                 | int64    |
| attributes   | start_month            | int64    |
| attributes   | total_amount           | double   |
| attributes   | updated_at             | int64    |
| attributes   | updated_by             | string   |
| data         | id                     | string   |
| data         | type [*required*] | enum     | Budget resource type. Allowed enum values: `budget` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "integer",
      "created_by": "string",
      "end_month": "integer",
      "entries": [
        {
          "amount": "number",
          "month": "integer",
          "tag_filters": [
            {
              "tag_key": "string",
              "tag_value": "string"
            }
          ]
        }
      ],
      "metrics_query": "string",
      "name": "string",
      "org_id": "integer",
      "start_month": "integer",
      "total_amount": "number",
      "updated_at": "integer",
      "updated_by": "string"
    },
    "id": "string",
    "type": "budget"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                               |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------------- |
|              | data                   | object   |
| data         | attributes             | object   |
| attributes   | errors                 | [string] |
| attributes   | valid                  | boolean  |
| data         | id                     | string   |
| data         | type [*required*] | enum     | Budget validation resource type. Allowed enum values: `budget_validation` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "errors": [],
      "valid": true
    },
    "id": "budget_validation",
    "type": "budget_validation"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/budget/validate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "budget"
  }
}
EOF
                
{% /tab %}

## Validate CSV budget{% #validate-csv-budget %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cost/budget/csv/validate |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cost/budget/csv/validate |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cost/budget/csv/validate      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cost/budget/csv/validate      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cost/budget/csv/validate     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cost/budget/csv/validate |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cost/budget/csv/validate |

### Overview



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing validation errors.

| Parent field | Field                     | Type     | Description                                                                                    |
| ------------ | ------------------------- | -------- | ---------------------------------------------------------------------------------------------- |
|              | errors                    | [object] | The `ValidationResponse` `errors`.                                                             |
| errors       | meta [*required*]    | object   | Describes additional metadata for validation errors, including field names and error messages. |
| meta         | field                     | string   | The field name that caused the error.                                                          |
| meta         | id                        | string   | The ID of the component in which the error occurred.                                           |
| meta         | message [*required*] | string   | The detailed error message.                                                                    |
| errors       | title [*required*]   | string   | A short, human-readable summary of the error.                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "meta": {
        "field": "region",
        "id": "datadog-agent-source",
        "message": "Field 'region' is required"
      },
      "title": "Field 'region' is required"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/budget/csv/validate" \
-H "Accept: application/json"
                
{% /tab %}

## Get budget{% #get-budget %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cost/budget/{budget_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cost/budget/{budget_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cost/budget/{budget_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cost/budget/{budget_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cost/budget/{budget_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cost/budget/{budget_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cost/budget/{budget_id} |

### Overview

Get a budget

### Arguments

#### Path Parameters

| Name                        | Type   | Description |
| --------------------------- | ------ | ----------- |
| budget_id [*required*] | string | Budget id.  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The definition of the `BudgetWithEntries` object.

| Parent field | Field         | Type     | Description                                      |
| ------------ | ------------- | -------- | ------------------------------------------------ |
|              | data          | object   | A budget and all its entries.                    |
| data         | attributes    | object   | The attributes of a budget.                      |
| attributes   | created_at    | int64    | The timestamp when the budget was created.       |
| attributes   | created_by    | string   | The id of the user that created the budget.      |
| attributes   | end_month     | int64    | The month when the budget ends.                  |
| attributes   | entries       | [object] |
| entries      | amount        | double   |
| entries      | month         | int64    |
| entries      | tag_filters   | [object] |
| tag_filters  | tag_key       | string   |
| tag_filters  | tag_value     | string   |
| attributes   | metrics_query | string   | The cost query used to track against the budget. |
| attributes   | name          | string   | The name of the budget.                          |
| attributes   | org_id        | int64    | The id of the org the budget belongs to.         |
| attributes   | start_month   | int64    | The month when the budget starts.                |
| attributes   | total_amount  | double   | The sum of all budget entries' amounts.          |
| attributes   | updated_at    | int64    | The timestamp when the budget was last updated.  |
| attributes   | updated_by    | string   | The id of the user that created the budget.      |
| data         | id            | string   | The `BudgetWithEntriesData` `id`.                |
| data         | type          | string   | The type of the object, must be `budget`.        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": 1738258683590,
      "created_by": "00000000-0a0a-0a0a-aaa0-00000000000a",
      "end_month": 202502,
      "entries": [
        {
          "amount": "number",
          "month": "integer",
          "tag_filters": [
            {
              "tag_key": "string",
              "tag_value": "string"
            }
          ]
        }
      ],
      "metrics_query": "aws.cost.amortized{service:ec2} by {service}",
      "name": "my budget",
      "org_id": 123,
      "start_month": 202501,
      "total_amount": 1000,
      "updated_at": 1738258683590,
      "updated_by": "00000000-0a0a-0a0a-aaa0-00000000000a"
    },
    "id": "00000000-0a0a-0a0a-aaa0-00000000000a",
    "type": ""
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
                  \# Path parametersexport budget_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/budget/${budget_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a budget returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_budget(
        budget_id="budget_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a budget returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
p api_instance.get_budget("budget_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a budget returns "OK" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	resp, r, err := api.GetBudget(ctx, "budget_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.GetBudget`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CloudCostManagementApi.GetBudget`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a budget returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;
import com.datadog.api.client.v2.model.BudgetWithEntries;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      BudgetWithEntries result = apiInstance.getBudget("budget_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#getBudget");
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
// Get a budget returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.get_budget("budget_id".to_string()).await;
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
 * Get a budget returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiGetBudgetRequest = {
  budgetId: "budget_id",
};

apiInstance
  .getBudget(params)
  .then((data: v2.BudgetWithEntries) => {
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

## Delete budget{% #delete-budget %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cost/budget/{budget_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cost/budget/{budget_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cost/budget/{budget_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cost/budget/{budget_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cost/budget/{budget_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cost/budget/{budget_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cost/budget/{budget_id} |

### Overview

Delete a budget

### Arguments

#### Path Parameters

| Name                        | Type   | Description |
| --------------------------- | ------ | ----------- |
| budget_id [*required*] | string | Budget id.  |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport budget_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cost/budget/${budget_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a budget returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_budget(
        budget_id="budget_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete a budget returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudCostManagementAPI.new
api_instance.delete_budget("budget_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete a budget returns "No Content" response

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
	api := datadogV2.NewCloudCostManagementApi(apiClient)
	r, err := api.DeleteBudget(ctx, "budget_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CloudCostManagementApi.DeleteBudget`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete a budget returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudCostManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudCostManagementApi apiInstance = new CloudCostManagementApi(defaultClient);

    try {
      apiInstance.deleteBudget("budget_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudCostManagementApi#deleteBudget");
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
// Delete a budget returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_cost_management::CloudCostManagementAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudCostManagementAPI::with_config(configuration);
    let resp = api.delete_budget("budget_id".to_string()).await;
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
 * Delete a budget returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudCostManagementApi(configuration);

const params: v2.CloudCostManagementApiDeleteBudgetRequest = {
  budgetId: "budget_id",
};

apiInstance
  .deleteBudget(params)
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
