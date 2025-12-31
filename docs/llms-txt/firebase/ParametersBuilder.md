# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ParametersBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/ParametersBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/ParametersBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder.md.txt

# ParametersBuilder

# ParametersBuilder


```
class ParametersBuilder
```

<br />

*** ** * ** ***

Helper class used to enable fluent syntax in [logEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)).

## Summary

|                                                            ### Public constructors                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| [ParametersBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#ParametersBuilder())`()` |

|                             ### Public functions                             |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Bundle](https://developer.android.com/reference/android/os/Bundle.html)`>)` Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)) to the logged event. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[Bundle](https://developer.android.com/reference/android/os/Bundle.html)`)` Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)) to the logged event.                                                                    |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)) to the logged event.                                                                        |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)) to the logged event.                                                                                  |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)) to the logged event.                                                                        |

## Public constructors

### ParametersBuilder

```
ParametersBuilder()
```  

## Public functions

### param

```
funÂ param(key:Â String,Â value:Â Array<Bundle>):Â Unit
```

Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Array)) to the logged event.  

### param

```
funÂ param(key:Â String,Â value:Â Bundle):Â Unit
```

Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,android.os.Bundle)) to the logged event.  

### param

```
funÂ param(key:Â String,Â value:Â Double):Â Unit
```

Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Double)) to the logged event.  

### param

```
funÂ param(key:Â String,Â value:Â Long):Â Unit
```

Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.Long)) to the logged event.  

### param

```
funÂ param(key:Â String,Â value:Â String):Â Unit
```

Add parameter named [key](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)) with [value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder#param(kotlin.String,kotlin.String)) to the logged event.