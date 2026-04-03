# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-debug-settings.md.txt

# firebase::ump::ConsentDebugSettings Struct Reference

# firebase::ump::ConsentDebugSettings


`#include <types.h>`

Debug settings for [ConsentInfo::RequestConsentInfoUpdate()](https://firebase.google.com/docs/reference/cpp/class/firebase/ump/consent-info#classfirebase_1_1ump_1_1_consent_info_1a38f38f22b70b35732c3cd63b18dd26d2).

## Summary

These let you force a specific geographic location. Be sure to include debug device IDs to enable this on hardware. Debug features are always enabled for simulators.

| ### Constructors and Destructors ||
|---|---|
| [ConsentDebugSettings](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-debug-settings#structfirebase_1_1ump_1_1_consent_debug_settings_1a8d8db19ba7b5b938cfdbac1add730c8c)`()` Create a default debug setting, with debugging disabled. ||

|                                                                                                                                                                                          ### Public attributes                                                                                                                                                                                          ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [debug_device_ids](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-debug-settings#structfirebase_1_1ump_1_1_consent_debug_settings_1aa5bbfbd54413b097490804d2efc833a2) | `std::vector< std::string >` A list of all device IDs that are allowed to use debug settings.                                                                                                        |
| [debug_geography](https://firebase.google.com/docs/reference/cpp/struct/firebase/ump/consent-debug-settings#structfirebase_1_1ump_1_1_consent_debug_settings_1a9654f654473af102491a0f9a07b92262)  | [ConsentDebugGeography](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump#namespacefirebase_1_1ump_1a31571b292445fe90e7dd4755f8ff93b6) The geographical location, for debugging. |

## Public attributes

### debug_device_ids

```c++
std::vector< std::string > firebase::ump::ConsentDebugSettings::debug_device_ids
```  
A list of all device IDs that are allowed to use debug settings.

You can obtain this from the device log after running with debug settings enabled.  

### debug_geography

```c++
ConsentDebugGeography firebase::ump::ConsentDebugSettings::debug_geography
```  
The geographical location, for debugging.

## Public functions

### ConsentDebugSettings

```c++
 firebase::ump::ConsentDebugSettings::ConsentDebugSettings()
```  
Create a default debug setting, with debugging disabled.