# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp.md.txt

# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp.md.txt

# Firebase.Firestore.Timestamp Struct Reference

# Firebase.Firestore.Timestamp

A nanosecond-precision immutable timestamp.

## Summary

When this is stored as part of a document in [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore), it is truncated to the microsecond, towards the start of time.

A [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time. It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to and from RFC 3339 date strings.

### Inheritance

Inherits from: IEquatable\< Timestamp \>, IComparable, IComparable\< Timestamp \>

|                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                     ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [CompareTo](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1aa8473658fac03fcc5fd3f43d59d1f2fd)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` other)` | `int`                                                                             |
| [CompareTo](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1aa8f912ceb96a9cb1086bee1b9056a4a6)`(object obj)`                                                                                                                                            | `int`                                                                             |
| [Equals](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a2008aaf712f03d6b2dea1bbfa73a36f6)`(object obj)`                                                                                                                                               | `override bool`                                                                   |
| [Equals](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a0a33f5a71841f6ac41d41bb07c47daab)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` other)`    | `bool`                                                                            |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a6883bb85b9267ceea85e447bfdf29054)`()`                                                                                                                                                    | `override int`                                                                    |
| [ToDateTime](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1ac73f6b8a33ac5eb77f24c1e0864df298)`()`                                                                                                                                                     | `DateTime` Converts this timestamp to a DateTime with a kind of DateTimeKind.Utc. |
| [ToDateTimeOffset](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a47460d698ea0f7ad5156f288803538d3)`()`                                                                                                                                               | `DateTimeOffset` Converts this timestamp into a DateTimeOffset.                   |
| [ToString](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1abe7f7de3868af5faa716a2e92e3a992d)`()`                                                                                                                                                       | `override string`                                                                 |

|                                                                                                                                                                                                                                                                                                                                                                                                    ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                    ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FromDateTime](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1aaebddca9f9cc22fb5d98175a9e7211d1)`(DateTime dateTime)`                                                                                                                                                                                                                                                                                      | [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) Converts a DateTime to a [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp).              |
| [FromDateTimeOffset](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a846bc7ea2a03fe449d862bd5edae34f1)`(DateTimeOffset dateTimeOffset)`                                                                                                                                                                                                                                                                    | [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) Converts the given DateTimeOffset to a [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) |
| [GetCurrentTimestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a2ee86d9e66b7d64e32e69c3e3b3a0b40)`()`                                                                                                                                                                                                                                                                                                | [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) Returns the current timestamp according to the system clock.                                                                                                                         |
| [operator!=](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1aaff1c43f831107a4bc9a39445d80f944)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` lhs, `[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` rhs)` | `bool` Operator overload to compare two [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) values for inequality.                                                                                                                       |
| [operator<](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a49f657f139b9301b60fd1216249d18f5)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` lhs, `[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` rhs)`  | `bool` Compares two timestamps.                                                                                                                                                                                                                                                                                                    |
| [operator<=](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1ab249daedacedcf07946ce7d1d4907fd5)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` lhs, `[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` rhs)` | `bool` Compares two timestamps.                                                                                                                                                                                                                                                                                                    |
| [operator==](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a47484b8a2b5f96c6ae6989c5bb62425f)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` lhs, `[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` rhs)` | `bool` Operator overload to compare two [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) values for equality.                                                                                                                         |
| [operator>](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1aa866a491b6ad38a75b777dc9f653f196)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` lhs, `[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` rhs)`  | `bool` Compares two timestamps.                                                                                                                                                                                                                                                                                                    |
| [operator>=](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp_1a05120a3ea0ecb100c3ad4d1ef8f1c772)`(`[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` lhs, `[Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)` rhs)` | `bool` Compares two timestamps.                                                                                                                                                                                                                                                                                                    |

## Public functions

### CompareTo

```c#
int Firebase::Firestore::Timestamp::CompareTo(
  Timestamp other
)
```  

### CompareTo

```c#
int Firebase::Firestore::Timestamp::CompareTo(
  object obj
)
```  

### Equals

```c#
override bool Firebase::Firestore::Timestamp::Equals(
  object obj
)
```  

### Equals

```c#
bool Firebase::Firestore::Timestamp::Equals(
  Timestamp other
)
```  

### GetHashCode

```c#
override int Firebase::Firestore::Timestamp::GetHashCode()
```  

### ToDateTime

```c#
DateTime Firebase::Firestore::Timestamp::ToDateTime()
```  
Converts this timestamp to a DateTime with a kind of DateTimeKind.Utc.

This can lose information as DateTime has a precision of a tick (100 nanoseconds). If the timestamp is not a precise number of ticks, it will be truncated towards the start of time.

<br />

|                          Details                          ||
|-------------|----------------------------------------------|
| **Returns** | A DateTime representation of this timestamp. |

### ToDateTimeOffset

```c#
DateTimeOffset Firebase::Firestore::Timestamp::ToDateTimeOffset()
```  
Converts this timestamp into a DateTimeOffset.

The resulting `DateTimeOffset` will always have an `Offset` of zero. If the timestamp is not a precise number of ticks, it will be truncated towards the start of time. DateTimeOffset value precisely on a second.

<br />

|                      Details                       ||
|-------------|---------------------------------------|
| **Returns** | This timestamp as a `DateTimeOffset`. |

### ToString

```c#
override string Firebase::Firestore::Timestamp::ToString()
```  

## Public static functions

### FromDateTime

```c#
Timestamp Firebase::Firestore::Timestamp::FromDateTime(
  DateTime dateTime
)
```  
Converts a DateTime to a [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp).

<br />

|                                                                                           Details                                                                                           ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|----------------------------------------------------------| | `dateTime` | The value to convert; its kind must be DateTimeKind.Utc. |                            |
| **Returns** | A [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) representation of *dateTime* . |

### FromDateTimeOffset

```c#
Timestamp Firebase::Firestore::Timestamp::FromDateTimeOffset(
  DateTimeOffset dateTimeOffset
)
```  
Converts the given DateTimeOffset to a [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp)

The offset is taken into consideration when converting the value (so the same instant in time is represented) but is not a separate part of the resulting value. In other words, there is no round-trip operation that can retrieve the original `DateTimeOffset`.

<br />

|                                                                                         Details                                                                                          ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------------|----------------------------------------------------------------| | `dateTimeOffset` | The date and time (with UTC offset) to convert to a timestamp. | |
| **Returns** | The converted timestamp.                                                                                                                                                    |

### GetCurrentTimestamp

```c#
Timestamp Firebase::Firestore::Timestamp::GetCurrentTimestamp()
```  
Returns the current timestamp according to the system clock.

The system time zone is irrelevant, as a timestamp represents an instant in time.

<br />

|                              Details                              ||
|-------------|------------------------------------------------------|
| **Returns** | The current timestamp according to the system clock. |

### operator!=

```c#
bool Firebase::Firestore::Timestamp::operator!=(
  Timestamp lhs,
  Timestamp rhs
)
```  
Operator overload to compare two [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) values for inequality.

<br />

|                                                        Details                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------| | `lhs` | Left value to compare  | | `rhs` | Right value to compare | |
| **Returns** | `false` if *lhs* is equal to *rhs* ; otherwise `true`.                                                   |

### operator\<

```c#
bool Firebase::Firestore::Timestamp::operator<(
  Timestamp lhs,
  Timestamp rhs
)
```  
Compares two timestamps.

<br />

|                                                                     Details                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------| | `lhs` | The left timestamp to compare.  | | `rhs` | The right timestamp to compare. | |
| **Returns** | `true` if *lhs* is strictly earlier than *rhs* ; otherwise `false`.                                                                 |

### operator\<=

```c#
bool Firebase::Firestore::Timestamp::operator<=(
  Timestamp lhs,
  Timestamp rhs
)
```  
Compares two timestamps.

<br />

|                                                                     Details                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------| | `lhs` | The left timestamp to compare.  | | `rhs` | The right timestamp to compare. | |
| **Returns** | `true` if *lhs* is earlier than or equal to *rhs* ; otherwise `false`.                                                              |

### operator==

```c#
bool Firebase::Firestore::Timestamp::operator==(
  Timestamp lhs,
  Timestamp rhs
)
```  
Operator overload to compare two [Timestamp](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/timestamp#struct_firebase_1_1_firestore_1_1_timestamp) values for equality.

<br />

|                                                        Details                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------| | `lhs` | Left value to compare  | | `rhs` | Right value to compare | |
| **Returns** | `true` if *lhs* is equal to *rhs* ; otherwise `false`.                                                   |

### operator\>

```c#
bool Firebase::Firestore::Timestamp::operator>(
  Timestamp lhs,
  Timestamp rhs
)
```  
Compares two timestamps.

<br />

|                                                                     Details                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------| | `lhs` | The left timestamp to compare.  | | `rhs` | The right timestamp to compare. | |
| **Returns** | `true` if *lhs* is strictly later than *rhs* ; otherwise `false`.                                                                   |

### operator\>=

```c#
bool Firebase::Firestore::Timestamp::operator>=(
  Timestamp lhs,
  Timestamp rhs
)
```  
Compares two timestamps.

<br />

|                                                                     Details                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------| | `lhs` | The left timestamp to compare.  | | `rhs` | The right timestamp to compare. | |
| **Returns** | `true` if *lhs* is later than or equal to *rhs* ; otherwise `false`.                                                                |