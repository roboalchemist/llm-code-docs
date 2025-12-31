# Source: https://firebase.google.com/docs/reference/js/vertexai.functiondeclarationstool.md.txt

# FunctionDeclarationsTool interface

A `FunctionDeclarationsTool` is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model.

**Signature:**  

    export declare interface FunctionDeclarationsTool 

## Properties

|                                                                        Property                                                                         |                                                                  Type                                                                  |                                                                                                                                                                                                                                                                                                                     Description                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [functionDeclarations](https://firebase.google.com/docs/reference/js/vertexai.functiondeclarationstool.md#functiondeclarationstoolfunctiondeclarations) | [FunctionDeclaration](https://firebase.google.com/docs/reference/js/vertexai.functiondeclaration.md#functiondeclaration_interface)\[\] | Optional. One or more function declarations to be passed to the model along with the current user query. Model may decide to call a subset of these functions by populating [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface) in the response. User should provide a [FunctionResponse](https://firebase.google.com/docs/reference/js/vertexai.functionresponse.md#functionresponse_interface) for each function call in the next turn. Based on the function responses, the model will generate the final response back to the user. Maximum 64 function declarations can be provided. |

## FunctionDeclarationsTool.functionDeclarations

Optional. One or more function declarations to be passed to the model along with the current user query. Model may decide to call a subset of these functions by populating [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface) in the response. User should provide a [FunctionResponse](https://firebase.google.com/docs/reference/js/vertexai.functionresponse.md#functionresponse_interface) for each function call in the next turn. Based on the function responses, the model will generate the final response back to the user. Maximum 64 function declarations can be provided.

**Signature:**  

    functionDeclarations?: FunctionDeclaration[];