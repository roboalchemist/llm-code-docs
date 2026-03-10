# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options.md.txt

# firebase::auth::PhoneAuthOptions Struct Reference

# firebase::auth::PhoneAuthOptions


`#include <credential.h>`

Options object for configuring phone validation flows in [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider).

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options#structfirebase_1_1auth_1_1_phone_auth_options_1af277d014a85917b83323ba594bbed504()` ||

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options#structfirebase_1_1auth_1_1_phone_auth_options_1aec4aaf0d4994672709037da53a7b680b` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token *` Sets the [PhoneAuthProvider::ForceResendingToken](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token) to force another verification SMS to be sent before the auto-retrieval timeout. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options#structfirebase_1_1auth_1_1_phone_auth_options_1acad93564b1b7392e0e8f543deb978311` | `std::string` The phone number for sign-in, sign-up, or second factor enrollment. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options#structfirebase_1_1auth_1_1_phone_auth_options_1a2e58febe0988c8ec04d86a7d1308148e` | `uint32_t` The maximum amount of time you're willing to wait for SMS auto-retrieval to be completed by the SDK. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options#structfirebase_1_1auth_1_1_phone_auth_options_1a6917ed9bb2cddbcd78dfce1d83c36e73` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase/auth#namespacefirebase_1_1auth_1a9b38b42e47035c229760f293282a5664` Sets the context to which the callbacks are scoped, and with which app verification will be completed. |

## Public attributes

### force_resending_token

```c++
PhoneAuthProvider::ForceResendingToken * firebase::auth::PhoneAuthOptions::force_resending_token
```
Sets the [PhoneAuthProvider::ForceResendingToken](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token) to force another verification SMS to be sent before the auto-retrieval timeout.

If nullptr, assume this is a new phone number to verify. If not-NULL, bypass the verification session deduping and force resending a new SMS. This token is received in [PhoneAuthProvider::Listener::OnCodeSent](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a65f3a2abf007af3dfb1f8d2136bf4c29). This should only be used when the user presses a Resend SMS button.

### phone_number

```c++
std::string firebase::auth::PhoneAuthOptions::phone_number
```
The phone number for sign-in, sign-up, or second factor enrollment.

### timeout_milliseconds

```c++
uint32_t firebase::auth::PhoneAuthOptions::timeout_milliseconds
```
The maximum amount of time you're willing to wait for SMS auto-retrieval to be completed by the SDK.

This value is supported on Android devices only.

The minimum timeout is 30 seconds, and the maximum timeout is 2 minutes. If you specified a positive value less than 30 seconds, the SDK will default to 30 seconds. Specifying a timeout that is greater than 120 seconds will result in an IllegalArgumentException being thrown.

Use 0 to disable SMS-auto-retrieval. This will also cause [PhoneAuthProvider::Listener::OnCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a3ea7ebac04e74de3ff76996ce4090193) to be called immediately.

### ui_parent

```c++
UIParent firebase::auth::PhoneAuthOptions::ui_parent
```
Sets the context to which the callbacks are scoped, and with which app verification will be completed.

On Android, the context should be a jobject referencing an Android Activity. On Apple platforms, this should be a pointer to UIView. For any other platforms, the context is ignored.

If ui_parent isn't defined (ie: nullptr or nil) then the FirebaseApp's default Activity or UIView will be used.

## Public functions

### PhoneAuthOptions

```c++
 firebase::auth::PhoneAuthOptions::PhoneAuthOptions()
```