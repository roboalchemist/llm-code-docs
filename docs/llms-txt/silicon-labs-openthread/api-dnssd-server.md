# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-dnssd-server.md

# DNS-SD Server

This module includes APIs for DNS-SD server. 

## Modules

[otDnssdServiceInstanceInfo](ot-dnssd-service-instance-info)

[otDnssdHostInfo](ot-dnssd-host-info)

[otUpstreamDnsCounters](ot-upstream-dns-counters)

[otDnssdCounters](ot-dnssd-counters)

## Enumerations

### otDnssdQueryType

```
enum otDnssdQueryType {
    OT_DNSSD_QUERY_TYPE_NONE = 0
    OT_DNSSD_QUERY_TYPE_BROWSE = 1
    OT_DNSSD_QUERY_TYPE_RESOLVE = 2
    OT_DNSSD_QUERY_TYPE_RESOLVE_HOST = 3
}
```

**Description:**

Specifies a DNS-SD query type.

**Enumerator:**

|   |   |
|---|---|
|OT_DNSSD_QUERY_TYPE_NONE|Service type unspecified.|
|OT_DNSSD_QUERY_TYPE_BROWSE|Service type browse service.|
|OT_DNSSD_QUERY_TYPE_RESOLVE|Service type resolve service instance.|
|OT_DNSSD_QUERY_TYPE_RESOLVE_HOST|Service type resolve hostname.|

## Typedefs

### otDnssdQuerySubscribeCallback

`typedef void(* otDnssdQuerySubscribeCallback) (void *aContext, const char *aFullName)`

**Description:**

Is called when a DNS-SD query subscribes one of:

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to the application-specific context.|
||[in]|aFullName|The null-terminated full service name (e.g. "_ipps._tcp.default.service.arpa."), or full service instance name (e.g. "OpenThread._ipps._tcp.default.service.arpa."), or full host name (e.g. "ot-host.default.service.arpa.").|

**Details:**

1. a service name.
2. a service instance name.
3. a host name.

The DNS-SD query implementation is responsible for identifying what `aFullName` is. If `aFullName` is a service name or service instance name, the DNS-SD query implementation should discover corresponding service instance information and notify the DNS-SD server using `otDnssdQueryHandleDiscoveredServiceInstance`. If `aFullName` is a host name, the DNS-SD query implementation should discover the host information and notify the DNS-SD server using `otDnssdQueryHandleDiscoveredHost`.

**Note**

- There can be multiple subscription to the same name. DNS-SD query implementation should record the number of active subscriptions and stop notifying when there is no active subscription for `aFullName`.

**See Also**

- [otDnssdQueryHandleDiscoveredServiceInstance](api-dnssd-server#ot-dnssd-query-handle-discovered-service-instance)
- [otDnssdQueryHandleDiscoveredHost](api-dnssd-server#ot-dnssd-query-handle-discovered-host)

### otDnssdQueryUnsubscribeCallback

`typedef void(* otDnssdQueryUnsubscribeCallback) (void *aContext, const char *aFullName)`

**Description:**

Is called when a DNS-SD query unsubscribes one of:

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to the application-specific context.|
||[in]|aFullName|The null-terminated full service name (e.g. "_ipps._tcp.default.service.arpa."), or full service instance name (e.g. "OpenThread._ipps._tcp.default.service.arpa.").|

**Details:**

1. a service name.
2. a service instance name.
3. a host name.

The DNS-SD query implementation is responsible for identifying what `aFullName` is.

**Note**

- There can be multiple subscription to the same name. DNS-SD query implementation should record the number of active subscriptions and stop notifying when there is no active subscription for `aFullName`.

### otDnssdQuery

`typedef void otDnssdQuery`

**Description:**

This opaque type represents a DNS-SD query.

### otDnssdServiceInstanceInfo

`typedef struct otDnssdServiceInstanceInfo otDnssdServiceInstanceInfo`

**Description:**

Represents information of a discovered service instance for a DNS-SD query.

### otDnssdHostInfo

`typedef struct otDnssdHostInfo otDnssdHostInfo`

**Description:**

Represents information of a discovered host for a DNS-SD query.

### otUpstreamDnsCounters

`typedef struct otUpstreamDnsCounters otUpstreamDnsCounters`

**Description:**

Represents the count of queries, responses, failures handled by upstream DNS server.

**Details:**

Requires `OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE`.

### otDnssdCounters

`typedef struct otDnssdCounters otDnssdCounters`

**Description:**

Contains the counters of DNS-SD server.

## Functions

### otDnssdQuerySetCallbacks

`void otDnssdQuerySetCallbacks(otInstance *aInstance, otDnssdQuerySubscribeCallback aSubscribe, otDnssdQueryUnsubscribeCallback aUnsubscribe, void *aContext)`

**Description:** Sets DNS-SD server query callbacks.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|
|[otDnssdQuerySubscribeCallback](api-dnssd-server#ot-dnssd-query-subscribe-callback)|[in]|aSubscribe|A pointer to the callback function to subscribe a service or service instance.|
|[otDnssdQueryUnsubscribeCallback](api-dnssd-server#ot-dnssd-query-unsubscribe-callback)|[in]|aUnsubscribe|A pointer to the callback function to unsubscribe a service or service instance.|
|void *|[in]|aContext|A pointer to the application-specific context.|

The DNS-SD server calls `aSubscribe` to subscribe to a service or service instance to resolve a DNS-SD query and `aUnsubscribe` to unsubscribe when the query is resolved or timeout.

**Note**

- `aSubscribe` and `aUnsubscribe` must be both set or unset.

### otDnssdQueryHandleDiscoveredServiceInstance

`void otDnssdQueryHandleDiscoveredServiceInstance(otInstance *aInstance, const char *aServiceFullName, otDnssdServiceInstanceInfo *aInstanceInfo)`

**Description:** Notifies a discovered service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|
|const char *|[in]|aServiceFullName|The null-terminated full service name.|
|[otDnssdServiceInstanceInfo](ot-dnssd-service-instance-info) *|[in]|aInstanceInfo|A pointer to the discovered service instance information.|

The external query resolver (e.g. Discovery Proxy) should call this function to notify OpenThread core of the subscribed services or service instances.

**Note**

- `aInstanceInfo` must not contain unspecified or link-local or loop-back or multicast IP addresses.

### otDnssdQueryHandleDiscoveredHost

`void otDnssdQueryHandleDiscoveredHost(otInstance *aInstance, const char *aHostFullName, otDnssdHostInfo *aHostInfo)`

**Description:** Notifies a discovered host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|
|const char *|[in]|aHostFullName|The null-terminated full host name.|
|[otDnssdHostInfo](ot-dnssd-host-info) *|[in]|aHostInfo|A pointer to the discovered service instance information.|

The external query resolver (e.g. Discovery Proxy) should call this function to notify OpenThread core of the subscribed hosts.

**Note**

- `aHostInfo` must not contain unspecified or link-local or loop-back or multicast IP addresses.

### otDnssdGetNextQuery

`const otDnssdQuery * otDnssdGetNextQuery(otInstance *aInstance, const otDnssdQuery *aQuery)`

**Description:** Acquires the next query in the DNS-SD server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|
|const [otDnssdQuery](api-dnssd-server#ot-dnssd-query) *|[in]|aQuery|The query pointer. Pass NULL to get the first query.|

**Returns**

- A pointer to the query or NULL if no more queries.

### otDnssdGetQueryTypeAndName

`otDnssdQueryType otDnssdGetQueryTypeAndName(const otDnssdQuery *aQuery, char(*aNameOutput)[OT_DNS_MAX_NAME_SIZE])`

**Description:** Acquires the DNS-SD query type and name for a specific query.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnssdQuery](api-dnssd-server#ot-dnssd-query) *|[in]|aQuery|The query pointer acquired from `otDnssdGetNextQuery`.|
|char(*)|[out]|aNameOutput|The name output buffer, which should be `OT_DNS_MAX_NAME_SIZE` bytes long.|

**Returns**

- The DNS-SD query type.

### otDnssdGetCounters

`const otDnssdCounters * otDnssdGetCounters(otInstance *aInstance)`

**Description:** Returns the counters of the DNS-SD server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|

**Returns**

- A pointer to the counters of the DNS-SD server.

### otDnssdUpstreamQuerySetEnabled

`void otDnssdUpstreamQuerySetEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Enable or disable forwarding DNS queries to platform DNS upstream API.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnabled|A boolean to enable/disable forwarding DNS queries to upstream.|

Available when `OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE` is enabled.

**See Also**

- [otPlatDnsStartUpstreamQuery](plat-dns#ot-plat-dns-start-upstream-query)
- [otPlatDnsCancelUpstreamQuery](plat-dns#ot-plat-dns-cancel-upstream-query)
- [otPlatDnsUpstreamQueryDone](plat-dns#ot-plat-dns-upstream-query-done)

### otDnssdUpstreamQueryIsEnabled

`bool otDnssdUpstreamQueryIsEnabled(otInstance *aInstance)`

**Description:** Returns whether the DNSSD server will forward DNS queries to the platform DNS upstream API.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Available when `OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE` is enabled.

**See Also**

- [otDnssdUpstreamQuerySetEnabled](api-dnssd-server#ot-dnssd-upstream-query-set-enabled)