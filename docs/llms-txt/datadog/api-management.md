# Source: https://docs.datadoghq.com/cloudcraft/components-azure/api-management.md

# Source: https://docs.datadoghq.com/api/latest/api-management.md

---
title: API Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > API Management
---

# API Management

Configure your API endpoints through the Datadog API.

## Create a new API{% #create-a-new-api %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/apicatalog/openapi |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/apicatalog/openapi |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/apicatalog/openapi      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/apicatalog/openapi      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/apicatalog/openapi     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/apicatalog/openapi |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/apicatalog/openapi |

### Overview

Create a new API from the [OpenAPI](https://spec.openapis.org/oas/latest.html) specification given. See the [API Catalog documentation](https://docs.datadoghq.com/api_catalog/add_metadata/) for additional information about the possible metadata. It returns the created API ID. This endpoint requires the `apm_api_catalog_write` permission.

OAuth apps require the `apm_api_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Field             | Type   | Description                |
| ----------------- | ------ | -------------------------- |
| openapi_spec_file | binary | Binary `OpenAPI` spec file |

{% /tab %}

{% tab title="Example" %}

```json
{
  "openapi_spec_file": "string"
}
```

{% /tab %}

### Response

{% tab title="201" %}
API created successfully
{% tab title="Model" %}
Response for `CreateOpenAPI` operation.

| Parent field     | Field            | Type     | Description                                 |
| ---------------- | ---------------- | -------- | ------------------------------------------- |
|                  | data             | object   | Data envelope for `CreateOpenAPIResponse`.  |
| data             | attributes       | object   | Attributes for `CreateOpenAPI`.             |
| attributes       | failed_endpoints | [object] | List of endpoints which couldn't be parsed. |
| failed_endpoints | method           | string   | The endpoint method.                        |
| failed_endpoints | path             | string   | The endpoint path.                          |
| data             | id               | uuid     | API identifier.                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "failed_endpoints": [
        {
          "method": "string",
          "path": "string"
        }
      ]
    },
    "id": "90646597-5fdb-4a17-a240-647003f8c028"
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

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/openapi" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F openapi_spec_file=@string
                
##### 

```python
"""
Create a new API returns "API created successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

configuration = Configuration()
configuration.unstable_operations["create_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.create_open_api(
        openapi_spec_file=open("openapi-spec.yaml", "rb"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create a new API returns "API created successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new
opts = {
  openapi_spec_file: File.open("openapi-spec.yaml", "r"),
}
p api_instance.create_open_api(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create a new API returns "API created successfully" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.CreateOpenAPI(ctx, *datadogV2.NewCreateOpenAPIOptionalParameters().WithOpenapiSpecFile(func() io.Reader { fp, _ := os.Open("openapi-spec.yaml"); return fp }()))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.CreateOpenAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.CreateOpenAPI`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create a new API returns "API created successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import com.datadog.api.client.v2.api.ApiManagementApi.CreateOpenAPIOptionalParameters;
import com.datadog.api.client.v2.model.CreateOpenAPIResponse;
import java.io.File;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    try {
      CreateOpenAPIResponse result =
          apiInstance.createOpenAPI(
              new CreateOpenAPIOptionalParameters().openapiSpecFile(new File("openapi-spec.yaml")));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#createOpenAPI");
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
// Create a new API returns "API created successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;
use datadog_api_client::datadogV2::api_api_management::CreateOpenAPIOptionalParams;
use std::fs;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api
        .create_open_api(
            CreateOpenAPIOptionalParams::default()
                .openapi_spec_file(fs::read("openapi-spec.yaml").unwrap()),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Create a new API returns "API created successfully" response
 */

import * as fs from "fs";
import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

const params: v2.APIManagementApiCreateOpenAPIRequest = {
  openapiSpecFile: {
    data: Buffer.from(fs.readFileSync("openapi-spec.yaml", "utf8")),
    name: "openapi-spec.yaml",
  },
};

apiInstance
  .createOpenAPI(params)
  .then((data: v2.CreateOpenAPIResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Update an API{% #update-an-api %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/apicatalog/api/{id}/openapi      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/apicatalog/api/{id}/openapi      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/apicatalog/api/{id}/openapi     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |

### Overview

Update information about a specific API. The given content will replace all API content of the given ID. The ID is returned by the create API, or can be found in the URL in the API catalog UI. This endpoint requires the `apm_api_catalog_write` permission.

OAuth apps require the `apm_api_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                 | Type   | Description             |
| -------------------- | ------ | ----------------------- |
| id [*required*] | string | ID of the API to modify |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Field             | Type   | Description                |
| ----------------- | ------ | -------------------------- |
| openapi_spec_file | binary | Binary `OpenAPI` spec file |

{% /tab %}

{% tab title="Example" %}

```json
{
  "openapi_spec_file": "string"
}
```

{% /tab %}

### Response

{% tab title="200" %}
API updated successfully
{% tab title="Model" %}
Response for `UpdateOpenAPI`.

| Parent field     | Field            | Type     | Description                                 |
| ---------------- | ---------------- | -------- | ------------------------------------------- |
|                  | data             | object   | Data envelope for `UpdateOpenAPIResponse`.  |
| data             | attributes       | object   | Attributes for `UpdateOpenAPI`.             |
| attributes       | failed_endpoints | [object] | List of endpoints which couldn't be parsed. |
| failed_endpoints | method           | string   | The endpoint method.                        |
| failed_endpoints | path             | string   | The endpoint path.                          |
| data             | id               | uuid     | API identifier.                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "failed_endpoints": [
        {
          "method": "string",
          "path": "string"
        }
      ]
    },
    "id": "90646597-5fdb-4a17-a240-647003f8c028"
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

{% tab title="403" %}
Forbidden
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
API not found error
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
                  \# Path parametersexport id="90646597-5fdb-4a17-a240-647003f8c028"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api/${id}/openapi" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F openapi_spec_file=@string
                
##### 

```python
"""
Update an API returns "API updated successfully" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = environ["MANAGED_API_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["update_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.update_open_api(
        id=MANAGED_API_DATA_ID,
        openapi_spec_file=open("openapi-spec.yaml", "rb"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update an API returns "API updated successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = ENV["MANAGED_API_DATA_ID"]
opts = {
  openapi_spec_file: File.open("openapi-spec.yaml", "r"),
}
p api_instance.update_open_api(MANAGED_API_DATA_ID, opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Update an API returns "API updated successfully" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "managed_api" in the system
	ManagedAPIDataID := uuid.MustParse(os.Getenv("MANAGED_API_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.UpdateOpenAPI(ctx, ManagedAPIDataID, *datadogV2.NewUpdateOpenAPIOptionalParameters().WithOpenapiSpecFile(func() io.Reader { fp, _ := os.Open("openapi-spec.yaml"); return fp }()))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.UpdateOpenAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.UpdateOpenAPI`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update an API returns "API updated successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import com.datadog.api.client.v2.api.ApiManagementApi.UpdateOpenAPIOptionalParameters;
import com.datadog.api.client.v2.model.UpdateOpenAPIResponse;
import java.io.File;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    // there is a valid "managed_api" in the system
    UUID MANAGED_API_DATA_ID = null;
    try {
      MANAGED_API_DATA_ID = UUID.fromString(System.getenv("MANAGED_API_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      UpdateOpenAPIResponse result =
          apiInstance.updateOpenAPI(
              MANAGED_API_DATA_ID,
              new UpdateOpenAPIOptionalParameters().openapiSpecFile(new File("openapi-spec.yaml")));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#updateOpenAPI");
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
// Update an API returns "API updated successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;
use datadog_api_client::datadogV2::api_api_management::UpdateOpenAPIOptionalParams;
use std::fs;

#[tokio::main]
async fn main() {
    // there is a valid "managed_api" in the system
    let managed_api_data_id = uuid::Uuid::parse_str(&std::env::var("MANAGED_API_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api
        .update_open_api(
            managed_api_data_id.clone(),
            UpdateOpenAPIOptionalParams::default()
                .openapi_spec_file(fs::read("openapi-spec.yaml").unwrap()),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Update an API returns "API updated successfully" response
 */

import * as fs from "fs";
import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

// there is a valid "managed_api" in the system
const MANAGED_API_DATA_ID = process.env.MANAGED_API_DATA_ID as string;

const params: v2.APIManagementApiUpdateOpenAPIRequest = {
  id: MANAGED_API_DATA_ID,
  openapiSpecFile: {
    data: Buffer.from(fs.readFileSync("openapi-spec.yaml", "utf8")),
    name: "openapi-spec.yaml",
  },
};

apiInstance
  .updateOpenAPI(params)
  .then((data: v2.UpdateOpenAPIResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Get an API{% #get-an-api %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/apicatalog/api/{id}/openapi      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/apicatalog/api/{id}/openapi      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/apicatalog/api/{id}/openapi     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/apicatalog/api/{id}/openapi |

### Overview

Retrieve information about a specific API in [OpenAPI](https://spec.openapis.org/oas/latest.html) format file. This endpoint requires the `apm_api_catalog_read` permission.

OAuth apps require the `apm_api_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                 | Type   | Description               |
| -------------------- | ------ | ------------------------- |
| id [*required*] | string | ID of the API to retrieve |

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

{% tab title="403" %}
Forbidden
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
API not found error
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
                  \# Path parametersexport id="90646597-5fdb-4a17-a240-647003f8c028"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api/${id}/openapi" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get an API returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = environ["MANAGED_API_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.get_open_api(
        id=MANAGED_API_DATA_ID,
    )

    print(response.read())
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get an API returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = ENV["MANAGED_API_DATA_ID"]
p api_instance.get_open_api(MANAGED_API_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get an API returns "OK" response

package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "managed_api" in the system
	ManagedAPIDataID := uuid.MustParse(os.Getenv("MANAGED_API_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.GetOpenAPI(ctx, ManagedAPIDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.GetOpenAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := ioutil.ReadAll(resp)
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.GetOpenAPI`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get an API returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import java.io.File;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    // there is a valid "managed_api" in the system
    UUID MANAGED_API_DATA_ID = null;
    try {
      MANAGED_API_DATA_ID = UUID.fromString(System.getenv("MANAGED_API_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      File result = apiInstance.getOpenAPI(MANAGED_API_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#getOpenAPI");
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
// Get an API returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "managed_api" in the system
    let managed_api_data_id = uuid::Uuid::parse_str(&std::env::var("MANAGED_API_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api.get_open_api(managed_api_data_id.clone()).await;
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
 * Get an API returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

// there is a valid "managed_api" in the system
const MANAGED_API_DATA_ID = process.env.MANAGED_API_DATA_ID as string;

const params: v2.APIManagementApiGetOpenAPIRequest = {
  id: MANAGED_API_DATA_ID,
};

apiInstance
  .getOpenAPI(params)
  .then((data: client.HttpFile) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## List APIs{% #list-apis %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/apicatalog/api |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/apicatalog/api |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/apicatalog/api      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/apicatalog/api      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/apicatalog/api     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/apicatalog/api |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/apicatalog/api |

### Overview

List APIs and their IDs. This endpoint requires the `apm_api_catalog_read` permission.

OAuth apps require the `apm_api_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description               |
| ------------ | ------- | ------------------------- |
| query        | string  | Filter APIs by name       |
| page[limit]  | integer | Number of items per page. |
| page[offset] | integer | Offset for pagination.    |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for `ListAPIs`.

| Parent field | Field       | Type     | Description                                             |
| ------------ | ----------- | -------- | ------------------------------------------------------- |
|              | data        | [object] | List of API items.                                      |
| data         | attributes  | object   | Attributes for `ListAPIsResponseData`.                  |
| attributes   | name        | string   | API name.                                               |
| data         | id          | uuid     | API identifier.                                         |
|              | meta        | object   | Metadata for `ListAPIsResponse`.                        |
| meta         | pagination  | object   | Pagination metadata information for `ListAPIsResponse`. |
| pagination   | limit       | int64    | Number of items in the current page.                    |
| pagination   | offset      | int64    | Offset for pagination.                                  |
| pagination   | total_count | int64    | Total number of items.                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "name": "Payments API"
      },
      "id": "90646597-5fdb-4a17-a240-647003f8c028"
    }
  ],
  "meta": {
    "pagination": {
      "limit": 20,
      "offset": 0,
      "total_count": 35
    }
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

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List APIs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

configuration = Configuration()
configuration.unstable_operations["list_apis"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.list_apis()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List APIs returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_apis".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new
p api_instance.list_apis()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List APIs returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListAPIs", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	resp, r, err := api.ListAPIs(ctx, *datadogV2.NewListAPIsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.ListAPIs`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APIManagementApi.ListAPIs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List APIs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import com.datadog.api.client.v2.model.ListAPIsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listAPIs", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    try {
      ListAPIsResponse result = apiInstance.listAPIs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#listAPIs");
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
// List APIs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;
use datadog_api_client::datadogV2::api_api_management::ListAPIsOptionalParams;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListAPIs", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api.list_apis(ListAPIsOptionalParams::default()).await;
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
 * List APIs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listAPIs"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

apiInstance
  .listAPIs()
  .then((data: v2.ListAPIsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Delete an API{% #delete-an-api %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/apicatalog/api/{id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/apicatalog/api/{id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/apicatalog/api/{id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/apicatalog/api/{id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/apicatalog/api/{id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/apicatalog/api/{id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/apicatalog/api/{id} |

### Overview

Delete a specific API by ID. This endpoint requires the `apm_api_catalog_write` permission.

OAuth apps require the `apm_api_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#api-management) to access this endpoint.



### Arguments

#### Path Parameters

| Name                 | Type   | Description             |
| -------------------- | ------ | ----------------------- |
| id [*required*] | string | ID of the API to delete |

### Response

{% tab title="204" %}
API deleted successfully
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

{% tab title="403" %}
Forbidden
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
API not found error
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
                  \# Path parametersexport id="90646597-5fdb-4a17-a240-647003f8c028"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apicatalog/api/${id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete an API returns "API deleted successfully" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = environ["MANAGED_API_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    api_instance.delete_open_api(
        id=MANAGED_API_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete an API returns "API deleted successfully" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_open_api".to_sym] = true
end
api_instance = DatadogAPIClient::V2::APIManagementAPI.new

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = ENV["MANAGED_API_DATA_ID"]
api_instance.delete_open_api(MANAGED_API_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete an API returns "API deleted successfully" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
	"github.com/google/uuid"
)

func main() {
	// there is a valid "managed_api" in the system
	ManagedAPIDataID := uuid.MustParse(os.Getenv("MANAGED_API_DATA_ID"))

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.DeleteOpenAPI", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewAPIManagementApi(apiClient)
	r, err := api.DeleteOpenAPI(ctx, ManagedAPIDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIManagementApi.DeleteOpenAPI`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete an API returns "API deleted successfully" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApiManagementApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteOpenAPI", true);
    ApiManagementApi apiInstance = new ApiManagementApi(defaultClient);

    // there is a valid "managed_api" in the system
    UUID MANAGED_API_DATA_ID = null;
    try {
      MANAGED_API_DATA_ID = UUID.fromString(System.getenv("MANAGED_API_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      apiInstance.deleteOpenAPI(MANAGED_API_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementApi#deleteOpenAPI");
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
// Delete an API returns "API deleted successfully" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_api_management::APIManagementAPI;

#[tokio::main]
async fn main() {
    // there is a valid "managed_api" in the system
    let managed_api_data_id = uuid::Uuid::parse_str(&std::env::var("MANAGED_API_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteOpenAPI", true);
    let api = APIManagementAPI::with_config(configuration);
    let resp = api.delete_open_api(managed_api_data_id.clone()).await;
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
 * Delete an API returns "API deleted successfully" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteOpenAPI"] = true;
const apiInstance = new v2.APIManagementApi(configuration);

// there is a valid "managed_api" in the system
const MANAGED_API_DATA_ID = process.env.MANAGED_API_DATA_ID as string;

const params: v2.APIManagementApiDeleteOpenAPIRequest = {
  id: MANAGED_API_DATA_ID,
};

apiInstance
  .deleteOpenAPI(params)
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