# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token.md.txt

# firebase::auth::PhoneAuthProvider::ForceResendingToken Class Reference

# firebase::auth::PhoneAuthProvider::ForceResendingToken


`#include <credential.h>`

Token to maintain current phone number verification session.

## Summary

Acquired via [Listener::OnCodeSent](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a65f3a2abf007af3dfb1f8d2136bf4c29). Used in [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84).

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token_1a61f1b41b38216810c578d27a872711f2()` This token will be invalid until it is assigned a value sent via [Listener::OnCodeSent](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a65f3a2abf007af3dfb1f8d2136bf4c29). ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token_1a606f043ac861209567cbe3d7914ff1f0(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token & rhs)` Make `this` token refer to the same phone session as `rhs`. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token_1a9013ec95ee953739d66401f44209e1e2()` Releases internal resources when destructing. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token_1acd94496067277e4c48d331521a92483d(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token & rhs) const ` | `bool` Return true if `rhs` is refers to a different phone number session as `this`. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token_1ac992c50789820f5e93a695b3112b4374(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token & rhs)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token &` Make `this` token refer to the same phone session as `rhs`. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token_1a3ac0911a8f4df4972f827f88dce9135e(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token & rhs) const ` | `bool` Return true if `rhs` is refers to the same phone number session as `this`. |

## Public functions

### ForceResendingToken

```c++
 ForceResendingToken()
```
This token will be invalid until it is assigned a value sent via [Listener::OnCodeSent](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a65f3a2abf007af3dfb1f8d2136bf4c29).

It can still be passed into [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84), but it will be ignored.

### ForceResendingToken

```c++
 ForceResendingToken(
  const ForceResendingToken & rhs
)
```
Make `this` token refer to the same phone session as `rhs`.

### operator!=

```c++
bool operator!=(
  const ForceResendingToken & rhs
) const 
```
Return true if `rhs` is refers to a different phone number session as `this`.

### operator=

```c++
ForceResendingToken & operator=(
  const ForceResendingToken & rhs
)
```
Make `this` token refer to the same phone session as `rhs`.

### operator==

```c++
bool operator==(
  const ForceResendingToken & rhs
) const 
```
Return true if `rhs` is refers to the same phone number session as `this`.

### \~ForceResendingToken

```c++
 ~ForceResendingToken()
```
Releases internal resources when destructing.