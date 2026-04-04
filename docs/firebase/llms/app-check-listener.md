# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener.md.txt

# firebase::app_check::AppCheckListener Class Reference

# firebase::app_check::AppCheckListener


**This is an abstract class.**


`#include <app_check.h>`

Base class used to receive messages when [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) token changes.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [~AppCheckListener](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener_1a82bb760dcc9be35267062ed607fa7570)`()` ||

|                                                                                                                                                                                                                                ### Public functions                                                                                                                                                                                                                                 ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [OnAppCheckTokenChanged](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener_1a9d0e527da64f1cf418559bee0b20622e)`(const `[AppCheckToken](https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token)` & token)=0` | `virtual void` This method gets invoked on the UI thread on changes to the token state. |

## Public functions

### OnAppCheckTokenChanged

```c++
virtual void OnAppCheckTokenChanged(
  const AppCheckToken & token
)=0
```  
This method gets invoked on the UI thread on changes to the token state.

Does not trigger on token expiry.  

### \~AppCheckListener

```c++
virtual  ~AppCheckListener()=0
```