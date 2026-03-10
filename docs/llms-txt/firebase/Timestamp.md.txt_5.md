# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp.md.txt

# Timestamp

# Timestamp


```
class Timestamp : Comparable, Parcelable
```

<br />

*** ** * ** ***

A Timestamp represents a point in time independent of any time zone or calendar.

Represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time. It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. Furthermore,It is encoded assuming all minutes are 60 seconds long, specifically leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to and from RFC 3339 date strings.

| See also |
|---|---|
|   | [Timestamp](https://git.page.link/timestamp-proto)The ref timestamp definition |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp.Companion#now()()` |

| ### Public companion properties |
|---|---|
| `https://developer.android.com/reference/kotlin/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp.Companion#CREATOR()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#Timestamp(java.util.Date)(date: https://developer.android.com/reference/kotlin/java/util/Date.html)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html(value = 26) https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#Timestamp(java.time.Instant)(time: https://developer.android.com/reference/kotlin/java/time/Instant.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#Timestamp(kotlin.Long,kotlin.Int)(seconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, nanoseconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp`. |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#compareTo(com.google.firebase.Timestamp)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#describeContents()()` |
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#hashCode()()` |
| `https://developer.android.com/reference/kotlin/java/util/Date.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#toDate()()` Returns a new `https://developer.android.com/reference/kotlin/java/util/Date.html` corresponding to this timestamp. |
| `https://developer.android.com/reference/kotlin/java/time/Instant.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html(value = 26) https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#toInstant()()` Returns a new `https://developer.android.com/reference/kotlin/java/time/Instant.html` that matches the time defined by this timestamp. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#toString()()` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#writeToParcel(android.os.Parcel,kotlin.Int)(dest: https://developer.android.com/reference/kotlin/android/os/Parcel.html, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#nanoseconds()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#seconds()` |

## Public companion functions

### now

```
fun now(): Timestamp
```

## Public companion properties

### CREATOR

```
val CREATOR: Parcelable.Creator<Timestamp>
```

## Public constructors

### Timestamp

```
Timestamp(date: Date)
```

### Timestamp

```
@RequiresApi(value = 26)
Timestamp(time: Instant)
```

### Timestamp

```
Timestamp(seconds: Long, nanoseconds: Int)
```

Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp`.

| Parameters |
|---|---|
| `seconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. |
| `nanoseconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | represents non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanoseconds values that count forward in time. Must be from 0 to 999,999,999 inclusive. |

## Public functions

### compareTo

```
open operator fun compareTo(other: Timestamp): Int
```

### describeContents

```
open fun describeContents(): Int
```

### equals

```
open operator fun equals(other: Any?): Boolean
```

### hashCode

```
open fun hashCode(): Int
```

### toDate

```
fun toDate(): Date
```

Returns a new `https://developer.android.com/reference/kotlin/java/util/Date.html` corresponding to this timestamp.

This may lose precision.

### toInstant

```
@RequiresApi(value = 26)
fun toInstant(): Instant
```

Returns a new `https://developer.android.com/reference/kotlin/java/time/Instant.html` that matches the time defined by this timestamp.

### toString

```
open fun toString(): String
```

### writeToParcel

```
open fun writeToParcel(dest: Parcel, flags: Int): Unit
```

## Public properties

### nanoseconds

```
val nanoseconds: Int
```

### seconds

```
val seconds: Long
```