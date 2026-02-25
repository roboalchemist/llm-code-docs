# Source: https://docs.datadoghq.com/api/latest/hosts.md

---
title: Hosts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Hosts
---

# Hosts

Get information about your infrastructure hosts in Datadog, and mute or unmute any notifications from your hosts. See the [Infrastructure page](https://docs.datadoghq.com/infrastructure/) for more information.

## Get all hosts for your organization{% #get-all-hosts-for-your-organization %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/hosts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/hosts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/hosts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/hosts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/hosts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/hosts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/hosts |

### Overview

This endpoint allows searching for hosts by name, alias, or tag. Hosts live within the past 3 hours are included by default. Retention is 7 days. Results are paginated with a max of 1000 results at a time. **Note:** If the host is an Amazon EC2 instance, `id` is replaced with `aws_id` in the response. **Note**: To enrich the data returned by this endpoint with security scans, see the new [api/v2/security/scanned-assets-metadata](https://docs.datadoghq.com/api/latest/security-monitoring/#list-scanned-assets-metadata) endpoint. This endpoint requires the `hosts_read` permission.

OAuth apps require the `hosts_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#hosts) to access this endpoint.



### Arguments

#### Query Strings

| Name                     | Type    | Description                                                                                                                                                                                                    |
| ------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter                   | string  | String to filter search results.                                                                                                                                                                               |
| sort_field               | string  | Sort hosts by this field.                                                                                                                                                                                      |
| sort_dir                 | string  | Direction of sort. Options include `asc` and `desc`.                                                                                                                                                           |
| start                    | integer | Specify the starting point for the host search results. For example, if you set `count` to 100 and the first 100 results have already been returned, you can set `start` to `101` to get the next 100 results. |
| count                    | integer | Number of hosts to return. Max 1000.                                                                                                                                                                           |
| from                     | integer | Number of seconds since UNIX epoch from which you want to search your hosts.                                                                                                                                   |
| include_muted_hosts_data | boolean | Include information on the muted status of hosts and when the mute expires.                                                                                                                                    |
| include_hosts_metadata   | boolean | Include additional metadata about the hosts (agent_version, machine, platform, processor, etc.).                                                                                                               |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with Host information from Datadog.

| Parent field         | Field              | Type     | Description                                                                                       |
| -------------------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------- |
|                      | host_list          | [object] | Array of hosts.                                                                                   |
| host_list            | aliases            | [string] | Host aliases collected by Datadog.                                                                |
| host_list            | apps               | [string] | The Datadog integrations reporting metrics for the host.                                          |
| host_list            | aws_name           | string   | AWS name of your host.                                                                            |
| host_list            | host_name          | string   | The host name.                                                                                    |
| host_list            | id                 | int64    | The host ID.                                                                                      |
| host_list            | is_muted           | boolean  | If a host is muted or unmuted.                                                                    |
| host_list            | last_reported_time | int64    | Last time the host reported a metric data point.                                                  |
| host_list            | meta               | object   | Metadata associated with your host.                                                               |
| meta                 | agent_checks       | [array]  | A list of Agent checks running on the host.                                                       |
| meta                 | agent_version      | string   | The Datadog Agent version.                                                                        |
| meta                 | cpuCores           | int64    | The number of cores.                                                                              |
| meta                 | fbsdV              | []       | An array of Mac versions.                                                                         |
| meta                 | gohai              | string   | JSON string containing system information.                                                        |
| meta                 | install_method     | object   | Agent install method.                                                                             |
| install_method       | installer_version  | string   | The installer version.                                                                            |
| install_method       | tool               | string   | Tool used to install the agent.                                                                   |
| install_method       | tool_version       | string   | The tool version.                                                                                 |
| meta                 | macV               | []       | An array of Mac versions.                                                                         |
| meta                 | machine            | string   | The machine architecture.                                                                         |
| meta                 | nixV               | []       | Array of Unix versions.                                                                           |
| meta                 | platform           | string   | The OS platform.                                                                                  |
| meta                 | processor          | string   | The processor.                                                                                    |
| meta                 | pythonV            | string   | The Python version.                                                                               |
| meta                 | socket-fqdn        | string   | The socket fqdn.                                                                                  |
| meta                 | socket-hostname    | string   | The socket hostname.                                                                              |
| meta                 | winV               | []       | An array of Windows versions.                                                                     |
| host_list            | metrics            | object   | Host Metrics collected.                                                                           |
| metrics              | cpu                | double   | The percent of CPU used (everything but idle).                                                    |
| metrics              | iowait             | double   | The percent of CPU spent waiting on the IO (not reported for all platforms).                      |
| metrics              | load               | double   | The system load over the last 15 minutes.                                                         |
| host_list            | mute_timeout       | int64    | Timeout of the mute applied to your host.                                                         |
| host_list            | name               | string   | The host name.                                                                                    |
| host_list            | sources            | [string] | Source or cloud provider associated with your host.                                               |
| host_list            | tags_by_source     | object   | List of tags for each source (AWS, Datadog Agent, Chef..).                                        |
| additionalProperties | <any-key>          | [string] | Array of tags for a single source.                                                                |
| host_list            | up                 | boolean  | Displays UP when the expected metrics are received and displays `???` if no metrics are received. |
|                      | total_matching     | int64    | Number of host matching the query.                                                                |
|                      | total_returned     | int64    | Number of host returned.                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "host_list": [
    {
      "aliases": [
        "mycoolhost-1"
      ],
      "apps": [
        "agent"
      ],
      "aws_name": "mycoolhost-1",
      "host_name": "i-deadbeef",
      "id": 123456,
      "is_muted": false,
      "last_reported_time": 1565000000,
      "meta": {
        "agent_checks": [
          "ntp",
          "ntp",
          "ntp:d884b5186b651429",
          "OK",
          "",
          ""
        ],
        "agent_version": "7.32.3",
        "cpuCores": 1,
        "fbsdV": [
          "FreeBSD"
        ],
        "gohai": "{\"cpu\":{\"cache_size\":\"8192 KB\",\"cpu_cores\":\"1\",\"cpu_logical_processors\":\"1\",\"family\":\"6\",\"mhz\":\"2712.000\",\"model\":\"142\",\"model_name\":\"Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz\",\"stepping\":\"10\",\"vendor_id\":\"GenuineIntel\"},\"filesystem\":[{\"kb_size\":\"3966896\",\"mounted_on\":\"/dev\",\"name\":\"udev\"},{\"kb_size\":\"797396\",\"mounted_on\":\"/run\",\"name\":\"tmpfs\"},{\"kb_size\":\"64800356\",\"mounted_on\":\"/\",\"name\":\"/dev/mapper/vagrant--vg-root\"},{\"kb_size\":\"3986972\",\"mounted_on\":\"/dev/shm\",\"name\":\"tmpfs\"},{\"kb_size\":\"5120\",\"mounted_on\":\"/run/lock\",\"name\":\"tmpfs\"},{\"kb_size\":\"3986972\",\"mounted_on\":\"/sys/fs/cgroup\",\"name\":\"tmpfs\"},{\"kb_size\":\"488245288\",\"mounted_on\":\"/vagrant\",\"name\":\"vagrant\"},{\"kb_size\":\"797392\",\"mounted_on\":\"/run/user/1000\",\"name\":\"tmpfs\"}],\"memory\":{\"swap_total\":\"1003516kB\",\"total\":\"7973944kB\"},\"network\":{\"interfaces\":[{\"ipv4\":\"10.0.2.15\",\"ipv4-network\":\"10.0.2.0/24\",\"ipv6\":\"fe80::a00:27ff:fec2:be11\",\"ipv6-network\":\"fe80::/64\",\"macaddress\":\"08:00:27:c2:be:11\",\"name\":\"eth0\"},{\"ipv4\":\"192.168.122.1\",\"ipv4-network\":\"192.168.122.0/24\",\"macaddress\":\"52:54:00:6f:1c:bf\",\"name\":\"virbr0\"}],\"ipaddress\":\"10.0.2.15\",\"ipaddressv6\":\"fe80::a00:27ff:fec2:be11\",\"macaddress\":\"08:00:27:c2:be:11\"},\"platform\":{\"GOOARCH\":\"amd64\",\"GOOS\":\"linux\",\"goV\":\"1.16.7\",\"hardware_platform\":\"x86_64\",\"hostname\":\"vagrant\",\"kernel_name\":\"Linux\",\"kernel_release\":\"4.15.0-29-generic\",\"kernel_version\":\"#31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018\",\"machine\":\"x86_64\",\"os\":\"GNU/Linux\",\"processor\":\"x86_64\",\"pythonV\":\"2.7.15rc1\"}}",
        "install_method": {
          "installer_version": "install_script-1.7.1",
          "tool": "install_script",
          "tool_version": "install_script"
        },
        "macV": [
          "Mac"
        ],
        "machine": "amd64",
        "nixV": [
          "Ubuntu"
        ],
        "platform": "linux",
        "processor": "Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz",
        "pythonV": "3.8.11",
        "socket-fqdn": "vagrant.vm.",
        "socket-hostname": "vagrant",
        "winV": [
          "Windows"
        ]
      },
      "metrics": {
        "cpu": 99,
        "iowait": 3.2,
        "load": 0.5
      },
      "mute_timeout": "integer",
      "name": "i-hostname",
      "sources": [
        "aws"
      ],
      "tags_by_source": {
        "<any-key>": [
          "test.example.com.host"
        ]
      },
      "up": true
    }
  ],
  "total_matching": 1,
  "total_returned": 1
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Invalid Parameter Error
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
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/hosts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all hosts for your organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get all hosts for your organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::HostsAPI.new
opts = {
  filter: "env:ci",
}
p api_instance.list_hosts(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.search_hosts()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get all hosts for your organization returns "OK" response

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
    api := datadogV1.NewHostsApi(apiClient)
    resp, r, err := api.ListHosts(ctx, *datadogV1.NewListHostsOptionalParameters().WithFilter("env:ci"))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `HostsApi.ListHosts`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `HostsApi.ListHosts`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get all hosts for your organization returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.HostsApi;
import com.datadog.api.client.v1.api.HostsApi.ListHostsOptionalParameters;
import com.datadog.api.client.v1.model.HostListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    HostsApi apiInstance = new HostsApi(defaultClient);

    try {
      HostListResponse result =
          apiInstance.listHosts(new ListHostsOptionalParameters().filter("env:ci"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostsApi#listHosts");
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
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Hosts.search()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
// Get all hosts for your organization returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_hosts::HostsAPI;
use datadog_api_client::datadogV1::api_hosts::ListHostsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = HostsAPI::with_config(configuration);
    let resp = api
        .list_hosts(ListHostsOptionalParams::default().filter("env:ci".to_string()))
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get all hosts for your organization returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.HostsApi(configuration);

const params: v1.HostsApiListHostsRequest = {
  filter: "env:ci",
};

apiInstance
  .listHosts(params)
  .then((data: v1.HostListResponse) => {
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

## Get the total number of active hosts{% #get-the-total-number-of-active-hosts %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/hosts/totals |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/hosts/totals |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/hosts/totals      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/hosts/totals      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/hosts/totals     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/hosts/totals |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/hosts/totals |

### Overview

This endpoint returns the total number of active and up hosts in your Datadog account. Active means the host has reported in the past hour, and up means it has reported in the past two hours. This endpoint requires the `hosts_read` permission.

OAuth apps require the `hosts_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#hosts) to access this endpoint.



### Arguments

#### Query Strings

| Name | Type    | Description                                                                |
| ---- | ------- | -------------------------------------------------------------------------- |
| from | integer | Number of seconds from which you want to get total number of active hosts. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Total number of host currently monitored by Datadog.

| Field        | Type  | Description                                                    |
| ------------ | ----- | -------------------------------------------------------------- |
| total_active | int64 | Total number of active host (UP and ???) reporting to Datadog. |
| total_up     | int64 | Number of host that are UP and reporting to Datadog.           |

{% /tab %}

{% tab title="Example" %}

```json
{
  "total_active": "integer",
  "total_up": "integer"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Invalid Parameter Error
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
Forbidden
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/hosts/totals" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get the total number of active hosts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.get_host_totals()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get the total number of active hosts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::HostsAPI.new
p api_instance.get_host_totals()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.host_totals()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get the total number of active hosts returns "OK" response

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
    api := datadogV1.NewHostsApi(apiClient)
    resp, r, err := api.GetHostTotals(ctx, *datadogV1.NewGetHostTotalsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `HostsApi.GetHostTotals`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `HostsApi.GetHostTotals`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get the total number of active hosts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.HostsApi;
import com.datadog.api.client.v1.model.HostTotals;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    HostsApi apiInstance = new HostsApi(defaultClient);

    try {
      HostTotals result = apiInstance.getHostTotals();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostsApi#getHostTotals");
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
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Hosts.totals()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
// Get the total number of active hosts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_hosts::GetHostTotalsOptionalParams;
use datadog_api_client::datadogV1::api_hosts::HostsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = HostsAPI::with_config(configuration);
    let resp = api
        .get_host_totals(GetHostTotalsOptionalParams::default())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Get the total number of active hosts returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.HostsApi(configuration);

apiInstance
  .getHostTotals()
  .then((data: v1.HostTotals) => {
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

## Mute a host{% #mute-a-host %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/host/{host_name}/mute |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/host/{host_name}/mute |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/host/{host_name}/mute      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/host/{host_name}/mute      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/host/{host_name}/mute     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/host/{host_name}/mute |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/host/{host_name}/mute |

### Overview

Mute a host. **Note:** This creates a [Downtime V2](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime) for the host.

### Arguments

#### Path Parameters

| Name                        | Type   | Description               |
| --------------------------- | ------ | ------------------------- |
| host_name [*required*] | string | Name of the host to mute. |

### Request

#### Body Data (required)

Mute a host request body.

{% tab title="Model" %}

| Field    | Type    | Description                                                                                                       |
| -------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| end      | int64   | POSIX timestamp in seconds when the host is unmuted. If omitted, the host remains muted until explicitly unmuted. |
| message  | string  | Message to associate with the muting of this host.                                                                |
| override | boolean | If true and the host is already muted, replaces existing host mute settings.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "end": 1579098130,
  "message": "Muting this host for a test!",
  "override": false
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with the list of muted host for your organization.

| Field    | Type   | Description                                          |
| -------- | ------ | ---------------------------------------------------- |
| action   | string | Action applied to the hosts.                         |
| end      | int64  | POSIX timestamp in seconds when the host is unmuted. |
| hostname | string | The host name.                                       |
| message  | string | Message associated with the mute.                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "action": "Muted",
  "end": 1579098130,
  "hostname": "test.host",
  "message": "Muting this host for a test!"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Invalid Parameter Error
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
Forbidden
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
                  \# Path parametersexport host_name="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/host/${host_name}/mute" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF

#####

```python
"""
Mute a host returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi
from datadog_api_client.v1.model.host_mute_settings import HostMuteSettings

body = HostMuteSettings(
    end=1579098130,
    message="Muting this host for a test!",
    override=False,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.mute_host(host_name="host_name", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Mute a host returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::HostsAPI.new

body = DatadogAPIClient::V1::HostMuteSettings.new({
  _end: 1579098130,
  message: "Muting this host for a test!",
  override: false,
})
p api_instance.mute_host("host_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Mute a host returns "OK" response

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
    body := datadogV1.HostMuteSettings{
        End:      datadog.PtrInt64(1579098130),
        Message:  datadog.PtrString("Muting this host for a test!"),
        Override: datadog.PtrBool(false),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewHostsApi(apiClient)
    resp, r, err := api.MuteHost(ctx, "host_name", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `HostsApi.MuteHost`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `HostsApi.MuteHost`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Mute a host returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.HostsApi;
import com.datadog.api.client.v1.model.HostMuteResponse;
import com.datadog.api.client.v1.model.HostMuteSettings;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    HostsApi apiInstance = new HostsApi(defaultClient);

    HostMuteSettings body =
        new HostMuteSettings()
            .end(1579098130L)
            .message("Muting this host for a test!")
            .override(false);

    try {
      HostMuteResponse result = apiInstance.muteHost("host_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostsApi#muteHost");
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
// Mute a host returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_hosts::HostsAPI;
use datadog_api_client::datadogV1::model::HostMuteSettings;

#[tokio::main]
async fn main() {
    let body = HostMuteSettings::new()
        .end(1579098130)
        .message("Muting this host for a test!".to_string())
        .override_(false);
    let configuration = datadog::Configuration::new();
    let api = HostsAPI::with_config(configuration);
    let resp = api.mute_host("host_name".to_string(), body).await;
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
 * Mute a host returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.HostsApi(configuration);

const params: v1.HostsApiMuteHostRequest = {
  body: {
    end: 1579098130,
    message: "Muting this host for a test!",
    override: false,
  },
  hostName: "host_name",
};

apiInstance
  .muteHost(params)
  .then((data: v1.HostMuteResponse) => {
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

## Unmute a host{% #unmute-a-host %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/host/{host_name}/unmute |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/host/{host_name}/unmute |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/host/{host_name}/unmute      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/host/{host_name}/unmute      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/host/{host_name}/unmute     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/host/{host_name}/unmute |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/host/{host_name}/unmute |

### Overview

Unmutes a host. This endpoint takes no JSON arguments.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                 |
| --------------------------- | ------ | --------------------------- |
| host_name [*required*] | string | Name of the host to unmute. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with the list of muted host for your organization.

| Field    | Type   | Description                                          |
| -------- | ------ | ---------------------------------------------------- |
| action   | string | Action applied to the hosts.                         |
| end      | int64  | POSIX timestamp in seconds when the host is unmuted. |
| hostname | string | The host name.                                       |
| message  | string | Message associated with the mute.                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "action": "Muted",
  "end": 1579098130,
  "hostname": "test.host",
  "message": "Muting this host for a test!"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Invalid Parameter Error
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
Forbidden
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
                  \# Path parametersexport host_name="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/host/${host_name}/unmute" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Unmute a host returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.unmute_host(
        host_name="host_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Unmute a host returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::HostsAPI.new
p api_instance.unmute_host("host_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Unmute a host returns "OK" response

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
    api := datadogV1.NewHostsApi(apiClient)
    resp, r, err := api.UnmuteHost(ctx, "host_name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `HostsApi.UnmuteHost`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `HostsApi.UnmuteHost`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Unmute a host returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.HostsApi;
import com.datadog.api.client.v1.model.HostMuteResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    HostsApi apiInstance = new HostsApi(defaultClient);

    try {
      HostMuteResponse result = apiInstance.unmuteHost("host_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostsApi#unmuteHost");
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
// Unmute a host returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_hosts::HostsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = HostsAPI::with_config(configuration);
    let resp = api.unmute_host("host_name".to_string()).await;
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
 * Unmute a host returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.HostsApi(configuration);

const params: v1.HostsApiUnmuteHostRequest = {
  hostName: "host_name",
};

apiInstance
  .unmuteHost(params)
  .then((data: v1.HostMuteResponse) => {
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
