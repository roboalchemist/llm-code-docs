# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.md.txt

# FirebaseAILogic Framework Reference

# FunctionCallPart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct FunctionCallPart : https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html

A predicted function call returned from the model.
- `


  ### [name](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart#/s:15FirebaseAILogic16FunctionCallPartV4nameSSvp)


  ` The name of the function to call.

  #### Declaration

  Swift

      public var name: String { get }

- `


  ### [args](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart#/s:15FirebaseAILogic16FunctionCallPartV4argsSDySSAA9JSONValueOGvp)


  ` The function parameters and values.

  #### Declaration

  Swift

      public var args: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Typealiases.html#/s:15FirebaseAILogic10JSONObjecta { get }

- `


  ### [isThought](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart#/s:15FirebaseAILogic4PartP9isThoughtSbvp)


  `

  #### Declaration

  Swift

      public var isThought: Bool { get }

- `


  ### [functionId](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart#/s:15FirebaseAILogic16FunctionCallPartV10functionIdSSSgvp)


  ` Unique id of the function call.

  If present, the returned `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.html` should have a matching `functionId` field.

  #### Declaration

  Swift

      public var functionId: String? { get }

- `


  ### [init(name:args:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart#/s:15FirebaseAILogic16FunctionCallPartV4name4argsACSS_SDySSAA9JSONValueOGtcfc)


  ` Constructs a new function call part.
  Note

  A `FunctionCallPart` is typically received from the model, rather than created
  manually.

  #### Declaration

  Swift

      public init(name: String, args: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Typealiases.html#/s:15FirebaseAILogic10JSONObjecta)

  #### Parameters

  |---|---|
  | ` name ` | The name of the function to call. |
  | ` args ` | The function parameters and values. |

- `


  ### [init(name:args:id:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart#/s:15FirebaseAILogic16FunctionCallPartV4name4args2idACSS_SDySSAA9JSONValueOGSSSgtcfc)


  ` Constructs a new function call part.
  Note

  A `FunctionCallPart` is typically received from the model, rather than created
  manually.

  #### Declaration

  Swift

      public init(name: String, args: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Typealiases.html#/s:15FirebaseAILogic10JSONObjecta, id: String? = nil)

  #### Parameters

  |---|---|
  | ` name ` | The name of the function to call. |
  | ` args ` | The function parameters and values. |
  | ` id ` | Unique id of the function call. If present, the returned `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.html` should have a matching `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionResponsePart.html#/s:15FirebaseAILogic20FunctionResponsePartV10functionIdSSSgvp` field. |