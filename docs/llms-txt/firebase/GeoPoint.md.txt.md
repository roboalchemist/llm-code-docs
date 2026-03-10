# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint.md.txt

# GeoPoint

# GeoPoint


```
public class GeoPoint implements Comparable
```

<br />

*** ** * ** ***

Immutable class representing a `GeoPoint` in Cloud Firestore

## Summary

| ### Public fields |
|---|---|
| `final double` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#latitude()` |
| `final double` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#longitude()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#GeoPoint(double,double)(double latitude, double longitude)` Construct a new `GeoPoint` using the provided latitude and longitude values. |

| ### Public methods |
|---|---|
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#compareTo(com.google.firebase.firestore.GeoPoint)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint other)` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `double` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#getLatitude()()` |
| `double` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#getLongitude()()` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint#toString()()` |

## Public fields

### latitude

```
public final double latitude
```

### longitude

```
public final double longitude
```

## Public constructors

### GeoPoint

```
public GeoPoint(double latitude, double longitude)
```

Construct a new `GeoPoint` using the provided latitude and longitude values.

| Parameters |
|---|---|
| `double latitude` | The latitude of this `GeoPoint` in the range \[-90, 90\]. |
| `double longitude` | The longitude of this `GeoPoint` in the range \[-180, 180\]. |

## Public methods

### compareTo

```
public int compareTo(@NonNull GeoPoint other)
```

### equals

```
public boolean equals(@Nullable Object o)
```

### getLatitude

```
public double getLatitude()
```

| Returns |
|---|---|
| `double` | The latitude value of this `GeoPoint`. |

### getLongitude

```
public double getLongitude()
```

| Returns |
|---|---|
| `double` | The longitude value of this `GeoPoint`. |

### hashCode

```
public int hashCode()
```

### toString

```
public @NonNull String toString()
```