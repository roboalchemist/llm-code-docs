# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult.md.txt

# HttpsCallableResult

# HttpsCallableResult


```
class HttpsCallableResult
```

<br />

*** ** * ** ***

The result of calling a `HttpsCallableReference` function.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult#getData()()` Returns the data that was returned from the Callable HTTPS trigger. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult#data()` The data that was returned from the Callable HTTPS trigger. |

## Public functions

### getData

```
fun getData(): Any?
```

Returns the data that was returned from the Callable HTTPS trigger.

The data is in the form of native Java objects. For example, if your trigger returned an array, this object would be a `List<Object>`. If your trigger returned a JavaScript object with keys and values, this object would be a `Map<String, Object>`.

## Public properties

### data

```
val data: Any?
```

The data that was returned from the Callable HTTPS trigger.

The data is in the form of native Java objects. For example, if your trigger returned an array, this object would be a `List<Object>`. If your trigger returned a JavaScript object with keys and values, this object would be a `Map<String, Object>`.