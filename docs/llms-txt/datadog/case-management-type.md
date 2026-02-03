# Source: https://docs.datadoghq.com/api/latest/case-management-type.md

---
title: Case Management Type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Case Management Type
---

# Case Management Type

View and configure case types within Case Management. See the [Case Management page](https://docs.datadoghq.com/service_management/case_management/) for more information.

## Get all case types{% #get-all-case-types %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cases/types |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cases/types |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cases/types      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cases/types      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cases/types     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cases/types |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cases/types |

### Overview

Get all case types

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Case types response.

| Parent field | Field                  | Type      | Description                                              |
| ------------ | ---------------------- | --------- | -------------------------------------------------------- |
|              | data                   | [object]  | List of case types                                       |
| data         | attributes             | object    | Case Type resource attributes                            |
| attributes   | deleted_at             | date-time | Timestamp of when the case type was deleted              |
| attributes   | description            | string    | Case type description.                                   |
| attributes   | emoji                  | string    | Case type emoji.                                         |
| attributes   | name [*required*] | string    | Case type name.                                          |
| data         | id                     | string    | Case type's identifier                                   |
| data         | type                   | enum      | Case type resource type Allowed enum values: `case_type` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "deleted_at": "2019-09-19T10:00:00.000Z",
        "description": "Investigations done in case management",
        "emoji": "ðµð»ââï¸",
        "name": "Investigation"
      },
      "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
      "type": "case_type"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all case types returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    response = api_instance.get_all_case_types()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all case types returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementTypeAPI.new
p api_instance.get_all_case_types()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all case types returns "OK" response

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
	api := datadogV2.NewCaseManagementTypeApi(apiClient)
	resp, r, err := api.GetAllCaseTypes(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementTypeApi.GetAllCaseTypes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementTypeApi.GetAllCaseTypes`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all case types returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementTypeApi;
import com.datadog.api.client.v2.model.CaseTypesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementTypeApi apiInstance = new CaseManagementTypeApi(defaultClient);

    try {
      CaseTypesResponse result = apiInstance.getAllCaseTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementTypeApi#getAllCaseTypes");
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
// Get all case types returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_type::CaseManagementTypeAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementTypeAPI::with_config(configuration);
    let resp = api.get_all_case_types().await;
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
 * Get all case types returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementTypeApi(configuration);

apiInstance
  .getAllCaseTypes()
  .then((data: v2.CaseTypesResponse) => {
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

## Create a case type{% #create-a-case-type %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/cases/types |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/cases/types |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/cases/types      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/cases/types      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/cases/types     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/cases/types |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/cases/types |

### Overview

Create a Case Type

### Request

#### Body Data (required)

Case type payload

{% tab title="Model" %}

| Parent field | Field                        | Type      | Description                                              |
| ------------ | ---------------------------- | --------- | -------------------------------------------------------- |
|              | data [*required*]       | object    | Case type                                                |
| data         | attributes [*required*] | object    | Case Type resource attributes                            |
| attributes   | deleted_at                   | date-time | Timestamp of when the case type was deleted              |
| attributes   | description                  | string    | Case type description.                                   |
| attributes   | emoji                        | string    | Case type emoji.                                         |
| attributes   | name [*required*]       | string    | Case type name.                                          |
| data         | type [*required*]       | enum      | Case type resource type Allowed enum values: `case_type` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Investigations done in case management",
      "emoji": "\ud83d\udc51",
      "name": "Investigation"
    },
    "type": "case_type"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Case type response

| Parent field | Field                  | Type      | Description                                              |
| ------------ | ---------------------- | --------- | -------------------------------------------------------- |
|              | data                   | object    | The definition of `CaseType` object.                     |
| data         | attributes             | object    | Case Type resource attributes                            |
| attributes   | deleted_at             | date-time | Timestamp of when the case type was deleted              |
| attributes   | description            | string    | Case type description.                                   |
| attributes   | emoji                  | string    | Case type emoji.                                         |
| attributes   | name [*required*] | string    | Case type name.                                          |
| data         | id                     | string    | Case type's identifier                                   |
| data         | type                   | enum      | Case type resource type Allowed enum values: `case_type` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "deleted_at": "2019-09-19T10:00:00.000Z",
      "description": "Investigations done in case management",
      "emoji": "ðµð»ââï¸",
      "name": "Investigation"
    },
    "id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001",
    "type": "case_type"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Investigations done in case management",
      "emoji": "\ud83d\udc51",
      "name": "Investigation"
    },
    "type": "case_type"
  }
}
EOF
                        
##### 

```go
// Create a case type returns "CREATED" response

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
	body := datadogV2.CaseTypeCreateRequest{
		Data: datadogV2.CaseTypeCreate{
			Attributes: datadogV2.CaseTypeResourceAttributes{
				Description: datadog.PtrString("Investigations done in case management"),
				Emoji:       datadog.PtrString("ð"),
				Name:        "Investigation",
			},
			Type: datadogV2.CASETYPERESOURCETYPE_CASE_TYPE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCaseManagementTypeApi(apiClient)
	resp, r, err := api.CreateCaseType(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementTypeApi.CreateCaseType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CaseManagementTypeApi.CreateCaseType`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create a case type returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementTypeApi;
import com.datadog.api.client.v2.model.CaseTypeCreate;
import com.datadog.api.client.v2.model.CaseTypeCreateRequest;
import com.datadog.api.client.v2.model.CaseTypeResourceAttributes;
import com.datadog.api.client.v2.model.CaseTypeResourceType;
import com.datadog.api.client.v2.model.CaseTypeResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementTypeApi apiInstance = new CaseManagementTypeApi(defaultClient);

    CaseTypeCreateRequest body =
        new CaseTypeCreateRequest()
            .data(
                new CaseTypeCreate()
                    .attributes(
                        new CaseTypeResourceAttributes()
                            .description("Investigations done in case management")
                            .emoji("ð")
                            .name("Investigation"))
                    .type(CaseTypeResourceType.CASE_TYPE));

    try {
      CaseTypeResponse result = apiInstance.createCaseType(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementTypeApi#createCaseType");
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
Create a case type returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi
from datadog_api_client.v2.model.case_type_create import CaseTypeCreate
from datadog_api_client.v2.model.case_type_create_request import CaseTypeCreateRequest
from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType

body = CaseTypeCreateRequest(
    data=CaseTypeCreate(
        attributes=CaseTypeResourceAttributes(
            description="Investigations done in case management",
            emoji="ð",
            name="Investigation",
        ),
        type=CaseTypeResourceType.CASE_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    response = api_instance.create_case_type(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create a case type returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementTypeAPI.new

body = DatadogAPIClient::V2::CaseTypeCreateRequest.new({
  data: DatadogAPIClient::V2::CaseTypeCreate.new({
    attributes: DatadogAPIClient::V2::CaseTypeResourceAttributes.new({
      description: "Investigations done in case management",
      emoji: "ð",
      name: "Investigation",
    }),
    type: DatadogAPIClient::V2::CaseTypeResourceType::CASE_TYPE,
  }),
})
p api_instance.create_case_type(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create a case type returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_type::CaseManagementTypeAPI;
use datadog_api_client::datadogV2::model::CaseTypeCreate;
use datadog_api_client::datadogV2::model::CaseTypeCreateRequest;
use datadog_api_client::datadogV2::model::CaseTypeResourceAttributes;
use datadog_api_client::datadogV2::model::CaseTypeResourceType;

#[tokio::main]
async fn main() {
    let body = CaseTypeCreateRequest::new(CaseTypeCreate::new(
        CaseTypeResourceAttributes::new("Investigation".to_string())
            .description("Investigations done in case management".to_string())
            .emoji("ð".to_string()),
        CaseTypeResourceType::CASE_TYPE,
    ));
    let configuration = datadog::Configuration::new();
    let api = CaseManagementTypeAPI::with_config(configuration);
    let resp = api.create_case_type(body).await;
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
 * Create a case type returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementTypeApi(configuration);

const params: v2.CaseManagementTypeApiCreateCaseTypeRequest = {
  body: {
    data: {
      attributes: {
        description: "Investigations done in case management",
        emoji: "ð",
        name: "Investigation",
      },
      type: "case_type",
    },
  },
};

apiInstance
  .createCaseType(params)
  .then((data: v2.CaseTypeResponse) => {
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

## Delete a case type{% #delete-a-case-type %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/cases/types/{case_type_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/cases/types/{case_type_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/cases/types/{case_type_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/cases/types/{case_type_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/cases/types/{case_type_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/cases/types/{case_type_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/cases/types/{case_type_id} |

### Overview

Delete a case type

### Arguments

#### Path Parameters

| Name                           | Type   | Description      |
| ------------------------------ | ------ | ---------------- |
| case_type_id [*required*] | string | Case type's UUID |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport case_type_id="f98a5a5b-e0ff-45d4-b2f5-afe6e74de505"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cases/types/${case_type_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a case type returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    api_instance.delete_case_type(
        case_type_id="case_type_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete a case type returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CaseManagementTypeAPI.new
api_instance.delete_case_type("case_type_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete a case type returns "No Content" response

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
	api := datadogV2.NewCaseManagementTypeApi(apiClient)
	r, err := api.DeleteCaseType(ctx, "case_type_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CaseManagementTypeApi.DeleteCaseType`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete a case type returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CaseManagementTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CaseManagementTypeApi apiInstance = new CaseManagementTypeApi(defaultClient);

    try {
      apiInstance.deleteCaseType("f98a5a5b-e0ff-45d4-b2f5-afe6e74de505");
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseManagementTypeApi#deleteCaseType");
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
// Delete a case type returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_case_management_type::CaseManagementTypeAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CaseManagementTypeAPI::with_config(configuration);
    let resp = api.delete_case_type("case_type_id".to_string()).await;
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
 * Delete a case type returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CaseManagementTypeApi(configuration);

const params: v2.CaseManagementTypeApiDeleteCaseTypeRequest = {
  caseTypeId: "case_type_id",
};

apiInstance
  .deleteCaseType(params)
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
