# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.md.txt

# FirebaseOptions

# FirebaseOptions


```
public final class FirebaseOptions
```

<br />

*** ** * ** ***

Configurable Firebase options.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder` Builder for constructing FirebaseOptions. |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#apiKey()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#applicationId()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#databaseUrl()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#gaTrackingId()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#gcmSenderId()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#projectId()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#storageBucket()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#fromResource(android.content.Context)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context)` Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` instance that is populated from string resources. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#getApiKey()()` API key used for authenticating requests from your app, e.g. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#getApplicationId()()` The Google App ID that is used to uniquely identify an instance of an app. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#getDatabaseUrl()()` The database root URL, e.g. http://abc-xyz-123.firebaseio.com. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#getGcmSenderId()()` The Project Number from the Google Developer's console, for example 012345678901, used to configure Google Cloud Messaging. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#getProjectId()()` The Google Cloud project ID, e.g. my-project-1234 |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#getStorageBucket()()` The Google Cloud Storage bucket name, e.g. abc-xyz-123.storage.firebase.com. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#hashCode()()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions#toString()()` |

## Public fields

### apiKey

```
public final String apiKey
```

### applicationId

```
public final String applicationId
```

### databaseUrl

```
public final String databaseUrl
```

### gaTrackingId

```
public final String gaTrackingId
```

### gcmSenderId

```
public final String gcmSenderId
```

### projectId

```
public final String projectId
```

### storageBucket

```
public final String storageBucket
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### fromResource

```
public static @Nullable FirebaseOptions fromResource(@NonNull Context context)
```

Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` instance that is populated from string resources.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` | The populated options or null if applicationId is missing from resources. |

### getApiKey

```
public @NonNull String getApiKey()
```

API key used for authenticating requests from your app, e.g. AIzaSyDdVgKwhZl0sTTTLZ7iTmt1r3N2cJLnaDk, used to identify your app to Google servers.

### getApplicationId

```
public @NonNull String getApplicationId()
```

The Google App ID that is used to uniquely identify an instance of an app.

### getDatabaseUrl

```
public @Nullable String getDatabaseUrl()
```

The database root URL, e.g. http://abc-xyz-123.firebaseio.com.

### getGcmSenderId

```
public @Nullable String getGcmSenderId()
```

The Project Number from the Google Developer's console, for example 012345678901, used to configure Google Cloud Messaging.

### getProjectId

```
public @Nullable String getProjectId()
```

The Google Cloud project ID, e.g. my-project-1234

### getStorageBucket

```
public @Nullable String getStorageBucket()
```

The Google Cloud Storage bucket name, e.g. abc-xyz-123.storage.firebase.com.

### hashCode

```
public int hashCode()
```

### toString

```
public String toString()
```