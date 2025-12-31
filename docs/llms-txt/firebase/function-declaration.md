# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration.md.txt

# Firebase.AI.FunctionDeclaration Struct Reference

# Firebase.AI.FunctionDeclaration

Structured representation of a function declaration.

## Summary

This [FunctionDeclaration](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration#struct_firebase_1_1_a_i_1_1_function_declaration) is a representation of a block of code that can be used as a [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool) by the model and executed by the client.

Function calling can be used to provide data to the model that was not known at the time it was trained (for example, the current date or weather conditions) or to allow it to interact with external systems (for example, making an API request or querying/updating a database). For more details and use cases, see [Introduction to function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling).

| ### Constructors and Destructors ||
|---|---|
| [FunctionDeclaration](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration#struct_firebase_1_1_a_i_1_1_function_declaration_1a978e9b4d2dd54c0819e711b704768868)`(string name, string description, IDictionary< string, `[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)` > parameters, IEnumerable< string > optionalParameters)` Constructs a new [FunctionDeclaration](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration#struct_firebase_1_1_a_i_1_1_function_declaration). ||

## Public functions

### FunctionDeclaration

```c#
 Firebase::AI::FunctionDeclaration::FunctionDeclaration(
  string name,
  string description,
  IDictionary< string, Schema > parameters,
  IEnumerable< string > optionalParameters
)
```  
Constructs a new [FunctionDeclaration](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration#struct_firebase_1_1_a_i_1_1_function_declaration).

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                                                                                                                                                                       ||
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|---------------------------------------------------------------------------------------------------------------------------------| | `name`               | The name of the function; must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 63.                | | `description`        | A brief description of the function.                                                                                            | | `parameters`         | Describes the parameters to this function.                                                                                      | | `optionalParameters` | The names of parameters that may be omitted by the model in function calls; by default, all parameters are considered required. | |