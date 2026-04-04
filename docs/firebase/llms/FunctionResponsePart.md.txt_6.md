# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.md.txt

# FirebaseAILogic Framework Reference

# FunctionResponsePart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct FunctionResponsePart : https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html

Result output from a function call.

Contains a string representing the `FunctionDeclaration.name` and a structured JSON object
containing any output from the function is used as context to the model. This should contain the
result of a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html` made based on model prediction.
- `


  ### [functionId](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart#/s:15FirebaseAILogic20FunctionResponsePartV10functionIdSSSgvp)


  ` Matching `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html#/s:15FirebaseAILogic16FunctionCallPartV10functionIdSSSgvp` for a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html`, if one was provided.

  #### Declaration

  Swift

      public var functionId: String? { get }

- `


  ### [name](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart#/s:15FirebaseAILogic20FunctionResponsePartV4nameSSvp)


  ` The name of the function that was called.

  #### Declaration

  Swift

      public var name: String { get }

- `


  ### [response](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart#/s:15FirebaseAILogic20FunctionResponsePartV8responseSDySSAA9JSONValueOGvp)


  ` The function's response or return value.

  #### Declaration

  Swift

      public var response: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Typealiases.html#/s:15FirebaseAILogic10JSONObjecta { get }

- `


  ### [isThought](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart#/s:15FirebaseAILogic4PartP9isThoughtSbvp)


  `

  #### Declaration

  Swift

      public var isThought: Bool { get }

- `


  ### [init(name:response:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart#/s:15FirebaseAILogic20FunctionResponsePartV4name8responseACSS_SDySSAA9JSONValueOGtcfc)


  ` Constructs a new `FunctionResponse`.

  #### Declaration

  Swift

      public init(name: String, response: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Typealiases.html#/s:15FirebaseAILogic10JSONObjecta)

  #### Parameters

  |---|---|
  | ` name ` | The name of the function that was called. |
  | ` response ` | The function's response. |

- `


  ### [init(name:response:functionId:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart#/s:15FirebaseAILogic20FunctionResponsePartV4name8response10functionIdACSS_SDySSAA9JSONValueOGSSSgtcfc)


  ` Constructs a new `FunctionResponse`.

  #### Declaration

  Swift

      public init(name: String, response: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Typealiases.html#/s:15FirebaseAILogic10JSONObjecta, functionId: String? = nil)

  #### Parameters

  |---|---|
  | ` name ` | The name of the function that was called. |
  | ` response ` | The function's response. |
  | ` functionId ` | Matching `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html#/s:15FirebaseAILogic16FunctionCallPartV10functionIdSSSgvp` for a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html`, if one was provided. |