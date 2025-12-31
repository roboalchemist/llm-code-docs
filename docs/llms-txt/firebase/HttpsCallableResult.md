# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult.md.txt

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

|                             ### Public functions                              |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | [getData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult#getData())`()` Returns the data that was returned from the Callable HTTPS trigger. |

|                             ### Public properties                             |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | [data](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult#data()) The data that was returned from the Callable HTTPS trigger. |

## Public functions

### getData

```
funÂ getData():Â Any?
```

Returns the data that was returned from the Callable HTTPS trigger.

The data is in the form of native Java objects. For example, if your trigger returned an array, this object would be a `List<Object>`. If your trigger returned a JavaScript object with keys and values, this object would be a `Map<String, Object>`.  

## Public properties

### data

```
valÂ data:Â Any?
```

The data that was returned from the Callable HTTPS trigger.

The data is in the form of native Java objects. For example, if your trigger returned an array, this object would be a `List<Object>`. If your trigger returned a JavaScript object with keys and values, this object would be a `Map<String, Object>`.