# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool.md.txt

# Firebase.AI.Tool

A helper tool that the model may use when generating responses.

## Summary

A [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool) is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model.

| ### Constructors and Destructors ||
|---|---|
| [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool_1af0704d27cdf64529504943499473939c)`(params `[FunctionDeclaration](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration#struct_firebase_1_1_a_i_1_1_function_declaration)`[] functionDeclarations)` Creates a tool that allows the model to perform function calling. ||
| [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool_1a940acfb6a5cf54df9100a9056f8ba324)`(IEnumerable< `[FunctionDeclaration](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration#struct_firebase_1_1_a_i_1_1_function_declaration)` > functionDeclarations)` Creates a tool that allows the model to perform function calling. ||
| [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool_1a74a37395f428b3091e2b3fbe4e9f74fc)`(`[GoogleSearch](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/google-search#struct_firebase_1_1_a_i_1_1_google_search)` googleSearch)` Creates a tool that allows the model to use Grounding with Google Search. ||
| [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool_1a1628358b2ac53696070f1dcc749c2350)`(`[CodeExecution](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/code-execution#struct_firebase_1_1_a_i_1_1_code_execution)` codeExecution)` Creates a tool that allows the model to use Code Execution. ||
| [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool_1ab0eb1eb191d952df6e63f6071bf6c36c)`(`[UrlContext](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-context#struct_firebase_1_1_a_i_1_1_url_context)` urlContext)` Creates a tool that allows you to provide additional context to the models in the form of public web URLs. ||

## Public functions

### Tool

```c#
 Firebase::AI::Tool::Tool(
  params FunctionDeclaration[] functionDeclarations
)
```  
Creates a tool that allows the model to perform function calling.

<br />

|                                                                                                                               Details                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|------------------------------------------------------------------------------------------------| | `functionDeclarations` | A list of `FunctionDeclarations` available to the model that can be used for function calling. | |

### Tool

```c#
 Firebase::AI::Tool::Tool(
  IEnumerable< FunctionDeclaration > functionDeclarations
)
```  
Creates a tool that allows the model to perform function calling.

<br />

|                                                                                                                               Details                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|------------------------------------------------------------------------------------------------| | `functionDeclarations` | A list of `FunctionDeclarations` available to the model that can be used for function calling. | |

### Tool

```c#
 Firebase::AI::Tool::Tool(
  GoogleSearch googleSearch
)
```  
Creates a tool that allows the model to use Grounding with Google Search.

<br />

|                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `googleSearch` | An empty [GoogleSearch](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/google-search#struct_firebase_1_1_a_i_1_1_google_search) object. The presence of this object in the list of tools enables the model to use Google Search. | |

### Tool

```c#
 Firebase::AI::Tool::Tool(
  CodeExecution codeExecution
)
```  
Creates a tool that allows the model to use Code Execution.

<br />

|                                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                                    ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `codeExecution` | An empty [CodeExecution](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/code-execution#struct_firebase_1_1_a_i_1_1_code_execution) object. The presence of this object in the list of tools enables the model to use Code Execution. | |

### Tool

```c#
 Firebase::AI::Tool::Tool(
  UrlContext urlContext
)
```  
Creates a tool that allows you to provide additional context to the models in the form of public web URLs.

<br />

|                                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                                      ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `urlContext` | An empty [UrlContext](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-context#struct_firebase_1_1_a_i_1_1_url_context) object. The presence of this object in the list of tools enables the model to use Url Contexts. | |