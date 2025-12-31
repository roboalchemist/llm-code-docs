# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerViewOptions.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPBannerViewOptions.md.txt

# GoogleMobileAds Framework Reference

# DFPBannerViewOptions

    class DFPBannerViewOptions : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions

Ad loader options for banner ads.
- `
  ``
  ``
  `

  ### [appEventDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPBannerViewOptions#/c:objc(cs)DFPBannerViewOptions(py)appEventDelegate)

  `
  `  
  Optional delegate that is notified if the loaded banner sends app events.  

  #### Declaration

  Swift  

      weak var appEventDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAppEventDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [adSizeDelegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPBannerViewOptions#/c:objc(cs)DFPBannerViewOptions(py)adSizeDelegate)

  `
  `  
  Optional delegate that is notified if the loaded banner changes size.  

  #### Declaration

  Swift  

      weak var adSizeDelegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdSizeDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [enableManualImpressions](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPBannerViewOptions#/c:objc(cs)DFPBannerViewOptions(py)enableManualImpressions)

  `
  `  
  Whether the publisher will record impressions manually when the ad becomes visible to the user.  

  #### Declaration

  Swift  

      var enableManualImpressions: Bool { get set }