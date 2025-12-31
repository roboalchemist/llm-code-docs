# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedUnifiedNativeAdNotificationSource

    class GADMediatedUnifiedNativeAdNotificationSource : NSObject

Notifies the Google Mobile Ads SDK about the events performed by adapters. Adapters may perform
some action (e.g. opening an in app browser or opening the iTunes store) when handling methods
in GADMediatedUnifiedNativeAd. Adapters in such case should notify the Google Mobile Ads SDK by
calling the relevant methods from this class.
- `
  ``
  ``
  `

  ### [mediatedNativeAdDidRecordImpression(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidRecordImpression:)

  `
  `  
  Called by the adapter when it has registered an impression on the tracked view. Adapter should
  only call this method if -\[GADMAdNetworkAdapter handlesUserImpressions\] returns YES.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidRecordImpression(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidRecordClick(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidRecordClick:)

  `
  `  
  Called by the adapter when it has registered a user click on the tracked view. Adapter should
  only call this method if -\[GADMAdNetworkAdapter handlesUserClicks\] returns YES.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidRecordClick(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdWillPresentScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdWillPresentScreen:)

  `
  `  
  Must be called by the adapter just before mediatedNativeAd has opened an in-app modal screen.  

  #### Declaration

  Swift  

      class func mediatedNativeAdWillPresentScreen(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdWillDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdWillDismissScreen:)

  `
  `  
  Must be called by the adapter just before the in-app modal screen opened by mediatedNativeAd is
  dismissed.  

  #### Declaration

  Swift  

      class func mediatedNativeAdWillDismissScreen(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidDismissScreen:)

  `
  `  
  Must be called by the adapter after the in-app modal screen opened by mediatedNativeAd is
  dismissed.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidDismissScreen(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdWillLeaveApplication:)

  `
  `  
  Must be called by the adapter just before mediatedNativeAd leaves the application.  

  #### Declaration

  Swift  

      class func mediatedNativeAdWillLeaveApplication(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

[## Mediated Native Video Ad Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/Mediated%20Native%20Video%20Ad%20Notifications)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidPlayVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidPlayVideo:)

  `
  `  
  Called by the adapter when native video playback has begun or resumed.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidPlayVideo(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidPauseVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidPauseVideo:)

  `
  `  
  Called by the adapter when native video playback has paused.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidPauseVideo(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [mediatedNativeAdDidEndVideoPlayback(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidEndVideoPlayback:)

  `
  `  
  Called by the adapter when native video playback has ended.  

  #### Declaration

  Swift  

      class func mediatedNativeAdDidEndVideoPlayback(_ mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)