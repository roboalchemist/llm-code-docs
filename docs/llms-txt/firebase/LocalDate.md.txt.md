# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate.md.txt

# LocalDate

# LocalDate


```
@Serializable(with = LocalDateSerializer)
class LocalDate
```

<br />

*** ** * ** ***

A date without a time-zone in the ISO-8601 calendar system, such as `2007-12-03`. This is the default Kotlin type used to represent a `Date` GraphQL custom scalar in Firebase Data Connect.

### Description (adapted from `https://developer.android.com/reference/kotlin/java/time/LocalDate.html`)

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` is an immutable date-time object that represents a date, often viewed as year-month-day. For example, the value "2nd October 2007" can be stored in a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate`.

This class does not store or represent a time or time-zone. Instead, it is a description of the date, as used for birthdays. It cannot represent an instant on the time-line without additional information such as an offset or time-zone.

### Relationship to `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` and `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate`

This class exists solely to fill the gap for a "day-month-year" data type in Android API versions less than 26. When the Firebase Android SDK updates its `minSdkVersion` to 26 or later, then this class will be marked as "deprecated" and eventually removed.

The `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` class was added in Android API 26 and should be used if it's available instead of this class. If `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` is available then `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` is a completely valid option as well, if it's desirable to take a dependency on [kotlinx-datetime](https://github.com/Kotlin/kotlinx-datetime).

Alternately, if your application has its `minSdkVersion` set to a value *less than* 26, you can use ["desugaring"](https://developer.android.com/studio/write/java8-support-table) to get access `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` class regardless of the API version used at runtime.

### Using `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` and `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` in code generation.

By default, the Firebase Data Connect code generation will use this class when generating code for Kotlin. If, however, you want to use the preferable `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` or `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` classes, add a `dateClass` entry in your `connector.yaml` set to the fully-qualified class name that you'd like to use. For example,

```kotlin
connectorId: demo
authMode: PUBLIC
generate:
  kotlinSdk:
    outputDir: ../../.generated/demo
    dateClass: java.time.LocalDate # or kotlinx.datetime.LocalDate
```

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#LocalDate(kotlin.Int,kotlin.Int,kotlin.Int)(year: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, month: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, day: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#hashCode()()` Calculates and returns the hash code for this object. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#day()` The day of the month. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#month()` The month. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#year()` The year. |

| ### Extension functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#(com.google.firebase.dataconnect.LocalDate).copy(kotlin.Int,kotlin.Int,kotlin.Int)(year: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, month: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, day: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` instance with the given property values. |
| `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()()` Creates and returns a `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` object that represents the same date as this object. |
| `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()()` Creates and returns a `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` object that represents the same date as this object. |

## Public constructors

### LocalDate

```
LocalDate(year: Int, month: Int, day: Int)
```

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` and has the same values for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#year()`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#month()`, and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate#day()` as this object, respectively. |

### hashCode

```
open fun hashCode(): Int
```

Calculates and returns the hash code for this object.

The hash code is *not* guaranteed to be stable across application restarts.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object, that incorporates the values of this object's public properties. |

### toString

```
open fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object, which includes the class name and the values of all public properties. |

## Public properties

### day

```
val day: Int
```

The day of the month. The valid range is between 1 and 31, inclusive; however, this is *not* checked or enforced by this class.

### month

```
val month: Int
```

The month. The valid range is between 1 and 12, inclusive; however, this is *not* checked or enforced by this class.

### year

```
val year: Int
```

The year. The valid range is between 1583 and 9999, inclusive; however, this is *not* checked or enforced by this class. Values less than 1583 are not strictly forbidden; however, their interpretation by the Data Connect backend is unspecified. See <https://en.wikipedia.org/wiki/ISO_8601#Years> for more details.

## Extension functions

### copy

```
fun LocalDate.copy(year: Int = this.year, month: Int = this.month, day: Int = this.day): LocalDate
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` instance with the given property values.

### toJavaLocalDate

```
fun LocalDate.toJavaLocalDate(): LocalDate
```

Creates and returns a `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` object that represents the same date as this object.

Be sure to *only* call this method if `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` is available; otherwise the behavior is undefined. If your application's `minSdkVersion` is greater than or equal to `26`, or if you have configured ["desugaring"](https://developer.android.com/studio/write/java8-support-table) then it is guaranteed to be available. Otherwise, check `https://developer.android.com/reference/kotlin/android/os/Build.VERSION.html#SDK_INT--` at runtime and verify that its value is at least `https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#O--` before calling this method.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(java.time.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(kotlinx.datetime.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()` |   |

### toKotlinxLocalDate

```
fun LocalDate.toKotlinxLocalDate(): LocalDate
```

Creates and returns a `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` object that represents the same date as this object.

Be sure to *only* call this method if your application has a dependency on `org.jetbrains.kotlinx:kotlinx-datetime`; otherwise, the behavior of this method is undefined. If your `minSdkVersion` is less than `26` then you *may* also need to configure ["desugaring"](https://developer.android.com/studio/write/java8-support-table).

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(kotlinx.datetime.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(java.time.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()` |   |