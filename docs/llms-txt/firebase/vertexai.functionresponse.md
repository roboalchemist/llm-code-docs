# Source: https://firebase.google.com/docs/reference/js/vertexai.functionresponse.md.txt

# FunctionResponse interface

The result output from a [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface) that contains a string representing the [FunctionDeclaration.name](https://firebase.google.com/docs/reference/js/vertexai.functiondeclaration.md#functiondeclarationname) and a structured JSON object containing any output from the function is used as context to the model. This should contain the result of a [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface) made based on model prediction.

**Signature:**  

    export interface FunctionResponse 

## Properties

|                                                    Property                                                     |  Type  | Description |
|-----------------------------------------------------------------------------------------------------------------|--------|-------------|
| [name](https://firebase.google.com/docs/reference/js/vertexai.functionresponse.md#functionresponsename)         | string |             |
| [response](https://firebase.google.com/docs/reference/js/vertexai.functionresponse.md#functionresponseresponse) | object |             |

## FunctionResponse.name

**Signature:**  

    name: string;

## FunctionResponse.response

**Signature:**  

    response: object;