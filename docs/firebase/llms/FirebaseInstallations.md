# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations.md.txt

# FirebaseInstallations

# FirebaseInstallations


```
class FirebaseInstallations : FirebaseInstallationsApi
```

<br />

*** ** * ** ***

Entry point for Firebase installations.

The Firebase installations service:

- provides a unique identifier for a Firebase installation
- provides an auth token for a Firebase installation
- provides a API to perform GDPR-compliant deletion of a Firebase installation.

## Summary

|                                                                                                            ### Public functions                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                             | [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete())`()` Call to delete this Firebase app installation from the Firebase backend.                                                                                                                                                                                                                                                                                                                                                   |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>`                                                       | [getId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getId())`()` Returns a globally unique identifier of this Firebase app installation.                                                                                                                                                                                                                                                                                                                                                      |
| `java-static `[FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations)                                                                                            | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getInstance())`()` Returns the [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).                                                                                                                                    |
| `java-static `[FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations)                                                                                            | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getInstance(com.google.firebase.FirebaseApp))`(app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)` Returns the [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp). |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[InstallationTokenResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/InstallationTokenResult)`!>` | [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getToken(boolean))`(forceRefresh: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Returns a valid authentication token for the Firebase installation.                                                                                                                                                                                                                                           |

## Public functions

### delete

```
funÂ delete():Â Task<Void!>
```

Call to delete this Firebase app installation from the Firebase backend. This call may cause Firebase Cloud Messaging, Firebase Remote Config, Firebase A/B Testing, or Firebase In-App Messaging to not function properly.  

### getId

```
funÂ getId():Â Task<String!>
```

Returns a globally unique identifier of this Firebase app installation. This is a url-safe base64 string of a 128-bit integer.  

### getInstance

```
java-staticÂ funÂ getInstance():Â FirebaseInstallations
```

Returns the [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).  

|                                                              Returns                                                               |
|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) | a [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) instance |

### getInstance

```
java-staticÂ funÂ getInstance(app:Â FirebaseApp):Â FirebaseInstallations
```

Returns the [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).  

|                                               Parameters                                                |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) | a custom [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) |

|                                                              Returns                                                               |
|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) | a [FirebaseInstallations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations) instance |

### getToken

```
funÂ getToken(forceRefresh:Â Boolean):Â Task<InstallationTokenResult!>
```

Returns a valid authentication token for the Firebase installation. Generates a new token if one doesn't exist, is expired, or is about to expire.

Should only be called if the Firebase installation is registered.  

|                                             Parameters                                             |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `forceRefresh: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Options to get an auth token either by force refreshing or not. |