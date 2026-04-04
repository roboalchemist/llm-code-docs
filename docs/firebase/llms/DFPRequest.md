# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPRequest.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPRequest.md.txt

# GoogleMobileAds Framework Reference

# DFPRequest

    class DFPRequest : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.html

Specifies optional parameters for ad requests.
- `
  ``
  ``
  `

  ### [publisherProvidedID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(py)publisherProvidedID)

  `
  `  
  Publisher provided user ID.  

  #### Declaration

  Swift  

      var publisherProvidedID: String? { get set }

- `
  ``
  ``
  `

  ### [categoryExclusions](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(py)categoryExclusions)

  `
  `  
  Array of strings used to exclude specified categories in ad results.  

  #### Declaration

  Swift  

      var categoryExclusions: [Any]? { get set }

- `
  ``
  ``
  `

  ### [customTargeting](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(py)customTargeting)

  `
  `  
  Key-value pairs used for custom targeting.  

  #### Declaration

  Swift  

      var customTargeting: [AnyHashable : Any]? { get set }

- `
  ``
  ``
  `

  ### [updateCorrelator()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPRequest#/c:objc(cs)DFPRequest(cm)updateCorrelator)

  `
  `  
  This API is deprecated and has no effect. Use an instance of GADCorrelator with DFPInterstitial
  or DFPBannerView objects to correlate requests.  

  #### Declaration

  Swift  

      class func updateCorrelator()