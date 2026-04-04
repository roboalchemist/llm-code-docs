# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder.md.txt

# FirebaseOptions.Builder

# FirebaseOptions.Builder


```
public final class FirebaseOptions.Builder
```

<br />

*** ** * ** ***

Builder for constructing FirebaseOptions.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#Builder()()` Constructs an empty builder. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#Builder(com.google.firebase.FirebaseOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options)` Initializes the builder's values from the options object. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#build()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setApiKey(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html apiKey)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setApplicationId(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html applicationId)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setDatabaseUrl(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html databaseUrl)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setGcmSenderId(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html gcmSenderId)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setProjectId(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html projectId)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html storageBucket)` |

## Public constructors

### Builder

```
public Builder()
```

Constructs an empty builder.

### Builder

```
public Builder(@NonNull FirebaseOptions options)
```

Initializes the builder's values from the options object.

The new builder is not backed by this objects values, that is changes made to the new builder don't change the values of the origin object.

## Public methods

### build

```
public @NonNull FirebaseOptions build()
```

### setApiKey

```
public @NonNull FirebaseOptions.Builder setApiKey(@NonNull String apiKey)
```

### setApplicationId

```
public @NonNull FirebaseOptions.Builder setApplicationId(@NonNull String applicationId)
```

### setDatabaseUrl

```
public @NonNull FirebaseOptions.Builder setDatabaseUrl(@Nullable String databaseUrl)
```

### setGcmSenderId

```
public @NonNull FirebaseOptions.Builder setGcmSenderId(@Nullable String gcmSenderId)
```

### setProjectId

```
public @NonNull FirebaseOptions.Builder setProjectId(@Nullable String projectId)
```

### setStorageBucket

```
public @NonNull FirebaseOptions.Builder setStorageBucket(@Nullable String storageBucket)
```