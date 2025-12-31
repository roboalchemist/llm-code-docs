# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventRequest.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventRequest

    class GADCustomEventRequest : NSObject

Specifies optional ad request targeting parameters that are provided by the publisher and are
forwarded to custom events for purposes of populating an ad request to a 3rd party ad network.
- `
  ``
  ``
  `

  ### [userHasLocation](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userHasLocation)

  `
  `  
  If the user's latitude, longitude, and accuracy are not specified, userHasLocation returns NO,
  and userLatitude, userLongitude, and userLocationAccuracyInMeters return 0.  

  #### Declaration

  Swift  

      var userHasLocation: Bool { get }

- `
  ``
  ``
  `

  ### [userLatitude](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userLatitude)

  `
  `  
  User's latitude set in GADRequest.  

  #### Declaration

  Swift  

      var userLatitude: CGFloat { get }

- `
  ``
  ``
  `

  ### [userLongitude](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userLongitude)

  `
  `  
  User's longitude set in GADRequest.  

  #### Declaration

  Swift  

      var userLongitude: CGFloat { get }

- `
  ``
  ``
  `

  ### [userLocationAccuracyInMeters](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userLocationAccuracyInMeters)

  `
  `  
  The accuracy, in meters, of the user's location data.  

  #### Declaration

  Swift  

      var userLocationAccuracyInMeters: CGFloat { get }

- `
  ``
  ``
  `

  ### [userLocationDescription](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userLocationDescription)

  `
  `  
  Description of the user's location, in free form text, set in GADRequest. If not available,
  returns nil. This may be set even if userHasLocation is NO.  

  #### Declaration

  Swift  

      var userLocationDescription: String? { get }

- `
  ``
  ``
  `

  ### [userKeywords](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userKeywords)

  `
  `  
  Keywords set in GADRequest. Returns nil if no keywords are set.  

  #### Declaration

  Swift  

      var userKeywords: [Any]? { get }

- `
  ``
  ``
  `

  ### [additionalParameters](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)additionalParameters)

  `
  `  
  The additional parameters set by the application. This property allows you to pass additional
  information from your application to your Custom Event object. To do so, create an instance of
  GADCustomEventExtras to pass to GADRequest -registerAdNetworkExtras:. The instance should have
  an NSDictionary set for a particular custom event label. That NSDictionary becomes the
  additionalParameters here.  

  #### Declaration

  Swift  

      var additionalParameters: [AnyHashable : Any]? { get }

- `
  ``
  ``
  `

  ### [isTesting](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)isTesting)

  `
  `  
  Indicates whether the testing property has been set in GADRequest.  

  #### Declaration

  Swift  

      var isTesting: Bool { get }

[## Deprecated methods](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/Deprecated%20methods)

- `
  ``
  ``
  `

  ### [userGender](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userGender)

  `
  `  
  Deprecated. User's gender set in GADRequest. If not specified, returns kGADGenderUnknown.  

  #### Declaration

  Swift  

      var userGender: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADGender.html { get }

- `
  ``
  ``
  `

  ### [userBirthday](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADCustomEventRequest#/c:objc(cs)GADCustomEventRequest(py)userBirthday)

  `
  `  
  Deprecated. User's birthday set in GADRequest. If not specified, returns nil.  

  #### Declaration

  Swift  

      var userBirthday: Date? { get }