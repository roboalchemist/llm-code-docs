# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/device-check-provider-factory.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/app-check/device-check-provider-factory.md.txt

# Firebase.AppCheck.DeviceCheckProviderFactory Class Reference

# Firebase.AppCheck.DeviceCheckProviderFactory

Implementation of an [IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory) that builds providering using the Device Check service.

## Summary

To be used when targeting the iOS platform.

### Inheritance

Inherits from: [Firebase.AppCheck.IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory)

|                                                                                                                                                                                                                                                                                                                               ### Properties                                                                                                                                                                                                                                                                                                                               ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Instance](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/device-check-provider-factory#class_firebase_1_1_app_check_1_1_device_check_provider_factory_1abab2b5509c0cedd2ef341bd557edd59d) | `static `[DeviceCheckProviderFactory](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/device-check-provider-factory#class_firebase_1_1_app_check_1_1_device_check_provider_factory) Gets an instance of this class for installation into a [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) instance. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CreateProvider](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/device-check-provider-factory#class_firebase_1_1_app_check_1_1_device_check_provider_factory_1a230364e15c5e107ad25b11cc6bb19e92)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)` | [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) Gets the [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance, or creates one if none already exists. |

## Properties

### Instance

```c#
static DeviceCheckProviderFactory Instance
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