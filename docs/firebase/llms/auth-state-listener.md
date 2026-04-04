# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth-state-listener.md.txt

# firebase::auth::AuthStateListener Class Reference

# firebase::auth::AuthStateListener


**This is an abstract class.**


`#include <auth.h>`

Listener called when there is a change in the authentication state.

## Summary

Override base class method to handle authentication state changes. Methods are invoked asynchronously and may be invoked on other threads.

| ### Constructors and Destructors ||
|---|---|
| [~AuthStateListener](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth-state-listener#classfirebase_1_1auth_1_1_auth_state_listener_1a1674fd3c94c8155ad79361b66f9eb487)`()` ||

|                                                                                                                                                                                       ### Public functions                                                                                                                                                                                        ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [OnAuthStateChanged](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth-state-listener#classfirebase_1_1auth_1_1_auth_state_listener_1a9ac0823945bfbd7074ad140a3206fd00)`(`[Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth)` *auth)=0` | `virtual void` Called when the authentication state of `auth` changes. |

## Public functions

### OnAuthStateChanged

```c++
virtual void OnAuthStateChanged(
  Auth *auth
)=0
```  
Called when the authentication state of `auth` changes.


- Right after the listener has been registered
- When a user is signed in
- When the current user is signed out
- When the current user changes

<br />

<br />

|                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                      ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `auth` | Disambiguates which [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) instance the event corresponds to, in the case where you are using more than one at the same time. | |

### \~AuthStateListener

```c++
virtual  ~AuthStateListener()
```  

| **Note:** : Destruction of the listener automatically calls RemoveAuthStateListener() from the Auths this listener is registered with, if those Auths have not yet been destroyed.

<br />