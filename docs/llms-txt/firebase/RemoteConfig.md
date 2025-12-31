# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfigswift/api/reference/Extensions/RemoteConfig.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig.md.txt

# FirebaseRemoteConfig Framework Reference

# RemoteConfig

    class RemoteConfig : NSObject, NSFastEnumeration

Firebase Remote Config class. The class method `remoteConfig()` can be used
to fetch, activate and read config results and set default config results on the default
Remote Config instance.
- `
  ``
  ``
  `

  ### [lastFetchTime](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(py)lastFetchTime)

  `
  `  
  Last successful fetch completion time.  

  #### Declaration

  Swift  

      var lastFetchTime: Date? { get }

- `
  ``
  ``
  `

  ### [lastFetchStatus](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(py)lastFetchStatus)

  `
  `  
  Last fetch status. The status can be any enumerated value from [RemoteConfigFetchStatus](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus.html).  

  #### Declaration

  Swift  

      var lastFetchStatus: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus.html { get }

- `
  ``
  ``
  `

  ### [configSettings](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(py)configSettings)

  `
  `  
  Config settings are custom settings.  

  #### Declaration

  Swift  

      var configSettings: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigSettings.html { get set }

- `
  ``
  ``
  `

  ### [remoteConfig()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(cm)remoteConfig)

  `
  `  
  Returns the `RemoteConfig` instance configured for the default Firebase app. This singleton
  object contains the complete set of Remote Config parameter values available to the app,
  including the Active Config and Default Config. This object also caches values fetched from the
  Remote Config server until they are copied to the Active Config by calling [activate()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig.html#/c:objc(cs)FIRRemoteConfig(im)activateWithCompletion:). When
  you fetch values from the Remote Config server using the default Firebase app, you should use
  this class method to create and reuse a shared instance of `RemoteConfig`.  

  #### Declaration

  Swift  

      class func remoteConfig() -> RemoteConfig

- `
  ``
  ``
  `

  ### [remoteConfig(app:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(cm)remoteConfigWithApp:)

  `
  `  
  Returns the `RemoteConfig` instance for your (non-default) Firebase appID. Note that Firebase
  analytics does not work for non-default app instances. This singleton object contains the
  complete set of Remote Config parameter values available to the app, including the Active Config
  and Default Config. This object also caches values fetched from the Remote Config Server until
  they are copied to the Active Config by calling `activate())`. When you fetch values
  from the Remote Config Server using the non-default Firebase app, you should use this
  class method to create and reuse shared instance of `RemoteConfig`.  

  #### Declaration

  Swift  

      class func remoteConfig(app: FIRApp) -> RemoteConfig

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)init)

  `
  `  
  Unavailable

  Use +remoteConfig instead.  
  Unavailable. Use +remoteConfig instead.
- `
  ``
  ``
  `

  ### [ensureInitialized()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)ensureInitializedWithCompletionHandler:)

  `
  `  
  Ensures initialization is complete and clients can begin querying for Remote Config values.  

  #### Declaration

  Swift  

      func ensureInitialized() async throws

  #### Parameters

  |---------------------------|--------------------------------------------------------|
  | ` `*completionHandler*` ` | Initialization complete callback with error parameter. |

[## Fetch](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/Fetch)

- `
  ``
  ``
  `

  ### [fetch()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)fetchWithCompletionHandler:)

  `
  `  
  Fetches Remote Config data with a callback. Call [activate()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig.html#/c:objc(cs)FIRRemoteConfig(im)activateWithCompletion:) to make fetched data
  available to your app.

  Note: This method uses a Firebase Installations token to identify the app instance, and once
  it's called, it periodically sends data to the Firebase backend. (see
  `Installations.authToken(completion:)`).
  To stop the periodic sync, call `Installations.delete(completion:)`
  and avoid calling this method again.  

  #### Declaration

  Swift  

      func fetch() async throws -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus.html

  #### Parameters

  |---------------------------|------------------------------------------------------------|
  | ` `*completionHandler*` ` | Fetch operation callback with status and error parameters. |

- `
  ``
  ``
  `

  ### [fetch(withExpirationDuration:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)fetchWithExpirationDuration:completionHandler:)

  `
  `  
  Fetches Remote Config data and sets a duration that specifies how long config data lasts.
  Call `activateWithCompletion:` to make fetched data available to your app.

  Note: This method uses a Firebase Installations token to identify the app instance, and once
  it's called, it periodically sends data to the Firebase backend. (see
  `Installations.authToken(completion:)`).
  To stop the periodic sync, call `Installations.delete(completion:)`
  and avoid calling this method again.  

  #### Declaration

  Swift  

      func fetch(withExpirationDuration expirationDuration: TimeInterval) async throws -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus.html

  #### Parameters

  |----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*expirationDuration*` ` | Override the (default or optionally set `minimumFetchInterval` property in RemoteConfigSettings) `minimumFetchInterval` for only the current request, in seconds. Setting a value of 0 seconds will force a fetch to the backend. |
  | ` `*completionHandler*` `  | Fetch operation callback with status and error parameters.                                                                                                                                                                        |

- `
  ``
  ``
  `

  ### [fetchAndActivate()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)fetchAndActivateWithCompletionHandler:)

  `
  `  
  Fetches Remote Config data and if successful, activates fetched data. Optional completion
  handler callback is invoked after the attempted activation of data, if the fetch call succeeded.

  Note: This method uses a Firebase Installations token to identify the app instance, and once
  it's called, it periodically sends data to the Firebase backend. (see
  `Installations.authToken(completion:)`).
  To stop the periodic sync, call `Installations.delete(completion:)`
  and avoid calling this method again.  

  #### Declaration

  Swift  

      func fetchAndActivate() async throws -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchAndActivateStatus.html

  #### Parameters

  |---------------------------|------------------------------------------------------------|
  | ` `*completionHandler*` ` | Fetch operation callback with status and error parameters. |

[## Apply](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/Apply)

- `
  ``
  ``
  `

  ### [activate()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)activateWithCompletion:)

  `
  `  
  Applies Fetched Config data to the Active Config, causing updates to the behavior and appearance
  of the app to take effect (depending on how config data is used in the app).  

  #### Declaration

  Swift  

      func activate() async throws -> Bool

  #### Parameters

  |--------------------|----------------------------------------------------------------|
  | ` `*completion*` ` | Activate operation callback with changed and error parameters. |

[## Get Config](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/Get-Config)

- `
  ``
  ``
  `

  ### [subscript(_:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)objectForKeyedSubscript:)

  `
  `  
  Enables access to configuration values by using object subscripting syntax.
  For example:
  let config = RemoteConfig.remoteConfig()
  let value = config\["yourKey"\]
  let boolValue = value.boolValue
  let number = config\["yourKey"\].numberValue  

  #### Declaration

  Swift  

      subscript(key: String) -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue.html { get }

- `
  ``
  ``
  `

  ### [configValue(forKey:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)configValueForKey:)

  `
  `  
  Gets the config value.  

  #### Declaration

  Swift  

      func configValue(forKey key: String?) -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue.html

  #### Parameters

  |-------------|-------------|
  | ` `*key*` ` | Config key. |

- `
  ``
  ``
  `

  ### [configValue(forKey:source:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)configValueForKey:source:)

  `
  `  
  Gets the config value of a given source from the default namespace.  

  #### Declaration

  Swift  

      func configValue(forKey key: String?, source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource.html) -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue.html

  #### Parameters

  |----------------|----------------------|
  | ` `*key*` `    | Config key.          |
  | ` `*source*` ` | Config value source. |

- `
  ``
  ``
  `

  ### [allKeys(from:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)allKeysFromSource:)

  `
  `  
  Gets all the parameter keys of a given source from the default namespace.  

  #### Declaration

  Swift  

      func allKeys(from source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource.html) -> [String]

  #### Parameters

  |----------------|-------------------------|
  | ` `*source*` ` | The config data source. |

  #### Return Value

  An array of keys under the given source.
- `
  ``
  ``
  `

  ### [keys(withPrefix:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)keysWithPrefix:)

  `
  `  
  Returns the set of parameter keys that start with the given prefix, from the default namespace
  in the active config.  

  #### Declaration

  Swift  

      func keys(withPrefix prefix: String?) -> Set<String>

  #### Parameters

  |----------------|------------------------------------------------------------------------------|
  | ` `*prefix*` ` | The key prefix to look for. If prefix is nil or empty, returns all the keys. |

  #### Return Value

The set of parameter keys that start with the specified prefix.  
[## Defaults](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/Defaults)

- `
  ``
  ``
  `

  ### [setDefaults(_:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)setDefaults:)

  `
  `  
  Sets config defaults for parameter keys and values in the default namespace config.  

  #### Declaration

  Swift  

      func setDefaults(_ defaults: [String : NSObject]?)

  #### Parameters

  |------------------|----------------------------------------------------------------|
  | ` `*defaults*` ` | A dictionary mapping a NSString \* key to a NSObject \* value. |

- `
  ``
  ``
  `

  ### [setDefaults(fromPlist:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)setDefaultsFromPlistFileName:)

  `
  `  
  Sets default configs from plist for default namespace.  

  #### Declaration

  Swift  

      func setDefaults(fromPlist fileName: String?)

  #### Parameters

  |------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fileName*` ` | The plist file name, with no file name extension. For example, if the plist file is named `defaultSamples.plist`: `RemoteConfig.remoteConfig().setDefaults(fromPlist: "defaultSamples")` |

- `
  ``
  ``
  `

  ### [defaultValue(forKey:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)defaultValueForKey:)

  `
  `  
  Returns the default value of a given key from the default config.  

  #### Declaration

  Swift  

      func defaultValue(forKey key: String?) -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue.html?

  #### Parameters

  |-------------|--------------------------------------|
  | ` `*key*` ` | The parameter key of default config. |

  #### Return Value

  Returns the default value of the specified key. Returns
nil if the key doesn't exist in the default config.  
[## Real-time Config Updates](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/Real-time-Config-Updates)

- `
  ``
  ``
  `

  ### [addOnConfigUpdateListener(remoteConfigUpdateCompletion:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)addOnConfigUpdateListener:)

  `
  `  
  Start listening for real-time config updates from the Remote Config backend and automatically
  fetch updates when they're available.

  If a connection to the Remote Config backend is not already open, calling this method will
  open it. Multiple listeners can be added by calling this method again, but subsequent calls
  re-use the same connection to the backend.

  Note: Real-time Remote Config requires the Firebase Remote Config Realtime API. See Get started
  with Firebase Remote Config at <https://firebase.google.com/docs/remote-config/get-started> for
  more information.  

  #### Declaration

  Swift  

      func addOnConfigUpdateListener(remoteConfigUpdateCompletion listener: @escaping @Sendable (https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigUpdate.html?, (any Error)?) -> Void) -> https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration.html

  #### Parameters

  |------------------|-----------------------------------------------------------------|
  | ` `*listener*` ` | The configured listener that is called for every config update. |

  #### Return Value

  Returns a registration representing the listener. The registration contains
  a remove method, which can be used to stop receiving updates for the provided listener.
- `
  ``
  ``
  `

  ### [-setCustomSignals:withCompletion:](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/c:objc(cs)FIRRemoteConfig(im)setCustomSignals:withCompletion:)

  `
  `  
  Undocumented
- `
  ``
  ``
  `

  ### [decoded(asType:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB0E7decoded6asTypexxm_tKSeRzlF)

  `
  `  
  Decodes a struct from the respective Remote Config values.  

  #### Declaration

  Swift  

      func decoded<Value>(asType: Value.Type = Value.self) throws -> Value where Value : Decodable

  #### Parameters

  |----------------|------------------------|
  | ` `*asType*` ` | The type to decode to. |

- `
  ``
  ``
  `

  ### [setDefaults(from:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB0E11setDefaults4fromyx_tKSERzlF)

  `
  `  
  Sets config defaults from an encodable struct.  

  #### Declaration

  Swift  

      func setDefaults<Value>(from value: Value) throws where Value : Encodable

  #### Parameters

  |---------------|----------------------------------------|
  | ` `*value*` ` | The object to use to set the defaults. |

- `
  ``
  ``
  `

  ### [setCustomSignals(_:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB0E16setCustomSignalsyySDySSAC0F11SignalValueVSgGYaKF)

  `
  `  
  Sets custom signals for this Remote Config instance.

  When a new key is provided, a new key-value pair is added to the custom signals.
  If an existing key is provided with a new value, the corresponding signal is updated.
  If the value for a key is `nil`, the signal associated with that key is removed.  

  #### Declaration

  Swift  

      func setCustomSignals(_ customSignals: [String : https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue.html?]) async throws

  #### Parameters

  |-----------------------|------------------------------------------------------------------------------------|
  | ` `*customSignals*` ` | A dictionary mapping string keys to custom signals to be set for the app instance. |

- `
  ``
  ``
  `

  ### [subscript(decodedValue:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB0E12decodedValuexSgSS_tcSeRzluip)

  `
  `  
  Return a typed RemoteConfigValue for a key.  

  #### Declaration

  Swift  

      subscript<T>(decodedValue key: String) -> T? where T : Decodable { get }

  #### Parameters

  |-------------|----------------------|
  | ` `*key*` ` | A Remote Config key. |

  #### Return Value

  A typed RemoteConfigValue.
- `
  ``
  ``
  `

  ### [subscript(jsonValue:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig#/s:So15FIRRemoteConfigC014FirebaseRemoteB0E9jsonValueSDySSs11AnyHashableVGSgSS_tcip)

  `
  `  
  Return a Dictionary for a RemoteConfig JSON key.  

  #### Declaration

  Swift  

      subscript(jsonValue key: String) -> [String : AnyHashable]? { get }

  #### Parameters

  |-------------|----------------------|
  | ` `*key*` ` | A Remote Config key. |

  #### Return Value

  A Dictionary representing a RemoteConfig JSON value.