# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint.md.txt

# GeoPoint

# GeoPoint


```
class GeoPoint : Comparable
```

<br />

*** ** * ** ***

Immutable class representing a `GeoPoint` in Cloud Firestore

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#GeoPoint(double,double)(latitude: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, longitude: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Construct a new `GeoPoint` using the provided latitude and longitude values. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#compareTo(com.google.firebase.firestore.GeoPoint)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#toString()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#latitude()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#longitude()` |

## Public constructors

### GeoPoint

```
GeoPoint(latitude: Double, longitude: Double)
```

Construct a new `GeoPoint` using the provided latitude and longitude values.

| Parameters |
|---|---|
| `latitude: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The latitude of this `GeoPoint` in the range \[-90, 90\]. |
| `longitude: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The longitude of this `GeoPoint` in the range \[-180, 180\]. |

## Public functions

### compareTo

```
fun compareTo(other: GeoPoint): Int
```

### equals

```
fun equals(o: Any?): Boolean
```

### hashCode

```
fun hashCode(): Int
```

### toString

```
fun toString(): String
```

## Public properties

### latitude

```
val latitude: Double
```

### longitude

```
val longitude: Double
```