# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ProviderQueryResult.md.txt

# ProviderQueryResult

public interface **ProviderQueryResult**  
**This interface is deprecated.**   

In favour of [SignInMethodQueryResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/SignInMethodQueryResult)
Result object that contains a list of strings that represent authentication provider IDs. For
example, [PROVIDER_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID)
or [PROVIDER_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider#PROVIDER_ID).  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract [List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\> | [getProviders](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ProviderQueryResult#getProviders())() Returns a [List](https://developer.android.com/reference/java/util/List.html) of string representing auth-provider ids. |

## Public Methods

#### public abstract [List](https://developer.android.com/reference/java/util/List.html)\<[String](https://developer.android.com/reference/java/lang/String.html)\>
**getProviders** ()

Returns a [List](https://developer.android.com/reference/java/util/List.html) of string
representing auth-provider ids. The list can be null or empty.