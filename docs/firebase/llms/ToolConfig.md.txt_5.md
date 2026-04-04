# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ToolConfig.md.txt

# FirebaseVertexAI Framework Reference

# ToolConfig

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ToolConfig : Sendable

    extension ToolConfig: Encodable

Tool configuration for any `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool.html` specified in the request.
- `


  ### [init(functionCallingConfig:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ToolConfig#/s:16FirebaseVertexAI10ToolConfigV015functionCallingE0AcA08FunctiongE0VSg_tcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(functionCallingConfig: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallingConfig.html? = nil)