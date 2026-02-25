# Source: https://docs.datadoghq.com/api/latest/datasets.md

---
title: Datasets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Datasets
---

# Datasets

Data Access Controls in Datadog is a feature that allows administrators and access managers to regulate access to sensitive data. By defining Restricted Datasets, you can ensure that only specific teams or roles can view certain types of telemetry (for example, logs, traces, metrics, and RUM data).

## Create a dataset{% #create-a-dataset %}

{% tab title="v2" %}
**Note: Data Access is in preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**
| Datadog site      | API endpoint                                       |
| ----------------- | -------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/datasets |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/datasets |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/datasets      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/datasets      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/datasets     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/datasets |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/datasets |

### Overview

Create a dataset with the configurations in the request. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.



### Request

#### Body Data (required)

Dataset payload

{% tab title="Model" %}

| Parent field    | Field                             | Type     | Description                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | data [*required*]            | object   | **Datasets Object Constraints**                                                                                                                                                                                                                                                                                                         | **Tag limit per dataset**: | **Tag key rules per telemetry type**: | **Tag value uniqueness**: |
| data            | attributes [*required*]      | object   | Dataset metadata and configurations.                                                                                                                                                                                                                                                                                                    |
| attributes      | name [*required*]            | string   | Name of the dataset.                                                                                                                                                                                                                                                                                                                    |
| attributes      | principals [*required*]      | [string] | List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.                                                                                                                                                                                                                                         |
| attributes      | product_filters [*required*] | [object] | List of product-specific filters.                                                                                                                                                                                                                                                                                                       |
| product_filters | filters [*required*]         | [string] | Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type. |
| product_filters | product [*required*]         | string   | Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.                                                                                                                                                                                                        |
| data            | type [*required*]            | enum     | Resource type, always set to `dataset`. Allowed enum values: `dataset`                                                                                                                                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single dataset object.

| Parent field    | Field                     | Type      | Description                                                                                                                                                                                                                                                                                                                             |
| --------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | data                      | object    | **Datasets Object Constraints**                                                                                                                                                                                                                                                                                                         | **Tag Limit per Dataset**: | **Tag Key Rules per Telemetry Type**: | **Tag Value Uniqueness**: |
| data            | attributes                | object    | Dataset metadata and configuration(s).                                                                                                                                                                                                                                                                                                  |
| attributes      | created_at                | date-time | Timestamp when the dataset was created.                                                                                                                                                                                                                                                                                                 |
| attributes      | created_by                | uuid      | Unique ID of the user who created the dataset.                                                                                                                                                                                                                                                                                          |
| attributes      | name                      | string    | Name of the dataset.                                                                                                                                                                                                                                                                                                                    |
| attributes      | principals                | [string]  | List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.                                                                                                                                                                                                                                         |
| attributes      | product_filters           | [object]  | List of product-specific filters.                                                                                                                                                                                                                                                                                                       |
| product_filters | filters [*required*] | [string]  | Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type. |
| product_filters | product [*required*] | string    | Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.                                                                                                                                                                                                        |
| data            | id                        | string    | Unique identifier for the dataset.                                                                                                                                                                                                                                                                                                      |
| data            | type                      | enum      | Resource type, always set to `dataset`. Allowed enum values: `dataset`                                                                                                                                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "name": "Security Audit Dataset",
      "principals": [
        "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "logs"
        }
      ]
    },
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "type": "dataset"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
EOF

#####

```go
// Create a dataset returns "OK" response

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
    body := datadogV2.DatasetCreateRequest{
        Data: datadogV2.DatasetRequest{
            Attributes: datadogV2.DatasetAttributesRequest{
                Name: "Security Audit Dataset",
                Principals: []string{
                    "role:94172442-be03-11e9-a77a-3b7612558ac1",
                },
                ProductFilters: []datadogV2.FiltersPerProduct{
                    {
                        Filters: []string{
                            "@application.id:ABCD",
                        },
                        Product: "metrics",
                    },
                },
            },
            Type: datadogV2.DATASETTYPE_DATASET,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateDataset", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDatasetsApi(apiClient)
    resp, r, err := api.CreateDataset(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.CreateDataset`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.CreateDataset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a dataset returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetAttributesRequest;
import com.datadog.api.client.v2.model.DatasetCreateRequest;
import com.datadog.api.client.v2.model.DatasetRequest;
import com.datadog.api.client.v2.model.DatasetResponseSingle;
import com.datadog.api.client.v2.model.DatasetType;
import com.datadog.api.client.v2.model.FiltersPerProduct;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    DatasetCreateRequest body =
        new DatasetCreateRequest()
            .data(
                new DatasetRequest()
                    .attributes(
                        new DatasetAttributesRequest()
                            .name("Security Audit Dataset")
                            .principals(
                                Collections.singletonList(
                                    "role:94172442-be03-11e9-a77a-3b7612558ac1"))
                            .productFilters(
                                Collections.singletonList(
                                    new FiltersPerProduct()
                                        .filters(Collections.singletonList("@application.id:ABCD"))
                                        .product("metrics"))))
                    .type(DatasetType.DATASET));

    try {
      DatasetResponseSingle result = apiInstance.createDataset(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#createDataset");
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
Create a dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi
from datadog_api_client.v2.model.dataset_attributes_request import DatasetAttributesRequest
from datadog_api_client.v2.model.dataset_create_request import DatasetCreateRequest
from datadog_api_client.v2.model.dataset_request import DatasetRequest
from datadog_api_client.v2.model.dataset_type import DatasetType
from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

body = DatasetCreateRequest(
    data=DatasetRequest(
        attributes=DatasetAttributesRequest(
            name="Security Audit Dataset",
            principals=[
                "role:94172442-be03-11e9-a77a-3b7612558ac1",
            ],
            product_filters=[
                FiltersPerProduct(
                    filters=[
                        "@application.id:ABCD",
                    ],
                    product="metrics",
                ),
            ],
        ),
        type=DatasetType.DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.create_dataset(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a dataset returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

body = DatadogAPIClient::V2::DatasetCreateRequest.new({
  data: DatadogAPIClient::V2::DatasetRequest.new({
    attributes: DatadogAPIClient::V2::DatasetAttributesRequest.new({
      name: "Security Audit Dataset",
      principals: [
        "role:94172442-be03-11e9-a77a-3b7612558ac1",
      ],
      product_filters: [
        DatadogAPIClient::V2::FiltersPerProduct.new({
          filters: [
            "@application.id:ABCD",
          ],
          product: "metrics",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::DatasetType::DATASET,
  }),
})
p api_instance.create_dataset(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create a dataset returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;
use datadog_api_client::datadogV2::model::DatasetAttributesRequest;
use datadog_api_client::datadogV2::model::DatasetCreateRequest;
use datadog_api_client::datadogV2::model::DatasetRequest;
use datadog_api_client::datadogV2::model::DatasetType;
use datadog_api_client::datadogV2::model::FiltersPerProduct;

#[tokio::main]
async fn main() {
    let body = DatasetCreateRequest::new(DatasetRequest::new(
        DatasetAttributesRequest::new(
            "Security Audit Dataset".to_string(),
            vec!["role:94172442-be03-11e9-a77a-3b7612558ac1".to_string()],
            vec![FiltersPerProduct::new(
                vec!["@application.id:ABCD".to_string()],
                "metrics".to_string(),
            )],
        ),
        DatasetType::DATASET,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.create_dataset(body).await;
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
 * Create a dataset returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

const params: v2.DatasetsApiCreateDatasetRequest = {
  body: {
    data: {
      attributes: {
        name: "Security Audit Dataset",
        principals: ["role:94172442-be03-11e9-a77a-3b7612558ac1"],
        productFilters: [
          {
            filters: ["@application.id:ABCD"],
            product: "metrics",
          },
        ],
      },
      type: "dataset",
    },
  },
};

apiInstance
  .createDataset(params)
  .then((data: v2.DatasetResponseSingle) => {
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

## Get a single dataset by ID{% #get-a-single-dataset-by-id %}

{% tab title="v2" %}
**Note: Data Access is in preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**
| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/datasets/{dataset_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/datasets/{dataset_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/datasets/{dataset_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/datasets/{dataset_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/datasets/{dataset_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/datasets/{dataset_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/datasets/{dataset_id} |

### Overview

Retrieves the dataset associated with the ID.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                  |
| ---------------------------- | ------ | ---------------------------- |
| dataset_id [*required*] | string | The ID of a defined dataset. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single dataset object.

| Parent field    | Field                     | Type      | Description                                                                                                                                                                                                                                                                                                                             |
| --------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | data                      | object    | **Datasets Object Constraints**                                                                                                                                                                                                                                                                                                         | **Tag Limit per Dataset**: | **Tag Key Rules per Telemetry Type**: | **Tag Value Uniqueness**: |
| data            | attributes                | object    | Dataset metadata and configuration(s).                                                                                                                                                                                                                                                                                                  |
| attributes      | created_at                | date-time | Timestamp when the dataset was created.                                                                                                                                                                                                                                                                                                 |
| attributes      | created_by                | uuid      | Unique ID of the user who created the dataset.                                                                                                                                                                                                                                                                                          |
| attributes      | name                      | string    | Name of the dataset.                                                                                                                                                                                                                                                                                                                    |
| attributes      | principals                | [string]  | List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.                                                                                                                                                                                                                                         |
| attributes      | product_filters           | [object]  | List of product-specific filters.                                                                                                                                                                                                                                                                                                       |
| product_filters | filters [*required*] | [string]  | Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type. |
| product_filters | product [*required*] | string    | Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.                                                                                                                                                                                                        |
| data            | id                        | string    | Unique identifier for the dataset.                                                                                                                                                                                                                                                                                                      |
| data            | type                      | enum      | Resource type, always set to `dataset`. Allowed enum values: `dataset`                                                                                                                                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "name": "Security Audit Dataset",
      "principals": [
        "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "logs"
        }
      ]
    },
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "type": "dataset"
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

### Code Example

#####
                  \# Path parametersexport dataset_id="0879ce27-29a1-481f-a12e-bc2a48ec9ae1"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets/${dataset_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a single dataset by ID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.get_dataset(
        dataset_id=DATASET_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a single dataset by ID returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

# there is a valid "dataset" in the system
DATASET_DATA_ID = ENV["DATASET_DATA_ID"]
p api_instance.get_dataset(DATASET_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a single dataset by ID returns "OK" response

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
    // there is a valid "dataset" in the system
    DatasetDataID := os.Getenv("DATASET_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetDataset", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDatasetsApi(apiClient)
    resp, r, err := api.GetDataset(ctx, DatasetDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.GetDataset`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.GetDataset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a single dataset by ID returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetResponseSingle;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    // there is a valid "dataset" in the system
    String DATASET_DATA_ID = System.getenv("DATASET_DATA_ID");

    try {
      DatasetResponseSingle result = apiInstance.getDataset(DATASET_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#getDataset");
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
// Get a single dataset by ID returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dataset" in the system
    let dataset_data_id = std::env::var("DATASET_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.get_dataset(dataset_data_id.clone()).await;
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
 * Get a single dataset by ID returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

// there is a valid "dataset" in the system
const DATASET_DATA_ID = process.env.DATASET_DATA_ID as string;

const params: v2.DatasetsApiGetDatasetRequest = {
  datasetId: DATASET_DATA_ID,
};

apiInstance
  .getDataset(params)
  .then((data: v2.DatasetResponseSingle) => {
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

## Get all datasets{% #get-all-datasets %}

{% tab title="v2" %}
**Note: Data Access is in preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**
| Datadog site      | API endpoint                                      |
| ----------------- | ------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/datasets |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/datasets |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/datasets      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/datasets      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/datasets     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/datasets |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/datasets |

### Overview

Get all datasets that have been configured for an organization. This endpoint requires the `user_access_read` permission.

OAuth apps require the `user_access_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of datasets.

| Parent field    | Field                     | Type      | Description                                                                                                                                                                                                                                                                                                                             |
| --------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | data                      | [object]  | The list of datasets returned in response.                                                                                                                                                                                                                                                                                              |
| data            | attributes                | object    | Dataset metadata and configuration(s).                                                                                                                                                                                                                                                                                                  |
| attributes      | created_at                | date-time | Timestamp when the dataset was created.                                                                                                                                                                                                                                                                                                 |
| attributes      | created_by                | uuid      | Unique ID of the user who created the dataset.                                                                                                                                                                                                                                                                                          |
| attributes      | name                      | string    | Name of the dataset.                                                                                                                                                                                                                                                                                                                    |
| attributes      | principals                | [string]  | List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.                                                                                                                                                                                                                                         |
| attributes      | product_filters           | [object]  | List of product-specific filters.                                                                                                                                                                                                                                                                                                       |
| product_filters | filters [*required*] | [string]  | Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type. |
| product_filters | product [*required*] | string    | Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.                                                                                                                                                                                                        |
| data            | id                        | string    | Unique identifier for the dataset.                                                                                                                                                                                                                                                                                                      |
| data            | type                      | enum      | Resource type, always set to `dataset`. Allowed enum values: `dataset`                                                                                                                                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "created_by": "string",
        "name": "Security Audit Dataset",
        "principals": [
          "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
        ],
        "product_filters": [
          {
            "filters": [
              "@application.id:ABCD"
            ],
            "product": "logs"
          }
        ]
      },
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "type": "dataset"
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all datasets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

configuration = Configuration()
configuration.unstable_operations["get_all_datasets"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.get_all_datasets()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get all datasets returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_all_datasets".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new
p api_instance.get_all_datasets()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get all datasets returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.GetAllDatasets", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDatasetsApi(apiClient)
    resp, r, err := api.GetAllDatasets(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.GetAllDatasets`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.GetAllDatasets`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get all datasets returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetResponseMulti;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getAllDatasets", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    try {
      DatasetResponseMulti result = apiInstance.getAllDatasets();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#getAllDatasets");
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
// Get all datasets returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetAllDatasets", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.get_all_datasets().await;
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
 * Get all datasets returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getAllDatasets"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

apiInstance
  .getAllDatasets()
  .then((data: v2.DatasetResponseMulti) => {
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

## Edit a dataset{% #edit-a-dataset %}

{% tab title="v2" %}
**Note: Data Access is in preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**
| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/datasets/{dataset_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/datasets/{dataset_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/datasets/{dataset_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/datasets/{dataset_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/datasets/{dataset_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/datasets/{dataset_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/datasets/{dataset_id} |

### Overview

Edits the dataset associated with the ID. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                  |
| ---------------------------- | ------ | ---------------------------- |
| dataset_id [*required*] | string | The ID of a defined dataset. |

### Request

#### Body Data (required)

Dataset payload

{% tab title="Model" %}

| Parent field    | Field                             | Type     | Description                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | data [*required*]            | object   | **Datasets Object Constraints**                                                                                                                                                                                                                                                                                                         | **Tag limit per dataset**: | **Tag key rules per telemetry type**: | **Tag value uniqueness**: |
| data            | attributes [*required*]      | object   | Dataset metadata and configurations.                                                                                                                                                                                                                                                                                                    |
| attributes      | name [*required*]            | string   | Name of the dataset.                                                                                                                                                                                                                                                                                                                    |
| attributes      | principals [*required*]      | [string] | List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.                                                                                                                                                                                                                                         |
| attributes      | product_filters [*required*] | [object] | List of product-specific filters.                                                                                                                                                                                                                                                                                                       |
| product_filters | filters [*required*]         | [string] | Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type. |
| product_filters | product [*required*]         | string   | Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.                                                                                                                                                                                                        |
| data            | type [*required*]            | enum     | Resource type, always set to `dataset`. Allowed enum values: `dataset`                                                                                                                                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:1234"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single dataset object.

| Parent field    | Field                     | Type      | Description                                                                                                                                                                                                                                                                                                                             |
| --------------- | ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | data                      | object    | **Datasets Object Constraints**                                                                                                                                                                                                                                                                                                         | **Tag Limit per Dataset**: | **Tag Key Rules per Telemetry Type**: | **Tag Value Uniqueness**: |
| data            | attributes                | object    | Dataset metadata and configuration(s).                                                                                                                                                                                                                                                                                                  |
| attributes      | created_at                | date-time | Timestamp when the dataset was created.                                                                                                                                                                                                                                                                                                 |
| attributes      | created_by                | uuid      | Unique ID of the user who created the dataset.                                                                                                                                                                                                                                                                                          |
| attributes      | name                      | string    | Name of the dataset.                                                                                                                                                                                                                                                                                                                    |
| attributes      | principals                | [string]  | List of access principals, formatted as `principal_type:id`. Principal can be 'team' or 'role'.                                                                                                                                                                                                                                         |
| attributes      | product_filters           | [object]  | List of product-specific filters.                                                                                                                                                                                                                                                                                                       |
| product_filters | filters [*required*] | [string]  | Defines the list of tag-based filters used to restrict access to telemetry data for a specific product. These filters act as access control rules. Each filter must follow the tag query syntax used by Datadog (such as `@tag.key:value`), and only one tag or attribute may be used to define the access strategy per telemetry type. |
| product_filters | product [*required*] | string    | Name of the product the dataset is for. Possible values are 'apm', 'rum', 'metrics', 'logs', 'error_tracking', and 'cloud_cost'.                                                                                                                                                                                                        |
| data            | id                        | string    | Unique identifier for the dataset.                                                                                                                                                                                                                                                                                                      |
| data            | type                      | enum      | Resource type, always set to `dataset`. Allowed enum values: `dataset`                                                                                                                                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "name": "Security Audit Dataset",
      "principals": [
        "role:86245fce-0a4e-11f0-92bd-da7ad0900002"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:ABCD"
          ],
          "product": "logs"
        }
      ]
    },
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "type": "dataset"
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

### Code Example

#####
                          \# Path parametersexport dataset_id="0879ce27-29a1-481f-a12e-bc2a48ec9ae1"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets/${dataset_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Security Audit Dataset",
      "principals": [
        "role:94172442-be03-11e9-a77a-3b7612558ac1"
      ],
      "product_filters": [
        {
          "filters": [
            "@application.id:1234"
          ],
          "product": "metrics"
        }
      ]
    },
    "type": "dataset"
  }
}
EOF

#####

```go
// Edit a dataset returns "OK" response

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
    // there is a valid "dataset" in the system
    DatasetDataID := os.Getenv("DATASET_DATA_ID")

    body := datadogV2.DatasetUpdateRequest{
        Data: datadogV2.DatasetRequest{
            Attributes: datadogV2.DatasetAttributesRequest{
                Name: "Security Audit Dataset",
                Principals: []string{
                    "role:94172442-be03-11e9-a77a-3b7612558ac1",
                },
                ProductFilters: []datadogV2.FiltersPerProduct{
                    {
                        Filters: []string{
                            "@application.id:1234",
                        },
                        Product: "metrics",
                    },
                },
            },
            Type: datadogV2.DATASETTYPE_DATASET,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.UpdateDataset", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDatasetsApi(apiClient)
    resp, r, err := api.UpdateDataset(ctx, DatasetDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.UpdateDataset`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `DatasetsApi.UpdateDataset`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Edit a dataset returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;
import com.datadog.api.client.v2.model.DatasetAttributesRequest;
import com.datadog.api.client.v2.model.DatasetRequest;
import com.datadog.api.client.v2.model.DatasetResponseSingle;
import com.datadog.api.client.v2.model.DatasetType;
import com.datadog.api.client.v2.model.DatasetUpdateRequest;
import com.datadog.api.client.v2.model.FiltersPerProduct;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    // there is a valid "dataset" in the system
    String DATASET_DATA_ID = System.getenv("DATASET_DATA_ID");

    DatasetUpdateRequest body =
        new DatasetUpdateRequest()
            .data(
                new DatasetRequest()
                    .attributes(
                        new DatasetAttributesRequest()
                            .name("Security Audit Dataset")
                            .principals(
                                Collections.singletonList(
                                    "role:94172442-be03-11e9-a77a-3b7612558ac1"))
                            .productFilters(
                                Collections.singletonList(
                                    new FiltersPerProduct()
                                        .filters(Collections.singletonList("@application.id:1234"))
                                        .product("metrics"))))
                    .type(DatasetType.DATASET));

    try {
      DatasetResponseSingle result = apiInstance.updateDataset(DATASET_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#updateDataset");
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
Edit a dataset returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi
from datadog_api_client.v2.model.dataset_attributes_request import DatasetAttributesRequest
from datadog_api_client.v2.model.dataset_request import DatasetRequest
from datadog_api_client.v2.model.dataset_type import DatasetType
from datadog_api_client.v2.model.dataset_update_request import DatasetUpdateRequest
from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

body = DatasetUpdateRequest(
    data=DatasetRequest(
        attributes=DatasetAttributesRequest(
            name="Security Audit Dataset",
            principals=[
                "role:94172442-be03-11e9-a77a-3b7612558ac1",
            ],
            product_filters=[
                FiltersPerProduct(
                    filters=[
                        "@application.id:1234",
                    ],
                    product="metrics",
                ),
            ],
        ),
        type=DatasetType.DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.update_dataset(dataset_id=DATASET_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Edit a dataset returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

# there is a valid "dataset" in the system
DATASET_DATA_ID = ENV["DATASET_DATA_ID"]

body = DatadogAPIClient::V2::DatasetUpdateRequest.new({
  data: DatadogAPIClient::V2::DatasetRequest.new({
    attributes: DatadogAPIClient::V2::DatasetAttributesRequest.new({
      name: "Security Audit Dataset",
      principals: [
        "role:94172442-be03-11e9-a77a-3b7612558ac1",
      ],
      product_filters: [
        DatadogAPIClient::V2::FiltersPerProduct.new({
          filters: [
            "@application.id:1234",
          ],
          product: "metrics",
        }),
      ],
    }),
    type: DatadogAPIClient::V2::DatasetType::DATASET,
  }),
})
p api_instance.update_dataset(DATASET_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Edit a dataset returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;
use datadog_api_client::datadogV2::model::DatasetAttributesRequest;
use datadog_api_client::datadogV2::model::DatasetRequest;
use datadog_api_client::datadogV2::model::DatasetType;
use datadog_api_client::datadogV2::model::DatasetUpdateRequest;
use datadog_api_client::datadogV2::model::FiltersPerProduct;

#[tokio::main]
async fn main() {
    // there is a valid "dataset" in the system
    let dataset_data_id = std::env::var("DATASET_DATA_ID").unwrap();
    let body = DatasetUpdateRequest::new(DatasetRequest::new(
        DatasetAttributesRequest::new(
            "Security Audit Dataset".to_string(),
            vec!["role:94172442-be03-11e9-a77a-3b7612558ac1".to_string()],
            vec![FiltersPerProduct::new(
                vec!["@application.id:1234".to_string()],
                "metrics".to_string(),
            )],
        ),
        DatasetType::DATASET,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.update_dataset(dataset_data_id.clone(), body).await;
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
 * Edit a dataset returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

// there is a valid "dataset" in the system
const DATASET_DATA_ID = process.env.DATASET_DATA_ID as string;

const params: v2.DatasetsApiUpdateDatasetRequest = {
  body: {
    data: {
      attributes: {
        name: "Security Audit Dataset",
        principals: ["role:94172442-be03-11e9-a77a-3b7612558ac1"],
        productFilters: [
          {
            filters: ["@application.id:1234"],
            product: "metrics",
          },
        ],
      },
      type: "dataset",
    },
  },
  datasetId: DATASET_DATA_ID,
};

apiInstance
  .updateDataset(params)
  .then((data: v2.DatasetResponseSingle) => {
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

## Delete a dataset{% #delete-a-dataset %}

{% tab title="v2" %}
**Note: Data Access is in preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**
| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/datasets/{dataset_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/datasets/{dataset_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/datasets/{dataset_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/datasets/{dataset_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/datasets/{dataset_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/datasets/{dataset_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/datasets/{dataset_id} |

### Overview

Deletes the dataset associated with the ID. This endpoint requires the `user_access_manage` permission.

OAuth apps require the `user_access_manage` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#datasets) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                  |
| ---------------------------- | ------ | ---------------------------- |
| dataset_id [*required*] | string | The ID of a defined dataset. |

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

### Code Example

#####
                  \# Path parametersexport dataset_id="0879ce27-29a1-481f-a12e-bc2a48ec9ae1"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/datasets/${dataset_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a dataset returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    api_instance.delete_dataset(
        dataset_id=DATASET_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete a dataset returns "No Content" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_dataset".to_sym] = true
end
api_instance = DatadogAPIClient::V2::DatasetsAPI.new

# there is a valid "dataset" in the system
DATASET_DATA_ID = ENV["DATASET_DATA_ID"]
api_instance.delete_dataset(DATASET_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete a dataset returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "dataset" in the system
    DatasetDataID := os.Getenv("DATASET_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.DeleteDataset", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewDatasetsApi(apiClient)
    r, err := api.DeleteDataset(ctx, DatasetDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DatasetsApi.DeleteDataset`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete a dataset returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteDataset", true);
    DatasetsApi apiInstance = new DatasetsApi(defaultClient);

    // there is a valid "dataset" in the system
    String DATASET_DATA_ID = System.getenv("DATASET_DATA_ID");

    try {
      apiInstance.deleteDataset(DATASET_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#deleteDataset");
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
// Delete a dataset returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_datasets::DatasetsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dataset" in the system
    let dataset_data_id = std::env::var("DATASET_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteDataset", true);
    let api = DatasetsAPI::with_config(configuration);
    let resp = api.delete_dataset(dataset_data_id.clone()).await;
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
 * Delete a dataset returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteDataset"] = true;
const apiInstance = new v2.DatasetsApi(configuration);

// there is a valid "dataset" in the system
const DATASET_DATA_ID = process.env.DATASET_DATA_ID as string;

const params: v2.DatasetsApiDeleteDatasetRequest = {
  datasetId: DATASET_DATA_ID,
};

apiInstance
  .deleteDataset(params)
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
