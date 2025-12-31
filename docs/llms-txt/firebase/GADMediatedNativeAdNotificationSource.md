# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeAdNotificationSource

    class GADMediatedNativeAdNotificationSource : NSObject

Notifies the Google Mobile Ads SDK about the events performed by adapters. Adapters may perform
some action (e.g. opening an in app browser or opening the iTunes store) when handling callbacks
from GADMediatedNativeAdDelegate. Adapters in such case should notify the Google Mobile Ads SDK
by calling the relevant methods from this class.
- `
  ``
  ``
  `

  ### [mediatedNativeAdDidRecordImpression(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdDidRecordImpression:)

  `
  `  
  Called by the adapter when it has registered an impression on the tracked view. Adapter should
  only call this method if -\[GADMAdNetworkAdapter handlesUserImpressions\] returns YES.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidRecordImpression(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidRecordClick(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdDidRecordClick:)

  `
  `  
  Called by the adapter when it has registered a user click on the tracked view. Adapter should
  only call this method if -\[GADMAdNetworkAdapter handlesUserClicks\] returns YES.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidRecordClick(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdWillPresentScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdWillPresentScreen:)

  `
  `  
  Must be called by the adapter just before mediatedNativeAd has opened an in-app modal screen.  

  #### Declaration

  Swift  

      class func mediatedNativeAdWillPresentScreen(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdWillDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdWillDismissScreen:)

  `
  `  
  Must be called by the adapter just before the in-app modal screen opened by mediatedNativeAd is
  dismissed.  

  #### Declaration

  Swift  

      class func mediatedNativeAdWillDismissScreen(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdDidDismissScreen:)

  `
  `  
  Must be called by the adapter after the in-app modal screen opened by mediatedNativeAd is
  dismissed.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidDismissScreen(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdWillLeaveApplication:)

  `
  `  
  Must be called by the adapter just before mediatedNativeAd leaves the application.  

  #### Declaration

  Swift  

      class func mediatedNativeAdWillLeaveApplication(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

[## Mediated Native Video Ad Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/Mediated%20Native%20Video%20Ad%20Notifications)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidPlayVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdDidPlayVideo:)

  `
  `  
  Called by the adapter when native video playback has begun or resumed.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidPlayVideo(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidPauseVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdDidPauseVideo:)

  `
  `  
  Called by the adapter when native video playback has paused.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidPauseVideo(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidEndVideoPlayback(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedNativeAdNotificationSource#/c:objc(cs)GADMediatedNativeAdNotificationSource(cm)mediatedNativeAdDidEndVideoPlayback:)

  `
  `  
  Called by the adapter when native video playback has ended.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidEndVideoPlayback(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)