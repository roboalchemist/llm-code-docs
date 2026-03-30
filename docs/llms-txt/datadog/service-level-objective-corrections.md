# Source: https://docs.datadoghq.com/api/latest/service-level-objective-corrections.md

---
title: Service Level Objective Corrections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Service Level Objective Corrections
---

# Service Level Objective Corrections

SLO Status Corrections allow you to prevent specific time periods from negatively impacting your SLO's status and error budget. You can use Status Corrections for various purposes, such as removing planned maintenance windows, non-business hours, or other time periods that do not correspond to genuine issues. See [SLO status corrections](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-status-corrections) for more information.

## Create an SLO correction{% #create-an-slo-correction %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/slo/correction |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/slo/correction |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/slo/correction      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/slo/correction      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/slo/correction     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/slo/correction |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/slo/correction |

### Overview

Create an SLO Correction. This endpoint requires the `slos_corrections` permission.

OAuth apps require the `slos_corrections` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objective-corrections) to access this endpoint.



### Request

#### Body Data (required)

Create an SLO Correction

{% tab title="Model" %}

| Parent field | Field                      | Type   | Description                                                                                                                                              |
| ------------ | -------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                       | object | The data object associated with the SLO correction to be created.                                                                                        |
| data         | attributes                 | object | The attribute object associated with the SLO correction to be created.                                                                                   |
| attributes   | category [*required*] | enum   | Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`                             |
| attributes   | description                | string | Description of the correction being made.                                                                                                                |
| attributes   | duration                   | int64  | Length of time (in seconds) for a specified `rrule` recurring SLO correction.                                                                            |
| attributes   | end                        | int64  | Ending time of the correction in epoch seconds.                                                                                                          |
| attributes   | rrule                      | string | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`. |
| attributes   | slo_id [*required*]   | string | ID of the SLO that this correction applies to.                                                                                                           |
| attributes   | start [*required*]    | int64  | Starting time of the correction in epoch seconds.                                                                                                        |
| attributes   | timezone                   | string | The timezone to display in the UI for the correction times (defaults to "UTC").                                                                          |
| data         | type [*required*]     | enum   | SLO correction resource type. Allowed enum values: `correction`                                                                                          |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "category": "Scheduled Maintenance",
      "description": "Example-Service-Level-Objective-Correction",
      "end": 1636632671,
      "slo_id": "string",
      "start": 1636629071,
      "timezone": "UTC"
    },
    "type": "correction"
  }
}
```

#####

```json
{
  "data": {
    "attributes": {
      "category": "Scheduled Maintenance",
      "description": "Example-Service-Level-Objective-Correction",
      "slo_id": "string",
      "start": 1636629071,
      "duration": 3600,
      "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5",
      "timezone": "UTC"
    },
    "type": "correction"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object of an SLO correction.

| Parent field | Field       | Type   | Description                                                                                                                                              |
| ------------ | ----------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data        | object | The response object of a list of SLO corrections.                                                                                                        |
| data         | attributes  | object | The attribute object associated with the SLO correction.                                                                                                 |
| attributes   | category    | enum   | Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`                             |
| attributes   | created_at  | int64  | The epoch timestamp of when the correction was created at.                                                                                               |
| attributes   | creator     | object | Object describing the creator of the shared element.                                                                                                     |
| creator      | email       | string | Email of the creator.                                                                                                                                    |
| creator      | handle      | string | Handle of the creator.                                                                                                                                   |
| creator      | name        | string | Name of the creator.                                                                                                                                     |
| attributes   | description | string | Description of the correction being made.                                                                                                                |
| attributes   | duration    | int64  | Length of time (in seconds) for a specified `rrule` recurring SLO correction.                                                                            |
| attributes   | end         | int64  | Ending time of the correction in epoch seconds.                                                                                                          |
| attributes   | modified_at | int64  | The epoch timestamp of when the correction was modified at.                                                                                              |
| attributes   | modifier    | object | Modifier of the object.                                                                                                                                  |
| modifier     | email       | string | Email of the Modifier.                                                                                                                                   |
| modifier     | handle      | string | Handle of the Modifier.                                                                                                                                  |
| modifier     | name        | string | Name of the Modifier.                                                                                                                                    |
| attributes   | rrule       | string | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`. |
| attributes   | slo_id      | string | ID of the SLO that this correction applies to.                                                                                                           |
| attributes   | start       | int64  | Starting time of the correction in epoch seconds.                                                                                                        |
| attributes   | timezone    | string | The timezone to display in the UI for the correction times (defaults to "UTC").                                                                          |
| data         | id          | string | The ID of the SLO correction.                                                                                                                            |
| data         | type        | enum   | SLO correction resource type. Allowed enum values: `correction`                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "category": "Scheduled Maintenance",
      "created_at": "integer",
      "creator": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "description": "string",
      "duration": 3600,
      "end": "integer",
      "modified_at": "integer",
      "modifier": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5",
      "slo_id": "string",
      "start": "integer",
      "timezone": "string"
    },
    "id": "string",
    "type": "correction"
  }
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
Forbidden
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

{% tab title="404" %}
SLO Not Found
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "category": "Scheduled Maintenance",
      "description": "Example-Service-Level-Objective-Correction",
      "end": 1636632671,
      "slo_id": "string",
      "start": 1636629071,
      "timezone": "UTC"
    },
    "type": "correction"
  }
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "category": "Scheduled Maintenance",
      "description": "Example-Service-Level-Objective-Correction",
      "slo_id": "string",
      "start": 1636629071,
      "duration": 3600,
      "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5",
      "timezone": "UTC"
    },
    "type": "correction"
  }
}
EOF

#####

```go
// Create an SLO correction returns "OK" response

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
    // there is a valid "slo" in the system
    SloData0ID := os.Getenv("SLO_DATA_0_ID")

    body := datadogV1.SLOCorrectionCreateRequest{
        Data: &datadogV1.SLOCorrectionCreateData{
            Attributes: &datadogV1.SLOCorrectionCreateRequestAttributes{
                Category:    datadogV1.SLOCORRECTIONCATEGORY_SCHEDULED_MAINTENANCE,
                Description: datadog.PtrString("Example-Service-Level-Objective-Correction"),
                End:         datadog.PtrInt64(time.Now().Add(time.Hour * 1).Unix()),
                SloId:       SloData0ID,
                Start:       time.Now().Unix(),
                Timezone:    datadog.PtrString("UTC"),
            },
            Type: datadogV1.SLOCORRECTIONTYPE_CORRECTION,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewServiceLevelObjectiveCorrectionsApi(apiClient)
    resp, r, err := api.CreateSLOCorrection(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectiveCorrectionsApi.CreateSLOCorrection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectiveCorrectionsApi.CreateSLOCorrection`:\n%s\n", responseContent)
}
```

#####

```go
// Create an SLO correction with rrule returns "OK" response

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
    // there is a valid "slo" in the system
    SloData0ID := os.Getenv("SLO_DATA_0_ID")

    body := datadogV1.SLOCorrectionCreateRequest{
        Data: &datadogV1.SLOCorrectionCreateData{
            Attributes: &datadogV1.SLOCorrectionCreateRequestAttributes{
                Category:    datadogV1.SLOCORRECTIONCATEGORY_SCHEDULED_MAINTENANCE,
                Description: datadog.PtrString("Example-Service-Level-Objective-Correction"),
                SloId:       SloData0ID,
                Start:       time.Now().Unix(),
                Duration:    datadog.PtrInt64(3600),
                Rrule:       datadog.PtrString("FREQ=DAILY;INTERVAL=10;COUNT=5"),
                Timezone:    datadog.PtrString("UTC"),
            },
            Type: datadogV1.SLOCORRECTIONTYPE_CORRECTION,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewServiceLevelObjectiveCorrectionsApi(apiClient)
    resp, r, err := api.CreateSLOCorrection(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectiveCorrectionsApi.CreateSLOCorrection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectiveCorrectionsApi.CreateSLOCorrection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create an SLO correction returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectiveCorrectionsApi;
import com.datadog.api.client.v1.model.SLOCorrectionCategory;
import com.datadog.api.client.v1.model.SLOCorrectionCreateData;
import com.datadog.api.client.v1.model.SLOCorrectionCreateRequest;
import com.datadog.api.client.v1.model.SLOCorrectionCreateRequestAttributes;
import com.datadog.api.client.v1.model.SLOCorrectionResponse;
import com.datadog.api.client.v1.model.SLOCorrectionType;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectiveCorrectionsApi apiInstance =
        new ServiceLevelObjectiveCorrectionsApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");

    SLOCorrectionCreateRequest body =
        new SLOCorrectionCreateRequest()
            .data(
                new SLOCorrectionCreateData()
                    .attributes(
                        new SLOCorrectionCreateRequestAttributes()
                            .category(SLOCorrectionCategory.SCHEDULED_MAINTENANCE)
                            .description("Example-Service-Level-Objective-Correction")
                            .end(OffsetDateTime.now().plusHours(1).toInstant().getEpochSecond())
                            .sloId(SLO_DATA_0_ID)
                            .start(OffsetDateTime.now().toInstant().getEpochSecond())
                            .timezone("UTC"))
                    .type(SLOCorrectionType.CORRECTION));

    try {
      SLOCorrectionResponse result = apiInstance.createSLOCorrection(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceLevelObjectiveCorrectionsApi#createSLOCorrection");
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
// Create an SLO correction with rrule returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectiveCorrectionsApi;
import com.datadog.api.client.v1.model.SLOCorrectionCategory;
import com.datadog.api.client.v1.model.SLOCorrectionCreateData;
import com.datadog.api.client.v1.model.SLOCorrectionCreateRequest;
import com.datadog.api.client.v1.model.SLOCorrectionCreateRequestAttributes;
import com.datadog.api.client.v1.model.SLOCorrectionResponse;
import com.datadog.api.client.v1.model.SLOCorrectionType;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectiveCorrectionsApi apiInstance =
        new ServiceLevelObjectiveCorrectionsApi(defaultClient);

    // there is a valid "slo" in the system
    String SLO_DATA_0_ID = System.getenv("SLO_DATA_0_ID");

    SLOCorrectionCreateRequest body =
        new SLOCorrectionCreateRequest()
            .data(
                new SLOCorrectionCreateData()
                    .attributes(
                        new SLOCorrectionCreateRequestAttributes()
                            .category(SLOCorrectionCategory.SCHEDULED_MAINTENANCE)
                            .description("Example-Service-Level-Objective-Correction")
                            .sloId(SLO_DATA_0_ID)
                            .start(OffsetDateTime.now().toInstant().getEpochSecond())
                            .duration(3600L)
                            .rrule("FREQ=DAILY;INTERVAL=10;COUNT=5")
                            .timezone("UTC"))
                    .type(SLOCorrectionType.CORRECTION));

    try {
      SLOCorrectionResponse result = apiInstance.createSLOCorrection(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceLevelObjectiveCorrectionsApi#createSLOCorrection");
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
Create an SLO correction returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_create_data import SLOCorrectionCreateData
from datadog_api_client.v1.model.slo_correction_create_request import SLOCorrectionCreateRequest
from datadog_api_client.v1.model.slo_correction_create_request_attributes import SLOCorrectionCreateRequestAttributes
from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

body = SLOCorrectionCreateRequest(
    data=SLOCorrectionCreateData(
        attributes=SLOCorrectionCreateRequestAttributes(
            category=SLOCorrectionCategory.SCHEDULED_MAINTENANCE,
            description="Example-Service-Level-Objective-Correction",
            end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
            slo_id=SLO_DATA_0_ID,
            start=int(datetime.now().timestamp()),
            timezone="UTC",
        ),
        type=SLOCorrectionType.CORRECTION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.create_slo_correction(body=body)

    print(response)
```

#####

```python
"""
Create an SLO correction with rrule returns "OK" response
"""

from datetime import datetime
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_create_data import SLOCorrectionCreateData
from datadog_api_client.v1.model.slo_correction_create_request import SLOCorrectionCreateRequest
from datadog_api_client.v1.model.slo_correction_create_request_attributes import SLOCorrectionCreateRequestAttributes
from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

body = SLOCorrectionCreateRequest(
    data=SLOCorrectionCreateData(
        attributes=SLOCorrectionCreateRequestAttributes(
            category=SLOCorrectionCategory.SCHEDULED_MAINTENANCE,
            description="Example-Service-Level-Objective-Correction",
            slo_id=SLO_DATA_0_ID,
            start=int(datetime.now().timestamp()),
            duration=3600,
            rrule="FREQ=DAILY;INTERVAL=10;COUNT=5",
            timezone="UTC",
        ),
        type=SLOCorrectionType.CORRECTION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.create_slo_correction(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create an SLO correction returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]

body = DatadogAPIClient::V1::SLOCorrectionCreateRequest.new({
  data: DatadogAPIClient::V1::SLOCorrectionCreateData.new({
    attributes: DatadogAPIClient::V1::SLOCorrectionCreateRequestAttributes.new({
      category: DatadogAPIClient::V1::SLOCorrectionCategory::SCHEDULED_MAINTENANCE,
      description: "Example-Service-Level-Objective-Correction",
      _end: (Time.now + 1 * 3600).to_i,
      slo_id: SLO_DATA_0_ID,
      start: Time.now.to_i,
      timezone: "UTC",
    }),
    type: DatadogAPIClient::V1::SLOCorrectionType::CORRECTION,
  }),
})
p api_instance.create_slo_correction(body)
```

#####

```ruby
# Create an SLO correction with rrule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]

body = DatadogAPIClient::V1::SLOCorrectionCreateRequest.new({
  data: DatadogAPIClient::V1::SLOCorrectionCreateData.new({
    attributes: DatadogAPIClient::V1::SLOCorrectionCreateRequestAttributes.new({
      category: DatadogAPIClient::V1::SLOCorrectionCategory::SCHEDULED_MAINTENANCE,
      description: "Example-Service-Level-Objective-Correction",
      slo_id: SLO_DATA_0_ID,
      start: Time.now.to_i,
      duration: 3600,
      rrule: "FREQ=DAILY;INTERVAL=10;COUNT=5",
      timezone: "UTC",
    }),
    type: DatadogAPIClient::V1::SLOCorrectionType::CORRECTION,
  }),
})
p api_instance.create_slo_correction(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create an SLO correction returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objective_corrections::ServiceLevelObjectiveCorrectionsAPI;
use datadog_api_client::datadogV1::model::SLOCorrectionCategory;
use datadog_api_client::datadogV1::model::SLOCorrectionCreateData;
use datadog_api_client::datadogV1::model::SLOCorrectionCreateRequest;
use datadog_api_client::datadogV1::model::SLOCorrectionCreateRequestAttributes;
use datadog_api_client::datadogV1::model::SLOCorrectionType;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let body = SLOCorrectionCreateRequest::new().data(
        SLOCorrectionCreateData::new(SLOCorrectionType::CORRECTION).attributes(
            SLOCorrectionCreateRequestAttributes::new(
                SLOCorrectionCategory::SCHEDULED_MAINTENANCE,
                slo_data_0_id.clone(),
                1636629071,
            )
            .description("Example-Service-Level-Objective-Correction".to_string())
            .end(1636632671)
            .timezone("UTC".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectiveCorrectionsAPI::with_config(configuration);
    let resp = api.create_slo_correction(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create an SLO correction with rrule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objective_corrections::ServiceLevelObjectiveCorrectionsAPI;
use datadog_api_client::datadogV1::model::SLOCorrectionCategory;
use datadog_api_client::datadogV1::model::SLOCorrectionCreateData;
use datadog_api_client::datadogV1::model::SLOCorrectionCreateRequest;
use datadog_api_client::datadogV1::model::SLOCorrectionCreateRequestAttributes;
use datadog_api_client::datadogV1::model::SLOCorrectionType;

#[tokio::main]
async fn main() {
    // there is a valid "slo" in the system
    let slo_data_0_id = std::env::var("SLO_DATA_0_ID").unwrap();
    let body = SLOCorrectionCreateRequest::new().data(
        SLOCorrectionCreateData::new(SLOCorrectionType::CORRECTION).attributes(
            SLOCorrectionCreateRequestAttributes::new(
                SLOCorrectionCategory::SCHEDULED_MAINTENANCE,
                slo_data_0_id.clone(),
                1636629071,
            )
            .description("Example-Service-Level-Objective-Correction".to_string())
            .duration(3600)
            .rrule("FREQ=DAILY;INTERVAL=10;COUNT=5".to_string())
            .timezone("UTC".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectiveCorrectionsAPI::with_config(configuration);
    let resp = api.create_slo_correction(body).await;
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
 * Create an SLO correction returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectiveCorrectionsApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;

const params: v1.ServiceLevelObjectiveCorrectionsApiCreateSLOCorrectionRequest =
  {
    body: {
      data: {
        attributes: {
          category: "Scheduled Maintenance",
          description: "Example-Service-Level-Objective-Correction",
          end: Math.round(
            new Date(new Date().getTime() + 1 * 3600 * 1000).getTime() / 1000
          ),
          sloId: SLO_DATA_0_ID,
          start: Math.round(new Date().getTime() / 1000),
          timezone: "UTC",
        },
        type: "correction",
      },
    },
  };

apiInstance
  .createSLOCorrection(params)
  .then((data: v1.SLOCorrectionResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create an SLO correction with rrule returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectiveCorrectionsApi(configuration);

// there is a valid "slo" in the system
const SLO_DATA_0_ID = process.env.SLO_DATA_0_ID as string;

const params: v1.ServiceLevelObjectiveCorrectionsApiCreateSLOCorrectionRequest =
  {
    body: {
      data: {
        attributes: {
          category: "Scheduled Maintenance",
          description: "Example-Service-Level-Objective-Correction",
          sloId: SLO_DATA_0_ID,
          start: Math.round(new Date().getTime() / 1000),
          duration: 3600,
          rrule: "FREQ=DAILY;INTERVAL=10;COUNT=5",
          timezone: "UTC",
        },
        type: "correction",
      },
    },
  };

apiInstance
  .createSLOCorrection(params)
  .then((data: v1.SLOCorrectionResponse) => {
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

## Get all SLO corrections{% #get-all-slo-corrections %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo/correction |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo/correction |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo/correction      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo/correction      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo/correction     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo/correction |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo/correction |

### Overview

Get all Service Level Objective corrections. This endpoint requires the `slos_read` permission.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objective-corrections) to access this endpoint.



### Arguments

#### Query Strings

| Name   | Type    | Description                                                             |
| ------ | ------- | ----------------------------------------------------------------------- |
| offset | integer | The specific offset to use as the beginning of the returned response.   |
| limit  | integer | The number of SLO corrections to return in the response. Default is 25. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A list of SLO correction objects.

| Parent field | Field                | Type     | Description                                                                                                                                              |
| ------------ | -------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                 | [object] | The list of SLO corrections objects.                                                                                                                     |
| data         | attributes           | object   | The attribute object associated with the SLO correction.                                                                                                 |
| attributes   | category             | enum     | Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`                             |
| attributes   | created_at           | int64    | The epoch timestamp of when the correction was created at.                                                                                               |
| attributes   | creator              | object   | Object describing the creator of the shared element.                                                                                                     |
| creator      | email                | string   | Email of the creator.                                                                                                                                    |
| creator      | handle               | string   | Handle of the creator.                                                                                                                                   |
| creator      | name                 | string   | Name of the creator.                                                                                                                                     |
| attributes   | description          | string   | Description of the correction being made.                                                                                                                |
| attributes   | duration             | int64    | Length of time (in seconds) for a specified `rrule` recurring SLO correction.                                                                            |
| attributes   | end                  | int64    | Ending time of the correction in epoch seconds.                                                                                                          |
| attributes   | modified_at          | int64    | The epoch timestamp of when the correction was modified at.                                                                                              |
| attributes   | modifier             | object   | Modifier of the object.                                                                                                                                  |
| modifier     | email                | string   | Email of the Modifier.                                                                                                                                   |
| modifier     | handle               | string   | Handle of the Modifier.                                                                                                                                  |
| modifier     | name                 | string   | Name of the Modifier.                                                                                                                                    |
| attributes   | rrule                | string   | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`. |
| attributes   | slo_id               | string   | ID of the SLO that this correction applies to.                                                                                                           |
| attributes   | start                | int64    | Starting time of the correction in epoch seconds.                                                                                                        |
| attributes   | timezone             | string   | The timezone to display in the UI for the correction times (defaults to "UTC").                                                                          |
| data         | id                   | string   | The ID of the SLO correction.                                                                                                                            |
| data         | type                 | enum     | SLO correction resource type. Allowed enum values: `correction`                                                                                          |
|              | meta                 | object   | Object describing meta attributes of response.                                                                                                           |
| meta         | page                 | object   | Pagination object.                                                                                                                                       |
| page         | total_count          | int64    | Total count.                                                                                                                                             |
| page         | total_filtered_count | int64    | Total count of elements matched by the filter.                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "category": "Scheduled Maintenance",
        "created_at": "integer",
        "creator": {
          "email": "string",
          "handle": "string",
          "name": "string"
        },
        "description": "string",
        "duration": 3600,
        "end": "integer",
        "modified_at": "integer",
        "modifier": {
          "email": "string",
          "handle": "string",
          "name": "string"
        },
        "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5",
        "slo_id": "string",
        "start": "integer",
        "timezone": "string"
      },
      "id": "string",
      "type": "correction"
    }
  ],
  "meta": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all SLO corrections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.list_slo_correction(
        offset=1,
        limit=1,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get all SLO corrections returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new
opts = {
  offset: 1,
  limit: 1,
}
p api_instance.list_slo_correction(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get all SLO corrections returns "OK" response

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
    api := datadogV1.NewServiceLevelObjectiveCorrectionsApi(apiClient)
    resp, r, err := api.ListSLOCorrection(ctx, *datadogV1.NewListSLOCorrectionOptionalParameters().WithOffset(1).WithLimit(1))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectiveCorrectionsApi.ListSLOCorrection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectiveCorrectionsApi.ListSLOCorrection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get all SLO corrections returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectiveCorrectionsApi;
import com.datadog.api.client.v1.api.ServiceLevelObjectiveCorrectionsApi.ListSLOCorrectionOptionalParameters;
import com.datadog.api.client.v1.model.SLOCorrectionListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectiveCorrectionsApi apiInstance =
        new ServiceLevelObjectiveCorrectionsApi(defaultClient);

    try {
      SLOCorrectionListResponse result =
          apiInstance.listSLOCorrection(
              new ListSLOCorrectionOptionalParameters().offset(1L).limit(1L));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceLevelObjectiveCorrectionsApi#listSLOCorrection");
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
// Get all SLO corrections returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objective_corrections::ListSLOCorrectionOptionalParams;
use datadog_api_client::datadogV1::api_service_level_objective_corrections::ServiceLevelObjectiveCorrectionsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectiveCorrectionsAPI::with_config(configuration);
    let resp = api
        .list_slo_correction(
            ListSLOCorrectionOptionalParams::default()
                .offset(1)
                .limit(1),
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
 * Get all SLO corrections returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectiveCorrectionsApi(configuration);

const params: v1.ServiceLevelObjectiveCorrectionsApiListSLOCorrectionRequest = {
  offset: 1,
  limit: 1,
};

apiInstance
  .listSLOCorrection(params)
  .then((data: v1.SLOCorrectionListResponse) => {
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

## Get an SLO correction for an SLO{% #get-an-slo-correction-for-an-slo %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo/correction/{slo_correction_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo/correction/{slo_correction_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo/correction/{slo_correction_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |

### Overview

Get an SLO correction.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                          |
| ----------------------------------- | ------ | ------------------------------------ |
| slo_correction_id [*required*] | string | The ID of the SLO correction object. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object of an SLO correction.

| Parent field | Field       | Type   | Description                                                                                                                                              |
| ------------ | ----------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data        | object | The response object of a list of SLO corrections.                                                                                                        |
| data         | attributes  | object | The attribute object associated with the SLO correction.                                                                                                 |
| attributes   | category    | enum   | Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`                             |
| attributes   | created_at  | int64  | The epoch timestamp of when the correction was created at.                                                                                               |
| attributes   | creator     | object | Object describing the creator of the shared element.                                                                                                     |
| creator      | email       | string | Email of the creator.                                                                                                                                    |
| creator      | handle      | string | Handle of the creator.                                                                                                                                   |
| creator      | name        | string | Name of the creator.                                                                                                                                     |
| attributes   | description | string | Description of the correction being made.                                                                                                                |
| attributes   | duration    | int64  | Length of time (in seconds) for a specified `rrule` recurring SLO correction.                                                                            |
| attributes   | end         | int64  | Ending time of the correction in epoch seconds.                                                                                                          |
| attributes   | modified_at | int64  | The epoch timestamp of when the correction was modified at.                                                                                              |
| attributes   | modifier    | object | Modifier of the object.                                                                                                                                  |
| modifier     | email       | string | Email of the Modifier.                                                                                                                                   |
| modifier     | handle      | string | Handle of the Modifier.                                                                                                                                  |
| modifier     | name        | string | Name of the Modifier.                                                                                                                                    |
| attributes   | rrule       | string | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`. |
| attributes   | slo_id      | string | ID of the SLO that this correction applies to.                                                                                                           |
| attributes   | start       | int64  | Starting time of the correction in epoch seconds.                                                                                                        |
| attributes   | timezone    | string | The timezone to display in the UI for the correction times (defaults to "UTC").                                                                          |
| data         | id          | string | The ID of the SLO correction.                                                                                                                            |
| data         | type        | enum   | SLO correction resource type. Allowed enum values: `correction`                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "category": "Scheduled Maintenance",
      "created_at": "integer",
      "creator": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "description": "string",
      "duration": 3600,
      "end": "integer",
      "modified_at": "integer",
      "modifier": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5",
      "slo_id": "string",
      "start": "integer",
      "timezone": "string"
    },
    "id": "string",
    "type": "correction"
  }
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
Forbidden
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
                  \# Path parametersexport slo_correction_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction/${slo_correction_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get an SLO correction for an SLO returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = environ["CORRECTION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.get_slo_correction(
        slo_correction_id=CORRECTION_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get an SLO correction for an SLO returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = ENV["CORRECTION_DATA_ID"]
p api_instance.get_slo_correction(CORRECTION_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get an SLO correction for an SLO returns "OK" response

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
    // there is a valid "correction" for "slo"
    CorrectionDataID := os.Getenv("CORRECTION_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewServiceLevelObjectiveCorrectionsApi(apiClient)
    resp, r, err := api.GetSLOCorrection(ctx, CorrectionDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectiveCorrectionsApi.GetSLOCorrection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectiveCorrectionsApi.GetSLOCorrection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get an SLO correction for an SLO returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectiveCorrectionsApi;
import com.datadog.api.client.v1.model.SLOCorrectionResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectiveCorrectionsApi apiInstance =
        new ServiceLevelObjectiveCorrectionsApi(defaultClient);

    // there is a valid "correction" for "slo"
    String CORRECTION_DATA_ID = System.getenv("CORRECTION_DATA_ID");

    try {
      SLOCorrectionResponse result = apiInstance.getSLOCorrection(CORRECTION_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceLevelObjectiveCorrectionsApi#getSLOCorrection");
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
// Get an SLO correction for an SLO returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objective_corrections::ServiceLevelObjectiveCorrectionsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "correction" for "slo"
    let correction_data_id = std::env::var("CORRECTION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectiveCorrectionsAPI::with_config(configuration);
    let resp = api.get_slo_correction(correction_data_id.clone()).await;
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
 * Get an SLO correction for an SLO returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectiveCorrectionsApi(configuration);

// there is a valid "correction" for "slo"
const CORRECTION_DATA_ID = process.env.CORRECTION_DATA_ID as string;

const params: v1.ServiceLevelObjectiveCorrectionsApiGetSLOCorrectionRequest = {
  sloCorrectionId: CORRECTION_DATA_ID,
};

apiInstance
  .getSLOCorrection(params)
  .then((data: v1.SLOCorrectionResponse) => {
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

## Update an SLO correction{% #update-an-slo-correction %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                  |
| ----------------- | ----------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v1/slo/correction/{slo_correction_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v1/slo/correction/{slo_correction_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v1/slo/correction/{slo_correction_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |

### Overview

Update the specified SLO correction object.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                          |
| ----------------------------------- | ------ | ------------------------------------ |
| slo_correction_id [*required*] | string | The ID of the SLO correction object. |

### Request

#### Body Data (required)

The edited SLO correction object.

{% tab title="Model" %}

| Parent field | Field       | Type   | Description                                                                                                                                              |
| ------------ | ----------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data        | object | The data object associated with the SLO correction to be updated.                                                                                        |
| data         | attributes  | object | The attribute object associated with the SLO correction to be updated.                                                                                   |
| attributes   | category    | enum   | Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`                             |
| attributes   | description | string | Description of the correction being made.                                                                                                                |
| attributes   | duration    | int64  | Length of time (in seconds) for a specified `rrule` recurring SLO correction.                                                                            |
| attributes   | end         | int64  | Ending time of the correction in epoch seconds.                                                                                                          |
| attributes   | rrule       | string | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`. |
| attributes   | start       | int64  | Starting time of the correction in epoch seconds.                                                                                                        |
| attributes   | timezone    | string | The timezone to display in the UI for the correction times (defaults to "UTC").                                                                          |
| data         | type        | enum   | SLO correction resource type. Allowed enum values: `correction`                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "category": "Deployment",
      "description": "Example-Service-Level-Objective-Correction",
      "end": 1636632671,
      "start": 1636629071,
      "timezone": "UTC"
    },
    "type": "correction"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object of an SLO correction.

| Parent field | Field       | Type   | Description                                                                                                                                              |
| ------------ | ----------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data        | object | The response object of a list of SLO corrections.                                                                                                        |
| data         | attributes  | object | The attribute object associated with the SLO correction.                                                                                                 |
| attributes   | category    | enum   | Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`                             |
| attributes   | created_at  | int64  | The epoch timestamp of when the correction was created at.                                                                                               |
| attributes   | creator     | object | Object describing the creator of the shared element.                                                                                                     |
| creator      | email       | string | Email of the creator.                                                                                                                                    |
| creator      | handle      | string | Handle of the creator.                                                                                                                                   |
| creator      | name        | string | Name of the creator.                                                                                                                                     |
| attributes   | description | string | Description of the correction being made.                                                                                                                |
| attributes   | duration    | int64  | Length of time (in seconds) for a specified `rrule` recurring SLO correction.                                                                            |
| attributes   | end         | int64  | Ending time of the correction in epoch seconds.                                                                                                          |
| attributes   | modified_at | int64  | The epoch timestamp of when the correction was modified at.                                                                                              |
| attributes   | modifier    | object | Modifier of the object.                                                                                                                                  |
| modifier     | email       | string | Email of the Modifier.                                                                                                                                   |
| modifier     | handle      | string | Handle of the Modifier.                                                                                                                                  |
| modifier     | name        | string | Name of the Modifier.                                                                                                                                    |
| attributes   | rrule       | string | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`. |
| attributes   | slo_id      | string | ID of the SLO that this correction applies to.                                                                                                           |
| attributes   | start       | int64  | Starting time of the correction in epoch seconds.                                                                                                        |
| attributes   | timezone    | string | The timezone to display in the UI for the correction times (defaults to "UTC").                                                                          |
| data         | id          | string | The ID of the SLO correction.                                                                                                                            |
| data         | type        | enum   | SLO correction resource type. Allowed enum values: `correction`                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "category": "Scheduled Maintenance",
      "created_at": "integer",
      "creator": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "description": "string",
      "duration": 3600,
      "end": "integer",
      "modified_at": "integer",
      "modifier": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5",
      "slo_id": "string",
      "start": "integer",
      "timezone": "string"
    },
    "id": "string",
    "type": "correction"
  }
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                          \# Path parametersexport slo_correction_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction/${slo_correction_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "category": "Deployment",
      "description": "Example-Service-Level-Objective-Correction",
      "end": 1636632671,
      "start": 1636629071,
      "timezone": "UTC"
    },
    "type": "correction"
  }
}
EOF

#####

```go
// Update an SLO correction returns "OK" response

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
    // there is a valid "correction" for "slo"
    CorrectionDataID := os.Getenv("CORRECTION_DATA_ID")

    body := datadogV1.SLOCorrectionUpdateRequest{
        Data: &datadogV1.SLOCorrectionUpdateData{
            Attributes: &datadogV1.SLOCorrectionUpdateRequestAttributes{
                Category:    datadogV1.SLOCORRECTIONCATEGORY_DEPLOYMENT.Ptr(),
                Description: datadog.PtrString("Example-Service-Level-Objective-Correction"),
                End:         datadog.PtrInt64(time.Now().Add(time.Hour * 1).Unix()),
                Start:       datadog.PtrInt64(time.Now().Unix()),
                Timezone:    datadog.PtrString("UTC"),
            },
            Type: datadogV1.SLOCORRECTIONTYPE_CORRECTION.Ptr(),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewServiceLevelObjectiveCorrectionsApi(apiClient)
    resp, r, err := api.UpdateSLOCorrection(ctx, CorrectionDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectiveCorrectionsApi.UpdateSLOCorrection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectiveCorrectionsApi.UpdateSLOCorrection`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update an SLO correction returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectiveCorrectionsApi;
import com.datadog.api.client.v1.model.SLOCorrectionCategory;
import com.datadog.api.client.v1.model.SLOCorrectionResponse;
import com.datadog.api.client.v1.model.SLOCorrectionType;
import com.datadog.api.client.v1.model.SLOCorrectionUpdateData;
import com.datadog.api.client.v1.model.SLOCorrectionUpdateRequest;
import com.datadog.api.client.v1.model.SLOCorrectionUpdateRequestAttributes;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectiveCorrectionsApi apiInstance =
        new ServiceLevelObjectiveCorrectionsApi(defaultClient);

    // there is a valid "correction" for "slo"
    String CORRECTION_DATA_ID = System.getenv("CORRECTION_DATA_ID");

    SLOCorrectionUpdateRequest body =
        new SLOCorrectionUpdateRequest()
            .data(
                new SLOCorrectionUpdateData()
                    .attributes(
                        new SLOCorrectionUpdateRequestAttributes()
                            .category(SLOCorrectionCategory.DEPLOYMENT)
                            .description("Example-Service-Level-Objective-Correction")
                            .end(OffsetDateTime.now().plusHours(1).toInstant().getEpochSecond())
                            .start(OffsetDateTime.now().toInstant().getEpochSecond())
                            .timezone("UTC"))
                    .type(SLOCorrectionType.CORRECTION));

    try {
      SLOCorrectionResponse result = apiInstance.updateSLOCorrection(CORRECTION_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceLevelObjectiveCorrectionsApi#updateSLOCorrection");
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
Update an SLO correction returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType
from datadog_api_client.v1.model.slo_correction_update_data import SLOCorrectionUpdateData
from datadog_api_client.v1.model.slo_correction_update_request import SLOCorrectionUpdateRequest
from datadog_api_client.v1.model.slo_correction_update_request_attributes import SLOCorrectionUpdateRequestAttributes

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = environ["CORRECTION_DATA_ID"]

body = SLOCorrectionUpdateRequest(
    data=SLOCorrectionUpdateData(
        attributes=SLOCorrectionUpdateRequestAttributes(
            category=SLOCorrectionCategory.DEPLOYMENT,
            description="Example-Service-Level-Objective-Correction",
            end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
            start=int(datetime.now().timestamp()),
            timezone="UTC",
        ),
        type=SLOCorrectionType.CORRECTION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.update_slo_correction(slo_correction_id=CORRECTION_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update an SLO correction returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = ENV["CORRECTION_DATA_ID"]

body = DatadogAPIClient::V1::SLOCorrectionUpdateRequest.new({
  data: DatadogAPIClient::V1::SLOCorrectionUpdateData.new({
    attributes: DatadogAPIClient::V1::SLOCorrectionUpdateRequestAttributes.new({
      category: DatadogAPIClient::V1::SLOCorrectionCategory::DEPLOYMENT,
      description: "Example-Service-Level-Objective-Correction",
      _end: (Time.now + 1 * 3600).to_i,
      start: Time.now.to_i,
      timezone: "UTC",
    }),
    type: DatadogAPIClient::V1::SLOCorrectionType::CORRECTION,
  }),
})
p api_instance.update_slo_correction(CORRECTION_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update an SLO correction returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objective_corrections::ServiceLevelObjectiveCorrectionsAPI;
use datadog_api_client::datadogV1::model::SLOCorrectionCategory;
use datadog_api_client::datadogV1::model::SLOCorrectionType;
use datadog_api_client::datadogV1::model::SLOCorrectionUpdateData;
use datadog_api_client::datadogV1::model::SLOCorrectionUpdateRequest;
use datadog_api_client::datadogV1::model::SLOCorrectionUpdateRequestAttributes;

#[tokio::main]
async fn main() {
    // there is a valid "correction" for "slo"
    let correction_data_id = std::env::var("CORRECTION_DATA_ID").unwrap();
    let body = SLOCorrectionUpdateRequest::new().data(
        SLOCorrectionUpdateData::new()
            .attributes(
                SLOCorrectionUpdateRequestAttributes::new()
                    .category(SLOCorrectionCategory::DEPLOYMENT)
                    .description("Example-Service-Level-Objective-Correction".to_string())
                    .end(1636632671)
                    .start(1636629071)
                    .timezone("UTC".to_string()),
            )
            .type_(SLOCorrectionType::CORRECTION),
    );
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectiveCorrectionsAPI::with_config(configuration);
    let resp = api
        .update_slo_correction(correction_data_id.clone(), body)
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
 * Update an SLO correction returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectiveCorrectionsApi(configuration);

// there is a valid "correction" for "slo"
const CORRECTION_DATA_ID = process.env.CORRECTION_DATA_ID as string;

const params: v1.ServiceLevelObjectiveCorrectionsApiUpdateSLOCorrectionRequest =
  {
    body: {
      data: {
        attributes: {
          category: "Deployment",
          description: "Example-Service-Level-Objective-Correction",
          end: Math.round(
            new Date(new Date().getTime() + 1 * 3600 * 1000).getTime() / 1000
          ),
          start: Math.round(new Date().getTime() / 1000),
          timezone: "UTC",
        },
        type: "correction",
      },
    },
    sloCorrectionId: CORRECTION_DATA_ID,
  };

apiInstance
  .updateSLOCorrection(params)
  .then((data: v1.SLOCorrectionResponse) => {
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

## Delete an SLO correction{% #delete-an-slo-correction %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/slo/correction/{slo_correction_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/slo/correction/{slo_correction_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/slo/correction/{slo_correction_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/slo/correction/{slo_correction_id} |

### Overview

Permanently delete the specified SLO correction object.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                          |
| ----------------------------------- | ------ | ------------------------------------ |
| slo_correction_id [*required*] | string | The ID of the SLO correction object. |

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="403" %}
Forbidden
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

{% tab title="404" %}
Not found
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
                  \# Path parametersexport slo_correction_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction/${slo_correction_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete an SLO correction returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    api_instance.delete_slo_correction(
        slo_correction_id="slo_correction_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete an SLO correction returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new
api_instance.delete_slo_correction("slo_correction_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete an SLO correction returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewServiceLevelObjectiveCorrectionsApi(apiClient)
    r, err := api.DeleteSLOCorrection(ctx, "slo_correction_id")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectiveCorrectionsApi.DeleteSLOCorrection`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete an SLO correction returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectiveCorrectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceLevelObjectiveCorrectionsApi apiInstance =
        new ServiceLevelObjectiveCorrectionsApi(defaultClient);

    try {
      apiInstance.deleteSLOCorrection("slo_correction_id");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceLevelObjectiveCorrectionsApi#deleteSLOCorrection");
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
// Delete an SLO correction returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objective_corrections::ServiceLevelObjectiveCorrectionsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceLevelObjectiveCorrectionsAPI::with_config(configuration);
    let resp = api
        .delete_slo_correction("slo_correction_id".to_string())
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
 * Delete an SLO correction returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectiveCorrectionsApi(configuration);

const params: v1.ServiceLevelObjectiveCorrectionsApiDeleteSLOCorrectionRequest =
  {
    sloCorrectionId: "slo_correction_id",
  };

apiInstance
  .deleteSLOCorrection(params)
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
