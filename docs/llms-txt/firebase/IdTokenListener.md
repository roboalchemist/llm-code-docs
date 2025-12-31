# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener.md.txt

# IdTokenListener

public interface **IdTokenListener**  
| **Provides an inter-operational interface only** ; instead, use [FirebaseAuth.IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener) to call a listener when an IdToken changes.

Used to deliver notifications when authentication state changes.  

### Public Method Summary

|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract void | [onIdTokenChanged](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/internal/IdTokenListener#onIdTokenChanged(com.google.firebase.internal.InternalTokenResult))([InternalTokenResult](https://firebase.google.com/docs/reference/android/com/google/firebase/internal/InternalTokenResult) tokenResult) | Provides an inter-operational interface only; instead use [FirebaseAuth.IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener). |

## Public Methods

#### public abstract void **onIdTokenChanged** ([InternalTokenResult](https://firebase.google.com/docs/reference/android/com/google/firebase/internal/InternalTokenResult) tokenResult)

| Provides an inter-operational interface only; instead use [FirebaseAuth.IdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener).

This method gets invoked on changes in the authentication state.  

##### Parameters

| tokenResult | represents the InternalTokenResult interface, which can be used to obtain a cached access token. |
|-------------|--------------------------------------------------------------------------------------------------|