# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/id-token-listener.md.txt

# firebase::auth::IdTokenListener Class Reference

# firebase::auth::IdTokenListener


**This is an abstract class.**


`#include <auth.h>`

Listener called when there is a change in the ID token.

## Summary

Override base class method to handle ID token changes. Methods are invoked asynchronously and may be invoked on other threads.

| ### Constructors and Destructors ||
|---|---|
| [~IdTokenListener](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/id-token-listener#classfirebase_1_1auth_1_1_id_token_listener_1a68c92b066db38dcddb317fdaec7d1555)`()` ||

|                                                                                                                                                                                      ### Public functions                                                                                                                                                                                      ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [OnIdTokenChanged](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/id-token-listener#classfirebase_1_1auth_1_1_id_token_listener_1aa09db55f7cd7321f5177c0c40bc7401a)`(`[Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth)` *auth)=0` | `virtual void` Called when there is a change in the current user's token. |

## Public functions

### OnIdTokenChanged

```c++
virtual void OnIdTokenChanged(
  Auth *auth
)=0
```  
Called when there is a change in the current user's token.


- Right after the listener has been registered
- When a user signs in
- When the current user signs out
- When the current user changes
- When there is a change in the current user's token

<br />

<br />

|                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                      ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `auth` | Disambiguates which [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) instance the event corresponds to, in the case where you are using more than one at the same time. | |

### \~IdTokenListener

```c++
virtual  ~IdTokenListener()
```  

| **Note:** : Destruction of the listener automatically calls RemoveIdTokenListener() from the Auths this listener is registered with, if those Auths have not yet been destroyed.

<br />