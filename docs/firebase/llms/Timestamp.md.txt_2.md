# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp.md.txt

# firebase::Timestamp Class Reference

# firebase::Timestamp


`#include <timestamp.h>`

A [Timestamp](https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp) represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time.

## Summary

It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.


**See also:**
<https://github.com/google/protobuf/blob/main/src/google/protobuf/timestamp.proto>

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1ac32e672755662f1056f0f5adabac787c()` Creates a new timestamp representing the epoch (with seconds and nanoseconds set to 0). ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1aef76dce7a9ecf4c432e9cdebcd843893(int64_t seconds, int32_t nanoseconds)` Creates a new timestamp. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a4b16397af48b6b5c968573f2c00b7ab7(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & other)` Copy constructor, `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` is trivially copyable. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1ac96b74066e10d8a904448e8cdec1a162(https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp && other)` Move constructor, equivalent to copying. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a6f41b38da6d7a697f7f7f8605a8f2298() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a5b3fd853ad5481a49de3d754fd072397() const ` | `std::chrono::time_point< Clock, Duration >` Converts this `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` to a `time_point`. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1af55d711a07d2c85e64c1f2708bf42fb0() const ` | `int32_t` The non-negative fractions of a second at nanosecond resolution. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a3500b2ec2bd3fdb47ffe37fa2f446750(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp &` Copy assignment operator, `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` is trivially copyable. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1aaa02a0f9322ed5c6eac06f57253c321d(https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp && other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp &` Move assignment operator, equivalent to copying. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1ac6e68b9314b36ae2568403792b16432a() const ` | `int64_t` The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a2fa2c8d8b5821aff9c3f3a6752d87369(std::chrono::time_point< std::chrono::system_clock > time_point)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` Converts `std::chrono::time_point` to a `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp`. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a8bec4b207c51b44bfc5afea8302cc50f(time_t seconds_since_unix_epoch)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` Converts `time_t` to a `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp`. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a7667c46bfe64d56ec2aaf675069036a7()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` Creates a new timestamp with the current date. |

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1aadca358b802a709960a0425b597ae78e` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` to the given stream. |

## Public functions

### Timestamp

```c++
 Timestamp()=default
```
Creates a new timestamp representing the epoch (with seconds and nanoseconds set to 0).

### Timestamp

```c++
 Timestamp(
  int64_t seconds,
  int32_t nanoseconds
)
```
Creates a new timestamp.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `seconds` | The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive; otherwise, assertion failure will be triggered. | | `nanoseconds` | The non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanoseconds values that count forward in time. Must be from 0 to 999,999,999 inclusive; otherwise, assertion failure will be triggered. | |

### Timestamp

```c++
 Timestamp(
  const Timestamp & other
)=default
```
Copy constructor, `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` is trivially copyable.

### Timestamp

```c++
 Timestamp(
  Timestamp && other
)=default
```
Move constructor, equivalent to copying.

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` for logging/debugging purposes.


> [!NOTE]
> **Note:** : the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### ToTimePoint

```c++
std::chrono::time_point< Clock, Duration > ToTimePoint() const 
```
Converts this `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` to a `time_point`.

Important: if overflow would occur, the returned value will be the maximum or minimum value that `Duration` can hold. Note in particular that `long long` is insufficient to hold the full range of `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` values with nanosecond precision (which is why `Duration` defaults to `microseconds`).

### nanoseconds

```c++
int32_t nanoseconds() const 
```
The non-negative fractions of a second at nanosecond resolution.

Negative second values with fractions still have non-negative nanoseconds values that count forward in time.

### operator=

```c++
Timestamp & operator=(
  const Timestamp & other
)=default
```
Copy assignment operator, `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` is trivially copyable.

### operator=

```c++
Timestamp & operator=(
  Timestamp && other
)=default
```
Move assignment operator, equivalent to copying.

### seconds

```c++
int64_t seconds() const 
```
The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z.

## Public static functions

### FromTimePoint

```c++
Timestamp FromTimePoint(
  std::chrono::time_point< std::chrono::system_clock > time_point
)
```
Converts `std::chrono::time_point` to a `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `time_point` | The time point with system clock's epoch, which is presumed to be Unix epoch 1970-01-01T00:00:00Z. Can be negative to represent dates before the epoch. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive; otherwise, assertion failure will be triggered. Note that while the epoch of `std::chrono::system_clock` is unspecified, it's usually Unix epoch. If this assumption is broken, this constructor will produce incorrect results. | |

### FromTimeT

```c++
Timestamp FromTimeT(
  time_t seconds_since_unix_epoch
)
```
Converts `time_t` to a `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `seconds_since_unix_epoch` | The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Can be negative to represent dates before the epoch. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive; otherwise, assertion failure will be triggered. Note that while the epoch of `time_t` is unspecified, it's usually Unix epoch. If this assumption is broken, this function will produce incorrect results. | |
| **Returns** | a new timestamp with the given number of seconds and zero nanoseconds. |

### Now

```c++
Timestamp Now()
```
Creates a new timestamp with the current date.

The precision is up to nanoseconds, depending on the system clock.

<br />

| Details ||
|---|---|
| **Returns** | a new timestamp representing the current date. |

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const Timestamp &timestamp)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp_1a6f41b38da6d7a697f7f7f8605a8f2298` for comments on the representation format.