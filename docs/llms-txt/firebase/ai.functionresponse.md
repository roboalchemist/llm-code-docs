# Source: https://firebase.google.com/docs/reference/js/ai.functionresponse.md.txt

# FunctionResponse interface

The result output from a [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) that contains a string representing the [FunctionDeclaration.name](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclarationname) and a structured JSON object containing any output from the function is used as context to the model. This should contain the result of a [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) made based on model prediction.

**Signature:**  

    export interface FunctionResponse 

## Properties

|                                                 Property                                                  |  Type  |                                                      Description                                                       |
|-----------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------|
| [id](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponseid)             | string | The id of the [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface). |
| [name](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponsename)         | string |                                                                                                                        |
| [response](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponseresponse) | object |                                                                                                                        |

## FunctionResponse.id

The id of the [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface).

This property is only supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this property will be `undefined`.

**Signature:**  

    id?: string;

## FunctionResponse.name

**Signature:**  

    name: string;

## FunctionResponse.response

**Signature:**  

    response: object;