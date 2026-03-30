# Source: https://docs.datadoghq.com/api/latest/ip-ranges.md

---
title: IP Ranges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > IP Ranges
---

# IP Ranges

Get a list of IP prefixes belonging to Datadog.

## List IP Ranges{% #list-ip-ranges %}

{% tab title="v1" %}

| Datadog site      | API endpoint                             |
| ----------------- | ---------------------------------------- |
| ap1.datadoghq.com | GET https://ip-ranges.ap1.datadoghq.com/ |
| ap2.datadoghq.com | GET https://ip-ranges.ap2.datadoghq.com/ |
| app.datadoghq.eu  | GET https://ip-ranges.datadoghq.eu/      |
| app.ddog-gov.com  | GET https://ip-ranges.ddog-gov.com/      |
| app.datadoghq.com | GET https://ip-ranges.datadoghq.com/     |
| us3.datadoghq.com | GET https://ip-ranges.us3.datadoghq.com/ |
| us5.datadoghq.com | GET https://ip-ranges.us5.datadoghq.com/ |

### Overview

Get information about Datadog IP ranges.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
IP ranges.

| Parent field                 | Field                        | Type     | Description                                                                  |
| ---------------------------- | ---------------------------- | -------- | ---------------------------------------------------------------------------- |
|                              | agents                       | object   | Available prefix information for the Agent endpoints.                        |
| agents                       | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| agents                       | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | api                          | object   | Available prefix information for the API endpoints.                          |
| api                          | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| api                          | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | apm                          | object   | Available prefix information for the APM endpoints.                          |
| apm                          | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| apm                          | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | global                       | object   | Available prefix information for all Datadog endpoints.                      |
| global                       | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| global                       | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | logs                         | object   | Available prefix information for the Logs endpoints.                         |
| logs                         | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| logs                         | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | modified                     | string   | Date when last updated, in the form `YYYY-MM-DD-hh-mm-ss`.                   |
|                              | orchestrator                 | object   | Available prefix information for the Orchestrator endpoints.                 |
| orchestrator                 | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| orchestrator                 | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | process                      | object   | Available prefix information for the Process endpoints.                      |
| process                      | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| process                      | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | remote-configuration         | object   | Available prefix information for the Remote Configuration endpoints.         |
| remote-configuration         | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| remote-configuration         | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | synthetics                   | object   | Available prefix information for the Synthetics endpoints.                   |
| synthetics                   | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| synthetics                   | prefixes_ipv4_by_location    | object   | List of IPv4 prefixes by location.                                           |
| additionalProperties         | <any-key>                    | [string] | List of IPv4 prefixes.                                                       |
| synthetics                   | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
| synthetics                   | prefixes_ipv6_by_location    | object   | List of IPv6 prefixes by location.                                           |
| additionalProperties         | <any-key>                    | [string] | List of IPv6 prefixes.                                                       |
|                              | synthetics-private-locations | object   | Available prefix information for the Synthetics Private Locations endpoints. |
| synthetics-private-locations | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| synthetics-private-locations | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |
|                              | version                      | int64    | Version of the IP list.                                                      |
|                              | webhooks                     | object   | Available prefix information for the Webhook endpoints.                      |
| webhooks                     | prefixes_ipv4                | [string] | List of IPv4 prefixes.                                                       |
| webhooks                     | prefixes_ipv6                | [string] | List of IPv6 prefixes.                                                       |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://ip-ranges.ap1.datadoghq.com"https://ip-ranges.ap2.datadoghq.com"https://ip-ranges.datadoghq.eu"https://ip-ranges.ddog-gov.com"https://ip-ranges.datadoghq.com"https://ip-ranges.us3.datadoghq.com"https://ip-ranges.us5.datadoghq.com/" \
-H "Accept: application/json"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" python3 "example.py"
#####

```ruby
# List IP Ranges returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::IPRangesAPI.new
p api_instance.get_ip_ranges()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" tsc "example.ts"
{% /tab %}
