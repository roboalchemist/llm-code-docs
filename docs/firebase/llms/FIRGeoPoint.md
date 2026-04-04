# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRGeoPoint.md.txt

# FirebaseFirestore Framework Reference

# FIRGeoPoint


    @interface FIRGeoPoint : NSObject <NSCopying>

An immutable object representing a geographical point in Firestore. The point is represented as
a latitude/longitude pair.

Latitude values are in the range of \[-90, 90\].
Longitude values are in the range of \[-180, 180\].
- `
  ``
  ``
  `

  ### [-initWithLatitude:longitude:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRGeoPoint#/c:objc(cs)FIRGeoPoint(im)initWithLatitude:longitude:)

  `
  `  
  Creates a `GeoPoint` from the provided latitude and longitude degrees.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithLatitude:(double)latitude
                                     longitude:(double)longitude;

  #### Parameters

  |-------------------|-----------------------------------------------|
  | ` `*latitude*` `  | The latitude as number between -90 and 90.    |
  | ` `*longitude*` ` | The longitude as number between -180 and 180. |

- `
  ``
  ``
  `

  ### [latitude](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRGeoPoint#/c:objc(cs)FIRGeoPoint(py)latitude)

  `
  `  
  The point's latitude. Must be a value between -90 and 90 (inclusive).  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) double latitude;

- `
  ``
  ``
  `

  ### [longitude](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRGeoPoint#/c:objc(cs)FIRGeoPoint(py)longitude)

  `
  `  
  The point's longitude. Must be a value between -180 and 180 (inclusive).  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) double longitude;