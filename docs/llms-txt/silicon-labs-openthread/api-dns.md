# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-dns.md

# DNS

This module includes functions that control DNS communication. 

The functions in this module are available only if feature `OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE` is enabled. 

## Modules

[otDnsTxtEntry](ot-dns-txt-entry)

[otDnsTxtEntryIterator](ot-dns-txt-entry-iterator)

[otDnsQueryConfig](ot-dns-query-config)

[otDnsServiceInfo](ot-dns-service-info)

[otDnsRecordInfo](ot-dns-record-info)

## Enumerations

### otDnsRecursionFlag

```
enum otDnsRecursionFlag {
    OT_DNS_FLAG_UNSPECIFIED = 0
    OT_DNS_FLAG_RECURSION_DESIRED = 1
    OT_DNS_FLAG_NO_RECURSION = 2
}
```

**Description:**

Type represents the "Recursion Desired" (RD) flag in an `otDnsQueryConfig`.

**Enumerator:**

|   |   |
|---|---|
|OT_DNS_FLAG_UNSPECIFIED|Indicates the flag is not specified.|
|OT_DNS_FLAG_RECURSION_DESIRED|Indicates DNS name server can resolve the query recursively.|
|OT_DNS_FLAG_NO_RECURSION|Indicates DNS name server can not resolve the query recursively.|

### otDnsNat64Mode

```
enum otDnsNat64Mode {
    OT_DNS_NAT64_UNSPECIFIED = 0
    OT_DNS_NAT64_ALLOW = 1
    OT_DNS_NAT64_DISALLOW = 2
}
```

**Description:**

Type represents the NAT64 mode in an `otDnsQueryConfig`.

**Details:**

The NAT64 mode indicates whether to allow or disallow NAT64 address translation during DNS client address resolution. This mode is only used when `OPENTHREAD_CONFIG_DNS_CLIENT_NAT64_ENABLE` is enabled.

**Enumerator:**

|   |   |
|---|---|
|OT_DNS_NAT64_UNSPECIFIED|NAT64 mode is not specified. Use default NAT64 mode.|
|OT_DNS_NAT64_ALLOW|Allow NAT64 address translation during DNS client address resolution.|
|OT_DNS_NAT64_DISALLOW|Do not allow NAT64 address translation during DNS client address resolution.|

### otDnsServiceMode

```
enum otDnsServiceMode {
    OT_DNS_SERVICE_MODE_UNSPECIFIED = 0
    OT_DNS_SERVICE_MODE_SRV = 1
    OT_DNS_SERVICE_MODE_TXT = 2
    OT_DNS_SERVICE_MODE_SRV_TXT = 3
    OT_DNS_SERVICE_MODE_SRV_TXT_SEPARATE = 4
    OT_DNS_SERVICE_MODE_SRV_TXT_OPTIMIZE = 5
}
```

**Description:**

Type represents the service resolution mode in an `otDnsQueryConfig`.

**Details:**

This is only used during DNS client service resolution `otDnsClientResolveService()`. It determines which record types to query.

**Enumerator:**

|   |   |
|---|---|
|OT_DNS_SERVICE_MODE_UNSPECIFIED|Mode is not specified. Use default service mode.|
|OT_DNS_SERVICE_MODE_SRV|Query for SRV record only.|
|OT_DNS_SERVICE_MODE_TXT|Query for TXT record only.|
|OT_DNS_SERVICE_MODE_SRV_TXT|Query for both SRV and TXT records in same message.|
|OT_DNS_SERVICE_MODE_SRV_TXT_SEPARATE|Query in parallel for SRV and TXT using separate messages.|
|OT_DNS_SERVICE_MODE_SRV_TXT_OPTIMIZE|Query for TXT/SRV together first, if fails then query separately.|

### otDnsTransportProto

```
enum otDnsTransportProto {
    OT_DNS_TRANSPORT_UNSPECIFIED = 0
    OT_DNS_TRANSPORT_UDP = 1
    OT_DNS_TRANSPORT_TCP = 2
}
```

**Description:**

Type represents the DNS transport protocol in an `otDnsQueryConfig`.

**Details:**

This `OT_DNS_TRANSPORT_TCP` is only supported when `OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE` is enabled.

**Enumerator:**

|   |   |
|---|---|
|OT_DNS_TRANSPORT_UNSPECIFIED||
|OT_DNS_TRANSPORT_UDP|DNS transport is unspecified.|
|OT_DNS_TRANSPORT_TCP|DNS query should be sent via UDP.|

### otDnsRecordSection

```
enum otDnsRecordSection {
    OT_DNS_SECTION_ANSWER
    OT_DNS_SECTION_AUTHORITY
    OT_DNS_SECTION_ADDITIONAL
}
```

**Description:**

Represents a section in a DNS query/response message.

**Enumerator:**

|   |   |
|---|---|
|OT_DNS_SECTION_ANSWER|Answer section.|
|OT_DNS_SECTION_AUTHORITY|Authority section.|
|OT_DNS_SECTION_ADDITIONAL|Additional section.|

## Typedefs

### otDnsTxtEntry

`typedef struct otDnsTxtEntry otDnsTxtEntry`

**Description:**

Represents a TXT record entry representing a key/value pair (RFC 6763 - section 6.3).

**Details:**

The string buffers pointed to by `mKey` and `mValue` MUST persist and remain unchanged after an instance of such structure is passed to OpenThread (as part of `otSrpClientService` instance).

An array of `otDnsTxtEntry` entries are used in `otSrpClientService` to specify the full TXT record (a list of entries).

### otDnsTxtEntryIterator

`typedef struct otDnsTxtEntryIterator otDnsTxtEntryIterator`

**Description:**

Represents an iterator for TXT record entries (key/value pairs).

**Details:**

The data fields in this structure are intended for use by OpenThread core and caller should not read or change them.

### otDnsQueryConfig

`typedef struct otDnsQueryConfig otDnsQueryConfig`

**Description:**

Represents a DNS query configuration.

**Details:**

Any of the fields in this structure can be set to zero to indicate that it is not specified. How the unspecified fields are treated is determined by the function which uses the instance of `otDnsQueryConfig`.

### otDnsAddressResponse

`typedef struct otDnsAddressResponse otDnsAddressResponse`

**Description:**

An opaque representation of a response to an address resolution DNS query.

**Details:**

Pointers to instance of this type are provided from callback `otDnsAddressCallback`.

### otDnsAddressCallback

`typedef void(* otDnsAddressCallback) (otError aError, const otDnsAddressResponse *aResponse, void *aContext)`

**Description:**

Pointer is called when a DNS response is received for an address resolution query.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aError|The result of the DNS transaction.|
||[in]|aResponse|A pointer to the response (it is always non-NULL).|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

Within this callback the user can use `otDnsAddressResponseGet{Item}()` functions along with the `aResponse` pointer to get more info about the response.

The `aResponse` pointer can only be used within this callback and after returning from this function it will not stay valid, so the user MUST NOT retain the `aResponse` pointer for later use.

The `aError` can have the following:

- OT_ERROR_NONE A response was received successfully.
- OT_ERROR_ABORT A DNS transaction was aborted by stack.
- OT_ERROR_RESPONSE_TIMEOUT No DNS response has been received within timeout.

If the server rejects the address resolution request the error code from server is mapped as follow:

- (0) NOERROR Success (no error condition) -> OT_ERROR_NONE
- (1) FORMERR Server unable to interpret due to format error -> OT_ERROR_PARSE
- (2) SERVFAIL Server encountered an internal failure -> OT_ERROR_FAILED
- (3) NXDOMAIN Name that ought to exist, does not exist -> OT_ERROR_NOT_FOUND
- (4) NOTIMP Server does not support the query type (OpCode) -> OT_ERROR_NOT_IMPLEMENTED
- (5) REFUSED Server refused for policy/security reasons -> OT_ERROR_SECURITY
- (6) YXDOMAIN Some name that ought not to exist, does exist -> OT_ERROR_DUPLICATED
- (7) YXRRSET Some RRset that ought not to exist, does exist -> OT_ERROR_DUPLICATED
- (8) NXRRSET Some RRset that ought to exist, does not exist -> OT_ERROR_NOT_FOUND
- (9) NOTAUTH Service is not authoritative for zone -> OT_ERROR_SECURITY
- (10) NOTZONE A name is not in the zone -> OT_ERROR_PARSE
- (20) BADNAME Bad name -> OT_ERROR_PARSE
- (21) BADALG Bad algorithm -> OT_ERROR_SECURITY
- (22) BADTRUN Bad truncation -> OT_ERROR_PARSE
- Other response codes -> OT_ERROR_FAILED

### otDnsBrowseResponse

`typedef struct otDnsBrowseResponse otDnsBrowseResponse`

**Description:**

An opaque representation of a response to a browse (service instance enumeration) DNS query.

**Details:**

Pointers to instance of this type are provided from callback `otDnsBrowseCallback`.

### otDnsBrowseCallback

`typedef void(* otDnsBrowseCallback) (otError aError, const otDnsBrowseResponse *aResponse, void *aContext)`

**Description:**

Pointer is called when a DNS response is received for a browse (service instance enumeration) query.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aError|The result of the DNS transaction.|
||[in]|aResponse|A pointer to the response (it is always non-NULL).|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

Within this callback the user can use `otDnsBrowseResponseGet{Item}()` functions along with the `aResponse` pointer to get more info about the response.

The `aResponse` pointer can only be used within this callback and after returning from this function it will not stay valid, so the user MUST NOT retain the `aResponse` pointer for later use.

For the full list of possible values for `aError`, please see `otDnsAddressCallback()`.

### otDnsServiceInfo

`typedef struct otDnsServiceInfo otDnsServiceInfo`

**Description:**

Provides info for a DNS service instance.

### otDnsServiceResponse

`typedef struct otDnsServiceResponse otDnsServiceResponse`

**Description:**

An opaque representation of a response to a service instance resolution DNS query.

**Details:**

Pointers to instance of this type are provided from callback `otDnsAddressCallback`.

### otDnsServiceCallback

`typedef void(* otDnsServiceCallback) (otError aError, const otDnsServiceResponse *aResponse, void *aContext)`

**Description:**

Pointer is called when a DNS response is received for a service instance resolution query.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aError|The result of the DNS transaction.|
||[in]|aResponse|A pointer to the response (it is always non-NULL).|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

Within this callback the user can use `otDnsServiceResponseGet{Item}()` functions along with the `aResponse` pointer to get more info about the response.

The `aResponse` pointer can only be used within this callback and after returning from this function it will not stay valid, so the user MUST NOT retain the `aResponse` pointer for later use.

For the full list of possible values for `aError`, please see `otDnsAddressCallback()`.

### otDnsRecordResponse

`typedef struct otDnsRecordResponse otDnsRecordResponse`

**Description:**

An opaque representation of a response to a query for an arbitrary record type.

**Details:**

Pointers to instance of this type are provided from callback `otDnsRecordCallback`.

### otDnsRecordCallback

`typedef void(* otDnsRecordCallback) (otError aError, const otDnsRecordResponse *aResponse, void *aContext)`

**Description:**

Pointer is called when a DNS response is received for a DNS query to an arbitrary record type.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aError|The result of the DNS transaction.|
||[in]|aResponse|A pointer to the response (it is always non-NULL).|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

Within this callback the user can use `otDnsRecordResponseGet{Item}()` functions along with the `aResponse` pointer to get more info about the response.

The `aResponse` pointer can only be used within this callback and after returning from this function it will not stay valid, so the user MUST NOT retain the `aResponse` pointer for later use.

The `aError` can have the following:

- OT_ERROR_NONE A response was received successfully.
- OT_ERROR_ABORT A DNS transaction was aborted by the stack.
- OT_ERROR_RESPONSE_TIMEOUT No DNS response has been received within timeout.

### otDnsRecordInfo

`typedef struct otDnsRecordInfo otDnsRecordInfo`

**Description:**

Represents info for a record in an `otDnsRecordResponse`.

**Details:**

This struct is used as input to `otDnsRecordResponseGetRecordInfo()`.

## Functions

### otDnsInitTxtEntryIterator

`void otDnsInitTxtEntryIterator(otDnsTxtEntryIterator *aIterator, const uint8_t *aTxtData, uint16_t aTxtDataLength)`

**Description:** Initializes a TXT record iterator.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otDnsTxtEntryIterator](ot-dns-txt-entry-iterator) *|[in]|aIterator|A pointer to the iterator to initialize (MUST NOT be NULL).|
|const uint8_t *|[in]|aTxtData|A pointer to buffer containing the encoded TXT data.|
|uint16_t|[in]|aTxtDataLength|The length (number of bytes) of `aTxtData`.|

The buffer pointer `aTxtData` and its content MUST persist and remain unchanged while `aIterator` object is being used.

### otDnsGetNextTxtEntry

`otError otDnsGetNextTxtEntry(otDnsTxtEntryIterator *aIterator, otDnsTxtEntry *aEntry)`

**Description:** Parses the TXT data from an iterator and gets the next TXT record entry (key/value pair).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otDnsTxtEntryIterator](ot-dns-txt-entry-iterator) *|[in]|aIterator|A pointer to the iterator (MUST NOT be NULL).|
|[otDnsTxtEntry](ot-dns-txt-entry) *|[out]|aEntry|A pointer to a `otDnsTxtEntry` structure to output the parsed/read entry (MUST NOT be NULL).|

The `aIterator` MUST be initialized using `otDnsInitTxtEntryIterator()` before calling this function and the TXT data buffer used to initialize the iterator MUST persist and remain unchanged. Otherwise the behavior of this function is undefined.

If the parsed key string length is smaller than or equal to `OT_DNS_TXT_KEY_ITER_MAX_LENGTH` the key string is returned in `mKey` in `aEntry`. But if the key is longer, then `mKey` is set to NULL and the entire encoded TXT entry string is returned in `mValue` and `mValueLength`.

### otDnsEncodeTxtData

`otError otDnsEncodeTxtData(const otDnsTxtEntry *aTxtEntries, uint16_t aNumTxtEntries, uint8_t *aTxtData, uint16_t *aTxtDataLength)`

**Description:** Encodes a given list of TXT record entries (key/value pairs) into TXT data (following format specified by RFC 6763).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsTxtEntry](ot-dns-txt-entry) *|[in]|aTxtEntries|Pointer to an array of `otDnsTxtEntry`.|
|uint16_t|[in]|aNumTxtEntries|Number of entries in `aTxtEntries` array.|
|uint8_t *|[out]|aTxtData|A pointer to a buffer to output the encoded TXT data.|
|uint16_t *|[inout]|aTxtDataLength|On input, size of buffer `aTxtData`. On output, length of the encoded TXT data.|

### otDnsSetNameCompressionEnabled

`void otDnsSetNameCompressionEnabled(bool aEnabled)`

**Description:** Enables/disables the "DNS name compression" mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|bool|[in]|aEnabled|TRUE to enable the "DNS name compression" mode, FALSE to disable.|

By default DNS name compression is enabled. When disabled, DNS names are appended as full and never compressed. This is applicable to OpenThread's DNS and SRP client/server modules.

This is intended for testing only and available when `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` config is enabled.

Note that in the case `OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE` is used, this mode applies to all OpenThread instances (i.e., calling this function enables/disables the compression mode on all OpenThread instances).

### otDnsIsNameCompressionEnabled

`bool otDnsIsNameCompressionEnabled(void)`

**Description:** Indicates whether the "DNS name compression" mode is enabled or not.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|void|N/A|undefined||

This is intended for testing only and available when `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` config is enabled.

**Returns**

- TRUE if the "DNS name compression" mode is enabled, FALSE otherwise.

### otDnsClientGetDefaultConfig

`const otDnsQueryConfig * otDnsClientGetDefaultConfig(otInstance *aInstance)`

**Description:** Gets the current default query config used by DNS client.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

When OpenThread stack starts, the default DNS query config is determined from a set of OT config options such as `OPENTHREAD_CONFIG_DNS_CLIENT_DEFAULT_SERVER_IP6_ADDRESS`, `_DEFAULT_SERVER_PORT`, `_DEFAULT_RESPONSE_TIMEOUT`, etc. (see `config/dns_client.h` for all related config options).

**Returns**

- A pointer to the current default config being used by DNS client.

### otDnsClientSetDefaultConfig

`void otDnsClientSetDefaultConfig(otInstance *aInstance, const otDnsQueryConfig *aConfig)`

**Description:** Sets the default query config on DNS client.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otDnsQueryConfig](ot-dns-query-config) *|[in]|aConfig|A pointer to the new query config to use as default.|

**Note**

- Any ongoing query will continue to use the config from when it was started. The new default config will be used for any future DNS queries.

The `aConfig` can be NULL. In this case the default config will be set to the defaults from OT config options `OPENTHREAD_CONFIG_DNS_CLIENT_DEFAULT_{}`. This resets the default query config back to to the config when the OpenThread stack starts.

In a non-NULL `aConfig`, caller can choose to leave some of the fields in `otDnsQueryConfig` instance unspecified (value zero). The unspecified fields are replaced by the corresponding OT config option definitions `OPENTHREAD_CONFIG_DNS_CLIENT_DEFAULT_{}` to form the default query config.

When `OPENTHREAD_CONFIG_DNS_CLIENT_DEFAULT_SERVER_ADDRESS_AUTO_SET_ENABLE` is enabled, the server's IPv6 address in the default config is automatically set and updated by DNS client. This is done only when user does not explicitly set or specify it. This behavior requires SRP client and its auto-start feature to be enabled. SRP client will then monitor the Thread Network Data for DNS/SRP Service entries to select an SRP server. The selected SRP server address is also set as the DNS server address in the default config.

### otDnsClientResolveAddress

`otError otDnsClientResolveAddress(otInstance *aInstance, const char *aHostName, otDnsAddressCallback aCallback, void *aContext, const otDnsQueryConfig *aConfig)`

**Description:** Sends an address resolution DNS query for AAAA (IPv6) record(s) for a given host name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const char *|[in]|aHostName|The host name for which to query the address (MUST NOT be NULL).|
|[otDnsAddressCallback](api-dns#ot-dns-address-callback)|[in]|aCallback|A function pointer that shall be called on response reception or time-out.|
|void *|[in]|aContext|A pointer to arbitrary context information.|
|const [otDnsQueryConfig](ot-dns-query-config) *|[in]|aConfig|A pointer to the config to use for this query.|

The `aConfig` can be NULL. In this case the default config (from `otDnsClientGetDefaultConfig()`) will be used as the config for this query. In a non-NULL `aConfig`, some of the fields can be left unspecified (value zero). The unspecified fields are then replaced by the values from the default config.

### otDnsClientResolveIp4Address

`otError otDnsClientResolveIp4Address(otInstance *aInstance, const char *aHostName, otDnsAddressCallback aCallback, void *aContext, const otDnsQueryConfig *aConfig)`

**Description:** Sends an address resolution DNS query for A (IPv4) record(s) for a given host name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const char *|[in]|aHostName|The host name for which to query the address (MUST NOT be NULL).|
|[otDnsAddressCallback](api-dns#ot-dns-address-callback)|[in]|aCallback|A function pointer that shall be called on response reception or time-out.|
|void *|[in]|aContext|A pointer to arbitrary context information.|
|const [otDnsQueryConfig](ot-dns-query-config) *|[in]|aConfig|A pointer to the config to use for this query.|

Requires and is available when `OPENTHREAD_CONFIG_DNS_CLIENT_NAT64_ENABLE` is enabled.

When a successful response is received, the addresses are returned from `aCallback` as NAT64 IPv6 translated versions of the IPv4 addresses from the query response.

The `aConfig` can be NULL. In this case the default config (from `otDnsClientGetDefaultConfig()`) will be used as the config for this query. In a non-NULL `aConfig`, some of the fields can be left unspecified (value zero). The unspecified fields are then replaced by the values from the default config.

### otDnsAddressResponseGetHostName

`otError otDnsAddressResponseGetHostName(const otDnsAddressResponse *aResponse, char *aNameBuffer, uint16_t aNameBufferSize)`

**Description:** Gets the full host name associated with an address resolution DNS response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsAddressResponse](api-dns#ot-dns-address-response) *|[in]|aResponse|A pointer to the response.|
|char *|[out]|aNameBuffer|A buffer to char array to output the full host name (MUST NOT be NULL).|
|uint16_t|[in]|aNameBufferSize|The size of `aNameBuffer`.|

MUST only be used from `otDnsAddressCallback`.

### otDnsAddressResponseGetAddress

`otError otDnsAddressResponseGetAddress(const otDnsAddressResponse *aResponse, uint16_t aIndex, otIp6Address *aAddress, uint32_t *aTtl)`

**Description:** Gets an IPv6 address associated with an address resolution DNS response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsAddressResponse](api-dns#ot-dns-address-response) *|[in]|aResponse|A pointer to the response.|
|uint16_t|[in]|aIndex|The address record index to retrieve.|
|[otIp6Address](ot-ip6-address) *|[out]|aAddress|A pointer to a IPv6 address to output the address (MUST NOT be NULL).|
|uint32_t *|[out]|aTtl|A pointer to an `uint32_t` to output TTL for the address. It can be NULL if caller does not want to get the TTL.|

MUST only be used from `otDnsAddressCallback`.

The response may include multiple IPv6 address records. `aIndex` can be used to iterate through the list of addresses. Index zero gets the first address and so on. When we reach end of the list, `OT_ERROR_NOT_FOUND` is returned.

### otDnsClientBrowse

`otError otDnsClientBrowse(otInstance *aInstance, const char *aServiceName, otDnsBrowseCallback aCallback, void *aContext, const otDnsQueryConfig *aConfig)`

**Description:** Sends a DNS browse (service instance enumeration) query for a given service name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const char *|[in]|aServiceName|The service name to query for (MUST NOT be NULL).|
|[otDnsBrowseCallback](api-dns#ot-dns-browse-callback)|[in]|aCallback|A function pointer that shall be called on response reception or time-out.|
|void *|[in]|aContext|A pointer to arbitrary context information.|
|const [otDnsQueryConfig](ot-dns-query-config) *|[in]|aConfig|A pointer to the config to use for this query.|

Is available when `OPENTHREAD_CONFIG_DNS_CLIENT_SERVICE_DISCOVERY_ENABLE` is enabled.

The `aConfig` can be NULL. In this case the default config (from `otDnsClientGetDefaultConfig()`) will be used as the config for this query. In a non-NULL `aConfig`, some of the fields can be left unspecified (value zero). The unspecified fields are then replaced by the values from the default config.

### otDnsBrowseResponseGetServiceName

`otError otDnsBrowseResponseGetServiceName(const otDnsBrowseResponse *aResponse, char *aNameBuffer, uint16_t aNameBufferSize)`

**Description:** Gets the service name associated with a DNS browse (service instance enumeration) response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsBrowseResponse](api-dns#ot-dns-browse-response) *|[in]|aResponse|A pointer to the response.|
|char *|[out]|aNameBuffer|A buffer to char array to output the service name (MUST NOT be NULL).|
|uint16_t|[in]|aNameBufferSize|The size of `aNameBuffer`.|

MUST only be used from `otDnsBrowseCallback`.

### otDnsBrowseResponseGetServiceInstance

`otError otDnsBrowseResponseGetServiceInstance(const otDnsBrowseResponse *aResponse, uint16_t aIndex, char *aLabelBuffer, uint8_t aLabelBufferSize)`

**Description:** Gets a service instance associated with a DNS browse (service instance enumeration) response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsBrowseResponse](api-dns#ot-dns-browse-response) *|[in]|aResponse|A pointer to the response.|
|uint16_t|[in]|aIndex|The service instance record index to retrieve.|
|char *|[out]|aLabelBuffer|A buffer to char array to output the service instance label (MUST NOT be NULL).|
|uint8_t|[in]|aLabelBufferSize|The size of `aLabelBuffer`.|

MUST only be used from `otDnsBrowseCallback`.

The response may include multiple service instance records. `aIndex` can be used to iterate through the list. Index zero gives the first record. When we reach end of the list, `OT_ERROR_NOT_FOUND` is returned.

Note that this function gets the service instance label and not the full service instance name which is of the form `<Instance>.<Service>.<Domain>`.

### otDnsBrowseResponseGetServiceInfo

`otError otDnsBrowseResponseGetServiceInfo(const otDnsBrowseResponse *aResponse, const char *aInstanceLabel, otDnsServiceInfo *aServiceInfo)`

**Description:** Gets info for a service instance from a DNS browse (service instance enumeration) response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsBrowseResponse](api-dns#ot-dns-browse-response) *|[in]|aResponse|A pointer to the response.|
|const char *|[in]|aInstanceLabel|The service instance label (MUST NOT be NULL).|
|[otDnsServiceInfo](ot-dns-service-info) *|[out]|aServiceInfo|A `ServiceInfo` to output the service instance information (MUST NOT be NULL).|

MUST only be used from `otDnsBrowseCallback`.

A browse DNS response can include SRV, TXT, and AAAA records for the service instances that are enumerated. This is a SHOULD and not a MUST requirement, and servers/resolvers are not required to provide this. This function attempts to retrieve this info for a given service instance when available.

- If no matching SRV record is found in `aResponse`, `OT_ERROR_NOT_FOUND` is returned. In this case, no additional records (no TXT and/or AAAA) are read.
- If a matching SRV record is found in `aResponse`, `aServiceInfo` is updated and `OT_ERROR_NONE` is returned.
- If no matching TXT record is found in `aResponse`, `mTxtDataSize` in `aServiceInfo` is set to zero.
- If TXT data length is greater than `mTxtDataSize`, it is read partially and `mTxtDataTruncated` is set to true.
- If no matching AAAA record is found in `aResponse`, `mHostAddress is set to all zero or unspecified address.`
- `If there are multiple AAAA records for the host name in @p aResponse,`mHostAddress`is set to the first one. The other addresses can be retrieved using`[otDnsBrowseResponseGetHostAddress()](api-dns#ot-dns-browse-response-get-host-address)`.

### otDnsBrowseResponseGetHostAddress

`otError otDnsBrowseResponseGetHostAddress(const otDnsBrowseResponse *aResponse, const char *aHostName, uint16_t aIndex, otIp6Address *aAddress, uint32_t *aTtl)`

**Description:** Gets the host IPv6 address from a DNS browse (service instance enumeration) response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsBrowseResponse](api-dns#ot-dns-browse-response) *|[in]|aResponse|A pointer to the response.|
|const char *|[in]|aHostName|The host name to get the address (MUST NOT be NULL).|
|uint16_t|[in]|aIndex|The address record index to retrieve.|
|[otIp6Address](ot-ip6-address) *|[out]|aAddress|A pointer to a IPv6 address to output the address (MUST NOT be NULL).|
|uint32_t *|[out]|aTtl|A pointer to an `uint32_t` to output TTL for the address. It can be NULL if caller does not want to get the TTL.|

MUST only be used from `otDnsBrowseCallback`.

The response can include zero or more IPv6 address records. `aIndex` can be used to iterate through the list of addresses. Index zero gets the first address and so on. When we reach end of the list, `OT_ERROR_NOT_FOUND` is returned.

### otDnsClientResolveService

`otError otDnsClientResolveService(otInstance *aInstance, const char *aInstanceLabel, const char *aServiceName, otDnsServiceCallback aCallback, void *aContext, const otDnsQueryConfig *aConfig)`

**Description:** Starts a DNS service instance resolution for a given service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const char *|[in]|aInstanceLabel|The service instance label.|
|const char *|[in]|aServiceName|The service name (together with `aInstanceLabel` form full instance name).|
|[otDnsServiceCallback](api-dns#ot-dns-service-callback)|[in]|aCallback|A function pointer that shall be called on response reception or time-out.|
|void *|[in]|aContext|A pointer to arbitrary context information.|
|const [otDnsQueryConfig](ot-dns-query-config) *|[in]|aConfig|A pointer to the config to use for this query.|

Is available when `OPENTHREAD_CONFIG_DNS_CLIENT_SERVICE_DISCOVERY_ENABLE` is enabled.

The `aConfig` can be NULL. In this case the default config (from `otDnsClientGetDefaultConfig()`) will be used as the config for this query. In a non-NULL `aConfig`, some of the fields can be left unspecified (value zero). The unspecified fields are then replaced by the values from the default config.

The function sends queries for SRV and/or TXT records for the given service instance. The `mServiceMode` field in `otDnsQueryConfig` determines which records to query (SRV only, TXT only, or both SRV and TXT) and how to perform the query (together in the same message, separately in parallel, or in optimized mode where client will try in the same message first and then separately if it fails to get a response).

The SRV record provides information about service port, priority, and weight along with the host name associated with the service instance. This function DOES NOT perform address resolution for the host name discovered from SRV record. The server/resolver may provide AAAA/A record(s) for the host name in the Additional Data section of the response to SRV/TXT query and this information can be retrieved using `otDnsServiceResponseGetServiceInfo()` in `otDnsServiceCallback`. Users of this API MUST NOT assume that host address will always be available from `otDnsServiceResponseGetServiceInfo()`.

### otDnsClientResolveServiceAndHostAddress

`otError otDnsClientResolveServiceAndHostAddress(otInstance *aInstance, const char *aInstanceLabel, const char *aServiceName, otDnsServiceCallback aCallback, void *aContext, const otDnsQueryConfig *aConfig)`

**Description:** Starts a DNS service instance resolution for a given service instance, with a potential follow-up address resolution for the host name discovered for the service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const char *|[in]|aInstanceLabel|The service instance label.|
|const char *|[in]|aServiceName|The service name (together with `aInstanceLabel` form full instance name).|
|[otDnsServiceCallback](api-dns#ot-dns-service-callback)|[in]|aCallback|A function pointer that shall be called on response reception or time-out.|
|void *|[in]|aContext|A pointer to arbitrary context information.|
|const [otDnsQueryConfig](ot-dns-query-config) *|[in]|aConfig|A pointer to the config to use for this query.|

Is available when `OPENTHREAD_CONFIG_DNS_CLIENT_SERVICE_DISCOVERY_ENABLE` is enabled.

The `aConfig` can be NULL. In this case the default config (from `otDnsClientGetDefaultConfig()`) will be used as the config for this query. In a non-NULL `aConfig`, some of the fields can be left unspecified (value zero). The unspecified fields are then replaced by the values from the default config. This function cannot be used with `mServiceMode` in DNS config set to `OT_DNS_SERVICE_MODE_TXT` (i.e., querying for TXT record only) and will return `OT_ERROR_INVALID_ARGS`.

Behaves similarly to `otDnsClientResolveService()` sending queries for SRV and TXT records. However, if the server/resolver does not provide AAAA/A records for the host name in the response to SRV query (in the Additional Data section), it will perform host name resolution (sending an AAAA query) for the discovered host name from the SRV record. The callback `aCallback` is invoked when responses for all queries are received (i.e., both service and host address resolutions are finished).

### otDnsServiceResponseGetServiceName

`otError otDnsServiceResponseGetServiceName(const otDnsServiceResponse *aResponse, char *aLabelBuffer, uint8_t aLabelBufferSize, char *aNameBuffer, uint16_t aNameBufferSize)`

**Description:** Gets the service instance name associated with a DNS service instance resolution response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsServiceResponse](api-dns#ot-dns-service-response) *|[in]|aResponse|A pointer to the response.|
|char *|[out]|aLabelBuffer|A buffer to char array to output the service instance label (MUST NOT be NULL).|
|uint8_t|[in]|aLabelBufferSize|The size of `aLabelBuffer`.|
|char *|[out]|aNameBuffer|A buffer to char array to output the rest of service name (can be NULL if user is not interested in getting the name.|
|uint16_t|[in]|aNameBufferSize|The size of `aNameBuffer`.|

MUST only be used from `otDnsServiceCallback`.

### otDnsServiceResponseGetServiceInfo

`otError otDnsServiceResponseGetServiceInfo(const otDnsServiceResponse *aResponse, otDnsServiceInfo *aServiceInfo)`

**Description:** Gets info for a service instance from a DNS service instance resolution response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsServiceResponse](api-dns#ot-dns-service-response) *|[in]|aResponse|A pointer to the response.|
|[otDnsServiceInfo](ot-dns-service-info) *|[out]|aServiceInfo|A `ServiceInfo` to output the service instance information (MUST NOT be NULL).|

MUST only be used from a `otDnsServiceCallback` triggered from `otDnsClientResolveService()` or `otDnsClientResolveServiceAndHostAddress()`.

When this is is used from a `otDnsClientResolveService()` callback, the DNS response from server/resolver may include AAAA records in its Additional Data section for the host name associated with the service instance that is resolved. This is a SHOULD and not a MUST requirement so servers/resolvers are not required to provide this. This function attempts to parse AAAA record(s) if included in the response. If it is not included `mHostAddress` is set to all zeros (unspecified address). To also resolve the host address, user can use the DNS client API function `otDnsClientResolveServiceAndHostAddress()` which will perform service resolution followed up by a host name address resolution query (when AAAA records are not provided by server/resolver in the SRV query response).

- If a matching SRV record is found in `aResponse`, `aServiceInfo` is updated.
- If no matching SRV record is found, `OT_ERROR_NOT_FOUND` is returned unless the query config for this query used `OT_DNS_SERVICE_MODE_TXT` for `mServiceMode` (meaning the request was only for TXT record). In this case, we still try to parse the SRV record from Additional Data Section of response (in case server provided the info).
- If no matching TXT record is found in `aResponse`, `mTxtDataSize` in `aServiceInfo` is set to zero.
- If TXT data length is greater than `mTxtDataSize`, it is read partially and `mTxtDataTruncated` is set to true.
- If no matching AAAA record is found in `aResponse`, `mHostAddress is set to all zero or unspecified address.`
- `If there are multiple AAAA records for the host name in @p aResponse,`mHostAddress`is set to the first one. The other addresses can be retrieved using`[otDnsServiceResponseGetHostAddress()](api-dns#ot-dns-service-response-get-host-address)`.

### otDnsServiceResponseGetHostAddress

`otError otDnsServiceResponseGetHostAddress(const otDnsServiceResponse *aResponse, const char *aHostName, uint16_t aIndex, otIp6Address *aAddress, uint32_t *aTtl)`

**Description:** Gets the host IPv6 address from a DNS service instance resolution response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsServiceResponse](api-dns#ot-dns-service-response) *|[in]|aResponse|A pointer to the response.|
|const char *|[in]|aHostName|The host name to get the address (MUST NOT be NULL).|
|uint16_t|[in]|aIndex|The address record index to retrieve.|
|[otIp6Address](ot-ip6-address) *|[out]|aAddress|A pointer to a IPv6 address to output the address (MUST NOT be NULL).|
|uint32_t *|[out]|aTtl|A pointer to an `uint32_t` to output TTL for the address. It can be NULL if caller does not want to get the TTL.|

MUST only be used from `otDnsServiceCallback`.

The response can include zero or more IPv6 address records. `aIndex` can be used to iterate through the list of addresses. Index zero gets the first address and so on. When we reach end of the list, `OT_ERROR_NOT_FOUND` is returned.

### otDnsClientQueryRecord

`otError otDnsClientQueryRecord(otInstance *aInstance, uint16_t aRecordType, const char *aFirstLabel, const char *aNextLabels, otDnsRecordCallback aCallback, void *aContext, const otDnsQueryConfig *aConfig)`

**Description:** Sends a DNS query for a given record type and name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint16_t|[in]|aRecordType|The resource record type to query.|
|const char *|[in]|aFirstLabel|The first label of the name to be queried (can be NULL if not needed).|
|const char *|[in]|aNextLabels|The next labels of the name to be queried (MUST NOT be NULL).|
|[otDnsRecordCallback](api-dns#ot-dns-record-callback)|[in]|aCallback|A function pointer that shall be called on response reception or time-out.|
|void *|[in]|aContext|A pointer to arbitrary context information used when `aCallback` is invoked.|
|const [otDnsQueryConfig](ot-dns-query-config) *|[in]|aConfig|A pointer to the config to use for this query.|

Requires `OPENTHREAD_CONFIG_DNS_CLIENT_ARBITRARY_RECORD_QUERY_ENABLE`.

The `aConfig` can be NULL. In this case the default config (from `otDnsClientGetDefaultConfig()`) will be used as the config for this query. In a non-NULL `aConfig`, some of the fields can be left unspecified (value zero). The unspecified fields are then replaced by the values from the default config.

### otDnsRecordResponseGetQueryName

`otError otDnsRecordResponseGetQueryName(const otDnsRecordResponse *aResponse, char *aNameBuffer, uint16_t aNameBufferSize)`

**Description:** Gets the query name associated with a record query DNS response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsRecordResponse](api-dns#ot-dns-record-response) *|[in]|aResponse|A pointer to the response.|
|char *|[out]|aNameBuffer|A buffer to char array to output the full query name (MUST NOT be NULL).|
|uint16_t|[in]|aNameBufferSize|The size of `aNameBuffer`.|

MUST only be used from `otDnsRecordCallback`.

### otDnsRecordResponseGetRecordInfo

`otError otDnsRecordResponseGetRecordInfo(const otDnsRecordResponse *aResponse, uint16_t aIndex, otDnsRecordInfo *aRecordInfo)`

**Description:** Reads the records from a DNS query response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otDnsRecordResponse](api-dns#ot-dns-record-response) *|[in]|aResponse|A pointer to the response.|
|uint16_t|[in]|aIndex|The record index to retrieve.|
|[otDnsRecordInfo](ot-dns-record-info) *|[out]|aRecordInfo|A pointer to a `otDnsRecordInfo` to populate with read record info.|

MUST only be used from `otDnsRecordCallback`.

The response may include multiple records. `aIndex` can be used to iterate through the list. Index zero gets the first record and so on. When we reach the end of the list, `OT_ERROR_NOT_FOUND` is returned.

Upon successful retrieval (`OT_ERROR_NONE`):

- `mRecordLength` is set to the actual length of the record's data.
- The data is copied into `mDataBuffer` (if not `NULL`) up to its capacity specified by `mDataBufferSize`.
- `mDataBufferSize` is then updated to reflect the number of bytes actually written into `mDataBuffer`.

If the retrieved record type is NS, CNAME, SOA, PTR, MX, RP, AFSDB, RT, PX, SRV, KX, DNAME, or NSEC, the record data in the received response contains a DNS name which may use DNS name compression. For these specific record types, the record data is first decompressed such that it contains the full uncompressed DNS name. This decompressed data is then provided in `mDataBuffer`, and `mRecordDataLength` will indicate the length of this decompressed data. For all other record types, the record data is read and provided as it appears in the received response message.

## Macros

`#define OT_DNS_MAX_NAME_SIZE 255`

**Description**: Maximum name string size (includes null char at the end of string).

`#define OT_DNS_MAX_LABEL_SIZE 64`

**Description**: Maximum label string size (include null char at the end of string).

`#define OT_DNS_TXT_KEY_MIN_LENGTH 1`

**Description**: Minimum length of TXT record key string (RFC 6763 - section 6.4).

`#define OT_DNS_TXT_KEY_MAX_LENGTH 9`

**Description**: Recommended maximum length of TXT record key string (RFC 6763 - section 6.4).

`#define OT_DNS_TXT_KEY_ITER_MAX_LENGTH 64`

**Description**: Maximum length of TXT key string supported by `otDnsTxtEntryIterator`.