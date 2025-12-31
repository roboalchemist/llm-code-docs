# Source: https://firebase.google.com/docs/reference/js/ai.liveservertoolcallcancellation.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Notification to cancel a previous function call triggered by[LiveServerToolCall](https://firebase.google.com/docs/reference/js/ai.liveservertoolcall.md#liveservertoolcall_interface).

**Signature:**  

    export interface LiveServerToolCallCancellation 

## Properties

|                                                                  Property                                                                   |          Type          |                                                                                                  Description                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [functionIds](https://firebase.google.com/docs/reference/js/ai.liveservertoolcallcancellation.md#liveservertoolcallcancellationfunctionids) | string\[\]             | ***(Public Preview)*** IDs of function calls that were cancelled. These refer to the`id`property of a[FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface). |
| [type](https://firebase.google.com/docs/reference/js/ai.liveservertoolcallcancellation.md#liveservertoolcallcancellationtype)               | 'toolCallCancellation' | ***(Public Preview)***                                                                                                                                                                                        |

## LiveServerToolCallCancellation.functionIds

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

IDs of function calls that were cancelled. These refer to the`id`property of a[FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface).

**Signature:**  

    functionIds: string[];

## LiveServerToolCallCancellation.type

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    type: 'toolCallCancellation';