# Source: https://docs.datadoghq.com/api/latest/network-device-monitoring.md

---
title: Network Device Monitoring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Network Device Monitoring
---

# Network Device Monitoring

The Network Device Monitoring API allows you to fetch devices and interfaces and their attributes. See the [Network Device Monitoring page](https://docs.datadoghq.com/network_monitoring/) for more information.

## Get the list of devices{% #get-the-list-of-devices %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/ndm/devices |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/ndm/devices |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/ndm/devices      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/ndm/devices      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/ndm/devices     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/ndm/devices |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/ndm/devices |

### Overview

Get the list of devices.

### Arguments

#### Query Strings

| Name         | Type    | Description                                              |
| ------------ | ------- | -------------------------------------------------------- |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100. |
| page[number] | integer | Specific page number to return.                          |
| sort         | string  | The field to sort the devices by.                        |
| filter[tag]  | string  | Filter devices by tag.                                   |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List devices response.

| Parent field       | Field                | Type     | Description                                                  |
| ------------------ | -------------------- | -------- | ------------------------------------------------------------ |
|                    | data                 | [object] | The list devices response data.                              |
| data               | attributes           | object   | The device attributes                                        |
| attributes         | description          | string   | The device description                                       |
| attributes         | device_type          | string   | The device type                                              |
| attributes         | integration          | string   | The device integration                                       |
| attributes         | interface_statuses   | object   | Count of the device interfaces by status                     |
| interface_statuses | down                 | int64    | The number of interfaces that are down                       |
| interface_statuses | off                  | int64    | The number of interfaces that are off                        |
| interface_statuses | up                   | int64    | The number of interfaces that are up                         |
| interface_statuses | warning              | int64    | The number of interfaces that are in a warning state         |
| attributes         | ip_address           | string   | The device IP address                                        |
| attributes         | location             | string   | The device location                                          |
| attributes         | model                | string   | The device model                                             |
| attributes         | name                 | string   | The device name                                              |
| attributes         | os_hostname          | string   | The device OS hostname                                       |
| attributes         | os_name              | string   | The device OS name                                           |
| attributes         | os_version           | string   | The device OS version                                        |
| attributes         | ping_status          | string   | The device ping status                                       |
| attributes         | product_name         | string   | The device product name                                      |
| attributes         | serial_number        | string   | The device serial number                                     |
| attributes         | status               | string   | The device SNMP status                                       |
| attributes         | subnet               | string   | The device subnet                                            |
| attributes         | sys_object_id        | string   | The device `sys_object_id`                                   |
| attributes         | tags                 | [string] | The list of device tags                                      |
| attributes         | vendor               | string   | The device vendor                                            |
| attributes         | version              | string   | The device version                                           |
| data               | id                   | string   | The device ID                                                |
| data               | type                 | string   | The type of the resource. The value should always be device. |
|                    | meta                 | object   | Object describing meta attributes of response.               |
| meta               | page                 | object   | Pagination object.                                           |
| page               | total_filtered_count | int64    | Total count of devices matched by the filter.                |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/devices" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get the device details{% #get-the-device-details %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/ndm/devices/{device_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/ndm/devices/{device_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/ndm/devices/{device_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/ndm/devices/{device_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/ndm/devices/{device_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/ndm/devices/{device_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/ndm/devices/{device_id} |

### Overview

Get the device details.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                    |
| --------------------------- | ------ | ------------------------------ |
| device_id [*required*] | string | The id of the device to fetch. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The `GetDevice` operation's response.

| Parent field | Field         | Type     | Description                                                  |
| ------------ | ------------- | -------- | ------------------------------------------------------------ |
|              | data          | object   | Get device response data.                                    |
| data         | attributes    | object   | The device attributes                                        |
| attributes   | description   | string   | A description of the device.                                 |
| attributes   | device_type   | string   | The type of the device.                                      |
| attributes   | integration   | string   | The integration of the device.                               |
| attributes   | ip_address    | string   | The IP address of the device.                                |
| attributes   | location      | string   | The location of the device.                                  |
| attributes   | model         | string   | The model of the device.                                     |
| attributes   | name          | string   | The name of the device.                                      |
| attributes   | os_hostname   | string   | The operating system hostname of the device.                 |
| attributes   | os_name       | string   | The operating system name of the device.                     |
| attributes   | os_version    | string   | The operating system version of the device.                  |
| attributes   | ping_status   | string   | The ping status of the device.                               |
| attributes   | product_name  | string   | The product name of the device.                              |
| attributes   | serial_number | string   | The serial number of the device.                             |
| attributes   | status        | string   | The status of the device.                                    |
| attributes   | subnet        | string   | The subnet of the device.                                    |
| attributes   | sys_object_id | string   | The device `sys_object_id`.                                  |
| attributes   | tags          | [string] | A list of tags associated with the device.                   |
| attributes   | vendor        | string   | The vendor of the device.                                    |
| attributes   | version       | string   | The version of the device.                                   |
| data         | id            | string   | The device ID                                                |
| data         | type          | string   | The type of the resource. The value should always be device. |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport device_id="example:1.2.3.4"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/devices/${device_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get the device details returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new
p api_instance.get_device("default_device")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get the list of interfaces of the device{% #get-the-list-of-interfaces-of-the-device %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/ndm/interfaces |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/ndm/interfaces |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/ndm/interfaces      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/ndm/interfaces      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/ndm/interfaces     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/ndm/interfaces |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/ndm/interfaces |

### Overview

Get the list of interfaces of the device.

### Arguments

#### Query Strings

| Name                        | Type    | Description                                        |
| --------------------------- | ------- | -------------------------------------------------- |
| device_id [*required*] | string  | The ID of the device to get interfaces from.       |
| get_ip_addresses            | boolean | Whether to get the IP addresses of the interfaces. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The `GetInterfaces` operation's response.

| Parent field | Field        | Type     | Description                                                     |
| ------------ | ------------ | -------- | --------------------------------------------------------------- |
|              | data         | [object] | Get Interfaces response                                         |
| data         | attributes   | object   | The interface attributes                                        |
| attributes   | alias        | string   | The interface alias                                             |
| attributes   | description  | string   | The interface description                                       |
| attributes   | index        | int64    | The interface index                                             |
| attributes   | ip_addresses | [string] | The interface IP addresses                                      |
| attributes   | mac_address  | string   | The interface MAC address                                       |
| attributes   | name         | string   | The interface name                                              |
| attributes   | status       | enum     | The interface status Allowed enum values: `up,down,warning,off` |
| data         | id           | string   | The interface ID                                                |
| data         | type         | string   | The type of the resource. The value should always be interface. |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Required query argumentsexport device_id="example:1.2.3.4"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/interfaces?device_id=${device_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get the list of interfaces of the device returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new
opts = {
  get_ip_addresses: true,
}
p api_instance.get_interfaces("default:1.2.3.4", opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get the list of tags for a device{% #get-the-list-of-tags-for-a-device %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/ndm/tags/devices/{device_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/ndm/tags/devices/{device_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/ndm/tags/devices/{device_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |

### Overview

Get the list of tags for a device.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                             |
| --------------------------- | ------ | --------------------------------------- |
| device_id [*required*] | string | The id of the device to fetch tags for. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List tags response.

| Parent field | Field      | Type     | Description                                                |
| ------------ | ---------- | -------- | ---------------------------------------------------------- |
|              | data       | object   | The list tags response data.                               |
| data         | attributes | object   | The definition of ListTagsResponseDataAttributes object.   |
| attributes   | tags       | [string] | The list of tags                                           |
| data         | id         | string   | The device ID                                              |
| data         | type       | string   | The type of the resource. The value should always be tags. |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Path parametersexport device_id="example:1.2.3.4"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/${device_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get the list of tags for a device returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::NetworkDeviceMonitoringAPI.new
p api_instance.list_device_user_tags("default_device")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update the tags for a device{% #update-the-tags-for-a-device %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/ndm/tags/devices/{device_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/ndm/tags/devices/{device_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/ndm/tags/devices/{device_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/{device_id} |

### Overview

Update the tags for a device.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                              |
| --------------------------- | ------ | ---------------------------------------- |
| device_id [*required*] | string | The id of the device to update tags for. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field      | Type     | Description                                                |
| ------------ | ---------- | -------- | ---------------------------------------------------------- |
|              | data       | object   | The list tags response data.                               |
| data         | attributes | object   | The definition of ListTagsResponseDataAttributes object.   |
| attributes   | tags       | [string] | The list of tags                                           |
| data         | id         | string   | The device ID                                              |
| data         | type       | string   | The type of the resource. The value should always be tags. |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List tags response.

| Parent field | Field      | Type     | Description                                                |
| ------------ | ---------- | -------- | ---------------------------------------------------------- |
|              | data       | object   | The list tags response data.                               |
| data         | attributes | object   | The definition of ListTagsResponseDataAttributes object.   |
| attributes   | tags       | [string] | The list of tags                                           |
| data         | id         | string   | The device ID                                              |
| data         | type       | string   | The type of the resource. The value should always be tags. |

{% /tab %}

{% tab title="Example" %}

```json
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
                          \# Path parametersexport device_id="example:1.2.3.4"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ndm/tags/devices/${device_id}" \
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
                        
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
