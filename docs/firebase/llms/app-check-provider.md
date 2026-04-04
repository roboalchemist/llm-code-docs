# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider.md.txt

# firebase::app_check::AppCheckProvider Class Reference

# firebase::app_check::AppCheckProvider


**This is an abstract class.**


`#include <app_check.h>`

Interface for a provider that generates [AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token)s.

## Summary

This provider can be called at any time by any Firebase library that depends (optionally or otherwise) on [AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token)s. This provider is responsible for determining if it can create a new token at the time of the call and returning that new token if it can.

| ### Constructors and Destructors ||
|---|---|
| [~AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider_1a88ddf70313c8de8fa8b137a3593504bc)`()` ||

|                                                                                                                                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                                                                                                                                     ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetToken](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider_1a1bfe8c92a50c664c35063f14c31a5647)`(std::function< void(`[AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token)`, int, const std::string &)> completion_callback)=0` | `virtual void` Fetches an [AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token) and then calls the provided callback method with the token or with an error code and error message. |

## Public functions

### GetToken

```c++
virtual void GetToken(
  std::function< void(AppCheckToken, int, const std::string &)> completion_callback
)=0
```  
Fetches an [AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token) and then calls the provided callback method with the token or with an error code and error message.  

### \~AppCheckProvider

```c++
virtual  ~AppCheckProvider()=0
```