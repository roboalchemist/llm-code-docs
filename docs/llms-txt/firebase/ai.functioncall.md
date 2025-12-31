# Source: https://firebase.google.com/docs/reference/js/ai.functioncall.md.txt

# FunctionCall interface

A predicted [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) returned from the model that contains a string representing the [FunctionDeclaration.name](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclarationname) and a structured JSON object containing the parameters and their values.

**Signature:**  

    export interface FunctionCall 

## Properties

|                                         Property                                          |  Type  |                                                                                        Description                                                                                         |
|-------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [args](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncallargs) | object |                                                                                                                                                                                            |
| [id](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncallid)     | string | The id of the function call. This must be sent back in the associated [FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface). |
| [name](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncallname) | string |                                                                                                                                                                                            |

## FunctionCall.args

**Signature:**  

    args: object;

## FunctionCall.id

The id of the function call. This must be sent back in the associated [FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface).

This property is only supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this property will be `undefined`.

**Signature:**  

    id?: string;

## FunctionCall.name

**Signature:**  

    name: string;