# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart.md.txt

# FirebaseVertexAI Framework Reference

# FunctionCallPart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct FunctionCallPart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html

A predicted function call returned from the model.
- `


  ### [name](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart#/s:16FirebaseVertexAI16FunctionCallPartV4nameSSvp)


  ` The name of the function to call.

  #### Declaration

  Swift

      public var name: String { get }

- `


  ### [args](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart#/s:16FirebaseVertexAI16FunctionCallPartV4argsSDySSAA9JSONValueOGvp)


  ` The function parameters and values.

  #### Declaration

  Swift

      public var args: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Typealiases.html#/s:16FirebaseVertexAI10JSONObjecta { get }

- `


  ### [init(name:args:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart#/s:16FirebaseVertexAI16FunctionCallPartV4name4argsACSS_SDySSAA9JSONValueOGtcfc)


  ` Constructs a new function call part.
  Note

  A `FunctionCallPart` is typically received from the model, rather than created
  manually.

  #### Declaration

  Swift

      public init(name: String, args: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Typealiases.html#/s:16FirebaseVertexAI10JSONObjecta)

  #### Parameters

  |---|---|
  | ` name ` | The name of the function to call. |
  | ` args ` | The function parameters and values. |