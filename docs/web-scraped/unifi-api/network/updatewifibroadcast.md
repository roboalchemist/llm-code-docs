# updatewifibroadcast

Source: https://developer.ui.com/network/v10.1.68/updatewifibroadcast

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Update Wifi Broadcast

PUT`/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}`

Update an existing Wifi Broadcast on the specified site.

path Parameters

wifiBroadcastId

required

string

siteId

required

string

request Body

type

required

string

STANDARDIOT\_OPTIMIZED

name

required

string

networkExpand

object (Wifi network reference)

enabled

required

boolean

securityConfigurationExpand

required

object

broadcastingDeviceFilterExpand

object (Broadcasting device filter)

Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.

mdnsProxyConfigurationExpand

object (mDNS filtering configuration)

multicastFilteringPolicyExpand

object (Multicast filtering policy)

multicastToUnicastConversionEnabled

required

boolean

clientIsolationEnabled

required

boolean

hideName

required

boolean

uapsdEnabled

required

boolean

Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled

basicDataRateKbpsByFrequencyGHzExpand

object

clientFilteringPolicyExpand

object

Client connection filtering policy. Allow/restrict access to the WiFi network based on client device MAC addresses.

blackoutScheduleConfigurationExpand

object

broadcastingFrequenciesGHzExpand

Array of number

hotspotConfigurationExpand

object (Wifi hotspot configuration)

mloEnabled

boolean

bandSteeringEnabled

boolean

arpProxyEnabled

boolean

bssTransitionEnabled

boolean

advertiseDeviceName

boolean

Indicates whether the device name is advertised in beacon frames.

dtimPeriodByFrequencyGHzOverrideExpand

object

## Responses

200

Response Schema: application/json

type

required

string

STANDARDIOT\_OPTIMIZED

id

required

string

name

required

string

metadataExpand

required

object (User or derived or orchestrated entity metadata)

enabled

required

boolean

networkExpand

object (Wifi network reference)

securityConfigurationExpand

required

object

broadcastingDeviceFilterExpand

object (Broadcasting device filter)

Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.

mdnsProxyConfigurationExpand

object (mDNS filtering configuration)

multicastFilteringPolicyExpand

object (Multicast filtering policy)

multicastToUnicastConversionEnabled

required

boolean

clientIsolationEnabled

required

boolean

hideName

required

boolean

uapsdEnabled

required

boolean

Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled

basicDataRateKbpsByFrequencyGHzExpand

object

clientFilteringPolicyExpand

object

Client connection filtering policy. Allow/restrict access to the WiFi network based on client device MAC addresses.

blackoutScheduleConfigurationExpand

object

broadcastingFrequenciesGHzExpand

Array of number

hotspotConfigurationExpand

object (Wifi hotspot configuration)

mloEnabled

boolean

bandSteeringEnabled

boolean

arpProxyEnabled

boolean

bssTransitionEnabled

boolean

advertiseDeviceName

boolean

Indicates whether the device name is advertised in beacon frames.

dtimPeriodByFrequencyGHzOverrideExpand

object

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X PUT "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"type\": \"string\",  \"name\": \"string\",  \"network\": {    \"type\": \"string\"  },  \"enabled\": true,  \"securityConfiguration\": {    \"type\": \"string\"  },  \"broadcastingDeviceFilter\": {    \"type\": \"string\"  },  \"mdnsProxyConfiguration\": {    \"mode\": \"string\"  },  \"multicastFilteringPolicy\": {    \"action\": \"string\"  },  \"multicastToUnicastConversionEnabled\": true,  \"clientIsolationEnabled\": true,  \"hideName\": true,  \"uapsdEnabled\": true,  \"basicDataRateKbpsByFrequencyGHz\": {    \"5\": 6000,    \"2.4\": 2000  },  \"clientFilteringPolicy\": {    \"action\": \"ALLOW\",    \"macAddressFilter\": [      \"string\"    ]  },  \"blackoutScheduleConfiguration\": {    \"days\": [      {        \"type\": \"string\",        \"day\": \"SUN\"      }    ]  }}"
```

Response Sample

200

```
{  "type": "string",  "id": "00000000-0000-0000-0000-000000000000",  "name": "string",  "metadata": {    "origin": "string"  },  "enabled": true,  "network": {    "type": "string"  },  "securityConfiguration": {    "type": "string",    "radiusConfiguration": null  },  "broadcastingDeviceFilter": {    "type": "string"  },  "mdnsProxyConfiguration": {    "mode": "string"  },  "multicastFilteringPolicy": {    "action": "string"  },  "multicastToUnicastConversionEnabled": true,  "clientIsolationEnabled": true,  "hideName": true,  "uapsdEnabled": true,  "basicDataRateKbpsByFrequencyGHz": {    "5": 0,    "2.4": 0  },  "clientFilteringPolicy": {    "action": "ALLOW",    "macAddressFilter": [      "string"    ]  },  "blackoutScheduleConfiguration": {    "days": [      {        "type": "string",        "day": "SUN"      }    ]  }}
```