# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallingConfig.md.txt

# FirebaseVertexAI Framework Reference

# FunctionCallingConfig

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct FunctionCallingConfig : Sendable

    extension FunctionCallingConfig: Encodable

Configuration for specifying function calling behavior.
- `


  ### [auto()](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallingConfig#/s:16FirebaseVertexAI21FunctionCallingConfigV4autoACyFZ)


  ` Creates a function calling config where the model calls functions at its discretion.
  Note

  This is the default behavior.

  #### Declaration

  Swift

      public static func auto() -> FunctionCallingConfig

- `


  ### [any(allowedFunctionNames:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallingConfig#/s:16FirebaseVertexAI21FunctionCallingConfigV3any07allowedD5NamesACSaySSGSg_tFZ)


  ` Creates a function calling config where the model will always call a provided function.

  #### Declaration

  Swift

      public static func any(allowedFunctionNames: [String]? = nil) -> FunctionCallingConfig

  #### Parameters

  |---|---|
  | ` allowedFunctionNames ` | A set of function names that, when provided, limits the functions that the model will call. |

- `


  ### [none()](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallingConfig#/s:16FirebaseVertexAI21FunctionCallingConfigV4noneACyFZ)


  ` Creates a function calling config where the model will never call a function.
  Note

  This can also be achieved by not passing any `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionDeclaration.html` tools when
  instantiating the model.

  #### Declaration

  Swift

      public static func none() -> FunctionCallingConfig