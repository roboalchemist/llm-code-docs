# Source: https://firebase.google.com/docs/reference/js/ai.liveservertoolcall.md.txt

# LiveServerToolCall interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A request from the model for the client to execute one or more functions.

**Signature:**  

    export interface LiveServerToolCall 

## Properties

|                                                        Property                                                         |                                                    Type                                                     |                        Description                        |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [functionCalls](https://firebase.google.com/docs/reference/js/ai.liveservertoolcall.md#liveservertoolcallfunctioncalls) | [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface)\[\] | ***(Public Preview)*** An array of function calls to run. |
| [type](https://firebase.google.com/docs/reference/js/ai.liveservertoolcall.md#liveservertoolcalltype)                   | 'toolCall'                                                                                                  | ***(Public Preview)***                                    |

## LiveServerToolCall.functionCalls

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An array of function calls to run.

**Signature:**  

    functionCalls: FunctionCall[];

## LiveServerToolCall.type

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    type: 'toolCall';