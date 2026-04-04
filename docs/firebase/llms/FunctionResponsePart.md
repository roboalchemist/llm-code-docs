# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionResponsePart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionResponsePart.md.txt

# FirebaseVertexAI Framework Reference

# FunctionResponsePart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct FunctionResponsePart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html

Result output from a function call.

Contains a string representing the `FunctionDeclaration.name` and a structured JSON object
containing any output from the function is used as context to the model. This should contain the
result of a [FunctionCallPart](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart.html) made based on model prediction.
- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionResponsePart#/s:16FirebaseVertexAI20FunctionResponsePartV4nameSSvp)

  `
  `  
  The name of the function that was called.  

  #### Declaration

  Swift  

      public var name: String { get }

- `
  ``
  ``
  `

  ### [response](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionResponsePart#/s:16FirebaseVertexAI20FunctionResponsePartV8responseSDySSAA9JSONValueOGvp)

  `
  `  
  The function's response or return value.  

  #### Declaration

  Swift  

      public var response: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Typealiases.html#/s:16FirebaseVertexAI10JSONObjecta { get }

- `
  ``
  ``
  `

  ### [init(name:response:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionResponsePart#/s:16FirebaseVertexAI20FunctionResponsePartV4name8responseACSS_SDySSAA9JSONValueOGtcfc)

  `
  `  
  Constructs a new `FunctionResponse`.  

  #### Declaration

  Swift  

      public init(name: String, response: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Typealiases.html#/s:16FirebaseVertexAI10JSONObjecta)

  #### Parameters

  |------------------|-------------------------------------------|
  | ` `*name*` `     | The name of the function that was called. |
  | ` `*response*` ` | The function's response.                  |