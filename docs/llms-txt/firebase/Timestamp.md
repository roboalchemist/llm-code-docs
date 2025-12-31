# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Timestamp.md.txt

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
|----------|--------------------------------------------------------------------------------|
|          | [Timestamp](https://git.page.link/timestamp-proto)The ref timestamp definition |

## Summary

|                                ### Public companion functions                                |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp) | [now](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp.Companion#now())`()` |

|                                                                                      ### Public companion properties                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [Parcelable.Creator](https://developer.android.com/reference/kotlin/android/os/Parcelable.Creator.html)`<`[Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)`>` | [CREATOR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp.Companion#CREATOR()) |

|                                                                                                                                                                                                     ### Public constructors                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#Timestamp(java.util.Date))`(date: `[Date](https://developer.android.com/reference/kotlin/java/util/Date.html)`)`                                                                                                                                                                                                                     |
| `@`[RequiresApi](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html)`(value = 26)` [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#Timestamp(java.time.Instant))`(time: `[Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)`)`                                                                                        |
| [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#Timestamp(kotlin.Long,kotlin.Int))`(seconds: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`, nanoseconds: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Creates a new [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp). |

|                                        ### Public functions                                        |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `open operator `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)         | [compareTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#compareTo(com.google.firebase.Timestamp))`(other: `[Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)`)`                                                                                                                                   |
| `open `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                  | [describeContents](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#describeContents())`()`                                                                                                                                                                                                                                                       |
| `open operator `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#equals(kotlin.Any))`(other: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)`                                                                                                                                                                             |
| `open `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                  | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#hashCode())`()`                                                                                                                                                                                                                                                                       |
| [Date](https://developer.android.com/reference/kotlin/java/util/Date.html)                         | [toDate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#toDate())`()` Returns a new [Date](https://developer.android.com/reference/kotlin/java/util/Date.html) corresponding to this timestamp.                                                                                                                                                 |
| [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)                   | `@`[RequiresApi](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html)`(value = 26)` [toInstant](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#toInstant())`()` Returns a new [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html) that matches the time defined by this timestamp. |
| `open `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)            | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#toString())`()`                                                                                                                                                                                                                                                                       |
| `open `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                | [writeToParcel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#writeToParcel(android.os.Parcel,kotlin.Int))`(dest: `[Parcel](https://developer.android.com/reference/kotlin/android/os/Parcel.html)`, flags: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)`                                                     |

|                            ### Public properties                             |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)   | [nanoseconds](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#nanoseconds()) |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [seconds](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp#seconds())         |

## Public companion functions

### now

```
funÂ now():Â Timestamp
```  

## Public companion properties

### CREATOR

```
valÂ CREATOR:Â Parcelable.Creator<Timestamp>
```  

## Public constructors

### Timestamp

```
Timestamp(date:Â Date)
```  

### Timestamp

```
@RequiresApi(valueÂ =Â 26)
Timestamp(time:Â Instant)
```  

### Timestamp

```
Timestamp(seconds:Â Long,Â nanoseconds:Â Int)
```

Creates a new [Timestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp).  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `seconds: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)   | represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.                                                                                         |
| `nanoseconds: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | represents non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanoseconds values that count forward in time. Must be from 0 to 999,999,999 inclusive. |

## Public functions

### compareTo

```
openÂ operatorÂ funÂ compareTo(other:Â Timestamp):Â Int
```  

### describeContents

```
openÂ funÂ describeContents():Â Int
```  

### equals

```
openÂ operatorÂ funÂ equals(other:Â Any?):Â Boolean
```  

### hashCode

```
openÂ funÂ hashCode():Â Int
```  

### toDate

```
funÂ toDate():Â Date
```

Returns a new [Date](https://developer.android.com/reference/kotlin/java/util/Date.html) corresponding to this timestamp.

This may lose precision.  

### toInstant

```
@RequiresApi(valueÂ =Â 26)
funÂ toInstant():Â Instant
```

Returns a new [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html) that matches the time defined by this timestamp.  

### toString

```
openÂ funÂ toString():Â String
```  

### writeToParcel

```
openÂ funÂ writeToParcel(dest:Â Parcel,Â flags:Â Int):Â Unit
```  

## Public properties

### nanoseconds

```
valÂ nanoseconds:Â Int
```  

### seconds

```
valÂ seconds:Â Long
```