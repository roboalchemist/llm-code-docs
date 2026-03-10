# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations.md.txt

# FirebaseInstallations

# FirebaseInstallations


```
public class FirebaseInstallations implements FirebaseInstallationsApi
```

<br />

*** ** * ** ***

Entry point for Firebase installations.

The Firebase installations service:

- provides a unique identifier for a Firebase installation
- provides an auth token for a Firebase installation
- provides a API to perform GDPR-compliant deletion of a Firebase installation.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#delete()()` Call to delete this Firebase app installation from the Firebase backend. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getId()()` Returns a globally unique identifier of this Firebase app installation. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` | `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getInstance()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` | `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/installations/InstallationTokenResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations#getToken(boolean)(boolean forceRefresh)` Returns a valid authentication token for the Firebase installation. |

## Public methods

### delete

```
public @NonNull Task<Void> delete()
```

Call to delete this Firebase app installation from the Firebase backend. This call may cause Firebase Cloud Messaging, Firebase Remote Config, Firebase A/B Testing, or Firebase In-App Messaging to not function properly.

### getId

```
public @NonNull Task<String> getId()
```

Returns a globally unique identifier of this Firebase app installation. This is a url-safe base64 string of a 128-bit integer.

### getInstance

```
public static @NonNull FirebaseInstallations getInstance()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` instance |

### getInstance

```
public static @NonNull FirebaseInstallations getInstance(@NonNull FirebaseApp app)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations` instance |

### getToken

```
public @NonNull Task<InstallationTokenResult> getToken(boolean forceRefresh)
```

Returns a valid authentication token for the Firebase installation. Generates a new token if one doesn't exist, is expired, or is about to expire.

Should only be called if the Firebase installation is registered.

| Parameters |
|---|---|
| `boolean forceRefresh` | Options to get an auth token either by force refreshing or not. |