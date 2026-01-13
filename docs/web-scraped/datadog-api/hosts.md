# Source: https://docs.datadoghq.com/api/latest/hosts

# Hosts
Get information about your infrastructure hosts in Datadog, and mute or unmute any notifications from your hosts. See the [Infrastructure page](https://docs.datadoghq.com/infrastructure/) for more information.
## [Get all hosts for your organization](https://docs.datadoghq.com/api/latest/hosts/#get-all-hosts-for-your-organization)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/hosts/#get-all-hosts-for-your-organization-v1)


GET https://api.ap1.datadoghq.com/api/v1/hostshttps://api.ap2.datadoghq.com/api/v1/hostshttps://api.datadoghq.eu/api/v1/hostshttps://api.ddog-gov.com/api/v1/hostshttps://api.datadoghq.com/api/v1/hostshttps://api.us3.datadoghq.com/api/v1/hostshttps://api.us5.datadoghq.com/api/v1/hosts
### Overview
This endpoint allows searching for hosts by name, alias, or tag. Hosts live within the past 3 hours are included by default. Retention is 7 days. Results are paginated with a max of 1000 results at a time. **Note:** If the host is an Amazon EC2 instance, `id` is replaced with `aws_id` in the response. **Note** : To enrich the data returned by this endpoint with security scans, see the new [api/v2/security/scanned-assets-metadata](https://docs.datadoghq.com/api/latest/security-monitoring/#list-scanned-assets-metadata) endpoint. This endpoint requires the `hosts_read` permission.
OAuth apps require the `hosts_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#hosts) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter
string
String to filter search results.
sort_field
string
Sort hosts by this field.
sort_dir
string
Direction of sort. Options include `asc` and `desc`.
start
integer
Specify the starting point for the host search results. For example, if you set `count` to 100 and the first 100 results have already been returned, you can set `start` to `101` to get the next 100 results.
count
integer
Number of hosts to return. Max 1000.
from
integer
Number of seconds since UNIX epoch from which you want to search your hosts.
include_muted_hosts_data
boolean
Include information on the muted status of hosts and when the mute expires.
include_hosts_metadata
boolean
Include additional metadata about the hosts (agent_version, machine, platform, processor, etc.).
### Response
  * [200](https://docs.datadoghq.com/api/latest/hosts/#ListHosts-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/hosts/#ListHosts-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/hosts/#ListHosts-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/hosts/#ListHosts-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


Response with Host information from Datadog.
Field
Type
Description
host_list
[object]
Array of hosts.
aliases
[string]
Host aliases collected by Datadog.
apps
[string]
The Datadog integrations reporting metrics for the host.
aws_name
string
AWS name of your host.
host_name
string
The host name.
id
int64
The host ID.
is_muted
boolean
If a host is muted or unmuted.
last_reported_time
int64
Last time the host reported a metric data point.
meta
object
Metadata associated with your host.
agent_checks
[array]
A list of Agent checks running on the host.
agent_version
string
The Datadog Agent version.
cpuCores
int64
The number of cores.
fbsdV
[]
An array of Mac versions.
gohai
string
JSON string containing system information.
install_method
object
Agent install method.
installer_version
string
The installer version.
tool
string
Tool used to install the agent.
tool_version
string
The tool version.
macV
[]
An array of Mac versions.
machine
string
The machine architecture.
nixV
[]
Array of Unix versions.
platform
string
The OS platform.
processor
string
The processor.
pythonV
string
The Python version.
socket-fqdn
string
The socket fqdn.
socket-hostname
string
The socket hostname.
winV
[]
An array of Windows versions.
metrics
object
Host Metrics collected.
cpu
double
The percent of CPU used (everything but idle).
iowait
double
The percent of CPU spent waiting on the IO (not reported for all platforms).
load
double
The system load over the last 15 minutes.
mute_timeout
int64
Timeout of the mute applied to your host.
name
string
The host name.
sources
[string]
Source or cloud provider associated with your host.
tags_by_source
object
List of tags for each source (AWS, Datadog Agent, Chef..).
<any-key>
[string]
Array of tags for a single source.
up
boolean
Displays UP when the expected metrics are received and displays `???` if no metrics are received.
total_matching
int64
Number of host matching the query.
total_returned
int64
Number of host returned.
```
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

Copy
Invalid Parameter Error
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/hosts/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/hosts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/hosts/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/hosts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/hosts/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/hosts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/hosts/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/hosts/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/hosts/?code-lang=python-legacy)


#####  Get all hosts for your organization
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/hosts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all hosts for your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all hosts for your organization
```
# Get all hosts for your organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::HostsAPI.new
opts = {
  filter: "env:ci",
}
p api_instance.list_hosts(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all hosts for your organization
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.search_hosts()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all hosts for your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all hosts for your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get all hosts for your organization
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Hosts.search()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get all hosts for your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get all hosts for your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get the total number of active hosts](https://docs.datadoghq.com/api/latest/hosts/#get-the-total-number-of-active-hosts)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/hosts/#get-the-total-number-of-active-hosts-v1)


GET https://api.ap1.datadoghq.com/api/v1/hosts/totalshttps://api.ap2.datadoghq.com/api/v1/hosts/totalshttps://api.datadoghq.eu/api/v1/hosts/totalshttps://api.ddog-gov.com/api/v1/hosts/totalshttps://api.datadoghq.com/api/v1/hosts/totalshttps://api.us3.datadoghq.com/api/v1/hosts/totalshttps://api.us5.datadoghq.com/api/v1/hosts/totals
### Overview
This endpoint returns the total number of active and up hosts in your Datadog account. Active means the host has reported in the past hour, and up means it has reported in the past two hours. This endpoint requires the `hosts_read` permission.
OAuth apps require the `hosts_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#hosts) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
from
integer
Number of seconds from which you want to get total number of active hosts.
### Response
  * [200](https://docs.datadoghq.com/api/latest/hosts/#GetHostTotals-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/hosts/#GetHostTotals-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/hosts/#GetHostTotals-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/hosts/#GetHostTotals-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


Total number of host currently monitored by Datadog.
Expand All
Field
Type
Description
total_active
int64
Total number of active host (UP and ???) reporting to Datadog.
total_up
int64
Number of host that are UP and reporting to Datadog.
```
{
  "total_active": "integer",
  "total_up": "integer"
}
```

Copy
Invalid Parameter Error
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/hosts/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/hosts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/hosts/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/hosts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/hosts/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/hosts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/hosts/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/hosts/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/hosts/?code-lang=python-legacy)


#####  Get the total number of active hosts
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/hosts/totals" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the total number of active hosts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get the total number of active hosts
```
# Get the total number of active hosts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::HostsAPI.new
p api_instance.get_host_totals()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get the total number of active hosts
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

dog.host_totals()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get the total number of active hosts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get the total number of active hosts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get the total number of active hosts
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Hosts.totals()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get the total number of active hosts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get the total number of active hosts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Mute a host](https://docs.datadoghq.com/api/latest/hosts/#mute-a-host)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/hosts/#mute-a-host-v1)


POST https://api.ap1.datadoghq.com/api/v1/host/{host_name}/mutehttps://api.ap2.datadoghq.com/api/v1/host/{host_name}/mutehttps://api.datadoghq.eu/api/v1/host/{host_name}/mutehttps://api.ddog-gov.com/api/v1/host/{host_name}/mutehttps://api.datadoghq.com/api/v1/host/{host_name}/mutehttps://api.us3.datadoghq.com/api/v1/host/{host_name}/mutehttps://api.us5.datadoghq.com/api/v1/host/{host_name}/mute
### Overview
Mute a host. **Note:** This creates a [Downtime V2](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime) for the host.
### Arguments
#### Path Parameters
Name
Type
Description
host_name [_required_]
string
Name of the host to mute.
### Request
#### Body Data (required)
Mute a host request body.
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


Expand All
Field
Type
Description
end
int64
POSIX timestamp in seconds when the host is unmuted. If omitted, the host remains muted until explicitly unmuted.
message
string
Message to associate with the muting of this host.
override
boolean
If true and the host is already muted, replaces existing host mute settings.
```
{
  "end": 1579098130,
  "message": "Muting this host for a test!",
  "override": false
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/hosts/#MuteHost-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/hosts/#MuteHost-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/hosts/#MuteHost-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/hosts/#MuteHost-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


Response with the list of muted host for your organization.
Expand All
Field
Type
Description
action
string
Action applied to the hosts.
end
int64
POSIX timestamp in seconds when the host is unmuted.
hostname
string
The host name.
message
string
Message associated with the mute.
```
{
  "action": "Muted",
  "end": 1579098130,
  "hostname": "test.host",
  "message": "Muting this host for a test!"
}
```

Copy
Invalid Parameter Error
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/hosts/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/hosts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/hosts/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/hosts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/hosts/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/hosts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/hosts/?code-lang=typescript)


#####  Mute a host
Copy
```
                  # Path parameters  
export host_name="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/host/${host_name}/mute" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Mute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Mute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Mute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Mute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Mute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Mute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Unmute a host](https://docs.datadoghq.com/api/latest/hosts/#unmute-a-host)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/hosts/#unmute-a-host-v1)


POST https://api.ap1.datadoghq.com/api/v1/host/{host_name}/unmutehttps://api.ap2.datadoghq.com/api/v1/host/{host_name}/unmutehttps://api.datadoghq.eu/api/v1/host/{host_name}/unmutehttps://api.ddog-gov.com/api/v1/host/{host_name}/unmutehttps://api.datadoghq.com/api/v1/host/{host_name}/unmutehttps://api.us3.datadoghq.com/api/v1/host/{host_name}/unmutehttps://api.us5.datadoghq.com/api/v1/host/{host_name}/unmute
### Overview
Unmutes a host. This endpoint takes no JSON arguments.
### Arguments
#### Path Parameters
Name
Type
Description
host_name [_required_]
string
Name of the host to unmute.
### Response
  * [200](https://docs.datadoghq.com/api/latest/hosts/#UnmuteHost-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/hosts/#UnmuteHost-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/hosts/#UnmuteHost-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/hosts/#UnmuteHost-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


Response with the list of muted host for your organization.
Expand All
Field
Type
Description
action
string
Action applied to the hosts.
end
int64
POSIX timestamp in seconds when the host is unmuted.
hostname
string
The host name.
message
string
Message associated with the mute.
```
{
  "action": "Muted",
  "end": 1579098130,
  "hostname": "test.host",
  "message": "Muting this host for a test!"
}
```

Copy
Invalid Parameter Error
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/hosts/)
  * [Example](https://docs.datadoghq.com/api/latest/hosts/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/hosts/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/hosts/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/hosts/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/hosts/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/hosts/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/hosts/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/hosts/?code-lang=typescript)


#####  Unmute a host
Copy
```
                  # Path parameters  
export host_name="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/host/${host_name}/unmute" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Unmute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Unmute a host
```
# Unmute a host returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::HostsAPI.new
p api_instance.unmute_host("host_name")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Unmute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Unmute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Unmute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Unmute a host
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0ad00c34-7baa-49c4-9189-f56e1e5b67cc&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=a7b8ed01-8ba2-4ae8-9d2e-178e6d027ddf&pt=Hosts&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fhosts%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0ad00c34-7baa-49c4-9189-f56e1e5b67cc&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=a7b8ed01-8ba2-4ae8-9d2e-178e6d027ddf&pt=Hosts&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fhosts%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=a0b328a9-4b82-4c9c-b0e9-63cebcadf5cf&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Hosts&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fhosts%2F&r=&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=317137)
