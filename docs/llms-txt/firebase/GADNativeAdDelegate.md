# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAdDelegate

    protocol GADNativeAdDelegate : NSObjectProtocol

Identifies native ad assets.
[## Ad Lifecycle Events](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/Ad%20Lifecycle%20Events)

- `
  ``
  ``
  `

  ### [nativeAdDidRecordImpression(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdDidRecordImpression:)

  `
  `  
  Called when an impression is recorded for an ad. Only called for Google ads and is not supported
  for mediation ads.  

  #### Declaration

  Swift  

      optional func nativeAdDidRecordImpression(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdDidRecordClick(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdDidRecordClick:)

  `
  `  
  Called when a click is recorded for an ad. Only called for Google ads and is not supported for
  mediation ads.  

  #### Declaration

  Swift  

      optional func nativeAdDidRecordClick(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html)

[## Click-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/Click-Time%20Lifecycle%20Notifications)

- `
  ``
  ``
  `

  ### [nativeAdWillPresentScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdWillPresentScreen:)

  `
  `  
  Called just before presenting the user a full screen view, such as a browser, in response to
  clicking on an ad. Use this opportunity to stop animations, time sensitive interactions, etc.

  Normally the user looks at the ad, dismisses it, and control returns to your application with
  the nativeAdDidDismissScreen: message. However, if the user hits the Home button or clicks on an
  App Store link, your application will end. The next method called will be the
  applicationWillResignActive: of your UIApplicationDelegate object.Immediately after that,
  nativeAdWillLeaveApplication: is called.  

  #### Declaration

  Swift  

      optional func nativeAdWillPresentScreen(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdWillDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdWillDismissScreen:)

  `
  `  
  Called just before dismissing a full screen view.  

  #### Declaration

  Swift  

      optional func nativeAdWillDismissScreen(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdDidDismissScreen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdDidDismissScreen:)

  `
  `  
  Called just after dismissing a full screen view. Use this opportunity to restart anything you
  may have stopped as part of nativeAdWillPresentScreen:.  

  #### Declaration

  Swift  

      optional func nativeAdDidDismissScreen(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html)

- `
  ``
  ``
  `

  ### [nativeAdWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdWillLeaveApplication:)

  `
  `  
  Called just before the application will go to the background or terminate due to an ad action
  that will launch another application (such as the App Store). The normal UIApplicationDelegate
  methods, like applicationDidEnterBackground:, will be called immediately before this.  

  #### Declaration

  Swift  

      optional func nativeAdWillLeaveApplication(_ nativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADNativeAd.html)