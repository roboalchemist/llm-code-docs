# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeAdDelegate

    @protocol GADNativeAdDelegate <NSObject>

Identifies native ad assets.
[## Ad Lifecycle Events](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/Ad%20Lifecycle%20Events)

- `


  ### [-nativeAdDidRecordImpression:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdDidRecordImpression:)


  ` Called when an impression is recorded for an ad. Only called for Google ads and is not supported
  for mediation ads.

  #### Declaration

  Objective-C

      - (void)nativeAdDidRecordImpression:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html *)nativeAd;

- `


  ### [-nativeAdDidRecordClick:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdDidRecordClick:)


  ` Called when a click is recorded for an ad. Only called for Google ads and is not supported for
  mediation ads.

  #### Declaration

  Objective-C

      - (void)nativeAdDidRecordClick:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html *)nativeAd;

[## Click-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/Click-Time%20Lifecycle%20Notifications)

- `


  ### [-nativeAdWillPresentScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdWillPresentScreen:)


  ` Called just before presenting the user a full screen view, such as a browser, in response to
  clicking on an ad. Use this opportunity to stop animations, time sensitive interactions, etc.

  Normally the user looks at the ad, dismisses it, and control returns to your application with
  the nativeAdDidDismissScreen: message. However, if the user hits the Home button or clicks on an
  App Store link, your application will end. The next method called will be the
  applicationWillResignActive: of your UIApplicationDelegate object.Immediately after that,
  nativeAdWillLeaveApplication: is called.

  #### Declaration

  Objective-C

      - (void)nativeAdWillPresentScreen:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html *)nativeAd;

- `


  ### [-nativeAdWillDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdWillDismissScreen:)


  ` Called just before dismissing a full screen view.

  #### Declaration

  Objective-C

      - (void)nativeAdWillDismissScreen:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html *)nativeAd;

- `


  ### [-nativeAdDidDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdDidDismissScreen:)


  ` Called just after dismissing a full screen view. Use this opportunity to restart anything you
  may have stopped as part of nativeAdWillPresentScreen:.

  #### Declaration

  Objective-C

      - (void)nativeAdDidDismissScreen:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html *)nativeAd;

- `


  ### [-nativeAdWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeAdDelegate#/c:objc(pl)GADNativeAdDelegate(im)nativeAdWillLeaveApplication:)


  ` Called just before the application will go to the background or terminate due to an ad action
  that will launch another application (such as the App Store). The normal UIApplicationDelegate
  methods, like applicationDidEnterBackground:, will be called immediately before this.

  #### Declaration

  Objective-C

      - (void)nativeAdWillLeaveApplication:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html *)nativeAd;