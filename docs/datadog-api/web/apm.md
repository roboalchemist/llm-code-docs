# Source: https://docs.datadoghq.com/api/latest/apm

# APM
Observe, troubleshoot, and improve cloud-scale applications with all telemetry in context
## [Get service list](https://docs.datadoghq.com/api/latest/apm/#get-service-list)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/apm/#get-service-list-v2)


GET https://api.ap1.datadoghq.com/api/v2/apm/serviceshttps://api.ap2.datadoghq.com/api/v2/apm/serviceshttps://api.datadoghq.eu/api/v2/apm/serviceshttps://api.ddog-gov.com/api/v2/apm/serviceshttps://api.datadoghq.com/api/v2/apm/serviceshttps://api.us3.datadoghq.com/api/v2/apm/serviceshttps://api.us5.datadoghq.com/api/v2/apm/services
### Overview
OAuth apps require the `apm_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#apm) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/apm/#GetServiceList-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/apm/#GetServiceList-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/apm/)
  * [Example](https://docs.datadoghq.com/api/latest/apm/)


Field
Type
Description
data
object
attributes
object
metadata
[object]
isTraced
boolean
isUsm
boolean
services
[string]
id
string
type [_required_]
enum
Services list resource type. Allowed enum values: `services_list`
default: `services_list`
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/apm/)
  * [Example](https://docs.datadoghq.com/api/latest/apm/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/apm/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/apm/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/apm/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/apm/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/apm/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/apm/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/apm/?code-lang=typescript)


#####  Get service list
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/apm/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get service list
```
"""
Get service list returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_api import APMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMApi(api_client)
    response = api_instance.get_service_list()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get service list
```
# Get service list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::APMAPI.new
p api_instance.get_service_list()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get service list
```
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
	resp, r, err := api.GetServiceList(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APMApi.GetServiceList`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `APMApi.GetServiceList`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get service list
```
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
      ServiceList result = apiInstance.getServiceList();
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get service list
```
// Get service list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_apm::APMAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = APMAPI::with_config(configuration);
    let resp = api.get_service_list().await;
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

#####  Get service list
```
/**
 * Get service list returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.APMApi(configuration);

apiInstance
  .getServiceList()
  .then((data: v2.ServiceList) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6941c77a-407e-4ba9-83f0-fa5729676259&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=fcb0ae40-1271-469d-bf9b-028e294d8e41&pt=APM&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapm%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6941c77a-407e-4ba9-83f0-fa5729676259&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=fcb0ae40-1271-469d-bf9b-028e294d8e41&pt=APM&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapm%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=90881391-8e3d-40b1-b348-262a698fcec0&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=APM&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fapm%2F&r=&lt=11343&evt=pageLoad&sv=2&asc=G&cdb=AQAC&rn=103209)
