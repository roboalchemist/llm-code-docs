# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder.md.txt

# ParametersBuilder

# ParametersBuilder


```
class ParametersBuilder
```

<br />

*** ** * ** ***

Helper class used to enable fluent syntax in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#ParametersBuilder()()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/android/os/Bundle.html>)` Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` to the logged event. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://developer.android.com/reference/android/os/Bundle.html)` Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` to the logged event. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` to the logged event. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` to the logged event. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` to the logged event. |

## Public constructors

### ParametersBuilder

```
ParametersBuilder()
```

## Public functions

### param

```
fun param(key: String, value: Array<Bundle>): Unit
```

Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)` to the logged event.

### param

```
fun param(key: String, value: Bundle): Unit
```

Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)` to the logged event.

### param

```
fun param(key: String, value: Double): Unit
```

Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)` to the logged event.

### param

```
fun param(key: String, value: Long): Unit
```

Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)` to the logged event.

### param

```
fun param(key: String, value: String): Unit
```

Add parameter named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)` to the logged event.