# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-ping-sender.md

# Ping Sender

This file includes the OpenThread API for the ping sender module. 

## Modules

[otPingSenderReply](ot-ping-sender-reply)

[otPingSenderStatistics](ot-ping-sender-statistics)

[otPingSenderConfig](ot-ping-sender-config)

## Typedefs

### otPingSenderReply

`typedef struct otPingSenderReply otPingSenderReply`

**Description:**

Represents a ping reply.

### otPingSenderStatistics

`typedef struct otPingSenderStatistics otPingSenderStatistics`

**Description:**

Represents statistics of a ping request.

### otPingSenderReplyCallback

`typedef void(* otPingSenderReplyCallback) (const otPingSenderReply *aReply, void *aContext)`

**Description:**

Pointer type specifies the callback to notify receipt of a ping reply.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aReply|A pointer to a `otPingSenderReply` containing info about the received ping reply.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otPingSenderStatisticsCallback

`typedef void(* otPingSenderStatisticsCallback) (const otPingSenderStatistics *aStatistics, void *aContext)`

**Description:**

Pointer type specifies the callback to report the ping statistics.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aStatistics|A pointer to a `otPingSenderStatistics` containing info about the received ping statistics.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otPingSenderConfig

`typedef struct otPingSenderConfig otPingSenderConfig`

**Description:**

Represents a ping request configuration.

## Functions

### otPingSenderPing

`otError otPingSenderPing(otInstance *aInstance, const otPingSenderConfig *aConfig)`

**Description:** Starts a ping.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otPingSenderConfig](ot-ping-sender-config) *|[in]|aConfig|The ping config to use.|

### otPingSenderStop

`void otPingSenderStop(otInstance *aInstance)`

**Description:** Stops an ongoing ping.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|