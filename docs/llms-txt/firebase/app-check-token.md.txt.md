# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token.md.txt

# firebase::app_check::AppCheckToken Struct Reference

# firebase::app_check::AppCheckToken


`#include <app_check.h>`

Struct to hold tokens emitted by the Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check service which are minted upon a successful application verification.

## Summary

These tokens are the federated output of a verification flow, the structure of which is independent of the mechanism by which the application was verified.

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token_1af4972408826c651f23fdd56bc631e789` | `int64_t` The time at which the token will expire in milliseconds since epoch. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token_1ac4ee2756ace2d1839b0fec62c073666a` | `std::string` A Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check token. |

## Public attributes

### expire_time_millis

```c++
int64_t firebase::app_check::AppCheckToken::expire_time_millis
```
The time at which the token will expire in milliseconds since epoch.

### token

```c++
std::string firebase::app_check::AppCheckToken::token
```
A Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check token.