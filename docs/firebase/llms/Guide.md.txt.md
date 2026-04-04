# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide.md.txt

# Guide

# Guide


```
@Target(allowedTargets = [AnnotationTarget.PROPERTY])
@Retention(value = AnnotationRetention.SOURCE)
public annotation Guide
```

<br />

*** ** * ** ***

This annotation is used with the `firebase-ai-ksp-processor` plugin to provide extra information on generated classes and fields.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide#description()` a description of the field |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide#format()` the format that a field must conform to |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide#maxItems()` the maximum number of items in a list |
| `final double` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide#maximum()` the maximum value (inclusive) which the numeric field may contain |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide#minItems()` the minimum number of items in a list |
| `final double` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide#minimum()` the minimum value (inclusive) which the numeric field may contain |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/annotations/Guide#Guide(kotlin.String,kotlin.Double,kotlin.Double,kotlin.Int,kotlin.Int,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, double minimum, double maximum, int minItems, int maxItems, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html format )` |

## Public fields

### description

```
public final @NonNull String description
```

a description of the field

### format

```
public final @NonNull String format
```

the format that a field must conform to

### maxItems

```
public final int maxItems
```

the maximum number of items in a list

### maximum

```
public final double maximum
```

the maximum value (inclusive) which the numeric field may contain

### minItems

```
public final int minItems
```

the minimum number of items in a list

### minimum

```
public final double minimum
```

the minimum value (inclusive) which the numeric field may contain

## Public constructors

### Guide

```
public Guide(
    @NonNull String description,
    double minimum,
    double maximum,
    int minItems,
    int maxItems,
    @NonNull String format
)
```