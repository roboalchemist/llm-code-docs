# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint.md.txt

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

|                                                                                                                                                                                         ### Public constructors                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GeoPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#GeoPoint(double,double))`(latitude: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`, longitude: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Construct a new `GeoPoint` using the provided latitude and longitude values. |

|                                ### Public functions                                |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)         | [compareTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#compareTo(com.google.firebase.firestore.GeoPoint))`(other: `[GeoPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint)`)` |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)`                                                          |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)         | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#hashCode())`()`                                                                                                                                                      |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)   | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#toString())`()`                                                                                                                                                      |

|                              ### Public properties                               |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | [latitude](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#latitude())   |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | [longitude](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint#longitude()) |

## Public constructors

### GeoPoint

```
GeoPoint(latitude:Â Double,Â longitude:Â Double)
```

Construct a new `GeoPoint` using the provided latitude and longitude values.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `latitude: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)  | The latitude of this `GeoPoint` in the range \[-90, 90\].    |
| `longitude: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The longitude of this `GeoPoint` in the range \[-180, 180\]. |

## Public functions

### compareTo

```
funÂ compareTo(other:Â GeoPoint):Â Int
```  

### equals

```
funÂ equals(o:Â Any?):Â Boolean
```  

### hashCode

```
funÂ hashCode():Â Int
```  

### toString

```
funÂ toString():Â String
```  

## Public properties

### latitude

```
valÂ latitude:Â Double
```  

### longitude

```
valÂ longitude:Â Double
```