# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-ip6.md

# IPv6

This module includes functions that control IPv6 communication.

## Modules

[otIp6InterfaceIdentifier](ot-ip6-interface-identifier)

[otIp6NetworkPrefix](ot-ip6-network-prefix)

[otIp6AddressComponents](ot-ip6-address-components)

[otIp6Address](ot-ip6-address)

[otIp6Prefix](ot-ip6-prefix)

[otNetifAddress](ot-netif-address)

[otNetifMulticastAddress](ot-netif-multicast-address)

[otSockAddr](ot-sock-addr)

[otMessageInfo](ot-message-info)

[otIp6AddressInfo](ot-ip6-address-info)

[otPacketsAndBytes](ot-packets-and-bytes)

[otBorderRoutingCounters](ot-border-routing-counters)

## Enumerations

### @2

```c
enum @2 {
    OT_ADDRESS_ORIGIN_THREAD = 0
    OT_ADDRESS_ORIGIN_SLAAC = 1
    OT_ADDRESS_ORIGIN_DHCPV6 = 2
    OT_ADDRESS_ORIGIN_MANUAL = 3
}
```

**Description:**

IPv6 Address origins.

**Enumerator:**

|   |   |
|---|---|
|OT_ADDRESS_ORIGIN_THREAD|Thread assigned address (ALOC, RLOC, MLEID, etc)|
|OT_ADDRESS_ORIGIN_SLAAC|SLAAC assigned address.|
|OT_ADDRESS_ORIGIN_DHCPV6|DHCPv6 assigned address.|
|OT_ADDRESS_ORIGIN_MANUAL|Manually assigned address.|

### @3

```c
enum @3 {
    OT_ECN_NOT_CAPABLE = 0x0
    OT_ECN_CAPABLE_0 = 0x2
    OT_ECN_CAPABLE_1 = 0x1
    OT_ECN_MARKED = 0x3
}
```

**Description:**

ECN statuses, represented as in the IP header.

**Enumerator:**

|   |   |
|---|---|
|OT_ECN_NOT_CAPABLE|Non-ECT.|
|OT_ECN_CAPABLE_0|ECT(0)|
|OT_ECN_CAPABLE_1|ECT(1)|
|OT_ECN_MARKED|Congestion encountered (CE)|

### @4

```c
enum @4 {
    OT_IP6_PROTO_HOP_OPTS = 0
    OT_IP6_PROTO_TCP = 6
    OT_IP6_PROTO_UDP = 17
    OT_IP6_PROTO_IP6 = 41
    OT_IP6_PROTO_ROUTING = 43
    OT_IP6_PROTO_FRAGMENT = 44
    OT_IP6_PROTO_ICMP6 = 58
    OT_IP6_PROTO_NONE = 59
    OT_IP6_PROTO_DST_OPTS = 60
}
```

**Description:**

Internet Protocol Numbers.

**Enumerator:**

|   |   |
|---|---|
|OT_IP6_PROTO_HOP_OPTS|IPv6 Hop-by-Hop Option.|
|OT_IP6_PROTO_TCP|Transmission Control Protocol.|
|OT_IP6_PROTO_UDP|User Datagram.|
|OT_IP6_PROTO_IP6|IPv6 encapsulation.|
|OT_IP6_PROTO_ROUTING|Routing Header for IPv6.|
|OT_IP6_PROTO_FRAGMENT|Fragment Header for IPv6.|
|OT_IP6_PROTO_ICMP6|ICMP for IPv6.|
|OT_IP6_PROTO_NONE|No Next Header for IPv6.|
|OT_IP6_PROTO_DST_OPTS|Destination Options for IPv6.|

## Typedefs

### otIp6InterfaceIdentifier

`typedef struct otIp6InterfaceIdentifier otIp6InterfaceIdentifier`

**Description:**

Represents the Interface Identifier of an IPv6 address.

### otIp6NetworkPrefix

`typedef struct otIp6NetworkPrefix otIp6NetworkPrefix`

**Description:**

Represents the Network Prefix of an IPv6 address (most significant 64 bits of the address).

### otIp6AddressComponents

`typedef struct otIp6AddressComponents otIp6AddressComponents`

**Description:**

Represents the components of an IPv6 address.

### otIp6Address

`typedef struct otIp6Address otIp6Address`

**Description:**

Represents an IPv6 address.

### otIp6Prefix

`typedef struct otIp6Prefix otIp6Prefix`

**Description:**

Represents an IPv6 prefix.

### otNetifAddress

`typedef struct otNetifAddress otNetifAddress`

**Description:**

Represents an IPv6 network interface unicast address.

### otNetifMulticastAddress

`typedef struct otNetifMulticastAddress otNetifMulticastAddress`

**Description:**

Represents an IPv6 network interface multicast address.

### otSockAddr

`typedef struct otSockAddr otSockAddr`

**Description:**

Represents an IPv6 socket address.

### otMessageInfo

`typedef struct otMessageInfo otMessageInfo`

**Description:**

Represents the local and peer IPv6 socket addresses.

### otIp6ReceiveCallback

`typedef void(* otIp6ReceiveCallback) (otMessage *aMessage, void *aContext)`

**Description:**

Pointer is called when an IPv6 datagram is received.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aMessage|A pointer to the message buffer containing the received IPv6 datagram. This function transfers the ownership of the `aMessage` to the receiver of the callback. The message should be freed by the receiver of the callback after it is processed (see [otMessageFree()](api-message#ot-message-free)).|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otIp6AddressInfo

`typedef struct otIp6AddressInfo otIp6AddressInfo`

**Description:**

Represents IPv6 address information.

### otIp6AddressCallback

`typedef void(* otIp6AddressCallback) (const otIp6AddressInfo *aAddressInfo, bool aIsAdded, void *aContext)`

**Description:**

Pointer is called when an internal IPv6 address is added or removed.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aAddressInfo|A pointer to the IPv6 address information.|
||[in]|aIsAdded|TRUE if the `aAddress` was added, FALSE if `aAddress` was removed.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otIp6SlaacPrefixFilter

`typedef bool(* otIp6SlaacPrefixFilter) (otInstance *aInstance, const otIp6Prefix *aPrefix)`

**Description:**

Pointer allows user to filter prefixes and not allow an SLAAC address based on a prefix to be added.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|A pointer to an OpenThread instance.|
||[in]|aPrefix|A pointer to prefix for which SLAAC address is about to be added.|

**Details:**

`otIp6SetSlaacPrefixFilter()` can be used to set the filter handler. The filter handler is invoked by SLAAC module when it is about to add a SLAAC address based on a prefix. Its boolean return value determines whether the address is filtered (not added) or not.

### otIp6RegisterMulticastListenersCallback

`typedef void(* otIp6RegisterMulticastListenersCallback) (void *aContext, otError aError, uint8_t aMlrStatus, const otIp6Address *aFailedAddresses, uint8_t aFailedAddressNum)`

**Description:**

Pointer is called with results of `otIp6RegisterMulticastListeners`.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to the user context.|
||[in]|aError|OT_ERROR_NONE when successfully sent MLR.req and received MLR.rsp, OT_ERROR_RESPONSE_TIMEOUT when failed to receive MLR.rsp, OT_ERROR_PARSE when failed to parse MLR.rsp.|
||[in]|aMlrStatus|The Multicast Listener Registration status when `aError` is OT_ERROR_NONE.|
||[in]|aFailedAddresses|A pointer to the failed IPv6 addresses when `aError` is OT_ERROR_NONE.|
||[in]|aFailedAddressNum|The number of failed IPv6 addresses when `aError` is OT_ERROR_NONE.|

**Details:**

#### See Also

- [otIp6RegisterMulticastListeners](api-ip6#ot-ip6-register-multicast-listeners)

### otPacketsAndBytes

`typedef struct otPacketsAndBytes otPacketsAndBytes`

**Description:**

Represents the counters for packets and bytes.

### otBorderRoutingCounters

`typedef struct otBorderRoutingCounters otBorderRoutingCounters`

**Description:**

Represents the counters of packets forwarded via Border Routing.

## Variables

### OT_TOOL_PACKED_END

```c
OT_TOOL_PACKED_BEGIN struct otIp6Prefix OT_TOOL_PACKED_END
```

## Functions

### otIp6SetEnabled

`otError otIp6SetEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Brings the IPv6 interface up or down.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnabled|TRUE to enable IPv6, FALSE otherwise.|

Call this to enable or disable IPv6 communication.

### otIp6IsEnabled

`bool otIp6IsEnabled(otInstance *aInstance)`

**Description:** Indicates whether or not the IPv6 interface is up.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otIp6AddUnicastAddress

`otError otIp6AddUnicastAddress(otInstance *aInstance, const otNetifAddress *aAddress)`

**Description:** Adds a Network Interface Address to the Thread interface.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otNetifAddress](ot-netif-address) *|[in]|aAddress|A pointer to a Network Interface Address.|

The passed-in instance `aAddress` is copied by the Thread interface. The Thread interface only supports a fixed number of externally added unicast addresses. See `OPENTHREAD_CONFIG_IP6_MAX_EXT_UCAST_ADDRS`.

### otIp6RemoveUnicastAddress

`otError otIp6RemoveUnicastAddress(otInstance *aInstance, const otIp6Address *aAddress)`

**Description:** Removes a Network Interface Address from the Thread interface.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to an IP Address.|

### otIp6GetUnicastAddresses

`const otNetifAddress * otIp6GetUnicastAddresses(otInstance *aInstance)`

**Description:** Gets the list of IPv6 addresses assigned to the Thread interface.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns

- A pointer to the first Network Interface Address.

### otIp6HasUnicastAddress

`bool otIp6HasUnicastAddress(otInstance *aInstance, const otIp6Address *aAddress)`

**Description:** Indicates whether or not a unicast IPv6 address is assigned to the Thread interface.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to the unicast address.|

### otIp6SubscribeMulticastAddress

`otError otIp6SubscribeMulticastAddress(otInstance *aInstance, const otIp6Address *aAddress)`

**Description:** Subscribes the Thread interface to a Network Interface Multicast Address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to an IP Address.|

The passed in instance `aAddress` will be copied by the Thread interface. The Thread interface only supports a fixed number of externally added multicast addresses. See `OPENTHREAD_CONFIG_IP6_MAX_EXT_MCAST_ADDRS`.

### otIp6UnsubscribeMulticastAddress

`otError otIp6UnsubscribeMulticastAddress(otInstance *aInstance, const otIp6Address *aAddress)`

**Description:** Unsubscribes the Thread interface to a Network Interface Multicast Address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to an IP Address.|

### otIp6GetMulticastAddresses

`const otNetifMulticastAddress * otIp6GetMulticastAddresses(otInstance *aInstance)`

**Description:** Gets the list of IPv6 multicast addresses subscribed to the Thread interface.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otIp6GetMulticastAddresses)

- A pointer to the first Network Interface Multicast Address.

### otIp6NewMessage

`otMessage * otIp6NewMessage(otInstance *aInstance, const otMessageSettings *aSettings)`

**Description:** Allocate a new message buffer for sending an IPv6 message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otMessageSettings](ot-message-settings) *|[in]|aSettings|A pointer to the message settings or NULL to set default settings.|

#### Note

- If `aSettings` is 'NULL', the link layer security is enabled and the message priority is set to OT_MESSAGE_PRIORITY_NORMAL by default.

##### Returns (Note)

- A pointer to the message buffer or NULL if no message buffers are available or parameters are invalid.

###### See Also (Returns)

- [otMessageFree](api-message#ot-message-free)

### otIp6NewMessageFromBuffer

`otMessage * otIp6NewMessageFromBuffer(otInstance *aInstance, const uint8_t *aData, uint16_t aDataLength, const otMessageSettings *aSettings)`

**Description:** Allocate a new message buffer and write the IPv6 datagram to the message buffer for sending an IPv6 message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const uint8_t *|[in]|aData|A pointer to the IPv6 datagram buffer.|
|uint16_t|[in]|aDataLength|The size of the IPv6 datagram buffer pointed by `aData`.|
|const [otMessageSettings](ot-message-settings) *|[in]|aSettings|A pointer to the message settings or NULL to set default settings.|

#### Note (otIp6NewMessageFromBuffer)

- If `aSettings` is NULL, the link layer security is enabled and the message priority is obtained from IPv6 message itself. If `aSettings` is not NULL, the `aSetting->mPriority` is ignored and obtained from IPv6 message itself.

##### Returns (otIp6NewMessageFromBuffer)

- A pointer to the message or NULL if malformed IPv6 header or insufficient message buffers are available.

###### See Also (otIp6NewMessageFromBuffer)

- [otMessageFree](api-message#ot-message-free)

### otIp6SetReceiveCallback

`void otIp6SetReceiveCallback(otInstance *aInstance, otIp6ReceiveCallback aCallback, void *aCallbackContext)`

**Description:** Registers a callback to provide received IPv6 datagrams.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otIp6ReceiveCallback](api-ip6#ot-ip6-receive-callback)|[in]|aCallback|A pointer to a function that is called when an IPv6 datagram is received or NULL to disable the callback.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|

By default, this callback does not pass Thread control traffic. See [otIp6SetReceiveFilterEnabled()](api-ip6#ot-ip6-set-receive-filter-enabled) to change the Thread control traffic filter setting.

#### See Also (otIp6SetReceiveCallback)

- [otIp6IsReceiveFilterEnabled](api-ip6#ot-ip6-is-receive-filter-enabled)
- [otIp6SetReceiveFilterEnabled](api-ip6#ot-ip6-set-receive-filter-enabled)

### otIp6SetAddressCallback

`void otIp6SetAddressCallback(otInstance *aInstance, otIp6AddressCallback aCallback, void *aCallbackContext)`

**Description:** Registers a callback to notify internal IPv6 address changes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otIp6AddressCallback](api-ip6#ot-ip6-address-callback)|[in]|aCallback|A pointer to a function that is called when an internal IPv6 address is added or removed. NULL to disable the callback.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|

### otIp6IsReceiveFilterEnabled

`bool otIp6IsReceiveFilterEnabled(otInstance *aInstance)`

**Description:** Indicates whether or not Thread control traffic is filtered out when delivering IPv6 datagrams via the callback specified in [otIp6SetReceiveCallback()](api-ip6#ot-ip6-set-receive-callback).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otIp6IsReceiveFilterEnabled)

- TRUE if Thread control traffic is filtered out, FALSE otherwise.

##### See Also (otIp6IsReceiveFilterEnabled)

- [otIp6SetReceiveCallback](api-ip6#ot-ip6-set-receive-callback)
- [otIp6SetReceiveFilterEnabled](api-ip6#ot-ip6-set-receive-filter-enabled)

### otIp6SetReceiveFilterEnabled

`void otIp6SetReceiveFilterEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Sets whether or not Thread control traffic is filtered out when delivering IPv6 datagrams via the callback specified in [otIp6SetReceiveCallback()](api-ip6#ot-ip6-set-receive-callback).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnabled|TRUE if Thread control traffic is filtered out, FALSE otherwise.|

#### See Also (otIp6SetReceiveFilterEnabled)

- [otIp6SetReceiveCallback](api-ip6#ot-ip6-set-receive-callback)
- otIsReceiveIp6FilterEnabled

### otIp6Send

`otError otIp6Send(otInstance *aInstance, otMessage *aMessage)`

**Description:** Sends an IPv6 datagram via the Thread interface.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to the message buffer containing the IPv6 datagram.|

The caller transfers ownership of `aMessage` when making this call. OpenThread will free `aMessage` when processing is complete, including when a value other than `OT_ERROR_NONE` is returned.

### otIp6AddUnsecurePort

`otError otIp6AddUnsecurePort(otInstance *aInstance, uint16_t aPort)`

**Description:** Adds a port to the allowed unsecured port list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint16_t|[in]|aPort|The port value.|

### otIp6RemoveUnsecurePort

`otError otIp6RemoveUnsecurePort(otInstance *aInstance, uint16_t aPort)`

**Description:** Removes a port from the allowed unsecure port list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint16_t|[in]|aPort|The port value.|

#### Note (otIp6RemoveUnsecurePort)

- This function removes `aPort` by overwriting `aPort` with the element after `aPort` in the internal port list. Be careful when calling [otIp6GetUnsecurePorts()](api-ip6#ot-ip6-get-unsecure-ports) followed by [otIp6RemoveUnsecurePort()](api-ip6#ot-ip6-remove-unsecure-port) to remove unsecure ports.

### otIp6RemoveAllUnsecurePorts

`void otIp6RemoveAllUnsecurePorts(otInstance *aInstance)`

**Description:** Removes all ports from the allowed unsecure port list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otIp6GetUnsecurePorts

`const uint16_t * otIp6GetUnsecurePorts(otInstance *aInstance, uint8_t *aNumEntries)`

**Description:** Returns a pointer to the unsecure port list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t *|[out]|aNumEntries|The number of entries in the list.|

#### Note (otIp6GetUnsecurePorts)

- Port value 0 is used to indicate an invalid entry.

##### Returns (otIp6GetUnsecurePorts)

- A pointer to the unsecure port list.

### otIp6IsAddressEqual

`bool otIp6IsAddressEqual(const otIp6Address *aFirst, const otIp6Address *aSecond)`

**Description:** Test if two IPv6 addresses are the same.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aFirst|A pointer to the first IPv6 address to compare.|
|const [otIp6Address](ot-ip6-address) *|[in]|aSecond|A pointer to the second IPv6 address to compare.|

### otIp6IsLinkLocalUnicast

`bool otIp6IsLinkLocalUnicast(const otIp6Address *aAddress)`

**Description:** Test whether or not the IPv6 address is a link-local unicast address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to the IPv6 address to test.|

### otIp6FormLinkLocalAddressFromExtAddress

`void otIp6FormLinkLocalAddressFromExtAddress(const otExtAddress *aExtAddress, otIp6Address *aAddress)`

**Description:** Forms a link-local unicast IPv6 address from the Interface Identifier generated from the given MAC Extended Address with the universal/local bit inverted.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|A pointer to the MAC Extended Address (used to generate the IID).|
|[otIp6Address](ot-ip6-address) *|[out]|aAddress|A pointer to output the IPv6 link-local unicast address.|

### otIp6ExtractExtAddressFromIp6AddressIid

`void otIp6ExtractExtAddressFromIp6AddressIid(const otIp6Address *aAddress, otExtAddress *aExtAddress)`

**Description:** Extracts the MAC Extended Address from the Interface Identifier of the given IPv6 address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to the IPv6 address.|
|[otExtAddress](ot-ext-address) *|[out]|aExtAddress|A pointer to output the MAC Extended Address (generated from the IID).|

### otIp6ArePrefixesEqual

`bool otIp6ArePrefixesEqual(const otIp6Prefix *aFirst, const otIp6Prefix *aSecond)`

**Description:** Test if two IPv6 prefixes are the same.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Prefix](ot-ip6-prefix) *|[in]|aFirst|A pointer to the first IPv6 prefix to compare.|
|const [otIp6Prefix](ot-ip6-prefix) *|[in]|aSecond|A pointer to the second IPv6 prefix to compare.|

### otIp6AddressFromString

`otError otIp6AddressFromString(const char *aString, otIp6Address *aAddress)`

**Description:** Converts a human-readable IPv6 address string into a binary representation.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const char *|[in]|aString|A pointer to a NULL-terminated string.|
|[otIp6Address](ot-ip6-address) *|[out]|aAddress|A pointer to an IPv6 address.|

### otIp6PrefixFromString

`otError otIp6PrefixFromString(const char *aString, otIp6Prefix *aPrefix)`

**Description:** Converts a human-readable IPv6 prefix string into a binary representation.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const char *|[in]|aString|A pointer to a NULL-terminated string.|
|[otIp6Prefix](ot-ip6-prefix) *|[out]|aPrefix|A pointer to an IPv6 prefix.|

The `aString` parameter should be a string in the format "<address>/<plen>", where `<address>` is an IPv6 address and `<plen>` is a prefix length.

### otIp6AddressToString

`void otIp6AddressToString(const otIp6Address *aAddress, char *aBuffer, uint16_t aSize)`

**Description:** Converts a given IPv6 address to a human-readable string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to an IPv6 address (MUST NOT be NULL).|
|char *|[out]|aBuffer|A pointer to a char array to output the string (MUST NOT be NULL).|
|uint16_t|[in]|aSize|The size of `aBuffer` (in bytes). Recommended to use `OT_IP6_ADDRESS_STRING_SIZE`.|

The IPv6 address string is formatted as 16 hex values separated by ':' (i.e., "%x:%x:%x:...:%x").

If the resulting string does not fit in `aBuffer` (within its `aSize` characters), the string will be truncated but the outputted string is always null-terminated.

### otIp6SockAddrToString

`void otIp6SockAddrToString(const otSockAddr *aSockAddr, char *aBuffer, uint16_t aSize)`

**Description:** Converts a given IPv6 socket address to a human-readable string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSockAddr](ot-sock-addr) *|[in]|aSockAddr|A pointer to an IPv6 socket address (MUST NOT be NULL).|
|char *|[out]|aBuffer|A pointer to a char array to output the string (MUST NOT be NULL).|
|uint16_t|[in]|aSize|The size of `aBuffer` (in bytes). Recommended to use `OT_IP6_SOCK_ADDR_STRING_SIZE`.|

The IPv6 socket address string is formatted as [`address`]:`port` where `address` is shown as 16 hex values separated by `:` and `port` is the port number in decimal format, for example "[%x:%x:...:%x]:%u".

If the resulting string does not fit in `aBuffer` (within its `aSize` characters), the string will be truncated but the outputted string is always null-terminated.

### otIp6PrefixToString

`void otIp6PrefixToString(const otIp6Prefix *aPrefix, char *aBuffer, uint16_t aSize)`

**Description:** Converts a given IPv6 prefix to a human-readable string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Prefix](ot-ip6-prefix) *|[in]|aPrefix|A pointer to an IPv6 prefix (MUST NOT be NULL).|
|char *|[out]|aBuffer|A pointer to a char array to output the string (MUST NOT be NULL).|
|uint16_t|[in]|aSize|The size of `aBuffer` (in bytes). Recommended to use `OT_IP6_PREFIX_STRING_SIZE`.|

The IPv6 address string is formatted as "%x:%x:%x:...[::]/plen".

If the resulting string does not fit in `aBuffer` (within its `aSize` characters), the string will be truncated but the outputted string is always null-terminated.

### otIp6PrefixMatch

`uint8_t otIp6PrefixMatch(const otIp6Address *aFirst, const otIp6Address *aSecond)`

**Description:** Returns the prefix match length (bits) for two IPv6 addresses.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aFirst|A pointer to the first IPv6 address.|
|const [otIp6Address](ot-ip6-address) *|[in]|aSecond|A pointer to the second IPv6 address.|

#### Returns (otIp6PrefixMatch)

- The prefix match length in bits.

### otIp6GetPrefix

`void otIp6GetPrefix(const otIp6Address *aAddress, uint8_t aLength, otIp6Prefix *aPrefix)`

**Description:** Gets a prefix with `aLength` from `aAddress`.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to an IPv6 address.|
|uint8_t|[in]|aLength|The length of prefix in bits.|
|[otIp6Prefix](ot-ip6-prefix) *|[out]|aPrefix|A pointer to output the IPv6 prefix.|

### otIp6IsAddressUnspecified

`bool otIp6IsAddressUnspecified(const otIp6Address *aAddress)`

**Description:** Indicates whether or not a given IPv6 address is the Unspecified Address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|A pointer to an IPv6 address.|

### otIp6SelectSourceAddress

`otError otIp6SelectSourceAddress(otInstance *aInstance, otMessageInfo *aMessageInfo)`

**Description:** Perform OpenThread source address selection.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMessageInfo](ot-message-info) *|[inout]|aMessageInfo|A pointer to the message information.|

### otIp6IsSlaacEnabled

`bool otIp6IsSlaacEnabled(otInstance *aInstance)`

**Description:** Indicates whether the SLAAC module is enabled or not.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

`OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE` build-time feature must be enabled.

### otIp6SetSlaacEnabled

`void otIp6SetSlaacEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Enables/disables the SLAAC module.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnabled|TRUE to enable, FALSE to disable.|

`OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE` build-time feature must be enabled.

When SLAAC module is enabled, SLAAC addresses (based on on-mesh prefixes in Network Data) are added to the interface. When SLAAC module is disabled any previously added SLAAC address is removed.

### otIp6SetSlaacPrefixFilter

`void otIp6SetSlaacPrefixFilter(otInstance *aInstance, otIp6SlaacPrefixFilter aFilter)`

**Description:** Sets the SLAAC module filter handler.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otIp6SlaacPrefixFilter](api-ip6#ot-ip6-slaac-prefix-filter)|[in]|aFilter|A pointer to SLAAC prefix filter handler, or NULL to disable filtering.|

`OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE` build-time feature must be enabled.

The filter handler is called by SLAAC module when it is about to add a SLAAC address based on a prefix to decide whether the address should be added or not.

A NULL filter handler disables filtering and allows all SLAAC addresses to be added.

If this function is not called, the default filter used by SLAAC module will be NULL (filtering is disabled).

### otIp6RegisterMulticastListeners

`otError otIp6RegisterMulticastListeners(otInstance *aInstance, const otIp6Address *aAddresses, uint8_t aAddressNum, const uint32_t *aTimeout, otIp6RegisterMulticastListenersCallback aCallback, void *aContext)`

**Description:** Registers Multicast Listeners to Primary Backbone Router.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddresses|A Multicast Address Array to register.|
|uint8_t|[in]|aAddressNum|The number of Multicast Address to register (0 if `aAddresses` is NULL).|
|const uint32_t *|[in]|aTimeout|A pointer to the timeout value (in seconds) to be included in MLR.req. A timeout value of 0 removes the corresponding Multicast Listener. If NULL, MLR.req would have no Timeout Tlv by default.|
|[otIp6RegisterMulticastListenersCallback](api-ip6#ot-ip6-register-multicast-listeners-callback)|[in]|aCallback|A pointer to the callback function.|
|void *|[in]|aContext|A pointer to the user context.|

`OPENTHREAD_CONFIG_TMF_PROXY_MLR_ENABLE` and `OPENTHREAD_CONFIG_COMMISSIONER_ENABLE` must be enabled.

#### See Also (otIp6RegisterMulticastListeners)

- [otIp6RegisterMulticastListenersCallback](api-ip6#ot-ip6-register-multicast-listeners-callback)

### otIp6SetMeshLocalIid

`otError otIp6SetMeshLocalIid(otInstance *aInstance, const otIp6InterfaceIdentifier *aIid)`

**Description:** Sets the Mesh Local IID (for test purpose).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6InterfaceIdentifier](ot-ip6-interface-identifier) *|[in]|aIid|A pointer to the Mesh Local IID to set.|

Requires `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE`.

### otIp6ProtoToString

`const char * otIp6ProtoToString(uint8_t aIpProto)`

**Description:** Converts a given IP protocol number to a human-readable string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|uint8_t|[in]|aIpProto|An IP protocol number (`OT_IP6_PROTO_*` enumeration).|

#### Returns (otIp6ProtoToString)

- A string representing `aIpProto`.

### otIp6GetBorderRoutingCounters

`const otBorderRoutingCounters * otIp6GetBorderRoutingCounters(otInstance *aInstance)`

**Description:** Gets the Border Routing counters.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

`OPENTHREAD_CONFIG_IP6_BR_COUNTERS_ENABLE` build-time feature must be enabled.

#### Returns (otIp6GetBorderRoutingCounters)

- A pointer to the Border Routing counters.

### otIp6ResetBorderRoutingCounters

`void otIp6ResetBorderRoutingCounters(otInstance *aInstance)`

**Description:** Resets the Border Routing counters.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

## Macros

`#define OT_IP6_PREFIX_SIZE 8`

**Description**: Size of an IPv6 prefix (bytes)

`#define OT_IP6_PREFIX_BITSIZE (OT_IP6_PREFIX_SIZE * 8)`

**Description**: Size of an IPv6 prefix (bits)

`#define OT_IP6_IID_SIZE 8`

**Description**: Size of an IPv6 Interface Identifier (bytes)

`#define OT_IP6_ADDRESS_SIZE 16`

**Description**: Size of an IPv6 address (bytes)

`#define OT_IP6_ADDRESS_BITSIZE (OT_IP6_ADDRESS_SIZE * 8)`

**Description**: Size of an IPv6 address (bits)

`#define OT_IP6_HEADER_SIZE 40`

**Description**: Size of an IPv6 header (bytes)

`#define OT_IP6_HEADER_PROTO_OFFSET 6`

**Description**: Offset of the proto field in the IPv6 header (bytes)

`#define OT_IP6_ADDRESS_STRING_SIZE 40`

**Description**: Recommended size for string representation of an IPv6 address.

`#define OT_IP6_SOCK_ADDR_STRING_SIZE 48`

**Description**: Recommended size for string representation of an IPv6 socket address.

`#define OT_IP6_PREFIX_STRING_SIZE 45`

**Description**: Recommended size for string representation of an IPv6 prefix.

`#define OT_IP6_MAX_MLR_ADDRESSES 15`

**Description**: Max number of IPv6 addresses supported by Multicast Listener Registration.
