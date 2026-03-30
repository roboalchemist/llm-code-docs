# Source: https://docs.datadoghq.com/api/latest/oci-integration.md

---
title: OCI Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > OCI Integration
---

# OCI Integration

Auto-generated tag OCI Integration

## List tenancy products{% #list-tenancy-products %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/oci/products |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/oci/products |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/oci/products      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/oci/products      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/oci/products     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/oci/products |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/oci/products |

### Overview

Lists the products for a given tenancy. Returns the enabled/disabled status of Datadog products (such as Cloud Security Posture Management) for specific OCI tenancies.

### Arguments

#### Query Strings

| Name                          | Type   | Description                                        |
| ----------------------------- | ------ | -------------------------------------------------- |
| productKeys [*required*] | string | Comma-separated list of product keys to filter by. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                   |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------------- |
|              | data [*required*] | [object] |
| data         | attributes             | object   |
| attributes   | products               | [object] |
| products     | enabled                | boolean  |
| products     | product_key            | string   |
| data         | id                     | string   |
| data         | type [*required*] | enum     | OCI tenancy product resource type. Allowed enum values: `oci_tenancy_product` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "products": [
          {
            "enabled": true,
            "product_key": "CLOUD_SECURITY_POSTURE_MANAGEMENT"
          }
        ]
      },
      "id": "ocid.tenancy.test",
      "type": "oci_tenancy_product"
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
                  \# Required query argumentsexport productKeys="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/oci/products?productKeys=${productKeys}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List tenancy products returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.list_tenancy_products(
        product_keys="productKeys",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List tenancy products returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OCIIntegrationAPI.new
p api_instance.list_tenancy_products("productKeys")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List tenancy products returns "OK" response

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
    api := datadogV2.NewOCIIntegrationApi(apiClient)
    resp, r, err := api.ListTenancyProducts(ctx, "productKeys")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OCIIntegrationApi.ListTenancyProducts`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OCIIntegrationApi.ListTenancyProducts`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List tenancy products returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OciIntegrationApi;
import com.datadog.api.client.v2.model.TenancyProductsList;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OciIntegrationApi apiInstance = new OciIntegrationApi(defaultClient);

    try {
      TenancyProductsList result = apiInstance.listTenancyProducts("productKeys");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OciIntegrationApi#listTenancyProducts");
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
// List tenancy products returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_oci_integration::OCIIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OCIIntegrationAPI::with_config(configuration);
    let resp = api.list_tenancy_products("productKeys".to_string()).await;
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
 * List tenancy products returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OCIIntegrationApi(configuration);

const params: v2.OCIIntegrationApiListTenancyProductsRequest = {
  productKeys: "productKeys",
};

apiInstance
  .listTenancyProducts(params)
  .then((data: v2.TenancyProductsList) => {
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

## Get tenancy configs{% #get-tenancy-configs %}

{% tab title="v2" %}
**Note**: This endpoint may be subject to changes.
| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/oci/tenancies |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/oci/tenancies |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/oci/tenancies      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/oci/tenancies      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/oci/tenancies     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/oci/tenancies |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies |

### Overview

Get a list of all configured OCI tenancy integrations. Returns basic information about each tenancy including authentication credentials, region settings, and collection preferences for metrics, logs, and resources.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field   | Field                       | Type     | Description                                                   |
| -------------- | --------------------------- | -------- | ------------------------------------------------------------- |
|                | data [*required*]      | [object] |
| data           | attributes                  | object   |
| attributes     | billing_plan_id             | int32    |
| attributes     | config_version              | int64    |
| attributes     | cost_collection_enabled     | boolean  |
| attributes     | dd_compartment_id           | string   |
| attributes     | dd_stack_id                 | string   |
| attributes     | home_region                 | string   |
| attributes     | logs_config                 | object   |
| logs_config    | compartment_tag_filters     | [string] |
| logs_config    | enabled                     | boolean  |
| logs_config    | enabled_services            | [string] |
| attributes     | metrics_config              | object   |
| metrics_config | compartment_tag_filters     | [string] |
| metrics_config | enabled                     | boolean  |
| metrics_config | excluded_services           | [string] |
| attributes     | parent_tenancy_name         | string   |
| attributes     | regions_config              | object   |
| regions_config | available                   | [string] |
| regions_config | disabled                    | [string] |
| regions_config | enabled                     | [string] |
| attributes     | resource_collection_enabled | boolean  |
| attributes     | tenancy_name                | string   |
| attributes     | user_ocid                   | string   |
| data           | id                          | string   |
| data           | type [*required*]      | enum     | OCI tenancy resource type. Allowed enum values: `oci_tenancy` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "config_version": 2,
        "cost_collection_enabled": true,
        "dd_compartment_id": "ocid.compartment.test",
        "dd_stack_id": "ocid.stack.test",
        "home_region": "us-ashburn-1",
        "logs_config": {
          "compartment_tag_filters": [
            "compartment.test"
          ],
          "enabled": true,
          "enabled_services": [
            "compute"
          ]
        },
        "metrics_config": {
          "compartment_tag_filters": [
            "compartment.test"
          ],
          "enabled": true,
          "excluded_services": [
            "compute"
          ]
        },
        "regions_config": {
          "available": [
            "us-ashburn-1",
            "us-phoenix-1"
          ],
          "disabled": [
            "us-phoenix-1"
          ],
          "enabled": [
            "us-ashburn-1"
          ]
        },
        "resource_collection_enabled": true,
        "user_ocid": "ocid.user.test"
      },
      "id": "ocid.tenancy.test",
      "type": "oci_tenancy"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get tenancy configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
configuration.unstable_operations["get_tenancy_configs"] = True
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.get_tenancy_configs()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get tenancy configs returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_tenancy_configs".to_sym] = true
end
api_instance = DatadogAPIClient::V2::OCIIntegrationAPI.new
p api_instance.get_tenancy_configs()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get tenancy configs returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.GetTenancyConfigs", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOCIIntegrationApi(apiClient)
    resp, r, err := api.GetTenancyConfigs(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OCIIntegrationApi.GetTenancyConfigs`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OCIIntegrationApi.GetTenancyConfigs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get tenancy configs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OciIntegrationApi;
import com.datadog.api.client.v2.model.TenancyConfigList;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getTenancyConfigs", true);
    OciIntegrationApi apiInstance = new OciIntegrationApi(defaultClient);

    try {
      TenancyConfigList result = apiInstance.getTenancyConfigs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OciIntegrationApi#getTenancyConfigs");
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
// Get tenancy configs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_oci_integration::OCIIntegrationAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetTenancyConfigs", true);
    let api = OCIIntegrationAPI::with_config(configuration);
    let resp = api.get_tenancy_configs().await;
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
 * Get tenancy configs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getTenancyConfigs"] = true;
const apiInstance = new v2.OCIIntegrationApi(configuration);

apiInstance
  .getTenancyConfigs()
  .then((data: v2.TenancyConfigList) => {
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

## Create tenancy config{% #create-tenancy-config %}

{% tab title="v2" %}
**Note**: This endpoint may be subject to changes.
| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/oci/tenancies |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/oci/tenancies |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/oci/tenancies      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/oci/tenancies      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/oci/tenancies     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/oci/tenancies |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies |

### Overview

Create a new tenancy config to establish monitoring and data collection from your OCI environment. Requires OCI authentication credentials and tenancy details. Warning: Datadog recommends interacting with this endpoint only through the Datadog web UI to ensure all necessary OCI resources have been created and configured properly.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field     | Field                              | Type     | Description                                                   |
| ---------------- | ---------------------------------- | -------- | ------------------------------------------------------------- |
|                  | data [*required*]             | object   |
| data             | attributes                         | object   |
| attributes       | auth_credentials [*required*] | object   |
| auth_credentials | fingerprint                        | string   |
| auth_credentials | private_key [*required*]      | string   |
| attributes       | config_version                     | int64    |
| attributes       | cost_collection_enabled            | boolean  |
| attributes       | dd_compartment_id                  | string   |
| attributes       | dd_stack_id                        | string   |
| attributes       | home_region [*required*]      | string   |
| attributes       | logs_config                        | object   |
| logs_config      | compartment_tag_filters            | [string] |
| logs_config      | enabled                            | boolean  |
| logs_config      | enabled_services                   | [string] |
| attributes       | metrics_config                     | object   |
| metrics_config   | compartment_tag_filters            | [string] |
| metrics_config   | enabled                            | boolean  |
| metrics_config   | excluded_services                  | [string] |
| attributes       | regions_config                     | object   |
| regions_config   | available                          | [string] |
| regions_config   | disabled                           | [string] |
| regions_config   | enabled                            | [string] |
| attributes       | resource_collection_enabled        | boolean  |
| attributes       | user_ocid [*required*]        | string   |
| data             | id [*required*]               | string   |
| data             | type [*required*]             | enum     | OCI tenancy resource type. Allowed enum values: `oci_tenancy` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "auth_credentials": {
        "fingerprint": "string",
        "private_key": ""
      },
      "config_version": "integer",
      "cost_collection_enabled": false,
      "dd_compartment_id": "string",
      "dd_stack_id": "string",
      "home_region": "",
      "logs_config": {
        "compartment_tag_filters": [],
        "enabled": false,
        "enabled_services": []
      },
      "metrics_config": {
        "compartment_tag_filters": [],
        "enabled": false,
        "excluded_services": []
      },
      "regions_config": {
        "available": [],
        "disabled": [],
        "enabled": []
      },
      "resource_collection_enabled": false,
      "user_ocid": ""
    },
    "id": "",
    "type": "oci_tenancy"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field   | Field                       | Type     | Description                                                   |
| -------------- | --------------------------- | -------- | ------------------------------------------------------------- |
|                | data                        | object   |
| data           | attributes                  | object   |
| attributes     | billing_plan_id             | int32    |
| attributes     | config_version              | int64    |
| attributes     | cost_collection_enabled     | boolean  |
| attributes     | dd_compartment_id           | string   |
| attributes     | dd_stack_id                 | string   |
| attributes     | home_region                 | string   |
| attributes     | logs_config                 | object   |
| logs_config    | compartment_tag_filters     | [string] |
| logs_config    | enabled                     | boolean  |
| logs_config    | enabled_services            | [string] |
| attributes     | metrics_config              | object   |
| metrics_config | compartment_tag_filters     | [string] |
| metrics_config | enabled                     | boolean  |
| metrics_config | excluded_services           | [string] |
| attributes     | parent_tenancy_name         | string   |
| attributes     | regions_config              | object   |
| regions_config | available                   | [string] |
| regions_config | disabled                    | [string] |
| regions_config | enabled                     | [string] |
| attributes     | resource_collection_enabled | boolean  |
| attributes     | tenancy_name                | string   |
| attributes     | user_ocid                   | string   |
| data           | id                          | string   |
| data           | type [*required*]      | enum     | OCI tenancy resource type. Allowed enum values: `oci_tenancy` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_version": 2,
      "cost_collection_enabled": true,
      "dd_compartment_id": "ocid.compartment.test",
      "dd_stack_id": "ocid.stack.test",
      "home_region": "us-ashburn-1",
      "logs_config": {
        "compartment_tag_filters": [
          "compartment.test"
        ],
        "enabled": true,
        "enabled_services": [
          "compute"
        ]
      },
      "metrics_config": {
        "compartment_tag_filters": [
          "compartment.test"
        ],
        "enabled": true,
        "excluded_services": [
          "compute"
        ]
      },
      "regions_config": {
        "available": [
          "us-ashburn-1",
          "us-phoenix-1"
        ],
        "disabled": [
          "us-phoenix-1"
        ],
        "enabled": [
          "us-ashburn-1"
        ]
      },
      "resource_collection_enabled": true,
      "user_ocid": "ocid.user.test"
    },
    "id": "ocid.tenancy.test",
    "type": "oci_tenancy"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "auth_credentials": {
        "private_key": ""
      },
      "home_region": "",
      "user_ocid": ""
    },
    "id": "",
    "type": "oci_tenancy"
  }
}
EOF

#####

```python
"""
Create tenancy config returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi
from datadog_api_client.v2.model.create_tenancy_config_data import CreateTenancyConfigData
from datadog_api_client.v2.model.create_tenancy_config_data_attributes import CreateTenancyConfigDataAttributes
from datadog_api_client.v2.model.create_tenancy_config_data_attributes_auth_credentials import (
    CreateTenancyConfigDataAttributesAuthCredentials,
)
from datadog_api_client.v2.model.create_tenancy_config_data_attributes_logs_config import (
    CreateTenancyConfigDataAttributesLogsConfig,
)
from datadog_api_client.v2.model.create_tenancy_config_data_attributes_metrics_config import (
    CreateTenancyConfigDataAttributesMetricsConfig,
)
from datadog_api_client.v2.model.create_tenancy_config_data_attributes_regions_config import (
    CreateTenancyConfigDataAttributesRegionsConfig,
)
from datadog_api_client.v2.model.create_tenancy_config_request import CreateTenancyConfigRequest
from datadog_api_client.v2.model.update_tenancy_config_data_type import UpdateTenancyConfigDataType

body = CreateTenancyConfigRequest(
    data=CreateTenancyConfigData(
        attributes=CreateTenancyConfigDataAttributes(
            auth_credentials=CreateTenancyConfigDataAttributesAuthCredentials(
                fingerprint="",
                private_key="----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----",
            ),
            config_version=None,
            cost_collection_enabled=True,
            dd_compartment_id="ocid.compartment.test",
            dd_stack_id="ocid.stack.test",
            home_region="us-ashburn-1",
            logs_config=CreateTenancyConfigDataAttributesLogsConfig(
                compartment_tag_filters=[
                    "datadog:true",
                    "env:prod",
                ],
                enabled=True,
                enabled_services=[
                    "service_1",
                    "service_1",
                ],
            ),
            metrics_config=CreateTenancyConfigDataAttributesMetricsConfig(
                compartment_tag_filters=[
                    "datadog:true",
                    "env:prod",
                ],
                enabled=True,
                excluded_services=[
                    "service_1",
                    "service_1",
                ],
            ),
            regions_config=CreateTenancyConfigDataAttributesRegionsConfig(
                available=[
                    "us-ashburn-1",
                    "us-phoenix-1",
                ],
                disabled=[
                    "us-phoenix-1",
                ],
                enabled=[
                    "us-ashburn-1",
                ],
            ),
            resource_collection_enabled=True,
            user_ocid="ocid.user.test",
        ),
        id="ocid.tenancy.test",
        type=UpdateTenancyConfigDataType.OCI_TENANCY,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_tenancy_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.create_tenancy_config(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create tenancy config returns "Created" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_tenancy_config".to_sym] = true
end
api_instance = DatadogAPIClient::V2::OCIIntegrationAPI.new

body = DatadogAPIClient::V2::CreateTenancyConfigRequest.new({
  data: DatadogAPIClient::V2::CreateTenancyConfigData.new({
    attributes: DatadogAPIClient::V2::CreateTenancyConfigDataAttributes.new({
      auth_credentials: DatadogAPIClient::V2::CreateTenancyConfigDataAttributesAuthCredentials.new({
        fingerprint: "",
        private_key: '----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----',
      }),
      config_version: nil,
      cost_collection_enabled: true,
      dd_compartment_id: "ocid.compartment.test",
      dd_stack_id: "ocid.stack.test",
      home_region: "us-ashburn-1",
      logs_config: DatadogAPIClient::V2::CreateTenancyConfigDataAttributesLogsConfig.new({
        compartment_tag_filters: [
          "datadog:true",
          "env:prod",
        ],
        enabled: true,
        enabled_services: [
          "service_1",
          "service_1",
        ],
      }),
      metrics_config: DatadogAPIClient::V2::CreateTenancyConfigDataAttributesMetricsConfig.new({
        compartment_tag_filters: [
          "datadog:true",
          "env:prod",
        ],
        enabled: true,
        excluded_services: [
          "service_1",
          "service_1",
        ],
      }),
      regions_config: DatadogAPIClient::V2::CreateTenancyConfigDataAttributesRegionsConfig.new({
        available: [
          "us-ashburn-1",
          "us-phoenix-1",
        ],
        disabled: [
          "us-phoenix-1",
        ],
        enabled: [
          "us-ashburn-1",
        ],
      }),
      resource_collection_enabled: true,
      user_ocid: "ocid.user.test",
    }),
    id: "ocid.tenancy.test",
    type: DatadogAPIClient::V2::UpdateTenancyConfigDataType::OCI_TENANCY,
  }),
})
p api_instance.create_tenancy_config(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create tenancy config returns "Created" response

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
    body := datadogV2.CreateTenancyConfigRequest{
        Data: datadogV2.CreateTenancyConfigData{
            Attributes: &datadogV2.CreateTenancyConfigDataAttributes{
                AuthCredentials: datadogV2.CreateTenancyConfigDataAttributesAuthCredentials{
                    Fingerprint: datadog.PtrString(""),
                    PrivateKey: `----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M
QsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR
C5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl
YnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn
QGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc
mOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU
nm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc
quMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3
LQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R
W+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx
l6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+
rWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY
PC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59
86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP
XpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS
DBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM
mcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs
-----END PRIVATE KEY-----`,
                },
                ConfigVersion:         *datadog.NewNullableInt64(nil),
                CostCollectionEnabled: datadog.PtrBool(true),
                DdCompartmentId:       datadog.PtrString("ocid.compartment.test"),
                DdStackId:             datadog.PtrString("ocid.stack.test"),
                HomeRegion:            "us-ashburn-1",
                LogsConfig: &datadogV2.CreateTenancyConfigDataAttributesLogsConfig{
                    CompartmentTagFilters: []string{
                        "datadog:true",
                        "env:prod",
                    },
                    Enabled: datadog.PtrBool(true),
                    EnabledServices: []string{
                        "service_1",
                        "service_1",
                    },
                },
                MetricsConfig: &datadogV2.CreateTenancyConfigDataAttributesMetricsConfig{
                    CompartmentTagFilters: []string{
                        "datadog:true",
                        "env:prod",
                    },
                    Enabled: datadog.PtrBool(true),
                    ExcludedServices: []string{
                        "service_1",
                        "service_1",
                    },
                },
                RegionsConfig: &datadogV2.CreateTenancyConfigDataAttributesRegionsConfig{
                    Available: []string{
                        "us-ashburn-1",
                        "us-phoenix-1",
                    },
                    Disabled: []string{
                        "us-phoenix-1",
                    },
                    Enabled: []string{
                        "us-ashburn-1",
                    },
                },
                ResourceCollectionEnabled: datadog.PtrBool(true),
                UserOcid:                  "ocid.user.test",
            },
            Id:   "ocid.tenancy.test",
            Type: datadogV2.UPDATETENANCYCONFIGDATATYPE_OCI_TENANCY,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateTenancyConfig", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOCIIntegrationApi(apiClient)
    resp, r, err := api.CreateTenancyConfig(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OCIIntegrationApi.CreateTenancyConfig`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OCIIntegrationApi.CreateTenancyConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create tenancy config returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OciIntegrationApi;
import com.datadog.api.client.v2.model.CreateTenancyConfigData;
import com.datadog.api.client.v2.model.CreateTenancyConfigDataAttributes;
import com.datadog.api.client.v2.model.CreateTenancyConfigDataAttributesAuthCredentials;
import com.datadog.api.client.v2.model.CreateTenancyConfigDataAttributesLogsConfig;
import com.datadog.api.client.v2.model.CreateTenancyConfigDataAttributesMetricsConfig;
import com.datadog.api.client.v2.model.CreateTenancyConfigDataAttributesRegionsConfig;
import com.datadog.api.client.v2.model.CreateTenancyConfigRequest;
import com.datadog.api.client.v2.model.TenancyConfig;
import com.datadog.api.client.v2.model.UpdateTenancyConfigDataType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createTenancyConfig", true);
    OciIntegrationApi apiInstance = new OciIntegrationApi(defaultClient);

    CreateTenancyConfigRequest body =
        new CreateTenancyConfigRequest()
            .data(
                new CreateTenancyConfigData()
                    .attributes(
                        new CreateTenancyConfigDataAttributes()
                            .authCredentials(
                                new CreateTenancyConfigDataAttributesAuthCredentials()
                                    .fingerprint("")
                                    .privateKey(
                                        """
----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M
QsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR
C5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl
YnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn
QGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc
mOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU
nm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc
quMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3
LQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R
W+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx
l6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+
rWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY
PC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59
86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP
XpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS
DBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM
mcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs
-----END PRIVATE KEY-----
"""))
                            .configVersion(null)
                            .costCollectionEnabled(true)
                            .ddCompartmentId("ocid.compartment.test")
                            .ddStackId("ocid.stack.test")
                            .homeRegion("us-ashburn-1")
                            .logsConfig(
                                new CreateTenancyConfigDataAttributesLogsConfig()
                                    .compartmentTagFilters(
                                        Arrays.asList("datadog:true", "env:prod"))
                                    .enabled(true)
                                    .enabledServices(Arrays.asList("service_1", "service_1")))
                            .metricsConfig(
                                new CreateTenancyConfigDataAttributesMetricsConfig()
                                    .compartmentTagFilters(
                                        Arrays.asList("datadog:true", "env:prod"))
                                    .enabled(true)
                                    .excludedServices(Arrays.asList("service_1", "service_1")))
                            .regionsConfig(
                                new CreateTenancyConfigDataAttributesRegionsConfig()
                                    .available(Arrays.asList("us-ashburn-1", "us-phoenix-1"))
                                    .disabled(Collections.singletonList("us-phoenix-1"))
                                    .enabled(Collections.singletonList("us-ashburn-1")))
                            .resourceCollectionEnabled(true)
                            .userOcid("ocid.user.test"))
                    .id("ocid.tenancy.test")
                    .type(UpdateTenancyConfigDataType.OCI_TENANCY));

    try {
      TenancyConfig result = apiInstance.createTenancyConfig(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OciIntegrationApi#createTenancyConfig");
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
// Create tenancy config returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_oci_integration::OCIIntegrationAPI;
use datadog_api_client::datadogV2::model::CreateTenancyConfigData;
use datadog_api_client::datadogV2::model::CreateTenancyConfigDataAttributes;
use datadog_api_client::datadogV2::model::CreateTenancyConfigDataAttributesAuthCredentials;
use datadog_api_client::datadogV2::model::CreateTenancyConfigDataAttributesLogsConfig;
use datadog_api_client::datadogV2::model::CreateTenancyConfigDataAttributesMetricsConfig;
use datadog_api_client::datadogV2::model::CreateTenancyConfigDataAttributesRegionsConfig;
use datadog_api_client::datadogV2::model::CreateTenancyConfigRequest;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigDataType;

#[tokio::main]
async fn main() {
    let body = CreateTenancyConfigRequest::new(
        CreateTenancyConfigData::new(
            "ocid.tenancy.test".to_string(),
            UpdateTenancyConfigDataType::OCI_TENANCY,
        )
        .attributes(
            CreateTenancyConfigDataAttributes::new(
                CreateTenancyConfigDataAttributesAuthCredentials::new(
                    r#"----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M
QsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR
C5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl
YnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn
QGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc
mOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU
nm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc
quMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3
LQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R
W+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx
l6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+
rWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY
PC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59
86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP
XpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS
DBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM
mcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs
-----END PRIVATE KEY-----"#
                        .to_string(),
                )
                .fingerprint("".to_string()),
                "us-ashburn-1".to_string(),
                "ocid.user.test".to_string(),
            )
            .config_version(None)
            .cost_collection_enabled(true)
            .dd_compartment_id("ocid.compartment.test".to_string())
            .dd_stack_id("ocid.stack.test".to_string())
            .logs_config(
                CreateTenancyConfigDataAttributesLogsConfig::new()
                    .compartment_tag_filters(vec![
                        "datadog:true".to_string(),
                        "env:prod".to_string(),
                    ])
                    .enabled(true)
                    .enabled_services(vec!["service_1".to_string(), "service_1".to_string()]),
            )
            .metrics_config(
                CreateTenancyConfigDataAttributesMetricsConfig::new()
                    .compartment_tag_filters(vec![
                        "datadog:true".to_string(),
                        "env:prod".to_string(),
                    ])
                    .enabled(true)
                    .excluded_services(vec!["service_1".to_string(), "service_1".to_string()]),
            )
            .regions_config(
                CreateTenancyConfigDataAttributesRegionsConfig::new()
                    .available(vec!["us-ashburn-1".to_string(), "us-phoenix-1".to_string()])
                    .disabled(vec!["us-phoenix-1".to_string()])
                    .enabled(vec!["us-ashburn-1".to_string()]),
            )
            .resource_collection_enabled(true),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateTenancyConfig", true);
    let api = OCIIntegrationAPI::with_config(configuration);
    let resp = api.create_tenancy_config(body).await;
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
 * Create tenancy config returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createTenancyConfig"] = true;
const apiInstance = new v2.OCIIntegrationApi(configuration);

const params: v2.OCIIntegrationApiCreateTenancyConfigRequest = {
  body: {
    data: {
      attributes: {
        authCredentials: {
          fingerprint: "",
          privateKey:
            "----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----",
        },
        configVersion: undefined,
        costCollectionEnabled: true,
        ddCompartmentId: "ocid.compartment.test",
        ddStackId: "ocid.stack.test",
        homeRegion: "us-ashburn-1",
        logsConfig: {
          compartmentTagFilters: ["datadog:true", "env:prod"],
          enabled: true,
          enabledServices: ["service_1", "service_1"],
        },
        metricsConfig: {
          compartmentTagFilters: ["datadog:true", "env:prod"],
          enabled: true,
          excludedServices: ["service_1", "service_1"],
        },
        regionsConfig: {
          available: ["us-ashburn-1", "us-phoenix-1"],
          disabled: ["us-phoenix-1"],
          enabled: ["us-ashburn-1"],
        },
        resourceCollectionEnabled: true,
        userOcid: "ocid.user.test",
      },
      id: "ocid.tenancy.test",
      type: "oci_tenancy",
    },
  },
};

apiInstance
  .createTenancyConfig(params)
  .then((data: v2.TenancyConfig) => {
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

## Delete tenancy config{% #delete-tenancy-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/oci/tenancies/{tenancy_ocid}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/oci/tenancies/{tenancy_ocid}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |

### Overview

Delete an existing tenancy config. This will stop all data collection from the specified OCI tenancy and remove the stored configuration. This operation cannot be undone.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                               |
| ------------------------------ | ------ | ----------------------------------------- |
| tenancy_ocid [*required*] | string | The OCID of the tenancy config to delete. |

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
                  \# Path parametersexport tenancy_ocid="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies/${tenancy_ocid}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete tenancy config returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    api_instance.delete_tenancy_config(
        tenancy_ocid="tenancy_ocid",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete tenancy config returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OCIIntegrationAPI.new
api_instance.delete_tenancy_config("tenancy_ocid")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete tenancy config returns "No Content" response

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
    api := datadogV2.NewOCIIntegrationApi(apiClient)
    r, err := api.DeleteTenancyConfig(ctx, "tenancy_ocid")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OCIIntegrationApi.DeleteTenancyConfig`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete tenancy config returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OciIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OciIntegrationApi apiInstance = new OciIntegrationApi(defaultClient);

    try {
      apiInstance.deleteTenancyConfig("tenancy_ocid");
    } catch (ApiException e) {
      System.err.println("Exception when calling OciIntegrationApi#deleteTenancyConfig");
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
// Delete tenancy config returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_oci_integration::OCIIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OCIIntegrationAPI::with_config(configuration);
    let resp = api.delete_tenancy_config("tenancy_ocid".to_string()).await;
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
 * Delete tenancy config returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OCIIntegrationApi(configuration);

const params: v2.OCIIntegrationApiDeleteTenancyConfigRequest = {
  tenancyOcid: "tenancy_ocid",
};

apiInstance
  .deleteTenancyConfig(params)
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

## Get tenancy config{% #get-tenancy-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/oci/tenancies/{tenancy_ocid}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/oci/tenancies/{tenancy_ocid}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |

### Overview

Get a single tenancy config object by its OCID. Returns detailed configuration including authentication credentials, enabled services, region settings, and collection preferences.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                                 |
| ------------------------------ | ------ | ------------------------------------------- |
| tenancy_ocid [*required*] | string | The OCID of the tenancy config to retrieve. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field   | Field                       | Type     | Description                                                   |
| -------------- | --------------------------- | -------- | ------------------------------------------------------------- |
|                | data                        | object   |
| data           | attributes                  | object   |
| attributes     | billing_plan_id             | int32    |
| attributes     | config_version              | int64    |
| attributes     | cost_collection_enabled     | boolean  |
| attributes     | dd_compartment_id           | string   |
| attributes     | dd_stack_id                 | string   |
| attributes     | home_region                 | string   |
| attributes     | logs_config                 | object   |
| logs_config    | compartment_tag_filters     | [string] |
| logs_config    | enabled                     | boolean  |
| logs_config    | enabled_services            | [string] |
| attributes     | metrics_config              | object   |
| metrics_config | compartment_tag_filters     | [string] |
| metrics_config | enabled                     | boolean  |
| metrics_config | excluded_services           | [string] |
| attributes     | parent_tenancy_name         | string   |
| attributes     | regions_config              | object   |
| regions_config | available                   | [string] |
| regions_config | disabled                    | [string] |
| regions_config | enabled                     | [string] |
| attributes     | resource_collection_enabled | boolean  |
| attributes     | tenancy_name                | string   |
| attributes     | user_ocid                   | string   |
| data           | id                          | string   |
| data           | type [*required*]      | enum     | OCI tenancy resource type. Allowed enum values: `oci_tenancy` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_version": 2,
      "cost_collection_enabled": true,
      "dd_compartment_id": "ocid.compartment.test",
      "dd_stack_id": "ocid.stack.test",
      "home_region": "us-ashburn-1",
      "logs_config": {
        "compartment_tag_filters": [
          "compartment.test"
        ],
        "enabled": true,
        "enabled_services": [
          "compute"
        ]
      },
      "metrics_config": {
        "compartment_tag_filters": [
          "compartment.test"
        ],
        "enabled": true,
        "excluded_services": [
          "compute"
        ]
      },
      "regions_config": {
        "available": [
          "us-ashburn-1",
          "us-phoenix-1"
        ],
        "disabled": [
          "us-phoenix-1"
        ],
        "enabled": [
          "us-ashburn-1"
        ]
      },
      "resource_collection_enabled": true,
      "user_ocid": "ocid.user.test"
    },
    "id": "ocid.tenancy.test",
    "type": "oci_tenancy"
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
                  \# Path parametersexport tenancy_ocid="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies/${tenancy_ocid}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get tenancy config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.get_tenancy_config(
        tenancy_ocid="tenancy_ocid",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get tenancy config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OCIIntegrationAPI.new
p api_instance.get_tenancy_config("tenancy_ocid")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get tenancy config returns "OK" response

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
    api := datadogV2.NewOCIIntegrationApi(apiClient)
    resp, r, err := api.GetTenancyConfig(ctx, "tenancy_ocid")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OCIIntegrationApi.GetTenancyConfig`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OCIIntegrationApi.GetTenancyConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get tenancy config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OciIntegrationApi;
import com.datadog.api.client.v2.model.TenancyConfig;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OciIntegrationApi apiInstance = new OciIntegrationApi(defaultClient);

    try {
      TenancyConfig result = apiInstance.getTenancyConfig("tenancy_ocid");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OciIntegrationApi#getTenancyConfig");
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
// Get tenancy config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_oci_integration::OCIIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OCIIntegrationAPI::with_config(configuration);
    let resp = api.get_tenancy_config("tenancy_ocid".to_string()).await;
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
 * Get tenancy config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OCIIntegrationApi(configuration);

const params: v2.OCIIntegrationApiGetTenancyConfigRequest = {
  tenancyOcid: "tenancy_ocid",
};

apiInstance
  .getTenancyConfig(params)
  .then((data: v2.TenancyConfig) => {
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

## Update tenancy config{% #update-tenancy-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integration/oci/tenancies/{tenancy_ocid}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integration/oci/tenancies/{tenancy_ocid}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies/{tenancy_ocid} |

### Overview

Update an existing tenancy config. You can modify authentication credentials, enable/disable collection types, update service filters, and change region settings. Warning: We recommend using the Datadog web UI to avoid unintended update effects.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                               |
| ------------------------------ | ------ | ----------------------------------------- |
| tenancy_ocid [*required*] | string | The OCID of the tenancy config to update. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field     | Field                         | Type     | Description                                                   |
| ---------------- | ----------------------------- | -------- | ------------------------------------------------------------- |
|                  | data [*required*]        | object   |
| data             | attributes                    | object   |
| attributes       | auth_credentials              | object   |
| auth_credentials | fingerprint                   | string   |
| auth_credentials | private_key [*required*] | string   |
| attributes       | cost_collection_enabled       | boolean  |
| attributes       | home_region                   | string   |
| attributes       | logs_config                   | object   |
| logs_config      | compartment_tag_filters       | [string] |
| logs_config      | enabled                       | boolean  |
| logs_config      | enabled_services              | [string] |
| attributes       | metrics_config                | object   |
| metrics_config   | compartment_tag_filters       | [string] |
| metrics_config   | enabled                       | boolean  |
| metrics_config   | excluded_services             | [string] |
| attributes       | regions_config                | object   |
| regions_config   | available                     | [string] |
| regions_config   | disabled                      | [string] |
| regions_config   | enabled                       | [string] |
| attributes       | resource_collection_enabled   | boolean  |
| attributes       | user_ocid                     | string   |
| data             | id [*required*]          | string   |
| data             | type [*required*]        | enum     | OCI tenancy resource type. Allowed enum values: `oci_tenancy` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "auth_credentials": {
        "fingerprint": "string",
        "private_key": ""
      },
      "cost_collection_enabled": false,
      "home_region": "string",
      "logs_config": {
        "compartment_tag_filters": [],
        "enabled": false,
        "enabled_services": []
      },
      "metrics_config": {
        "compartment_tag_filters": [],
        "enabled": false,
        "excluded_services": []
      },
      "regions_config": {
        "available": [],
        "disabled": [],
        "enabled": []
      },
      "resource_collection_enabled": false,
      "user_ocid": "string"
    },
    "id": "",
    "type": "oci_tenancy"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field   | Field                       | Type     | Description                                                   |
| -------------- | --------------------------- | -------- | ------------------------------------------------------------- |
|                | data                        | object   |
| data           | attributes                  | object   |
| attributes     | billing_plan_id             | int32    |
| attributes     | config_version              | int64    |
| attributes     | cost_collection_enabled     | boolean  |
| attributes     | dd_compartment_id           | string   |
| attributes     | dd_stack_id                 | string   |
| attributes     | home_region                 | string   |
| attributes     | logs_config                 | object   |
| logs_config    | compartment_tag_filters     | [string] |
| logs_config    | enabled                     | boolean  |
| logs_config    | enabled_services            | [string] |
| attributes     | metrics_config              | object   |
| metrics_config | compartment_tag_filters     | [string] |
| metrics_config | enabled                     | boolean  |
| metrics_config | excluded_services           | [string] |
| attributes     | parent_tenancy_name         | string   |
| attributes     | regions_config              | object   |
| regions_config | available                   | [string] |
| regions_config | disabled                    | [string] |
| regions_config | enabled                     | [string] |
| attributes     | resource_collection_enabled | boolean  |
| attributes     | tenancy_name                | string   |
| attributes     | user_ocid                   | string   |
| data           | id                          | string   |
| data           | type [*required*]      | enum     | OCI tenancy resource type. Allowed enum values: `oci_tenancy` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "config_version": 2,
      "cost_collection_enabled": true,
      "dd_compartment_id": "ocid.compartment.test",
      "dd_stack_id": "ocid.stack.test",
      "home_region": "us-ashburn-1",
      "logs_config": {
        "compartment_tag_filters": [
          "compartment.test"
        ],
        "enabled": true,
        "enabled_services": [
          "compute"
        ]
      },
      "metrics_config": {
        "compartment_tag_filters": [
          "compartment.test"
        ],
        "enabled": true,
        "excluded_services": [
          "compute"
        ]
      },
      "regions_config": {
        "available": [
          "us-ashburn-1",
          "us-phoenix-1"
        ],
        "disabled": [
          "us-phoenix-1"
        ],
        "enabled": [
          "us-ashburn-1"
        ]
      },
      "resource_collection_enabled": true,
      "user_ocid": "ocid.user.test"
    },
    "id": "ocid.tenancy.test",
    "type": "oci_tenancy"
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
                  \# Path parametersexport tenancy_ocid="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/oci/tenancies/${tenancy_ocid}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "auth_credentials": {
        "private_key": ""
      }
    },
    "id": "",
    "type": "oci_tenancy"
  }
}
EOF

#####

```python
"""
Update tenancy config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi
from datadog_api_client.v2.model.update_tenancy_config_data import UpdateTenancyConfigData
from datadog_api_client.v2.model.update_tenancy_config_data_attributes import UpdateTenancyConfigDataAttributes
from datadog_api_client.v2.model.update_tenancy_config_data_attributes_auth_credentials import (
    UpdateTenancyConfigDataAttributesAuthCredentials,
)
from datadog_api_client.v2.model.update_tenancy_config_data_attributes_logs_config import (
    UpdateTenancyConfigDataAttributesLogsConfig,
)
from datadog_api_client.v2.model.update_tenancy_config_data_attributes_metrics_config import (
    UpdateTenancyConfigDataAttributesMetricsConfig,
)
from datadog_api_client.v2.model.update_tenancy_config_data_attributes_regions_config import (
    UpdateTenancyConfigDataAttributesRegionsConfig,
)
from datadog_api_client.v2.model.update_tenancy_config_data_type import UpdateTenancyConfigDataType
from datadog_api_client.v2.model.update_tenancy_config_request import UpdateTenancyConfigRequest

body = UpdateTenancyConfigRequest(
    data=UpdateTenancyConfigData(
        attributes=UpdateTenancyConfigDataAttributes(
            auth_credentials=UpdateTenancyConfigDataAttributesAuthCredentials(
                fingerprint="",
                private_key="----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----",
            ),
            cost_collection_enabled=True,
            home_region="us-ashburn-1",
            logs_config=UpdateTenancyConfigDataAttributesLogsConfig(
                compartment_tag_filters=[
                    "datadog:true",
                    "env:prod",
                ],
                enabled=True,
                enabled_services=[
                    "service_1",
                    "service_1",
                ],
            ),
            metrics_config=UpdateTenancyConfigDataAttributesMetricsConfig(
                compartment_tag_filters=[
                    "datadog:true",
                    "env:prod",
                ],
                enabled=True,
                excluded_services=[
                    "service_1",
                    "service_1",
                ],
            ),
            regions_config=UpdateTenancyConfigDataAttributesRegionsConfig(
                available=[
                    "us-ashburn-1",
                    "us-phoenix-1",
                ],
                disabled=[
                    "us-phoenix-1",
                ],
                enabled=[
                    "us-ashburn-1",
                ],
            ),
            resource_collection_enabled=True,
            user_ocid="ocid.user.test",
        ),
        id="ocid.tenancy.test",
        type=UpdateTenancyConfigDataType.OCI_TENANCY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.update_tenancy_config(tenancy_ocid="tenancy_ocid", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update tenancy config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OCIIntegrationAPI.new

body = DatadogAPIClient::V2::UpdateTenancyConfigRequest.new({
  data: DatadogAPIClient::V2::UpdateTenancyConfigData.new({
    attributes: DatadogAPIClient::V2::UpdateTenancyConfigDataAttributes.new({
      auth_credentials: DatadogAPIClient::V2::UpdateTenancyConfigDataAttributesAuthCredentials.new({
        fingerprint: "",
        private_key: '----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----',
      }),
      cost_collection_enabled: true,
      home_region: "us-ashburn-1",
      logs_config: DatadogAPIClient::V2::UpdateTenancyConfigDataAttributesLogsConfig.new({
        compartment_tag_filters: [
          "datadog:true",
          "env:prod",
        ],
        enabled: true,
        enabled_services: [
          "service_1",
          "service_1",
        ],
      }),
      metrics_config: DatadogAPIClient::V2::UpdateTenancyConfigDataAttributesMetricsConfig.new({
        compartment_tag_filters: [
          "datadog:true",
          "env:prod",
        ],
        enabled: true,
        excluded_services: [
          "service_1",
          "service_1",
        ],
      }),
      regions_config: DatadogAPIClient::V2::UpdateTenancyConfigDataAttributesRegionsConfig.new({
        available: [
          "us-ashburn-1",
          "us-phoenix-1",
        ],
        disabled: [
          "us-phoenix-1",
        ],
        enabled: [
          "us-ashburn-1",
        ],
      }),
      resource_collection_enabled: true,
      user_ocid: "ocid.user.test",
    }),
    id: "ocid.tenancy.test",
    type: DatadogAPIClient::V2::UpdateTenancyConfigDataType::OCI_TENANCY,
  }),
})
p api_instance.update_tenancy_config("tenancy_ocid", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Update tenancy config returns "OK" response

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
    body := datadogV2.UpdateTenancyConfigRequest{
        Data: datadogV2.UpdateTenancyConfigData{
            Attributes: &datadogV2.UpdateTenancyConfigDataAttributes{
                AuthCredentials: &datadogV2.UpdateTenancyConfigDataAttributesAuthCredentials{
                    Fingerprint: datadog.PtrString(""),
                    PrivateKey: `----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M
QsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR
C5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl
YnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn
QGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc
mOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU
nm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc
quMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3
LQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R
W+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx
l6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+
rWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY
PC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59
86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP
XpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS
DBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM
mcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs
-----END PRIVATE KEY-----`,
                },
                CostCollectionEnabled: datadog.PtrBool(true),
                HomeRegion:            datadog.PtrString("us-ashburn-1"),
                LogsConfig: &datadogV2.UpdateTenancyConfigDataAttributesLogsConfig{
                    CompartmentTagFilters: []string{
                        "datadog:true",
                        "env:prod",
                    },
                    Enabled: datadog.PtrBool(true),
                    EnabledServices: []string{
                        "service_1",
                        "service_1",
                    },
                },
                MetricsConfig: &datadogV2.UpdateTenancyConfigDataAttributesMetricsConfig{
                    CompartmentTagFilters: []string{
                        "datadog:true",
                        "env:prod",
                    },
                    Enabled: datadog.PtrBool(true),
                    ExcludedServices: []string{
                        "service_1",
                        "service_1",
                    },
                },
                RegionsConfig: &datadogV2.UpdateTenancyConfigDataAttributesRegionsConfig{
                    Available: []string{
                        "us-ashburn-1",
                        "us-phoenix-1",
                    },
                    Disabled: []string{
                        "us-phoenix-1",
                    },
                    Enabled: []string{
                        "us-ashburn-1",
                    },
                },
                ResourceCollectionEnabled: datadog.PtrBool(true),
                UserOcid:                  datadog.PtrString("ocid.user.test"),
            },
            Id:   "ocid.tenancy.test",
            Type: datadogV2.UPDATETENANCYCONFIGDATATYPE_OCI_TENANCY,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOCIIntegrationApi(apiClient)
    resp, r, err := api.UpdateTenancyConfig(ctx, "tenancy_ocid", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OCIIntegrationApi.UpdateTenancyConfig`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OCIIntegrationApi.UpdateTenancyConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update tenancy config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OciIntegrationApi;
import com.datadog.api.client.v2.model.TenancyConfig;
import com.datadog.api.client.v2.model.UpdateTenancyConfigData;
import com.datadog.api.client.v2.model.UpdateTenancyConfigDataAttributes;
import com.datadog.api.client.v2.model.UpdateTenancyConfigDataAttributesAuthCredentials;
import com.datadog.api.client.v2.model.UpdateTenancyConfigDataAttributesLogsConfig;
import com.datadog.api.client.v2.model.UpdateTenancyConfigDataAttributesMetricsConfig;
import com.datadog.api.client.v2.model.UpdateTenancyConfigDataAttributesRegionsConfig;
import com.datadog.api.client.v2.model.UpdateTenancyConfigDataType;
import com.datadog.api.client.v2.model.UpdateTenancyConfigRequest;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OciIntegrationApi apiInstance = new OciIntegrationApi(defaultClient);

    UpdateTenancyConfigRequest body =
        new UpdateTenancyConfigRequest()
            .data(
                new UpdateTenancyConfigData()
                    .attributes(
                        new UpdateTenancyConfigDataAttributes()
                            .authCredentials(
                                new UpdateTenancyConfigDataAttributesAuthCredentials()
                                    .fingerprint("")
                                    .privateKey(
                                        """
----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M
QsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR
C5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl
YnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn
QGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc
mOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU
nm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc
quMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3
LQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R
W+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx
l6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+
rWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY
PC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59
86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP
XpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS
DBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM
mcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs
-----END PRIVATE KEY-----
"""))
                            .costCollectionEnabled(true)
                            .homeRegion("us-ashburn-1")
                            .logsConfig(
                                new UpdateTenancyConfigDataAttributesLogsConfig()
                                    .compartmentTagFilters(
                                        Arrays.asList("datadog:true", "env:prod"))
                                    .enabled(true)
                                    .enabledServices(Arrays.asList("service_1", "service_1")))
                            .metricsConfig(
                                new UpdateTenancyConfigDataAttributesMetricsConfig()
                                    .compartmentTagFilters(
                                        Arrays.asList("datadog:true", "env:prod"))
                                    .enabled(true)
                                    .excludedServices(Arrays.asList("service_1", "service_1")))
                            .regionsConfig(
                                new UpdateTenancyConfigDataAttributesRegionsConfig()
                                    .available(Arrays.asList("us-ashburn-1", "us-phoenix-1"))
                                    .disabled(Collections.singletonList("us-phoenix-1"))
                                    .enabled(Collections.singletonList("us-ashburn-1")))
                            .resourceCollectionEnabled(true)
                            .userOcid("ocid.user.test"))
                    .id("ocid.tenancy.test")
                    .type(UpdateTenancyConfigDataType.OCI_TENANCY));

    try {
      TenancyConfig result = apiInstance.updateTenancyConfig("tenancy_ocid", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OciIntegrationApi#updateTenancyConfig");
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
// Update tenancy config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_oci_integration::OCIIntegrationAPI;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigData;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigDataAttributes;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigDataAttributesAuthCredentials;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigDataAttributesLogsConfig;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigDataAttributesMetricsConfig;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigDataAttributesRegionsConfig;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigDataType;
use datadog_api_client::datadogV2::model::UpdateTenancyConfigRequest;

#[tokio::main]
async fn main() {
    let body = UpdateTenancyConfigRequest::new(
        UpdateTenancyConfigData::new(
            "ocid.tenancy.test".to_string(),
            UpdateTenancyConfigDataType::OCI_TENANCY,
        )
        .attributes(
            UpdateTenancyConfigDataAttributes::new()
                .auth_credentials(
                    UpdateTenancyConfigDataAttributesAuthCredentials::new(
                        r#"----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M
QsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR
C5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl
YnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn
QGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc
mOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU
nm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc
quMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3
LQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R
W+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx
l6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+
rWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY
PC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59
86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP
XpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS
DBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM
mcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs
-----END PRIVATE KEY-----"#
                            .to_string(),
                    )
                    .fingerprint("".to_string()),
                )
                .cost_collection_enabled(true)
                .home_region("us-ashburn-1".to_string())
                .logs_config(
                    UpdateTenancyConfigDataAttributesLogsConfig::new()
                        .compartment_tag_filters(vec![
                            "datadog:true".to_string(),
                            "env:prod".to_string(),
                        ])
                        .enabled(true)
                        .enabled_services(vec!["service_1".to_string(), "service_1".to_string()]),
                )
                .metrics_config(
                    UpdateTenancyConfigDataAttributesMetricsConfig::new()
                        .compartment_tag_filters(vec![
                            "datadog:true".to_string(),
                            "env:prod".to_string(),
                        ])
                        .enabled(true)
                        .excluded_services(vec!["service_1".to_string(), "service_1".to_string()]),
                )
                .regions_config(
                    UpdateTenancyConfigDataAttributesRegionsConfig::new()
                        .available(vec!["us-ashburn-1".to_string(), "us-phoenix-1".to_string()])
                        .disabled(vec!["us-phoenix-1".to_string()])
                        .enabled(vec!["us-ashburn-1".to_string()]),
                )
                .resource_collection_enabled(true)
                .user_ocid("ocid.user.test".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = OCIIntegrationAPI::with_config(configuration);
    let resp = api
        .update_tenancy_config("tenancy_ocid".to_string(), body)
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
 * Update tenancy config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OCIIntegrationApi(configuration);

const params: v2.OCIIntegrationApiUpdateTenancyConfigRequest = {
  body: {
    data: {
      attributes: {
        authCredentials: {
          fingerprint: "",
          privateKey:
            "----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----",
        },
        costCollectionEnabled: true,
        homeRegion: "us-ashburn-1",
        logsConfig: {
          compartmentTagFilters: ["datadog:true", "env:prod"],
          enabled: true,
          enabledServices: ["service_1", "service_1"],
        },
        metricsConfig: {
          compartmentTagFilters: ["datadog:true", "env:prod"],
          enabled: true,
          excludedServices: ["service_1", "service_1"],
        },
        regionsConfig: {
          available: ["us-ashburn-1", "us-phoenix-1"],
          disabled: ["us-phoenix-1"],
          enabled: ["us-ashburn-1"],
        },
        resourceCollectionEnabled: true,
        userOcid: "ocid.user.test",
      },
      id: "ocid.tenancy.test",
      type: "oci_tenancy",
    },
  },
  tenancyOcid: "tenancy_ocid",
};

apiInstance
  .updateTenancyConfig(params)
  .then((data: v2.TenancyConfig) => {
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
