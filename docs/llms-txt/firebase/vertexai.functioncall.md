# Source: https://firebase.google.com/docs/reference/js/vertexai.functioncall.md.txt

# FunctionCall interface

A predicted [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface) returned from the model that contains a string representing the [FunctionDeclaration.name](https://firebase.google.com/docs/reference/js/vertexai.functiondeclaration.md#functiondeclarationname) and a structured JSON object containing the parameters and their values.

**Signature:**  

    export interface FunctionCall 

## Properties

|                                            Property                                             |  Type  | Description |
|-------------------------------------------------------------------------------------------------|--------|-------------|
| [args](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncallargs) | object |             |
| [name](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncallname) | string |             |

## FunctionCall.args

**Signature:**  

    args: object;

## FunctionCall.name

**Signature:**  

    name: string;