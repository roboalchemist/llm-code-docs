# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfig.md.txt

# FirebaseRemoteConfigSwift Framework Reference

# RemoteConfig

    public extension RemoteConfig

- `


  ### [decoded(asType:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB5SwiftE7decoded6asTypexxm_tKSeRzlF)


  ` Decodes a struct from the respective Remote Config values.

  #### Declaration

  Swift

      func decoded<Value>(asType: Value.Type = Value.self) throws -> Value where Value : Decodable

  #### Parameters

  |---|---|
  | ` asType ` | The type to decode to. |

- `


  ### [setDefaults(from:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB5SwiftE11setDefaults4fromyx_tKSERzlF)


  ` Sets config defaults from an encodable struct.

  #### Declaration

  Swift

      func setDefaults<Value>(from value: Value) throws where Value : Encodable

  #### Parameters

  |---|---|
  | ` value ` | The object to use to set the defaults. |

- `


  ### [subscript(decodedValue:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB5SwiftE12decodedValuexSgSS_tcSeRzluip)


  ` Return a typed RemoteConfigValue for a key.

  #### Declaration

  Swift

      subscript<T>(decodedValue key: String) -> T? where T : Decodable { get }

  #### Parameters

  |---|---|
  | ` key ` | A Remote Config key. |

  #### Return Value

  A typed RemoteConfigValue.
- `


  ### [subscript(jsonValue:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB5SwiftE9jsonValueSDySSs11AnyHashableVGSgSS_tcip)


  ` Return a Dictionary for a RemoteConfig JSON key.

  #### Declaration

  Swift

      subscript(jsonValue key: String) -> [String : AnyHashable]? { get }

  #### Parameters

  |---|---|
  | ` key ` | A Remote Config key. |

  #### Return Value

  A Dictionary representing a RemoteConfig JSON value.