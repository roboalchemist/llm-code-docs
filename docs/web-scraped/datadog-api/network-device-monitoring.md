# Source: https://docs.datadoghq.com/api/latest/network-device-monitoring/

# Network Device Monitoring
The Network Device Monitoring API allows you to fetch devices and interfaces and their attributes. See the [Network Device Monitoring page](https://docs.datadoghq.com/network_monitoring/) for more information.
## [Get the list of devices](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-list-of-devices)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-list-of-devices-v2)


GET https://api.ap1.datadoghq.com/api/v2/ndm/deviceshttps://api.ap2.datadoghq.com/api/v2/ndm/deviceshttps://api.datadoghq.eu/api/v2/ndm/deviceshttps://api.ddog-gov.com/api/v2/ndm/deviceshttps://api.datadoghq.com/api/v2/ndm/deviceshttps://api.us3.datadoghq.com/api/v2/ndm/deviceshttps://api.us5.datadoghq.com/api/v2/ndm/devices
### Overview
Get the list of devices.
### Arguments
#### Query Strings
Name
Type
Description
page[size]
integer
Size for a given page. The maximum allowed value is 100.
page[number]
integer
Specific page number to return.
sort
string
The field to sort the devices by.
filter[tag]
string
Filter devices by tag.
### Response
  * [200](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDevices-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDevices-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDevices-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDevices-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


List devices response.
Field
Type
Description
data
[object]
The list devices response data.
attributes
object
The device attributes
description
string
The device description
device_type
string
The device type
integration
string
The device integration
interface_statuses
object
Count of the device interfaces by status
down
int64
The number of interfaces that are down
off
int64
The number of interfaces that are off
up
int64
The number of interfaces that are up
warning
int64
The number of interfaces that are in a warning state
ip_address
string
The device IP address
location
string
The device location
model
string
The device model
name
string
The device name
os_hostname
string
The device OS hostname
os_name
string
The device OS name
os_version
string
The device OS version
ping_status
string
The device ping status
product_name
string
The device product name
serial_number
string
The device serial number
status
string
The device SNMP status
subnet
string
The device subnet
sys_object_id
string
The device `sys_object_id`
tags
[string]
The list of device tags
vendor
string
The device vendor
version
string
The device version
id
string
The device ID
type
string
The type of the resource. The value should always be device.
meta
object
Object describing meta attributes of response.
page
object
Pagination object.
total_filtered_count
int64
Total count of devices matched by the filter.
```
{
  "data": [
    {
      "attributes": {
        "description": "a device monitored with NDM",
        "device_type": "other",
        "integration": "snmp",
        "interface_statuses": {
          "down": "integer",
          "off": "integer",
          "up": "integer",
          "warning": "integer"
        },
        "ip_address": "1.2.3.4",
        "location": "paris",
        "model": "xx-123",
        "name": "example device",
        "os_hostname": "string",
        "os_name": "example OS",
        "os_version": "1.0.2",
        "ping_status": "unmonitored",
        "product_name": "example device",
        "serial_number": "X12345",
        "status": "ok",
        "subnet": "1.2.3.4/24",
        "sys_object_id": "1.3.6.1.4.1.99999",
        "tags": [
          "device_ip:1.2.3.4",
          "device_id:example:1.2.3.4"
        ],
        "vendor": "example vendor",
        "version": "1.2.3"
      },
      "id": "example:1.2.3.4",
      "type": "string"
    }
  ],
  "meta": {
    "page": {
      "total_filtered_count": 1
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=typescript)


#####  Get the list of devices
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/devices" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the list of devices
```
"""
Get the list of devices returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.list_devices(
        page_size=1,
        page_number=0,
        filter_tag="device_namespace:default",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the list of devices
```
# Get the list of devices returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new
opts = {
  page_size: 1,
  page_number: 0,
  filter_tag: "device_namespace:default",
}
p api_instance.list_devices(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the list of devices
```
// Get the list of devices returns "OK" response

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
	api := datadogV2.NewNetworkDeviceMonitoringApi(apiClient)
	resp, r, err := api.ListDevices(ctx, *datadogV2.NewListDevicesOptionalParameters().WithPageSize(1).WithPageNumber(0).WithFilterTag("device_namespace:default"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NetworkDeviceMonitoringApi.ListDevices`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NetworkDeviceMonitoringApi.ListDevices`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the list of devices
```
// Get the list of devices returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.NetworkDeviceMonitoringApi;
import com.datadog.api.client.v2.api.NetworkDeviceMonitoringApi.ListDevicesOptionalParameters;
import com.datadog.api.client.v2.model.ListDevicesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NetworkDeviceMonitoringApi apiInstance = new NetworkDeviceMonitoringApi(defaultClient);

    try {
      ListDevicesResponse result =
          apiInstance.listDevices(
              new ListDevicesOptionalParameters()
                  .pageSize(1L)
                  .pageNumber(0L)
                  .filterTag("device_namespace:default"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkDeviceMonitoringApi#listDevices");
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

#####  Get the list of devices
```
// Get the list of devices returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_network_device_monitoring::ListDevicesOptionalParams;
use datadog_api_client::datadogV2::api_network_device_monitoring::NetworkDeviceMonitoringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = NetworkDeviceMonitoringAPI::with_config(configuration);
    let resp = api
        .list_devices(
            ListDevicesOptionalParams::default()
                .page_size(1)
                .page_number(0)
                .filter_tag("device_namespace:default".to_string()),
        )
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

#####  Get the list of devices
```
/**
 * Get the list of devices returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.NetworkDeviceMonitoringApi(configuration);

const params: v2.NetworkDeviceMonitoringApiListDevicesRequest = {
  pageSize: 1,
  pageNumber: 0,
  filterTag: "device_namespace:default",
};

apiInstance
  .listDevices(params)
  .then((data: v2.ListDevicesResponse) => {
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
## [Get the device details](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-device-details)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-device-details-v2)


GET https://api.ap1.datadoghq.com/api/v2/ndm/devices/{device_id}https://api.ap2.datadoghq.com/api/v2/ndm/devices/{device_id}https://api.datadoghq.eu/api/v2/ndm/devices/{device_id}https://api.ddog-gov.com/api/v2/ndm/devices/{device_id}https://api.datadoghq.com/api/v2/ndm/devices/{device_id}https://api.us3.datadoghq.com/api/v2/ndm/devices/{device_id}https://api.us5.datadoghq.com/api/v2/ndm/devices/{device_id}
### Overview
Get the device details.
### Arguments
#### Path Parameters
Name
Type
Description
device_id [_required_]
string
The id of the device to fetch.
### Response
  * [200](https://docs.datadoghq.com/api/latest/network-device-monitoring/#GetDevice-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/network-device-monitoring/#GetDevice-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/network-device-monitoring/#GetDevice-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/network-device-monitoring/#GetDevice-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


The `GetDevice` operation’s response.
Field
Type
Description
data
object
Get device response data.
attributes
object
The device attributes
description
string
A description of the device.
device_type
string
The type of the device.
integration
string
The integration of the device.
ip_address
string
The IP address of the device.
location
string
The location of the device.
model
string
The model of the device.
name
string
The name of the device.
os_hostname
string
The operating system hostname of the device.
os_name
string
The operating system name of the device.
os_version
string
The operating system version of the device.
ping_status
string
The ping status of the device.
product_name
string
The product name of the device.
serial_number
string
The serial number of the device.
status
string
The status of the device.
subnet
string
The subnet of the device.
sys_object_id
string
The device `sys_object_id`.
tags
[string]
A list of tags associated with the device.
vendor
string
The vendor of the device.
version
string
The version of the device.
id
string
The device ID
type
string
The type of the resource. The value should always be device.
```
{
  "data": {
    "attributes": {
      "description": "a device monitored with NDM",
      "device_type": "other",
      "integration": "snmp",
      "ip_address": "1.2.3.4",
      "location": "paris",
      "model": "xx-123",
      "name": "example device",
      "os_hostname": "1.0.2",
      "os_name": "example OS",
      "os_version": "1.0.2",
      "ping_status": "unmonitored",
      "product_name": "example device",
      "serial_number": "X12345",
      "status": "ok",
      "subnet": "1.2.3.4/24",
      "sys_object_id": "1.3.6.1.4.1.99999",
      "tags": [
        "device_ip:1.2.3.4",
        "device_id:example:1.2.3.4"
      ],
      "vendor": "example vendor",
      "version": "1.2.3"
    },
    "id": "example:1.2.3.4",
    "type": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=typescript)


#####  Get the device details
Copy
```
                  # Path parameters  
export device_id="example:1.2.3.4"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/devices/${device_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the device details
```
"""
Get the device details returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.get_device(
        device_id="default_device",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the device details
```
# Get the device details returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new
p api_instance.get_device("default_device")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the device details
```
// Get the device details returns "OK" response

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
	api := datadogV2.NewNetworkDeviceMonitoringApi(apiClient)
	resp, r, err := api.GetDevice(ctx, "default_device")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NetworkDeviceMonitoringApi.GetDevice`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NetworkDeviceMonitoringApi.GetDevice`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the device details
```
// Get the device details returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.NetworkDeviceMonitoringApi;
import com.datadog.api.client.v2.model.GetDeviceResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NetworkDeviceMonitoringApi apiInstance = new NetworkDeviceMonitoringApi(defaultClient);

    try {
      GetDeviceResponse result = apiInstance.getDevice("default_device");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkDeviceMonitoringApi#getDevice");
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

#####  Get the device details
```
// Get the device details returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_network_device_monitoring::NetworkDeviceMonitoringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = NetworkDeviceMonitoringAPI::with_config(configuration);
    let resp = api.get_device("default_device".to_string()).await;
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

#####  Get the device details
```
/**
 * Get the device details returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.NetworkDeviceMonitoringApi(configuration);

const params: v2.NetworkDeviceMonitoringApiGetDeviceRequest = {
  deviceId: "default_device",
};

apiInstance
  .getDevice(params)
  .then((data: v2.GetDeviceResponse) => {
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
## [Get the list of interfaces of the device](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-list-of-interfaces-of-the-device)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-list-of-interfaces-of-the-device-v2)


GET https://api.ap1.datadoghq.com/api/v2/ndm/interfaceshttps://api.ap2.datadoghq.com/api/v2/ndm/interfaceshttps://api.datadoghq.eu/api/v2/ndm/interfaceshttps://api.ddog-gov.com/api/v2/ndm/interfaceshttps://api.datadoghq.com/api/v2/ndm/interfaceshttps://api.us3.datadoghq.com/api/v2/ndm/interfaceshttps://api.us5.datadoghq.com/api/v2/ndm/interfaces
### Overview
Get the list of interfaces of the device.
### Arguments
#### Query Strings
Name
Type
Description
device_id [_required_]
string
The ID of the device to get interfaces from.
get_ip_addresses
boolean
Whether to get the IP addresses of the interfaces.
### Response
  * [200](https://docs.datadoghq.com/api/latest/network-device-monitoring/#GetInterfaces-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/network-device-monitoring/#GetInterfaces-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/network-device-monitoring/#GetInterfaces-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


The `GetInterfaces` operation’s response.
Field
Type
Description
data
[object]
Get Interfaces response
attributes
object
The interface attributes
alias
string
The interface alias
description
string
The interface description
index
int64
The interface index
ip_addresses
[string]
The interface IP addresses
mac_address
string
The interface MAC address
name
string
The interface name
status
enum
The interface status Allowed enum values: `up,down,warning,off`
id
string
The interface ID
type
string
The type of the resource. The value should always be interface.
```
{
  "data": [
    {
      "attributes": {
        "alias": "interface_0",
        "description": "a network interface",
        "index": 0,
        "ip_addresses": [
          "1.1.1.1",
          "1.1.1.2"
        ],
        "mac_address": "00:00:00:00:00:00",
        "name": "if0",
        "status": "up"
      },
      "id": "example:1.2.3.4:99",
      "type": "string"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=typescript)


#####  Get the list of interfaces of the device
Copy
```
                  # Required query arguments  
export device_id="example:1.2.3.4"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/interfaces?device_id=${device_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the list of interfaces of the device
```
"""
Get the list of interfaces of the device returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.get_interfaces(
        device_id="default:1.2.3.4",
        get_ip_addresses=True,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the list of interfaces of the device
```
# Get the list of interfaces of the device returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new
opts = {
  get_ip_addresses: true,
}
p api_instance.get_interfaces("default:1.2.3.4", opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the list of interfaces of the device
```
// Get the list of interfaces of the device returns "OK" response

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
	api := datadogV2.NewNetworkDeviceMonitoringApi(apiClient)
	resp, r, err := api.GetInterfaces(ctx, "default:1.2.3.4", *datadogV2.NewGetInterfacesOptionalParameters().WithGetIpAddresses(true))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NetworkDeviceMonitoringApi.GetInterfaces`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NetworkDeviceMonitoringApi.GetInterfaces`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the list of interfaces of the device
```
// Get the list of interfaces of the device returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.NetworkDeviceMonitoringApi;
import com.datadog.api.client.v2.api.NetworkDeviceMonitoringApi.GetInterfacesOptionalParameters;
import com.datadog.api.client.v2.model.GetInterfacesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NetworkDeviceMonitoringApi apiInstance = new NetworkDeviceMonitoringApi(defaultClient);

    try {
      GetInterfacesResponse result =
          apiInstance.getInterfaces(
              "default:1.2.3.4", new GetInterfacesOptionalParameters().getIpAddresses(true));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkDeviceMonitoringApi#getInterfaces");
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

#####  Get the list of interfaces of the device
```
// Get the list of interfaces of the device returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_network_device_monitoring::GetInterfacesOptionalParams;
use datadog_api_client::datadogV2::api_network_device_monitoring::NetworkDeviceMonitoringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = NetworkDeviceMonitoringAPI::with_config(configuration);
    let resp = api
        .get_interfaces(
            "default:1.2.3.4".to_string(),
            GetInterfacesOptionalParams::default().get_ip_addresses(true),
        )
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

#####  Get the list of interfaces of the device
```
/**
 * Get the list of interfaces of the device returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.NetworkDeviceMonitoringApi(configuration);

const params: v2.NetworkDeviceMonitoringApiGetInterfacesRequest = {
  deviceId: "default:1.2.3.4",
  getIpAddresses: true,
};

apiInstance
  .getInterfaces(params)
  .then((data: v2.GetInterfacesResponse) => {
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
## [Get the list of tags for a device](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-list-of-tags-for-a-device)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/network-device-monitoring/#get-the-list-of-tags-for-a-device-v2)


GET https://api.ap1.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.ap2.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.datadoghq.eu/api/v2/ndm/tags/devices/{device_id}https://api.ddog-gov.com/api/v2/ndm/tags/devices/{device_id}https://api.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.us3.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/{device_id}
### Overview
Get the list of tags for a device.
### Arguments
#### Path Parameters
Name
Type
Description
device_id [_required_]
string
The id of the device to fetch tags for.
### Response
  * [200](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDeviceUserTags-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDeviceUserTags-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDeviceUserTags-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/network-device-monitoring/#ListDeviceUserTags-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


List tags response.
Field
Type
Description
data
object
The list tags response data.
attributes
object
The definition of ListTagsResponseDataAttributes object.
tags
[string]
The list of tags
id
string
The device ID
type
string
The type of the resource. The value should always be tags.
```
{
  "data": {
    "attributes": {
      "tags": [
        "tag:test",
        "tag:testbis"
      ]
    },
    "id": "example:1.2.3.4",
    "type": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=typescript)


#####  Get the list of tags for a device
Copy
```
                  # Path parameters  
export device_id="example:1.2.3.4"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/${device_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get the list of tags for a device
```
"""
Get the list of tags for a device returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.list_device_user_tags(
        device_id="default_device",
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get the list of tags for a device
```
# Get the list of tags for a device returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new
p api_instance.list_device_user_tags("default_device")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get the list of tags for a device
```
// Get the list of tags for a device returns "OK" response

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
	api := datadogV2.NewNetworkDeviceMonitoringApi(apiClient)
	resp, r, err := api.ListDeviceUserTags(ctx, "default_device")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NetworkDeviceMonitoringApi.ListDeviceUserTags`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NetworkDeviceMonitoringApi.ListDeviceUserTags`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get the list of tags for a device
```
// Get the list of tags for a device returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.NetworkDeviceMonitoringApi;
import com.datadog.api.client.v2.model.ListTagsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NetworkDeviceMonitoringApi apiInstance = new NetworkDeviceMonitoringApi(defaultClient);

    try {
      ListTagsResponse result = apiInstance.listDeviceUserTags("default_device");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkDeviceMonitoringApi#listDeviceUserTags");
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

#####  Get the list of tags for a device
```
// Get the list of tags for a device returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_network_device_monitoring::NetworkDeviceMonitoringAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = NetworkDeviceMonitoringAPI::with_config(configuration);
    let resp = api
        .list_device_user_tags("default_device".to_string())
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

#####  Get the list of tags for a device
```
/**
 * Get the list of tags for a device returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.NetworkDeviceMonitoringApi(configuration);

const params: v2.NetworkDeviceMonitoringApiListDeviceUserTagsRequest = {
  deviceId: "default_device",
};

apiInstance
  .listDeviceUserTags(params)
  .then((data: v2.ListTagsResponse) => {
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
## [Update the tags for a device](https://docs.datadoghq.com/api/latest/network-device-monitoring/#update-the-tags-for-a-device)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/network-device-monitoring/#update-the-tags-for-a-device-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.ap2.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.datadoghq.eu/api/v2/ndm/tags/devices/{device_id}https://api.ddog-gov.com/api/v2/ndm/tags/devices/{device_id}https://api.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.us3.datadoghq.com/api/v2/ndm/tags/devices/{device_id}https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/{device_id}
### Overview
Update the tags for a device.
### Arguments
#### Path Parameters
Name
Type
Description
device_id [_required_]
string
The id of the device to update tags for.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


Field
Type
Description
data
object
The list tags response data.
attributes
object
The definition of ListTagsResponseDataAttributes object.
tags
[string]
The list of tags
id
string
The device ID
type
string
The type of the resource. The value should always be tags.
```
{
  "data": {
    "attributes": {
      "tags": [
        "tag:test",
        "tag:testbis"
      ]
    },
    "id": "default_device",
    "type": "tags"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/network-device-monitoring/#UpdateDeviceUserTags-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/network-device-monitoring/#UpdateDeviceUserTags-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/network-device-monitoring/#UpdateDeviceUserTags-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/network-device-monitoring/#UpdateDeviceUserTags-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


List tags response.
Field
Type
Description
data
object
The list tags response data.
attributes
object
The definition of ListTagsResponseDataAttributes object.
tags
[string]
The list of tags
id
string
The device ID
type
string
The type of the resource. The value should always be tags.
```
{
  "data": {
    "attributes": {
      "tags": [
        "tag:test",
        "tag:testbis"
      ]
    },
    "id": "example:1.2.3.4",
    "type": "string"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Model](https://docs.datadoghq.com/api/latest/network-device-monitoring/)
  * [Example](https://docs.datadoghq.com/api/latest/network-device-monitoring/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/network-device-monitoring/?code-lang=typescript)


#####  Update the tags for a device returns "OK" response
Copy
```
                          # Path parameters  
export device_id="example:1.2.3.4"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/${device_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "tags": [
        "tag:test",
        "tag:testbis"
      ]
    },
    "id": "default_device",
    "type": "tags"
  }
}
EOF  

                        
```

#####  Update the tags for a device returns "OK" response
```
// Update the tags for a device returns "OK" response

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
	body := datadogV2.ListTagsResponse{
		Data: &datadogV2.ListTagsResponseData{
			Attributes: &datadogV2.ListTagsResponseDataAttributes{
				Tags: []string{
					"tag:test",
					"tag:testbis",
				},
			},
			Id:   datadog.PtrString("default_device"),
			Type: datadog.PtrString("tags"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewNetworkDeviceMonitoringApi(apiClient)
	resp, r, err := api.UpdateDeviceUserTags(ctx, "default_device", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NetworkDeviceMonitoringApi.UpdateDeviceUserTags`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NetworkDeviceMonitoringApi.UpdateDeviceUserTags`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update the tags for a device returns "OK" response
```
// Update the tags for a device returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.NetworkDeviceMonitoringApi;
import com.datadog.api.client.v2.model.ListTagsResponse;
import com.datadog.api.client.v2.model.ListTagsResponseData;
import com.datadog.api.client.v2.model.ListTagsResponseDataAttributes;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NetworkDeviceMonitoringApi apiInstance = new NetworkDeviceMonitoringApi(defaultClient);

    ListTagsResponse body =
        new ListTagsResponse()
            .data(
                new ListTagsResponseData()
                    .attributes(
                        new ListTagsResponseDataAttributes()
                            .tags(Arrays.asList("tag:test", "tag:testbis")))
                    .id("default_device")
                    .type("tags"));

    try {
      ListTagsResponse result = apiInstance.updateDeviceUserTags("default_device", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkDeviceMonitoringApi#updateDeviceUserTags");
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

#####  Update the tags for a device returns "OK" response
```
"""
Update the tags for a device returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi
from datadog_api_client.v2.model.list_tags_response import ListTagsResponse
from datadog_api_client.v2.model.list_tags_response_data import ListTagsResponseData
from datadog_api_client.v2.model.list_tags_response_data_attributes import ListTagsResponseDataAttributes

body = ListTagsResponse(
    data=ListTagsResponseData(
        attributes=ListTagsResponseDataAttributes(
            tags=[
                "tag:test",
                "tag:testbis",
            ],
        ),
        id="default_device",
        type="tags",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.update_device_user_tags(device_id="default_device", body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update the tags for a device returns "OK" response
```
# Update the tags for a device returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new

body = DatadogAPIClient::V2::ListTagsResponse.new({
  data: DatadogAPIClient::V2::ListTagsResponseData.new({
    attributes: DatadogAPIClient::V2::ListTagsResponseDataAttributes.new({
      tags: [
        "tag:test",
        "tag:testbis",
      ],
    }),
    id: "default_device",
    type: "tags",
  }),
})
p api_instance.update_device_user_tags("default_device", body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update the tags for a device returns "OK" response
```
// Update the tags for a device returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_network_device_monitoring::NetworkDeviceMonitoringAPI;
use datadog_api_client::datadogV2::model::ListTagsResponse;
use datadog_api_client::datadogV2::model::ListTagsResponseData;
use datadog_api_client::datadogV2::model::ListTagsResponseDataAttributes;

#[tokio::main]
async fn main() {
    let body = ListTagsResponse::new().data(
        ListTagsResponseData::new()
            .attributes(
                ListTagsResponseDataAttributes::new()
                    .tags(vec!["tag:test".to_string(), "tag:testbis".to_string()]),
            )
            .id("default_device".to_string())
            .type_("tags".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = NetworkDeviceMonitoringAPI::with_config(configuration);
    let resp = api
        .update_device_user_tags("default_device".to_string(), body)
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

#####  Update the tags for a device returns "OK" response
```
/**
 * Update the tags for a device returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.NetworkDeviceMonitoringApi(configuration);

const params: v2.NetworkDeviceMonitoringApiUpdateDeviceUserTagsRequest = {
  body: {
    data: {
      attributes: {
        tags: ["tag:test", "tag:testbis"],
      },
      id: "default_device",
      type: "tags",
    },
  },
  deviceId: "default_device",
};

apiInstance
  .updateDeviceUserTags(params)
  .then((data: v2.ListTagsResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=7bfc6e4e-3957-4b28-836c-4394ebabea1a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d0e1e88c-cee3-4d98-9977-dde9c3ba8306&pt=Network%20Device%20Monitoring&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fnetwork-device-monitoring%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=7bfc6e4e-3957-4b28-836c-4394ebabea1a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=d0e1e88c-cee3-4d98-9977-dde9c3ba8306&pt=Network%20Device%20Monitoring&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fnetwork-device-monitoring%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=f8cb8352-2655-45f4-9002-45cb5899e364&bo=2&sid=e7969980f0bf11f08c054320cbbd0092&vid=e7972810f0bf11f09bf29f699b2daf47&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Network%20Device%20Monitoring&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fnetwork-device-monitoring%2F&r=&lt=1239&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=811024)
