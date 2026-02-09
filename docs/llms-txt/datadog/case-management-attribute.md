# Source: https://docs.datadoghq.com/api/latest/case-management-attribute.md

---
title: Case Management Attribute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Case Management Attribute
---

# Case Management Attribute

View and configure custom attributes within Case Management. See the [Case Management page](https://docs.datadoghq.com/service_management/case_management/) for more information.

## Get all custom attributes{% #get-all-custom-attributes %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases/types/custom_attributes |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases/types/custom_attributes |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases/types/custom_attributes      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases/types/custom_attributes      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases/types/custom_attributes     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases/types/custom_attributes |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases/types/custom_attributes |

### Overview

Get all custom attributes

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Custom attribute configs response.

| Parent field | Field                          | Type     | Description                                                                             |
| ------------ | ------------------------------ | -------- | --------------------------------------------------------------------------------------- |
|              | data                           | [object] | List of custom attribute configs of case type                                           |
| data         | attributes                     | object   | Custom attribute resource attributes                                                    |
| attributes   | case_type_id [*required*] | string   | Custom attribute config identifier.                                                     |
| attributes   | description                    | string   | Custom attribute description.                                                           |
| attributes   | display_name [*required*] | string   | Custom attribute name.                                                                  |
| attributes   | is_multi [*required*]     | boolean  | Whether multiple values can be set                                                      |
| attributes   | key [*required*]          | string   | Custom attribute key. This will be the value use to search on this custom attribute     |
| attributes   | type [*required*]         | enum     | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                    |
| data         | id                             | string   | Custom attribute configs identifier                                                     |
| data         | type                           | enum     | Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "case_type_id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
        "description": "AWS Region, must be a valid region supported by AWS",
        "display_name": "AWS Region",
        "is_multi": true,
        "key": "aws_region",
        "type": "NUMBER"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "custom_attribute"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/custom_attributes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all custom attributes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.get_all_custom_attributes()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all custom attributes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new
p api_instance.get_all_custom_attributes()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all custom attributes returns "OK" response

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
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	resp, r, err := api.GetAllCustomAttributes(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.GetAllCustomAttributes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementAttributeApi.GetAllCustomAttributes`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all custom attributes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;
import com.datadog.api.client.v2.model.CustomAttributeConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    try {
      CustomAttributeConfigsResponse result = apiInstance.getAllCustomAttributes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CaseManagementAttributeApi#getAllCustomAttributes");
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
// Get all custom attributes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api.get_all_custom_attributes().await;
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
 * Get all custom attributes returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

apiInstance
  .getAllCustomAttributes()
  .then((data: v2.CustomAttributeConfigsResponse) => {
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

## Get all custom attributes config of case type{% #get-all-custom-attributes-config-of-case-type %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases/types/{case_type_id}/custom_attributes      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases/types/{case_type_id}/custom_attributes      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |

### Overview

Get all custom attribute config of case type

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| case_type_id [*required*] | string | Case type's UUID |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Custom attribute configs response.

| Parent field | Field                          | Type     | Description                                                                             |
| ------------ | ------------------------------ | -------- | --------------------------------------------------------------------------------------- |
|              | data                           | [object] | List of custom attribute configs of case type                                           |
| data         | attributes                     | object   | Custom attribute resource attributes                                                    |
| attributes   | case_type_id [*required*] | string   | Custom attribute config identifier.                                                     |
| attributes   | description                    | string   | Custom attribute description.                                                           |
| attributes   | display_name [*required*] | string   | Custom attribute name.                                                                  |
| attributes   | is_multi [*required*]     | boolean  | Whether multiple values can be set                                                      |
| attributes   | key [*required*]          | string   | Custom attribute key. This will be the value use to search on this custom attribute     |
| attributes   | type [*required*]         | enum     | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                    |
| data         | id                             | string   | Custom attribute configs identifier                                                     |
| data         | type                           | enum     | Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "case_type_id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
        "description": "AWS Region, must be a valid region supported by AWS",
        "display_name": "AWS Region",
        "is_multi": true,
        "key": "aws_region",
        "type": "NUMBER"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "custom_attribute"
    }
  ]
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

{% tab title="401" %}
Unauthorized
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
                  \# Path parametersexport case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}/custom_attributes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all custom attributes config of case type returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.get_all_custom_attribute_configs_by_case_type(
        case_type_id=CASE_TYPE_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all custom attributes config of case type returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new

# there is a valid "case_type" in the system
CASE_TYPE_ID = ENV["CASE_TYPE_ID"]
p api_instance.get_all_custom_attribute_configs_by_case_type(CASE_TYPE_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all custom attributes config of case type returns "OK" response

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
	// there is a valid "case_type" in the system
	CaseTypeID := os.Getenv("CASE_TYPE_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	resp, r, err := api.GetAllCustomAttributeConfigsByCaseType(ctx, CaseTypeID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.GetAllCustomAttributeConfigsByCaseType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementAttributeApi.GetAllCustomAttributeConfigsByCaseType`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all custom attributes config of case type returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;
import com.datadog.api.client.v2.model.CustomAttributeConfigsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    // there is a valid "case_type" in the system
    String CASE_TYPE_ID = System.getenv("CASE_TYPE_ID");

    try {
      CustomAttributeConfigsResponse result =
          apiInstance.getAllCustomAttributeConfigsByCaseType(CASE_TYPE_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling"
              + " CaseManagementAttributeApi#getAllCustomAttributeConfigsByCaseType");
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
// Get all custom attributes config of case type returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;

#[tokio::main]
async fn main() {
    // there is a valid "case_type" in the system
    let case_type_id = std::env::var("CASE_TYPE_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api
        .get_all_custom_attribute_configs_by_case_type(case_type_id.clone())
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
 * Get all custom attributes config of case type returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

// there is a valid "case_type" in the system
const CASE_TYPE_ID = process.env.CASE_TYPE_ID as string;

const params: v2.CaseManagementAttributeApiGetAllCustomAttributeConfigsByCaseTypeRequest =
  {
    caseTypeId: CASE_TYPE_ID,
  };

apiInstance
  .getAllCustomAttributeConfigsByCaseType(params)
  .then((data: v2.CustomAttributeConfigsResponse) => {
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

## Create custom attribute config for a case type{% #create-custom-attribute-config-for-a-case-type %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                           |
| ----------------- | -------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/types/{case_type_id}/custom_attributes      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/types/{case_type_id}/custom_attributes      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes |

### Overview

Create custom attribute config for a case type

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| case_type_id [*required*] | string | Case type's UUID |

### Request

#### Body Data (required)

Custom attribute config payload

{% tab title="Model" %}

| Parent field | Field                          | Type    | Description                                                                             |
| ------------ | ------------------------------ | ------- | --------------------------------------------------------------------------------------- |
|              | data [*required*]         | object  | Custom attribute config                                                                 |
| data         | attributes [*required*]   | object  | Custom attribute config resource attributes                                             |
| attributes   | description                    | string  | Custom attribute description.                                                           |
| attributes   | display_name [*required*] | string  | Custom attribute name.                                                                  |
| attributes   | is_multi [*required*]     | boolean | Whether multiple values can be set                                                      |
| attributes   | key [*required*]          | string  | Custom attribute key. This will be the value use to search on this custom attribute     |
| attributes   | type [*required*]         | enum    | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                    |
| data         | type [*required*]         | enum    | Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "display_name": "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
      "is_multi": true,
      "key": "region_d9fe56bc9274fbb6",
      "type": "NUMBER"
    },
    "type": "custom_attribute"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Custom attribute config response.

| Parent field | Field                          | Type    | Description                                                                             |
| ------------ | ------------------------------ | ------- | --------------------------------------------------------------------------------------- |
|              | data                           | object  | The definition of `CustomAttributeConfig` object.                                       |
| data         | attributes                     | object  | Custom attribute resource attributes                                                    |
| attributes   | case_type_id [*required*] | string  | Custom attribute config identifier.                                                     |
| attributes   | description                    | string  | Custom attribute description.                                                           |
| attributes   | display_name [*required*] | string  | Custom attribute name.                                                                  |
| attributes   | is_multi [*required*]     | boolean | Whether multiple values can be set                                                      |
| attributes   | key [*required*]          | string  | Custom attribute key. This will be the value use to search on this custom attribute     |
| attributes   | type [*required*]         | enum    | Custom attributes type Allowed enum values: `URL,TEXT,NUMBER,SELECT`                    |
| data         | id                             | string  | Custom attribute configs identifier                                                     |
| data         | type                           | enum    | Custom attributes config JSON:API resource type Allowed enum values: `custom_attribute` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "case_type_id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "description": "AWS Region, must be a valid region supported by AWS",
      "display_name": "AWS Region",
      "is_multi": true,
      "key": "aws_region",
      "type": "NUMBER"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "custom_attribute"
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

{% tab title="401" %}
Unauthorized
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
                          \# Path parametersexport case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}/custom_attributes" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "display_name": "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
      "is_multi": true,
      "key": "region_d9fe56bc9274fbb6",
      "type": "NUMBER"
    },
    "type": "custom_attribute"
  }
}
EOF
                        
##### 

```go
// Create custom attribute config for a case type returns "CREATED" response

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
	// there is a valid "case_type" in the system
	CaseTypeID := os.Getenv("CASE_TYPE_ID")

	body := datadogV2.CustomAttributeConfigCreateRequest{
		Data: datadogV2.CustomAttributeConfigCreate{
			Attributes: datadogV2.CustomAttributeConfigAttributesCreate{
				DisplayName: "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
				IsMulti:     true,
				Key:         "region_d9fe56bc9274fbb6",
				Type:        datadogV2.CUSTOMATTRIBUTETYPE_NUMBER,
			},
			Type: datadogV2.CUSTOMATTRIBUTECONFIGRESOURCETYPE_CUSTOM_ATTRIBUTE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	resp, r, err := api.CreateCustomAttributeConfig(ctx, CaseTypeID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.CreateCustomAttributeConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementAttributeApi.CreateCustomAttributeConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create custom attribute config for a case type returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;
import com.datadog.api.client.v2.model.CustomAttributeConfigAttributesCreate;
import com.datadog.api.client.v2.model.CustomAttributeConfigCreate;
import com.datadog.api.client.v2.model.CustomAttributeConfigCreateRequest;
import com.datadog.api.client.v2.model.CustomAttributeConfigResourceType;
import com.datadog.api.client.v2.model.CustomAttributeConfigResponse;
import com.datadog.api.client.v2.model.CustomAttributeType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    // there is a valid "case_type" in the system
    String CASE_TYPE_ID = System.getenv("CASE_TYPE_ID");

    CustomAttributeConfigCreateRequest body =
        new CustomAttributeConfigCreateRequest()
            .data(
                new CustomAttributeConfigCreate()
                    .attributes(
                        new CustomAttributeConfigAttributesCreate()
                            .displayName("AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d")
                            .isMulti(true)
                            .key("region_d9fe56bc9274fbb6")
                            .type(CustomAttributeType.NUMBER))
                    .type(CustomAttributeConfigResourceType.CUSTOM_ATTRIBUTE));

    try {
      CustomAttributeConfigResponse result =
          apiInstance.createCustomAttributeConfig(CASE_TYPE_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CaseManagementAttributeApi#createCustomAttributeConfig");
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
Create custom attribute config for a case type returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi
from datadog_api_client.v2.model.custom_attribute_config_attributes_create import CustomAttributeConfigAttributesCreate
from datadog_api_client.v2.model.custom_attribute_config_create import CustomAttributeConfigCreate
from datadog_api_client.v2.model.custom_attribute_config_create_request import CustomAttributeConfigCreateRequest
from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType
from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

body = CustomAttributeConfigCreateRequest(
    data=CustomAttributeConfigCreate(
        attributes=CustomAttributeConfigAttributesCreate(
            display_name="AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
            is_multi=True,
            key="region_d9fe56bc9274fbb6",
            type=CustomAttributeType.NUMBER,
        ),
        type=CustomAttributeConfigResourceType.CUSTOM_ATTRIBUTE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.create_custom_attribute_config(case_type_id=CASE_TYPE_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create custom attribute config for a case type returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new

# there is a valid "case_type" in the system
CASE_TYPE_ID = ENV["CASE_TYPE_ID"]

body = DatadogAPIClient::V2::CustomAttributeConfigCreateRequest.new({
  data: DatadogAPIClient::V2::CustomAttributeConfigCreate.new({
    attributes: DatadogAPIClient::V2::CustomAttributeConfigAttributesCreate.new({
      display_name: "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
      is_multi: true,
      key: "region_d9fe56bc9274fbb6",
      type: DatadogAPIClient::V2::CustomAttributeType::NUMBER,
    }),
    type: DatadogAPIClient::V2::CustomAttributeConfigResourceType::CUSTOM_ATTRIBUTE,
  }),
})
p api_instance.create_custom_attribute_config(CASE_TYPE_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create custom attribute config for a case type returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;
use datadog_api_client::datadogV2::model::CustomAttributeConfigAttributesCreate;
use datadog_api_client::datadogV2::model::CustomAttributeConfigCreate;
use datadog_api_client::datadogV2::model::CustomAttributeConfigCreateRequest;
use datadog_api_client::datadogV2::model::CustomAttributeConfigResourceType;
use datadog_api_client::datadogV2::model::CustomAttributeType;

#[tokio::main]
async fn main() {
    // there is a valid "case_type" in the system
    let case_type_id = std::env::var("CASE_TYPE_ID").unwrap();
    let body = CustomAttributeConfigCreateRequest::new(CustomAttributeConfigCreate::new(
        CustomAttributeConfigAttributesCreate::new(
            "AWS Region ".to_string(),
            true,
            "region_d9fe56bc9274fbb6".to_string(),
            CustomAttributeType::NUMBER,
        ),
        CustomAttributeConfigResourceType::CUSTOM_ATTRIBUTE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api
        .create_custom_attribute_config(case_type_id.clone(), body)
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
 * Create custom attribute config for a case type returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

// there is a valid "case_type" in the system
const CASE_TYPE_ID = process.env.CASE_TYPE_ID as string;

const params: v2.CaseManagementAttributeApiCreateCustomAttributeConfigRequest =
  {
    body: {
      data: {
        attributes: {
          displayName: "AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
          isMulti: true,
          key: "region_d9fe56bc9274fbb6",
          type: "NUMBER",
        },
        type: "custom_attribute",
      },
    },
    caseTypeId: CASE_TYPE_ID,
  };

apiInstance
  .createCustomAttributeConfig(params)
  .then((data: v2.CustomAttributeConfigResponse) => {
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

## Delete custom attributes config{% #delete-custom-attributes-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                   |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id} |

### Overview

Delete custom attribute config

### Arguments

#### Path Parameters

| Name                                  | Type   | Description                  |
| ------------------------------------- | ------ | ---------------------------- |
| case_type_id [*required*]        | string | Case type's UUID             |
| custom_attribute_id [*required*] | string | Case Custom attribute's UUID |

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

{% tab title="401" %}
Unauthorized
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
                  \# Path parametersexport case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"export custom_attribute_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}/custom_attributes/${custom_attribute_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete custom attributes config returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ID = environ["CUSTOM_ATTRIBUTE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    api_instance.delete_custom_attribute_config(
        case_type_id=CASE_TYPE_ID,
        custom_attribute_id=CUSTOM_ATTRIBUTE_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete custom attributes config returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementAttributeAPI.new

# there is a valid "case_type" in the system
CASE_TYPE_ID = ENV["CASE_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ID = ENV["CUSTOM_ATTRIBUTE_ID"]
api_instance.delete_custom_attribute_config(CASE_TYPE_ID, CUSTOM_ATTRIBUTE_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete custom attributes config returns "No Content" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "case_type" in the system
	CaseTypeID := os.Getenv("CASE_TYPE_ID")

	// there is a valid "custom_attribute" in the system
	CustomAttributeID := os.Getenv("CUSTOM_ATTRIBUTE_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementAttributeApi(apiClient)
	r, err := api.DeleteCustomAttributeConfig(ctx, CaseTypeID, CustomAttributeID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementAttributeApi.DeleteCustomAttributeConfig`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete custom attributes config returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementAttributeApi apiInstance = new CaseManagementAttributeApi(defaultClient);

    // there is a valid "case_type" in the system
    String CASE_TYPE_ID = System.getenv("CASE_TYPE_ID");

    // there is a valid "custom_attribute" in the system
    String CUSTOM_ATTRIBUTE_ID = System.getenv("CUSTOM_ATTRIBUTE_ID");

    try {
      apiInstance.deleteCustomAttributeConfig(CASE_TYPE_ID, CUSTOM_ATTRIBUTE_ID);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CaseManagementAttributeApi#deleteCustomAttributeConfig");
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
// Delete custom attributes config returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_attribute::CaseManagementAttributeAPI;

#[tokio::main]
async fn main() {
    // there is a valid "case_type" in the system
    let case_type_id = std::env::var("CASE_TYPE_ID").unwrap();

    // there is a valid "custom_attribute" in the system
    let custom_attribute_id = std::env::var("CUSTOM_ATTRIBUTE_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = CaseManagementAttributeAPI::with_config(configuration);
    let resp = api
        .delete_custom_attribute_config(case_type_id.clone(), custom_attribute_id.clone())
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
 * Delete custom attributes config returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementAttributeApi(configuration);

// there is a valid "case_type" in the system
const CASE_TYPE_ID = process.env.CASE_TYPE_ID as string;

// there is a valid "custom_attribute" in the system
const CUSTOM_ATTRIBUTE_ID = process.env.CUSTOM_ATTRIBUTE_ID as string;

const params: v2.CaseManagementAttributeApiDeleteCustomAttributeConfigRequest =
  {
    caseTypeId: CASE_TYPE_ID,
    customAttributeId: CUSTOM_ATTRIBUTE_ID,
  };

apiInstance
  .deleteCustomAttributeConfig(params)
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
