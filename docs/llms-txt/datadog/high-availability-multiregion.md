# Source: https://docs.datadoghq.com/api/latest/high-availability-multiregion.md

---
title: High Availability MultiRegion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > High Availability MultiRegion
---

# High Availability MultiRegion

Configure High Availability Multi-Region (HAMR) connections between Datadog organizations. HAMR provides disaster recovery capabilities by maintaining synchronized data between primary and secondary organizations across different datacenters.

## Create or update HAMR organization connection{% #create-or-update-hamr-organization-connection %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/hamr |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/hamr |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/hamr      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/hamr      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/hamr     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/hamr |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/hamr |

### Overview

Create or update the High Availability Multi-Region (HAMR) organization connection. This endpoint allows you to configure the HAMR connection between the authenticated organization and a target organization, including setting the connection status (ONBOARDING, PASSIVE, FAILOVER, ACTIVE, RECOVERY)

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                                   | Type    | Description                                                                                                                                                                               |
| ------------ | --------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                  | object  |
| data         | attributes [*required*]            | object  |
| attributes   | hamr_status [*required*]           | enum    | Status of the HAMR connection:                                                                                                                                                            |
| attributes   | is_primary [*required*]            | boolean | Indicates whether this organization is the primary organization in the HAMR relationship. If true, this is the primary organization. If false, this is the secondary/backup organization. |
| attributes   | modified_by [*required*]           | string  | Username or identifier of the user who last modified this HAMR connection.                                                                                                                |
| attributes   | target_org_datacenter [*required*] | string  | Datacenter location of the target organization (e.g., us1, eu1, us5).                                                                                                                     |
| attributes   | target_org_name [*required*]       | string  | Name of the target organization in the HAMR relationship.                                                                                                                                 |
| attributes   | target_org_uuid [*required*]       | string  | UUID of the target organization in the HAMR relationship.                                                                                                                                 |
| data         | id [*required*]                    | string  | The organization UUID for this HAMR connection. Must match the authenticated organization's UUID.                                                                                         |
| data         | type [*required*]                  | enum    | Type of the HAMR organization connection resource. Allowed enum values: `hamr_org_connections`                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                                   | Type    | Description                                                                                                                                                                               |
| ------------ | --------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                  | object  |
| data         | attributes [*required*]            | object  |
| attributes   | hamr_status [*required*]           | enum    | Status of the HAMR connection:                                                                                                                                                            |
| attributes   | is_primary [*required*]            | boolean | Indicates whether this organization is the primary organization in the HAMR relationship. If true, this is the primary organization. If false, this is the secondary/backup organization. |
| attributes   | modified_at [*required*]           | string  | Timestamp of when this HAMR connection was last modified (RFC3339 format).                                                                                                                |
| attributes   | modified_by [*required*]           | string  | Username or identifier of the user who last modified this HAMR connection.                                                                                                                |
| attributes   | target_org_datacenter [*required*] | string  | Datacenter location of the target organization (e.g., us1, eu1, us5).                                                                                                                     |
| attributes   | target_org_name [*required*]       | string  | Name of the target organization in the HAMR relationship.                                                                                                                                 |
| attributes   | target_org_uuid [*required*]       | string  | UUID of the target organization in the HAMR relationship.                                                                                                                                 |
| data         | id [*required*]                    | string  | The organization UUID for this HAMR connection.                                                                                                                                           |
| data         | type [*required*]                  | enum    | Type of the HAMR organization connection resource. Allowed enum values: `hamr_org_connections`                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_at": "2026-01-13T17:26:48.830968Z",
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="500" %}
Internal Server Error
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

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/hamr" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
  }
}
EOF

#####

```python
"""
Create or update HAMR organization connection returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.high_availability_multi_region_api import HighAvailabilityMultiRegionApi
from datadog_api_client.v2.model.hamr_org_connection_attributes_request import HamrOrgConnectionAttributesRequest
from datadog_api_client.v2.model.hamr_org_connection_data_request import HamrOrgConnectionDataRequest
from datadog_api_client.v2.model.hamr_org_connection_request import HamrOrgConnectionRequest
from datadog_api_client.v2.model.hamr_org_connection_status import HamrOrgConnectionStatus
from datadog_api_client.v2.model.hamr_org_connection_type import HamrOrgConnectionType

body = HamrOrgConnectionRequest(
    data=HamrOrgConnectionDataRequest(
        attributes=HamrOrgConnectionAttributesRequest(
            hamr_status=HamrOrgConnectionStatus.ACTIVE,
            is_primary=True,
            modified_by="admin@example.com",
            target_org_datacenter="us1",
            target_org_name="Production Backup Org",
            target_org_uuid="660f9511-f3ac-52e5-b827-557766551111",
        ),
        id="550e8400-e29b-41d4-a716-446655440000",
        type=HamrOrgConnectionType.HAMR_ORG_CONNECTIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_hamr_org_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = HighAvailabilityMultiRegionApi(api_client)
    response = api_instance.create_hamr_org_connection(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create or update HAMR organization connection returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_hamr_org_connection".to_sym] = true
end
api_instance = DatadogAPIClient::V2::HighAvailabilityMultiRegionAPI.new

body = DatadogAPIClient::V2::HamrOrgConnectionRequest.new({
  data: DatadogAPIClient::V2::HamrOrgConnectionDataRequest.new({
    attributes: DatadogAPIClient::V2::HamrOrgConnectionAttributesRequest.new({
      hamr_status: DatadogAPIClient::V2::HamrOrgConnectionStatus::ACTIVE,
      is_primary: true,
      modified_by: "admin@example.com",
      target_org_datacenter: "us1",
      target_org_name: "Production Backup Org",
      target_org_uuid: "660f9511-f3ac-52e5-b827-557766551111",
    }),
    id: "550e8400-e29b-41d4-a716-446655440000",
    type: DatadogAPIClient::V2::HamrOrgConnectionType::HAMR_ORG_CONNECTIONS,
  }),
})
p api_instance.create_hamr_org_connection(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create or update HAMR organization connection returns "OK" response

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
    body := datadogV2.HamrOrgConnectionRequest{
        Data: datadogV2.HamrOrgConnectionDataRequest{
            Attributes: datadogV2.HamrOrgConnectionAttributesRequest{
                HamrStatus:          datadogV2.HAMRORGCONNECTIONSTATUS_ACTIVE,
                IsPrimary:           true,
                ModifiedBy:          "admin@example.com",
                TargetOrgDatacenter: "us1",
                TargetOrgName:       "Production Backup Org",
                TargetOrgUuid:       "660f9511-f3ac-52e5-b827-557766551111",
            },
            Id:   "550e8400-e29b-41d4-a716-446655440000",
            Type: datadogV2.HAMRORGCONNECTIONTYPE_HAMR_ORG_CONNECTIONS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateHamrOrgConnection", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewHighAvailabilityMultiRegionApi(apiClient)
    resp, r, err := api.CreateHamrOrgConnection(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `HighAvailabilityMultiRegionApi.CreateHamrOrgConnection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `HighAvailabilityMultiRegionApi.CreateHamrOrgConnection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create or update HAMR organization connection returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.HighAvailabilityMultiRegionApi;
import com.datadog.api.client.v2.model.HamrOrgConnectionAttributesRequest;
import com.datadog.api.client.v2.model.HamrOrgConnectionDataRequest;
import com.datadog.api.client.v2.model.HamrOrgConnectionRequest;
import com.datadog.api.client.v2.model.HamrOrgConnectionResponse;
import com.datadog.api.client.v2.model.HamrOrgConnectionStatus;
import com.datadog.api.client.v2.model.HamrOrgConnectionType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createHamrOrgConnection", true);
    HighAvailabilityMultiRegionApi apiInstance = new HighAvailabilityMultiRegionApi(defaultClient);

    HamrOrgConnectionRequest body =
        new HamrOrgConnectionRequest()
            .data(
                new HamrOrgConnectionDataRequest()
                    .attributes(
                        new HamrOrgConnectionAttributesRequest()
                            .hamrStatus(HamrOrgConnectionStatus.ACTIVE)
                            .isPrimary(true)
                            .modifiedBy("admin@example.com")
                            .targetOrgDatacenter("us1")
                            .targetOrgName("Production Backup Org")
                            .targetOrgUuid("660f9511-f3ac-52e5-b827-557766551111"))
                    .id("550e8400-e29b-41d4-a716-446655440000")
                    .type(HamrOrgConnectionType.HAMR_ORG_CONNECTIONS));

    try {
      HamrOrgConnectionResponse result = apiInstance.createHamrOrgConnection(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling HighAvailabilityMultiRegionApi#createHamrOrgConnection");
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
// Create or update HAMR organization connection returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_high_availability_multi_region::HighAvailabilityMultiRegionAPI;
use datadog_api_client::datadogV2::model::HamrOrgConnectionAttributesRequest;
use datadog_api_client::datadogV2::model::HamrOrgConnectionDataRequest;
use datadog_api_client::datadogV2::model::HamrOrgConnectionRequest;
use datadog_api_client::datadogV2::model::HamrOrgConnectionStatus;
use datadog_api_client::datadogV2::model::HamrOrgConnectionType;

#[tokio::main]
async fn main() {
    let body = HamrOrgConnectionRequest::new(HamrOrgConnectionDataRequest::new(
        HamrOrgConnectionAttributesRequest::new(
            HamrOrgConnectionStatus::ACTIVE,
            true,
            "admin@example.com".to_string(),
            "us1".to_string(),
            "Production Backup Org".to_string(),
            "660f9511-f3ac-52e5-b827-557766551111".to_string(),
        ),
        "550e8400-e29b-41d4-a716-446655440000".to_string(),
        HamrOrgConnectionType::HAMR_ORG_CONNECTIONS,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateHamrOrgConnection", true);
    let api = HighAvailabilityMultiRegionAPI::with_config(configuration);
    let resp = api.create_hamr_org_connection(body).await;
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
 * Create or update HAMR organization connection returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createHamrOrgConnection"] = true;
const apiInstance = new v2.HighAvailabilityMultiRegionApi(configuration);

const params: v2.HighAvailabilityMultiRegionApiCreateHamrOrgConnectionRequest =
  {
    body: {
      data: {
        attributes: {
          hamrStatus: 4,
          isPrimary: true,
          modifiedBy: "admin@example.com",
          targetOrgDatacenter: "us1",
          targetOrgName: "Production Backup Org",
          targetOrgUuid: "660f9511-f3ac-52e5-b827-557766551111",
        },
        id: "550e8400-e29b-41d4-a716-446655440000",
        type: "hamr_org_connections",
      },
    },
  };

apiInstance
  .createHamrOrgConnection(params)
  .then((data: v2.HamrOrgConnectionResponse) => {
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

## Get HAMR organization connection{% #get-hamr-organization-connection %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                  |
| ----------------- | --------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/hamr |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/hamr |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/hamr      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/hamr      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/hamr     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/hamr |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/hamr |

### Overview

Retrieve the High Availability Multi-Region (HAMR) organization connection details for the authenticated organization. This endpoint returns information about the HAMR connection configuration, including the target organization, datacenter, status, and whether this is the primary or secondary organization in the HAMR relationship.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                                   | Type    | Description                                                                                                                                                                               |
| ------------ | --------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                  | object  |
| data         | attributes [*required*]            | object  |
| attributes   | hamr_status [*required*]           | enum    | Status of the HAMR connection:                                                                                                                                                            |
| attributes   | is_primary [*required*]            | boolean | Indicates whether this organization is the primary organization in the HAMR relationship. If true, this is the primary organization. If false, this is the secondary/backup organization. |
| attributes   | modified_at [*required*]           | string  | Timestamp of when this HAMR connection was last modified (RFC3339 format).                                                                                                                |
| attributes   | modified_by [*required*]           | string  | Username or identifier of the user who last modified this HAMR connection.                                                                                                                |
| attributes   | target_org_datacenter [*required*] | string  | Datacenter location of the target organization (e.g., us1, eu1, us5).                                                                                                                     |
| attributes   | target_org_name [*required*]       | string  | Name of the target organization in the HAMR relationship.                                                                                                                                 |
| attributes   | target_org_uuid [*required*]       | string  | UUID of the target organization in the HAMR relationship.                                                                                                                                 |
| data         | id [*required*]                    | string  | The organization UUID for this HAMR connection.                                                                                                                                           |
| data         | type [*required*]                  | enum    | Type of the HAMR organization connection resource. Allowed enum values: `hamr_org_connections`                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_at": "2026-01-13T17:26:48.830968Z",
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
Not Found
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/hamr" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get HAMR organization connection returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.high_availability_multi_region_api import HighAvailabilityMultiRegionApi

configuration = Configuration()
configuration.unstable_operations["get_hamr_org_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = HighAvailabilityMultiRegionApi(api_client)
    response = api_instance.get_hamr_org_connection()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get HAMR organization connection returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_hamr_org_connection".to_sym] = true
end
api_instance = DatadogAPIClient::V2::HighAvailabilityMultiRegionAPI.new
p api_instance.get_hamr_org_connection()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get HAMR organization connection returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.GetHamrOrgConnection", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewHighAvailabilityMultiRegionApi(apiClient)
    resp, r, err := api.GetHamrOrgConnection(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `HighAvailabilityMultiRegionApi.GetHamrOrgConnection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `HighAvailabilityMultiRegionApi.GetHamrOrgConnection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get HAMR organization connection returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.HighAvailabilityMultiRegionApi;
import com.datadog.api.client.v2.model.HamrOrgConnectionResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getHamrOrgConnection", true);
    HighAvailabilityMultiRegionApi apiInstance = new HighAvailabilityMultiRegionApi(defaultClient);

    try {
      HamrOrgConnectionResponse result = apiInstance.getHamrOrgConnection();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling HighAvailabilityMultiRegionApi#getHamrOrgConnection");
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
// Get HAMR organization connection returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_high_availability_multi_region::HighAvailabilityMultiRegionAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetHamrOrgConnection", true);
    let api = HighAvailabilityMultiRegionAPI::with_config(configuration);
    let resp = api.get_hamr_org_connection().await;
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
 * Get HAMR organization connection returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getHamrOrgConnection"] = true;
const apiInstance = new v2.HighAvailabilityMultiRegionApi(configuration);

apiInstance
  .getHamrOrgConnection()
  .then((data: v2.HamrOrgConnectionResponse) => {
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
