# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion.md.txt

# FirebaseFunctions.Companion

# FirebaseFunctions.Companion


```
public static class FirebaseFunctions.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance()()` Creates a Cloud Functions client with the default app. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Creates a Cloud Functions client with the given app. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain)` Creates a Cloud Functions client with the default app and given region or custom domain. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain)` Creates a Cloud Functions client with the given app and region or custom domain. |

## Public methods

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance()
```

Creates a Cloud Functions client with the default app.

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance(@NonNull FirebaseApp app)
```

Creates a Cloud Functions client with the given app.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The app for the Firebase project. |

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance(@NonNull String regionOrCustomDomain)
```

Creates a Cloud Functions client with the default app and given region or custom domain.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain` | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance(@NonNull FirebaseApp app, @NonNull String regionOrCustomDomain)
```

Creates a Cloud Functions client with the given app and region or custom domain.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The app for the Firebase project. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain` | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |