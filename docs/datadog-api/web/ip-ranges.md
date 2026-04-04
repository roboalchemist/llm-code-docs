# Source: https://docs.datadoghq.com/api/latest/ip-ranges/

# IP Ranges
Get a list of IP prefixes belonging to Datadog.
## [List IP Ranges](https://docs.datadoghq.com/api/latest/ip-ranges/#list-ip-ranges)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/ip-ranges/#list-ip-ranges-v1)


GET https://ip-ranges.ap1.datadoghq.com/https://ip-ranges.ap2.datadoghq.com/https://ip-ranges.datadoghq.eu/https://ip-ranges.ddog-gov.com/https://ip-ranges.datadoghq.com/https://ip-ranges.us3.datadoghq.com/https://ip-ranges.us5.datadoghq.com/
### Overview
Get information about Datadog IP ranges.
### Response
  * [200](https://docs.datadoghq.com/api/latest/ip-ranges/#GetIPRanges-200-v1)
  * [429](https://docs.datadoghq.com/api/latest/ip-ranges/#GetIPRanges-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/ip-ranges/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-ranges/)


IP ranges.
Field
Type
Description
agents
object
Available prefix information for the Agent endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
api
object
Available prefix information for the API endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
apm
object
Available prefix information for the APM endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
global
object
Available prefix information for all Datadog endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
logs
object
Available prefix information for the Logs endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
modified
string
Date when last updated, in the form `YYYY-MM-DD-hh-mm-ss`.
orchestrator
object
Available prefix information for the Orchestrator endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
process
object
Available prefix information for the Process endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
remote-configuration
object
Available prefix information for the Remote Configuration endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
synthetics
object
Available prefix information for the Synthetics endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv4_by_location
object
List of IPv4 prefixes by location.
<any-key>
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
prefixes_ipv6_by_location
object
List of IPv6 prefixes by location.
<any-key>
[string]
List of IPv6 prefixes.
synthetics-private-locations
object
Available prefix information for the Synthetics Private Locations endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
version
int64
Version of the IP list.
webhooks
object
Available prefix information for the Webhook endpoints.
prefixes_ipv4
[string]
List of IPv4 prefixes.
prefixes_ipv6
[string]
List of IPv6 prefixes.
```
{
  "agents": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "api": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "apm": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "global": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "logs": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "modified": "2019-10-31-20-00-00",
  "orchestrator": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "process": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "remote-configuration": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "synthetics": {
    "prefixes_ipv4": [],
    "prefixes_ipv4_by_location": {
      "<any-key>": []
    },
    "prefixes_ipv6": [],
    "prefixes_ipv6_by_location": {
      "<any-key>": []
    }
  },
  "synthetics-private-locations": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  },
  "version": 11,
  "webhooks": {
    "prefixes_ipv4": [],
    "prefixes_ipv6": []
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/ip-ranges/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-ranges/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/ip-ranges/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/ip-ranges/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/ip-ranges/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/ip-ranges/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/ip-ranges/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/ip-ranges/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/ip-ranges/?code-lang=typescript)


#####  List IP Ranges
Copy
```
                  # Curl command  
curl -X GET "https://ip-ranges.ap1.datadoghq.com"https://ip-ranges.ap2.datadoghq.com"https://ip-ranges.datadoghq.eu"https://ip-ranges.ddog-gov.com"https://ip-ranges.datadoghq.com"https://ip-ranges.us3.datadoghq.com"https://ip-ranges.us5.datadoghq.com/" \
-H "Accept: application/json"  

                
```

#####  List IP Ranges
```
"""
List IP Ranges returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.ip_ranges_api import IPRangesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IPRangesApi(api_client)
    response = api_instance.get_ip_ranges()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" python3 "example.py"


```

#####  List IP Ranges
```
# List IP Ranges returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::IPRangesAPI.new
p api_instance.get_ip_ranges()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" rb "example.rb"


```

#####  List IP Ranges
```
// List IP Ranges returns "OK" response

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
	api := datadogV1.NewIPRangesApi(apiClient)
	resp, r, err := api.GetIPRanges(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IPRangesApi.GetIPRanges`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IPRangesApi.GetIPRanges`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" go run "main.go"


```

#####  List IP Ranges
```
// List IP Ranges returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.IpRangesApi;
import com.datadog.api.client.v1.model.IPRanges;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    IpRangesApi apiInstance = new IpRangesApi(defaultClient);

    try {
      IPRanges result = apiInstance.getIPRanges();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpRangesApi#getIPRanges");
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" java "Example.java"


```

#####  List IP Ranges
```
// List IP Ranges returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_ip_ranges::IPRangesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = IPRangesAPI::with_config(configuration);
    let resp = api.get_ip_ranges().await;
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" cargo run


```

#####  List IP Ranges
```
/**
 * List IP Ranges returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.IPRangesApi(configuration);

apiInstance
  .getIPRanges()
  .then((data: v1.IPRanges) => {
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=165a87e1-922a-4b1f-9e3c-f8cb92880f42&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=cfc80acf-2cb7-4e74-8c86-c1505102f113&pt=IP%20Ranges&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fip-ranges%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=165a87e1-922a-4b1f-9e3c-f8cb92880f42&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=cfc80acf-2cb7-4e74-8c86-c1505102f113&pt=IP%20Ranges&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fip-ranges%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=9ac8729a-978b-42b6-b5ad-25f35e8ef79a&bo=2&sid=ba46b8a0f0bf11f08761a3199a385bde&vid=ba46dde0f0bf11f0b26b6ba9935020b6&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=IP%20Ranges&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fip-ranges%2F&r=&lt=1047&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=944965)
