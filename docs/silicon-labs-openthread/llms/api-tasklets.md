# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-tasklets.md

# Tasklets

This module includes functions that control the Thread stack's execution.

## Functions

### otTaskletsProcess

`void otTaskletsProcess(otInstance *aInstance)`

**Description:** Run all queued OpenThread tasklets at the time this is called.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otTaskletsArePending

`bool otTaskletsArePending(otInstance *aInstance)`

**Description:** Indicates whether or not OpenThread has tasklets pending.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otTaskletsSignalPending

`void otTaskletsSignalPending(otInstance *aInstance)`

**Description:** OpenThread calls this function when the tasklet queue transitions from empty to non-empty.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
