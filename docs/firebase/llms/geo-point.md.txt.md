# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point.md.txt

# firebase::firestore::GeoPoint Class Reference

# firebase::firestore::GeoPoint


`#include <geo_point.h>`

An immutable object representing a geographical point in [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore).

## Summary

The point is represented as a latitude/longitude pair.

Latitude values are in the range of \[-90, 90\]. Longitude values are in the range of \[-180, 180\].

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1abeaa0258595983ace6e0c0a833272a32()` Creates a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` with both latitude and longitude set to 0. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1af75b37aa89a82c258ff670313b563e49(double latitude, double longitude)` Creates a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` from the provided latitude and longitude values. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1a0ec4d648318c335388b14e7878aa5070(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point & other)` Copy constructor, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` is trivially copyable. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1a2e6c4a10f17fcb0bcce7836dff813755(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point && other)` Move constructor, equivalent to copying. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1ab4704568b6f925a4fcc825cce5285d58() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1a161b2857f46a46f9e1f4c94ae493d776() const ` | `double` Returns the latitude value of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point`. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1a52f379541316f6ad12fc8b7e6b5b5725() const ` | `double` Returns the latitude value of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point`. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1a2c0be427f41b902e156009e0962ee612(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point & other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point &` Copy assignment operator, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` is trivially copyable. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1ae1b1e4f4c167ef3b1b2889c0b2225f01(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point && other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point &` Move assignment operator, equivalent to copying. |

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1a3c417a204df76e7ba637858a24c22006` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` to the given stream. |

## Public functions

### GeoPoint

```c++
 GeoPoint()=default
```
Creates a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` with both latitude and longitude set to 0.

### GeoPoint

```c++
 GeoPoint(
  double latitude,
  double longitude
)
```
Creates a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` from the provided latitude and longitude values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `latitude` | The latitude as number of degrees between -90 and 90. | | `longitude` | The longitude as number of degrees between -180 and 180. | |

### GeoPoint

```c++
 GeoPoint(
  const GeoPoint & other
)=default
```
Copy constructor, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` is trivially copyable.

### GeoPoint

```c++
 GeoPoint(
  GeoPoint && other
)=default
```
Move constructor, equivalent to copying.

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` for logging/debugging purposes.


> [!NOTE]
> **Note:** : the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### latitude

```c++
double latitude() const 
```
Returns the latitude value of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point`.

### longitude

```c++
double longitude() const 
```
Returns the latitude value of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point`.

### operator=

```c++
GeoPoint & operator=(
  const GeoPoint & other
)=default
```
Copy assignment operator, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` is trivially copyable.

### operator=

```c++
GeoPoint & operator=(
  GeoPoint && other
)=default
```
Move assignment operator, equivalent to copying.

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const GeoPoint &geo_point)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point_1ab4704568b6f925a4fcc825cce5285d58` for comments on the representation format.