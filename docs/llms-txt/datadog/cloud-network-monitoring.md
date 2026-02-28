# Source: https://docs.datadoghq.com/api/latest/cloud-network-monitoring.md

---
title: Cloud Network Monitoring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Cloud Network Monitoring
---

# Cloud Network Monitoring

The Cloud Network Monitoring API allows you to fetch aggregated connections and DNS traffic with their attributes. See the [Cloud Network Monitoring page](https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/) and [DNS Monitoring page](https://docs.datadoghq.com/network_monitoring/dns/) for more information.

## Get all aggregated connections{% #get-all-aggregated-connections %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/network/connections/aggregate |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/network/connections/aggregate |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/network/connections/aggregate      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/network/connections/aggregate      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/network/connections/aggregate     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/network/connections/aggregate |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/network/connections/aggregate |

### Overview

Get all aggregated connections.

### Arguments

#### Query Strings

| Name     | Type    | Description                                                                                                                                                                                                                                               |
| -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from     | integer | Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window is 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`. |
| to       | integer | Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window is the current time. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`.                         |
| group_by | string  | Comma-separated list of fields to group connections by. The maximum number of group_by(s) is 10.                                                                                                                                                          |
| tags     | string  | Comma-separated list of tags to filter connections by.                                                                                                                                                                                                    |
| limit    | integer | The number of connections to be returned. The maximum value is 7500. The default is 100.                                                                                                                                                                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of aggregated connections.

| Parent field         | Field                       | Type     | Description                                                                                                                                                                                             |
| -------------------- | --------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                        | [object] | Array of aggregated connection objects.                                                                                                                                                                 |
| data                 | attributes                  | object   | Attributes for an aggregated connection.                                                                                                                                                                |
| attributes           | bytes_sent_by_client        | int64    | The total number of bytes sent by the client over the given period.                                                                                                                                     |
| attributes           | bytes_sent_by_server        | int64    | The total number of bytes sent by the server over the given period.                                                                                                                                     |
| attributes           | group_bys                   | object   | The key, value pairs for each group by.                                                                                                                                                                 |
| additionalProperties | <any-key>                   | [string] | The values for each group by.                                                                                                                                                                           |
| attributes           | packets_sent_by_client      | int64    | The total number of packets sent by the client over the given period.                                                                                                                                   |
| attributes           | packets_sent_by_server      | int64    | The total number of packets sent by the server over the given period.                                                                                                                                   |
| attributes           | rtt_micro_seconds           | int64    | Measured as TCP smoothed round trip time in microseconds (the time between a TCP frame being sent and acknowledged).                                                                                    |
| attributes           | tcp_closed_connections      | int64    | The number of TCP connections in a closed state. Measured in connections per second from the client.                                                                                                    |
| attributes           | tcp_established_connections | int64    | The number of TCP connections in an established state. Measured in connections per second from the client.                                                                                              |
| attributes           | tcp_refusals                | int64    | The number of TCP connections that were refused by the server. Typically this indicates an attempt to connect to an IP/port that is not receiving connections, or a firewall/security misconfiguration. |
| attributes           | tcp_resets                  | int64    | The number of TCP connections that were reset by the server.                                                                                                                                            |
| attributes           | tcp_retransmits             | int64    | TCP Retransmits represent detected failures that are retransmitted to ensure delivery. Measured in count of retransmits from the client.                                                                |
| attributes           | tcp_timeouts                | int64    | The number of TCP connections that timed out from the perspective of the operating system. This can indicate general connectivity and latency issues.                                                   |
| data                 | id                          | string   | A unique identifier for the aggregated connection based on the group by values.                                                                                                                         |
| data                 | type                        | enum     | Aggregated connection resource type. Allowed enum values: `aggregated_connection`                                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "bytes_sent_by_client": 100,
        "bytes_sent_by_server": 200,
        "group_bys": {
          "client_team": [
            "networks"
          ],
          "server_service": [
            "hucklebuck"
          ]
        },
        "packets_sent_by_client": 10,
        "packets_sent_by_server": 20,
        "rtt_micro_seconds": 800,
        "tcp_closed_connections": 30,
        "tcp_established_connections": 40,
        "tcp_refusals": 7,
        "tcp_resets": 5,
        "tcp_retransmits": 30,
        "tcp_timeouts": 6
      },
      "id": "client_team:networks, server_service:hucklebuck",
      "type": "aggregated_connection"
    }
  ]
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/network/connections/aggregate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all aggregated connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_network_monitoring_api import CloudNetworkMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudNetworkMonitoringApi(api_client)
    response = api_instance.get_aggregated_connections()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all aggregated connections returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudNetworkMonitoringAPI.new
p api_instance.get_aggregated_connections()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all aggregated connections returns "OK" response

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
    api := datadogV2.NewCloudNetworkMonitoringApi(apiClient)
    resp, r, err := api.GetAggregatedConnections(ctx, *datadogV2.NewGetAggregatedConnectionsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `CloudNetworkMonitoringApi.GetAggregatedConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `CloudNetworkMonitoringApi.GetAggregatedConnections`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all aggregated connections returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudNetworkMonitoringApi;
import com.datadog.api.client.v2.model.SingleAggregatedConnectionResponseArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudNetworkMonitoringApi apiInstance = new CloudNetworkMonitoringApi(defaultClient);

    try {
      SingleAggregatedConnectionResponseArray result = apiInstance.getAggregatedConnections();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CloudNetworkMonitoringApi#getAggregatedConnections");
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
// Get all aggregated connections returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_network_monitoring::CloudNetworkMonitoringAPI;
use datadog_api_client::datadogV2::api_cloud_network_monitoring::GetAggregatedConnectionsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudNetworkMonitoringAPI::with_config(configuration);
    let resp = api
        .get_aggregated_connections(GetAggregatedConnectionsOptionalParams::default())
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
 * Get all aggregated connections returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudNetworkMonitoringApi(configuration);

apiInstance
  .getAggregatedConnections()
  .then((data: v2.SingleAggregatedConnectionResponseArray) => {
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

## Get all aggregated DNS traffic{% #get-all-aggregated-dns-traffic %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/network/dns/aggregate |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/network/dns/aggregate |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/network/dns/aggregate      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/network/dns/aggregate      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/network/dns/aggregate     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/network/dns/aggregate |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/network/dns/aggregate |

### Overview

Get all aggregated DNS traffic.

### Arguments

#### Query Strings

| Name     | Type    | Description                                                                                                                                                                                                                                               |
| -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from     | integer | Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window is 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`. |
| to       | integer | Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window is the current time. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`.                         |
| group_by | string  | Comma-separated list of fields to group DNS traffic by. The server side defaults to `network.dns_query` if unspecified. `server_ungrouped` may be used if groups are not desired. The maximum number of group_by(s) is 10.                                |
| tags     | string  | Comma-separated list of tags to filter DNS traffic by.                                                                                                                                                                                                    |
| limit    | integer | The number of aggregated DNS entries to be returned. The maximum value is 7500. The default is 100.                                                                                                                                                       |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of aggregated DNS flows.

| Parent field | Field      | Type     | Description                                                                                                                                                                                                                                                                       |
| ------------ | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | [object] | Array of aggregated DNS objects.                                                                                                                                                                                                                                                  |
| data         | attributes | object   | Attributes for an aggregated DNS flow.                                                                                                                                                                                                                                            |
| attributes   | group_bys  | [object] | The key, value pairs for each group by.                                                                                                                                                                                                                                           |
| group_bys    | key        | string   | The group by key.                                                                                                                                                                                                                                                                 |
| group_bys    | value      | string   | The group by value.                                                                                                                                                                                                                                                               |
| attributes   | metrics    | [object] | Metrics associated with an aggregated DNS flow.                                                                                                                                                                                                                                   |
| metrics      | key        | enum     | The metric key for DNS metrics. Allowed enum values: `dns_total_requests,dns_failures,dns_successful_responses,dns_failed_responses,dns_timeouts,dns_responses.nxdomain,dns_responses.servfail,dns_responses.other,dns_success_latency_percentile,dns_failure_latency_percentile` |
| metrics      | value      | int64    | The metric value.                                                                                                                                                                                                                                                                 |
| data         | id         | string   | A unique identifier for the aggregated DNS traffic based on the group by values.                                                                                                                                                                                                  |
| data         | type       | enum     | Aggregated DNS resource type. Allowed enum values: `aggregated_dns`                                                                                                                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "group_bys": [
          {
            "key": "client_service",
            "value": "example-service"
          },
          {
            "key": "network.dns_query",
            "value": "example.com"
          }
        ],
        "metrics": [
          {
            "key": "dns_total_requests",
            "value": 100
          },
          {
            "key": "dns_failures",
            "value": 7
          },
          {
            "key": "dns_successful_responses",
            "value": 93
          },
          {
            "key": "dns_failed_responses",
            "value": 5
          },
          {
            "key": "dns_timeouts",
            "value": 2
          },
          {
            "key": "dns_responses.nxdomain",
            "value": 1
          },
          {
            "key": "dns_responses.servfail",
            "value": 1
          },
          {
            "key": "dns_responses.other",
            "value": 3
          },
          {
            "key": "dns_success_latency_percentile",
            "value": 50
          },
          {
            "key": "dns_failure_latency_percentile",
            "value": 75
          }
        ]
      },
      "id": "client_service:example-service,network.dns_query:example.com",
      "type": "aggregated_dns"
    }
  ]
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/network/dns/aggregate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all aggregated DNS traffic returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_network_monitoring_api import CloudNetworkMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudNetworkMonitoringApi(api_client)
    response = api_instance.get_aggregated_dns()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all aggregated DNS traffic returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudNetworkMonitoringAPI.new
p api_instance.get_aggregated_dns()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all aggregated DNS traffic returns "OK" response

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
    api := datadogV2.NewCloudNetworkMonitoringApi(apiClient)
    resp, r, err := api.GetAggregatedDns(ctx, *datadogV2.NewGetAggregatedDnsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `CloudNetworkMonitoringApi.GetAggregatedDns`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `CloudNetworkMonitoringApi.GetAggregatedDns`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all aggregated DNS traffic returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CloudNetworkMonitoringApi;
import com.datadog.api.client.v2.model.SingleAggregatedDnsResponseArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CloudNetworkMonitoringApi apiInstance = new CloudNetworkMonitoringApi(defaultClient);

    try {
      SingleAggregatedDnsResponseArray result = apiInstance.getAggregatedDns();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudNetworkMonitoringApi#getAggregatedDns");
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
// Get all aggregated DNS traffic returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_cloud_network_monitoring::CloudNetworkMonitoringAPI;
use datadog_api_client::datadogV2::api_cloud_network_monitoring::GetAggregatedDnsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CloudNetworkMonitoringAPI::with_config(configuration);
    let resp = api
        .get_aggregated_dns(GetAggregatedDnsOptionalParams::default())
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
 * Get all aggregated DNS traffic returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CloudNetworkMonitoringApi(configuration);

apiInstance
  .getAggregatedDns()
  .then((data: v2.SingleAggregatedDnsResponseArray) => {
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
