# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-udp-forward.md

# UDP Forward

This module includes functions for UDP forward feature. 

The functions in this module are available when udp-forward feature (`OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE`) is enabled. 

## Typedefs

### otUdpForwarder

`typedef void(* otUdpForwarder) (otMessage *aMessage, uint16_t aPeerPort, otIp6Address *aPeerAddr, uint16_t aSockPort, void *aContext)`

**Description:**

Pointer delivers the UDP packet to host and host should send the packet through its own network stack.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aMessage|A pointer to the UDP Message.|
||[in]|aPeerPort|The destination UDP port.|
||[in]|aPeerAddr|A pointer to the destination IPv6 address.|
||[in]|aSockPort|The source UDP port.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

## Functions

### otUdpForwardSetForwarder

`void otUdpForwardSetForwarder(otInstance *aInstance, otUdpForwarder aForwarder, void *aContext)`

**Description:** Set UDP forward callback to deliver UDP packets to host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpForwarder](api-udp-forward#ot-udp-forwarder)|[in]|aForwarder|A pointer to a function called to forward UDP packet to host.|
|void *|[in]|aContext|A pointer to application-specific context.|

### otUdpForwardReceive

`void otUdpForwardReceive(otInstance *aInstance, otMessage *aMessage, uint16_t aPeerPort, const otIp6Address *aPeerAddr, uint16_t aSockPort)`

**Description:** Handle a UDP packet received from host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to the UDP Message.|
|uint16_t|[in]|aPeerPort|The source UDP port.|
|const [otIp6Address](ot-ip6-address) *|[in]|aPeerAddr|A pointer to the source address.|
|uint16_t|[in]|aSockPort|The destination UDP port.|

**Warnings**

- No matter the call success or fail, the message is freed.

### otUdpIsPortInUse

`bool otUdpIsPortInUse(otInstance *aInstance, uint16_t port)`

**Description:** Determines if the given UDP port is exclusively opened by OpenThread API.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint16_t|[in]|port|UDP port number to verify.|