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

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete()()` Call to delete this Firebase app installation from the Firebase backend. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getId()()` Returns a globally unique identifier of this Firebase app installation. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getInstance()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/InstallationTokenResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#getToken(boolean)(forceRefresh: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a valid authentication token for the Firebase installation. |

## Public functions

### delete

```
fun delete(): Task<Void!>
```

Call to delete this Firebase app installation from the Firebase backend. This call may cause Firebase Cloud Messaging, Firebase Remote Config, Firebase A/B Testing, or Firebase In-App Messaging to not function properly.

### getId

```
fun getId(): Task<String!>
```

Returns a globally unique identifier of this Firebase app installation. This is a url-safe base64 string of a 128-bit integer.

### getInstance

```
java-static fun getInstance(): FirebaseInstallations
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` instance |

### getInstance

```
java-static fun getInstance(app: FirebaseApp): FirebaseInstallations
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations` instance |

### getToken

```
fun getToken(forceRefresh: Boolean): Task<InstallationTokenResult!>
```

Returns a valid authentication token for the Firebase installation. Generates a new token if one doesn't exist, is expired, or is about to expire.

Should only be called if the Firebase installation is registered.

| Parameters |
|---|---|
| `forceRefresh: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Options to get an auth token either by force refreshing or not. |