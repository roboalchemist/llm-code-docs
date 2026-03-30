# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide.md.txt

# Guide

# Guide


```
@Target(allowedTargets = [AnnotationTarget.PROPERTY])
@Retention(value = AnnotationRetention.SOURCE)
annotation Guide
```

<br />

*** ** * ** ***

This annotation is used with the `firebase-ai-ksp-processor` plugin to provide extra information on generated classes and fields.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide#Guide(kotlin.String,kotlin.Double,kotlin.Double,kotlin.Int,kotlin.Int,kotlin.String)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, minItems: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, maxItems: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, format: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide#description()` a description of the field |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide#format()` the format that a field must conform to |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide#maxItems()` the maximum number of items in a list |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide#maximum()` the maximum value (inclusive) which the numeric field may contain |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide#minItems()` the minimum number of items in a list |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/annotations/Guide#minimum()` the minimum value (inclusive) which the numeric field may contain |

## Public constructors

### Guide

```
Guide(
    description: String = "",
    minimum: Double = -1.0,
    maximum: Double = -1.0,
    minItems: Int = -1,
    maxItems: Int = -1,
    format: String = ""
)
```

## Public properties

### description

```
val description: String
```

a description of the field

### format

```
val format: String
```

the format that a field must conform to

### maxItems

```
val maxItems: Int
```

the maximum number of items in a list

### maximum

```
val maximum: Double
```

the maximum value (inclusive) which the numeric field may contain

### minItems

```
val minItems: Int
```

the minimum number of items in a list

### minimum

```
val minimum: Double
```

the minimum value (inclusive) which the numeric field may contain