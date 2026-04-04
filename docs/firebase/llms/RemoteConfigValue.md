# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfigValue.md.txt

# FirebaseRemoteConfigSwift Framework Reference

# RemoteConfigValue

    public extension RemoteConfigValue

- `
  ``
  ``
  `

  ### [decoded(asType:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfigValue#/s:So20FIRRemoteConfigValueC014FirebaseRemoteB5SwiftE7decoded6asTypexxm_tKSeRzlF)

  `
  `  
  Extracts a RemoteConfigValue JSON-encoded object and decodes it to the requested type.  

  #### Declaration

  Swift  

      func decoded<Value>(asType: Value.Type = Value.self) throws -> Value where Value : Decodable

  #### Parameters

  |----------------|---------------------------------------|
  | ` `*asType*` ` | The type to decode the JSON-object to |