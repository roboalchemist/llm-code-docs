# Source: https://docs.datadoghq.com/api/latest/service-level-objective-corrections

# Service Level Objective Corrections
SLO Status Corrections allow you to prevent specific time periods from negatively impacting your SLO’s status and error budget. You can use Status Corrections for various purposes, such as removing planned maintenance windows, non-business hours, or other time periods that do not correspond to genuine issues. See [SLO status corrections](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-status-corrections) for more information.
## [Create an SLO correction](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#create-an-slo-correction)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#create-an-slo-correction-v1)


POST https://api.ap1.datadoghq.com/api/v1/slo/correctionhttps://api.ap2.datadoghq.com/api/v1/slo/correctionhttps://api.datadoghq.eu/api/v1/slo/correctionhttps://api.ddog-gov.com/api/v1/slo/correctionhttps://api.datadoghq.com/api/v1/slo/correctionhttps://api.us3.datadoghq.com/api/v1/slo/correctionhttps://api.us5.datadoghq.com/api/v1/slo/correction
### Overview
Create an SLO Correction. This endpoint requires the `slos_corrections` permission.
OAuth apps require the `slos_corrections` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objective-corrections) to access this endpoint.
### Request
#### Body Data (required)
Create an SLO Correction
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


Field
Type
Description
data
object
The data object associated with the SLO correction to be created.
attributes
object
The attribute object associated with the SLO correction to be created.
category [_required_]
enum
Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`
description
string
Description of the correction being made.
duration
int64
Length of time (in seconds) for a specified `rrule` recurring SLO correction.
end
int64
Ending time of the correction in epoch seconds.
rrule
string
The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`.
slo_id [_required_]
string
ID of the SLO that this correction applies to.
start [_required_]
int64
Starting time of the correction in epoch seconds.
timezone
string
The timezone to display in the UI for the correction times (defaults to "UTC").
type [_required_]
enum
SLO correction resource type. Allowed enum values: `correction`
default: `correction`
#####  Create an SLO correction returns "OK" response
```
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

Copy
#####  Create an SLO correction with rrule returns "OK" response
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#CreateSLOCorrection-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#CreateSLOCorrection-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#CreateSLOCorrection-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#CreateSLOCorrection-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#CreateSLOCorrection-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


The response object of an SLO correction.
Field
Type
Description
data
object
The response object of a list of SLO corrections.
attributes
object
The attribute object associated with the SLO correction.
category
enum
Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`
created_at
int64
The epoch timestamp of when the correction was created at.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
Description of the correction being made.
duration
int64
Length of time (in seconds) for a specified `rrule` recurring SLO correction.
end
int64
Ending time of the correction in epoch seconds.
modified_at
int64
The epoch timestamp of when the correction was modified at.
modifier
object
Modifier of the object.
email
string
Email of the Modifier.
handle
string
Handle of the Modifier.
name
string
Name of the Modifier.
rrule
string
The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`.
slo_id
string
ID of the SLO that this correction applies to.
start
int64
Starting time of the correction in epoch seconds.
timezone
string
The timezone to display in the UI for the correction times (defaults to "UTC").
id
string
The ID of the SLO correction.
type
enum
SLO correction resource type. Allowed enum values: `correction`
default: `correction`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
SLO Not Found
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=typescript)


#####  Create an SLO correction returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction" \
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

                        
```

#####  Create an SLO correction with rrule returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction" \
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

                        
```

#####  Create an SLO correction returns "OK" response 
```
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

Copy
#####  Create an SLO correction with rrule returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create an SLO correction returns "OK" response 
```
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

Copy
#####  Create an SLO correction with rrule returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create an SLO correction returns "OK" response 
```
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

Copy
#####  Create an SLO correction with rrule returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create an SLO correction returns "OK" response 
```
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

Copy
#####  Create an SLO correction with rrule returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create an SLO correction returns "OK" response 
```
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

Copy
#####  Create an SLO correction with rrule returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create an SLO correction returns "OK" response 
```
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

Copy
#####  Create an SLO correction with rrule returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get all SLO corrections](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#get-all-slo-corrections)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#get-all-slo-corrections-v1)


GET https://api.ap1.datadoghq.com/api/v1/slo/correctionhttps://api.ap2.datadoghq.com/api/v1/slo/correctionhttps://api.datadoghq.eu/api/v1/slo/correctionhttps://api.ddog-gov.com/api/v1/slo/correctionhttps://api.datadoghq.com/api/v1/slo/correctionhttps://api.us3.datadoghq.com/api/v1/slo/correctionhttps://api.us5.datadoghq.com/api/v1/slo/correction
### Overview
Get all Service Level Objective corrections. This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objective-corrections) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
offset
integer
The specific offset to use as the beginning of the returned response.
limit
integer
The number of SLO corrections to return in the response. Default is 25.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#ListSLOCorrection-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#ListSLOCorrection-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#ListSLOCorrection-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


A list of SLO correction objects.
Field
Type
Description
data
[object]
The list of SLO corrections objects.
attributes
object
The attribute object associated with the SLO correction.
category
enum
Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`
created_at
int64
The epoch timestamp of when the correction was created at.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
Description of the correction being made.
duration
int64
Length of time (in seconds) for a specified `rrule` recurring SLO correction.
end
int64
Ending time of the correction in epoch seconds.
modified_at
int64
The epoch timestamp of when the correction was modified at.
modifier
object
Modifier of the object.
email
string
Email of the Modifier.
handle
string
Handle of the Modifier.
name
string
Name of the Modifier.
rrule
string
The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`.
slo_id
string
ID of the SLO that this correction applies to.
start
int64
Starting time of the correction in epoch seconds.
timezone
string
The timezone to display in the UI for the correction times (defaults to "UTC").
id
string
The ID of the SLO correction.
type
enum
SLO correction resource type. Allowed enum values: `correction`
default: `correction`
meta
object
Object describing meta attributes of response.
page
object
Pagination object.
total_count
int64
Total count.
total_filtered_count
int64
Total count of elements matched by the filter.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=typescript)


#####  Get all SLO corrections
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all SLO corrections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all SLO corrections
```
# Get all SLO corrections returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new
opts = {
  offset: 1,
  limit: 1,
}
p api_instance.list_slo_correction(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all SLO corrections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all SLO corrections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get all SLO corrections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get all SLO corrections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get an SLO correction for an SLO](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#get-an-slo-correction-for-an-slo)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#get-an-slo-correction-for-an-slo-v1)


GET https://api.ap1.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.ap2.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.datadoghq.eu/api/v1/slo/correction/{slo_correction_id}https://api.ddog-gov.com/api/v1/slo/correction/{slo_correction_id}https://api.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.us3.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.us5.datadoghq.com/api/v1/slo/correction/{slo_correction_id}
### Overview
Get an SLO correction.
### Arguments
#### Path Parameters
Name
Type
Description
slo_correction_id [_required_]
string
The ID of the SLO correction object.
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#GetSLOCorrection-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#GetSLOCorrection-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#GetSLOCorrection-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#GetSLOCorrection-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


The response object of an SLO correction.
Field
Type
Description
data
object
The response object of a list of SLO corrections.
attributes
object
The attribute object associated with the SLO correction.
category
enum
Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`
created_at
int64
The epoch timestamp of when the correction was created at.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
Description of the correction being made.
duration
int64
Length of time (in seconds) for a specified `rrule` recurring SLO correction.
end
int64
Ending time of the correction in epoch seconds.
modified_at
int64
The epoch timestamp of when the correction was modified at.
modifier
object
Modifier of the object.
email
string
Email of the Modifier.
handle
string
Handle of the Modifier.
name
string
Name of the Modifier.
rrule
string
The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`.
slo_id
string
ID of the SLO that this correction applies to.
start
int64
Starting time of the correction in epoch seconds.
timezone
string
The timezone to display in the UI for the correction times (defaults to "UTC").
id
string
The ID of the SLO correction.
type
enum
SLO correction resource type. Allowed enum values: `correction`
default: `correction`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=typescript)


#####  Get an SLO correction for an SLO
Copy
```
                  # Path parameters  
export slo_correction_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction/${slo_correction_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get an SLO correction for an SLO
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get an SLO correction for an SLO
```
# Get an SLO correction for an SLO returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = ENV["CORRECTION_DATA_ID"]
p api_instance.get_slo_correction(CORRECTION_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get an SLO correction for an SLO
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get an SLO correction for an SLO
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get an SLO correction for an SLO
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get an SLO correction for an SLO
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update an SLO correction](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#update-an-slo-correction)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#update-an-slo-correction-v1)


PATCH https://api.ap1.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.ap2.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.datadoghq.eu/api/v1/slo/correction/{slo_correction_id}https://api.ddog-gov.com/api/v1/slo/correction/{slo_correction_id}https://api.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.us3.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.us5.datadoghq.com/api/v1/slo/correction/{slo_correction_id}
### Overview
Update the specified SLO correction object.
### Arguments
#### Path Parameters
Name
Type
Description
slo_correction_id [_required_]
string
The ID of the SLO correction object.
### Request
#### Body Data (required)
The edited SLO correction object.
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


Field
Type
Description
data
object
The data object associated with the SLO correction to be updated.
attributes
object
The attribute object associated with the SLO correction to be updated.
category
enum
Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`
description
string
Description of the correction being made.
duration
int64
Length of time (in seconds) for a specified `rrule` recurring SLO correction.
end
int64
Ending time of the correction in epoch seconds.
rrule
string
The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`.
start
int64
Starting time of the correction in epoch seconds.
timezone
string
The timezone to display in the UI for the correction times (defaults to "UTC").
type
enum
SLO correction resource type. Allowed enum values: `correction`
default: `correction`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#UpdateSLOCorrection-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#UpdateSLOCorrection-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#UpdateSLOCorrection-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#UpdateSLOCorrection-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#UpdateSLOCorrection-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


The response object of an SLO correction.
Field
Type
Description
data
object
The response object of a list of SLO corrections.
attributes
object
The attribute object associated with the SLO correction.
category
enum
Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`
created_at
int64
The epoch timestamp of when the correction was created at.
creator
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
description
string
Description of the correction being made.
duration
int64
Length of time (in seconds) for a specified `rrule` recurring SLO correction.
end
int64
Ending time of the correction in epoch seconds.
modified_at
int64
The epoch timestamp of when the correction was modified at.
modifier
object
Modifier of the object.
email
string
Email of the Modifier.
handle
string
Handle of the Modifier.
name
string
Name of the Modifier.
rrule
string
The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`.
slo_id
string
ID of the SLO that this correction applies to.
start
int64
Starting time of the correction in epoch seconds.
timezone
string
The timezone to display in the UI for the correction times (defaults to "UTC").
id
string
The ID of the SLO correction.
type
enum
SLO correction resource type. Allowed enum values: `correction`
default: `correction`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=typescript)


#####  Update an SLO correction returns "OK" response
Copy
```
                          # Path parameters  
export slo_correction_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction/${slo_correction_id}" \
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

                        
```

#####  Update an SLO correction returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update an SLO correction returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update an SLO correction returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update an SLO correction returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update an SLO correction returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update an SLO correction returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete an SLO correction](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#delete-an-slo-correction)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#delete-an-slo-correction-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.ap2.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.datadoghq.eu/api/v1/slo/correction/{slo_correction_id}https://api.ddog-gov.com/api/v1/slo/correction/{slo_correction_id}https://api.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.us3.datadoghq.com/api/v1/slo/correction/{slo_correction_id}https://api.us5.datadoghq.com/api/v1/slo/correction/{slo_correction_id}
### Overview
Permanently delete the specified SLO correction object.
### Arguments
#### Path Parameters
Name
Type
Description
slo_correction_id [_required_]
string
The ID of the SLO correction object.
### Response
  * [204](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#DeleteSLOCorrection-204-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#DeleteSLOCorrection-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#DeleteSLOCorrection-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#DeleteSLOCorrection-429-v1)


OK
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
Not found
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Model](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)
  * [Example](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/?code-lang=typescript)


#####  Delete an SLO correction
Copy
```
                  # Path parameters  
export slo_correction_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/correction/${slo_correction_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete an SLO correction
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete an SLO correction
```
# Delete an SLO correction returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectiveCorrectionsAPI.new
api_instance.delete_slo_correction("slo_correction_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete an SLO correction
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete an SLO correction
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete an SLO correction
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete an SLO correction
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=53e74415-c067-46ce-b980-e700b0b104f7&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=15df1f91-205c-4a5f-bd05-7b4f3bb87e5c&pt=Service%20Level%20Objective%20Corrections&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-level-objective-corrections%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=53e74415-c067-46ce-b980-e700b0b104f7&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=15df1f91-205c-4a5f-bd05-7b4f3bb87e5c&pt=Service%20Level%20Objective%20Corrections&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-level-objective-corrections%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=e3a147f8-9029-422c-94a7-f43d56d384f8&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Service%20Level%20Objective%20Corrections&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-level-objective-corrections%2F&r=&lt=11045&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=872927)
