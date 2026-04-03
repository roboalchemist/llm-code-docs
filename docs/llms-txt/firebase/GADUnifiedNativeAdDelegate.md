# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADUnifiedNativeAdDelegate

    protocol GADUnifiedNativeAdDelegate : NSObjectProtocol

Identifies native ad assets.
[## Ad Lifecycle Events](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/Ad%20Lifecycle%20Events)

- `
  ``
  ``
  `

  ### [nativeAdDidRecordImpression(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/c:objc(pl)GADUnifiedNativeAdDelegate(im)nativeAdDidRecordImpression:)

  `
  `  
  Called when an impression is recorded for an ad. Only called for Google ads and is not supported
  for mediated ads.  

  #### Declaration

  Swift  

      optional func nativeAdDidRecordImpression(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdDidRecordClick(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/c:objc(pl)GADUnifiedNativeAdDelegate(im)nativeAdDidRecordClick:)

  `
  `  
  Called when a click is recorded for an ad. Only called for Google ads and is not supported for
  mediated ads.  

  #### Declaration

  Swift  

      optional func nativeAdDidRecordClick(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)

[## Click-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/Click-Time%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [nativeAdWillPresentScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/c:objc(pl)GADUnifiedNativeAdDelegate(im)nativeAdWillPresentScreen:)

  `
  `  
  Called before presenting the user a full screen view in response to an ad action. Use this
  opportunity to stop animations, time sensitive interactions, etc.

  Normally the user looks at the ad, dismisses it, and control returns to your application with
  the nativeAdDidDismissScreen: message. However, if the user hits the Home button or clicks on an
  App Store link, your application will be backgrounded. The next method called will be the
  applicationWillResignActive: of your UIApplicationDelegate object. Immediately after that,
  nativeAdWillLeaveApplication: is called.  

  #### Declaration

  Swift  

      optional func nativeAdWillPresentScreen(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdWillDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/c:objc(pl)GADUnifiedNativeAdDelegate(im)nativeAdWillDismissScreen:)

  `
  `  
  Called before dismissing a full screen view.  

  #### Declaration

  Swift  

      optional func nativeAdWillDismissScreen(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdDidDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/c:objc(pl)GADUnifiedNativeAdDelegate(im)nativeAdDidDismissScreen:)

  `
  `  
  Called after dismissing a full screen view. Use this opportunity to restart anything you may
  have stopped as part of nativeAdWillPresentScreen:.  

  #### Declaration

  Swift  

      optional func nativeAdDidDismissScreen(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/c:objc(pl)GADUnifiedNativeAdDelegate(im)nativeAdWillLeaveApplication:)

  `
  `  
  Called before the application will go to the background or terminate due to an ad action that
  will launch another application (such as the App Store). The normal UIApplicationDelegate
  methods, like applicationDidEnterBackground:, will be called immediately before this.  

  #### Declaration

  Swift  

      optional func nativeAdWillLeaveApplication(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)

[## Mute This Ad](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/Mute%20This%20Ad)

- `
  ``
  ``
  `

  ### [nativeAdIsMuted(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADUnifiedNativeAdDelegate#/c:objc(pl)GADUnifiedNativeAdDelegate(im)nativeAdIsMuted:)

  `
  `  
  Used for Mute This Ad feature. Called after the native ad is muted. Only called for Google ads
  and is not supported for mediated ads.  

  #### Declaration

  Swift  

      optional func nativeAdIsMuted(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADUnifiedNativeAd.html)