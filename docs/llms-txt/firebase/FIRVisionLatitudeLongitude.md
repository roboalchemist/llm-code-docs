# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionLatitudeLongitude.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionLatitudeLongitude


    @interface FIRVisionLatitudeLongitude : NSObject

An object representing a latitude/longitude pair. This is expressed as a pair of doubles
representing degrees latitude and degrees longitude. Unless specified otherwise, this must
conform to the [WGS84
standard](http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf). Values must be within normalized ranges.
- `
  ``
  ``
  `

  ### [latitude](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(py)latitude)

  `
  `  
  The latitude in degrees. It must be in the range \[-90.0, +90.0\]. The value is double.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) NSNumber *latitude;

- `
  ``
  ``
  `

  ### [longitude](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(py)longitude)

  `
  `  
  The longitude in degrees. It must be in the range \[-180.0, +180.0\]. The value is double.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) NSNumber *longitude;

- `
  ``
  ``
  `

  ### [-initWithLatitude:longitude:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(im)initWithLatitude:longitude:)

  `
  `  
  Initializes a VisionLatitudeLongitude with the given latitude and longitude.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithLatitude:(nullable NSNumber *)latitude
                                     longitude:(nullable NSNumber *)longitude;

  #### Parameters

  |-------------------|-------------------------------------------------|
  | ` `*latitude*` `  | Latitude of the location. The value is double.  |
  | ` `*longitude*` ` | Longitude of the location. The value is double. |

  #### Return Value

  A VisionLatitudeLongitude instance with the given latigude and longitude.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;