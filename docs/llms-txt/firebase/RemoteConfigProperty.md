# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/RemoteConfigProperty.md.txt

# FirebaseRemoteConfig Framework Reference

# RemoteConfigProperty

    @available(iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, *)
    @propertyWrapper
    @MainActor
    public struct RemoteConfigProperty<T> : DynamicProperty where T : Decodable

A property wrapper that listens to a Remote Config value.
- `
  ``
  ``
  `

  ### [key](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/RemoteConfigProperty#/s:20FirebaseRemoteConfig0bC8PropertyV3keySSvp)

  `
  `  
  Remote Config key name for this property  

  #### Declaration

  Swift  

      @MainActor
      public let key: String

- `
  ``
  ``
  `

  ### [wrappedValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/RemoteConfigProperty#/s:20FirebaseRemoteConfig0bC8PropertyV12wrappedValuexvp)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      @MainActor
      public var wrappedValue: T { get }

- `
  ``
  ``
  `

  ### [init(key:fallback:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/RemoteConfigProperty#/s:20FirebaseRemoteConfig0bC8PropertyV3key8fallbackACyxGSS_xtcfc)

  `
  `  
  Creates an instance by providing a config key.  

  #### Declaration

  Swift  

      @MainActor
      public init(key: String, fallback: T)

  #### Parameters

  |------------------|---------------------------------------------------------------------------------|
  | ` `*key*` `      | key name                                                                        |
  | ` `*fallback*` ` | The value to fall back to if the key doesn't exist in remote or default configs |