# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs.md.txt

# FirebaseRemoteConfig Framework Reference

# Structures

The following structures are available globally.
- `


  ### [CustomSignalValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue)


  ` Represents a value associated with a key in a custom signal, restricted to the allowed data
  types : String, Int, Double.

  #### Declaration

  Swift

      public struct CustomSignalValue

      extension CustomSignalValue: ExpressibleByStringInterpolation

      extension CustomSignalValue: ExpressibleByIntegerLiteral

      extension CustomSignalValue: ExpressibleByFloatLiteral

- `


  ### [RemoteConfigProperty](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/RemoteConfigProperty)


  ` A property wrapper that listens to a Remote Config value.

  #### Declaration

  Swift

      @available(iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, *)
      @propertyWrapper
      @MainActor
      public struct RemoteConfigProperty<T> : DynamicProperty where T : Decodable