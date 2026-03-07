# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-nat64.md

# NAT64

This module includes functions and structs for the NAT64 function on the border router.

These functions are only available when `OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE` is enabled.

## Modules

[otIp4Address](ot-ip4-address)

[otIp4Cidr](ot-ip4-cidr)

[otNat64Counters](ot-nat64-counters)

[otNat64ProtocolCounters](ot-nat64-protocol-counters)

[otNat64ErrorCounters](ot-nat64-error-counters)

[otNat64AddressMapping](ot-nat64-address-mapping)

[otNat64AddressMappingIterator](ot-nat64-address-mapping-iterator)

## Enumerations

### otNat64DropReason

```c

enum otNat64DropReason {
    OT_NAT64_DROP_REASON_UNKNOWN = 0
    OT_NAT64_DROP_REASON_ILLEGAL_PACKET
    OT_NAT64_DROP_REASON_UNSUPPORTED_PROTO
    OT_NAT64_DROP_REASON_NO_MAPPING
    OT_NAT64_DROP_REASON_COUNT
}

```

**Description**:

Packet drop reasons.

**Enumerator**:

|   |   |
|---|---|
|OT_NAT64_DROP_REASON_UNKNOWN|Packet drop for unknown reasons.|
|OT_NAT64_DROP_REASON_ILLEGAL_PACKET|Packet drop due to failed to parse the datagram.|
|OT_NAT64_DROP_REASON_UNSUPPORTED_PROTO|Packet drop due to unsupported IP protocol.|
|OT_NAT64_DROP_REASON_NO_MAPPING|Packet drop due to no mappings found or mapping pool exhausted.|
|OT_NAT64_DROP_REASON_COUNT||

### otNat64State

```c

enum otNat64State {
    OT_NAT64_STATE_DISABLED = 0
    OT_NAT64_STATE_NOT_RUNNING
    OT_NAT64_STATE_IDLE
    OT_NAT64_STATE_ACTIVE
}

```

**Description**:

States of NAT64.

**Enumerator**:

|   |   |
|---|---|
|OT_NAT64_STATE_DISABLED|NAT64 is disabled.|
|OT_NAT64_STATE_NOT_RUNNING|NAT64 is enabled, but one or more dependencies of NAT64 are not running.|
|OT_NAT64_STATE_IDLE|NAT64 is enabled, but this BR is not an active NAT64 BR.|
|OT_NAT64_STATE_ACTIVE|The BR is publishing a NAT64 prefix and/or translating packets.|

## Typedefs

### otIp4Address

`typedef struct otIp4Address otIp4Address`

**Description**:

Represents an IPv4 address.

### otIp4Cidr

`typedef struct otIp4Cidr otIp4Cidr`

### otNat64Counters

`typedef struct otNat64Counters otNat64Counters`

**Description**:

Represents the counters for NAT64.

### otNat64ProtocolCounters

`typedef struct otNat64ProtocolCounters otNat64ProtocolCounters`

**Description**:

Represents the counters for the protocols supported by NAT64.

### otNat64DropReason (Typedef)

`typedef enum otNat64DropReason otNat64DropReason`

**Description**:

Packet drop reasons.

### otNat64ErrorCounters

`typedef struct otNat64ErrorCounters otNat64ErrorCounters`

**Description**:

Represents the counters of dropped packets due to errors when handling NAT64 packets.

### otNat64AddressMapping

`typedef struct otNat64AddressMapping otNat64AddressMapping`

**Description**:

Represents an address mapping record for NAT64.

**Details**:

**Note:**

- The counters will be reset for each mapping session even for the same address pair. Applications can use `mId` to identify different sessions to calculate the packets correctly.

### otNat64AddressMappingIterator

`typedef struct otNat64AddressMappingIterator otNat64AddressMappingIterator`

**Description**:

Used to iterate through NAT64 address mappings.

**Details**:

The fields in this type are opaque (intended for use by OpenThread core only) and therefore should not be accessed or used by caller.

Before using an iterator, it MUST be initialized using `otNat64InitAddressMappingIterator()`.

The member fields in this struct are for internal OpenThread stack use and should not be accessed directly.

### otNat64ReceiveIp4Callback

`typedef void(* otNat64ReceiveIp4Callback) (otMessage *aMessage, void *aContext)`

**Description**:

Pointer is called when an IPv4 datagram (translated by NAT64 translator) is received.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aMessage|A pointer to the message buffer containing the received IPv6 datagram. This function transfers the ownership of the `aMessage` to the receiver of the callback. The message should be freed by the receiver of the callback after it is processed.|
||[in]|aContext|A pointer to application-specific context.|

**Details**:

## Variables

### OT_TOOL_PACKED_END

```c

OT_TOOL_PACKED_BEGIN struct otIp4Address OT_TOOL_PACKED_END

```

## Functions

### otNat64GetCounters

`void otNat64GetCounters(otInstance *aInstance, otNat64ProtocolCounters *aCounters)`

**Description:** Gets NAT64 translator counters.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otNat64ProtocolCounters](ot-nat64-protocol-counters) *|[out]|aCounters|A pointer to an `otNat64Counters` where the counters of NAT64 translator will be placed.|

The counter is counted since the instance initialized.

Available when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled.

### otNat64GetErrorCounters

`void otNat64GetErrorCounters(otInstance *aInstance, otNat64ErrorCounters *aCounters)`

**Description:** Gets the NAT64 translator error counters.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otNat64ErrorCounters](ot-nat64-error-counters) *|[out]|aCounters|A pointer to an `otNat64Counters` where the counters of NAT64 translator will be placed.|

The counters are initialized to zero when the OpenThread instance is initialized.

### otNat64InitAddressMappingIterator

`void otNat64InitAddressMappingIterator(otInstance *aInstance, otNat64AddressMappingIterator *aIterator)`

**Description:** Initializes an `otNat64AddressMappingIterator`.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otNat64AddressMappingIterator](ot-nat64-address-mapping-iterator) *|[out]|aIterator|A pointer to the iterator to initialize.|

Available when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled.

An iterator MUST be initialized before it is used. An iterator can be initialized again to restart from the beginning of the mapping info list.

The iterator initialization time is used to report the `mRemainingTimeMs` in the `otNat64AddressMapping` retrieved when calling `otNat64GetNextAddressMapping()` to iterate over the list. This ensures that all entry `mRemainingTimeMs` values are consistent and are from the same time origin, regardless of how or when `otNat64GetNextAddressMapping()` is called.

### otNat64GetNextAddressMapping

`otError otNat64GetNextAddressMapping(otInstance *aInstance, otNat64AddressMappingIterator *aIterator, otNat64AddressMapping *aMapping)`

**Description:** Gets the next AddressMapping info (using an iterator).

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otNat64AddressMappingIterator](ot-nat64-address-mapping-iterator) *|[inout]|aIterator|A pointer to the iterator. On success the iterator will be updated to point to next NAT64 address mapping record.|
|[otNat64AddressMapping](ot-nat64-address-mapping) *|[out]|aMapping|A pointer to an `otNat64AddressMapping` where information of next NAT64 address mapping record is placed (on success).|

Available when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled.

### otNat64GetTranslatorState

`otNat64State otNat64GetTranslatorState(otInstance *aInstance)`

**Description:** Gets the state of NAT64 translator.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Available when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled.

### otNat64GetPrefixManagerState

`otNat64State otNat64GetPrefixManagerState(otInstance *aInstance)`

**Description:** Gets the state of NAT64 prefix manager.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Available when `OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE` is enabled.

### otNat64SetEnabled

`void otNat64SetEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Enable or disable NAT64 functions.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnabled|A boolean to enable/disable the NAT64 functions|

Note: This includes the NAT64 Translator (when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled) and the NAT64 Prefix Manager (when `OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE` is enabled).

When `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled, setting disabled to true resets the mapping table in the translator.

Available when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` or `OPENTHREAD_CONFIG_NAT64_BORDER_ROUTING_ENABLE` is enabled.

**See Also:**

- [otNat64GetTranslatorState](api-nat64#ot-nat64-get-translator-state)
- [otNat64GetPrefixManagerState](api-nat64#ot-nat64-get-prefix-manager-state)

### otIp4NewMessage

`otMessage * otIp4NewMessage(otInstance *aInstance, const otMessageSettings *aSettings)`

**Description:** Allocate a new message buffer for sending an IPv4 message to the NAT64 translator.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otMessageSettings](ot-message-settings) *|[in]|aSettings|A pointer to the message settings or NULL to set default settings.|

Message buffers allocated by this function will have 20 bytes (difference between the size of IPv6 headers and IPv4 header sizes) reserved.

Available when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled.

**Note:**

- If `aSettings` is `NULL`, the link layer security is enabled and the message priority is set to OT_MESSAGE_PRIORITY_NORMAL by default.

**Returns:**

- A pointer to the message buffer or NULL if no message buffers are available or parameters are invalid.

**See Also:**

- [otNat64Send](api-nat64#ot-nat64-send)

### otNat64SetIp4Cidr

`otError otNat64SetIp4Cidr(otInstance *aInstance, const otIp4Cidr *aCidr)`

**Description:** Sets the CIDR used when setting the source address of the outgoing translated IPv4 packets.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp4Cidr](ot-ip4-cidr) *|[in]|aCidr|A pointer to an [otIp4Cidr](ot-ip4-cidr) for the IPv4 CIDR block for NAT64.|

Is available only when OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE is enabled.

**Note:**

- A valid CIDR must have a non-zero prefix length. The actual addresses pool is limited by the size of the mapping pool and the number of addresses available in the CIDR block.
- This function can be called at any time, but the NAT64 translator will be reset and all existing sessions will be expired when updating the configured CIDR.

**See Also:**

- [otNat64Send](api-nat64#ot-nat64-send)
- [otNat64SetReceiveIp4Callback](api-nat64#ot-nat64-set-receive-ip4-callback)

### otNat64ClearIp4Cidr

`void otNat64ClearIp4Cidr(otInstance *aInstance)`

**Description:** Clears the CIDR used when setting the source address of the outgoing translated IPv4 packets.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Is available only when OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE is enabled.

**Note:**

- This function can be called at any time, but the NAT64 translator will be reset and all existing sessions will be expired when clearing the configured CIDR.

**See Also:**

- [otNat64SetIp4Cidr](api-nat64#ot-nat64-set-ip4-cidr)

### otNat64Send

`otError otNat64Send(otInstance *aInstance, otMessage *aMessage)`

**Description:** Translates an IPv4 datagram to an IPv6 datagram and sends via the Thread interface.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to the message buffer containing the IPv4 datagram.|

The caller transfers ownership of `aMessage` when making this call. OpenThread will free `aMessage` when processing is complete, including when a value other than `OT_ERROR_NONE` is returned.

### otNat64SetReceiveIp4Callback

`void otNat64SetReceiveIp4Callback(otInstance *aInstance, otNat64ReceiveIp4Callback aCallback, void *aContext)`

**Description:** Registers a callback to provide received IPv4 datagrams.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otNat64ReceiveIp4Callback](api-nat64#ot-nat64-receive-ip4-callback)|[in]|aCallback|A pointer to a function that is called when an IPv4 datagram is received or NULL to disable the callback.|
|void *|[in]|aContext|A pointer to application-specific context.|

### otNat64GetCidr

`otError otNat64GetCidr(otInstance *aInstance, otIp4Cidr *aCidr)`

**Description:** Gets the IPv4 CIDR configured in the NAT64 translator.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otIp4Cidr](ot-ip4-cidr) *|[out]|aCidr|A pointer to an [otIp4Cidr](ot-ip4-cidr). Where the CIDR will be filled.|

Available when `OPENTHREAD_CONFIG_NAT64_TRANSLATOR_ENABLE` is enabled.

### otIp4IsAddressEqual

`bool otIp4IsAddressEqual(const otIp4Address *aFirst, const otIp4Address *aSecond)`

**Description:** Test if two IPv4 addresses are the same.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp4Address](ot-ip4-address) *|[in]|aFirst|A pointer to the first IPv4 address to compare.|
|const [otIp4Address](ot-ip4-address) *|[in]|aSecond|A pointer to the second IPv4 address to compare.|

### otIp4ExtractFromIp6Address

`void otIp4ExtractFromIp6Address(uint8_t aPrefixLength, const otIp6Address *aIp6Address, otIp4Address *aIp4Address)`

**Description:** Set `aIp4Address` by performing NAT64 address translation from `aIp6Address` as specified in RFC 6052.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|uint8_t|[in]|aPrefixLength|The prefix length to use for IPv4/IPv6 translation.|
|const [otIp6Address](ot-ip6-address) *|[in]|aIp6Address|A pointer to an IPv6 address.|
|[otIp4Address](ot-ip4-address) *|[out]|aIp4Address|A pointer to output the IPv4 address.|

The NAT64 `aPrefixLength` MUST be one of the following values: 32, 40, 48, 56, 64, or 96, otherwise the behavior of this method is undefined.

### otIp4FromIp4MappedIp6Address

`otError otIp4FromIp4MappedIp6Address(const otIp6Address *aIp6Address, otIp4Address *aIp4Address)`

**Description:** Extracts the IPv4 address from a given IPv4-mapped IPv6 address.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aIp6Address|An IPv6 address to extract IPv4 from.|
|[otIp4Address](ot-ip4-address) *|[out]|aIp4Address|An IPv4 address to output the extracted address.|

An IPv4-mapped IPv6 address consists of an 80-bit prefix of zeros, the next 16 bits set to ones, and the remaining, least-significant 32 bits contain the IPv4 address, e.g., `::ffff:192.0.2.128` representing `192.0.2.128`.

### otIp4ToIp4MappedIp6Address

`void otIp4ToIp4MappedIp6Address(const otIp4Address *aIp4Address, otIp6Address *aIp6Address)`

**Description:** Converts a given IP4 address to an IPv6 address following the IPv4-mapped IPv6 address format.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp4Address](ot-ip4-address) *|[in]|aIp4Address|An IPv4 address to convert.|
|[otIp6Address](ot-ip6-address) *|[out]|aIp6Address|An IPv6 address to set.|

### otIp4AddressToString

`void otIp4AddressToString(const otIp4Address *aAddress, char *aBuffer, uint16_t aSize)`

**Description:** Converts the address to a string.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp4Address](ot-ip4-address) *|[in]|aAddress|A pointer to an IPv4 address (MUST NOT be NULL).|
|char *|[out]|aBuffer|A pointer to a char array to output the string (MUST NOT be NULL).|
|uint16_t|[in]|aSize|The size of `aBuffer` (in bytes).|

The string format uses quad-dotted notation of four bytes in the address (e.g., "127.0.0.1").

If the resulting string does not fit in `aBuffer` (within its `aSize` characters), the string will be truncated but the outputted string is always null-terminated.

### otIp4CidrFromString

`otError otIp4CidrFromString(const char *aString, otIp4Cidr *aCidr)`

**Description:** Converts a human-readable IPv4 CIDR string into a binary representation.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const char *|[in]|aString|A pointer to a NULL-terminated string.|
|[otIp4Cidr](ot-ip4-cidr) *|[out]|aCidr|A pointer to an IPv4 CIDR.|

### otIp4CidrToString

`void otIp4CidrToString(const otIp4Cidr *aCidr, char *aBuffer, uint16_t aSize)`

**Description:** Converts the IPv4 CIDR to a string.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp4Cidr](ot-ip4-cidr) *|[in]|aCidr|A pointer to an IPv4 CIDR (MUST NOT be NULL).|
|char *|[out]|aBuffer|A pointer to a char array to output the string (MUST NOT be NULL).|
|uint16_t|[in]|aSize|The size of `aBuffer` (in bytes).|

The string format uses quad-dotted notation of four bytes in the address with the length of prefix (e.g., "127.0.0.1/32").

If the resulting string does not fit in `aBuffer` (within its `aSize` characters), the string will be truncated but the outputted string is always null-terminated.

### otIp4AddressFromString

`otError otIp4AddressFromString(const char *aString, otIp4Address *aAddress)`

**Description:** Converts a human-readable IPv4 address string into a binary representation.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const char *|[in]|aString|A pointer to a NULL-terminated string.|
|[otIp4Address](ot-ip4-address) *|[out]|aAddress|A pointer to an IPv4 address.|

### otNat64SynthesizeIp6Address

`otError otNat64SynthesizeIp6Address(otInstance *aInstance, const otIp4Address *aIp4Address, otIp6Address *aIp6Address)`

**Description:** Sets the IPv6 address by performing NAT64 address translation from the preferred NAT64 prefix and the given IPv4 address as specified in RFC 6052.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp4Address](ot-ip4-address) *|[in]|aIp4Address|A pointer to the IPv4 address to translate to IPv6.|
|[otIp6Address](ot-ip6-address) *|[out]|aIp6Address|A pointer to the synthesized IPv6 address.|

**Returns:**

- OT_ERROR_NONE Successfully synthesized the IPv6 address from NAT64 prefix and IPv4 address.
- OT_ERROR_INVALID_STATE No valid NAT64 prefix in the network data.

## Macros

`#define OT_IP4_ADDRESS_SIZE 4`

**Description**: Size of an IPv4 address (bytes)

`#define OT_IP4_ADDRESS_STRING_SIZE 17`

**Description**: Length of 000.000.000.000 plus a suffix NUL.

`#define OT_IP4_CIDR_STRING_SIZE 20`

**Description**: Length of 000.000.000.000/00 plus a suffix NUL.
