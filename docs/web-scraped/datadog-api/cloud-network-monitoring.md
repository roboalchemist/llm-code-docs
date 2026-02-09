# Source: https://docs.datadoghq.com/api/latest/cloud-network-monitoring/

# Cloud Network Monitoring
The Cloud Network Monitoring API allows you to fetch aggregated connections and DNS traffic with their attributes. See the [Cloud Network Monitoring page](https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/) and [DNS Monitoring page](https://docs.datadoghq.com/network_monitoring/dns/) for more information.
## [Get all aggregated connections](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#get-all-aggregated-connections)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#get-all-aggregated-connections-v2)


GET https://api.ap1.datadoghq.com/api/v2/network/connections/aggregatehttps://api.ap2.datadoghq.com/api/v2/network/connections/aggregatehttps://api.datadoghq.eu/api/v2/network/connections/aggregatehttps://api.ddog-gov.com/api/v2/network/connections/aggregatehttps://api.datadoghq.com/api/v2/network/connections/aggregatehttps://api.us3.datadoghq.com/api/v2/network/connections/aggregatehttps://api.us5.datadoghq.com/api/v2/network/connections/aggregate
### Overview
Get all aggregated connections.
### Arguments
#### Query Strings
Name
Type
Description
from
integer
Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window is 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`.
to
integer
Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window is the current time. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`.
group_by
string
Comma-separated list of fields to group connections by. The maximum number of group_by(s) is 10.
tags
string
Comma-separated list of tags to filter connections by.
limit
integer
The number of connections to be returned. The maximum value is 7500. The default is 100.
### Response
  * [200](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#GetAggregatedConnections-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#GetAggregatedConnections-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#GetAggregatedConnections-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)


List of aggregated connections.
Field
Type
Description
data
[object]
Array of aggregated connection objects.
attributes
object
Attributes for an aggregated connection.
bytes_sent_by_client
int64
The total number of bytes sent by the client over the given period.
bytes_sent_by_server
int64
The total number of bytes sent by the server over the given period.
group_bys
object
The key, value pairs for each group by.
<any-key>
[string]
The values for each group by.
packets_sent_by_client
int64
The total number of packets sent by the client over the given period.
packets_sent_by_server
int64
The total number of packets sent by the server over the given period.
rtt_micro_seconds
int64
Measured as TCP smoothed round trip time in microseconds (the time between a TCP frame being sent and acknowledged).
tcp_closed_connections
int64
The number of TCP connections in a closed state. Measured in connections per second from the client.
tcp_established_connections
int64
The number of TCP connections in an established state. Measured in connections per second from the client.
tcp_refusals
int64
The number of TCP connections that were refused by the server. Typically this indicates an attempt to connect to an IP/port that is not receiving connections, or a firewall/security misconfiguration.
tcp_resets
int64
The number of TCP connections that were reset by the server.
tcp_retransmits
int64
TCP Retransmits represent detected failures that are retransmitted to ensure delivery. Measured in count of retransmits from the client.
tcp_timeouts
int64
The number of TCP connections that timed out from the perspective of the operating system. This can indicate general connectivity and latency issues.
id
string
A unique identifier for the aggregated connection based on the group by values.
type
enum
Aggregated connection resource type. Allowed enum values: `aggregated_connection`
default: `aggregated_connection`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=typescript)


#####  Get all aggregated connections
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/network/connections/aggregate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all aggregated connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all aggregated connections
```
# Get all aggregated connections returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudNetworkMonitoringAPI.new
p api_instance.get_aggregated_connections()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all aggregated connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all aggregated connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get all aggregated connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get all aggregated connections
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get all aggregated DNS traffic](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#get-all-aggregated-dns-traffic)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#get-all-aggregated-dns-traffic-v2)


GET https://api.ap1.datadoghq.com/api/v2/network/dns/aggregatehttps://api.ap2.datadoghq.com/api/v2/network/dns/aggregatehttps://api.datadoghq.eu/api/v2/network/dns/aggregatehttps://api.ddog-gov.com/api/v2/network/dns/aggregatehttps://api.datadoghq.com/api/v2/network/dns/aggregatehttps://api.us3.datadoghq.com/api/v2/network/dns/aggregatehttps://api.us5.datadoghq.com/api/v2/network/dns/aggregate
### Overview
Get all aggregated DNS traffic.
### Arguments
#### Query Strings
Name
Type
Description
from
integer
Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window is 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`.
to
integer
Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window is the current time. If neither `from` nor `to` are provided, the query window is `[now - 15m, now]`.
group_by
string
Comma-separated list of fields to group DNS traffic by. The server side defaults to `network.dns_query` if unspecified. `server_ungrouped` may be used if groups are not desired. The maximum number of group_by(s) is 10.
tags
string
Comma-separated list of tags to filter DNS traffic by.
limit
integer
The number of aggregated DNS entries to be returned. The maximum value is 7500. The default is 100.
### Response
  * [200](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#GetAggregatedDns-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#GetAggregatedDns-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/#GetAggregatedDns-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)


List of aggregated DNS flows.
Field
Type
Description
data
[object]
Array of aggregated DNS objects.
attributes
object
Attributes for an aggregated DNS flow.
group_bys
[object]
The key, value pairs for each group by.
key
string
The group by key.
value
string
The group by value.
metrics
[object]
Metrics associated with an aggregated DNS flow.
key
enum
The metric key for DNS metrics. Allowed enum values: `dns_total_requests,dns_failures,dns_successful_responses,dns_failed_responses,dns_timeouts,dns_responses.nxdomain,dns_responses.servfail,dns_responses.other,dns_success_latency_percentile,dns_failure_latency_percentile`
value
int64
The metric value.
id
string
A unique identifier for the aggregated DNS traffic based on the group by values.
type
enum
Aggregated DNS resource type. Allowed enum values: `aggregated_dns`
default: `aggregated_dns`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/cloud-network-monitoring/?code-lang=typescript)


#####  Get all aggregated DNS traffic
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/network/dns/aggregate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all aggregated DNS traffic
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all aggregated DNS traffic
```
# Get all aggregated DNS traffic returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CloudNetworkMonitoringAPI.new
p api_instance.get_aggregated_dns()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all aggregated DNS traffic
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all aggregated DNS traffic
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get all aggregated DNS traffic
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get all aggregated DNS traffic
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b22495e6-c287-43d7-bbd4-cb180383d202&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=e44df2fb-ca5d-4940-bfd0-97f116cb55a3&pt=Cloud%20Network%20Monitoring&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcloud-network-monitoring%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b22495e6-c287-43d7-bbd4-cb180383d202&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=e44df2fb-ca5d-4940-bfd0-97f116cb55a3&pt=Cloud%20Network%20Monitoring&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcloud-network-monitoring%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=c8b20a9a-8b67-4907-addd-23944eeaa41a&bo=2&sid=39b42aa0f0bf11f0ad99cb7dbf58476b&vid=39b4a9f0f0bf11f0a926e11ddcbf2165&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Cloud%20Network%20Monitoring&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcloud-network-monitoring%2F&r=&lt=1240&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=464708)
