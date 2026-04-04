# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ToolConfig.md.txt

# FirebaseAILogic Framework Reference

# ToolConfig

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ToolConfig : Sendable

    extension ToolConfig: Encodable

Tool configuration for any `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html` specified in the request.
- `


  ### [init(functionCallingConfig:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ToolConfig#/s:15FirebaseAILogic10ToolConfigV015functionCallingD0AcA08FunctionfD0VSg_tcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(functionCallingConfig: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallingConfig.html? = nil)