# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/play-integrity-provider-factory.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/app-check/play-integrity-provider-factory.md.txt

# Firebase.AppCheck.PlayIntegrityProviderFactory Class Reference

# Firebase.AppCheck.PlayIntegrityProviderFactory

Implementation of an [IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory) that builds providering using the Play Integrity service.

## Summary

To be used when targeting the Android platform.

### Inheritance

Inherits from: [Firebase.AppCheck.IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory)

|                                                                                                                                                                                                                                                                                                                                    ### Properties                                                                                                                                                                                                                                                                                                                                    ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Instance](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/play-integrity-provider-factory#class_firebase_1_1_app_check_1_1_play_integrity_provider_factory_1ad26cad4c80441b227dd4fbe882c81b8c) | `static `[PlayIntegrityProviderFactory](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/play-integrity-provider-factory#class_firebase_1_1_app_check_1_1_play_integrity_provider_factory) Gets an instance of this class for installation into a [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) instance. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CreateProvider](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/play-integrity-provider-factory#class_firebase_1_1_app_check_1_1_play_integrity_provider_factory_1aeb8a25279810b214086f3978f6769e6c)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)` | [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) Gets the [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance, or creates one if none already exists. |

## Properties

### Instance

```c#
static PlayIntegrityProviderFactory Instance
```  
Gets an instance of this class for installation into a [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) instance.

## Public functions

### CreateProvider

```c#
IAppCheckProvider CreateProvider(
  FirebaseApp app
)
```  
Gets the [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance, or creates one if none already exists.