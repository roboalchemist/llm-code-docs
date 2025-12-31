# Source: https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md.txt

# FunctionDeclaration interface

Structured representation of a function declaration as defined by the [OpenAPI 3.0 specification](https://spec.openapis.org/oas/v3.0.3). Included in this declaration are the function name and parameters. This `FunctionDeclaration` is a representation of a block of code that can be used as a Tool by the model and executed by the client.

**Signature:**  

    export interface FunctionDeclaration 

## Properties

|                                                       Property                                                        |                                                                                                                Type                                                                                                                 |                                                                                                          Description                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclarationdescription) | string                                                                                                                                                                                                                              | Description and purpose of the function. Model uses it to decide how and whether to call the function.                                                                                                                        |
| [name](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclarationname)               | string                                                                                                                                                                                                                              | The name of the function to call. Must start with a letter or an underscore. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a max length of 64.                                                               |
| [parameters](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclarationparameters)   | [ObjectSchema](https://firebase.google.com/docs/reference/js/ai.objectschema.md#objectschema_class) \| [ObjectSchemaRequest](https://firebase.google.com/docs/reference/js/ai.objectschemarequest.md#objectschemarequest_interface) | Optional. Describes the parameters to this function in JSON Schema Object format. Reflects the Open API 3.03 Parameter Object. Parameter names are case-sensitive. For a function with no parameters, this can be left unset. |

## FunctionDeclaration.description

Description and purpose of the function. Model uses it to decide how and whether to call the function.

**Signature:**  

    description: string;

## FunctionDeclaration.name

The name of the function to call. Must start with a letter or an underscore. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a max length of 64.

**Signature:**  

    name: string;

## FunctionDeclaration.parameters

Optional. Describes the parameters to this function in JSON Schema Object format. Reflects the Open API 3.03 Parameter Object. Parameter names are case-sensitive. For a function with no parameters, this can be left unset.

**Signature:**  

    parameters?: ObjectSchema | ObjectSchemaRequest;