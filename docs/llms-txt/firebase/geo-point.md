# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point.md.txt

# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point.md.txt

# Firebase.Firestore.GeoPoint Struct Reference

# Firebase.Firestore.GeoPoint

Immutable struct representing a geographic location in Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore).

## Summary

### Inheritance

Inherits from: IEquatable\< GeoPoint \>

| ### Constructors and Destructors ||
|---|---|
| [GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1a71f80013c8b159efd2080abcef3c08bc)`(double latitude, double longitude)` Creates a new value using the provided latitude and longitude values. ||

|                                                                                                                      ### Properties                                                                                                                       ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [Latitude](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1a8f8d88f505922cbdbcffbf25d4cd758f)  | `double` The latitude, in degrees, in the range -90 to 90 inclusive.    |
| [Longitude](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1ac76f10ef21dada2e6ef85b72f0f87d8e) | `double` The longitude, in degrees, in the range -180 to 180 inclusive. |

|                                                                                                                                                                   ### Public functions                                                                                                                                                                   ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1aabeded90cf8cbd37f0aee7091173676b)`(object obj)`                                                                                                                                           | `override bool`   |
| [Equals](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1a10d7ec49a069e70538babaab8e3becd4)`(`[GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point)` other)` | `bool`            |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1a1e5242377fc00fc34aeae393e9071ebf)`()`                                                                                                                                                | `override int`    |
| [ToString](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1a31c8e9a05cab86b397b61205c0b05c16)`()`                                                                                                                                                   | `override string` |

|                                                                                                                                                                                                                                                                                                                                       ### Public static functions                                                                                                                                                                                                                                                                                                                                        ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [operator!=](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1aad9eb40217f69d39a7dc5b4b2f9b5dd0)`(`[GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point)` lhs, `[GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point)` rhs)` | `bool` Operator overload to compare two [GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point) values for inequality. |
| [operator==](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point_1af92ad8a79be0e235cdec98f8f4407807)`(`[GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point)` lhs, `[GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point)` rhs)` | `bool` Operator overload to compare two [GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point) values for equality.   |

## Properties

### Latitude

```c#
double Firebase::Firestore::GeoPoint::Latitude
```  
The latitude, in degrees, in the range -90 to 90 inclusive.  

### Longitude

```c#
double Firebase::Firestore::GeoPoint::Longitude
```  
The longitude, in degrees, in the range -180 to 180 inclusive.

## Public functions

### Equals

```c#
override bool Firebase::Firestore::GeoPoint::Equals(
  object obj
)
```  

### Equals

```c#
bool Firebase::Firestore::GeoPoint::Equals(
  GeoPoint other
)
```  

### GeoPoint

```c#
 Firebase::Firestore::GeoPoint::GeoPoint(
  double latitude,
  double longitude
)
```  
Creates a new value using the provided latitude and longitude values.

<br />

|                                                                                                                                        Details                                                                                                                                         ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------|------------------------------------------------------------------------| | `latitude`  | The latitude of the point in degrees, between -90 and 90 inclusive.    | | `longitude` | The longitude of the point in degrees, between -180 and 180 inclusive. | |

### GetHashCode

```c#
override int Firebase::Firestore::GeoPoint::GetHashCode()
```  

### ToString

```c#
override string Firebase::Firestore::GeoPoint::ToString()
```  

## Public static functions

### operator!=

```c#
bool Firebase::Firestore::GeoPoint::operator!=(
  GeoPoint lhs,
  GeoPoint rhs
)
```  
Operator overload to compare two [GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point) values for inequality.

<br />

|                                                        Details                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------| | `lhs` | Left value to compare  | | `rhs` | Right value to compare | |
| **Returns** | `false` if *lhs* is equal to *rhs* ; otherwise `true`.                                                   |

### operator==

```c#
bool Firebase::Firestore::GeoPoint::operator==(
  GeoPoint lhs,
  GeoPoint rhs
)
```  
Operator overload to compare two [GeoPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/firestore/geo-point#struct_firebase_1_1_firestore_1_1_geo_point) values for equality.

<br />

|                                                        Details                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------| | `lhs` | Left value to compare  | | `rhs` | Right value to compare | |
| **Returns** | `true` if *lhs* is equal to *rhs* ; otherwise `false`.                                                   |