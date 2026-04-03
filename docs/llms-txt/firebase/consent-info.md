# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info.md.txt

# firebase::ump::ConsentInfo Class Reference

# firebase::ump::ConsentInfo


`#include <consent_info.h>`

Consent Information class for the User Messaging Platform SDK.

## Summary

The User Messaging Platform (UMP) SDK is Google's option to handle user privacy and consent in mobile apps.

This class contains all of the methods necessary for obtaining consent from the user.

| ### Constructors and Destructors ||
|---|---|
| [~ConsentInfo](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a7bf59445e683021fba71e4056b220e42)`()` Shut down the User Messaging Platform Consent SDK. ||

|                                                                                                                                                                                                                                                                                                                                                                                                                                       ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                        ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CanRequestAds](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ad3bef17d14769e2897ac144590e11c63)`()`                                                                                                                                                                                                           | `bool` Indicates whether the app has completed the necessary steps for gathering updated user consent.                                                                                                                                                                                                                                                                                                                                                                                                    |
| [GetConsentFormStatus](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a3774c6a2f5da1a4e784a4f066ee018e0)`()`                                                                                                                                                                                                    | [ConsentFormStatus](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump#namespacefirebase_1_1ump_1ae649338824dc5088b6534b51b33107dd) Consent form status.                                                                                                                                                                                                                                                                                                                               |
| [GetConsentStatus](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ae8f8910f6e27429d4a81fb8b486fde56)`()`                                                                                                                                                                                                        | [ConsentStatus](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump#namespacefirebase_1_1ump_1a6e109ceb2bcc5f23925ed2b97cda8a03) The user's consent status.                                                                                                                                                                                                                                                                                                                             |
| [GetPrivacyOptionsRequirementStatus](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a319e98b6dee0df64e31876c0de032e7e)`()`                                                                                                                                                                                      | [PrivacyOptionsRequirementStatus](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump#namespacefirebase_1_1ump_1a9306e65217f577d523b053354d26e479) Check whether the privacy options form needs to be displayed.                                                                                                                                                                                                                                                                        |
| [LoadAndShowConsentFormIfRequired](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a7e8661fd1c74ed047ee579fd74b07903)`(`[FormParent](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump#namespacefirebase_1_1ump_1aa0543ea7f5b1511b6ebf8cedd4b3bd44)` parent)`                                | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Loads a consent form and immediately presents it using the given FormParent, if ConsentStatus is kConsentStatusRequired.                                                                                                                                                                                                                                                                |
| [LoadAndShowConsentFormIfRequiredLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a7fa80f1e36c8ffc3176cf40fdfad77cd)`()`                                                                                                                                                                              | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [LoadAndShowConsentFormIfRequired()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a7e8661fd1c74ed047ee579fd74b07903).                                             |
| [LoadConsentForm](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1aa20ce33d2e4e8fe5f1c5fe390dce5b5f)`()`                                                                                                                                                                                                         | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Loads a consent form.                                                                                                                                                                                                                                                                                                                                                                   |
| [LoadConsentFormLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a244f1fc0f2730cb37b74939f98031c6e)`()`                                                                                                                                                                                               | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [LoadConsentForm()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1aa20ce33d2e4e8fe5f1c5fe390dce5b5f).                                                              |
| [RequestConsentInfoUpdate](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2)`(const `[ConsentRequestParameters](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-request-parameters#structfirebase_1_1ump_1_1_consent_request_parameters)` & params)` | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Requests consent information update.                                                                                                                                                                                                                                                                                                                                                    |
| [RequestConsentInfoUpdateLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a60953bd0246a112e3f69a60eb789afdb)`()`                                                                                                                                                                                      | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2).                                                     |
| [Reset](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a63447dfb9110e2cf4df0bfa9b3f8365d)`()`                                                                                                                                                                                                                   | `void` Clears all consent state from persistent storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [ShowConsentForm](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a66259b326dfcda9035bffec424d8908d)`(`[FormParent](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump#namespacefirebase_1_1ump_1aa0543ea7f5b1511b6ebf8cedd4b3bd44)` parent)`                                                 | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Presents the full screen consent form using the given FormParent, which is defined as an Activity on Android and a UIViewController on iOS.                                                                                                                                                                                                                                             |
| [ShowConsentFormLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a44a7b187f5c0719b369c731681da4e13)`()`                                                                                                                                                                                               | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [ShowConsentForm()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a66259b326dfcda9035bffec424d8908d).                                                              |
| [ShowPrivacyOptionsForm](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a56684b2b823cef513297084a440dd363)`(`[FormParent](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump#namespacefirebase_1_1ump_1aa0543ea7f5b1511b6ebf8cedd4b3bd44)` parent)`                                          | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` If [GetPrivacyOptionsRequirementStatus()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a319e98b6dee0df64e31876c0de032e7e) is kPrivacyOptionsRequirementStatusRequired, presents a privacy options form from the provided FormParent, which is defined as an Activity on Android and a UIViewController on iOS. |
| [ShowPrivacyOptionsFormLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ada0d27fdf95458385b745720b740b7d1)`()`                                                                                                                                                                                        | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [ShowPrivacyOptionsForm()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a56684b2b823cef513297084a440dd363).                                                       |

|                                                                                                                                                                                                                                                                                                                              ### Public static functions                                                                                                                                                                                                                                                                                                                               ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetInstance](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ade91da575ad67f322256d12ddb0699ac)`(const ::`[firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` & app, `[InitResult](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478)` *init_result_out)` | [ConsentInfo](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info)` *` Initializes the User Messaging Platform Consent SDK.                              |
| [GetInstance](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a2f4300106379890615e1a769ea809c22)`(JNIEnv *jni_env, jobject activity, `[InitResult](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478)` *init_result_out)`                                                                                        | [ConsentInfo](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info)` *` Initializes the User Messaging Platform Consent SDK without Firebase for Android. |
| [GetInstance](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a40b77d2cc67ed25d012bc48753ac807e)`(`[InitResult](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478)` *init_result_out)`                                                                                                                           | [ConsentInfo](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info)` *` Initializes User Messaging Platform for iOS without Firebase.                     |

## Public functions

### CanRequestAds

```c++
bool CanRequestAds()
```  
Indicates whether the app has completed the necessary steps for gathering updated user consent.

Returns true if [RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2) has been called and GetConsentStatus returns either kConsentStatusNotRequired or kConsentStatusObtained.  

### GetConsentFormStatus

```c++
ConsentFormStatus GetConsentFormStatus()
```  
Consent form status.

This value defaults to kConsentFormStatusUnknown and requires a call to [RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2) to update.  

### GetConsentStatus

```c++
ConsentStatus GetConsentStatus()
```  
The user's consent status.

This value defaults to kConsentStatusUnknown until [RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2) is called, and defaults to the previous session's value until [RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2) completes.  

### GetPrivacyOptionsRequirementStatus

```c++
PrivacyOptionsRequirementStatus GetPrivacyOptionsRequirementStatus()
```  
Check whether the privacy options form needs to be displayed.

This is updated by [RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2).  

### LoadAndShowConsentFormIfRequired

```c++
Future< void > LoadAndShowConsentFormIfRequired(
  FormParent parent
)
```  
Loads a consent form and immediately presents it using the given FormParent, if ConsentStatus is kConsentStatusRequired.

The FormParent is defined as an Activity on Android and a UIViewController on iOS. The [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) will be completed successfully after the user selects an option (and the form is dismissed), or if the form is not required. The [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) will be completed with an error if the form fails to load or show.

[GetConsentStatus()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ae8f8910f6e27429d4a81fb8b486fde56) and [CanRequestAds()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ad3bef17d14769e2897ac144590e11c63) will be updated prior to the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) being completed.

<br />

|                                                                                                             Details                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------|--------------------------------------------------------------------------------------------| | `parent` | A FormParent, which is an Activity object on Android and a UIViewController object on iOS. | |

### LoadAndShowConsentFormIfRequiredLastResult

```c++
Future< void > LoadAndShowConsentFormIfRequiredLastResult()
```  
Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [LoadAndShowConsentFormIfRequired()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a7e8661fd1c74ed047ee579fd74b07903).  

### LoadConsentForm

```c++
Future< void > LoadConsentForm()
```  
Loads a consent form.

Returns an error if the consent form is unavailable or cannot be loaded.  

### LoadConsentFormLastResult

```c++
Future< void > LoadConsentFormLastResult()
```  
Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [LoadConsentForm()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1aa20ce33d2e4e8fe5f1c5fe390dce5b5f).  

### RequestConsentInfoUpdate

```c++
Future< void > RequestConsentInfoUpdate(
  const ConsentRequestParameters & params
)
```  
Requests consent information update.

Must be called in every app session before checking the user's consent status or loading a consent form. After calling this method, [GetConsentStatus()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ae8f8910f6e27429d4a81fb8b486fde56) and [CanRequestAds()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ad3bef17d14769e2897ac144590e11c63) will be updated immediately to hold the consent state from the previous app session, if one exists. [GetConsentStatus()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ae8f8910f6e27429d4a81fb8b486fde56) and [CanRequestAds()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ad3bef17d14769e2897ac144590e11c63) may be updated again immediately before the returned future is completed.  

### RequestConsentInfoUpdateLastResult

```c++
Future< void > RequestConsentInfoUpdateLastResult()
```  
Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2).  

### Reset

```c++
void Reset()
```  
Clears all consent state from persistent storage.

This can be used in development to simulate a new installation.  

### ShowConsentForm

```c++
Future< void > ShowConsentForm(
  FormParent parent
)
```  
Presents the full screen consent form using the given FormParent, which is defined as an Activity on Android and a UIViewController on iOS.

The form will be dismissed and the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) will be completed after the user selects an option.

[GetConsentStatus()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ae8f8910f6e27429d4a81fb8b486fde56) and [CanRequestAds()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ad3bef17d14769e2897ac144590e11c63) are updated when the returned [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed.


| **Note:** You must call [LoadConsentForm()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1aa20ce33d2e4e8fe5f1c5fe390dce5b5f) and wait for it to complete before calling this method.

<br />

|                                                                                                             Details                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------|--------------------------------------------------------------------------------------------| | `parent` | A FormParent, which is an Activity object on Android and a UIViewController object on iOS. | |

### ShowConsentFormLastResult

```c++
Future< void > ShowConsentFormLastResult()
```  
Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [ShowConsentForm()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a66259b326dfcda9035bffec424d8908d).  

### ShowPrivacyOptionsForm

```c++
Future< void > ShowPrivacyOptionsForm(
  FormParent parent
)
```  
If [GetPrivacyOptionsRequirementStatus()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a319e98b6dee0df64e31876c0de032e7e) is kPrivacyOptionsRequirementStatusRequired, presents a privacy options form from the provided FormParent, which is defined as an Activity on Android and a UIViewController on iOS.

This method should only be called in response to a user input to request a privacy options form to be shown.

The future completes when the user selects an option and dismisses the form or is completed immediately with an error code if no form is presented. The privacy options form is preloaded by the SDK automatically when a form becomes available. If no form has been preloaded, the SDK will try to load one asynchronously.

<br />

|                                                                                                             Details                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------|--------------------------------------------------------------------------------------------| | `parent` | A FormParent, which is an Activity object on Android and a UIViewController object on iOS. | |

### ShowPrivacyOptionsFormLastResult

```c++
Future< void > ShowPrivacyOptionsFormLastResult()
```  
Get the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from the most recent call to [ShowPrivacyOptionsForm()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a56684b2b823cef513297084a440dd363).  

### \~ConsentInfo

```c++
 ~ConsentInfo()
```  
Shut down the User Messaging Platform Consent SDK.

## Public static functions

### GetInstance

```c++
ConsentInfo * GetInstance(
  const ::firebase::App & app,
  InitResult *init_result_out
)
```  
Initializes the User Messaging Platform Consent SDK.

<br />

|                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                               ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app`             | Any Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance.                                                                                | | `init_result_out` | Optional: If provided, write the basic init result here. kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if there are Android dependencies missing. | |
| **Returns** | A pointer to the [ConsentInfo](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info) instance if UMP was successfully initialized, nullptr otherwise. Each call to [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ade91da575ad67f322256d12ddb0699ac) will return the same pointer; when you are finished using the SDK, you can delete the pointer and the UMP SDK will shut down.                                                                                                                                              |

### GetInstance

```c++
ConsentInfo * GetInstance(
  JNIEnv *jni_env,
  jobject activity,
  InitResult *init_result_out
)
```  
Initializes the User Messaging Platform Consent SDK without Firebase for Android.

The arguments to [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ade91da575ad67f322256d12ddb0699ac) are platform-specific so the caller must do something like this:  

```c++
#if defined(__ANDROID__)
consent_info = firebase::ump::ConsentInfo::GetInstance(jni_env,
activity);
#else
consent_info = firebase::ump::GetInstance();
#endif
```

<br />

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `jni_env`         | JNIEnv pointer.                                                                                                                                                                                      | | `activity`        | Activity used to start the application.                                                                                                                                                              | | `init_result_out` | Optional: If provided, write the basic init result here. kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if there are Android dependencies missing. | |
| **Returns** | A pointer to the [ConsentInfo](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info) instance if UMP was successfully initialized, nullptr otherwise. Each call to [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ade91da575ad67f322256d12ddb0699ac) will return the same pointer; when you are finished using the SDK, you can delete the pointer and the UMP SDK will shut down.                                                                                                                                                                                                                                                                                                                                                                           |

### GetInstance

```c++
ConsentInfo * GetInstance(
  InitResult *init_result_out
)
```  
Initializes User Messaging Platform for iOS without Firebase.


| **Note:** Once any overload of [ConsentInfo::GetInstance](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ade91da575ad67f322256d12ddb0699ac) has been called, you can use this method to obtain the same instance again.

<br />

|                                                                                                                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                                                                                                                   ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `init_result_out` | Optional: If provided, write the basic init result here. kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency if a dependency is missing. On iOS, this will always return kInitResultSuccess, as missing dependencies would have caused a linker error at build time. | |
| **Returns** | A pointer to the [ConsentInfo](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info) instance. Each call to [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1ade91da575ad67f322256d12ddb0699ac) will return the same pointer; when you are finished using the SDK, you can delete the pointer, and the UMP SDK will shut down.                                                                                                                                                                           |