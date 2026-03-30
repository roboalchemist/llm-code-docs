# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes.md.txt

# FirebaseRemoteConfig Framework Reference

# Classes

The following classes are available globally.
[## FIRRemoteConfigValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfigValue)

- `


  ### [RemoteConfigValue](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigValue)


  ` This class provides a wrapper for Remote Config parameter values, with methods to get parameter
  values as different data types.

  #### Declaration

  Swift

      class RemoteConfigValue : NSObject, NSCopying

[## FIRRemoteConfig](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfig)

- `


  ### [RemoteConfig](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfig)


  ` Firebase Remote Config class. The class method `remoteConfig()` can be used
  to fetch, activate and read config results and set default config results on the default
  Remote Config instance.

  #### Declaration

  Swift

      class RemoteConfig : NSObject, NSFastEnumeration

- `


  ### [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration)


  ` Listener registration returned by `addOnConfigUpdateListener`. Calling its method `remove` stops
  the associated listener from receiving config updates and unregisters itself.

  If remove is called and no other listener registrations remain, the connection to the real-time
  RC backend is closed. Subsequently calling `addOnConfigUpdateListener` will re-open the
  connection.

  #### Declaration

  Swift

      class ConfigUpdateListenerRegistration : NSObject, @unchecked Sendable

[## FIRRemoteConfigSettings](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfigSettings)

- `


  ### [RemoteConfigSettings](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigSettings)


  ` Firebase Remote Config settings.

  #### Declaration

  Swift

      class RemoteConfigSettings : NSObject

[## FIRRemoteConfigUpdate](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfigUpdate)

- `


  ### [RemoteConfigUpdate](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/RemoteConfigUpdate)


  ` Used by Remote Config real-time config update service, this class represents changes between the
  newly fetched config and the current one. An instance of this class is passed to
  `https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Type-Definitions#/c:FIRRemoteConfig.h@T@FIRRemoteConfigUpdateCompletion` when a new config version has been automatically fetched.

  #### Declaration

  Swift

      class RemoteConfigUpdate : NSObject