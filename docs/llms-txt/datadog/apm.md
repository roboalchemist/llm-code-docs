# Source: https://docs.datadoghq.com/api/latest/apm.md

---
title: APM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > APM
---

# APM

Observe, troubleshoot, and improve cloud-scale applications with all telemetry in context

## Get service list{% #get-service-list %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/apm/services |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/apm/services |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/apm/services      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/apm/services      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/apm/services     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/apm/services |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/apm/services |

### Overview



OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#apm) to access this endpoint.



### Arguments

#### Query Strings

| Name                          | Type   | Description                                                                                       |
| ----------------------------- | ------ | ------------------------------------------------------------------------------------------------- |
| filter[env] [*required*] | string | Filter services by environment. Can be set to `*` to return all services across all environments. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                       |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------- |
|              | data                   | object   |
| data         | attributes             | object   |
| attributes   | metadata               | [object] |
| metadata     | isTraced               | boolean  |
| metadata     | isUsm                  | boolean  |
| attributes   | services               | [string] |
| data         | id                     | string   |
| data         | type [*required*] | enum     | Services list resource type. Allowed enum values: `services_list` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "metadata": [
        {
          "isTraced": false,
          "isUsm": false
        }
      ],
      "services": []
    },
    "id": "string",
    "type": "services_list"
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
                  \# Required query argumentsexport filter[env]="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/services?filter[env]=${filter[env]}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get service list returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_api import APMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMApi(api_client)
    response = api_instance.get_service_list(
        filter_env="filter[env]",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get service list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMAPI.new
p api_instance.get_service_list("filter[env]")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get service list returns "OK" response

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
	api := datadogV2.NewAPMApi(apiClient)
	resp, r, err := api.GetServiceList(ctx, "filter[env]")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APMApi.GetServiceList`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APMApi.GetServiceList`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get service list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ApmApi;
import com.datadog.api.client.v2.model.ServiceList;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ApmApi apiInstance = new ApmApi(defaultClient);

    try {
      ServiceList result = apiInstance.getServiceList("filter[env]");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApmApi#getServiceList");
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
// Get service list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm::APMAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = APMAPI::with_config(configuration);
    let resp = api.get_service_list("filter[env]".to_string()).await;
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
 * Get service list returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMApi(configuration);

const params: v2.APMApiGetServiceListRequest = {
  filterEnv: "filter[env]",
};

apiInstance
  .getServiceList(params)
  .then((data: v2.ServiceList) => {
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
