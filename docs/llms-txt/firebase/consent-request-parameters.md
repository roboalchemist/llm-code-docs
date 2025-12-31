# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-request-parameters.md.txt

# firebase::ump::ConsentRequestParameters Struct Reference

# firebase::ump::ConsentRequestParameters


`#include <types.h>`

Parameters for the [ConsentInfo::RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2) operation.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [ConsentRequestParameters](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-request-parameters#structfirebase_1_1ump_1_1_consent_request_parameters_1a7982ae1b5c9a778ee8db467c6c8135db)`()` ||

|                                                                                                                                                                                                       ### Public attributes                                                                                                                                                                                                       ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [debug_settings](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-request-parameters#structfirebase_1_1ump_1_1_consent_request_parameters_1a32806732350dc720de7769d20cd755cf)               | [ConsentDebugSettings](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-debug-settings#structfirebase_1_1ump_1_1_consent_debug_settings) Debug settings for the consent request. |
| [tag_for_under_age_of_consent](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-request-parameters#structfirebase_1_1ump_1_1_consent_request_parameters_1a40ac5e8eda2ceaca3be1fdcb7994ce57) | `bool` Whether the user is under the age of consent.                                                                                                                                                       |

## Public attributes

### debug_settings

```c++
ConsentDebugSettings firebase::ump::ConsentRequestParameters::debug_settings
```  
Debug settings for the consent request.  

### tag_for_under_age_of_consent

```c++
bool firebase::ump::ConsentRequestParameters::tag_for_under_age_of_consent
```  
Whether the user is under the age of consent.

## Public functions

### ConsentRequestParameters

```c++
 firebase::ump::ConsentRequestParameters::ConsentRequestParameters()
```