# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/InternalAuthProvider.md.txt

# InternalAuthProvider

public interface **InternalAuthProvider**  
| **Provides an inter-operational interface only** ; instead, use the public methods specified for [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) and [FirebaseUser](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser).

Provides an interface for internal clients of Firebase Authentication to get an access
token for a signed-in user.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract void                                                                                                                 | [addIdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/InternalAuthProvider#addIdTokenListener(com.google.firebase.auth.internal.IdTokenListener))([IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener) listener) | Provides an inter-operational interface only; instead, use [FirebaseAuth.addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)).                     |
| abstract Task\<[GetTokenResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult)\> | [getAccessToken](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/InternalAuthProvider#getAccessToken(boolean))(boolean forceRefresh) | Provides an inter-operational interface only; instead, use [FirebaseUser.getIdToken(boolean)](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getIdToken(boolean)).                                                                                                                                                                                                                                                                                               |
| abstract [String](https://developer.android.com/reference/java/lang/String.html)                                              | [getUid](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/InternalAuthProvider#getUid())() | Provides an inter-operational interface only; instead, use [UserInfo.getUid()](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getUid()).                                                                                                                                                                                                                                                                                                                                                                        |
| abstract void                                                                                                                 | [removeIdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/InternalAuthProvider#removeIdTokenListener(com.google.firebase.auth.internal.IdTokenListener))([IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener) listenerToRemove) | Provides an inter-operational interface only; instead, use [FirebaseAuth.removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)). |

## Public Methods

#### public abstract void **addIdTokenListener** ([IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener) listener)

| Provides an inter-operational interface only; instead, use [FirebaseAuth.addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)).

Adds an [IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener)
to the list of interested listeners. Also indicates that you *need* a fresh
IdToken at all times, turning on Proactive Token Refreshing. Unlike the public method,
this method does *not* trigger immediately when added.  

##### Parameters

| listener | represents the [IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener) that should be notified when the user state changes. |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public abstract Task\<[GetTokenResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult)\>
**getAccessToken** (boolean forceRefresh)

| Provides an inter-operational interface only; instead, use [FirebaseUser.getIdToken(boolean)](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getIdToken(boolean)).

Fetches a valid STS Token.  

##### Parameters

| forceRefresh | force refreshes the token. Should only be set to `true` if the token is invalidated out of band. |
|--------------|--------------------------------------------------------------------------------------------------|

##### Returns

- a [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task)  

#### public abstract [String](https://developer.android.com/reference/java/lang/String.html) **getUid** ()

| Provides an inter-operational interface only; instead, use [UserInfo.getUid()](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getUid()).

Returns a string used to uniquely identify a signed-in user in a Firebase project's
user database.

This identifier is opaque and does not correspond necessarily to the user's email
address or any other field.  

##### Returns

- the string representation of the `uid`. Returns null if [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) is not added to the Firebase project, or if there is not a currently signed-in user.  

#### public abstract void **removeIdTokenListener** ([IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener) listenerToRemove)

| Provides an inter-operational interface only; instead, use [FirebaseAuth.removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)).

Removes an [IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener)
from the list of interested listeners.  

##### Parameters

| listenerToRemove | represents the instance of [IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener) to be removed. |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|