# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/KeyValueBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/ktx/KeyValueBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/KeyValueBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder.md.txt

# KeyValueBuilder

# KeyValueBuilder


```
public final class KeyValueBuilder
```

<br />

*** ** * ** ***

Helper class to enable convenient syntax in [setCustomKeys](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1)) and [recordException](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).recordException(kotlin.Throwable,kotlin.Function1))

## Summary

| ### Public methods |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final void`       | [key](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder#key(kotlin.String,kotlin.Boolean))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` key, boolean value)` Sets a custom key and value that are associated with reports.                                                                                                                                                                       |
| `final void`       | [key](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder#key(kotlin.String,kotlin.Double))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` key, double value)` Sets a custom key and value that are associated with reports.                                                                                                                                                                         |
| `final void`       | [key](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder#key(kotlin.String,kotlin.Float))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` key, float value)` Sets a custom key and value that are associated with reports.                                                                                                                                                                           |
| `final void`       | [key](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder#key(kotlin.String,kotlin.Int))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` key, int value)` Sets a custom key and value that are associated with reports.                                                                                                                                                                               |
| `final void`       | [key](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder#key(kotlin.String,kotlin.Long))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` key, long value)` Sets a custom key and value that are associated with reports.                                                                                                                                                                             |
| `final void`       | [key](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder#key(kotlin.String,kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` key, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` value)` Sets a custom key and value that are associated with reports. |

## Public methods

### key

```
publicÂ finalÂ voidÂ key(@NonNull StringÂ key,Â booleanÂ value)
```

Sets a custom key and value that are associated with reports.  

### key

```
publicÂ finalÂ voidÂ key(@NonNull StringÂ key,Â doubleÂ value)
```

Sets a custom key and value that are associated with reports.  

### key

```
publicÂ finalÂ voidÂ key(@NonNull StringÂ key,Â floatÂ value)
```

Sets a custom key and value that are associated with reports.  

### key

```
publicÂ finalÂ voidÂ key(@NonNull StringÂ key,Â intÂ value)
```

Sets a custom key and value that are associated with reports.  

### key

```
publicÂ finalÂ voidÂ key(@NonNull StringÂ key,Â longÂ value)
```

Sets a custom key and value that are associated with reports.  

### key

```
publicÂ finalÂ voidÂ key(@NonNull StringÂ key,Â @NonNull StringÂ value)
```

Sets a custom key and value that are associated with reports.