# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Generable.md.txt

# Generable

# Generable


```
@Target(allowedTargets = [AnnotationTarget.CLASS])
@Retention(value = AnnotationRetention.SOURCE)
annotation Generable
```

<br />

*** ** * ** ***

This annotation is used with the `firebase-ai-ksp-processor` plugin to generate `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` that match an existing Kotlin class structure. For more info see: [Firebase KSP Processor Readme](https://github.com/firebase/firebase-android-sdk/blob/main/firebase-ai-ksp-processor/README.md)

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Generable#Generable(kotlin.String)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Generable#description()` a description of the class to be forwarded to the model. |

## Public constructors

### Generable

```
Generable(description: String = "")
```

## Public properties

### description

```
val description: String
```

a description of the class to be forwarded to the model. This will override a kDoc description.