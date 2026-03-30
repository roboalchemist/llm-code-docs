# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt.md.txt

# FirebaseKt

# FirebaseKt


```
public final class FirebaseKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/package-summary#(com.google.firebase.Firebase).app()` Returns the default firebase app instance. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/package-summary#(com.google.firebase.Firebase).options()` Returns options of default FirebaseApp |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).app(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns a named firebase app instance. |
| `static final https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).initialize(android.content.Context)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context )` Initializes and returns a FirebaseApp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options )` Initializes and returns a FirebaseApp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name )` Initializes and returns a FirebaseApp. |

## Public fields

### app

```
public final @NonNull FirebaseApp app
```

Returns the default firebase app instance.

### options

```
public final @NonNull FirebaseOptions options
```

Returns options of default FirebaseApp

## Public methods

### FirebaseKt.app

```
public static final @NonNull FirebaseApp FirebaseKt.app(@NonNull Firebase receiver, @NonNull String name)
```

Returns a named firebase app instance.

### FirebaseKt.initialize

```
public static final FirebaseApp FirebaseKt.initialize(
    @NonNull Firebase receiver,
    @NonNull Context context
)
```

Initializes and returns a FirebaseApp.

### FirebaseKt.initialize

```
public static final @NonNull FirebaseApp FirebaseKt.initialize(
    @NonNull Firebase receiver,
    @NonNull Context context,
    @NonNull FirebaseOptions options
)
```

Initializes and returns a FirebaseApp.

### FirebaseKt.initialize

```
public static final @NonNull FirebaseApp FirebaseKt.initialize(
    @NonNull Firebase receiver,
    @NonNull Context context,
    @NonNull FirebaseOptions options,
    @NonNull String name
)
```

Initializes and returns a FirebaseApp.