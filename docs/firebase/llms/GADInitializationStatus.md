# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInitializationStatus.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInitializationStatus.md.txt

# GoogleMobileAds Framework Reference

# GADInitializationStatus

    class GADInitializationStatus : NSObject, NSCopying

An immutable snapshot of the Google Mobile Ads SDK's initialization status, categorized by
mediation adapter.
- `
  ``
  ``
  `

  ### [adapterStatusesByClassName](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInitializationStatus#/c:objc(cs)GADInitializationStatus(py)adapterStatusesByClassName)

  `
  `  
  Initialization status of each ad network available to the Google Mobile Ads SDK, keyed by its
  GADMAdapter's class name. The list of available ad networks may be incomplete during early
  phases of SDK initialization.  

  #### Declaration

  Swift  

      var adapterStatusesByClassName: [String : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdapterStatus.html] { get }