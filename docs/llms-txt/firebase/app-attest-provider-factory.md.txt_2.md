# Source: https://firebase.google.com/docs/reference/unity/class/firebase/app-check/app-attest-provider-factory.md.txt

# Firebase.AppCheck.AppAttestProviderFactory Class Reference

# Firebase.AppCheck.AppAttestProviderFactory

Implementation of an [IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory) that builds providering using the App Attest service.

## Summary

To be used when targeting the iOS platform.

### Inheritance

Inherits from: [Firebase.AppCheck.IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory)

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/app-attest-provider-factory#class_firebase_1_1_app_check_1_1_app_attest_provider_factory_1ad386274b1bc89b4db3444b7995023d79` | `static https://firebase.google.com/docs/reference/unity/class/firebase/app-check/app-attest-provider-factory#class_firebase_1_1_app_check_1_1_app_attest_provider_factory` Gets an instance of this class for installation into a [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) instance. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/app-attest-provider-factory#class_firebase_1_1_app_check_1_1_app_attest_provider_factory_1a16ca522ce754d33ad80843f8c2bf4e92(https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app app)` | `https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider` Gets the [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance, or creates one if none already exists. |

## Properties

### Instance

```c#
static AppAttestProviderFactory Instance
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