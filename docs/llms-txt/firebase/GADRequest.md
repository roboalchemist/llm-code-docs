# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.md.txt

# GoogleMobileAds Framework Reference

# GADRequest

    class GADRequest : NSObject, NSCopying

Specifies optional parameters for ad requests.
- `
  ``
  ``
  `

  ### [+request](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(cm)request)

  `
  `  
Returns a default request.  
[## Additional Parameters For Ad Networks](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/Additional%20Parameters%20For%20Ad%20Networks)

- `
  ``
  ``
  `

  ### [register(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(im)registerAdNetworkExtras:)

  `
  `  
  Ad networks may have additional parameters they accept. To pass these parameters to them, create
  the ad network extras object for that network, fill in the parameters, and register it here. The
  ad network should have a header defining the interface for the 'extras' object to create. All
  networks will have access to the basic settings you've set in this GADRequest. If you register
  an extras object that is the same class as one you have registered before, the previous extras
  will be overwritten.  

  #### Declaration

  Swift  

      func register(_ extras: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras)

- `
  ``
  ``
  `

  ### [adNetworkExtras(for:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(im)adNetworkExtrasFor:)

  `
  `  
  Returns the network extras defined for an ad network.  

  #### Declaration

  Swift  

      func adNetworkExtras(for aClass: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras.Type) -> https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras?

- `
  ``
  ``
  `

  ### [removeAdNetworkExtras(for:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(im)removeAdNetworkExtrasFor:)

  `
  `  
  Removes the extras for an ad network. \|aClass\| is the class which represents that network's
  extras type.  

  #### Declaration

  Swift  

      func removeAdNetworkExtras(for aClass: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras.Type)

[## Collecting SDK Information](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/Collecting%20SDK%20Information)

- `
  ``
  ``
  `

  ### [sdkVersion()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(cm)sdkVersion)

  `
  `  
  Returns the version of the SDK.  

  #### Declaration

  Swift  

      class func sdkVersion() -> String

[## Testing](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/Testing)

- `
  ``
  ``
  `

  ### [testDevices](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(py)testDevices)

  `
  `  
  Test ads will be returned for devices with device IDs specified in this array.  

  #### Declaration

  Swift  

      var testDevices: [Any]? { get set }

[## User Information](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/User%20Information)

- `
  ``
  ``
  `

  ### [setLocationWithLatitude(_:longitude:accuracy:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(im)setLocationWithLatitude:longitude:accuracy:)

  `
  `  
  The user's current location may be used to deliver more relevant ads. However do not use Core
  Location just for advertising, make sure it is used for more beneficial reasons as well. It is
  both a good idea and part of Apple's guidelines.  

  #### Declaration

  Swift  

      func setLocationWithLatitude(_ latitude: CGFloat, longitude: CGFloat, accuracy accuracyInMeters: CGFloat)

[## Contextual Information](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/Contextual%20Information)

- `
  ``
  ``
  `

  ### [keywords](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(py)keywords)

  `
  `  
  Array of keyword strings. Keywords are words or phrases describing the current user activity
  such as @Sports Scores or @Football. Set this property to nil to clear the keywords.  

  #### Declaration

  Swift  

      var keywords: [Any]? { get set }

- `
  ``
  ``
  `

  ### [contentURL](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(py)contentURL)

  `
  `  
  URL string for a webpage whose content matches the app content. This webpage content is used for
  targeting purposes.  

  #### Declaration

  Swift  

      var contentURL: String? { get set }

[## Request Agent Information](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/Request%20Agent%20Information)

- `
  ``
  ``
  `

  ### [requestAgent](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(py)requestAgent)

  `
  `  
  String that identifies the ad request's origin. Third party libraries that reference the Mobile
  Ads SDK should set this property to denote the platform from which the ad request originated.
  For example, a third party ad network called CoolAds network that is mediating requests to the
  Mobile Ads SDK should set this property as CoolAds.  

  #### Declaration

  Swift  

      var requestAgent: String? { get set }

[## Deprecated Methods](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/Deprecated%20Methods)

- `
  ``
  ``
  `

  ### [gender](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(py)gender)

  `
  `  
  Deprecated property. The user's gender.  

  #### Declaration

  Swift  

      var gender: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADGender.html { get set }

- `
  ``
  ``
  `

  ### [birthday](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(py)birthday)

  `
  `  
  Deprecated property. The user's birthday.  

  #### Declaration

  Swift  

      var birthday: Date? { get set }

- `
  ``
  ``
  `

  ### [setBirthdayWithMonth(_:day:year:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(im)setBirthdayWithMonth:day:year:)

  `
  `  
  Provide the user's birthday to increase ad relevancy.  

  #### Declaration

  Swift  

      func setBirthdayWithMonth(_ month: Int, day: Int, year: Int)

- `
  ``
  ``
  `

  ### [setLocationWithDescription(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(im)setLocationWithDescription:)

  `
  `  
  When Core Location isn't available but the user's location is known, supplying it here may
  deliver more relevant ads. It can be any free-form text such as @Champs-Elysees Paris or
  @94041 US.  

  #### Declaration

  Swift  

      func setLocationWithDescription(_ locationDescription: String?)

- `
  ``
  ``
  `

  ### [tag(forChildDirectedTreatment:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest#/c:objc(cs)GADRequest(im)tagForChildDirectedTreatment:)

  `
  `  
  \[Optional\] This method allows you to specify whether you would like your app to be treated as
  child-directed for purposes of the Children's Online Privacy Protection Act (COPPA),
  <http://business.ftc.gov/privacy-and-security/childrens-privacy>.

  If you call this method with YES, you are indicating that your app should be treated as
  child-directed for purposes of the Children's Online Privacy Protection Act (COPPA). If you call
  this method with NO, you are indicating that your app should not be treated as child-directed
  for purposes of the Children's Online Privacy Protection Act (COPPA). If you do not call this
  method, ad requests will include no indication of how you would like your app treated with
  respect to COPPA.

  By setting this method, you certify that this notification is accurate and you are authorized to
  act on behalf of the owner of the app. You understand that abuse of this setting may result in
  termination of your Google account.

  It may take some time for this designation to be fully implemented in applicable Google
  services. This designation will only apply to ad requests for which you have set this method.  

  #### Declaration

  Swift  

      func tag(forChildDirectedTreatment childDirectedTreatment: Bool)