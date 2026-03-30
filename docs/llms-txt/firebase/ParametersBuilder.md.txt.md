# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder.md.txt

# ParametersBuilder

# ParametersBuilder


```
public final class ParametersBuilder
```

<br />

*** ** * ** ***

Helper class used to enable fluent syntax in `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#ParametersBuilder()()` |

| ### Public methods |
|---|---|
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html key, @https://developer.android.com/reference/androidx/annotation/NonNull.html Bundle[] value)` Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` to the logged event. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html key, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Bundle.html value)` Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` to the logged event. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html key, double value)` Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` to the logged event. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html key, long value)` Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` to the logged event. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html key, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html value)` Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` to the logged event. |

## Public constructors

### ParametersBuilder

```
public ParametersBuilder()
```

## Public methods

### param

```
public final void param(@NonNull String key, @NonNull Bundle[] value)
```

Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` to the logged event.

### param

```
public final void param(@NonNull String key, @NonNull Bundle value)
```

Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` to the logged event.

### param

```
public final void param(@NonNull String key, double value)
```

Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` to the logged event.

### param

```
public final void param(@NonNull String key, long value)
```

Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` to the logged event.

### param

```
public final void param(@NonNull String key, @NonNull String value)
```

Add parameter named `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` with `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` to the logged event.