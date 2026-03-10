# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint.md.txt

# FirebaseFirestore Framework Reference

# GeoPoint

    class GeoPoint : NSObject, NSCopying, @unchecked Sendable

An immutable object representing a geographical point in Firestore. The point is represented as
a latitude/longitude pair.

Latitude values are in the range of \[-90, 90\].
Longitude values are in the range of \[-180, 180\].
- `


  ### [init(latitude:longitude:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint#/c:objc(cs)FIRGeoPoint(im)initWithLatitude:longitude:)


  ` Creates a `GeoPoint` from the provided latitude and longitude degrees.

  #### Declaration

  Swift

      init(latitude: Double, longitude: Double)

  #### Parameters

  |---|---|
  | ` latitude ` | The latitude as number between -90 and 90. |
  | ` longitude ` | The longitude as number between -180 and 180. |

- `


  ### [latitude](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint#/c:objc(cs)FIRGeoPoint(py)latitude)


  ` The point's latitude. Must be a value between -90 and 90 (inclusive).

  #### Declaration

  Swift

      var latitude: Double { get }

- `


  ### [longitude](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint#/c:objc(cs)FIRGeoPoint(py)longitude)


  ` The point's longitude. Must be a value between -180 and 180 (inclusive).

  #### Declaration

  Swift

      var longitude: Double { get }