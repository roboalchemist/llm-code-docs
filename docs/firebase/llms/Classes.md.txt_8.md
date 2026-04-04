# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes.md.txt

# FirebaseRemoteConfig Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRConfigUpdateListenerRegistration)


  ` Listener registration returned by `addOnConfigUpdateListener`. Calling its method `remove` stops
  the associated listener from receiving config updates and unregisters itself.

  If remove is called and no other listener registrations remain, the connection to the real-time
  RC backend is closed. Subsequently calling `addOnConfigUpdateListener` will re-open the
  connection.

  #### Declaration

  Objective-C


      @interface FIRConfigUpdateListenerRegistration : NSObject

[## FIRRemoteConfigValue](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfigValue)

- `


  ### [FIRRemoteConfigValue](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigValue)


  ` This class provides a wrapper for Remote Config parameter values, with methods to get parameter
  values as different data types.

  #### Declaration

  Objective-C


      @interface FIRRemoteConfigValue : NSObject <NSCopying>

[## FIRRemoteConfigSettings](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfigSettings)

- `


  ### [FIRRemoteConfigSettings](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigSettings)


  ` Firebase Remote Config settings.

  #### Declaration

  Objective-C


      @interface FIRRemoteConfigSettings : NSObject

[## FIRRemoteConfigUpdate](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfigUpdate)

- `


  ### [FIRRemoteConfigUpdate](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigUpdate)


  ` Used by Remote Config real-time config update service, this class represents changes between the
  newly fetched config and the current one. An instance of this class is passed to
  `https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions#/c:FIRRemoteConfig.h@T@FIRRemoteConfigUpdateCompletion` when a new config version has been automatically fetched.

  #### Declaration

  Objective-C


      @interface FIRRemoteConfigUpdate : NSObject

[## FIRRemoteConfig](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes#/FIRRemoteConfig)

- `


  ### [FIRRemoteConfig](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfig)


  ` Firebase Remote Config class. The class method `remoteConfig()` can be used
  to fetch, activate and read config results and set default config results on the default
  Remote Config instance.

  #### Declaration

  Objective-C


      @interface FIRRemoteConfig : NSObject <NSFastEnumeration>