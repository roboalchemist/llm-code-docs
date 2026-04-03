# Source: https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory.md.txt

# Firebase.AppCheck.IAppCheckProviderFactory Interface Reference

# Firebase.AppCheck.IAppCheckProviderFactory

Interface for a factory that generates AppCheckProviders.

## Summary

### Inheritance

Direct Known Subclasses:[Firebase.AppCheck.AppAttestProviderFactory](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/app-attest-provider-factory), [Firebase.AppCheck.DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/debug-app-check-provider-factory), [Firebase.AppCheck.DeviceCheckProviderFactory](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/device-check-provider-factory), [Firebase.AppCheck.PlayIntegrityProviderFactory](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/play-integrity-provider-factory)

|                                                                                                                                                                                                                                                                                                                                                                                                                 ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CreateProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory_1a6738ecfb0cec25e239de95865335e57c)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)` | [IAppCheckProvider](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider) Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/unity/other/) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance, or creates one if none already exists. |

## Public functions

### CreateProvider

```c#
IAppCheckProvider CreateProvider(
  FirebaseApp app
)
```  
Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/unity/other/) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance, or creates one if none already exists.