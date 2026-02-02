# Unifi API

**Version:** 9.1.120

**Last Updated:** 2026-02-01

---

## Overview

Unifi Controller API

### API Base URL

- https://{host}:{port}/proxy/network/api - Unifi Controller API
- https://{host}:{port}/api - Unifi Controller API

## API Endpoints


### Account

#### GET /s/{siteId}/rest/account

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/account

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/AccountCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/account/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/account/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/account/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/AccountUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### BroadcastGroup

#### GET /s/{siteId}/rest/broadcastgroup

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/broadcastgroup

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/BroadcastGroupCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/broadcastgroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/broadcastgroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/broadcastgroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/BroadcastGroupUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### ChannelPlan

#### GET /s/{siteId}/rest/channelplan

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/channelplan

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/ChannelPlanCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/channelplan/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/channelplan/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/channelplan/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/ChannelPlanUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### DHCPOption

#### GET /s/{siteId}/rest/dhcpoption

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/dhcpoption

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DHCPOptionCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/dhcpoption/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/dhcpoption/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/dhcpoption/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DHCPOptionUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### Dashboard

#### GET /s/{siteId}/rest/dashboard

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/dashboard

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DashboardCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/dashboard/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/dashboard/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/dashboard/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DashboardUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### Device

#### POST /s/{siteId}/rest/device

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DeviceCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/device/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### PUT /s/{siteId}/rest/device/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DeviceUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created

#### GET /s/{siteId}/stat/device

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/stat/device/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 


### DpiApp

#### GET /s/{siteId}/rest/dpiapp

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/dpiapp

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DpiAppCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/dpiapp/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/dpiapp/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/dpiapp/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DpiAppUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### DpiGroup

#### GET /s/{siteId}/rest/dpigroup

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/dpigroup

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DpiGroupCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/dpigroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/dpigroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/dpigroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DpiGroupUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### DynamicDNS

#### GET /s/{siteId}/rest/dynamicdns

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/dynamicdns

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DynamicDNSCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/dynamicdns/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/dynamicdns/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/dynamicdns/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/DynamicDNSUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### FirewallGroup

#### GET /s/{siteId}/rest/firewallgroup

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/firewallgroup

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/FirewallGroupCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/firewallgroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/firewallgroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/firewallgroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/FirewallGroupUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### FirewallRule

#### GET /s/{siteId}/rest/firewallrule

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/firewallrule

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/FirewallRuleCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/firewallrule/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/firewallrule/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/firewallrule/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/FirewallRuleUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### HeatMap

#### GET /s/{siteId}/rest/heatmap

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/heatmap

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HeatMapCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/heatmap/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/heatmap/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/heatmap/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HeatMapUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### HeatMapPoint

#### GET /s/{siteId}/rest/heatmappoint

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/heatmappoint

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HeatMapPointCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/heatmappoint/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/heatmappoint/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/heatmappoint/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HeatMapPointUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### Hotspot2Conf

#### GET /s/{siteId}/rest/hotspot2conf

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/hotspot2conf

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/Hotspot2ConfCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/hotspot2conf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/hotspot2conf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/hotspot2conf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/Hotspot2ConfUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### HotspotOp

#### GET /s/{siteId}/rest/hotspotop

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/hotspotop

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HotspotOpCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/hotspotop/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/hotspotop/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/hotspotop/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HotspotOpUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### HotspotPackage

#### GET /s/{siteId}/rest/hotspotpackage

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/hotspotpackage

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HotspotPackageCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/hotspotpackage/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/hotspotpackage/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/hotspotpackage/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/HotspotPackageUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### Map

#### GET /s/{siteId}/rest/map

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/map

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/MapCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/map/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/map/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/map/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/MapUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### MediaFile

#### GET /s/{siteId}/rest/mediafile

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/mediafile

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/MediaFileCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/mediafile/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/mediafile/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/mediafile/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/MediaFileUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### Network

#### GET /s/{siteId}/rest/networkconf

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/networkconf

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/NetworkCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/networkconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/networkconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/networkconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/NetworkUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### PortForward

#### GET /s/{siteId}/rest/portforward

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/portforward

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/PortForwardCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/portforward/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/portforward/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/portforward/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/PortForwardUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### PortProfile

#### GET /s/{siteId}/rest/portconf

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/portconf

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/PortProfileCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/portconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/portconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/portconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/PortProfileUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### RADIUSProfile

#### GET /s/{siteId}/rest/radiusprofile

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/radiusprofile

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/RADIUSProfileCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/radiusprofile/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/radiusprofile/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/radiusprofile/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/RADIUSProfileUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### Routing

#### GET /s/{siteId}/rest/routing

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/routing

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/RoutingCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/routing/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/routing/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/routing/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/RoutingUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### ScheduleTask

#### GET /s/{siteId}/rest/scheduletask

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/scheduletask

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/ScheduleTaskCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/scheduletask/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/scheduletask/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/scheduletask/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/ScheduleTaskUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingAutoSpeedtest

#### GET /s/{siteId}/get/setting/auto_speedtest

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/auto_speedtest

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingAutoSpeedtestUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingBaresip

#### GET /s/{siteId}/get/setting/baresip

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/baresip

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingBaresipUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingBroadcast

#### GET /s/{siteId}/get/setting/broadcast

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/broadcast

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingBroadcastUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingConnectivity

#### GET /s/{siteId}/get/setting/connectivity

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/connectivity

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingConnectivityUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingCountry

#### GET /s/{siteId}/get/setting/country

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/country

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingCountryUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingDashboard

#### GET /s/{siteId}/get/setting/dashboard

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/dashboard

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingDashboardUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingDoh

#### GET /s/{siteId}/get/setting/doh

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/doh

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingDohUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingDpi

#### GET /s/{siteId}/get/setting/dpi

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/dpi

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingDpiUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingElementAdopt

#### GET /s/{siteId}/get/setting/element_adopt

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/element_adopt

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingElementAdoptUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingEtherLighting

#### GET /s/{siteId}/get/setting/ether_lighting

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/ether_lighting

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingEtherLightingUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingEvaluationScore

#### GET /s/{siteId}/get/setting/evaluation_score

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/evaluation_score

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingEvaluationScoreUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingGlobalAp

#### GET /s/{siteId}/get/setting/global_ap

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/global_ap

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingGlobalApUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingGlobalNat

#### GET /s/{siteId}/get/setting/global_nat

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/global_nat

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingGlobalNatUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingGlobalSwitch

#### GET /s/{siteId}/get/setting/global_switch

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/global_switch

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingGlobalSwitchUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingGuestAccess

#### GET /s/{siteId}/get/setting/guest_access

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/guest_access

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingGuestAccessUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingIps

#### GET /s/{siteId}/get/setting/ips

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/ips

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingIpsUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingLcm

#### GET /s/{siteId}/get/setting/lcm

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/lcm

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingLcmUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingLocale

#### GET /s/{siteId}/get/setting/locale

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/locale

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingLocaleUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingMagicSiteToSiteVpn

#### GET /s/{siteId}/get/setting/magic_site_to_site_vpn

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/magic_site_to_site_vpn

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingMagicSiteToSiteVpnUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingMdns

#### GET /s/{siteId}/get/setting/mdns

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/mdns

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingMdnsUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingMgmt

#### GET /s/{siteId}/get/setting/mgmt

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/mgmt

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingMgmtUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingNetflow

#### GET /s/{siteId}/get/setting/netflow

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/netflow

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingNetflowUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingNetworkOptimization

#### GET /s/{siteId}/get/setting/network_optimization

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/network_optimization

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingNetworkOptimizationUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingNtp

#### GET /s/{siteId}/get/setting/ntp

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/ntp

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingNtpUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingPorta

#### GET /s/{siteId}/get/setting/porta

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/porta

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingPortaUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingRadioAi

#### GET /s/{siteId}/get/setting/radio_ai

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/radio_ai

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingRadioAiUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingRadius

#### GET /s/{siteId}/get/setting/radius

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/radius

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingRadiusUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingRsyslogd

#### GET /s/{siteId}/get/setting/rsyslogd

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/rsyslogd

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingRsyslogdUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSnmp

#### GET /s/{siteId}/get/setting/snmp

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/snmp

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSnmpUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSslInspection

#### GET /s/{siteId}/get/setting/ssl_inspection

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/ssl_inspection

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSslInspectionUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperCloudaccess

#### GET /s/{siteId}/get/setting/super_cloudaccess

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_cloudaccess

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperCloudaccessUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperEvents

#### GET /s/{siteId}/get/setting/super_events

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_events

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperEventsUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperFwupdate

#### GET /s/{siteId}/get/setting/super_fwupdate

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_fwupdate

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperFwupdateUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperIdentity

#### GET /s/{siteId}/get/setting/super_identity

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_identity

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperIdentityUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperMail

#### GET /s/{siteId}/get/setting/super_mail

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_mail

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperMailUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperMgmt

#### GET /s/{siteId}/get/setting/super_mgmt

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_mgmt

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperMgmtUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperSdn

#### GET /s/{siteId}/get/setting/super_sdn

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_sdn

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperSdnUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingSuperSmtp

#### GET /s/{siteId}/get/setting/super_smtp

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/super_smtp

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingSuperSmtpUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingTeleport

#### GET /s/{siteId}/get/setting/teleport

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/teleport

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingTeleportUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingTrafficFlow

#### GET /s/{siteId}/get/setting/traffic_flow

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/traffic_flow

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingTrafficFlowUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingUsg

#### GET /s/{siteId}/get/setting/usg

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/usg

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingUsgUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SettingUsw

#### GET /s/{siteId}/get/setting/usw

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/set/setting/usw

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SettingUswUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### SpatialRecord

#### GET /s/{siteId}/rest/spatialrecord

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/spatialrecord

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SpatialRecordCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/spatialrecord/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/spatialrecord/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/spatialrecord/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/SpatialRecordUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### Tag

#### GET /s/{siteId}/rest/tag

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/tag

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/TagCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/tag/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/tag/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/tag/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/TagUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### User

#### GET /s/{siteId}/rest/user

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/user

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/UserCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/user/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/user/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/user/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/UserUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### UserGroup

#### GET /s/{siteId}/rest/usergroup

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/usergroup

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/UserGroupCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/usergroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/usergroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/usergroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/UserGroupUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### VirtualDevice

#### GET /s/{siteId}/rest/virtualdevice

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/virtualdevice

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/VirtualDeviceCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/virtualdevice/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/virtualdevice/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/virtualdevice/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/VirtualDeviceUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### WLAN

#### GET /s/{siteId}/rest/wlanconf

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/wlanconf

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/WLANCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/wlanconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/wlanconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/wlanconf/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/WLANUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


### WLANGroup

#### GET /s/{siteId}/rest/wlangroup

**Parameters:**

- `siteId` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### POST /s/{siteId}/rest/wlangroup

**Parameters:**

- `siteId` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/WLANGroupCreateRequest"
}
```

**Responses:**

- **204**: No Content

#### DELETE /s/{siteId}/rest/wlangroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: OK

#### GET /s/{siteId}/rest/wlangroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Responses:**

- **200**: OK
- **default**: 

#### PUT /s/{siteId}/rest/wlangroup/{id}

**Parameters:**

- `siteId` (path) (required): 
- `id` (path) (required): 

**Request Body:**

```json
{
  "$ref": "#/components/schemas/WLANGroupUpdateRequest"
}
```

**Responses:**

- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **429**: Too Many Requests
- **500**: Internal Server Error
- **default**: Created


## Data Models

### Account

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "filter_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "ip": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "networkconf_id": {
      "type":
```

### AccountCreateRequest

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "filter_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "ip": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "networkconf_id": {
      "type":
```

### AccountResponse

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/Account"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "meta": {
      "$ref": "#/components/schemas/Meta"
    }
  },
  "type": "object"
}
```

### AccountUpdateRequest

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "filter_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "ip": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "networkconf_id": {
      "type":
```

### BroadcastGroup

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "member_table": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "name": {
      "type": "string"
    },
    "site_id": {
      "type": "string"
    }
  },
  "type": "object"
}
```

### BroadcastGroupCreateRequest

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "member_table": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "name": {
      "type": "string"
    },
    "site_id": {
      "type": "string"
    }
  },
  "type": "object"
}
```

### BroadcastGroupResponse

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/BroadcastGroup"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "meta": {
      "$ref": "#/components/schemas/Meta"
    }
  },
  "type": "object"
}
```

### BroadcastGroupUpdateRequest

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "member_table": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "name": {
      "type": "string"
    },
    "site_id": {
      "type": "string"
    }
  },
  "type": "object"
}
```

### ChannelPlan

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "ap_blacklisted_channels": {
      "items": {
        "$ref": "#/components/schemas/ChannelPlanApBlacklistedChannels"
      },
      "type": "array"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "conf_source": {
      "type": "string"
    },
    "couplin
```

### ChannelPlanApBlacklistedChannels

```json
{
  "properties": {
    "channel": {
      "type": "integer"
    },
    "mac": {
      "type": "string"
    },
    "timestamp": {
      "type": "integer"
    }
  },
  "type": "object"
}
```

### ChannelPlanCoupling

```json
{
  "properties": {
    "rssi": {
      "type": "integer"
    },
    "source": {
      "type": "string"
    },
    "target": {
      "type": "string"
    }
  },
  "type": "object"
}
```

### ChannelPlanCreateRequest

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "ap_blacklisted_channels": {
      "items": {
        "$ref": "#/components/schemas/ChannelPlanApBlacklistedChannels"
      },
      "type": "array"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "conf_source": {
      "type": "string"
    },
    "couplin
```

### ChannelPlanRadioTable

```json
{
  "properties": {
    "backup_channel": {
      "type": "string"
    },
    "channel": {
      "type": "string"
    },
    "device_mac": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "tx_power": {
      "type": "string"
    },
    "tx_power_mode": {
      "type": "string"
    },
    "width": {
      "type": "integer"
    }
  },
  "type": "object"
}
```

### ChannelPlanResponse

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/ChannelPlan"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "meta": {
      "$ref": "#/components/schemas/Meta"
    }
  },
  "type": "object"
}
```

### ChannelPlanSatisfactionTable

```json
{
  "properties": {
    "device_mac": {
      "type": "string"
    },
    "satisfaction": {
      "type": "number"
    }
  },
  "type": "object"
}
```

### ChannelPlanSiteBlacklistedChannels

```json
{
  "properties": {
    "channel": {
      "type": "integer"
    },
    "timestamp": {
      "type": "integer"
    }
  },
  "type": "object"
}
```

### ChannelPlanUpdateRequest

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "ap_blacklisted_channels": {
      "items": {
        "$ref": "#/components/schemas/ChannelPlanApBlacklistedChannels"
      },
      "type": "array"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "conf_source": {
      "type": "string"
    },
    "couplin
```

### DHCPOption

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "code": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "signed": {
      "type": "boolean"
    },
    "site_id": {
      "type": "string"
    },
    "type": {
      "type": "string"
    
```

### DHCPOptionCreateRequest

```json
{
  "properties": {
    "_id": {
      "type": "string"
    },
    "attr_hidden": {
      "type": "boolean"
    },
    "attr_hidden_id": {
      "type": "string"
    },
    "attr_no_delete": {
      "type": "boolean"
    },
    "attr_no_edit": {
      "type": "boolean"
    },
    "code": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "signed": {
      "type": "boolean"
    },
    "site_id": {
      "type": "string"
    },
    "type": {
      "type": "string"
    
```

### DHCPOptionResponse

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/DHCPOption"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "meta": {
      "$ref": "#/components/schemas/Meta"
    }
  },
  "type": "object"
}
```

