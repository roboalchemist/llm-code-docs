# Source: https://firebase.google.com/docs/reference/js/vertexai.functioncallpart.md.txt

# FunctionCallPart interface

Content part interface if the part represents a [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface).

**Signature:**  

    export interface FunctionCallPart 

## Properties

|                                                            Property                                                             |                                                     Type                                                      | Description |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------|
| [functionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncallpart.md#functioncallpartfunctioncall)         | [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface) |             |
| [functionResponse](https://firebase.google.com/docs/reference/js/vertexai.functioncallpart.md#functioncallpartfunctionresponse) | never                                                                                                         |             |
| [inlineData](https://firebase.google.com/docs/reference/js/vertexai.functioncallpart.md#functioncallpartinlinedata)             | never                                                                                                         |             |
| [text](https://firebase.google.com/docs/reference/js/vertexai.functioncallpart.md#functioncallparttext)                         | never                                                                                                         |             |

## FunctionCallPart.functionCall

**Signature:**  

    functionCall: FunctionCall;

## FunctionCallPart.functionResponse

**Signature:**  

    functionResponse?: never;

## FunctionCallPart.inlineData

**Signature:**  

    inlineData?: never;

## FunctionCallPart.text

**Signature:**  

    text?: never;