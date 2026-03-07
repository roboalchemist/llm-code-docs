# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-error.md

# Error

This module includes error definitions used in OpenThread. 

## Typedefs

### otError

`enum OT_MUST_USE_RESULT otError`

**Description:**

Represents error codes used throughout OpenThread.

## Functions

### otThreadErrorToString

`const char * otThreadErrorToString(otError aError)`

**Description:** Converts an otError enum into a string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otError](api-error#ot-error)|[in]|aError|An otError enum.|

**Returns**

- A string representation of an otError.