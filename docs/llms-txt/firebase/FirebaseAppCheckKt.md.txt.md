# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt.md.txt

# FirebaseAppCheckKt

# FirebaseAppCheckKt


```
public final class FirebaseAppCheckKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/package-summary#(com.google.firebase.Firebase).appCheck()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt#(com.google.firebase.Firebase).appCheck(com.google.firebase.FirebaseApp)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide token. |
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis. |

## Public fields

### appCheck

```
public final @NonNull FirebaseAppCheck appCheck
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

## Public methods

### FirebaseAppCheckKt.appCheck

```
public static final @NonNull FirebaseAppCheck FirebaseAppCheckKt.appCheck(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### FirebaseAppCheckKt.component1

```
public static final @NonNull String FirebaseAppCheckKt.component1(@NonNull AppCheckToken receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide token.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the token of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` |

### FirebaseAppCheckKt.component2

```
public static final long FirebaseAppCheckKt.component2(@NonNull AppCheckToken receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis.

| Returns |
|---|---|
| `long` | the expireTimeMillis of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` |