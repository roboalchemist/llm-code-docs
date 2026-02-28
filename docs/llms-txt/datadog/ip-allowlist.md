# Source: https://docs.datadoghq.com/api/latest/ip-allowlist.md

---
title: IP Allowlist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > IP Allowlist
---

# IP Allowlist

The IP allowlist API is used to manage the IP addresses that can access the Datadog API and web UI. It does not block access to intake APIs or public dashboards.

This is an enterprise-only feature. Request access by contacting Datadog support, or see the [IP Allowlist page](https://docs.datadoghq.com/account_management/org_settings/ip_allowlist/) for more information.

## Get IP Allowlist{% #get-ip-allowlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/ip_allowlist |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/ip_allowlist |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/ip_allowlist      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/ip_allowlist      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/ip_allowlist     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/ip_allowlist |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/ip_allowlist |

### Overview

Returns the IP allowlist and its enabled or disabled state. This endpoint requires the `org_management` permission.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ip-allowlist) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about the IP allowlist.

| Parent field | Field                  | Type      | Description                                                        |
| ------------ | ---------------------- | --------- | ------------------------------------------------------------------ |
|              | data                   | object    | IP allowlist data.                                                 |
| data         | attributes             | object    | Attributes of the IP allowlist.                                    |
| attributes   | enabled                | boolean   | Whether the IP allowlist logic is enabled or not.                  |
| attributes   | entries                | [object]  | Array of entries in the IP allowlist.                              |
| entries      | data [*required*] | object    | Data of the IP allowlist entry object.                             |
| data         | attributes             | object    | Attributes of the IP allowlist entry.                              |
| attributes   | cidr_block             | string    | The CIDR block describing the IP range of the entry.               |
| attributes   | created_at             | date-time | Creation time of the entry.                                        |
| attributes   | modified_at            | date-time | Time of last entry modification.                                   |
| attributes   | note                   | string    | A note describing the IP allowlist entry.                          |
| data         | id                     | string    | The unique identifier of the IP allowlist entry.                   |
| data         | type [*required*] | enum      | IP allowlist Entry type. Allowed enum values: `ip_allowlist_entry` |
| data         | id                     | string    | The unique identifier of the org.                                  |
| data         | type [*required*] | enum      | IP allowlist type. Allowed enum values: `ip_allowlist`             |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ip_allowlist" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get IP Allowlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::IPAllowlistAPI.new
p api_instance.get_ip_allowlist()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update IP Allowlist{% #update-ip-allowlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/ip_allowlist |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/ip_allowlist |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/ip_allowlist      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/ip_allowlist      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/ip_allowlist     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/ip_allowlist |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/ip_allowlist |

### Overview

Edit the entries in the IP allowlist, and enable or disable it. This endpoint requires the `org_management` permission.

OAuth apps require the `org_management` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ip-allowlist) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type      | Description                                                        |
| ------------ | ---------------------- | --------- | ------------------------------------------------------------------ |
|              | data [*required*] | object    | IP allowlist data.                                                 |
| data         | attributes             | object    | Attributes of the IP allowlist.                                    |
| attributes   | enabled                | boolean   | Whether the IP allowlist logic is enabled or not.                  |
| attributes   | entries                | [object]  | Array of entries in the IP allowlist.                              |
| entries      | data [*required*] | object    | Data of the IP allowlist entry object.                             |
| data         | attributes             | object    | Attributes of the IP allowlist entry.                              |
| attributes   | cidr_block             | string    | The CIDR block describing the IP range of the entry.               |
| attributes   | created_at             | date-time | Creation time of the entry.                                        |
| attributes   | modified_at            | date-time | Time of last entry modification.                                   |
| attributes   | note                   | string    | A note describing the IP allowlist entry.                          |
| data         | id                     | string    | The unique identifier of the IP allowlist entry.                   |
| data         | type [*required*] | enum      | IP allowlist Entry type. Allowed enum values: `ip_allowlist_entry` |
| data         | id                     | string    | The unique identifier of the org.                                  |
| data         | type [*required*] | enum      | IP allowlist type. Allowed enum values: `ip_allowlist`             |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about the IP allowlist.

| Parent field | Field                  | Type      | Description                                                        |
| ------------ | ---------------------- | --------- | ------------------------------------------------------------------ |
|              | data                   | object    | IP allowlist data.                                                 |
| data         | attributes             | object    | Attributes of the IP allowlist.                                    |
| attributes   | enabled                | boolean   | Whether the IP allowlist logic is enabled or not.                  |
| attributes   | entries                | [object]  | Array of entries in the IP allowlist.                              |
| entries      | data [*required*] | object    | Data of the IP allowlist entry object.                             |
| data         | attributes             | object    | Attributes of the IP allowlist entry.                              |
| attributes   | cidr_block             | string    | The CIDR block describing the IP range of the entry.               |
| attributes   | created_at             | date-time | Creation time of the entry.                                        |
| attributes   | modified_at            | date-time | Time of last entry modification.                                   |
| attributes   | note                   | string    | A note describing the IP allowlist entry.                          |
| data         | id                     | string    | The unique identifier of the IP allowlist entry.                   |
| data         | type [*required*] | enum      | IP allowlist Entry type. Allowed enum values: `ip_allowlist_entry` |
| data         | id                     | string    | The unique identifier of the org.                                  |
| data         | type [*required*] | enum      | IP allowlist type. Allowed enum values: `ip_allowlist`             |

{% /tab %}

{% tab title="Example" %}

```json
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
Forbidden
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
                          \# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ip_allowlist" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
