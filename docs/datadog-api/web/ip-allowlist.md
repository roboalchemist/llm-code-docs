# Source: https://docs.datadoghq.com/api/latest/ip-allowlist

# IP Allowlist
The IP allowlist API is used to manage the IP addresses that can access the Datadog API and web UI. It does not block access to intake APIs or public dashboards.
This is an enterprise-only feature. Request access by contacting Datadog support, or see the [IP Allowlist page](https://docs.datadoghq.com/account_management/org_settings/ip_allowlist/) for more information.
## [Get IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#get-ip-allowlist)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/ip-allowlist/#get-ip-allowlist-v2)


GET https://api.ap1.datadoghq.com/api/v2/ip_allowlisthttps://api.ap2.datadoghq.com/api/v2/ip_allowlisthttps://api.datadoghq.eu/api/v2/ip_allowlisthttps://api.ddog-gov.com/api/v2/ip_allowlisthttps://api.datadoghq.com/api/v2/ip_allowlisthttps://api.us3.datadoghq.com/api/v2/ip_allowlisthttps://api.us5.datadoghq.com/api/v2/ip_allowlist
### Overview
Returns the IP allowlist and its enabled or disabled state. This endpoint requires the `org_management` permission.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ip-allowlist) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/ip-allowlist/#GetIPAllowlist-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/ip-allowlist/#GetIPAllowlist-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/ip-allowlist/#GetIPAllowlist-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/ip-allowlist/#GetIPAllowlist-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


Response containing information about the IP allowlist.
Field
Type
Description
data
object
IP allowlist data.
attributes
object
Attributes of the IP allowlist.
enabled
boolean
Whether the IP allowlist logic is enabled or not.
entries
[object]
Array of entries in the IP allowlist.
data [_required_]
object
Data of the IP allowlist entry object.
attributes
object
Attributes of the IP allowlist entry.
cidr_block
string
The CIDR block describing the IP range of the entry.
created_at
date-time
Creation time of the entry.
modified_at
date-time
Time of last entry modification.
note
string
A note describing the IP allowlist entry.
id
string
The unique identifier of the IP allowlist entry.
type [_required_]
enum
IP allowlist Entry type. Allowed enum values: `ip_allowlist_entry`
default: `ip_allowlist_entry`
id
string
The unique identifier of the org.
type [_required_]
enum
IP allowlist type. Allowed enum values: `ip_allowlist`
default: `ip_allowlist`
```
{
  "data": {
    "attributes": {
      "enabled": false,
      "entries": [
        {
          "data": {
            "attributes": {
              "cidr_block": "string",
              "created_at": "2019-09-19T10:00:00.000Z",
              "modified_at": "2019-09-19T10:00:00.000Z",
              "note": "string"
            },
            "id": "string",
            "type": "ip_allowlist_entry"
          }
        }
      ]
    },
    "id": "string",
    "type": "ip_allowlist"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


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
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=typescript)


#####  Get IP Allowlist
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ip_allowlist" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get IP Allowlist
```
"""
Get IP Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ip_allowlist_api import IPAllowlistApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IPAllowlistApi(api_client)
    response = api_instance.get_ip_allowlist()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get IP Allowlist
```
# Get IP Allowlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::IPAllowlistAPI.new
p api_instance.get_ip_allowlist()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get IP Allowlist
```
// Get IP Allowlist returns "OK" response

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
	api := datadogV2.NewIPAllowlistApi(apiClient)
	resp, r, err := api.GetIPAllowlist(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IPAllowlistApi.GetIPAllowlist`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IPAllowlistApi.GetIPAllowlist`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get IP Allowlist
```
// Get IP Allowlist returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IpAllowlistApi;
import com.datadog.api.client.v2.model.IPAllowlistResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    IpAllowlistApi apiInstance = new IpAllowlistApi(defaultClient);

    try {
      IPAllowlistResponse result = apiInstance.getIPAllowlist();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpAllowlistApi#getIPAllowlist");
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

#####  Get IP Allowlist
```
// Get IP Allowlist returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ip_allowlist::IPAllowlistAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = IPAllowlistAPI::with_config(configuration);
    let resp = api.get_ip_allowlist().await;
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

#####  Get IP Allowlist
```
/**
 * Get IP Allowlist returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.IPAllowlistApi(configuration);

apiInstance
  .getIPAllowlist()
  .then((data: v2.IPAllowlistResponse) => {
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
## [Update IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#update-ip-allowlist)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/ip-allowlist/#update-ip-allowlist-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/ip_allowlisthttps://api.ap2.datadoghq.com/api/v2/ip_allowlisthttps://api.datadoghq.eu/api/v2/ip_allowlisthttps://api.ddog-gov.com/api/v2/ip_allowlisthttps://api.datadoghq.com/api/v2/ip_allowlisthttps://api.us3.datadoghq.com/api/v2/ip_allowlisthttps://api.us5.datadoghq.com/api/v2/ip_allowlist
### Overview
Edit the entries in the IP allowlist, and enable or disable it. This endpoint requires the `org_management` permission.
OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ip-allowlist) to access this endpoint.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


Field
Type
Description
data [_required_]
object
IP allowlist data.
attributes
object
Attributes of the IP allowlist.
enabled
boolean
Whether the IP allowlist logic is enabled or not.
entries
[object]
Array of entries in the IP allowlist.
data [_required_]
object
Data of the IP allowlist entry object.
attributes
object
Attributes of the IP allowlist entry.
cidr_block
string
The CIDR block describing the IP range of the entry.
created_at
date-time
Creation time of the entry.
modified_at
date-time
Time of last entry modification.
note
string
A note describing the IP allowlist entry.
id
string
The unique identifier of the IP allowlist entry.
type [_required_]
enum
IP allowlist Entry type. Allowed enum values: `ip_allowlist_entry`
default: `ip_allowlist_entry`
id
string
The unique identifier of the org.
type [_required_]
enum
IP allowlist type. Allowed enum values: `ip_allowlist`
default: `ip_allowlist`
```
{
  "data": {
    "attributes": {
      "entries": [
        {
          "data": {
            "attributes": {
              "note": "Example-IP-Allowlist",
              "cidr_block": "127.0.0.1"
            },
            "type": "ip_allowlist_entry"
          }
        }
      ],
      "enabled": false
    },
    "type": "ip_allowlist"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/ip-allowlist/#UpdateIPAllowlist-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/ip-allowlist/#UpdateIPAllowlist-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/ip-allowlist/#UpdateIPAllowlist-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/ip-allowlist/#UpdateIPAllowlist-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/ip-allowlist/#UpdateIPAllowlist-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


Response containing information about the IP allowlist.
Field
Type
Description
data
object
IP allowlist data.
attributes
object
Attributes of the IP allowlist.
enabled
boolean
Whether the IP allowlist logic is enabled or not.
entries
[object]
Array of entries in the IP allowlist.
data [_required_]
object
Data of the IP allowlist entry object.
attributes
object
Attributes of the IP allowlist entry.
cidr_block
string
The CIDR block describing the IP range of the entry.
created_at
date-time
Creation time of the entry.
modified_at
date-time
Time of last entry modification.
note
string
A note describing the IP allowlist entry.
id
string
The unique identifier of the IP allowlist entry.
type [_required_]
enum
IP allowlist Entry type. Allowed enum values: `ip_allowlist_entry`
default: `ip_allowlist_entry`
id
string
The unique identifier of the org.
type [_required_]
enum
IP allowlist type. Allowed enum values: `ip_allowlist`
default: `ip_allowlist`
```
{
  "data": {
    "attributes": {
      "enabled": false,
      "entries": [
        {
          "data": {
            "attributes": {
              "cidr_block": "string",
              "created_at": "2019-09-19T10:00:00.000Z",
              "modified_at": "2019-09-19T10:00:00.000Z",
              "note": "string"
            },
            "id": "string",
            "type": "ip_allowlist_entry"
          }
        }
      ]
    },
    "id": "string",
    "type": "ip_allowlist"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


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
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


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
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/ip-allowlist/)
  * [Example](https://docs.datadoghq.com/api/latest/ip-allowlist/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/ip-allowlist/?code-lang=typescript)


#####  Update IP Allowlist returns "OK" response
Copy
```
                          # Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ip_allowlist" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "entries": [
        {
          "data": {
            "attributes": {
              "note": "Example-IP-Allowlist",
              "cidr_block": "127.0.0.1"
            },
            "type": "ip_allowlist_entry"
          }
        }
      ],
      "enabled": false
    },
    "type": "ip_allowlist"
  }
}
EOF  

                        
```

#####  Update IP Allowlist returns "OK" response
```
// Update IP Allowlist returns "OK" response

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
	body := datadogV2.IPAllowlistUpdateRequest{
		Data: datadogV2.IPAllowlistData{
			Attributes: &datadogV2.IPAllowlistAttributes{
				Entries: []datadogV2.IPAllowlistEntry{
					{
						Data: datadogV2.IPAllowlistEntryData{
							Attributes: &datadogV2.IPAllowlistEntryAttributes{
								Note:      datadog.PtrString("Example-IP-Allowlist"),
								CidrBlock: datadog.PtrString("127.0.0.1"),
							},
							Type: datadogV2.IPALLOWLISTENTRYTYPE_IP_ALLOWLIST_ENTRY,
						},
					},
				},
				Enabled: datadog.PtrBool(false),
			},
			Type: datadogV2.IPALLOWLISTTYPE_IP_ALLOWLIST,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewIPAllowlistApi(apiClient)
	resp, r, err := api.UpdateIPAllowlist(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `IPAllowlistApi.UpdateIPAllowlist`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `IPAllowlistApi.UpdateIPAllowlist`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update IP Allowlist returns "OK" response
```
// Update IP Allowlist returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IpAllowlistApi;
import com.datadog.api.client.v2.model.IPAllowlistAttributes;
import com.datadog.api.client.v2.model.IPAllowlistData;
import com.datadog.api.client.v2.model.IPAllowlistEntry;
import com.datadog.api.client.v2.model.IPAllowlistEntryAttributes;
import com.datadog.api.client.v2.model.IPAllowlistEntryData;
import com.datadog.api.client.v2.model.IPAllowlistEntryType;
import com.datadog.api.client.v2.model.IPAllowlistResponse;
import com.datadog.api.client.v2.model.IPAllowlistType;
import com.datadog.api.client.v2.model.IPAllowlistUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    IpAllowlistApi apiInstance = new IpAllowlistApi(defaultClient);

    IPAllowlistUpdateRequest body =
        new IPAllowlistUpdateRequest()
            .data(
                new IPAllowlistData()
                    .attributes(
                        new IPAllowlistAttributes()
                            .entries(
                                Collections.singletonList(
                                    new IPAllowlistEntry()
                                        .data(
                                            new IPAllowlistEntryData()
                                                .attributes(
                                                    new IPAllowlistEntryAttributes()
                                                        .note("Example-IP-Allowlist")
                                                        .cidrBlock("127.0.0.1"))
                                                .type(IPAllowlistEntryType.IP_ALLOWLIST_ENTRY))))
                            .enabled(false))
                    .type(IPAllowlistType.IP_ALLOWLIST));

    try {
      IPAllowlistResponse result = apiInstance.updateIPAllowlist(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpAllowlistApi#updateIPAllowlist");
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

#####  Update IP Allowlist returns "OK" response
```
"""
Update IP Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ip_allowlist_api import IPAllowlistApi
from datadog_api_client.v2.model.ip_allowlist_attributes import IPAllowlistAttributes
from datadog_api_client.v2.model.ip_allowlist_data import IPAllowlistData
from datadog_api_client.v2.model.ip_allowlist_entry import IPAllowlistEntry
from datadog_api_client.v2.model.ip_allowlist_entry_attributes import IPAllowlistEntryAttributes
from datadog_api_client.v2.model.ip_allowlist_entry_data import IPAllowlistEntryData
from datadog_api_client.v2.model.ip_allowlist_entry_type import IPAllowlistEntryType
from datadog_api_client.v2.model.ip_allowlist_type import IPAllowlistType
from datadog_api_client.v2.model.ip_allowlist_update_request import IPAllowlistUpdateRequest

body = IPAllowlistUpdateRequest(
    data=IPAllowlistData(
        attributes=IPAllowlistAttributes(
            entries=[
                IPAllowlistEntry(
                    data=IPAllowlistEntryData(
                        attributes=IPAllowlistEntryAttributes(
                            note="Example-IP-Allowlist",
                            cidr_block="127.0.0.1",
                        ),
                        type=IPAllowlistEntryType.IP_ALLOWLIST_ENTRY,
                    ),
                ),
            ],
            enabled=False,
        ),
        type=IPAllowlistType.IP_ALLOWLIST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IPAllowlistApi(api_client)
    response = api_instance.update_ip_allowlist(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update IP Allowlist returns "OK" response
```
# Update IP Allowlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::IPAllowlistAPI.new

body = DatadogAPIClient::V2::IPAllowlistUpdateRequest.new({
  data: DatadogAPIClient::V2::IPAllowlistData.new({
    attributes: DatadogAPIClient::V2::IPAllowlistAttributes.new({
      entries: [
        DatadogAPIClient::V2::IPAllowlistEntry.new({
          data: DatadogAPIClient::V2::IPAllowlistEntryData.new({
            attributes: DatadogAPIClient::V2::IPAllowlistEntryAttributes.new({
              note: "Example-IP-Allowlist",
              cidr_block: "127.0.0.1",
            }),
            type: DatadogAPIClient::V2::IPAllowlistEntryType::IP_ALLOWLIST_ENTRY,
          }),
        }),
      ],
      enabled: false,
    }),
    type: DatadogAPIClient::V2::IPAllowlistType::IP_ALLOWLIST,
  }),
})
p api_instance.update_ip_allowlist(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update IP Allowlist returns "OK" response
```
// Update IP Allowlist returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ip_allowlist::IPAllowlistAPI;
use datadog_api_client::datadogV2::model::IPAllowlistAttributes;
use datadog_api_client::datadogV2::model::IPAllowlistData;
use datadog_api_client::datadogV2::model::IPAllowlistEntry;
use datadog_api_client::datadogV2::model::IPAllowlistEntryAttributes;
use datadog_api_client::datadogV2::model::IPAllowlistEntryData;
use datadog_api_client::datadogV2::model::IPAllowlistEntryType;
use datadog_api_client::datadogV2::model::IPAllowlistType;
use datadog_api_client::datadogV2::model::IPAllowlistUpdateRequest;

#[tokio::main]
async fn main() {
    let body = IPAllowlistUpdateRequest::new(
        IPAllowlistData::new(IPAllowlistType::IP_ALLOWLIST).attributes(
            IPAllowlistAttributes::new()
                .enabled(false)
                .entries(vec![IPAllowlistEntry::new(
                    IPAllowlistEntryData::new(IPAllowlistEntryType::IP_ALLOWLIST_ENTRY).attributes(
                        IPAllowlistEntryAttributes::new()
                            .cidr_block("127.0.0.1".to_string())
                            .note("Example-IP-Allowlist".to_string()),
                    ),
                )]),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = IPAllowlistAPI::with_config(configuration);
    let resp = api.update_ip_allowlist(body).await;
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

#####  Update IP Allowlist returns "OK" response
```
/**
 * Update IP Allowlist returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.IPAllowlistApi(configuration);

const params: v2.IPAllowlistApiUpdateIPAllowlistRequest = {
  body: {
    data: {
      attributes: {
        entries: [
          {
            data: {
              attributes: {
                note: "Example-IP-Allowlist",
                cidrBlock: "127.0.0.1",
              },
              type: "ip_allowlist_entry",
            },
          },
        ],
        enabled: false,
      },
      type: "ip_allowlist",
    },
  },
};

apiInstance
  .updateIPAllowlist(params)
  .then((data: v2.IPAllowlistResponse) => {
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
![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=32b1d487-2c22-4c91-9142-f7f8c9ad92ad&bo=1&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=IP%20Allowlist&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fip-allowlist%2F&r=&evt=pageLoad&sv=2&cdb=AQAA&rn=479532)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=1e55f83e-6475-4659-8ebd-e677e7dbaf75&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=6f5f89fa-5c38-446c-ad0c-72de0723f539&pt=IP%20Allowlist&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fip-allowlist%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=1e55f83e-6475-4659-8ebd-e677e7dbaf75&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=6f5f89fa-5c38-446c-ad0c-72de0723f539&pt=IP%20Allowlist&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fip-allowlist%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
