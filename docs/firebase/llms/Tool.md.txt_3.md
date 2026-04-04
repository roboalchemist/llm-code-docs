# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool.md.txt

# FirebaseVertexAI Framework Reference

# Tool

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct Tool : Sendable

    extension Tool: Encodable

A helper tool that the model may use when generating responses.

A `Tool` is a piece of code that enables the system to interact with external systems to perform
an action, or set of actions, outside of knowledge and scope of the model.
- `


  ### [functionDeclarations(_:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool#/s:16FirebaseVertexAI4ToolV20functionDeclarationsyACSayAA19FunctionDeclarationVGFZ)


  ` Creates a tool that allows the model to perform function calling.

  Function calling can be used to provide data to the model that was not known at the time it
  was trained (for example, the current date or weather conditions) or to allow it to interact
  with external systems (for example, making an API request or querying/updating a database).
  For more details and use cases, see [Function calling using the Gemini
  API](http://firebase.google.com/docs/vertex-ai/function-calling?platform=ios).

  #### Declaration

  Swift

      public static func functionDeclarations(_ functionDeclarations: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionDeclaration.html]) -> Tool

  #### Parameters

  |---|---|
  | ` functionDeclarations ` | A list of `FunctionDeclarations` available to the model that can be used for function calling. The model or system does not execute the function. Instead the defined function may be returned as a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart.html` with arguments to the client side for execution. The model may decide to call none, some or all of the declared functions; this behavior may be configured by specifying a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ToolConfig.html` when instantiating the model. When a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart.html` is received, the next conversation turn may contain a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionResponsePart.html` in `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent.html#/s:16FirebaseVertexAI12ModelContentV5partsSayAA4Part_pGvp` with a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent.html#/s:16FirebaseVertexAI12ModelContentV4roleSSSgvp` of `"function"`; this response contains the result of executing the function on the client, providing generation context for the model's next turn. |