# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Generable.md.txt

# Generable

# Generable


```
@Target(allowedTargets = [AnnotationTarget.CLASS])
@Retention(value = AnnotationRetention.SOURCE)
public annotation Generable
```

<br />

*** ** * ** ***

This annotation is used with the `firebase-ai-ksp-processor` plugin to generate `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` that match an existing Kotlin class structure. For more info see: [Firebase KSP Processor Readme](https://github.com/firebase/firebase-android-sdk/blob/main/firebase-ai-ksp-processor/README.md)

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Generable#description()` a description of the class to be forwarded to the model. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Generable#Generable(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description)` |

## Public fields

### description

```
public final @NonNull String description
```

a description of the class to be forwarded to the model. This will override a kDoc description.

## Public constructors

### Generable

```
public Generable(@NonNull String description)
```