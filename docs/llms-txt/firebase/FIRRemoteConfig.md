# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfig


    @interface FIRRemoteConfig : NSObject <NSFastEnumeration>

Firebase Remote Config class. The class method `remoteConfig()` can be used
to fetch, activate and read config results and set default config results on the default
Remote Config instance.
- `
  ``
  ``
  `

  ### [lastFetchTime](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(py)lastFetchTime)

  `
  `  
  Last successful fetch completion time.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly, nullable) NSDate *lastFetchTime;

- `
  ``
  ``
  `

  ### [lastFetchStatus](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(py)lastFetchStatus)

  `
  `  
  Last fetch status. The status can be any enumerated value from `RemoteConfigFetchStatus`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchStatus.html lastFetchStatus;

- `
  ``
  ``
  `

  ### [configSettings](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(py)configSettings)

  `
  `  
  Config settings are custom settings.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, nonnull) https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigSettings.html *configSettings;

- `
  ``
  ``
  `

  ### [+remoteConfig](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(cm)remoteConfig)

  `
  `  
  Returns the `RemoteConfig` instance configured for the default Firebase app. This singleton
  object contains the complete set of Remote Config parameter values available to the app,
  including the Active Config and Default Config. This object also caches values fetched from the
  Remote Config server until they are copied to the Active Config by calling `activate()`. When
  you fetch values from the Remote Config server using the default Firebase app, you should use
  this class method to create and reuse a shared instance of `RemoteConfig`.  

  #### Declaration

  Objective-C  

      + (nonnull FIRRemoteConfig *)remoteConfig;

- `
  ``
  ``
  `

  ### [+remoteConfigWithApp:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(cm)remoteConfigWithApp:)

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

  Objective-C  

      + (nonnull FIRRemoteConfig *)remoteConfigWithApp:(nonnull FIRApp *)app;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)init)

  `
  `  
  Unavailable

  Use +remoteConfig instead.  
  Unavailable. Use +remoteConfig instead.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-ensureInitializedWithCompletionHandler:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)ensureInitializedWithCompletionHandler:)

  `
  `  
  Ensures initialization is complete and clients can begin querying for Remote Config values.  

  #### Declaration

  Objective-C  

      - (void)ensureInitializedWithCompletionHandler:
          (void (^_Nonnull)(NSError *_Nullable))completionHandler;

  #### Parameters

  |---------------------------|--------------------------------------------------------|
  | ` `*completionHandler*` ` | Initialization complete callback with error parameter. |

[## Fetch](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/Fetch)

- `
  ``
  ``
  `

  ### [-fetchWithCompletionHandler:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)fetchWithCompletionHandler:)

  `
  `  
  Fetches Remote Config data with a callback. Call `activate()` to make fetched data
  available to your app.

  Note: This method uses a Firebase Installations token to identify the app instance, and once
  it's called, it periodically sends data to the Firebase backend. (see
  `Installations.authToken(completion:)`).
  To stop the periodic sync, call `Installations.delete(completion:)`
  and avoid calling this method again.  

  #### Declaration

  Objective-C  

      - (void)fetchWithCompletionHandler:
          (void (^_Nullable)(https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchStatus.html,
                             NSError *_Nullable))completionHandler;

  #### Parameters

  |---------------------------|------------------------------------------------------------|
  | ` `*completionHandler*` ` | Fetch operation callback with status and error parameters. |

- `
  ``
  ``
  `

  ### [-fetchWithExpirationDuration:completionHandler:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)fetchWithExpirationDuration:completionHandler:)

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

  Objective-C  

      - (void)fetchWithExpirationDuration:(NSTimeInterval)expirationDuration
                        completionHandler:
                            (void (^_Nullable)(https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchStatus.html,
                                               NSError *_Nullable))completionHandler;

  #### Parameters

  |----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*expirationDuration*` ` | Override the (default or optionally set `minimumFetchInterval` property in RemoteConfigSettings) `minimumFetchInterval` for only the current request, in seconds. Setting a value of 0 seconds will force a fetch to the backend. |
  | ` `*completionHandler*` `  | Fetch operation callback with status and error parameters.                                                                                                                                                                        |

- `
  ``
  ``
  `

  ### [-fetchAndActivateWithCompletionHandler:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)fetchAndActivateWithCompletionHandler:)

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

  Objective-C  

      - (void)fetchAndActivateWithCompletionHandler:
          (void (^_Nullable)(https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchAndActivateStatus.html,
                             NSError *_Nullable))completionHandler;

  #### Parameters

  |---------------------------|------------------------------------------------------------|
  | ` `*completionHandler*` ` | Fetch operation callback with status and error parameters. |

[## Apply](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/Apply)

- `
  ``
  ``
  `

  ### [-activateWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)activateWithCompletion:)

  `
  `  
  Applies Fetched Config data to the Active Config, causing updates to the behavior and appearance
  of the app to take effect (depending on how config data is used in the app).  

  #### Declaration

  Objective-C  

      - (void)activateWithCompletion:
          (void (^_Nullable)(BOOL, NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------------------------------------|
  | ` `*completion*` ` | Activate operation callback with changed and error parameters. |

[## Get Config](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/Get-Config)

- `
  ``
  ``
  `

  ### [-objectForKeyedSubscript:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)objectForKeyedSubscript:)

  `
  `  
  Enables access to configuration values by using object subscripting syntax.
  For example:
  let config = RemoteConfig.remoteConfig()
  let value = config\["yourKey"\]
  let boolValue = value.boolValue
  let number = config\["yourKey"\].numberValue  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue.html *)objectForKeyedSubscript:
          (nonnull NSString *)key;

- `
  ``
  ``
  `

  ### [-configValueForKey:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)configValueForKey:)

  `
  `  
  Gets the config value.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue.html *)configValueForKey:(nullable NSString *)key;

  #### Parameters

  |-------------|-------------|
  | ` `*key*` ` | Config key. |

- `
  ``
  ``
  `

  ### [-configValueForKey:source:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)configValueForKey:source:)

  `
  `  
  Gets the config value of a given source from the default namespace.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue.html *)configValueForKey:(nullable NSString *)key
                                                   source:
                                                       (https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource.html)source;

  #### Parameters

  |----------------|----------------------|
  | ` `*key*` `    | Config key.          |
  | ` `*source*` ` | Config value source. |

- `
  ``
  ``
  `

  ### [-allKeysFromSource:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)allKeysFromSource:)

  `
  `  
  Gets all the parameter keys of a given source from the default namespace.  

  #### Declaration

  Objective-C  

      - (nonnull NSArray<NSString *> *)allKeysFromSource:
          (https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource.html)source;

  #### Parameters

  |----------------|-------------------------|
  | ` `*source*` ` | The config data source. |

  #### Return Value

  An array of keys under the given source.
- `
  ``
  ``
  `

  ### [-keysWithPrefix:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)keysWithPrefix:)

  `
  `  
  Returns the set of parameter keys that start with the given prefix, from the default namespace
  in the active config.  

  #### Declaration

  Objective-C  

      - (nonnull NSSet<NSString *> *)keysWithPrefix:(nullable NSString *)prefix;

  #### Parameters

  |----------------|------------------------------------------------------------------------------|
  | ` `*prefix*` ` | The key prefix to look for. If prefix is nil or empty, returns all the keys. |

  #### Return Value

The set of parameter keys that start with the specified prefix.  
[## Defaults](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/Defaults)

- `
  ``
  ``
  `

  ### [-setDefaults:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)setDefaults:)

  `
  `  
  Sets config defaults for parameter keys and values in the default namespace config.  

  #### Declaration

  Objective-C  

      - (void)setDefaults:(nullable NSDictionary<NSString *, NSObject *> *)defaults;

  #### Parameters

  |------------------|----------------------------------------------------------------|
  | ` `*defaults*` ` | A dictionary mapping a NSString \* key to a NSObject \* value. |

- `
  ``
  ``
  `

  ### [-setDefaultsFromPlistFileName:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)setDefaultsFromPlistFileName:)

  `
  `  
  Sets default configs from plist for default namespace.  

  #### Declaration

  Objective-C  

      - (void)setDefaultsFromPlistFileName:(nullable NSString *)fileName;

  #### Parameters

  |------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fileName*` ` | The plist file name, with no file name extension. For example, if the plist file is named `defaultSamples.plist`: `RemoteConfig.remoteConfig().setDefaults(fromPlist: "defaultSamples")` |

- `
  ``
  ``
  `

  ### [-defaultValueForKey:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)defaultValueForKey:)

  `
  `  
  Returns the default value of a given key from the default config.  

  #### Declaration

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue.html *)defaultValueForKey:(nullable NSString *)key;

  #### Parameters

  |-------------|--------------------------------------|
  | ` `*key*` ` | The parameter key of default config. |

  #### Return Value

  Returns the default value of the specified key. Returns
nil if the key doesn't exist in the default config.  
[## Real-time Config Updates](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/Real-time-Config-Updates)

- `
  ``
  ``
  `

  ### [-addOnConfigUpdateListener:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)addOnConfigUpdateListener:)

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

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRConfigUpdateListenerRegistration.html *_Nonnull)addOnConfigUpdateListener:
          (https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions.html#/c:FIRRemoteConfig.h@T@FIRRemoteConfigUpdateCompletion _Nonnull)listener;

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

  ### [-setCustomSignals:withCompletion:](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig#/c:objc(cs)FIRRemoteConfig(im)setCustomSignals:withCompletion:)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (void)setCustomSignals:(nonnull NSDictionary<NSString *, NSObject *> *)customSignals
                withCompletion:(void (^_Nullable)(NSError *_Nullable error))completionHandler
          NS_REFINED_FOR_SWIFT;