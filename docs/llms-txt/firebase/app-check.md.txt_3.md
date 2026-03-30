# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check.md.txt

# firebase::app_check Namespace

# firebase::app_check

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check#namespacefirebase_1_1app__check_1a33540279e7fe84f0d36f7d6a6d0b0197{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check#namespacefirebase_1_1app__check_1a33540279e7fe84f0d36f7d6a6d0b0197a260576b9cd49e253da346ab8cf69da5a = 0, https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check#namespacefirebase_1_1app__check_1a33540279e7fe84f0d36f7d6a6d0b0197a7a275866e89c6eeaa6704ac3947ef086 = 1, https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check#namespacefirebase_1_1app__check_1a33540279e7fe84f0d36f7d6a6d0b0197a3b8533d72b93900c6611dd383b7ddf03 = 2, https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check#namespacefirebase_1_1app__check_1a33540279e7fe84f0d36f7d6a6d0b0197afd496eb0b9b4360847acef5ab8f6c594 = 3, https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check#namespacefirebase_1_1app__check_1a33540279e7fe84f0d36f7d6a6d0b0197aad4b4e5e452adec7ef09764fb45e4e4a = 4, https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check#namespacefirebase_1_1app__check_1a33540279e7fe84f0d36f7d6a6d0b0197a8f4ba3da0adaa8727e80c8f07a5f0f2c = 5 }` | enumError code returned by [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) C++ functions. |

| ### Classes ||
|---|---|
| [firebase::app_check::AppAttestProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-attest-provider-factory) | Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory) that builds AppAttestProviders. |
| [firebase::app_check::AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check) | Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check object. |
| [firebase::app_check::AppCheckListener](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener) | Base class used to receive messages when [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) token changes. |
| [firebase::app_check::AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider) | Interface for a provider that generates [AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token)s. |
| [firebase::app_check::AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory) | Interface for a factory that generates [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider)s. |
| [firebase::app_check::DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory) | Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory) that builds DebugAppCheckProviders. |
| [firebase::app_check::DeviceCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/device-check-provider-factory) | Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory) that builds DeviceCheckProviders. |
| [firebase::app_check::PlayIntegrityProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/play-integrity-provider-factory) | Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory) that builds PlayIntegrityProviders. |

| ### Structs ||
|---|---|
| [firebase::app_check::AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token) | Struct to hold tokens emitted by the Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check service which are minted upon a successful application verification. |

## Enumerations

### AppCheckError

```c++
 AppCheckError
```
Error code returned by [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) C++ functions.

| Properties ||
|---|---|
| `kAppCheckErrorInvalidConfiguration` | Invalid configuration error. Currently, an exception is thrown but this error is reserved for future implementations of invalid configuration detection. |
| `kAppCheckErrorNone` | The operation was a success, no error occurred. |
| `kAppCheckErrorServerUnreachable` | A network connection error. |
| `kAppCheckErrorSystemKeychain` | System keychain access error. Ensure that the app has proper keychain access. |
| `kAppCheckErrorUnknown` | An unknown error occurred. |
| `kAppCheckErrorUnsupportedProvider` | Selected [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) provider is not supported on the current platform or OS version. |