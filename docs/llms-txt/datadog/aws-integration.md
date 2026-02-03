# Source: https://docs.datadoghq.com/api/latest/aws-integration.md

---
title: AWS Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > AWS Integration
---

# AWS Integration

Configure your Datadog-AWS integration directly through the Datadog API. For more information, see the [AWS integration page](https://docs.datadoghq.com/integrations/amazon_web_services).

## Get all AWS tag filters{% #get-all-aws-tag-filters %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/aws/filtering |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/aws/filtering |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/aws/filtering      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/aws/filtering      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/aws/filtering     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/aws/filtering |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/aws/filtering |

### Overview

Get all AWS tag filters. This endpoint requires the `aws_configuration_read` permission.

### Arguments

#### Query Strings

| Name                         | Type   | Description                                             |
| ---------------------------- | ------ | ------------------------------------------------------- |
| account_id [*required*] | string | Only return AWS filters that matches this `account_id`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An array of tag filter rules by `namespace` and tag filter string.

| Parent field | Field          | Type     | Description                                                                                                                                     |
| ------------ | -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|              | filters        | [object] | An array of tag filters.                                                                                                                        |
| filters      | namespace      | enum     | The namespace associated with the tag filter entry. Allowed enum values: `elb,application_elb,sqs,rds,custom,network_elb,lambda,step_functions` |
| filters      | tag_filter_str | string   | The tag filter string.                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "filters": [
    {
      "namespace": "string",
      "tag_filter_str": "prod*"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Required query argumentsexport account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/filtering?account_id=${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all AWS tag filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_aws_tag_filters(
        account_id="account_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all AWS tag filters returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new
p api_instance.list_aws_tag_filters("account_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all AWS tag filters returns "OK" response

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
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.ListAWSTagFilters(ctx, "account_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.ListAWSTagFilters`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.ListAWSTagFilters`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all AWS tag filters returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSTagFilterListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSTagFilterListResponse result = apiInstance.listAWSTagFilters("account_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#listAWSTagFilters");
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
// Get all AWS tag filters returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.list_aws_tag_filters("account_id".to_string()).await;
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
 * Get all AWS tag filters returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiListAWSTagFiltersRequest = {
  accountId: "account_id",
};

apiInstance
  .listAWSTagFilters(params)
  .then((data: v1.AWSTagFilterListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
## List available namespaces{% #list-available-namespaces %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/available_namespaces |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/available_namespaces |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/available_namespaces      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/available_namespaces      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/available_namespaces     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/available_namespaces |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/available_namespaces |

### Overview

Get a list of available AWS CloudWatch namespaces that can send metrics to Datadog. This endpoint requires the `aws_configuration_read` permission.

### Response

{% tab title="200" %}
AWS Namespaces List object
{% tab title="Model" %}
AWS Namespaces response body.

| Parent field | Field                        | Type     | Description                                                               |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------- |
|              | data [*required*]       | object   | AWS Namespaces response data.                                             |
| data         | attributes                   | object   | AWS Namespaces response attributes.                                       |
| attributes   | namespaces [*required*] | [string] | AWS CloudWatch namespace.                                                 |
| data         | id [*required*]         | string   | The `AWSNamespacesResponseData` `id`.                                     |
| data         | type [*required*]       | enum     | The `AWSNamespacesResponseData` `type`. Allowed enum values: `namespaces` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "namespaces": [
        "AWS/ApiGateway"
      ]
    },
    "id": "namespaces",
    "type": "namespaces"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/available_namespaces" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List available namespaces returns "AWS Namespaces List object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_aws_namespaces()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List available namespaces returns "AWS Namespaces List object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new
p api_instance.list_aws_namespaces()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List available namespaces returns "AWS Namespaces List object" response

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
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.ListAWSNamespaces(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.ListAWSNamespaces`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.ListAWSNamespaces`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List available namespaces returns "AWS Namespaces List object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSNamespacesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSNamespacesResponse result = apiInstance.listAWSNamespaces();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#listAWSNamespaces");
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
// List available namespaces returns "AWS Namespaces List object" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.list_aws_namespaces().await;
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
 * List available namespaces returns "AWS Namespaces List object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

apiInstance
  .listAWSNamespaces()
  .then((data: v2.AWSNamespacesResponse) => {
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

## Set an AWS tag filter{% #set-an-aws-tag-filter %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/aws/filtering |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/aws/filtering |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/aws/filtering      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/aws/filtering      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/aws/filtering     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/aws/filtering |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/aws/filtering |

### Overview

Set an AWS tag filter. This endpoint requires the `aws_configuration_edit` permission.

### Request

#### Body Data (required)

Set an AWS tag filter using an `aws_account_identifier`, `namespace`, and filtering string. Namespace options are `application_elb`, `elb`, `lambda`, `network_elb`, `rds`, `sqs`, and `custom`.

{% tab title="Model" %}

| Field          | Type   | Description                                                                                                                                     |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id     | string | Your AWS Account ID without dashes.                                                                                                             |
| namespace      | enum   | The namespace associated with the tag filter entry. Allowed enum values: `elb,application_elb,sqs,rds,custom,network_elb,lambda,step_functions` |
| tag_filter_str | string | The tag filter string.                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "123456789012",
  "namespace": "string",
  "tag_filter_str": "prod*"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/filtering" \
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
Set an AWS tag filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_namespace import AWSNamespace
from datadog_api_client.v1.model.aws_tag_filter_create_request import AWSTagFilterCreateRequest

body = AWSTagFilterCreateRequest(
    account_id="123456789012",
    namespace=AWSNamespace.ELB,
    tag_filter_str="prod*",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_tag_filter(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Set an AWS tag filter returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSTagFilterCreateRequest.new({
  account_id: "123456789012",
  namespace: DatadogAPIClient::V1::AWSNamespace::ELB,
  tag_filter_str: "prod*",
})
p api_instance.create_aws_tag_filter(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Set an AWS tag filter returns "OK" response

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
	body := datadogV1.AWSTagFilterCreateRequest{
		AccountId:    datadog.PtrString("123456789012"),
		Namespace:    datadogV1.AWSNAMESPACE_ELB.Ptr(),
		TagFilterStr: datadog.PtrString("prod*"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateAWSTagFilter(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateAWSTagFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateAWSTagFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Set an AWS tag filter returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSNamespace;
import com.datadog.api.client.v1.model.AWSTagFilterCreateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSTagFilterCreateRequest body =
        new AWSTagFilterCreateRequest()
            .accountId("123456789012")
            .namespace(AWSNamespace.ELB)
            .tagFilterStr("prod*");

    try {
      apiInstance.createAWSTagFilter(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createAWSTagFilter");
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
// Set an AWS tag filter returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSNamespace;
use datadog_api_client::datadogV1::model::AWSTagFilterCreateRequest;

#[tokio::main]
async fn main() {
    let body = AWSTagFilterCreateRequest::new()
        .account_id("123456789012".to_string())
        .namespace(AWSNamespace::ELB)
        .tag_filter_str("prod*".to_string());
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_aws_tag_filter(body).await;
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
 * Set an AWS tag filter returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiCreateAWSTagFilterRequest = {
  body: {
    accountId: "123456789012",
    namespace: "elb",
    tagFilterStr: "prod*",
  },
};

apiInstance
  .createAWSTagFilter(params)
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
## Delete a tag filtering entry{% #delete-a-tag-filtering-entry %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/aws/filtering |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/aws/filtering |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/aws/filtering      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/aws/filtering      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/aws/filtering     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/aws/filtering |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/aws/filtering |

### Overview

Delete a tag filtering entry. This endpoint requires the `aws_configuration_edit` permission.

### Request

#### Body Data (required)

Delete a tag filtering entry for a given AWS account and `dd-aws` namespace.

{% tab title="Model" %}

| Field      | Type   | Description                                                                                                                                     |
| ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | string | The unique identifier of your AWS account.                                                                                                      |
| namespace  | enum   | The namespace associated with the tag filter entry. Allowed enum values: `elb,application_elb,sqs,rds,custom,network_elb,lambda,step_functions` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "FAKEAC0FAKEAC2FAKEAC",
  "namespace": "string"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/filtering" \
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
Delete a tag filtering entry returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_namespace import AWSNamespace
from datadog_api_client.v1.model.aws_tag_filter_delete_request import AWSTagFilterDeleteRequest

body = AWSTagFilterDeleteRequest(
    account_id="FAKEAC0FAKEAC2FAKEAC",
    namespace=AWSNamespace.ELB,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_tag_filter(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a tag filtering entry returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSTagFilterDeleteRequest.new({
  account_id: "FAKEAC0FAKEAC2FAKEAC",
  namespace: DatadogAPIClient::V1::AWSNamespace::ELB,
})
p api_instance.delete_aws_tag_filter(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a tag filtering entry returns "OK" response

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
	body := datadogV1.AWSTagFilterDeleteRequest{
		AccountId: datadog.PtrString("FAKEAC0FAKEAC2FAKEAC"),
		Namespace: datadogV1.AWSNAMESPACE_ELB.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.DeleteAWSTagFilter(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.DeleteAWSTagFilter`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.DeleteAWSTagFilter`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a tag filtering entry returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSNamespace;
import com.datadog.api.client.v1.model.AWSTagFilterDeleteRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSTagFilterDeleteRequest body =
        new AWSTagFilterDeleteRequest()
            .accountId("FAKEAC0FAKEAC2FAKEAC")
            .namespace(AWSNamespace.ELB);

    try {
      apiInstance.deleteAWSTagFilter(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#deleteAWSTagFilter");
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
// Delete a tag filtering entry returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSNamespace;
use datadog_api_client::datadogV1::model::AWSTagFilterDeleteRequest;

#[tokio::main]
async fn main() {
    let body = AWSTagFilterDeleteRequest::new()
        .account_id("FAKEAC0FAKEAC2FAKEAC".to_string())
        .namespace(AWSNamespace::ELB);
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.delete_aws_tag_filter(body).await;
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
 * Delete a tag filtering entry returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiDeleteAWSTagFilterRequest = {
  body: {
    accountId: "FAKEAC0FAKEAC2FAKEAC",
    namespace: "elb",
  },
};

apiInstance
  .deleteAWSTagFilter(params)
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
## Get an AWS integration by config ID{% #get-an-aws-integration-by-config-id %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/accounts/{aws_account_config_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/accounts/{aws_account_config_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |

### Overview

Get an AWS Account Integration Config by config ID. This endpoint requires the `aws_configuration_read` permission.

### Arguments

#### Path Parameters

| Name                                    | Type   | Description                                                                                                                                                                                                                                               |
| --------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| aws_account_config_id [*required*] | string | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID. |

### Response

{% tab title="200" %}
AWS Account object
{% tab title="Model" %}
AWS Account response body.

| Parent field      | Field                                        | Type          | Description                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | data [*required*]                       | object        | AWS Account response data.                                                                                                                                                                                                                                                  |
| data              | attributes                                   | object        | AWS Account response attributes.                                                                                                                                                                                                                                            |
| attributes        | account_tags                                 | [string]      | Tags to apply to all hosts and metrics reporting for this account. Defaults to `[]`.                                                                                                                                                                                        |
| attributes        | auth_config                                  |  <oneOf> | AWS Authentication config.                                                                                                                                                                                                                                                  |
| auth_config       | Option 1                                     | object        | AWS Authentication config to integrate your account using an access key pair.                                                                                                                                                                                               |
| Option 1          | access_key_id [*required*]              | string        | AWS Access Key ID.                                                                                                                                                                                                                                                          |
| Option 1          | secret_access_key                            | string        | AWS Secret Access Key.                                                                                                                                                                                                                                                      |
| auth_config       | Option 2                                     | object        | AWS Authentication config to integrate your account using an IAM role.                                                                                                                                                                                                      |
| Option 2          | external_id                                  | string        | AWS IAM External ID for associated role.                                                                                                                                                                                                                                    |
| Option 2          | role_name [*required*]                  | string        | AWS IAM Role name.                                                                                                                                                                                                                                                          |
| attributes        | aws_account_id [*required*]             | string        | AWS Account ID.                                                                                                                                                                                                                                                             |
| attributes        | aws_partition                                | enum          | AWS partition your AWS account is scoped to. Defaults to `aws`. See [Partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) in the AWS documentation for more information. Allowed enum values: `aws,aws-cn,aws-us-gov` |
| attributes        | aws_regions                                  |  <oneOf> | AWS Regions to collect data from. Defaults to `include_all`.                                                                                                                                                                                                                |
| aws_regions       | Option 1                                     | object        | Include all regions. Defaults to `true`.                                                                                                                                                                                                                                    |
| Option 1          | include_all [*required*]                | boolean       | Include all regions.                                                                                                                                                                                                                                                        |
| aws_regions       | Option 2                                     | object        | Include only these regions.                                                                                                                                                                                                                                                 |
| Option 2          | include_only [*required*]               | [string]      | Include only these regions.                                                                                                                                                                                                                                                 |
| attributes        | created_at                                   | date-time     | Timestamp of when the account integration was created.                                                                                                                                                                                                                      |
| attributes        | logs_config                                  | object        | AWS Logs Collection config.                                                                                                                                                                                                                                                 |
| logs_config       | lambda_forwarder                             | object        | Log Autosubscription configuration for Datadog Forwarder Lambda functions. Automatically set up triggers for existing and new logs for some services, ensuring no logs from new resources are missed and saving time spent on manual configuration.                         |
| lambda_forwarder  | lambdas                                      | [string]      | List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to `[]`.                                                                                                                                                                                            |
| lambda_forwarder  | log_source_config                            | object        | Log source configuration.                                                                                                                                                                                                                                                   |
| log_source_config | tag_filters                                  | [object]      | List of AWS log source tag filters. Defaults to `[]`.                                                                                                                                                                                                                       |
| tag_filters       | source                                       | string        | The AWS log source to which the tag filters defined in `tags` are applied.                                                                                                                                                                                                  |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the log source specified by `source`.                                                                                                                                                                                                |
| lambda_forwarder  | sources                                      | [string]      | List of service IDs set to enable automatic log collection. Discover the list of available services with the [Get list of AWS log ready services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services) endpoint.                 |
| attributes        | metrics_config                               | object        | AWS Metrics Collection config.                                                                                                                                                                                                                                              |
| metrics_config    | automute_enabled                             | boolean       | Enable EC2 automute for AWS metrics. Defaults to `true`.                                                                                                                                                                                                                    |
| metrics_config    | collect_cloudwatch_alarms                    | boolean       | Enable CloudWatch alarms collection. Defaults to `false`.                                                                                                                                                                                                                   |
| metrics_config    | collect_custom_metrics                       | boolean       | Enable custom metrics collection. Defaults to `false`.                                                                                                                                                                                                                      |
| metrics_config    | enabled                                      | boolean       | Enable AWS metrics collection. Defaults to `true`.                                                                                                                                                                                                                          |
| metrics_config    | namespace_filters                            |  <oneOf> | AWS Metrics namespace filters. Defaults to `exclude_only`.                                                                                                                                                                                                                  |
| namespace_filters | Option 1                                     | object        | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| Option 1          | exclude_only [*required*]               | [string]      | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| namespace_filters | Option 2                                     | object        | Include only these namespaces.                                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these namespaces.                                                                                                                                                                                                                                              |
| metrics_config    | tag_filters                                  | [object]      | AWS Metrics collection tag filters list. Defaults to `[]`.                                                                                                                                                                                                                  |
| tag_filters       | namespace                                    | string        | The AWS service for which the tag filters defined in `tags` will be applied.                                                                                                                                                                                                |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the service specified by `namespace`.                                                                                                                                                                                                |
| attributes        | modified_at                                  | date-time     | Timestamp of when the account integration was updated.                                                                                                                                                                                                                      |
| attributes        | resources_config                             | object        | AWS Resources Collection config.                                                                                                                                                                                                                                            |
| resources_config  | cloud_security_posture_management_collection | boolean       | Enable Cloud Security Management to scan AWS resources for vulnerabilities, misconfigurations, identity risks, and compliance violations. Defaults to `false`. Requires `extended_collection` to be set to `true`.                                                          |
| resources_config  | extended_collection                          | boolean       | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Defaults to `true`. Required for `cloud_security_posture_management_collection`.                                                                      |
| attributes        | traces_config                                | object        | AWS Traces Collection config.                                                                                                                                                                                                                                               |
| traces_config     | xray_services                                |  <oneOf> | AWS X-Ray services to collect traces from. Defaults to `include_only`.                                                                                                                                                                                                      |
| xray_services     | Option 1                                     | object        | Include all services.                                                                                                                                                                                                                                                       |
| Option 1          | include_all [*required*]                | boolean       | Include all services.                                                                                                                                                                                                                                                       |
| xray_services     | Option 2                                     | object        | Include only these services. Defaults to `[]`.                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these services.                                                                                                                                                                                                                                                |
| data              | id [*required*]                         | string        | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID.                   |
| data              | type [*required*]                       | enum          | AWS Account resource type. Allowed enum values: `account`                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_tags": [
        "env:prod"
      ],
      "auth_config": {
        "access_key_id": "AKIAIOSFODNN7EXAMPLE",
        "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "aws_regions": {
        "include_all": true
      },
      "created_at": "2019-09-19T10:00:00.000Z",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "env:prod"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": false,
        "collect_custom_metrics": false,
        "enabled": true,
        "namespace_filters": {
          "exclude_only": [
            "AWS/SQS",
            "AWS/ElasticMapReduce",
            "AWS/Usage"
          ]
        },
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "datadog:true"
            ]
          }
        ]
      },
      "modified_at": "2019-09-19T10:00:00.000Z",
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": true
      },
      "traces_config": {
        "xray_services": {
          "include_all": false
        }
      }
    },
    "id": "00000000-abcd-0001-0000-000000000000",
    "type": "account"
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
                  \# Path parametersexport aws_account_config_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/accounts/${aws_account_config_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get an AWS integration by config ID returns "AWS Account object" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ID = environ["AWS_ACCOUNT_V2_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_account(
        aws_account_config_id=AWS_ACCOUNT_V2_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get an AWS integration by config ID returns "AWS Account object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ID = ENV["AWS_ACCOUNT_V2_DATA_ID"]
p api_instance.get_aws_account(AWS_ACCOUNT_V2_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get an AWS integration by config ID returns "AWS Account object" response

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
	// there is a valid "aws_account_v2" in the system
	AwsAccountV2DataID := os.Getenv("AWS_ACCOUNT_V2_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.GetAWSAccount(ctx, AwsAccountV2DataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.GetAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.GetAWSAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get an AWS integration by config ID returns "AWS Account object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSAccountResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    // there is a valid "aws_account_v2" in the system
    String AWS_ACCOUNT_V2_DATA_ID = System.getenv("AWS_ACCOUNT_V2_DATA_ID");

    try {
      AWSAccountResponse result = apiInstance.getAWSAccount(AWS_ACCOUNT_V2_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#getAWSAccount");
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
// Get an AWS integration by config ID returns "AWS Account object" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "aws_account_v2" in the system
    let aws_account_v2_data_id = std::env::var("AWS_ACCOUNT_V2_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.get_aws_account(aws_account_v2_data_id.clone()).await;
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
 * Get an AWS integration by config ID returns "AWS Account object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

// there is a valid "aws_account_v2" in the system
const AWS_ACCOUNT_V2_DATA_ID = process.env.AWS_ACCOUNT_V2_DATA_ID as string;

const params: v2.AWSIntegrationApiGetAWSAccountRequest = {
  awsAccountConfigId: AWS_ACCOUNT_V2_DATA_ID,
};

apiInstance
  .getAWSAccount(params)
  .then((data: v2.AWSAccountResponse) => {
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

## Generate a new external ID{% #generate-a-new-external-id %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/integration/aws/generate_new_external_id |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/integration/aws/generate_new_external_id |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/integration/aws/generate_new_external_id      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/integration/aws/generate_new_external_id      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/integration/aws/generate_new_external_id     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/integration/aws/generate_new_external_id |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/integration/aws/generate_new_external_id |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** Generate a new AWS external ID for a given AWS account ID and role name pair. This endpoint requires the `aws_configuration_edit` permission.

### Request

#### Body Data (required)

Your Datadog role delegation name. For more information about your AWS account Role name, see the [Datadog AWS integration configuration info](https://docs.datadoghq.com/integrations/amazon_web_services/#setup).

{% tab title="Model" %}

| Parent field         | Field                                | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | access_key_id                        | string   | Your AWS access key ID. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | account_id                           | string   | Your AWS Account ID without dashes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                      | account_specific_namespace_rules     | object   | An object (in the form `{"namespace1":true/false, "namespace2":true/false}`) containing user-supplied overrides for AWS namespace metric collection. **Important**: This field only contains namespaces explicitly configured through API calls, not the comprehensive enabled or disabled status of all namespaces. If a namespace is absent from this field, it uses Datadog's internal defaults (all namespaces enabled by default, except `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage`). For a complete view of all namespace statuses, use the V2 AWS Integration API instead. |
| additionalProperties | <any-key>                            | boolean  | A list of additional properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                      | cspm_resource_collection_enabled     | boolean  | Whether Datadog collects cloud security posture management resources from your AWS account. This includes additional resources not covered under the general `resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                       |
|                      | excluded_regions                     | [string] | An array of [AWS regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) to exclude from metrics collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | extended_resource_collection_enabled | boolean  | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Required for `cspm_resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | filter_tags                          | [string] | The array of EC2 tags (in the form `key:value`) defines a filter that Datadog uses when collecting metrics from EC2. Wildcards, such as `?` (for single characters) and `*` (for multiple characters) can also be used. Only hosts that match one of the defined tags will be imported into Datadog. The rest will be ignored. Host matching a given tag can also be excluded by adding `!` before the tag. For example, `env:production,instance-type:c1.*,!region:us-east-1`                                                                                                            |
|                      | host_tags                            | [string] | Array of tags (in the form `key:value`) to add to all hosts and metrics reporting through this integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | metrics_collection_enabled           | boolean  | Whether Datadog collects metrics for this AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | resource_collection_enabled          | boolean  | **DEPRECATED**: Deprecated in favor of 'extended_resource_collection_enabled'. Whether Datadog collects a standard set of resources from your AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | role_name                            | string   | Your Datadog role delegation name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | secret_access_key                    | string   | Your AWS secret access key. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "access_key_id": "string",
  "account_id": "123456789012",
  "account_specific_namespace_rules": {
    "<any-key>": false
  },
  "cspm_resource_collection_enabled": true,
  "excluded_regions": [
    "us-east-1",
    "us-west-2"
  ],
  "extended_resource_collection_enabled": true,
  "filter_tags": [
    "$KEY:$VALUE"
  ],
  "host_tags": [
    "$KEY:$VALUE"
  ],
  "metrics_collection_enabled": false,
  "resource_collection_enabled": true,
  "role_name": "DatadogAWSIntegrationRole",
  "secret_access_key": "string"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The Response returned by the AWS Create Account call.

| Field       | Type   | Description      |
| ----------- | ------ | ---------------- |
| external_id | string | AWS external_id. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "external_id": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/generate_new_external_id" \
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
Generate a new external ID returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_account import AWSAccount

body = AWSAccount(
    account_id="123456789012",
    account_specific_namespace_rules=dict(
        auto_scaling=False,
        opswork=False,
    ),
    cspm_resource_collection_enabled=True,
    excluded_regions=[
        "us-east-1",
        "us-west-2",
    ],
    extended_resource_collection_enabled=True,
    filter_tags=[
        "$KEY:$VALUE",
    ],
    host_tags=[
        "$KEY:$VALUE",
    ],
    metrics_collection_enabled=False,
    resource_collection_enabled=True,
    role_name="DatadogAWSIntegrationRole",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_new_aws_external_id(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Generate a new external ID returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccount.new({
  account_id: "123456789012",
  account_specific_namespace_rules: {
    auto_scaling: false, opswork: false,
  },
  cspm_resource_collection_enabled: true,
  excluded_regions: [
    "us-east-1",
    "us-west-2",
  ],
  extended_resource_collection_enabled: true,
  filter_tags: [
    "$KEY:$VALUE",
  ],
  host_tags: [
    "$KEY:$VALUE",
  ],
  metrics_collection_enabled: false,
  resource_collection_enabled: true,
  role_name: "DatadogAWSIntegrationRole",
})
p api_instance.create_new_aws_external_id(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Generate a new external ID returns "OK" response

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
	body := datadogV1.AWSAccount{
		AccountId: datadog.PtrString("123456789012"),
		AccountSpecificNamespaceRules: map[string]bool{
			"auto_scaling": false,
			"opswork":      false,
		},
		CspmResourceCollectionEnabled: datadog.PtrBool(true),
		ExcludedRegions: []string{
			"us-east-1",
			"us-west-2",
		},
		ExtendedResourceCollectionEnabled: datadog.PtrBool(true),
		FilterTags: []string{
			"$KEY:$VALUE",
		},
		HostTags: []string{
			"$KEY:$VALUE",
		},
		MetricsCollectionEnabled:  datadog.PtrBool(false),
		ResourceCollectionEnabled: datadog.PtrBool(true),
		RoleName:                  datadog.PtrString("DatadogAWSIntegrationRole"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateNewAWSExternalID(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateNewAWSExternalID`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateNewAWSExternalID`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Generate a new external ID returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSAccount;
import com.datadog.api.client.v1.model.AWSAccountCreateResponse;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSAccount body =
        new AWSAccount()
            .accountId("123456789012")
            .accountSpecificNamespaceRules(
                Map.ofEntries(Map.entry("auto_scaling", false), Map.entry("opswork", false)))
            .cspmResourceCollectionEnabled(true)
            .excludedRegions(Arrays.asList("us-east-1", "us-west-2"))
            .extendedResourceCollectionEnabled(true)
            .filterTags(Collections.singletonList("$KEY:$VALUE"))
            .hostTags(Collections.singletonList("$KEY:$VALUE"))
            .metricsCollectionEnabled(false)
            .resourceCollectionEnabled(true)
            .roleName("DatadogAWSIntegrationRole");

    try {
      AWSAccountCreateResponse result = apiInstance.createNewAWSExternalID(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createNewAWSExternalID");
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
// Generate a new external ID returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSAccount;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = AWSAccount::new()
        .account_id("123456789012".to_string())
        .account_specific_namespace_rules(BTreeMap::from([
            ("auto_scaling".to_string(), false),
            ("opswork".to_string(), false),
        ]))
        .cspm_resource_collection_enabled(true)
        .excluded_regions(vec!["us-east-1".to_string(), "us-west-2".to_string()])
        .extended_resource_collection_enabled(true)
        .filter_tags(vec!["$KEY:$VALUE".to_string()])
        .host_tags(vec!["$KEY:$VALUE".to_string()])
        .metrics_collection_enabled(false)
        .resource_collection_enabled(true)
        .role_name("DatadogAWSIntegrationRole".to_string());
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_new_aws_external_id(body).await;
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
 * Generate a new external ID returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiCreateNewAWSExternalIDRequest = {
  body: {
    accountId: "123456789012",
    accountSpecificNamespaceRules: {
      auto_scaling: false,
      opswork: false,
    },
    cspmResourceCollectionEnabled: true,
    excludedRegions: ["us-east-1", "us-west-2"],
    extendedResourceCollectionEnabled: true,
    filterTags: ["$KEY:$VALUE"],
    hostTags: ["$KEY:$VALUE"],
    metricsCollectionEnabled: false,
    resourceCollectionEnabled: true,
    roleName: "DatadogAWSIntegrationRole",
  },
};

apiInstance
  .createNewAWSExternalID(params)
  .then((data: v1.AWSAccountCreateResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/aws/generate_new_external_id |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/aws/generate_new_external_id |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/aws/generate_new_external_id      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/aws/generate_new_external_id      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/aws/generate_new_external_id     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/aws/generate_new_external_id |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/aws/generate_new_external_id |

### Overview

Generate a new external ID for AWS role-based authentication. This endpoint requires the `aws_configuration_edit` permission.

### Response

{% tab title="200" %}
AWS External ID object
{% tab title="Model" %}
AWS External ID response body.

| Parent field | Field                         | Type   | Description                                                                   |
| ------------ | ----------------------------- | ------ | ----------------------------------------------------------------------------- |
|              | data [*required*]        | object | AWS External ID response body.                                                |
| data         | attributes                    | object | AWS External ID response body.                                                |
| attributes   | external_id [*required*] | string | AWS IAM External ID for associated role.                                      |
| data         | id [*required*]          | string | The `AWSNewExternalIDResponseData` `id`.                                      |
| data         | type [*required*]        | enum   | The `AWSNewExternalIDResponseData` `type`. Allowed enum values: `external_id` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "external_id": "acb8f6b8a844443dbb726d07dcb1a870"
    },
    "id": "external_id",
    "type": "external_id"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/generate_new_external_id" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Generate a new external ID returns "AWS External ID object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_new_aws_external_id()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Generate a new external ID returns "AWS External ID object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new
p api_instance.create_new_aws_external_id()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Generate a new external ID returns "AWS External ID object" response

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
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateNewAWSExternalID(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateNewAWSExternalID`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateNewAWSExternalID`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Generate a new external ID returns "AWS External ID object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSNewExternalIDResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSNewExternalIDResponse result = apiInstance.createNewAWSExternalID();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createNewAWSExternalID");
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
// Generate a new external ID returns "AWS External ID object" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_new_aws_external_id().await;
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
 * Generate a new external ID returns "AWS External ID object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

apiInstance
  .createNewAWSExternalID()
  .then((data: v2.AWSNewExternalIDResponse) => {
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

## List namespace rules{% #list-namespace-rules %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/aws/available_namespace_rules |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/aws/available_namespace_rules |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/aws/available_namespace_rules      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/aws/available_namespace_rules      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/aws/available_namespace_rules |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/aws/available_namespace_rules |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** List all namespace rules for a given Datadog-AWS integration. This endpoint takes no arguments. This endpoint requires the `aws_configuration_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type   | Description |
| ----- | ------ | ----------- |
|       | string |

{% /tab %}

{% tab title="Example" %}

```json
[
  "namespace1",
  "namespace2",
  "namespace3"
]
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/available_namespace_rules" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List namespace rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_available_aws_namespaces()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List namespace rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new
p api_instance.list_available_aws_namespaces()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.aws_integration_list_namespaces
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List namespace rules returns "OK" response

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
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.ListAvailableAWSNamespaces(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.ListAvailableAWSNamespaces`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.ListAvailableAWSNamespaces`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List namespace rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      List<String> result = apiInstance.listAvailableAWSNamespaces();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#listAvailableAWSNamespaces");
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

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AwsIntegration.list_namespace_rules()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
##### 

```rust
// List namespace rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.list_available_aws_namespaces().await;
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
 * List namespace rules returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

apiInstance
  .listAvailableAWSNamespaces()
  .then((data: string[]) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
## Get AWS integration IAM permissions{% #get-aws-integration-iam-permissions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/iam_permissions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/iam_permissions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/iam_permissions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/iam_permissions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/iam_permissions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/iam_permissions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/iam_permissions |

### Overview

Get all AWS IAM permissions required for the AWS integration.

### Response

{% tab title="200" %}
AWS IAM Permissions object
{% tab title="Model" %}
AWS Integration IAM Permissions response body.

| Parent field | Field                         | Type     | Description                                                                               |
| ------------ | ----------------------------- | -------- | ----------------------------------------------------------------------------------------- |
|              | data [*required*]        | object   | AWS Integration IAM Permissions response data.                                            |
| data         | attributes                    | object   | AWS Integration IAM Permissions response attributes.                                      |
| attributes   | permissions [*required*] | [string] | List of AWS IAM permissions required for the integration.                                 |
| data         | id                            | string   | The `AWSIntegrationIamPermissionsResponseData` `id`.                                      |
| data         | type                          | enum     | The `AWSIntegrationIamPermissionsResponseData` `type`. Allowed enum values: `permissions` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "permissions": [
        "account:GetContactInformation",
        "amplify:ListApps",
        "amplify:ListArtifacts",
        "amplify:ListBackendEnvironments",
        "amplify:ListBranches"
      ]
    },
    "id": "permissions",
    "type": "permissions"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/iam_permissions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get AWS integration IAM permissions returns "AWS IAM Permissions object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_integration_iam_permissions()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get AWS integration IAM permissions returns "AWS IAM Permissions object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new
p api_instance.get_aws_integration_iam_permissions()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get AWS integration IAM permissions returns "AWS IAM Permissions object" response

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
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.GetAWSIntegrationIAMPermissions(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.GetAWSIntegrationIAMPermissions`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.GetAWSIntegrationIAMPermissions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get AWS integration IAM permissions returns "AWS IAM Permissions object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSIntegrationIamPermissionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSIntegrationIamPermissionsResponse result = apiInstance.getAWSIntegrationIAMPermissions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling AwsIntegrationApi#getAWSIntegrationIAMPermissions");
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
// Get AWS integration IAM permissions returns "AWS IAM Permissions object"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.get_aws_integration_iam_permissions().await;
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
 * Get AWS integration IAM permissions returns "AWS IAM Permissions object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

apiInstance
  .getAWSIntegrationIAMPermissions()
  .then((data: v2.AWSIntegrationIamPermissionsResponse) => {
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

## List all AWS integrations{% #list-all-aws-integrations %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/aws |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/aws |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/aws      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/aws      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/aws     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/aws |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/aws |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** List all Datadog-AWS integrations available in your Datadog organization. This endpoint requires the `aws_configuration_read` permission.

### Arguments

#### Query Strings

| Name          | Type   | Description                                                 |
| ------------- | ------ | ----------------------------------------------------------- |
| account_id    | string | Only return AWS accounts that matches this `account_id`.    |
| role_name     | string | Only return AWS accounts that matches this role_name.       |
| access_key_id | string | Only return AWS accounts that matches this `access_key_id`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of enabled AWS accounts.

| Parent field         | Field                                | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | accounts                             | [object] | List of enabled AWS accounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| accounts             | access_key_id                        | string   | Your AWS access key ID. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| accounts             | account_id                           | string   | Your AWS Account ID without dashes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| accounts             | account_specific_namespace_rules     | object   | An object (in the form `{"namespace1":true/false, "namespace2":true/false}`) containing user-supplied overrides for AWS namespace metric collection. **Important**: This field only contains namespaces explicitly configured through API calls, not the comprehensive enabled or disabled status of all namespaces. If a namespace is absent from this field, it uses Datadog's internal defaults (all namespaces enabled by default, except `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage`). For a complete view of all namespace statuses, use the V2 AWS Integration API instead. |
| additionalProperties | <any-key>                            | boolean  | A list of additional properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| accounts             | cspm_resource_collection_enabled     | boolean  | Whether Datadog collects cloud security posture management resources from your AWS account. This includes additional resources not covered under the general `resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                       |
| accounts             | excluded_regions                     | [string] | An array of [AWS regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) to exclude from metrics collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| accounts             | extended_resource_collection_enabled | boolean  | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Required for `cspm_resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| accounts             | filter_tags                          | [string] | The array of EC2 tags (in the form `key:value`) defines a filter that Datadog uses when collecting metrics from EC2. Wildcards, such as `?` (for single characters) and `*` (for multiple characters) can also be used. Only hosts that match one of the defined tags will be imported into Datadog. The rest will be ignored. Host matching a given tag can also be excluded by adding `!` before the tag. For example, `env:production,instance-type:c1.*,!region:us-east-1`                                                                                                            |
| accounts             | host_tags                            | [string] | Array of tags (in the form `key:value`) to add to all hosts and metrics reporting through this integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| accounts             | metrics_collection_enabled           | boolean  | Whether Datadog collects metrics for this AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| accounts             | resource_collection_enabled          | boolean  | **DEPRECATED**: Deprecated in favor of 'extended_resource_collection_enabled'. Whether Datadog collects a standard set of resources from your AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| accounts             | role_name                            | string   | Your Datadog role delegation name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| accounts             | secret_access_key                    | string   | Your AWS secret access key. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "accounts": [
    {
      "access_key_id": "string",
      "account_id": "123456789012",
      "account_specific_namespace_rules": {
        "<any-key>": false
      },
      "cspm_resource_collection_enabled": true,
      "excluded_regions": [
        "us-east-1",
        "us-west-2"
      ],
      "extended_resource_collection_enabled": true,
      "filter_tags": [
        "$KEY:$VALUE"
      ],
      "host_tags": [
        "$KEY:$VALUE"
      ],
      "metrics_collection_enabled": false,
      "resource_collection_enabled": true,
      "role_name": "DatadogAWSIntegrationRole",
      "secret_access_key": "string"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List all AWS integrations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_aws_accounts()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List all AWS integrations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new
p api_instance.list_aws_accounts()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.aws_integration_list
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List all AWS integrations returns "OK" response

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
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.ListAWSAccounts(ctx, *datadogV1.NewListAWSAccountsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.ListAWSAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.ListAWSAccounts`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List all AWS integrations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSAccountListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSAccountListResponse result = apiInstance.listAWSAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#listAWSAccounts");
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

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AwsIntegration.list()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
##### 

```rust
// List all AWS integrations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::api_aws_integration::ListAWSAccountsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api
        .list_aws_accounts(ListAWSAccountsOptionalParams::default())
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
 * List all AWS integrations returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

apiInstance
  .listAWSAccounts()
  .then((data: v1.AWSAccountListResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/accounts |

### Overview

Get a list of AWS Account Integration Configs. This endpoint requires the `aws_configuration_read` permission.

### Arguments

#### Query Strings

| Name           | Type   | Description                                                                                                |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| aws_account_id | string | Optional query parameter to filter accounts by AWS Account ID. If not provided, all accounts are returned. |

### Response

{% tab title="200" %}
AWS Accounts List object
{% tab title="Model" %}
AWS Accounts response body.

| Parent field      | Field                                        | Type          | Description                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | data [*required*]                       | [object]      | List of AWS Account Integration Configs.                                                                                                                                                                                                                                    |
| data              | attributes                                   | object        | AWS Account response attributes.                                                                                                                                                                                                                                            |
| attributes        | account_tags                                 | [string]      | Tags to apply to all hosts and metrics reporting for this account. Defaults to `[]`.                                                                                                                                                                                        |
| attributes        | auth_config                                  |  <oneOf> | AWS Authentication config.                                                                                                                                                                                                                                                  |
| auth_config       | Option 1                                     | object        | AWS Authentication config to integrate your account using an access key pair.                                                                                                                                                                                               |
| Option 1          | access_key_id [*required*]              | string        | AWS Access Key ID.                                                                                                                                                                                                                                                          |
| Option 1          | secret_access_key                            | string        | AWS Secret Access Key.                                                                                                                                                                                                                                                      |
| auth_config       | Option 2                                     | object        | AWS Authentication config to integrate your account using an IAM role.                                                                                                                                                                                                      |
| Option 2          | external_id                                  | string        | AWS IAM External ID for associated role.                                                                                                                                                                                                                                    |
| Option 2          | role_name [*required*]                  | string        | AWS IAM Role name.                                                                                                                                                                                                                                                          |
| attributes        | aws_account_id [*required*]             | string        | AWS Account ID.                                                                                                                                                                                                                                                             |
| attributes        | aws_partition                                | enum          | AWS partition your AWS account is scoped to. Defaults to `aws`. See [Partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) in the AWS documentation for more information. Allowed enum values: `aws,aws-cn,aws-us-gov` |
| attributes        | aws_regions                                  |  <oneOf> | AWS Regions to collect data from. Defaults to `include_all`.                                                                                                                                                                                                                |
| aws_regions       | Option 1                                     | object        | Include all regions. Defaults to `true`.                                                                                                                                                                                                                                    |
| Option 1          | include_all [*required*]                | boolean       | Include all regions.                                                                                                                                                                                                                                                        |
| aws_regions       | Option 2                                     | object        | Include only these regions.                                                                                                                                                                                                                                                 |
| Option 2          | include_only [*required*]               | [string]      | Include only these regions.                                                                                                                                                                                                                                                 |
| attributes        | created_at                                   | date-time     | Timestamp of when the account integration was created.                                                                                                                                                                                                                      |
| attributes        | logs_config                                  | object        | AWS Logs Collection config.                                                                                                                                                                                                                                                 |
| logs_config       | lambda_forwarder                             | object        | Log Autosubscription configuration for Datadog Forwarder Lambda functions. Automatically set up triggers for existing and new logs for some services, ensuring no logs from new resources are missed and saving time spent on manual configuration.                         |
| lambda_forwarder  | lambdas                                      | [string]      | List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to `[]`.                                                                                                                                                                                            |
| lambda_forwarder  | log_source_config                            | object        | Log source configuration.                                                                                                                                                                                                                                                   |
| log_source_config | tag_filters                                  | [object]      | List of AWS log source tag filters. Defaults to `[]`.                                                                                                                                                                                                                       |
| tag_filters       | source                                       | string        | The AWS log source to which the tag filters defined in `tags` are applied.                                                                                                                                                                                                  |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the log source specified by `source`.                                                                                                                                                                                                |
| lambda_forwarder  | sources                                      | [string]      | List of service IDs set to enable automatic log collection. Discover the list of available services with the [Get list of AWS log ready services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services) endpoint.                 |
| attributes        | metrics_config                               | object        | AWS Metrics Collection config.                                                                                                                                                                                                                                              |
| metrics_config    | automute_enabled                             | boolean       | Enable EC2 automute for AWS metrics. Defaults to `true`.                                                                                                                                                                                                                    |
| metrics_config    | collect_cloudwatch_alarms                    | boolean       | Enable CloudWatch alarms collection. Defaults to `false`.                                                                                                                                                                                                                   |
| metrics_config    | collect_custom_metrics                       | boolean       | Enable custom metrics collection. Defaults to `false`.                                                                                                                                                                                                                      |
| metrics_config    | enabled                                      | boolean       | Enable AWS metrics collection. Defaults to `true`.                                                                                                                                                                                                                          |
| metrics_config    | namespace_filters                            |  <oneOf> | AWS Metrics namespace filters. Defaults to `exclude_only`.                                                                                                                                                                                                                  |
| namespace_filters | Option 1                                     | object        | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| Option 1          | exclude_only [*required*]               | [string]      | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| namespace_filters | Option 2                                     | object        | Include only these namespaces.                                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these namespaces.                                                                                                                                                                                                                                              |
| metrics_config    | tag_filters                                  | [object]      | AWS Metrics collection tag filters list. Defaults to `[]`.                                                                                                                                                                                                                  |
| tag_filters       | namespace                                    | string        | The AWS service for which the tag filters defined in `tags` will be applied.                                                                                                                                                                                                |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the service specified by `namespace`.                                                                                                                                                                                                |
| attributes        | modified_at                                  | date-time     | Timestamp of when the account integration was updated.                                                                                                                                                                                                                      |
| attributes        | resources_config                             | object        | AWS Resources Collection config.                                                                                                                                                                                                                                            |
| resources_config  | cloud_security_posture_management_collection | boolean       | Enable Cloud Security Management to scan AWS resources for vulnerabilities, misconfigurations, identity risks, and compliance violations. Defaults to `false`. Requires `extended_collection` to be set to `true`.                                                          |
| resources_config  | extended_collection                          | boolean       | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Defaults to `true`. Required for `cloud_security_posture_management_collection`.                                                                      |
| attributes        | traces_config                                | object        | AWS Traces Collection config.                                                                                                                                                                                                                                               |
| traces_config     | xray_services                                |  <oneOf> | AWS X-Ray services to collect traces from. Defaults to `include_only`.                                                                                                                                                                                                      |
| xray_services     | Option 1                                     | object        | Include all services.                                                                                                                                                                                                                                                       |
| Option 1          | include_all [*required*]                | boolean       | Include all services.                                                                                                                                                                                                                                                       |
| xray_services     | Option 2                                     | object        | Include only these services. Defaults to `[]`.                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these services.                                                                                                                                                                                                                                                |
| data              | id [*required*]                         | string        | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID.                   |
| data              | type [*required*]                       | enum          | AWS Account resource type. Allowed enum values: `account`                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "account_tags": [
          "env:prod"
        ],
        "auth_config": {
          "access_key_id": "AKIAIOSFODNN7EXAMPLE",
          "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        },
        "aws_account_id": "123456789012",
        "aws_partition": "aws",
        "aws_regions": {
          "include_all": true
        },
        "created_at": "2019-09-19T10:00:00.000Z",
        "logs_config": {
          "lambda_forwarder": {
            "lambdas": [
              "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
            ],
            "log_source_config": {
              "tag_filters": [
                {
                  "source": "s3",
                  "tags": [
                    "env:prod"
                  ]
                }
              ]
            },
            "sources": [
              "s3"
            ]
          }
        },
        "metrics_config": {
          "automute_enabled": true,
          "collect_cloudwatch_alarms": false,
          "collect_custom_metrics": false,
          "enabled": true,
          "namespace_filters": {
            "exclude_only": [
              "AWS/SQS",
              "AWS/ElasticMapReduce",
              "AWS/Usage"
            ]
          },
          "tag_filters": [
            {
              "namespace": "AWS/EC2",
              "tags": [
                "datadog:true"
              ]
            }
          ]
        },
        "modified_at": "2019-09-19T10:00:00.000Z",
        "resources_config": {
          "cloud_security_posture_management_collection": false,
          "extended_collection": true
        },
        "traces_config": {
          "xray_services": {
            "include_all": false
          }
        }
      },
      "id": "00000000-abcd-0001-0000-000000000000",
      "type": "account"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List all AWS integrations returns "AWS Accounts List object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_aws_accounts()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List all AWS integrations returns "AWS Accounts List object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new
p api_instance.list_aws_accounts()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List all AWS integrations returns "AWS Accounts List object" response

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
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.ListAWSAccounts(ctx, *datadogV2.NewListAWSAccountsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.ListAWSAccounts`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.ListAWSAccounts`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List all AWS integrations returns "AWS Accounts List object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSAccountsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSAccountsResponse result = apiInstance.listAWSAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#listAWSAccounts");
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
// List all AWS integrations returns "AWS Accounts List object" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV2::api_aws_integration::ListAWSAccountsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api
        .list_aws_accounts(ListAWSAccountsOptionalParams::default())
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
 * List all AWS integrations returns "AWS Accounts List object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

apiInstance
  .listAWSAccounts()
  .then((data: v2.AWSAccountsResponse) => {
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

## Delete an AWS integration{% #delete-an-aws-integration %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                |
| ----------------- | ----------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/aws |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/aws |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/aws      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/aws      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/aws     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/aws |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/aws |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** Delete a Datadog-AWS integration matching the specified `account_id` and `role_name parameters`. This endpoint requires the `aws_configurations_manage` permission.

### Request

#### Body Data (required)

AWS request object

{% tab title="Model" %}

| Field         | Type   | Description                                                                               |
| ------------- | ------ | ----------------------------------------------------------------------------------------- |
| access_key_id | string | Your AWS access key ID. Only required if your AWS account is a GovCloud or China account. |
| account_id    | string | Your AWS Account ID without dashes.                                                       |
| role_name     | string | Your Datadog role delegation name.                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "163662907100",
  "role_name": "DatadogAWSIntegrationRole"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="409" %}
Conflict Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                          \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "163662907100",
  "role_name": "DatadogAWSIntegrationRole"
}
EOF
                        
##### 

```go
// Delete an AWS integration returns "OK" response

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
	body := datadogV1.AWSAccountDeleteRequest{
		AccountId: datadog.PtrString("163662907100"),
		RoleName:  datadog.PtrString("DatadogAWSIntegrationRole"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.DeleteAWSAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.DeleteAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.DeleteAWSAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete an AWS integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSAccountDeleteRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSAccountDeleteRequest body =
        new AWSAccountDeleteRequest()
            .accountId("163662907100")
            .roleName("DatadogAWSIntegrationRole");

    try {
      apiInstance.deleteAWSAccount(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#deleteAWSAccount");
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

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

account_id = "<AWS_ACCOUNT_ID>"
role_name = "<AWS_ROLE_NAME>"

api.AwsIntegration.delete(account_id=account_id, role_name=role_name)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
##### 

```python
"""
Delete an AWS integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_account_delete_request import AWSAccountDeleteRequest

body = AWSAccountDeleteRequest(
    account_id="163662907100",
    role_name="DatadogAWSIntegrationRole",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_account(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

config = {
  "account_id": '<AWS_ACCOUNT_ID>',
  "role_name": 'DatadogAWSIntegrationRole'
}

dog = Dogapi::Client.new(api_key, app_key)

dog.aws_integration_delete(config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```ruby
# Delete an AWS integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccountDeleteRequest.new({
  account_id: "163662907100",
  role_name: "DatadogAWSIntegrationRole",
})
p api_instance.delete_aws_account(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Delete an AWS integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSAccountDeleteRequest;

#[tokio::main]
async fn main() {
    let body = AWSAccountDeleteRequest::new()
        .account_id("163662907100".to_string())
        .role_name("DatadogAWSIntegrationRole".to_string());
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.delete_aws_account(body).await;
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
 * Delete an AWS integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiDeleteAWSAccountRequest = {
  body: {
    accountId: "163662907100",
    roleName: "DatadogAWSIntegrationRole",
  },
};

apiInstance
  .deleteAWSAccount(params)
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/aws/accounts/{aws_account_config_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/aws/accounts/{aws_account_config_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |

### Overview

Delete an AWS Account Integration Config by config ID. This endpoint requires the `aws_configurations_manage` permission.

### Arguments

#### Path Parameters

| Name                                    | Type   | Description                                                                                                                                                                                                                                               |
| --------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| aws_account_config_id [*required*] | string | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID. |

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
                  \# Path parametersexport aws_account_config_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/accounts/${aws_account_config_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete an AWS integration returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ID = environ["AWS_ACCOUNT_V2_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    api_instance.delete_aws_account(
        aws_account_config_id=AWS_ACCOUNT_V2_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an AWS integration returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ID = ENV["AWS_ACCOUNT_V2_DATA_ID"]
api_instance.delete_aws_account(AWS_ACCOUNT_V2_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete an AWS integration returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "aws_account_v2" in the system
	AwsAccountV2DataID := os.Getenv("AWS_ACCOUNT_V2_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	r, err := api.DeleteAWSAccount(ctx, AwsAccountV2DataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.DeleteAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete an AWS integration returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    // there is a valid "aws_account_v2" in the system
    String AWS_ACCOUNT_V2_DATA_ID = System.getenv("AWS_ACCOUNT_V2_DATA_ID");

    try {
      apiInstance.deleteAWSAccount(AWS_ACCOUNT_V2_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#deleteAWSAccount");
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
// Delete an AWS integration returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    // there is a valid "aws_account_v2" in the system
    let aws_account_v2_data_id = std::env::var("AWS_ACCOUNT_V2_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.delete_aws_account(aws_account_v2_data_id.clone()).await;
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
 * Delete an AWS integration returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

// there is a valid "aws_account_v2" in the system
const AWS_ACCOUNT_V2_DATA_ID = process.env.AWS_ACCOUNT_V2_DATA_ID as string;

const params: v2.AWSIntegrationApiDeleteAWSAccountRequest = {
  awsAccountConfigId: AWS_ACCOUNT_V2_DATA_ID,
};

apiInstance
  .deleteAWSAccount(params)
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

## Get AWS integration standard IAM permissions{% #get-aws-integration-standard-iam-permissions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/iam_permissions/standard |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/iam_permissions/standard |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/iam_permissions/standard      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/iam_permissions/standard      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/iam_permissions/standard     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/iam_permissions/standard |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/iam_permissions/standard |

### Overview

Get all standard AWS IAM permissions required for the AWS integration.

### Response

{% tab title="200" %}
AWS integration standard IAM permissions.
{% tab title="Model" %}
AWS Integration IAM Permissions response body.

| Parent field | Field                         | Type     | Description                                                                               |
| ------------ | ----------------------------- | -------- | ----------------------------------------------------------------------------------------- |
|              | data [*required*]        | object   | AWS Integration IAM Permissions response data.                                            |
| data         | attributes                    | object   | AWS Integration IAM Permissions response attributes.                                      |
| attributes   | permissions [*required*] | [string] | List of AWS IAM permissions required for the integration.                                 |
| data         | id                            | string   | The `AWSIntegrationIamPermissionsResponseData` `id`.                                      |
| data         | type                          | enum     | The `AWSIntegrationIamPermissionsResponseData` `type`. Allowed enum values: `permissions` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "permissions": [
        "account:GetContactInformation",
        "amplify:ListApps",
        "amplify:ListArtifacts",
        "amplify:ListBackendEnvironments",
        "amplify:ListBranches"
      ]
    },
    "id": "permissions",
    "type": "permissions"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/iam_permissions/standard" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get AWS integration standard IAM permissions returns "AWS integration standard IAM permissions." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_integration_iam_permissions_standard()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get AWS integration standard IAM permissions returns "AWS integration standard IAM permissions." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new
p api_instance.get_aws_integration_iam_permissions_standard()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get AWS integration standard IAM permissions returns "AWS integration standard IAM permissions." response

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
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.GetAWSIntegrationIAMPermissionsStandard(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.GetAWSIntegrationIAMPermissionsStandard`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.GetAWSIntegrationIAMPermissionsStandard`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get AWS integration standard IAM permissions returns "AWS integration standard IAM permissions."
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSIntegrationIamPermissionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSIntegrationIamPermissionsResponse result =
          apiInstance.getAWSIntegrationIAMPermissionsStandard();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling AwsIntegrationApi#getAWSIntegrationIAMPermissionsStandard");
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
// Get AWS integration standard IAM permissions returns "AWS integration standard
// IAM permissions." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.get_aws_integration_iam_permissions_standard().await;
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
 * Get AWS integration standard IAM permissions returns "AWS integration standard IAM permissions." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

apiInstance
  .getAWSIntegrationIAMPermissionsStandard()
  .then((data: v2.AWSIntegrationIamPermissionsResponse) => {
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

## Create an AWS integration{% #create-an-aws-integration %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/aws |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/aws |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/aws      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/aws      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/aws     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/aws |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/aws |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** Create a Datadog-Amazon Web Services integration. Using the `POST` method updates your integration configuration by adding your new configuration to the existing one in your Datadog organization. A unique AWS Account ID for role based authentication. This endpoint requires the `aws_configurations_manage` permission.

### Request

#### Body Data (required)

AWS Request Object

{% tab title="Model" %}

| Parent field         | Field                                | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | access_key_id                        | string   | Your AWS access key ID. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | account_id                           | string   | Your AWS Account ID without dashes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                      | account_specific_namespace_rules     | object   | An object (in the form `{"namespace1":true/false, "namespace2":true/false}`) containing user-supplied overrides for AWS namespace metric collection. **Important**: This field only contains namespaces explicitly configured through API calls, not the comprehensive enabled or disabled status of all namespaces. If a namespace is absent from this field, it uses Datadog's internal defaults (all namespaces enabled by default, except `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage`). For a complete view of all namespace statuses, use the V2 AWS Integration API instead. |
| additionalProperties | <any-key>                            | boolean  | A list of additional properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                      | cspm_resource_collection_enabled     | boolean  | Whether Datadog collects cloud security posture management resources from your AWS account. This includes additional resources not covered under the general `resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                       |
|                      | excluded_regions                     | [string] | An array of [AWS regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) to exclude from metrics collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | extended_resource_collection_enabled | boolean  | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Required for `cspm_resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | filter_tags                          | [string] | The array of EC2 tags (in the form `key:value`) defines a filter that Datadog uses when collecting metrics from EC2. Wildcards, such as `?` (for single characters) and `*` (for multiple characters) can also be used. Only hosts that match one of the defined tags will be imported into Datadog. The rest will be ignored. Host matching a given tag can also be excluded by adding `!` before the tag. For example, `env:production,instance-type:c1.*,!region:us-east-1`                                                                                                            |
|                      | host_tags                            | [string] | Array of tags (in the form `key:value`) to add to all hosts and metrics reporting through this integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | metrics_collection_enabled           | boolean  | Whether Datadog collects metrics for this AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | resource_collection_enabled          | boolean  | **DEPRECATED**: Deprecated in favor of 'extended_resource_collection_enabled'. Whether Datadog collects a standard set of resources from your AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | role_name                            | string   | Your Datadog role delegation name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | secret_access_key                    | string   | Your AWS secret access key. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "163662907100",
  "account_specific_namespace_rules": {
    "auto_scaling": false
  },
  "cspm_resource_collection_enabled": true,
  "excluded_regions": [
    "us-east-1",
    "us-west-2"
  ],
  "extended_resource_collection_enabled": true,
  "filter_tags": [
    "$KEY:$VALUE"
  ],
  "host_tags": [
    "$KEY:$VALUE"
  ],
  "metrics_collection_enabled": false,
  "role_name": "DatadogAWSIntegrationRole"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The Response returned by the AWS Create Account call.

| Field       | Type   | Description      |
| ----------- | ------ | ---------------- |
| external_id | string | AWS external_id. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "external_id": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="409" %}
Conflict Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "163662907100",
  "account_specific_namespace_rules": {
    "auto_scaling": false
  },
  "cspm_resource_collection_enabled": true,
  "excluded_regions": [
    "us-east-1",
    "us-west-2"
  ],
  "extended_resource_collection_enabled": true,
  "filter_tags": [
    "$KEY:$VALUE"
  ],
  "host_tags": [
    "$KEY:$VALUE"
  ],
  "metrics_collection_enabled": false,
  "role_name": "DatadogAWSIntegrationRole"
}
EOF
                        
##### 

```go
// Create an AWS integration returns "OK" response

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
	body := datadogV1.AWSAccount{
		AccountId: datadog.PtrString("163662907100"),
		AccountSpecificNamespaceRules: map[string]bool{
			"auto_scaling": false,
		},
		CspmResourceCollectionEnabled: datadog.PtrBool(true),
		ExcludedRegions: []string{
			"us-east-1",
			"us-west-2",
		},
		ExtendedResourceCollectionEnabled: datadog.PtrBool(true),
		FilterTags: []string{
			"$KEY:$VALUE",
		},
		HostTags: []string{
			"$KEY:$VALUE",
		},
		MetricsCollectionEnabled: datadog.PtrBool(false),
		RoleName:                 datadog.PtrString("DatadogAWSIntegrationRole"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateAWSAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateAWSAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create an AWS integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSAccount;
import com.datadog.api.client.v1.model.AWSAccountCreateResponse;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSAccount body =
        new AWSAccount()
            .accountId("163662907100")
            .accountSpecificNamespaceRules(Map.ofEntries(Map.entry("auto_scaling", false)))
            .cspmResourceCollectionEnabled(true)
            .excludedRegions(Arrays.asList("us-east-1", "us-west-2"))
            .extendedResourceCollectionEnabled(true)
            .filterTags(Collections.singletonList("$KEY:$VALUE"))
            .hostTags(Collections.singletonList("$KEY:$VALUE"))
            .metricsCollectionEnabled(false)
            .roleName("DatadogAWSIntegrationRole");

    try {
      AWSAccountCreateResponse result = apiInstance.createAWSAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createAWSAccount");
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

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.AwsIntegration.create(
    account_id="<AWS_ACCOUNT_ID>",
    host_tags=["tag:example"],
    filter_tags=["filter:example"],
    role_name="<AWS_ROLE_NAME>",
    account_specific_namespace_rules={'namespace1': True/False, 'namespace2': True/False},
    excluded_regions=["us-east-1", "us-west-1"]
)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python "example.py"
##### 

```python
"""
Create an AWS integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_account import AWSAccount

body = AWSAccount(
    account_id="163662907100",
    account_specific_namespace_rules=dict(
        auto_scaling=False,
    ),
    cspm_resource_collection_enabled=True,
    excluded_regions=[
        "us-east-1",
        "us-west-2",
    ],
    extended_resource_collection_enabled=True,
    filter_tags=[
        "$KEY:$VALUE",
    ],
    host_tags=[
        "$KEY:$VALUE",
    ],
    metrics_collection_enabled=False,
    role_name="DatadogAWSIntegrationRole",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_account(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

config = {
  "account_id": "<AWS_ACCOUNT_ID>",
  "filter_tags": ["<KEY>:<VALUE>"],
  "host_tags": ["<KEY>:<VALUE>"],
  "role_name": "DatadogAWSIntegrationRole",
  "account_specific_namespace_rules": {"auto_scaling": false, "opsworks": false},
  "excluded_regions": ["us-east-1", "us-west-1"]
}

dog.aws_integration_create(config)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```ruby
# Create an AWS integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccount.new({
  account_id: "163662907100",
  account_specific_namespace_rules: {
    auto_scaling: false,
  },
  cspm_resource_collection_enabled: true,
  excluded_regions: [
    "us-east-1",
    "us-west-2",
  ],
  extended_resource_collection_enabled: true,
  filter_tags: [
    "$KEY:$VALUE",
  ],
  host_tags: [
    "$KEY:$VALUE",
  ],
  metrics_collection_enabled: false,
  role_name: "DatadogAWSIntegrationRole",
})
p api_instance.create_aws_account(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create an AWS integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSAccount;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = AWSAccount::new()
        .account_id("163662907100".to_string())
        .account_specific_namespace_rules(BTreeMap::from([("auto_scaling".to_string(), false)]))
        .cspm_resource_collection_enabled(true)
        .excluded_regions(vec!["us-east-1".to_string(), "us-west-2".to_string()])
        .extended_resource_collection_enabled(true)
        .filter_tags(vec!["$KEY:$VALUE".to_string()])
        .host_tags(vec!["$KEY:$VALUE".to_string()])
        .metrics_collection_enabled(false)
        .role_name("DatadogAWSIntegrationRole".to_string());
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_aws_account(body).await;
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
 * Create an AWS integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiCreateAWSAccountRequest = {
  body: {
    accountId: "163662907100",
    accountSpecificNamespaceRules: {
      auto_scaling: false,
    },
    cspmResourceCollectionEnabled: true,
    excludedRegions: ["us-east-1", "us-west-2"],
    extendedResourceCollectionEnabled: true,
    filterTags: ["$KEY:$VALUE"],
    hostTags: ["$KEY:$VALUE"],
    metricsCollectionEnabled: false,
    roleName: "DatadogAWSIntegrationRole",
  },
};

apiInstance
  .createAWSAccount(params)
  .then((data: v1.AWSAccountCreateResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/aws/accounts |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/aws/accounts |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/aws/accounts      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/aws/accounts      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/aws/accounts     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/aws/accounts |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/aws/accounts |

### Overview

Create a new AWS Account Integration Config. This endpoint requires the `aws_configurations_manage` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field      | Field                                        | Type          | Description                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | data [*required*]                       | object        | AWS Account Create Request data.                                                                                                                                                                                                                                            |
| data              | attributes [*required*]                 | object        | The AWS Account Integration Config to be created.                                                                                                                                                                                                                           |
| attributes        | account_tags                                 | [string]      | Tags to apply to all hosts and metrics reporting for this account. Defaults to `[]`.                                                                                                                                                                                        |
| attributes        | auth_config [*required*]                |  <oneOf> | AWS Authentication config.                                                                                                                                                                                                                                                  |
| auth_config       | Option 1                                     | object        | AWS Authentication config to integrate your account using an access key pair.                                                                                                                                                                                               |
| Option 1          | access_key_id [*required*]              | string        | AWS Access Key ID.                                                                                                                                                                                                                                                          |
| Option 1          | secret_access_key                            | string        | AWS Secret Access Key.                                                                                                                                                                                                                                                      |
| auth_config       | Option 2                                     | object        | AWS Authentication config to integrate your account using an IAM role.                                                                                                                                                                                                      |
| Option 2          | external_id                                  | string        | AWS IAM External ID for associated role.                                                                                                                                                                                                                                    |
| Option 2          | role_name [*required*]                  | string        | AWS IAM Role name.                                                                                                                                                                                                                                                          |
| attributes        | aws_account_id [*required*]             | string        | AWS Account ID.                                                                                                                                                                                                                                                             |
| attributes        | aws_partition [*required*]              | enum          | AWS partition your AWS account is scoped to. Defaults to `aws`. See [Partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) in the AWS documentation for more information. Allowed enum values: `aws,aws-cn,aws-us-gov` |
| attributes        | aws_regions                                  |  <oneOf> | AWS Regions to collect data from. Defaults to `include_all`.                                                                                                                                                                                                                |
| aws_regions       | Option 1                                     | object        | Include all regions. Defaults to `true`.                                                                                                                                                                                                                                    |
| Option 1          | include_all [*required*]                | boolean       | Include all regions.                                                                                                                                                                                                                                                        |
| aws_regions       | Option 2                                     | object        | Include only these regions.                                                                                                                                                                                                                                                 |
| Option 2          | include_only [*required*]               | [string]      | Include only these regions.                                                                                                                                                                                                                                                 |
| attributes        | logs_config                                  | object        | AWS Logs Collection config.                                                                                                                                                                                                                                                 |
| logs_config       | lambda_forwarder                             | object        | Log Autosubscription configuration for Datadog Forwarder Lambda functions. Automatically set up triggers for existing and new logs for some services, ensuring no logs from new resources are missed and saving time spent on manual configuration.                         |
| lambda_forwarder  | lambdas                                      | [string]      | List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to `[]`.                                                                                                                                                                                            |
| lambda_forwarder  | log_source_config                            | object        | Log source configuration.                                                                                                                                                                                                                                                   |
| log_source_config | tag_filters                                  | [object]      | List of AWS log source tag filters. Defaults to `[]`.                                                                                                                                                                                                                       |
| tag_filters       | source                                       | string        | The AWS log source to which the tag filters defined in `tags` are applied.                                                                                                                                                                                                  |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the log source specified by `source`.                                                                                                                                                                                                |
| lambda_forwarder  | sources                                      | [string]      | List of service IDs set to enable automatic log collection. Discover the list of available services with the [Get list of AWS log ready services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services) endpoint.                 |
| attributes        | metrics_config                               | object        | AWS Metrics Collection config.                                                                                                                                                                                                                                              |
| metrics_config    | automute_enabled                             | boolean       | Enable EC2 automute for AWS metrics. Defaults to `true`.                                                                                                                                                                                                                    |
| metrics_config    | collect_cloudwatch_alarms                    | boolean       | Enable CloudWatch alarms collection. Defaults to `false`.                                                                                                                                                                                                                   |
| metrics_config    | collect_custom_metrics                       | boolean       | Enable custom metrics collection. Defaults to `false`.                                                                                                                                                                                                                      |
| metrics_config    | enabled                                      | boolean       | Enable AWS metrics collection. Defaults to `true`.                                                                                                                                                                                                                          |
| metrics_config    | namespace_filters                            |  <oneOf> | AWS Metrics namespace filters. Defaults to `exclude_only`.                                                                                                                                                                                                                  |
| namespace_filters | Option 1                                     | object        | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| Option 1          | exclude_only [*required*]               | [string]      | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| namespace_filters | Option 2                                     | object        | Include only these namespaces.                                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these namespaces.                                                                                                                                                                                                                                              |
| metrics_config    | tag_filters                                  | [object]      | AWS Metrics collection tag filters list. Defaults to `[]`.                                                                                                                                                                                                                  |
| tag_filters       | namespace                                    | string        | The AWS service for which the tag filters defined in `tags` will be applied.                                                                                                                                                                                                |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the service specified by `namespace`.                                                                                                                                                                                                |
| attributes        | resources_config                             | object        | AWS Resources Collection config.                                                                                                                                                                                                                                            |
| resources_config  | cloud_security_posture_management_collection | boolean       | Enable Cloud Security Management to scan AWS resources for vulnerabilities, misconfigurations, identity risks, and compliance violations. Defaults to `false`. Requires `extended_collection` to be set to `true`.                                                          |
| resources_config  | extended_collection                          | boolean       | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Defaults to `true`. Required for `cloud_security_posture_management_collection`.                                                                      |
| attributes        | traces_config                                | object        | AWS Traces Collection config.                                                                                                                                                                                                                                               |
| traces_config     | xray_services                                |  <oneOf> | AWS X-Ray services to collect traces from. Defaults to `include_only`.                                                                                                                                                                                                      |
| xray_services     | Option 1                                     | object        | Include all services.                                                                                                                                                                                                                                                       |
| Option 1          | include_all [*required*]                | boolean       | Include all services.                                                                                                                                                                                                                                                       |
| xray_services     | Option 2                                     | object        | Include only these services. Defaults to `[]`.                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these services.                                                                                                                                                                                                                                                |
| data              | type [*required*]                       | enum          | AWS Account resource type. Allowed enum values: `account`                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "data": {
    "attributes": {
      "account_tags": [
        "key:value"
      ],
      "auth_config": {
        "role_name": "DatadogIntegrationRole"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "test:test"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": true,
        "collect_custom_metrics": true,
        "enabled": true,
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "key:value"
            ]
          }
        ]
      },
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": false
      },
      "traces_config": {}
    },
    "type": "account"
  }
}
```

##### 

```json
{
  "data": {
    "attributes": {
      "account_tags": [
        "key:value"
      ],
      "auth_config": {
        "access_key_id": "AKIAIOSFODNN7EXAMPLE",
        "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "test:test"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": true,
        "collect_custom_metrics": true,
        "enabled": true,
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "key:value"
            ]
          }
        ]
      },
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": false
      },
      "traces_config": {}
    },
    "type": "account"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
AWS Account object
{% tab title="Model" %}
AWS Account response body.

| Parent field      | Field                                        | Type          | Description                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | data [*required*]                       | object        | AWS Account response data.                                                                                                                                                                                                                                                  |
| data              | attributes                                   | object        | AWS Account response attributes.                                                                                                                                                                                                                                            |
| attributes        | account_tags                                 | [string]      | Tags to apply to all hosts and metrics reporting for this account. Defaults to `[]`.                                                                                                                                                                                        |
| attributes        | auth_config                                  |  <oneOf> | AWS Authentication config.                                                                                                                                                                                                                                                  |
| auth_config       | Option 1                                     | object        | AWS Authentication config to integrate your account using an access key pair.                                                                                                                                                                                               |
| Option 1          | access_key_id [*required*]              | string        | AWS Access Key ID.                                                                                                                                                                                                                                                          |
| Option 1          | secret_access_key                            | string        | AWS Secret Access Key.                                                                                                                                                                                                                                                      |
| auth_config       | Option 2                                     | object        | AWS Authentication config to integrate your account using an IAM role.                                                                                                                                                                                                      |
| Option 2          | external_id                                  | string        | AWS IAM External ID for associated role.                                                                                                                                                                                                                                    |
| Option 2          | role_name [*required*]                  | string        | AWS IAM Role name.                                                                                                                                                                                                                                                          |
| attributes        | aws_account_id [*required*]             | string        | AWS Account ID.                                                                                                                                                                                                                                                             |
| attributes        | aws_partition                                | enum          | AWS partition your AWS account is scoped to. Defaults to `aws`. See [Partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) in the AWS documentation for more information. Allowed enum values: `aws,aws-cn,aws-us-gov` |
| attributes        | aws_regions                                  |  <oneOf> | AWS Regions to collect data from. Defaults to `include_all`.                                                                                                                                                                                                                |
| aws_regions       | Option 1                                     | object        | Include all regions. Defaults to `true`.                                                                                                                                                                                                                                    |
| Option 1          | include_all [*required*]                | boolean       | Include all regions.                                                                                                                                                                                                                                                        |
| aws_regions       | Option 2                                     | object        | Include only these regions.                                                                                                                                                                                                                                                 |
| Option 2          | include_only [*required*]               | [string]      | Include only these regions.                                                                                                                                                                                                                                                 |
| attributes        | created_at                                   | date-time     | Timestamp of when the account integration was created.                                                                                                                                                                                                                      |
| attributes        | logs_config                                  | object        | AWS Logs Collection config.                                                                                                                                                                                                                                                 |
| logs_config       | lambda_forwarder                             | object        | Log Autosubscription configuration for Datadog Forwarder Lambda functions. Automatically set up triggers for existing and new logs for some services, ensuring no logs from new resources are missed and saving time spent on manual configuration.                         |
| lambda_forwarder  | lambdas                                      | [string]      | List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to `[]`.                                                                                                                                                                                            |
| lambda_forwarder  | log_source_config                            | object        | Log source configuration.                                                                                                                                                                                                                                                   |
| log_source_config | tag_filters                                  | [object]      | List of AWS log source tag filters. Defaults to `[]`.                                                                                                                                                                                                                       |
| tag_filters       | source                                       | string        | The AWS log source to which the tag filters defined in `tags` are applied.                                                                                                                                                                                                  |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the log source specified by `source`.                                                                                                                                                                                                |
| lambda_forwarder  | sources                                      | [string]      | List of service IDs set to enable automatic log collection. Discover the list of available services with the [Get list of AWS log ready services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services) endpoint.                 |
| attributes        | metrics_config                               | object        | AWS Metrics Collection config.                                                                                                                                                                                                                                              |
| metrics_config    | automute_enabled                             | boolean       | Enable EC2 automute for AWS metrics. Defaults to `true`.                                                                                                                                                                                                                    |
| metrics_config    | collect_cloudwatch_alarms                    | boolean       | Enable CloudWatch alarms collection. Defaults to `false`.                                                                                                                                                                                                                   |
| metrics_config    | collect_custom_metrics                       | boolean       | Enable custom metrics collection. Defaults to `false`.                                                                                                                                                                                                                      |
| metrics_config    | enabled                                      | boolean       | Enable AWS metrics collection. Defaults to `true`.                                                                                                                                                                                                                          |
| metrics_config    | namespace_filters                            |  <oneOf> | AWS Metrics namespace filters. Defaults to `exclude_only`.                                                                                                                                                                                                                  |
| namespace_filters | Option 1                                     | object        | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| Option 1          | exclude_only [*required*]               | [string]      | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| namespace_filters | Option 2                                     | object        | Include only these namespaces.                                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these namespaces.                                                                                                                                                                                                                                              |
| metrics_config    | tag_filters                                  | [object]      | AWS Metrics collection tag filters list. Defaults to `[]`.                                                                                                                                                                                                                  |
| tag_filters       | namespace                                    | string        | The AWS service for which the tag filters defined in `tags` will be applied.                                                                                                                                                                                                |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the service specified by `namespace`.                                                                                                                                                                                                |
| attributes        | modified_at                                  | date-time     | Timestamp of when the account integration was updated.                                                                                                                                                                                                                      |
| attributes        | resources_config                             | object        | AWS Resources Collection config.                                                                                                                                                                                                                                            |
| resources_config  | cloud_security_posture_management_collection | boolean       | Enable Cloud Security Management to scan AWS resources for vulnerabilities, misconfigurations, identity risks, and compliance violations. Defaults to `false`. Requires `extended_collection` to be set to `true`.                                                          |
| resources_config  | extended_collection                          | boolean       | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Defaults to `true`. Required for `cloud_security_posture_management_collection`.                                                                      |
| attributes        | traces_config                                | object        | AWS Traces Collection config.                                                                                                                                                                                                                                               |
| traces_config     | xray_services                                |  <oneOf> | AWS X-Ray services to collect traces from. Defaults to `include_only`.                                                                                                                                                                                                      |
| xray_services     | Option 1                                     | object        | Include all services.                                                                                                                                                                                                                                                       |
| Option 1          | include_all [*required*]                | boolean       | Include all services.                                                                                                                                                                                                                                                       |
| xray_services     | Option 2                                     | object        | Include only these services. Defaults to `[]`.                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these services.                                                                                                                                                                                                                                                |
| data              | id [*required*]                         | string        | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID.                   |
| data              | type [*required*]                       | enum          | AWS Account resource type. Allowed enum values: `account`                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_tags": [
        "env:prod"
      ],
      "auth_config": {
        "access_key_id": "AKIAIOSFODNN7EXAMPLE",
        "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "aws_regions": {
        "include_all": true
      },
      "created_at": "2019-09-19T10:00:00.000Z",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "env:prod"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": false,
        "collect_custom_metrics": false,
        "enabled": true,
        "namespace_filters": {
          "exclude_only": [
            "AWS/SQS",
            "AWS/ElasticMapReduce",
            "AWS/Usage"
          ]
        },
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "datadog:true"
            ]
          }
        ]
      },
      "modified_at": "2019-09-19T10:00:00.000Z",
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": true
      },
      "traces_config": {
        "xray_services": {
          "include_all": false
        }
      }
    },
    "id": "00000000-abcd-0001-0000-000000000000",
    "type": "account"
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

{% tab title="409" %}
Conflict
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_tags": [
        "key:value"
      ],
      "auth_config": {
        "role_name": "DatadogIntegrationRole"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "test:test"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": true,
        "collect_custom_metrics": true,
        "enabled": true,
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "key:value"
            ]
          }
        ]
      },
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": false
      },
      "traces_config": {}
    },
    "type": "account"
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_tags": [
        "key:value"
      ],
      "auth_config": {
        "access_key_id": "AKIAIOSFODNN7EXAMPLE",
        "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "test:test"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": true,
        "collect_custom_metrics": true,
        "enabled": true,
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "key:value"
            ]
          }
        ]
      },
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": false
      },
      "traces_config": {}
    },
    "type": "account"
  }
}
EOF
                        
##### 

```go
// Create an AWS account returns "AWS Account object" response

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
	body := datadogV2.AWSAccountCreateRequest{
		Data: datadogV2.AWSAccountCreateRequestData{
			Attributes: datadogV2.AWSAccountCreateRequestAttributes{
				AccountTags: *datadog.NewNullableList(&[]string{
					"key:value",
				}),
				AuthConfig: datadogV2.AWSAuthConfig{
					AWSAuthConfigRole: &datadogV2.AWSAuthConfigRole{
						RoleName: "DatadogIntegrationRole",
					}},
				AwsAccountId: "123456789012",
				AwsPartition: datadogV2.AWSACCOUNTPARTITION_AWS,
				CcmConfig: &datadogV2.AWSCCMConfig{
					DataExportConfigs: []datadogV2.DataExportConfig{
						{
							BucketName:   datadog.PtrString("my-bucket"),
							BucketRegion: datadog.PtrString("us-east-1"),
							ReportName:   datadog.PtrString("my-report"),
							ReportPrefix: datadog.PtrString("reports"),
							ReportType:   datadog.PtrString("CUR2.0"),
						},
					},
				},
				LogsConfig: &datadogV2.AWSLogsConfig{
					LambdaForwarder: &datadogV2.AWSLambdaForwarderConfig{
						Lambdas: []string{
							"arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
						},
						LogSourceConfig: &datadogV2.AWSLambdaForwarderConfigLogSourceConfig{
							TagFilters: []datadogV2.AWSLogSourceTagFilter{
								{
									Source: datadog.PtrString("s3"),
									Tags: *datadog.NewNullableList(&[]string{
										"test:test",
									}),
								},
							},
						},
						Sources: []string{
							"s3",
						},
					},
				},
				MetricsConfig: &datadogV2.AWSMetricsConfig{
					AutomuteEnabled:         datadog.PtrBool(true),
					CollectCloudwatchAlarms: datadog.PtrBool(true),
					CollectCustomMetrics:    datadog.PtrBool(true),
					Enabled:                 datadog.PtrBool(true),
					TagFilters: []datadogV2.AWSNamespaceTagFilter{
						{
							Namespace: datadog.PtrString("AWS/EC2"),
							Tags: *datadog.NewNullableList(&[]string{
								"key:value",
							}),
						},
					},
				},
				ResourcesConfig: &datadogV2.AWSResourcesConfig{
					CloudSecurityPostureManagementCollection: datadog.PtrBool(false),
					ExtendedCollection:                       datadog.PtrBool(false),
				},
				TracesConfig: &datadogV2.AWSTracesConfig{},
			},
			Type: datadogV2.AWSACCOUNTTYPE_ACCOUNT,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateAWSAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateAWSAccount`:\n%s\n", responseContent)
}
```

##### 

```go
// Create an AWS integration returns "AWS Account object" response

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
	body := datadogV2.AWSAccountCreateRequest{
		Data: datadogV2.AWSAccountCreateRequestData{
			Attributes: datadogV2.AWSAccountCreateRequestAttributes{
				AccountTags: *datadog.NewNullableList(&[]string{
					"key:value",
				}),
				AuthConfig: datadogV2.AWSAuthConfig{
					AWSAuthConfigKeys: &datadogV2.AWSAuthConfigKeys{
						AccessKeyId:     "AKIAIOSFODNN7EXAMPLE",
						SecretAccessKey: datadog.PtrString("wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"),
					}},
				AwsAccountId: "123456789012",
				AwsPartition: datadogV2.AWSACCOUNTPARTITION_AWS,
				CcmConfig: &datadogV2.AWSCCMConfig{
					DataExportConfigs: []datadogV2.DataExportConfig{
						{
							BucketName:   datadog.PtrString("my-bucket"),
							BucketRegion: datadog.PtrString("us-east-1"),
							ReportName:   datadog.PtrString("my-report"),
							ReportPrefix: datadog.PtrString("reports"),
							ReportType:   datadog.PtrString("CUR2.0"),
						},
					},
				},
				LogsConfig: &datadogV2.AWSLogsConfig{
					LambdaForwarder: &datadogV2.AWSLambdaForwarderConfig{
						Lambdas: []string{
							"arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
						},
						LogSourceConfig: &datadogV2.AWSLambdaForwarderConfigLogSourceConfig{
							TagFilters: []datadogV2.AWSLogSourceTagFilter{
								{
									Source: datadog.PtrString("s3"),
									Tags: *datadog.NewNullableList(&[]string{
										"test:test",
									}),
								},
							},
						},
						Sources: []string{
							"s3",
						},
					},
				},
				MetricsConfig: &datadogV2.AWSMetricsConfig{
					AutomuteEnabled:         datadog.PtrBool(true),
					CollectCloudwatchAlarms: datadog.PtrBool(true),
					CollectCustomMetrics:    datadog.PtrBool(true),
					Enabled:                 datadog.PtrBool(true),
					TagFilters: []datadogV2.AWSNamespaceTagFilter{
						{
							Namespace: datadog.PtrString("AWS/EC2"),
							Tags: *datadog.NewNullableList(&[]string{
								"key:value",
							}),
						},
					},
				},
				ResourcesConfig: &datadogV2.AWSResourcesConfig{
					CloudSecurityPostureManagementCollection: datadog.PtrBool(false),
					ExtendedCollection:                       datadog.PtrBool(false),
				},
				TracesConfig: &datadogV2.AWSTracesConfig{},
			},
			Type: datadogV2.AWSACCOUNTTYPE_ACCOUNT,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateAWSAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateAWSAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create an AWS account returns "AWS Account object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSAccountCreateRequest;
import com.datadog.api.client.v2.model.AWSAccountCreateRequestAttributes;
import com.datadog.api.client.v2.model.AWSAccountCreateRequestData;
import com.datadog.api.client.v2.model.AWSAccountPartition;
import com.datadog.api.client.v2.model.AWSAccountResponse;
import com.datadog.api.client.v2.model.AWSAccountType;
import com.datadog.api.client.v2.model.AWSAuthConfig;
import com.datadog.api.client.v2.model.AWSAuthConfigRole;
import com.datadog.api.client.v2.model.AWSCCMConfig;
import com.datadog.api.client.v2.model.AWSLambdaForwarderConfig;
import com.datadog.api.client.v2.model.AWSLambdaForwarderConfigLogSourceConfig;
import com.datadog.api.client.v2.model.AWSLogSourceTagFilter;
import com.datadog.api.client.v2.model.AWSLogsConfig;
import com.datadog.api.client.v2.model.AWSMetricsConfig;
import com.datadog.api.client.v2.model.AWSNamespaceTagFilter;
import com.datadog.api.client.v2.model.AWSResourcesConfig;
import com.datadog.api.client.v2.model.AWSTracesConfig;
import com.datadog.api.client.v2.model.DataExportConfig;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSAccountCreateRequest body =
        new AWSAccountCreateRequest()
            .data(
                new AWSAccountCreateRequestData()
                    .attributes(
                        new AWSAccountCreateRequestAttributes()
                            .accountTags(Collections.singletonList("key:value"))
                            .authConfig(
                                new AWSAuthConfig(
                                    new AWSAuthConfigRole().roleName("DatadogIntegrationRole")))
                            .awsAccountId("123456789012")
                            .awsPartition(AWSAccountPartition.AWS)
                            .ccmConfig(
                                new AWSCCMConfig()
                                    .dataExportConfigs(
                                        Collections.singletonList(
                                            new DataExportConfig()
                                                .bucketName("my-bucket")
                                                .bucketRegion("us-east-1")
                                                .reportName("my-report")
                                                .reportPrefix("reports")
                                                .reportType("CUR2.0"))))
                            .logsConfig(
                                new AWSLogsConfig()
                                    .lambdaForwarder(
                                        new AWSLambdaForwarderConfig()
                                            .lambdas(
                                                Collections.singletonList(
                                                    "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"))
                                            .logSourceConfig(
                                                new AWSLambdaForwarderConfigLogSourceConfig()
                                                    .tagFilters(
                                                        Collections.singletonList(
                                                            new AWSLogSourceTagFilter()
                                                                .source("s3")
                                                                .tags(
                                                                    Collections.singletonList(
                                                                        "test:test")))))
                                            .sources(Collections.singletonList("s3"))))
                            .metricsConfig(
                                new AWSMetricsConfig()
                                    .automuteEnabled(true)
                                    .collectCloudwatchAlarms(true)
                                    .collectCustomMetrics(true)
                                    .enabled(true)
                                    .tagFilters(
                                        Collections.singletonList(
                                            new AWSNamespaceTagFilter()
                                                .namespace("AWS/EC2")
                                                .tags(Collections.singletonList("key:value")))))
                            .resourcesConfig(
                                new AWSResourcesConfig()
                                    .cloudSecurityPostureManagementCollection(false)
                                    .extendedCollection(false))
                            .tracesConfig(new AWSTracesConfig()))
                    .type(AWSAccountType.ACCOUNT));

    try {
      AWSAccountResponse result = apiInstance.createAWSAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createAWSAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Create an AWS integration returns "AWS Account object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSAccountCreateRequest;
import com.datadog.api.client.v2.model.AWSAccountCreateRequestAttributes;
import com.datadog.api.client.v2.model.AWSAccountCreateRequestData;
import com.datadog.api.client.v2.model.AWSAccountPartition;
import com.datadog.api.client.v2.model.AWSAccountResponse;
import com.datadog.api.client.v2.model.AWSAccountType;
import com.datadog.api.client.v2.model.AWSAuthConfig;
import com.datadog.api.client.v2.model.AWSAuthConfigKeys;
import com.datadog.api.client.v2.model.AWSCCMConfig;
import com.datadog.api.client.v2.model.AWSLambdaForwarderConfig;
import com.datadog.api.client.v2.model.AWSLambdaForwarderConfigLogSourceConfig;
import com.datadog.api.client.v2.model.AWSLogSourceTagFilter;
import com.datadog.api.client.v2.model.AWSLogsConfig;
import com.datadog.api.client.v2.model.AWSMetricsConfig;
import com.datadog.api.client.v2.model.AWSNamespaceTagFilter;
import com.datadog.api.client.v2.model.AWSResourcesConfig;
import com.datadog.api.client.v2.model.AWSTracesConfig;
import com.datadog.api.client.v2.model.DataExportConfig;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSAccountCreateRequest body =
        new AWSAccountCreateRequest()
            .data(
                new AWSAccountCreateRequestData()
                    .attributes(
                        new AWSAccountCreateRequestAttributes()
                            .accountTags(Collections.singletonList("key:value"))
                            .authConfig(
                                new AWSAuthConfig(
                                    new AWSAuthConfigKeys()
                                        .accessKeyId("AKIAIOSFODNN7EXAMPLE")
                                        .secretAccessKey(
                                            "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")))
                            .awsAccountId("123456789012")
                            .awsPartition(AWSAccountPartition.AWS)
                            .ccmConfig(
                                new AWSCCMConfig()
                                    .dataExportConfigs(
                                        Collections.singletonList(
                                            new DataExportConfig()
                                                .bucketName("my-bucket")
                                                .bucketRegion("us-east-1")
                                                .reportName("my-report")
                                                .reportPrefix("reports")
                                                .reportType("CUR2.0"))))
                            .logsConfig(
                                new AWSLogsConfig()
                                    .lambdaForwarder(
                                        new AWSLambdaForwarderConfig()
                                            .lambdas(
                                                Collections.singletonList(
                                                    "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"))
                                            .logSourceConfig(
                                                new AWSLambdaForwarderConfigLogSourceConfig()
                                                    .tagFilters(
                                                        Collections.singletonList(
                                                            new AWSLogSourceTagFilter()
                                                                .source("s3")
                                                                .tags(
                                                                    Collections.singletonList(
                                                                        "test:test")))))
                                            .sources(Collections.singletonList("s3"))))
                            .metricsConfig(
                                new AWSMetricsConfig()
                                    .automuteEnabled(true)
                                    .collectCloudwatchAlarms(true)
                                    .collectCustomMetrics(true)
                                    .enabled(true)
                                    .tagFilters(
                                        Collections.singletonList(
                                            new AWSNamespaceTagFilter()
                                                .namespace("AWS/EC2")
                                                .tags(Collections.singletonList("key:value")))))
                            .resourcesConfig(
                                new AWSResourcesConfig()
                                    .cloudSecurityPostureManagementCollection(false)
                                    .extendedCollection(false))
                            .tracesConfig(new AWSTracesConfig()))
                    .type(AWSAccountType.ACCOUNT));

    try {
      AWSAccountResponse result = apiInstance.createAWSAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createAWSAccount");
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

```python
"""
Create an AWS account returns "AWS Account object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes
from datadog_api_client.v2.model.aws_account_create_request_data import AWSAccountCreateRequestData
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
from datadog_api_client.v2.model.aws_account_type import AWSAccountType
from datadog_api_client.v2.model.aws_auth_config_role import AWSAuthConfigRole
from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig
from datadog_api_client.v2.model.aws_lambda_forwarder_config_log_source_config import (
    AWSLambdaForwarderConfigLogSourceConfig,
)
from datadog_api_client.v2.model.aws_log_source_tag_filter import AWSLogSourceTagFilter
from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig
from datadog_api_client.v2.model.awsccm_config import AWSCCMConfig
from datadog_api_client.v2.model.data_export_config import DataExportConfig

body = AWSAccountCreateRequest(
    data=AWSAccountCreateRequestData(
        attributes=AWSAccountCreateRequestAttributes(
            account_tags=[
                "key:value",
            ],
            auth_config=AWSAuthConfigRole(
                role_name="DatadogIntegrationRole",
            ),
            aws_account_id="123456789012",
            aws_partition=AWSAccountPartition.AWS,
            ccm_config=AWSCCMConfig(
                data_export_configs=[
                    DataExportConfig(
                        bucket_name="my-bucket",
                        bucket_region="us-east-1",
                        report_name="my-report",
                        report_prefix="reports",
                        report_type="CUR2.0",
                    ),
                ],
            ),
            logs_config=AWSLogsConfig(
                lambda_forwarder=AWSLambdaForwarderConfig(
                    lambdas=[
                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
                    ],
                    log_source_config=AWSLambdaForwarderConfigLogSourceConfig(
                        tag_filters=[
                            AWSLogSourceTagFilter(
                                source="s3",
                                tags=[
                                    "test:test",
                                ],
                            ),
                        ],
                    ),
                    sources=[
                        "s3",
                    ],
                ),
            ),
            metrics_config=AWSMetricsConfig(
                automute_enabled=True,
                collect_cloudwatch_alarms=True,
                collect_custom_metrics=True,
                enabled=True,
                tag_filters=[
                    AWSNamespaceTagFilter(
                        namespace="AWS/EC2",
                        tags=[
                            "key:value",
                        ],
                    ),
                ],
            ),
            resources_config=AWSResourcesConfig(
                cloud_security_posture_management_collection=False,
                extended_collection=False,
            ),
            traces_config=AWSTracesConfig(),
        ),
        type=AWSAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_account(body=body)

    print(response)
```

##### 

```python
"""
Create an AWS integration returns "AWS Account object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes
from datadog_api_client.v2.model.aws_account_create_request_data import AWSAccountCreateRequestData
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
from datadog_api_client.v2.model.aws_account_type import AWSAccountType
from datadog_api_client.v2.model.aws_auth_config_keys import AWSAuthConfigKeys
from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig
from datadog_api_client.v2.model.aws_lambda_forwarder_config_log_source_config import (
    AWSLambdaForwarderConfigLogSourceConfig,
)
from datadog_api_client.v2.model.aws_log_source_tag_filter import AWSLogSourceTagFilter
from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig
from datadog_api_client.v2.model.awsccm_config import AWSCCMConfig
from datadog_api_client.v2.model.data_export_config import DataExportConfig

body = AWSAccountCreateRequest(
    data=AWSAccountCreateRequestData(
        attributes=AWSAccountCreateRequestAttributes(
            account_tags=[
                "key:value",
            ],
            auth_config=AWSAuthConfigKeys(
                access_key_id="AKIAIOSFODNN7EXAMPLE",
                secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            ),
            aws_account_id="123456789012",
            aws_partition=AWSAccountPartition.AWS,
            ccm_config=AWSCCMConfig(
                data_export_configs=[
                    DataExportConfig(
                        bucket_name="my-bucket",
                        bucket_region="us-east-1",
                        report_name="my-report",
                        report_prefix="reports",
                        report_type="CUR2.0",
                    ),
                ],
            ),
            logs_config=AWSLogsConfig(
                lambda_forwarder=AWSLambdaForwarderConfig(
                    lambdas=[
                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
                    ],
                    log_source_config=AWSLambdaForwarderConfigLogSourceConfig(
                        tag_filters=[
                            AWSLogSourceTagFilter(
                                source="s3",
                                tags=[
                                    "test:test",
                                ],
                            ),
                        ],
                    ),
                    sources=[
                        "s3",
                    ],
                ),
            ),
            metrics_config=AWSMetricsConfig(
                automute_enabled=True,
                collect_cloudwatch_alarms=True,
                collect_custom_metrics=True,
                enabled=True,
                tag_filters=[
                    AWSNamespaceTagFilter(
                        namespace="AWS/EC2",
                        tags=[
                            "key:value",
                        ],
                    ),
                ],
            ),
            resources_config=AWSResourcesConfig(
                cloud_security_posture_management_collection=False,
                extended_collection=False,
            ),
            traces_config=AWSTracesConfig(),
        ),
        type=AWSAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_account(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create an AWS account returns "AWS Account object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new

body = DatadogAPIClient::V2::AWSAccountCreateRequest.new({
  data: DatadogAPIClient::V2::AWSAccountCreateRequestData.new({
    attributes: DatadogAPIClient::V2::AWSAccountCreateRequestAttributes.new({
      account_tags: [
        "key:value",
      ],
      auth_config: DatadogAPIClient::V2::AWSAuthConfigRole.new({
        role_name: "DatadogIntegrationRole",
      }),
      aws_account_id: "123456789012",
      aws_partition: DatadogAPIClient::V2::AWSAccountPartition::AWS,
      ccm_config: DatadogAPIClient::V2::AWSCCMConfig.new({
        data_export_configs: [
          DatadogAPIClient::V2::DataExportConfig.new({
            bucket_name: "my-bucket",
            bucket_region: "us-east-1",
            report_name: "my-report",
            report_prefix: "reports",
            report_type: "CUR2.0",
          }),
        ],
      }),
      logs_config: DatadogAPIClient::V2::AWSLogsConfig.new({
        lambda_forwarder: DatadogAPIClient::V2::AWSLambdaForwarderConfig.new({
          lambdas: [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
          ],
          log_source_config: DatadogAPIClient::V2::AWSLambdaForwarderConfigLogSourceConfig.new({
            tag_filters: [
              DatadogAPIClient::V2::AWSLogSourceTagFilter.new({
                source: "s3",
                tags: [
                  "test:test",
                ],
              }),
            ],
          }),
          sources: [
            "s3",
          ],
        }),
      }),
      metrics_config: DatadogAPIClient::V2::AWSMetricsConfig.new({
        automute_enabled: true,
        collect_cloudwatch_alarms: true,
        collect_custom_metrics: true,
        enabled: true,
        tag_filters: [
          DatadogAPIClient::V2::AWSNamespaceTagFilter.new({
            namespace: "AWS/EC2",
            tags: [
              "key:value",
            ],
          }),
        ],
      }),
      resources_config: DatadogAPIClient::V2::AWSResourcesConfig.new({
        cloud_security_posture_management_collection: false,
        extended_collection: false,
      }),
      traces_config: DatadogAPIClient::V2::AWSTracesConfig.new({}),
    }),
    type: DatadogAPIClient::V2::AWSAccountType::ACCOUNT,
  }),
})
p api_instance.create_aws_account(body)
```

##### 

```ruby
# Create an AWS integration returns "AWS Account object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new

body = DatadogAPIClient::V2::AWSAccountCreateRequest.new({
  data: DatadogAPIClient::V2::AWSAccountCreateRequestData.new({
    attributes: DatadogAPIClient::V2::AWSAccountCreateRequestAttributes.new({
      account_tags: [
        "key:value",
      ],
      auth_config: DatadogAPIClient::V2::AWSAuthConfigKeys.new({
        access_key_id: "AKIAIOSFODNN7EXAMPLE",
        secret_access_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
      }),
      aws_account_id: "123456789012",
      aws_partition: DatadogAPIClient::V2::AWSAccountPartition::AWS,
      ccm_config: DatadogAPIClient::V2::AWSCCMConfig.new({
        data_export_configs: [
          DatadogAPIClient::V2::DataExportConfig.new({
            bucket_name: "my-bucket",
            bucket_region: "us-east-1",
            report_name: "my-report",
            report_prefix: "reports",
            report_type: "CUR2.0",
          }),
        ],
      }),
      logs_config: DatadogAPIClient::V2::AWSLogsConfig.new({
        lambda_forwarder: DatadogAPIClient::V2::AWSLambdaForwarderConfig.new({
          lambdas: [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
          ],
          log_source_config: DatadogAPIClient::V2::AWSLambdaForwarderConfigLogSourceConfig.new({
            tag_filters: [
              DatadogAPIClient::V2::AWSLogSourceTagFilter.new({
                source: "s3",
                tags: [
                  "test:test",
                ],
              }),
            ],
          }),
          sources: [
            "s3",
          ],
        }),
      }),
      metrics_config: DatadogAPIClient::V2::AWSMetricsConfig.new({
        automute_enabled: true,
        collect_cloudwatch_alarms: true,
        collect_custom_metrics: true,
        enabled: true,
        tag_filters: [
          DatadogAPIClient::V2::AWSNamespaceTagFilter.new({
            namespace: "AWS/EC2",
            tags: [
              "key:value",
            ],
          }),
        ],
      }),
      resources_config: DatadogAPIClient::V2::AWSResourcesConfig.new({
        cloud_security_posture_management_collection: false,
        extended_collection: false,
      }),
      traces_config: DatadogAPIClient::V2::AWSTracesConfig.new({}),
    }),
    type: DatadogAPIClient::V2::AWSAccountType::ACCOUNT,
  }),
})
p api_instance.create_aws_account(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create an AWS account returns "AWS Account object" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV2::model::AWSAccountCreateRequest;
use datadog_api_client::datadogV2::model::AWSAccountCreateRequestAttributes;
use datadog_api_client::datadogV2::model::AWSAccountCreateRequestData;
use datadog_api_client::datadogV2::model::AWSAccountPartition;
use datadog_api_client::datadogV2::model::AWSAccountType;
use datadog_api_client::datadogV2::model::AWSAuthConfig;
use datadog_api_client::datadogV2::model::AWSAuthConfigRole;
use datadog_api_client::datadogV2::model::AWSCCMConfig;
use datadog_api_client::datadogV2::model::AWSLambdaForwarderConfig;
use datadog_api_client::datadogV2::model::AWSLambdaForwarderConfigLogSourceConfig;
use datadog_api_client::datadogV2::model::AWSLogSourceTagFilter;
use datadog_api_client::datadogV2::model::AWSLogsConfig;
use datadog_api_client::datadogV2::model::AWSMetricsConfig;
use datadog_api_client::datadogV2::model::AWSNamespaceTagFilter;
use datadog_api_client::datadogV2::model::AWSResourcesConfig;
use datadog_api_client::datadogV2::model::AWSTracesConfig;
use datadog_api_client::datadogV2::model::DataExportConfig;

#[tokio::main]
async fn main() {
    let body = AWSAccountCreateRequest::new(AWSAccountCreateRequestData::new(
        AWSAccountCreateRequestAttributes::new(
            AWSAuthConfig::AWSAuthConfigRole(Box::new(AWSAuthConfigRole::new(
                "DatadogIntegrationRole".to_string(),
            ))),
            "123456789012".to_string(),
            AWSAccountPartition::AWS,
        )
        .account_tags(Some(vec!["key:value".to_string()]))
        .ccm_config(AWSCCMConfig::new().data_export_configs(vec![
                                DataExportConfig::new()
                                    .bucket_name("my-bucket".to_string())
                                    .bucket_region("us-east-1".to_string())
                                    .report_name("my-report".to_string())
                                    .report_prefix("reports".to_string())
                                    .report_type("CUR2.0".to_string())
                            ]))
        .logs_config(
            AWSLogsConfig::new().lambda_forwarder(
                AWSLambdaForwarderConfig::new()
                    .lambdas(vec![
                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
                            .to_string(),
                    ])
                    .log_source_config(AWSLambdaForwarderConfigLogSourceConfig::new().tag_filters(
                        vec![
                                            AWSLogSourceTagFilter::new()
                                                .source("s3".to_string())
                                                .tags(Some(vec!["test:test".to_string()]))
                                        ],
                    ))
                    .sources(vec!["s3".to_string()]),
            ),
        )
        .metrics_config(
            AWSMetricsConfig::new()
                .automute_enabled(true)
                .collect_cloudwatch_alarms(true)
                .collect_custom_metrics(true)
                .enabled(true)
                .tag_filters(vec![AWSNamespaceTagFilter::new()
                    .namespace("AWS/EC2".to_string())
                    .tags(Some(vec!["key:value".to_string()]))]),
        )
        .resources_config(
            AWSResourcesConfig::new()
                .cloud_security_posture_management_collection(false)
                .extended_collection(false),
        )
        .traces_config(AWSTracesConfig::new()),
        AWSAccountType::ACCOUNT,
    ));
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_aws_account(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Create an AWS integration returns "AWS Account object" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV2::model::AWSAccountCreateRequest;
use datadog_api_client::datadogV2::model::AWSAccountCreateRequestAttributes;
use datadog_api_client::datadogV2::model::AWSAccountCreateRequestData;
use datadog_api_client::datadogV2::model::AWSAccountPartition;
use datadog_api_client::datadogV2::model::AWSAccountType;
use datadog_api_client::datadogV2::model::AWSAuthConfig;
use datadog_api_client::datadogV2::model::AWSAuthConfigKeys;
use datadog_api_client::datadogV2::model::AWSCCMConfig;
use datadog_api_client::datadogV2::model::AWSLambdaForwarderConfig;
use datadog_api_client::datadogV2::model::AWSLambdaForwarderConfigLogSourceConfig;
use datadog_api_client::datadogV2::model::AWSLogSourceTagFilter;
use datadog_api_client::datadogV2::model::AWSLogsConfig;
use datadog_api_client::datadogV2::model::AWSMetricsConfig;
use datadog_api_client::datadogV2::model::AWSNamespaceTagFilter;
use datadog_api_client::datadogV2::model::AWSResourcesConfig;
use datadog_api_client::datadogV2::model::AWSTracesConfig;
use datadog_api_client::datadogV2::model::DataExportConfig;

#[tokio::main]
async fn main() {
    let body = AWSAccountCreateRequest::new(AWSAccountCreateRequestData::new(
        AWSAccountCreateRequestAttributes::new(
            AWSAuthConfig::AWSAuthConfigKeys(Box::new(
                AWSAuthConfigKeys::new("AKIAIOSFODNN7EXAMPLE".to_string())
                    .secret_access_key("wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY".to_string()),
            )),
            "123456789012".to_string(),
            AWSAccountPartition::AWS,
        )
        .account_tags(Some(vec!["key:value".to_string()]))
        .ccm_config(AWSCCMConfig::new().data_export_configs(vec![
                                DataExportConfig::new()
                                    .bucket_name("my-bucket".to_string())
                                    .bucket_region("us-east-1".to_string())
                                    .report_name("my-report".to_string())
                                    .report_prefix("reports".to_string())
                                    .report_type("CUR2.0".to_string())
                            ]))
        .logs_config(
            AWSLogsConfig::new().lambda_forwarder(
                AWSLambdaForwarderConfig::new()
                    .lambdas(vec![
                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
                            .to_string(),
                    ])
                    .log_source_config(AWSLambdaForwarderConfigLogSourceConfig::new().tag_filters(
                        vec![
                                            AWSLogSourceTagFilter::new()
                                                .source("s3".to_string())
                                                .tags(Some(vec!["test:test".to_string()]))
                                        ],
                    ))
                    .sources(vec!["s3".to_string()]),
            ),
        )
        .metrics_config(
            AWSMetricsConfig::new()
                .automute_enabled(true)
                .collect_cloudwatch_alarms(true)
                .collect_custom_metrics(true)
                .enabled(true)
                .tag_filters(vec![AWSNamespaceTagFilter::new()
                    .namespace("AWS/EC2".to_string())
                    .tags(Some(vec!["key:value".to_string()]))]),
        )
        .resources_config(
            AWSResourcesConfig::new()
                .cloud_security_posture_management_collection(false)
                .extended_collection(false),
        )
        .traces_config(AWSTracesConfig::new()),
        AWSAccountType::ACCOUNT,
    ));
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_aws_account(body).await;
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
 * Create an AWS account returns "AWS Account object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

const params: v2.AWSIntegrationApiCreateAWSAccountRequest = {
  body: {
    data: {
      attributes: {
        accountTags: ["key:value"],
        authConfig: {
          roleName: "DatadogIntegrationRole",
        },
        awsAccountId: "123456789012",
        awsPartition: "aws",
        ccmConfig: {
          dataExportConfigs: [
            {
              bucketName: "my-bucket",
              bucketRegion: "us-east-1",
              reportName: "my-report",
              reportPrefix: "reports",
              reportType: "CUR2.0",
            },
          ],
        },
        logsConfig: {
          lambdaForwarder: {
            lambdas: [
              "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
            ],
            logSourceConfig: {
              tagFilters: [
                {
                  source: "s3",
                  tags: ["test:test"],
                },
              ],
            },
            sources: ["s3"],
          },
        },
        metricsConfig: {
          automuteEnabled: true,
          collectCloudwatchAlarms: true,
          collectCustomMetrics: true,
          enabled: true,
          tagFilters: [
            {
              namespace: "AWS/EC2",
              tags: ["key:value"],
            },
          ],
        },
        resourcesConfig: {
          cloudSecurityPostureManagementCollection: false,
          extendedCollection: false,
        },
        tracesConfig: {},
      },
      type: "account",
    },
  },
};

apiInstance
  .createAWSAccount(params)
  .then((data: v2.AWSAccountResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Create an AWS integration returns "AWS Account object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

const params: v2.AWSIntegrationApiCreateAWSAccountRequest = {
  body: {
    data: {
      attributes: {
        accountTags: ["key:value"],
        authConfig: {
          accessKeyId: "AKIAIOSFODNN7EXAMPLE",
          secretAccessKey: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        },
        awsAccountId: "123456789012",
        awsPartition: "aws",
        ccmConfig: {
          dataExportConfigs: [
            {
              bucketName: "my-bucket",
              bucketRegion: "us-east-1",
              reportName: "my-report",
              reportPrefix: "reports",
              reportType: "CUR2.0",
            },
          ],
        },
        logsConfig: {
          lambdaForwarder: {
            lambdas: [
              "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
            ],
            logSourceConfig: {
              tagFilters: [
                {
                  source: "s3",
                  tags: ["test:test"],
                },
              ],
            },
            sources: ["s3"],
          },
        },
        metricsConfig: {
          automuteEnabled: true,
          collectCloudwatchAlarms: true,
          collectCustomMetrics: true,
          enabled: true,
          tagFilters: [
            {
              namespace: "AWS/EC2",
              tags: ["key:value"],
            },
          ],
        },
        resourcesConfig: {
          cloudSecurityPostureManagementCollection: false,
          extendedCollection: false,
        },
        tracesConfig: {},
      },
      type: "account",
    },
  },
};

apiInstance
  .createAWSAccount(params)
  .then((data: v2.AWSAccountResponse) => {
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

## Get resource collection IAM permissions{% #get-resource-collection-iam-permissions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/iam_permissions/resource_collection |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/iam_permissions/resource_collection |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/iam_permissions/resource_collection      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/iam_permissions/resource_collection      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/iam_permissions/resource_collection     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/iam_permissions/resource_collection |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/iam_permissions/resource_collection |

### Overview

Get all resource collection AWS IAM permissions required for the AWS integration.

### Response

{% tab title="200" %}
AWS integration resource collection IAM permissions.
{% tab title="Model" %}
AWS Integration IAM Permissions response body.

| Parent field | Field                         | Type     | Description                                                                               |
| ------------ | ----------------------------- | -------- | ----------------------------------------------------------------------------------------- |
|              | data [*required*]        | object   | AWS Integration IAM Permissions response data.                                            |
| data         | attributes                    | object   | AWS Integration IAM Permissions response attributes.                                      |
| attributes   | permissions [*required*] | [string] | List of AWS IAM permissions required for the integration.                                 |
| data         | id                            | string   | The `AWSIntegrationIamPermissionsResponseData` `id`.                                      |
| data         | type                          | enum     | The `AWSIntegrationIamPermissionsResponseData` `type`. Allowed enum values: `permissions` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "permissions": [
        "account:GetContactInformation",
        "amplify:ListApps",
        "amplify:ListArtifacts",
        "amplify:ListBackendEnvironments",
        "amplify:ListBranches"
      ]
    },
    "id": "permissions",
    "type": "permissions"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/iam_permissions/resource_collection" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get resource collection IAM permissions returns "AWS integration resource collection IAM permissions." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_integration_iam_permissions_resource_collection()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get resource collection IAM permissions returns "AWS integration resource collection IAM permissions." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new
p api_instance.get_aws_integration_iam_permissions_resource_collection()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get resource collection IAM permissions returns "AWS integration resource collection IAM permissions." response

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
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.GetAWSIntegrationIAMPermissionsResourceCollection(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.GetAWSIntegrationIAMPermissionsResourceCollection`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.GetAWSIntegrationIAMPermissionsResourceCollection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get resource collection IAM permissions returns "AWS integration resource collection IAM
// permissions." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSIntegrationIamPermissionsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSIntegrationIamPermissionsResponse result =
          apiInstance.getAWSIntegrationIAMPermissionsResourceCollection();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling"
              + " AwsIntegrationApi#getAWSIntegrationIAMPermissionsResourceCollection");
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
// Get resource collection IAM permissions returns "AWS integration resource
// collection IAM permissions." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api
        .get_aws_integration_iam_permissions_resource_collection()
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
 * Get resource collection IAM permissions returns "AWS integration resource collection IAM permissions." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

apiInstance
  .getAWSIntegrationIAMPermissionsResourceCollection()
  .then((data: v2.AWSIntegrationIamPermissionsResponse) => {
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

## Update an AWS integration{% #update-an-aws-integration %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/integration/aws |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/integration/aws |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/integration/aws      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/integration/aws      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/integration/aws     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/integration/aws |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/integration/aws |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** Update a Datadog-Amazon Web Services integration. This endpoint requires the `aws_configuration_edit` permission.

### Arguments

#### Query Strings

| Name          | Type   | Description                                                                                                          |
| ------------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| account_id    | string | Only return AWS accounts that matches this `account_id`.                                                             |
| role_name     | string | Only return AWS accounts that match this `role_name`. Required if `account_id` is specified.                         |
| access_key_id | string | Only return AWS accounts that matches this `access_key_id`. Required if none of the other two options are specified. |

### Request

#### Body Data (required)

AWS request object

{% tab title="Model" %}

| Parent field         | Field                                | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | access_key_id                        | string   | Your AWS access key ID. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                      | account_id                           | string   | Your AWS Account ID without dashes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                      | account_specific_namespace_rules     | object   | An object (in the form `{"namespace1":true/false, "namespace2":true/false}`) containing user-supplied overrides for AWS namespace metric collection. **Important**: This field only contains namespaces explicitly configured through API calls, not the comprehensive enabled or disabled status of all namespaces. If a namespace is absent from this field, it uses Datadog's internal defaults (all namespaces enabled by default, except `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage`). For a complete view of all namespace statuses, use the V2 AWS Integration API instead. |
| additionalProperties | <any-key>                            | boolean  | A list of additional properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                      | cspm_resource_collection_enabled     | boolean  | Whether Datadog collects cloud security posture management resources from your AWS account. This includes additional resources not covered under the general `resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                       |
|                      | excluded_regions                     | [string] | An array of [AWS regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) to exclude from metrics collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | extended_resource_collection_enabled | boolean  | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Required for `cspm_resource_collection`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                      | filter_tags                          | [string] | The array of EC2 tags (in the form `key:value`) defines a filter that Datadog uses when collecting metrics from EC2. Wildcards, such as `?` (for single characters) and `*` (for multiple characters) can also be used. Only hosts that match one of the defined tags will be imported into Datadog. The rest will be ignored. Host matching a given tag can also be excluded by adding `!` before the tag. For example, `env:production,instance-type:c1.*,!region:us-east-1`                                                                                                            |
|                      | host_tags                            | [string] | Array of tags (in the form `key:value`) to add to all hosts and metrics reporting through this integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                      | metrics_collection_enabled           | boolean  | Whether Datadog collects metrics for this AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      | resource_collection_enabled          | boolean  | **DEPRECATED**: Deprecated in favor of 'extended_resource_collection_enabled'. Whether Datadog collects a standard set of resources from your AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | role_name                            | string   | Your Datadog role delegation name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                      | secret_access_key                    | string   | Your AWS secret access key. Only required if your AWS account is a GovCloud or China account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "163662907100",
  "account_specific_namespace_rules": {
    "auto_scaling": false
  },
  "cspm_resource_collection_enabled": false,
  "excluded_regions": [
    "us-east-1",
    "us-west-2"
  ],
  "extended_resource_collection_enabled": true,
  "filter_tags": [
    "$KEY:$VALUE"
  ],
  "host_tags": [
    "$KEY:$VALUE"
  ],
  "metrics_collection_enabled": true,
  "role_name": "DatadogAWSIntegrationRole"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="409" %}
Conflict Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                          \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "account_id": "163662907100",
  "account_specific_namespace_rules": {
    "auto_scaling": false
  },
  "cspm_resource_collection_enabled": false,
  "excluded_regions": [
    "us-east-1",
    "us-west-2"
  ],
  "extended_resource_collection_enabled": true,
  "filter_tags": [
    "$KEY:$VALUE"
  ],
  "host_tags": [
    "$KEY:$VALUE"
  ],
  "metrics_collection_enabled": true,
  "role_name": "DatadogAWSIntegrationRole"
}
EOF
                        
##### 

```go
// Update an AWS integration returns "OK" response

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
	body := datadogV1.AWSAccount{
		AccountId: datadog.PtrString("163662907100"),
		AccountSpecificNamespaceRules: map[string]bool{
			"auto_scaling": false,
		},
		CspmResourceCollectionEnabled: datadog.PtrBool(false),
		ExcludedRegions: []string{
			"us-east-1",
			"us-west-2",
		},
		ExtendedResourceCollectionEnabled: datadog.PtrBool(true),
		FilterTags: []string{
			"$KEY:$VALUE",
		},
		HostTags: []string{
			"$KEY:$VALUE",
		},
		MetricsCollectionEnabled: datadog.PtrBool(true),
		RoleName:                 datadog.PtrString("DatadogAWSIntegrationRole"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.UpdateAWSAccount(ctx, body, *datadogV1.NewUpdateAWSAccountOptionalParameters().WithAccountId("163662907100").WithRoleName("DatadogAWSIntegrationRole"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.UpdateAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.UpdateAWSAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update an AWS integration returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.api.AwsIntegrationApi.UpdateAWSAccountOptionalParameters;
import com.datadog.api.client.v1.model.AWSAccount;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSAccount body =
        new AWSAccount()
            .accountId("163662907100")
            .accountSpecificNamespaceRules(Map.ofEntries(Map.entry("auto_scaling", false)))
            .cspmResourceCollectionEnabled(false)
            .excludedRegions(Arrays.asList("us-east-1", "us-west-2"))
            .extendedResourceCollectionEnabled(true)
            .filterTags(Collections.singletonList("$KEY:$VALUE"))
            .hostTags(Collections.singletonList("$KEY:$VALUE"))
            .metricsCollectionEnabled(true)
            .roleName("DatadogAWSIntegrationRole");

    try {
      apiInstance.updateAWSAccount(
          body,
          new UpdateAWSAccountOptionalParameters()
              .accountId("163662907100")
              .roleName("DatadogAWSIntegrationRole"));
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#updateAWSAccount");
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

```python
"""
Update an AWS integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_account import AWSAccount

body = AWSAccount(
    account_id="163662907100",
    account_specific_namespace_rules=dict(
        auto_scaling=False,
    ),
    cspm_resource_collection_enabled=False,
    excluded_regions=[
        "us-east-1",
        "us-west-2",
    ],
    extended_resource_collection_enabled=True,
    filter_tags=[
        "$KEY:$VALUE",
    ],
    host_tags=[
        "$KEY:$VALUE",
    ],
    metrics_collection_enabled=True,
    role_name="DatadogAWSIntegrationRole",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.update_aws_account(
        account_id="163662907100", role_name="DatadogAWSIntegrationRole", body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update an AWS integration returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSAccount.new({
  account_id: "163662907100",
  account_specific_namespace_rules: {
    auto_scaling: false,
  },
  cspm_resource_collection_enabled: false,
  excluded_regions: [
    "us-east-1",
    "us-west-2",
  ],
  extended_resource_collection_enabled: true,
  filter_tags: [
    "$KEY:$VALUE",
  ],
  host_tags: [
    "$KEY:$VALUE",
  ],
  metrics_collection_enabled: true,
  role_name: "DatadogAWSIntegrationRole",
})
opts = {
  account_id: "163662907100",
  role_name: "DatadogAWSIntegrationRole",
}
p api_instance.update_aws_account(body, opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update an AWS integration returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::api_aws_integration::UpdateAWSAccountOptionalParams;
use datadog_api_client::datadogV1::model::AWSAccount;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = AWSAccount::new()
        .account_id("163662907100".to_string())
        .account_specific_namespace_rules(BTreeMap::from([("auto_scaling".to_string(), false)]))
        .cspm_resource_collection_enabled(false)
        .excluded_regions(vec!["us-east-1".to_string(), "us-west-2".to_string()])
        .extended_resource_collection_enabled(true)
        .filter_tags(vec!["$KEY:$VALUE".to_string()])
        .host_tags(vec!["$KEY:$VALUE".to_string()])
        .metrics_collection_enabled(true)
        .role_name("DatadogAWSIntegrationRole".to_string());
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api
        .update_aws_account(
            body,
            UpdateAWSAccountOptionalParams::default()
                .account_id("163662907100".to_string())
                .role_name("DatadogAWSIntegrationRole".to_string()),
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
 * Update an AWS integration returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiUpdateAWSAccountRequest = {
  body: {
    accountId: "163662907100",
    accountSpecificNamespaceRules: {
      auto_scaling: false,
    },
    cspmResourceCollectionEnabled: false,
    excludedRegions: ["us-east-1", "us-west-2"],
    extendedResourceCollectionEnabled: true,
    filterTags: ["$KEY:$VALUE"],
    hostTags: ["$KEY:$VALUE"],
    metricsCollectionEnabled: true,
    roleName: "DatadogAWSIntegrationRole",
  },
  accountId: "163662907100",
  roleName: "DatadogAWSIntegrationRole",
};

apiInstance
  .updateAWSAccount(params)
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integration/aws/accounts/{aws_account_config_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integration/aws/accounts/{aws_account_config_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integration/aws/accounts/{aws_account_config_id} |

### Overview

Update an AWS Account Integration Config by config ID. This endpoint requires the `aws_configuration_edit` permission.

### Arguments

#### Path Parameters

| Name                                    | Type   | Description                                                                                                                                                                                                                                               |
| --------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| aws_account_config_id [*required*] | string | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field      | Field                                        | Type          | Description                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | data [*required*]                       | object        | AWS Account Update Request data.                                                                                                                                                                                                                                            |
| data              | attributes [*required*]                 | object        | The AWS Account Integration Config to be updated.                                                                                                                                                                                                                           |
| attributes        | account_tags                                 | [string]      | Tags to apply to all hosts and metrics reporting for this account. Defaults to `[]`.                                                                                                                                                                                        |
| attributes        | auth_config                                  |  <oneOf> | AWS Authentication config.                                                                                                                                                                                                                                                  |
| auth_config       | Option 1                                     | object        | AWS Authentication config to integrate your account using an access key pair.                                                                                                                                                                                               |
| Option 1          | access_key_id [*required*]              | string        | AWS Access Key ID.                                                                                                                                                                                                                                                          |
| Option 1          | secret_access_key                            | string        | AWS Secret Access Key.                                                                                                                                                                                                                                                      |
| auth_config       | Option 2                                     | object        | AWS Authentication config to integrate your account using an IAM role.                                                                                                                                                                                                      |
| Option 2          | external_id                                  | string        | AWS IAM External ID for associated role.                                                                                                                                                                                                                                    |
| Option 2          | role_name [*required*]                  | string        | AWS IAM Role name.                                                                                                                                                                                                                                                          |
| attributes        | aws_account_id [*required*]             | string        | AWS Account ID.                                                                                                                                                                                                                                                             |
| attributes        | aws_partition                                | enum          | AWS partition your AWS account is scoped to. Defaults to `aws`. See [Partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) in the AWS documentation for more information. Allowed enum values: `aws,aws-cn,aws-us-gov` |
| attributes        | aws_regions                                  |  <oneOf> | AWS Regions to collect data from. Defaults to `include_all`.                                                                                                                                                                                                                |
| aws_regions       | Option 1                                     | object        | Include all regions. Defaults to `true`.                                                                                                                                                                                                                                    |
| Option 1          | include_all [*required*]                | boolean       | Include all regions.                                                                                                                                                                                                                                                        |
| aws_regions       | Option 2                                     | object        | Include only these regions.                                                                                                                                                                                                                                                 |
| Option 2          | include_only [*required*]               | [string]      | Include only these regions.                                                                                                                                                                                                                                                 |
| attributes        | logs_config                                  | object        | AWS Logs Collection config.                                                                                                                                                                                                                                                 |
| logs_config       | lambda_forwarder                             | object        | Log Autosubscription configuration for Datadog Forwarder Lambda functions. Automatically set up triggers for existing and new logs for some services, ensuring no logs from new resources are missed and saving time spent on manual configuration.                         |
| lambda_forwarder  | lambdas                                      | [string]      | List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to `[]`.                                                                                                                                                                                            |
| lambda_forwarder  | log_source_config                            | object        | Log source configuration.                                                                                                                                                                                                                                                   |
| log_source_config | tag_filters                                  | [object]      | List of AWS log source tag filters. Defaults to `[]`.                                                                                                                                                                                                                       |
| tag_filters       | source                                       | string        | The AWS log source to which the tag filters defined in `tags` are applied.                                                                                                                                                                                                  |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the log source specified by `source`.                                                                                                                                                                                                |
| lambda_forwarder  | sources                                      | [string]      | List of service IDs set to enable automatic log collection. Discover the list of available services with the [Get list of AWS log ready services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services) endpoint.                 |
| attributes        | metrics_config                               | object        | AWS Metrics Collection config.                                                                                                                                                                                                                                              |
| metrics_config    | automute_enabled                             | boolean       | Enable EC2 automute for AWS metrics. Defaults to `true`.                                                                                                                                                                                                                    |
| metrics_config    | collect_cloudwatch_alarms                    | boolean       | Enable CloudWatch alarms collection. Defaults to `false`.                                                                                                                                                                                                                   |
| metrics_config    | collect_custom_metrics                       | boolean       | Enable custom metrics collection. Defaults to `false`.                                                                                                                                                                                                                      |
| metrics_config    | enabled                                      | boolean       | Enable AWS metrics collection. Defaults to `true`.                                                                                                                                                                                                                          |
| metrics_config    | namespace_filters                            |  <oneOf> | AWS Metrics namespace filters. Defaults to `exclude_only`.                                                                                                                                                                                                                  |
| namespace_filters | Option 1                                     | object        | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| Option 1          | exclude_only [*required*]               | [string]      | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| namespace_filters | Option 2                                     | object        | Include only these namespaces.                                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these namespaces.                                                                                                                                                                                                                                              |
| metrics_config    | tag_filters                                  | [object]      | AWS Metrics collection tag filters list. Defaults to `[]`.                                                                                                                                                                                                                  |
| tag_filters       | namespace                                    | string        | The AWS service for which the tag filters defined in `tags` will be applied.                                                                                                                                                                                                |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the service specified by `namespace`.                                                                                                                                                                                                |
| attributes        | resources_config                             | object        | AWS Resources Collection config.                                                                                                                                                                                                                                            |
| resources_config  | cloud_security_posture_management_collection | boolean       | Enable Cloud Security Management to scan AWS resources for vulnerabilities, misconfigurations, identity risks, and compliance violations. Defaults to `false`. Requires `extended_collection` to be set to `true`.                                                          |
| resources_config  | extended_collection                          | boolean       | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Defaults to `true`. Required for `cloud_security_posture_management_collection`.                                                                      |
| attributes        | traces_config                                | object        | AWS Traces Collection config.                                                                                                                                                                                                                                               |
| traces_config     | xray_services                                |  <oneOf> | AWS X-Ray services to collect traces from. Defaults to `include_only`.                                                                                                                                                                                                      |
| xray_services     | Option 1                                     | object        | Include all services.                                                                                                                                                                                                                                                       |
| Option 1          | include_all [*required*]                | boolean       | Include all services.                                                                                                                                                                                                                                                       |
| xray_services     | Option 2                                     | object        | Include only these services. Defaults to `[]`.                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these services.                                                                                                                                                                                                                                                |
| data              | id                                           | string        | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID.                   |
| data              | type [*required*]                       | enum          | AWS Account resource type. Allowed enum values: `account`                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_tags": [
        "key:value"
      ],
      "auth_config": {
        "role_name": "DatadogIntegrationRole"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "test:test"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": true,
        "collect_custom_metrics": true,
        "enabled": true,
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "key:value"
            ]
          }
        ]
      },
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": false
      },
      "traces_config": {}
    },
    "type": "account"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
AWS Account object
{% tab title="Model" %}
AWS Account response body.

| Parent field      | Field                                        | Type          | Description                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | data [*required*]                       | object        | AWS Account response data.                                                                                                                                                                                                                                                  |
| data              | attributes                                   | object        | AWS Account response attributes.                                                                                                                                                                                                                                            |
| attributes        | account_tags                                 | [string]      | Tags to apply to all hosts and metrics reporting for this account. Defaults to `[]`.                                                                                                                                                                                        |
| attributes        | auth_config                                  |  <oneOf> | AWS Authentication config.                                                                                                                                                                                                                                                  |
| auth_config       | Option 1                                     | object        | AWS Authentication config to integrate your account using an access key pair.                                                                                                                                                                                               |
| Option 1          | access_key_id [*required*]              | string        | AWS Access Key ID.                                                                                                                                                                                                                                                          |
| Option 1          | secret_access_key                            | string        | AWS Secret Access Key.                                                                                                                                                                                                                                                      |
| auth_config       | Option 2                                     | object        | AWS Authentication config to integrate your account using an IAM role.                                                                                                                                                                                                      |
| Option 2          | external_id                                  | string        | AWS IAM External ID for associated role.                                                                                                                                                                                                                                    |
| Option 2          | role_name [*required*]                  | string        | AWS IAM Role name.                                                                                                                                                                                                                                                          |
| attributes        | aws_account_id [*required*]             | string        | AWS Account ID.                                                                                                                                                                                                                                                             |
| attributes        | aws_partition                                | enum          | AWS partition your AWS account is scoped to. Defaults to `aws`. See [Partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) in the AWS documentation for more information. Allowed enum values: `aws,aws-cn,aws-us-gov` |
| attributes        | aws_regions                                  |  <oneOf> | AWS Regions to collect data from. Defaults to `include_all`.                                                                                                                                                                                                                |
| aws_regions       | Option 1                                     | object        | Include all regions. Defaults to `true`.                                                                                                                                                                                                                                    |
| Option 1          | include_all [*required*]                | boolean       | Include all regions.                                                                                                                                                                                                                                                        |
| aws_regions       | Option 2                                     | object        | Include only these regions.                                                                                                                                                                                                                                                 |
| Option 2          | include_only [*required*]               | [string]      | Include only these regions.                                                                                                                                                                                                                                                 |
| attributes        | created_at                                   | date-time     | Timestamp of when the account integration was created.                                                                                                                                                                                                                      |
| attributes        | logs_config                                  | object        | AWS Logs Collection config.                                                                                                                                                                                                                                                 |
| logs_config       | lambda_forwarder                             | object        | Log Autosubscription configuration for Datadog Forwarder Lambda functions. Automatically set up triggers for existing and new logs for some services, ensuring no logs from new resources are missed and saving time spent on manual configuration.                         |
| lambda_forwarder  | lambdas                                      | [string]      | List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to `[]`.                                                                                                                                                                                            |
| lambda_forwarder  | log_source_config                            | object        | Log source configuration.                                                                                                                                                                                                                                                   |
| log_source_config | tag_filters                                  | [object]      | List of AWS log source tag filters. Defaults to `[]`.                                                                                                                                                                                                                       |
| tag_filters       | source                                       | string        | The AWS log source to which the tag filters defined in `tags` are applied.                                                                                                                                                                                                  |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the log source specified by `source`.                                                                                                                                                                                                |
| lambda_forwarder  | sources                                      | [string]      | List of service IDs set to enable automatic log collection. Discover the list of available services with the [Get list of AWS log ready services](https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services) endpoint.                 |
| attributes        | metrics_config                               | object        | AWS Metrics Collection config.                                                                                                                                                                                                                                              |
| metrics_config    | automute_enabled                             | boolean       | Enable EC2 automute for AWS metrics. Defaults to `true`.                                                                                                                                                                                                                    |
| metrics_config    | collect_cloudwatch_alarms                    | boolean       | Enable CloudWatch alarms collection. Defaults to `false`.                                                                                                                                                                                                                   |
| metrics_config    | collect_custom_metrics                       | boolean       | Enable custom metrics collection. Defaults to `false`.                                                                                                                                                                                                                      |
| metrics_config    | enabled                                      | boolean       | Enable AWS metrics collection. Defaults to `true`.                                                                                                                                                                                                                          |
| metrics_config    | namespace_filters                            |  <oneOf> | AWS Metrics namespace filters. Defaults to `exclude_only`.                                                                                                                                                                                                                  |
| namespace_filters | Option 1                                     | object        | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| Option 1          | exclude_only [*required*]               | [string]      | Exclude only these namespaces from metrics collection. Defaults to `["AWS/SQS", "AWS/ElasticMapReduce", "AWS/Usage"]`. `AWS/SQS`, `AWS/ElasticMapReduce`, and `AWS/Usage` are excluded by default to reduce your AWS CloudWatch costs from `GetMetricData` API calls.       |
| namespace_filters | Option 2                                     | object        | Include only these namespaces.                                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these namespaces.                                                                                                                                                                                                                                              |
| metrics_config    | tag_filters                                  | [object]      | AWS Metrics collection tag filters list. Defaults to `[]`.                                                                                                                                                                                                                  |
| tag_filters       | namespace                                    | string        | The AWS service for which the tag filters defined in `tags` will be applied.                                                                                                                                                                                                |
| tag_filters       | tags                                         | [string]      | The AWS resource tags to filter on for the service specified by `namespace`.                                                                                                                                                                                                |
| attributes        | modified_at                                  | date-time     | Timestamp of when the account integration was updated.                                                                                                                                                                                                                      |
| attributes        | resources_config                             | object        | AWS Resources Collection config.                                                                                                                                                                                                                                            |
| resources_config  | cloud_security_posture_management_collection | boolean       | Enable Cloud Security Management to scan AWS resources for vulnerabilities, misconfigurations, identity risks, and compliance violations. Defaults to `false`. Requires `extended_collection` to be set to `true`.                                                          |
| resources_config  | extended_collection                          | boolean       | Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Defaults to `true`. Required for `cloud_security_posture_management_collection`.                                                                      |
| attributes        | traces_config                                | object        | AWS Traces Collection config.                                                                                                                                                                                                                                               |
| traces_config     | xray_services                                |  <oneOf> | AWS X-Ray services to collect traces from. Defaults to `include_only`.                                                                                                                                                                                                      |
| xray_services     | Option 1                                     | object        | Include all services.                                                                                                                                                                                                                                                       |
| Option 1          | include_all [*required*]                | boolean       | Include all services.                                                                                                                                                                                                                                                       |
| xray_services     | Option 2                                     | object        | Include only these services. Defaults to `[]`.                                                                                                                                                                                                                              |
| Option 2          | include_only [*required*]               | [string]      | Include only these services.                                                                                                                                                                                                                                                |
| data              | id [*required*]                         | string        | Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the [List all AWS integrations](https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations) endpoint and query by AWS Account ID.                   |
| data              | type [*required*]                       | enum          | AWS Account resource type. Allowed enum values: `account`                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_tags": [
        "env:prod"
      ],
      "auth_config": {
        "access_key_id": "AKIAIOSFODNN7EXAMPLE",
        "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "aws_regions": {
        "include_all": true
      },
      "created_at": "2019-09-19T10:00:00.000Z",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "env:prod"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": false,
        "collect_custom_metrics": false,
        "enabled": true,
        "namespace_filters": {
          "exclude_only": [
            "AWS/SQS",
            "AWS/ElasticMapReduce",
            "AWS/Usage"
          ]
        },
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "datadog:true"
            ]
          }
        ]
      },
      "modified_at": "2019-09-19T10:00:00.000Z",
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": true
      },
      "traces_config": {
        "xray_services": {
          "include_all": false
        }
      }
    },
    "id": "00000000-abcd-0001-0000-000000000000",
    "type": "account"
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
                          \# Path parametersexport aws_account_config_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/accounts/${aws_account_config_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_tags": [
        "key:value"
      ],
      "auth_config": {
        "role_name": "DatadogIntegrationRole"
      },
      "aws_account_id": "123456789012",
      "aws_partition": "aws",
      "logs_config": {
        "lambda_forwarder": {
          "lambdas": [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"
          ],
          "log_source_config": {
            "tag_filters": [
              {
                "source": "s3",
                "tags": [
                  "test:test"
                ]
              }
            ]
          },
          "sources": [
            "s3"
          ]
        }
      },
      "metrics_config": {
        "automute_enabled": true,
        "collect_cloudwatch_alarms": true,
        "collect_custom_metrics": true,
        "enabled": true,
        "tag_filters": [
          {
            "namespace": "AWS/EC2",
            "tags": [
              "key:value"
            ]
          }
        ]
      },
      "resources_config": {
        "cloud_security_posture_management_collection": false,
        "extended_collection": false
      },
      "traces_config": {}
    },
    "type": "account"
  }
}
EOF
                        
##### 

```go
// Update an AWS integration returns "AWS Account object" response

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
	// there is a valid "aws_account_v2" in the system
	AwsAccountV2DataID := os.Getenv("AWS_ACCOUNT_V2_DATA_ID")

	body := datadogV2.AWSAccountUpdateRequest{
		Data: datadogV2.AWSAccountUpdateRequestData{
			Attributes: datadogV2.AWSAccountUpdateRequestAttributes{
				AccountTags: *datadog.NewNullableList(&[]string{
					"key:value",
				}),
				AuthConfig: &datadogV2.AWSAuthConfig{
					AWSAuthConfigRole: &datadogV2.AWSAuthConfigRole{
						RoleName: "DatadogIntegrationRole",
					}},
				AwsAccountId: "123456789012",
				AwsPartition: datadogV2.AWSACCOUNTPARTITION_AWS.Ptr(),
				CcmConfig: &datadogV2.AWSCCMConfig{
					DataExportConfigs: []datadogV2.DataExportConfig{
						{
							BucketName:   datadog.PtrString("updated-bucket"),
							BucketRegion: datadog.PtrString("us-west-2"),
							ReportName:   datadog.PtrString("updated-report"),
							ReportPrefix: datadog.PtrString("cost-reports"),
							ReportType:   datadog.PtrString("CUR2.0"),
						},
					},
				},
				LogsConfig: &datadogV2.AWSLogsConfig{
					LambdaForwarder: &datadogV2.AWSLambdaForwarderConfig{
						Lambdas: []string{
							"arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
						},
						LogSourceConfig: &datadogV2.AWSLambdaForwarderConfigLogSourceConfig{
							TagFilters: []datadogV2.AWSLogSourceTagFilter{
								{
									Source: datadog.PtrString("s3"),
									Tags: *datadog.NewNullableList(&[]string{
										"test:test",
									}),
								},
							},
						},
						Sources: []string{
							"s3",
						},
					},
				},
				MetricsConfig: &datadogV2.AWSMetricsConfig{
					AutomuteEnabled:         datadog.PtrBool(true),
					CollectCloudwatchAlarms: datadog.PtrBool(true),
					CollectCustomMetrics:    datadog.PtrBool(true),
					Enabled:                 datadog.PtrBool(true),
					TagFilters: []datadogV2.AWSNamespaceTagFilter{
						{
							Namespace: datadog.PtrString("AWS/EC2"),
							Tags: *datadog.NewNullableList(&[]string{
								"key:value",
							}),
						},
					},
				},
				ResourcesConfig: &datadogV2.AWSResourcesConfig{
					CloudSecurityPostureManagementCollection: datadog.PtrBool(false),
					ExtendedCollection:                       datadog.PtrBool(false),
				},
				TracesConfig: &datadogV2.AWSTracesConfig{},
			},
			Type: datadogV2.AWSACCOUNTTYPE_ACCOUNT,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.UpdateAWSAccount(ctx, AwsAccountV2DataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.UpdateAWSAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.UpdateAWSAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update an AWS integration returns "AWS Account object" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSAccountPartition;
import com.datadog.api.client.v2.model.AWSAccountResponse;
import com.datadog.api.client.v2.model.AWSAccountType;
import com.datadog.api.client.v2.model.AWSAccountUpdateRequest;
import com.datadog.api.client.v2.model.AWSAccountUpdateRequestAttributes;
import com.datadog.api.client.v2.model.AWSAccountUpdateRequestData;
import com.datadog.api.client.v2.model.AWSAuthConfig;
import com.datadog.api.client.v2.model.AWSAuthConfigRole;
import com.datadog.api.client.v2.model.AWSCCMConfig;
import com.datadog.api.client.v2.model.AWSLambdaForwarderConfig;
import com.datadog.api.client.v2.model.AWSLambdaForwarderConfigLogSourceConfig;
import com.datadog.api.client.v2.model.AWSLogSourceTagFilter;
import com.datadog.api.client.v2.model.AWSLogsConfig;
import com.datadog.api.client.v2.model.AWSMetricsConfig;
import com.datadog.api.client.v2.model.AWSNamespaceTagFilter;
import com.datadog.api.client.v2.model.AWSResourcesConfig;
import com.datadog.api.client.v2.model.AWSTracesConfig;
import com.datadog.api.client.v2.model.DataExportConfig;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    // there is a valid "aws_account_v2" in the system
    String AWS_ACCOUNT_V2_DATA_ID = System.getenv("AWS_ACCOUNT_V2_DATA_ID");

    AWSAccountUpdateRequest body =
        new AWSAccountUpdateRequest()
            .data(
                new AWSAccountUpdateRequestData()
                    .attributes(
                        new AWSAccountUpdateRequestAttributes()
                            .accountTags(Collections.singletonList("key:value"))
                            .authConfig(
                                new AWSAuthConfig(
                                    new AWSAuthConfigRole().roleName("DatadogIntegrationRole")))
                            .awsAccountId("123456789012")
                            .awsPartition(AWSAccountPartition.AWS)
                            .ccmConfig(
                                new AWSCCMConfig()
                                    .dataExportConfigs(
                                        Collections.singletonList(
                                            new DataExportConfig()
                                                .bucketName("updated-bucket")
                                                .bucketRegion("us-west-2")
                                                .reportName("updated-report")
                                                .reportPrefix("cost-reports")
                                                .reportType("CUR2.0"))))
                            .logsConfig(
                                new AWSLogsConfig()
                                    .lambdaForwarder(
                                        new AWSLambdaForwarderConfig()
                                            .lambdas(
                                                Collections.singletonList(
                                                    "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"))
                                            .logSourceConfig(
                                                new AWSLambdaForwarderConfigLogSourceConfig()
                                                    .tagFilters(
                                                        Collections.singletonList(
                                                            new AWSLogSourceTagFilter()
                                                                .source("s3")
                                                                .tags(
                                                                    Collections.singletonList(
                                                                        "test:test")))))
                                            .sources(Collections.singletonList("s3"))))
                            .metricsConfig(
                                new AWSMetricsConfig()
                                    .automuteEnabled(true)
                                    .collectCloudwatchAlarms(true)
                                    .collectCustomMetrics(true)
                                    .enabled(true)
                                    .tagFilters(
                                        Collections.singletonList(
                                            new AWSNamespaceTagFilter()
                                                .namespace("AWS/EC2")
                                                .tags(Collections.singletonList("key:value")))))
                            .resourcesConfig(
                                new AWSResourcesConfig()
                                    .cloudSecurityPostureManagementCollection(false)
                                    .extendedCollection(false))
                            .tracesConfig(new AWSTracesConfig()))
                    .type(AWSAccountType.ACCOUNT));

    try {
      AWSAccountResponse result = apiInstance.updateAWSAccount(AWS_ACCOUNT_V2_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#updateAWSAccount");
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

```python
"""
Update an AWS integration returns "AWS Account object" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
from datadog_api_client.v2.model.aws_account_type import AWSAccountType
from datadog_api_client.v2.model.aws_account_update_request import AWSAccountUpdateRequest
from datadog_api_client.v2.model.aws_account_update_request_attributes import AWSAccountUpdateRequestAttributes
from datadog_api_client.v2.model.aws_account_update_request_data import AWSAccountUpdateRequestData
from datadog_api_client.v2.model.aws_auth_config_role import AWSAuthConfigRole
from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig
from datadog_api_client.v2.model.aws_lambda_forwarder_config_log_source_config import (
    AWSLambdaForwarderConfigLogSourceConfig,
)
from datadog_api_client.v2.model.aws_log_source_tag_filter import AWSLogSourceTagFilter
from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig
from datadog_api_client.v2.model.awsccm_config import AWSCCMConfig
from datadog_api_client.v2.model.data_export_config import DataExportConfig

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ID = environ["AWS_ACCOUNT_V2_DATA_ID"]

body = AWSAccountUpdateRequest(
    data=AWSAccountUpdateRequestData(
        attributes=AWSAccountUpdateRequestAttributes(
            account_tags=[
                "key:value",
            ],
            auth_config=AWSAuthConfigRole(
                role_name="DatadogIntegrationRole",
            ),
            aws_account_id="123456789012",
            aws_partition=AWSAccountPartition.AWS,
            ccm_config=AWSCCMConfig(
                data_export_configs=[
                    DataExportConfig(
                        bucket_name="updated-bucket",
                        bucket_region="us-west-2",
                        report_name="updated-report",
                        report_prefix="cost-reports",
                        report_type="CUR2.0",
                    ),
                ],
            ),
            logs_config=AWSLogsConfig(
                lambda_forwarder=AWSLambdaForwarderConfig(
                    lambdas=[
                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
                    ],
                    log_source_config=AWSLambdaForwarderConfigLogSourceConfig(
                        tag_filters=[
                            AWSLogSourceTagFilter(
                                source="s3",
                                tags=[
                                    "test:test",
                                ],
                            ),
                        ],
                    ),
                    sources=[
                        "s3",
                    ],
                ),
            ),
            metrics_config=AWSMetricsConfig(
                automute_enabled=True,
                collect_cloudwatch_alarms=True,
                collect_custom_metrics=True,
                enabled=True,
                tag_filters=[
                    AWSNamespaceTagFilter(
                        namespace="AWS/EC2",
                        tags=[
                            "key:value",
                        ],
                    ),
                ],
            ),
            resources_config=AWSResourcesConfig(
                cloud_security_posture_management_collection=False,
                extended_collection=False,
            ),
            traces_config=AWSTracesConfig(),
        ),
        type=AWSAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.update_aws_account(aws_account_config_id=AWS_ACCOUNT_V2_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update an AWS integration returns "AWS Account object" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ID = ENV["AWS_ACCOUNT_V2_DATA_ID"]

body = DatadogAPIClient::V2::AWSAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::AWSAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::AWSAccountUpdateRequestAttributes.new({
      account_tags: [
        "key:value",
      ],
      auth_config: DatadogAPIClient::V2::AWSAuthConfigRole.new({
        role_name: "DatadogIntegrationRole",
      }),
      aws_account_id: "123456789012",
      aws_partition: DatadogAPIClient::V2::AWSAccountPartition::AWS,
      ccm_config: DatadogAPIClient::V2::AWSCCMConfig.new({
        data_export_configs: [
          DatadogAPIClient::V2::DataExportConfig.new({
            bucket_name: "updated-bucket",
            bucket_region: "us-west-2",
            report_name: "updated-report",
            report_prefix: "cost-reports",
            report_type: "CUR2.0",
          }),
        ],
      }),
      logs_config: DatadogAPIClient::V2::AWSLogsConfig.new({
        lambda_forwarder: DatadogAPIClient::V2::AWSLambdaForwarderConfig.new({
          lambdas: [
            "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
          ],
          log_source_config: DatadogAPIClient::V2::AWSLambdaForwarderConfigLogSourceConfig.new({
            tag_filters: [
              DatadogAPIClient::V2::AWSLogSourceTagFilter.new({
                source: "s3",
                tags: [
                  "test:test",
                ],
              }),
            ],
          }),
          sources: [
            "s3",
          ],
        }),
      }),
      metrics_config: DatadogAPIClient::V2::AWSMetricsConfig.new({
        automute_enabled: true,
        collect_cloudwatch_alarms: true,
        collect_custom_metrics: true,
        enabled: true,
        tag_filters: [
          DatadogAPIClient::V2::AWSNamespaceTagFilter.new({
            namespace: "AWS/EC2",
            tags: [
              "key:value",
            ],
          }),
        ],
      }),
      resources_config: DatadogAPIClient::V2::AWSResourcesConfig.new({
        cloud_security_posture_management_collection: false,
        extended_collection: false,
      }),
      traces_config: DatadogAPIClient::V2::AWSTracesConfig.new({}),
    }),
    type: DatadogAPIClient::V2::AWSAccountType::ACCOUNT,
  }),
})
p api_instance.update_aws_account(AWS_ACCOUNT_V2_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update an AWS integration returns "AWS Account object" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV2::model::AWSAccountPartition;
use datadog_api_client::datadogV2::model::AWSAccountType;
use datadog_api_client::datadogV2::model::AWSAccountUpdateRequest;
use datadog_api_client::datadogV2::model::AWSAccountUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::AWSAccountUpdateRequestData;
use datadog_api_client::datadogV2::model::AWSAuthConfig;
use datadog_api_client::datadogV2::model::AWSAuthConfigRole;
use datadog_api_client::datadogV2::model::AWSCCMConfig;
use datadog_api_client::datadogV2::model::AWSLambdaForwarderConfig;
use datadog_api_client::datadogV2::model::AWSLambdaForwarderConfigLogSourceConfig;
use datadog_api_client::datadogV2::model::AWSLogSourceTagFilter;
use datadog_api_client::datadogV2::model::AWSLogsConfig;
use datadog_api_client::datadogV2::model::AWSMetricsConfig;
use datadog_api_client::datadogV2::model::AWSNamespaceTagFilter;
use datadog_api_client::datadogV2::model::AWSResourcesConfig;
use datadog_api_client::datadogV2::model::AWSTracesConfig;
use datadog_api_client::datadogV2::model::DataExportConfig;

#[tokio::main]
async fn main() {
    // there is a valid "aws_account_v2" in the system
    let aws_account_v2_data_id = std::env::var("AWS_ACCOUNT_V2_DATA_ID").unwrap();
    let body =
        AWSAccountUpdateRequest::new(
            AWSAccountUpdateRequestData::new(
                AWSAccountUpdateRequestAttributes::new("123456789012".to_string())
                    .account_tags(Some(vec!["key:value".to_string()]))
                    .auth_config(
                        AWSAuthConfig::AWSAuthConfigRole(
                            Box::new(AWSAuthConfigRole::new("DatadogIntegrationRole".to_string())),
                        ),
                    )
                    .aws_partition(AWSAccountPartition::AWS)
                    .ccm_config(
                        AWSCCMConfig
                        ::new().data_export_configs(
                            vec![
                                DataExportConfig::new()
                                    .bucket_name("updated-bucket".to_string())
                                    .bucket_region("us-west-2".to_string())
                                    .report_name("updated-report".to_string())
                                    .report_prefix("cost-reports".to_string())
                                    .report_type("CUR2.0".to_string())
                            ],
                        ),
                    )
                    .logs_config(
                        AWSLogsConfig
                        ::new().lambda_forwarder(
                            AWSLambdaForwarderConfig::new()
                                .lambdas(
                                    vec![
                                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder".to_string()
                                    ],
                                )
                                .log_source_config(
                                    AWSLambdaForwarderConfigLogSourceConfig
                                    ::new().tag_filters(
                                        vec![
                                            AWSLogSourceTagFilter::new()
                                                .source("s3".to_string())
                                                .tags(Some(vec!["test:test".to_string()]))
                                        ],
                                    ),
                                )
                                .sources(vec!["s3".to_string()]),
                        ),
                    )
                    .metrics_config(
                        AWSMetricsConfig::new()
                            .automute_enabled(true)
                            .collect_cloudwatch_alarms(true)
                            .collect_custom_metrics(true)
                            .enabled(true)
                            .tag_filters(
                                vec![
                                    AWSNamespaceTagFilter::new()
                                        .namespace("AWS/EC2".to_string())
                                        .tags(Some(vec!["key:value".to_string()]))
                                ],
                            ),
                    )
                    .resources_config(
                        AWSResourcesConfig::new()
                            .cloud_security_posture_management_collection(false)
                            .extended_collection(false),
                    )
                    .traces_config(AWSTracesConfig::new()),
                AWSAccountType::ACCOUNT,
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api
        .update_aws_account(aws_account_v2_data_id.clone(), body)
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
 * Update an AWS integration returns "AWS Account object" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

// there is a valid "aws_account_v2" in the system
const AWS_ACCOUNT_V2_DATA_ID = process.env.AWS_ACCOUNT_V2_DATA_ID as string;

const params: v2.AWSIntegrationApiUpdateAWSAccountRequest = {
  body: {
    data: {
      attributes: {
        accountTags: ["key:value"],
        authConfig: {
          roleName: "DatadogIntegrationRole",
        },
        awsAccountId: "123456789012",
        awsPartition: "aws",
        ccmConfig: {
          dataExportConfigs: [
            {
              bucketName: "updated-bucket",
              bucketRegion: "us-west-2",
              reportName: "updated-report",
              reportPrefix: "cost-reports",
              reportType: "CUR2.0",
            },
          ],
        },
        logsConfig: {
          lambdaForwarder: {
            lambdas: [
              "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
            ],
            logSourceConfig: {
              tagFilters: [
                {
                  source: "s3",
                  tags: ["test:test"],
                },
              ],
            },
            sources: ["s3"],
          },
        },
        metricsConfig: {
          automuteEnabled: true,
          collectCloudwatchAlarms: true,
          collectCustomMetrics: true,
          enabled: true,
          tagFilters: [
            {
              namespace: "AWS/EC2",
              tags: ["key:value"],
            },
          ],
        },
        resourcesConfig: {
          cloudSecurityPostureManagementCollection: false,
          extendedCollection: false,
        },
        tracesConfig: {},
      },
      type: "account",
    },
  },
  awsAccountConfigId: AWS_ACCOUNT_V2_DATA_ID,
};

apiInstance
  .updateAWSAccount(params)
  .then((data: v2.AWSAccountResponse) => {
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

## Get all Amazon EventBridge sources{% #get-all-amazon-eventbridge-sources %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/integration/aws/event_bridge |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/integration/aws/event_bridge |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/integration/aws/event_bridge      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/integration/aws/event_bridge      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/integration/aws/event_bridge     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/integration/aws/event_bridge |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/integration/aws/event_bridge |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** Get all Amazon EventBridge sources.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An object describing the EventBridge configuration for multiple accounts.

| Parent field | Field       | Type     | Description                                                                                                                  |
| ------------ | ----------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | accounts    | [object] | List of accounts with their event sources.                                                                                   |
| accounts     | accountId   | string   | Your AWS Account ID without dashes.                                                                                          |
| accounts     | eventHubs   | [object] | Array of AWS event sources associated with this account.                                                                     |
| eventHubs    | name        | string   | The event source name.                                                                                                       |
| eventHubs    | region      | string   | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).                |
| accounts     | tags        | [string] | Array of tags (in the form `key:value`) which are added to all hosts and metrics reporting through the main AWS integration. |
|              | isInstalled | boolean  | True if the EventBridge sub-integration is enabled for your organization.                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "accounts": [
    {
      "accountId": "123456789012",
      "eventHubs": [
        {
          "name": "string",
          "region": "string"
        }
      ],
      "tags": [
        "$KEY:$VALUE"
      ]
    }
  ],
  "isInstalled": false
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/event_bridge" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all Amazon EventBridge sources returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_aws_event_bridge_sources()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all Amazon EventBridge sources returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new
p api_instance.list_aws_event_bridge_sources()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all Amazon EventBridge sources returns "OK" response

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
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.ListAWSEventBridgeSources(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.ListAWSEventBridgeSources`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.ListAWSEventBridgeSources`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all Amazon EventBridge sources returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSEventBridgeListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSEventBridgeListResponse result = apiInstance.listAWSEventBridgeSources();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#listAWSEventBridgeSources");
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
// Get all Amazon EventBridge sources returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.list_aws_event_bridge_sources().await;
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
 * Get all Amazon EventBridge sources returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

apiInstance
  .listAWSEventBridgeSources()
  .then((data: v1.AWSEventBridgeListResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/aws/event_bridge |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/aws/event_bridge |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/aws/event_bridge      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/aws/event_bridge      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/aws/event_bridge     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/aws/event_bridge |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/aws/event_bridge |

### Overview

Get all Amazon EventBridge sources. This endpoint requires the `integrations_read` permission.

### Response

{% tab title="200" %}
Amazon EventBridge sources list.
{% tab title="Model" %}
Amazon EventBridge list response body.

| Parent field | Field                        | Type     | Description                                                                                                                  |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Amazon EventBridge list response data.                                                                                       |
| data         | attributes [*required*] | object   | An object describing the EventBridge configuration for multiple accounts.                                                    |
| attributes   | accounts                     | [object] | List of accounts with their event sources.                                                                                   |
| accounts     | account_id                   | string   | Your AWS Account ID without dashes.                                                                                          |
| accounts     | event_hubs                   | [object] | Array of AWS event sources associated with this account.                                                                     |
| event_hubs   | name                         | string   | The event source name.                                                                                                       |
| event_hubs   | region                       | string   | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).                |
| accounts     | tags                         | [string] | Array of tags (in the form `key:value`) which are added to all hosts and metrics reporting through the main AWS integration. |
| attributes   | is_installed                 | boolean  | True if the EventBridge integration is enabled for your organization.                                                        |
| data         | id [*required*]         | string   | The ID of the Amazon EventBridge list response data.                                                                         |
| data         | type [*required*]       | enum     | Amazon EventBridge resource type. Allowed enum values: `event_bridge`                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "accounts": [
        {
          "account_id": "123456789012",
          "event_hubs": [
            {
              "name": "app-alerts-zyxw3210",
              "region": "us-east-1"
            }
          ],
          "tags": [
            "$KEY:$VALUE"
          ]
        }
      ],
      "is_installed": false
    },
    "id": "get_event_bridge",
    "type": "event_bridge"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/event_bridge" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all Amazon EventBridge sources returns "Amazon EventBridge sources list." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_aws_event_bridge_sources()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all Amazon EventBridge sources returns "Amazon EventBridge sources list." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new
p api_instance.list_aws_event_bridge_sources()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all Amazon EventBridge sources returns "Amazon EventBridge sources list." response

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
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.ListAWSEventBridgeSources(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.ListAWSEventBridgeSources`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.ListAWSEventBridgeSources`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all Amazon EventBridge sources returns "Amazon EventBridge sources list." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSEventBridgeListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    try {
      AWSEventBridgeListResponse result = apiInstance.listAWSEventBridgeSources();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#listAWSEventBridgeSources");
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
// Get all Amazon EventBridge sources returns "Amazon EventBridge sources list."
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.list_aws_event_bridge_sources().await;
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
 * Get all Amazon EventBridge sources returns "Amazon EventBridge sources list." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

apiInstance
  .listAWSEventBridgeSources()
  .then((data: v2.AWSEventBridgeListResponse) => {
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

## Create an Amazon EventBridge source{% #create-an-amazon-eventbridge-source %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/integration/aws/event_bridge |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/integration/aws/event_bridge |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/integration/aws/event_bridge      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/integration/aws/event_bridge      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/integration/aws/event_bridge     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/integration/aws/event_bridge |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/integration/aws/event_bridge |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** Create an Amazon EventBridge source. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)

Create an Amazon EventBridge source for an AWS account with a given name and region.

{% tab title="Model" %}

| Field                | Type    | Description                                                                                                                   |
| -------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| account_id           | string  | Your AWS Account ID without dashes.                                                                                           |
| create_event_bus     | boolean | True if Datadog should create the event bus in addition to the event source. Requires the `events:CreateEventBus` permission. |
| event_generator_name | string  | The given part of the event source name, which is then combined with an assigned suffix to form the full name.                |
| region               | string  | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "123456789012",
  "create_event_bus": true,
  "event_generator_name": "app-alerts",
  "region": "us-east-1"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A created EventBridge source.

| Field             | Type    | Description                                                                                                   |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| event_source_name | string  | The event source name.                                                                                        |
| has_bus           | boolean | True if the event bus was created in addition to the source.                                                  |
| region            | string  | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints). |
| status            | enum    | The event source status "created". Allowed enum values: `created`                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "event_source_name": "app-alerts-zyxw3210",
  "has_bus": true,
  "region": "us-east-1",
  "status": "created"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/event_bridge" \
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
Create an Amazon EventBridge source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_event_bridge_create_request import AWSEventBridgeCreateRequest

body = AWSEventBridgeCreateRequest(
    account_id="123456789012",
    create_event_bus=True,
    event_generator_name="app-alerts",
    region="us-east-1",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_event_bridge_source(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create an Amazon EventBridge source returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSEventBridgeCreateRequest.new({
  account_id: "123456789012",
  create_event_bus: true,
  event_generator_name: "app-alerts",
  region: "us-east-1",
})
p api_instance.create_aws_event_bridge_source(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Create an Amazon EventBridge source returns "OK" response

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
	body := datadogV1.AWSEventBridgeCreateRequest{
		AccountId:          datadog.PtrString("123456789012"),
		CreateEventBus:     datadog.PtrBool(true),
		EventGeneratorName: datadog.PtrString("app-alerts"),
		Region:             datadog.PtrString("us-east-1"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateAWSEventBridgeSource(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateAWSEventBridgeSource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateAWSEventBridgeSource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create an Amazon EventBridge source returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSEventBridgeCreateRequest;
import com.datadog.api.client.v1.model.AWSEventBridgeCreateResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSEventBridgeCreateRequest body =
        new AWSEventBridgeCreateRequest()
            .accountId("123456789012")
            .createEventBus(true)
            .eventGeneratorName("app-alerts")
            .region("us-east-1");

    try {
      AWSEventBridgeCreateResponse result = apiInstance.createAWSEventBridgeSource(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createAWSEventBridgeSource");
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
// Create an Amazon EventBridge source returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSEventBridgeCreateRequest;

#[tokio::main]
async fn main() {
    let body = AWSEventBridgeCreateRequest::new()
        .account_id("123456789012".to_string())
        .create_event_bus(true)
        .event_generator_name("app-alerts".to_string())
        .region("us-east-1".to_string());
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_aws_event_bridge_source(body).await;
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
 * Create an Amazon EventBridge source returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiCreateAWSEventBridgeSourceRequest = {
  body: {
    accountId: "123456789012",
    createEventBus: true,
    eventGeneratorName: "app-alerts",
    region: "us-east-1",
  },
};

apiInstance
  .createAWSEventBridgeSource(params)
  .then((data: v1.AWSEventBridgeCreateResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/aws/event_bridge |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/aws/event_bridge |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/aws/event_bridge      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/aws/event_bridge      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/aws/event_bridge     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/aws/event_bridge |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/aws/event_bridge |

### Overview

Create an Amazon EventBridge source. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)

Create an Amazon EventBridge source for an AWS account with a given name and region.

{% tab title="Model" %}

| Parent field | Field                                  | Type    | Description                                                                                                                          |
| ------------ | -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
|              | data [*required*]                 | object  | Amazon EventBridge create request data.                                                                                              |
| data         | attributes [*required*]           | object  | The EventBridge source to be created.                                                                                                |
| attributes   | account_id [*required*]           | string  | AWS Account ID.                                                                                                                      |
| attributes   | create_event_bus                       | boolean | Set to true if Datadog should create the event bus in addition to the event source. Requires the `events:CreateEventBus` permission. |
| attributes   | event_generator_name [*required*] | string  | The given part of the event source name, which is then combined with an assigned suffix to form the full name.                       |
| attributes   | region [*required*]               | string  | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).                        |
| data         | type [*required*]                 | enum    | Amazon EventBridge resource type. Allowed enum values: `event_bridge`                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_id": "123456789012",
      "create_event_bus": true,
      "event_generator_name": "app-alerts",
      "region": "us-east-1"
    },
    "type": "event_bridge"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Amazon EventBridge source created.
{% tab title="Model" %}
Amazon EventBridge create response body.

| Parent field | Field                        | Type    | Description                                                                                                   |
| ------------ | ---------------------------- | ------- | ------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object  | Amazon EventBridge create response data.                                                                      |
| data         | attributes [*required*] | object  | A created EventBridge source.                                                                                 |
| attributes   | event_source_name            | string  | The event source name.                                                                                        |
| attributes   | has_bus                      | boolean | True if the event bus was created in addition to the source.                                                  |
| attributes   | region                       | string  | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints). |
| attributes   | status                       | enum    | The event source status "created". Allowed enum values: `created`                                             |
| data         | id                           | string  | The ID of the Amazon EventBridge create response data.                                                        |
| data         | type [*required*]       | enum    | Amazon EventBridge resource type. Allowed enum values: `event_bridge`                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "event_source_name": "app-alerts-zyxw3210",
      "has_bus": true,
      "region": "us-east-1",
      "status": "created"
    },
    "id": "create_event_bridge",
    "type": "event_bridge"
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

{% tab title="409" %}
Conflict
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/event_bridge" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_id": "123456789012",
      "event_generator_name": "app-alerts",
      "region": "us-east-1"
    },
    "type": "event_bridge"
  }
}
EOF
                
##### 

```python
"""
Create an Amazon EventBridge source returns "Amazon EventBridge source created." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_event_bridge_create_request import AWSEventBridgeCreateRequest
from datadog_api_client.v2.model.aws_event_bridge_create_request_attributes import AWSEventBridgeCreateRequestAttributes
from datadog_api_client.v2.model.aws_event_bridge_create_request_data import AWSEventBridgeCreateRequestData
from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType

body = AWSEventBridgeCreateRequest(
    data=AWSEventBridgeCreateRequestData(
        attributes=AWSEventBridgeCreateRequestAttributes(
            account_id="123456789012",
            create_event_bus=True,
            event_generator_name="app-alerts",
            region="us-east-1",
        ),
        type=AWSEventBridgeType.EVENT_BRIDGE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_event_bridge_source(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create an Amazon EventBridge source returns "Amazon EventBridge source created." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new

body = DatadogAPIClient::V2::AWSEventBridgeCreateRequest.new({
  data: DatadogAPIClient::V2::AWSEventBridgeCreateRequestData.new({
    attributes: DatadogAPIClient::V2::AWSEventBridgeCreateRequestAttributes.new({
      account_id: "123456789012",
      create_event_bus: true,
      event_generator_name: "app-alerts",
      region: "us-east-1",
    }),
    type: DatadogAPIClient::V2::AWSEventBridgeType::EVENT_BRIDGE,
  }),
})
p api_instance.create_aws_event_bridge_source(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Create an Amazon EventBridge source returns "Amazon EventBridge source created." response

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
	body := datadogV2.AWSEventBridgeCreateRequest{
		Data: datadogV2.AWSEventBridgeCreateRequestData{
			Attributes: datadogV2.AWSEventBridgeCreateRequestAttributes{
				AccountId:          "123456789012",
				CreateEventBus:     datadog.PtrBool(true),
				EventGeneratorName: "app-alerts",
				Region:             "us-east-1",
			},
			Type: datadogV2.AWSEVENTBRIDGETYPE_EVENT_BRIDGE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.CreateAWSEventBridgeSource(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.CreateAWSEventBridgeSource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.CreateAWSEventBridgeSource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create an Amazon EventBridge source returns "Amazon EventBridge source created." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSEventBridgeCreateRequest;
import com.datadog.api.client.v2.model.AWSEventBridgeCreateRequestAttributes;
import com.datadog.api.client.v2.model.AWSEventBridgeCreateRequestData;
import com.datadog.api.client.v2.model.AWSEventBridgeCreateResponse;
import com.datadog.api.client.v2.model.AWSEventBridgeType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSEventBridgeCreateRequest body =
        new AWSEventBridgeCreateRequest()
            .data(
                new AWSEventBridgeCreateRequestData()
                    .attributes(
                        new AWSEventBridgeCreateRequestAttributes()
                            .accountId("123456789012")
                            .createEventBus(true)
                            .eventGeneratorName("app-alerts")
                            .region("us-east-1"))
                    .type(AWSEventBridgeType.EVENT_BRIDGE));

    try {
      AWSEventBridgeCreateResponse result = apiInstance.createAWSEventBridgeSource(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#createAWSEventBridgeSource");
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
// Create an Amazon EventBridge source returns "Amazon EventBridge source
// created." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV2::model::AWSEventBridgeCreateRequest;
use datadog_api_client::datadogV2::model::AWSEventBridgeCreateRequestAttributes;
use datadog_api_client::datadogV2::model::AWSEventBridgeCreateRequestData;
use datadog_api_client::datadogV2::model::AWSEventBridgeType;

#[tokio::main]
async fn main() {
    let body = AWSEventBridgeCreateRequest::new(AWSEventBridgeCreateRequestData::new(
        AWSEventBridgeCreateRequestAttributes::new(
            "123456789012".to_string(),
            "app-alerts".to_string(),
            "us-east-1".to_string(),
        )
        .create_event_bus(true),
        AWSEventBridgeType::EVENT_BRIDGE,
    ));
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.create_aws_event_bridge_source(body).await;
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
 * Create an Amazon EventBridge source returns "Amazon EventBridge source created." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

const params: v2.AWSIntegrationApiCreateAWSEventBridgeSourceRequest = {
  body: {
    data: {
      attributes: {
        accountId: "123456789012",
        createEventBus: true,
        eventGeneratorName: "app-alerts",
        region: "us-east-1",
      },
      type: "event_bridge",
    },
  },
};

apiInstance
  .createAWSEventBridgeSource(params)
  .then((data: v2.AWSEventBridgeCreateResponse) => {
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

## Delete an Amazon EventBridge source{% #delete-an-amazon-eventbridge-source %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/integration/aws/event_bridge |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/integration/aws/event_bridge |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/integration/aws/event_bridge      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/integration/aws/event_bridge      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/integration/aws/event_bridge     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/integration/aws/event_bridge |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/integration/aws/event_bridge |

### Overview

**This endpoint is deprecated - use the V2 endpoints instead.** Delete an Amazon EventBridge source. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)

Delete the Amazon EventBridge source with the given name, region, and associated AWS account.

{% tab title="Model" %}

| Field                | Type   | Description                                                                                                   |
| -------------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| account_id           | string | Your AWS Account ID without dashes.                                                                           |
| event_generator_name | string | The event source name.                                                                                        |
| region               | string | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints). |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account_id": "123456789012",
  "event_generator_name": "app-alerts-zyxw3210",
  "region": "us-east-1"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An indicator of the successful deletion of an EventBridge source.

| Field  | Type | Description                                                   |
| ------ | ---- | ------------------------------------------------------------- |
| status | enum | The event source status "empty". Allowed enum values: `empty` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "status": "empty"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/integration/aws/event_bridge" \
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
Delete an Amazon EventBridge source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_event_bridge_delete_request import AWSEventBridgeDeleteRequest

body = AWSEventBridgeDeleteRequest(
    account_id="123456789012",
    event_generator_name="app-alerts-zyxw3210",
    region="us-east-1",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_event_bridge_source(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an Amazon EventBridge source returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::AWSIntegrationAPI.new

body = DatadogAPIClient::V1::AWSEventBridgeDeleteRequest.new({
  account_id: "123456789012",
  event_generator_name: "app-alerts-zyxw3210",
  region: "us-east-1",
})
p api_instance.delete_aws_event_bridge_source(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete an Amazon EventBridge source returns "OK" response

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
	body := datadogV1.AWSEventBridgeDeleteRequest{
		AccountId:          datadog.PtrString("123456789012"),
		EventGeneratorName: datadog.PtrString("app-alerts-zyxw3210"),
		Region:             datadog.PtrString("us-east-1"),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.DeleteAWSEventBridgeSource(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.DeleteAWSEventBridgeSource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.DeleteAWSEventBridgeSource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete an Amazon EventBridge source returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.AwsIntegrationApi;
import com.datadog.api.client.v1.model.AWSEventBridgeDeleteRequest;
import com.datadog.api.client.v1.model.AWSEventBridgeDeleteResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSEventBridgeDeleteRequest body =
        new AWSEventBridgeDeleteRequest()
            .accountId("123456789012")
            .eventGeneratorName("app-alerts-zyxw3210")
            .region("us-east-1");

    try {
      AWSEventBridgeDeleteResponse result = apiInstance.deleteAWSEventBridgeSource(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#deleteAWSEventBridgeSource");
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
// Delete an Amazon EventBridge source returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV1::model::AWSEventBridgeDeleteRequest;

#[tokio::main]
async fn main() {
    let body = AWSEventBridgeDeleteRequest::new()
        .account_id("123456789012".to_string())
        .event_generator_name("app-alerts-zyxw3210".to_string())
        .region("us-east-1".to_string());
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.delete_aws_event_bridge_source(body).await;
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
 * Delete an Amazon EventBridge source returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.AWSIntegrationApi(configuration);

const params: v1.AWSIntegrationApiDeleteAWSEventBridgeSourceRequest = {
  body: {
    accountId: "123456789012",
    eventGeneratorName: "app-alerts-zyxw3210",
    region: "us-east-1",
  },
};

apiInstance
  .deleteAWSEventBridgeSource(params)
  .then((data: v1.AWSEventBridgeDeleteResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/aws/event_bridge |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/aws/event_bridge |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/aws/event_bridge      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/aws/event_bridge      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/aws/event_bridge     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/aws/event_bridge |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/aws/event_bridge |

### Overview

Delete an Amazon EventBridge source. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)

Delete the Amazon EventBridge source with the given name, region, and associated AWS account.

{% tab title="Model" %}

| Parent field | Field                                  | Type   | Description                                                                                                   |
| ------------ | -------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                 | object | Amazon EventBridge delete request data.                                                                       |
| data         | attributes [*required*]           | object | The EventBridge source to be deleted.                                                                         |
| attributes   | account_id [*required*]           | string | AWS Account ID.                                                                                               |
| attributes   | event_generator_name [*required*] | string | The event source name.                                                                                        |
| attributes   | region [*required*]               | string | The event source's [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints). |
| data         | type [*required*]                 | enum   | Amazon EventBridge resource type. Allowed enum values: `event_bridge`                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "account_id": "123456789012",
      "event_generator_name": "app-alerts-zyxw3210",
      "region": "us-east-1"
    },
    "type": "event_bridge"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
Amazon EventBridge source deleted.
{% tab title="Model" %}
Amazon EventBridge delete response body.

| Parent field | Field                        | Type   | Description                                                           |
| ------------ | ---------------------------- | ------ | --------------------------------------------------------------------- |
|              | data [*required*]       | object | Amazon EventBridge delete response data.                              |
| data         | attributes [*required*] | object | The EventBridge source delete response attributes.                    |
| attributes   | status                       | enum   | The event source status "empty". Allowed enum values: `empty`         |
| data         | id                           | string | The ID of the Amazon EventBridge list response data.                  |
| data         | type [*required*]       | enum   | Amazon EventBridge resource type. Allowed enum values: `event_bridge` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "status": "empty"
    },
    "id": "delete_event_bridge",
    "type": "event_bridge"
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
                  \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/aws/event_bridge" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "account_id": "123456789012",
      "event_generator_name": "app-alerts-zyxw3210",
      "region": "us-east-1"
    },
    "type": "event_bridge"
  }
}
EOF
                
##### 

```python
"""
Delete an Amazon EventBridge source returns "Amazon EventBridge source deleted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_event_bridge_delete_request import AWSEventBridgeDeleteRequest
from datadog_api_client.v2.model.aws_event_bridge_delete_request_attributes import AWSEventBridgeDeleteRequestAttributes
from datadog_api_client.v2.model.aws_event_bridge_delete_request_data import AWSEventBridgeDeleteRequestData
from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType

body = AWSEventBridgeDeleteRequest(
    data=AWSEventBridgeDeleteRequestData(
        attributes=AWSEventBridgeDeleteRequestAttributes(
            account_id="123456789012",
            event_generator_name="app-alerts-zyxw3210",
            region="us-east-1",
        ),
        type=AWSEventBridgeType.EVENT_BRIDGE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_event_bridge_source(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete an Amazon EventBridge source returns "Amazon EventBridge source deleted." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::AWSIntegrationAPI.new

body = DatadogAPIClient::V2::AWSEventBridgeDeleteRequest.new({
  data: DatadogAPIClient::V2::AWSEventBridgeDeleteRequestData.new({
    attributes: DatadogAPIClient::V2::AWSEventBridgeDeleteRequestAttributes.new({
      account_id: "123456789012",
      event_generator_name: "app-alerts-zyxw3210",
      region: "us-east-1",
    }),
    type: DatadogAPIClient::V2::AWSEventBridgeType::EVENT_BRIDGE,
  }),
})
p api_instance.delete_aws_event_bridge_source(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete an Amazon EventBridge source returns "Amazon EventBridge source deleted." response

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
	body := datadogV2.AWSEventBridgeDeleteRequest{
		Data: datadogV2.AWSEventBridgeDeleteRequestData{
			Attributes: datadogV2.AWSEventBridgeDeleteRequestAttributes{
				AccountId:          "123456789012",
				EventGeneratorName: "app-alerts-zyxw3210",
				Region:             "us-east-1",
			},
			Type: datadogV2.AWSEVENTBRIDGETYPE_EVENT_BRIDGE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAWSIntegrationApi(apiClient)
	resp, r, err := api.DeleteAWSEventBridgeSource(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AWSIntegrationApi.DeleteAWSEventBridgeSource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `AWSIntegrationApi.DeleteAWSEventBridgeSource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete an Amazon EventBridge source returns "Amazon EventBridge source deleted." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.AwsIntegrationApi;
import com.datadog.api.client.v2.model.AWSEventBridgeDeleteRequest;
import com.datadog.api.client.v2.model.AWSEventBridgeDeleteRequestAttributes;
import com.datadog.api.client.v2.model.AWSEventBridgeDeleteRequestData;
import com.datadog.api.client.v2.model.AWSEventBridgeDeleteResponse;
import com.datadog.api.client.v2.model.AWSEventBridgeType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    AwsIntegrationApi apiInstance = new AwsIntegrationApi(defaultClient);

    AWSEventBridgeDeleteRequest body =
        new AWSEventBridgeDeleteRequest()
            .data(
                new AWSEventBridgeDeleteRequestData()
                    .attributes(
                        new AWSEventBridgeDeleteRequestAttributes()
                            .accountId("123456789012")
                            .eventGeneratorName("app-alerts-zyxw3210")
                            .region("us-east-1"))
                    .type(AWSEventBridgeType.EVENT_BRIDGE));

    try {
      AWSEventBridgeDeleteResponse result = apiInstance.deleteAWSEventBridgeSource(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AwsIntegrationApi#deleteAWSEventBridgeSource");
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
// Delete an Amazon EventBridge source returns "Amazon EventBridge source
// deleted." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_aws_integration::AWSIntegrationAPI;
use datadog_api_client::datadogV2::model::AWSEventBridgeDeleteRequest;
use datadog_api_client::datadogV2::model::AWSEventBridgeDeleteRequestAttributes;
use datadog_api_client::datadogV2::model::AWSEventBridgeDeleteRequestData;
use datadog_api_client::datadogV2::model::AWSEventBridgeType;

#[tokio::main]
async fn main() {
    let body = AWSEventBridgeDeleteRequest::new(AWSEventBridgeDeleteRequestData::new(
        AWSEventBridgeDeleteRequestAttributes::new(
            "123456789012".to_string(),
            "app-alerts-zyxw3210".to_string(),
            "us-east-1".to_string(),
        ),
        AWSEventBridgeType::EVENT_BRIDGE,
    ));
    let configuration = datadog::Configuration::new();
    let api = AWSIntegrationAPI::with_config(configuration);
    let resp = api.delete_aws_event_bridge_source(body).await;
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
 * Delete an Amazon EventBridge source returns "Amazon EventBridge source deleted." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.AWSIntegrationApi(configuration);

const params: v2.AWSIntegrationApiDeleteAWSEventBridgeSourceRequest = {
  body: {
    data: {
      attributes: {
        accountId: "123456789012",
        eventGeneratorName: "app-alerts-zyxw3210",
        region: "us-east-1",
      },
      type: "event_bridge",
    },
  },
};

apiInstance
  .deleteAWSEventBridgeSource(params)
  .then((data: v2.AWSEventBridgeDeleteResponse) => {
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
