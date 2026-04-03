# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/app-check/debug-app-check-provider-factory.md.txt

# Firebase.AppCheck.DebugAppCheckProviderFactory Class Reference

# Firebase.AppCheck.DebugAppCheckProviderFactory

Implementation of an [IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory) that builds DebugAppCheckProviders.

## Summary

DebugAppCheckProvider can exchange a debug token registered in the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) console for a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check token. The debug provider is designed to enable testing applications on a simulator or test environment.

NOTE: Do not use the debug provider in applications used by real users.

### Inheritance

Inherits from: [Firebase.AppCheck.IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory)

|                                                                                                                                                                                                                                                                                                                                      ### Properties                                                                                                                                                                                                                                                                                                                                      ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Instance](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/debug-app-check-provider-factory#class_firebase_1_1_app_check_1_1_debug_app_check_provider_factory_1a75f262d05f1eaeba39f2c3fecc8eed65) | `static `[DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/debug-app-check-provider-factory#class_firebase_1_1_app_check_1_1_debug_app_check_provider_factory) Gets an instance of this class for installation into a [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) instance. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CreateProvider](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/debug-app-check-provider-factory#class_firebase_1_1_app_check_1_1_debug_app_check_provider_factory_1a4c9e012d058888a3be56e8f4ec11d9e3)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)` | [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) Gets the [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance, or creates one if none already exists. |
| [SetDebugToken](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/debug-app-check-provider-factory#class_firebase_1_1_app_check_1_1_debug_app_check_provider_factory_1a98ac9cca533911d3072db4ef775eca8d)`(string token)`                                                                                                                       | `void` Sets the Debug Token to use when communicating with the backend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Properties

### Instance

```c#
static DebugAppCheckProviderFactory Instance
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

### SetDebugToken

```c#
void SetDebugToken(
  string token
)
```  
Sets the Debug Token to use when communicating with the backend.

This should match a debug token set in the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) console for your App.