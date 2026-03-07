# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api.md

# API Reference

This module includes the application programming interface to the OpenThread stack. 

Important note: The OpenThread stack is not re-entrant. All OpenThread public APIs, platform APIs, and callbacks MUST be invoked from the same OS context (e.g., the same thread/process or the same task in an RTOS). Any exceptions to this rule, where an API can be called from a different context, will be explicitly documented in that API's reference. Failure to follow this rule can lead to undefined and unexpected behaviors.

If an API call returns an error status (any value other than success), the caller MUST assume any of the output parameters passed to the API may have been modified and are in an indeterminate state. Assuming that an output parameter remains unchanged upon error is invalid. If an API deviates from this default behavior (e.g., by guaranteeing parameters are untouched on error), it will be explicitly documented. Otherwise, developers MUST NOT make this assumption. 

## Modules

[Error](api-error)

[Execution](api-execution)

[IPv6 Networking](api-net)

[Link](api-link)

[Message](api-message)

[Multi Radio Link](api-multi-radio)

[TREL - Thread Stack](api-trel)

[Thread](api-thread)

[Add-Ons](api-addons)

[Provisional](api-provisional)