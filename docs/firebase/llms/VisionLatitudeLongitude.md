# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionLatitudeLongitude.md.txt

# FirebaseMLVision Framework Reference

# VisionLatitudeLongitude

    class VisionLatitudeLongitude : NSObject

An object representing a latitude/longitude pair. This is expressed as a pair of doubles
representing degrees latitude and degrees longitude. Unless specified otherwise, this must
conform to the [WGS84
standard](http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf). Values must be within normalized ranges.
- `
  ``
  ``
  `

  ### [latitude](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(py)latitude)

  `
  `  
  The latitude in degrees. It must be in the range \[-90.0, +90.0\]. The value is double.  

  #### Declaration

  Swift  

      var latitude: NSNumber? { get set }

- `
  ``
  ``
  `

  ### [longitude](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(py)longitude)

  `
  `  
  The longitude in degrees. It must be in the range \[-180.0, +180.0\]. The value is double.  

  #### Declaration

  Swift  

      var longitude: NSNumber? { get set }

- `
  ``
  ``
  `

  ### [init(latitude:longitude:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(im)initWithLatitude:longitude:)

  `
  `  
  Initializes a VisionLatitudeLongitude with the given latitude and longitude.  

  #### Declaration

  Swift  

      init(latitude: NSNumber?, longitude: NSNumber?)

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

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionLatitudeLongitude#/c:objc(cs)FIRVisionLatitudeLongitude(im)init)

  `
  `  
  Unavailable.