# Source: https://docs.datadoghq.com/api/latest/service-checks.md

---
title: Service Checks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Service Checks
---

# Service Checks

The service check endpoint allows you to post check statuses for use with monitors. Service check messages are limited to 500 characters. If a check is posted with a message containing more than 500 characters, only the first 500 characters are displayed. Messages are limited for checks with a Critical or Warning status, they are dropped for checks with an OK status.

- [Read more about Service Check monitors](https://docs.datadoghq.com/monitors/types/service_check/).
- [Read more about Process Check monitors](https://docs.datadoghq.com/monitors/create/types/process_check/?tab=checkalert).
- [Read more about Network monitors](https://docs.datadoghq.com/monitors/create/types/network/?tab=checkalert).
- [Read more about Custom Check monitors](https://docs.datadoghq.com/monitors/create/types/custom_check/?tab=checkalert).
- [Read more about Service Checks and status codes](https://docs.datadoghq.com/developers/service_checks/).

## Submit a Service Check{% #submit-a-service-check %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/check_run |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/check_run |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/check_run      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/check_run      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/check_run     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/check_run |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/check_run |

### Overview



Submit a list of Service Checks.

**Notes**:

- A valid API key is required.
- Service checks can be submitted up to 10 minutes in the past.



### Request

#### Body Data (required)

Service Check request body.

{% tab title="Model" %}

| Field     | Type     | Description                                                                                                                              |
| --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| check     | string   | The check.                                                                                                                               |
| host_name | string   | The host name correlated with the check.                                                                                                 |
| message   | string   | Message containing check status.                                                                                                         |
| status    | enum     | The status of a service check. Set to `0` for OK, `1` for warning, `2` for critical, and `3` for unknown. Allowed enum values: `0,1,2,3` |
| tags      | [string] | Tags related to a check.                                                                                                                 |
| timestamp | int64    | Time of check.                                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
[
  {
    "check": "app.ok",
    "host_name": "host",
    "status": 0,
    "tags": [
      "test:ExampleServiceCheck"
    ]
  }
]
```

{% /tab %}

### Response

{% tab title="202" %}
Payload accepted
{% tab title="Model" %}
The payload accepted for intake.

| Field  | Type   | Description                       |
| ------ | ------ | --------------------------------- |
| status | string | The status of the intake payload. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "status": "ok"
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

{% tab title="408" %}
Request timeout
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

{% tab title="413" %}
Payload too large
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/check_run" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
[
  {
    "check": "app.ok",
    "host_name": "host",
    "status": 0,
    "tags": [
      "test:ExampleServiceCheck"
    ]
  }
]
EOF
                        
##### 

```go
// Submit a Service Check returns "Payload accepted" response

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
	body := []datadogV1.ServiceCheck{
		{
			Check:    "app.ok",
			HostName: "host",
			Status:   datadogV1.SERVICECHECKSTATUS_OK,
			Tags: []string{
				"test:ExampleServiceCheck",
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewServiceChecksApi(apiClient)
	resp, r, err := api.SubmitServiceCheck(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ServiceChecksApi.SubmitServiceCheck`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ServiceChecksApi.SubmitServiceCheck`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
##### 

```java
// Submit a Service Check returns "Payload accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceChecksApi;
import com.datadog.api.client.v1.model.IntakePayloadAccepted;
import com.datadog.api.client.v1.model.ServiceCheck;
import com.datadog.api.client.v1.model.ServiceCheckStatus;
import java.util.Collections;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceChecksApi apiInstance = new ServiceChecksApi(defaultClient);

    List<ServiceCheck> body =
        Collections.singletonList(
            new ServiceCheck()
                .check("app.ok")
                .hostName("host")
                .status(ServiceCheckStatus.OK)
                .tags(Collections.singletonList("test:ExampleServiceCheck")));

    try {
      IntakePayloadAccepted result = apiInstance.submitServiceCheck(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceChecksApi#submitServiceCheck");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
##### 

```python
from datadog import initialize, api
from datadog.api.constants import CheckStatus

options = {'api_key': '<DATADOG_API_KEY>',
           'app_key': '<DATADOG_APPLICATION_KEY>'}

initialize(**options)

check = 'app.ok'
host = 'app1'
status = CheckStatus.OK  # equals 0
tags = ['env:test']

api.ServiceCheck.check(check=check, host_name=host, status=status, message='Response: 200 OK', tags=tags)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python "example.py"
##### 

```python
"""
Submit a Service Check returns "Payload accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_checks_api import ServiceChecksApi
from datadog_api_client.v1.model.service_check import ServiceCheck
from datadog_api_client.v1.model.service_check_status import ServiceCheckStatus
from datadog_api_client.v1.model.service_checks import ServiceChecks

body = ServiceChecks(
    [
        ServiceCheck(
            check="app.ok",
            host_name="host",
            status=ServiceCheckStatus.OK,
            tags=[
                "test:ExampleServiceCheck",
            ],
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceChecksApi(api_client)
    response = api_instance.submit_service_check(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# submitting a check doesn't require an app_key
dog = Dogapi::Client.new(api_key)

dog.service_check('app.is_ok', 'app1', 0, :message => 'Response: 200 OK', :tags => ['env:test'])
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```ruby
# Submit a Service Check returns "Payload accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceChecksAPI.new

body = [
  DatadogAPIClient::V1::ServiceCheck.new({
    check: "app.ok",
    host_name: "host",
    status: DatadogAPIClient::V1::ServiceCheckStatus::OK,
    tags: [
      "test:ExampleServiceCheck",
    ],
  }),
]
p api_instance.submit_service_check(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```rust
// Submit a Service Check returns "Payload accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_checks::ServiceChecksAPI;
use datadog_api_client::datadogV1::model::ServiceCheck;
use datadog_api_client::datadogV1::model::ServiceCheckStatus;

#[tokio::main]
async fn main() {
    let body = vec![ServiceCheck::new(
        "app.ok".to_string(),
        "host".to_string(),
        ServiceCheckStatus::OK,
        vec!["test:ExampleServiceCheck".to_string()],
    )];
    let configuration = datadog::Configuration::new();
    let api = ServiceChecksAPI::with_config(configuration);
    let resp = api.submit_service_check(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
##### 

```typescript
/**
 * Submit a Service Check returns "Payload accepted" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceChecksApi(configuration);

const params: v1.ServiceChecksApiSubmitServiceCheckRequest = {
  body: [
    {
      check: "app.ok",
      hostName: "host",
      status: 0,
      tags: ["test:ExampleServiceCheck"],
    },
  ],
};

apiInstance
  .submitServiceCheck(params)
  .then((data: v1.IntakePayloadAccepted) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}
