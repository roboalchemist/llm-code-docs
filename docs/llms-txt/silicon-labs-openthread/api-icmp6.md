# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-icmp6.md

# ICMPv6

This module includes functions that control ICMPv6 communication. 

## Modules

[otIcmp6Header](ot-icmp6-header)

[otIcmp6Handler](ot-icmp6-handler)

## Enumerations

### otIcmp6Type

```
enum otIcmp6Type {
    OT_ICMP6_TYPE_DST_UNREACH = 1
    OT_ICMP6_TYPE_PACKET_TO_BIG = 2
    OT_ICMP6_TYPE_TIME_EXCEEDED = 3
    OT_ICMP6_TYPE_PARAMETER_PROBLEM = 4
    OT_ICMP6_TYPE_ECHO_REQUEST = 128
    OT_ICMP6_TYPE_ECHO_REPLY = 129
    OT_ICMP6_TYPE_ROUTER_SOLICIT = 133
    OT_ICMP6_TYPE_ROUTER_ADVERT = 134
    OT_ICMP6_TYPE_NEIGHBOR_SOLICIT = 135
    OT_ICMP6_TYPE_NEIGHBOR_ADVERT = 136
}
```

**Description:**

ICMPv6 Message Types.

**Enumerator:**

|   |   |
|---|---|
|OT_ICMP6_TYPE_DST_UNREACH|Destination Unreachable.|
|OT_ICMP6_TYPE_PACKET_TO_BIG|Packet To Big.|
|OT_ICMP6_TYPE_TIME_EXCEEDED|Time Exceeded.|
|OT_ICMP6_TYPE_PARAMETER_PROBLEM|Parameter Problem.|
|OT_ICMP6_TYPE_ECHO_REQUEST|Echo Request.|
|OT_ICMP6_TYPE_ECHO_REPLY|Echo Reply.|
|OT_ICMP6_TYPE_ROUTER_SOLICIT|Router Solicitation.|
|OT_ICMP6_TYPE_ROUTER_ADVERT|Router Advertisement.|
|OT_ICMP6_TYPE_NEIGHBOR_SOLICIT|Neighbor Solicitation.|
|OT_ICMP6_TYPE_NEIGHBOR_ADVERT|Neighbor Advertisement.|

### otIcmp6Code

```
enum otIcmp6Code {
    OT_ICMP6_CODE_DST_UNREACH_NO_ROUTE = 0
    OT_ICMP6_CODE_DST_UNREACH_PROHIBITED = 1
    OT_ICMP6_CODE_FRAGM_REAS_TIME_EX = 1
}
```

**Description:**

ICMPv6 Message Codes.

**Enumerator:**

|   |   |
|---|---|
|OT_ICMP6_CODE_DST_UNREACH_NO_ROUTE|Destination Unreachable (Type 1) - No Route.|
|OT_ICMP6_CODE_DST_UNREACH_PROHIBITED|Destination Unreachable (Type 1) - Administratively Prohibited.|
|OT_ICMP6_CODE_FRAGM_REAS_TIME_EX|Time Exceeded (Type 3) - Fragment Reassembly.|

### otIcmp6EchoMode

```
enum otIcmp6EchoMode {
    OT_ICMP6_ECHO_HANDLER_DISABLED = 0
    OT_ICMP6_ECHO_HANDLER_UNICAST_ONLY = 1
    OT_ICMP6_ECHO_HANDLER_MULTICAST_ONLY = 2
    OT_ICMP6_ECHO_HANDLER_ALL = 3
    OT_ICMP6_ECHO_HANDLER_RLOC_ALOC_ONLY = 4
}
```

**Description:**

ICMPv6 Echo Reply Modes.

**Enumerator:**

|   |   |
|---|---|
|OT_ICMP6_ECHO_HANDLER_DISABLED|ICMPv6 Echo processing disabled.|
|OT_ICMP6_ECHO_HANDLER_UNICAST_ONLY|ICMPv6 Echo processing enabled only for unicast requests only.|
|OT_ICMP6_ECHO_HANDLER_MULTICAST_ONLY|ICMPv6 Echo processing enabled only for multicast requests only.|
|OT_ICMP6_ECHO_HANDLER_ALL|ICMPv6 Echo processing enabled for unicast and multicast requests.|
|OT_ICMP6_ECHO_HANDLER_RLOC_ALOC_ONLY|ICMPv6 Echo processing enabled for RLOC/ALOC destinations only.|

## Typedefs

### otIcmp6Type

`typedef enum otIcmp6Type otIcmp6Type`

**Description:**

ICMPv6 Message Types.

### otIcmp6Code

`typedef enum otIcmp6Code otIcmp6Code`

**Description:**

ICMPv6 Message Codes.

### otIcmp6Header

`typedef struct otIcmp6Header otIcmp6Header`

**Description:**

Represents an ICMPv6 header.

### otIcmp6ReceiveCallback

`typedef void(* otIcmp6ReceiveCallback) (void *aContext, otMessage *aMessage, const otMessageInfo *aMessageInfo, const otIcmp6Header *aIcmpHeader)`

**Description:**

This callback allows OpenThread to inform the application of a received ICMPv6 message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to arbitrary context information.|
||[in]|aMessage|A pointer to the received message.|
||[in]|aMessageInfo|A pointer to message information associated with `aMessage`.|
||[in]|aIcmpHeader|A pointer to the received ICMPv6 header.|

**Details:**

### otIcmp6Handler

`typedef struct otIcmp6Handler otIcmp6Handler`

**Description:**

Implements ICMPv6 message handler.

### otIcmp6EchoMode

`typedef enum otIcmp6EchoMode otIcmp6EchoMode`

**Description:**

ICMPv6 Echo Reply Modes.

## Variables

### OT_TOOL_PACKED_END

```
OT_TOOL_PACKED_BEGIN struct otIcmp6Header OT_TOOL_PACKED_END
```

## Functions

### otIcmp6GetEchoMode

`otIcmp6EchoMode otIcmp6GetEchoMode(otInstance *aInstance)`

**Description:** Indicates whether or not ICMPv6 Echo processing is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otIcmp6SetEchoMode

`void otIcmp6SetEchoMode(otInstance *aInstance, otIcmp6EchoMode aMode)`

**Description:** Sets whether or not ICMPv6 Echo processing is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otIcmp6EchoMode](api-icmp6#ot-icmp6-echo-mode)|[in]|aMode|The ICMPv6 Echo processing mode.|

### otIcmp6RegisterHandler

`otError otIcmp6RegisterHandler(otInstance *aInstance, otIcmp6Handler *aHandler)`

**Description:** Registers a handler to provide received ICMPv6 messages.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otIcmp6Handler](ot-icmp6-handler) *|[in]|aHandler|A pointer to a handler containing callback that is called when an ICMPv6 message is received.|

**Note**

- A handler structure `aHandler` has to be stored in persistent (static) memory. OpenThread does not make a copy of handler structure.

### otIcmp6SendEchoRequest

`otError otIcmp6SendEchoRequest(otInstance *aInstance, otMessage *aMessage, const otMessageInfo *aMessageInfo, uint16_t aIdentifier)`

**Description:** Sends an ICMPv6 Echo Request via the Thread interface.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to the message buffer containing the ICMPv6 payload.|
|const [otMessageInfo](ot-message-info) *|[in]|aMessageInfo|A reference to message information associated with `aMessage`.|
|uint16_t|[in]|aIdentifier|An identifier to aid in matching Echo Replies to this Echo Request. May be zero.|

## Macros

`#define OT_ICMP6_HEADER_DATA_SIZE 4`

**Description**: Size of ICMPv6 Header.

`#define OT_ICMP6_ROUTER_ADVERT_MIN_SIZE 16`

**Description**: Size of a Router Advertisement message without any options.