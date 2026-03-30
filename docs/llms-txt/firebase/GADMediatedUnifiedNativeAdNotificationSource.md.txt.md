# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedUnifiedNativeAdNotificationSource

    @interface GADMediatedUnifiedNativeAdNotificationSource : NSObject

Notifies the Google Mobile Ads SDK about the events performed by adapters. Adapters may perform
some action (e.g. opening an in app browser or opening the iTunes store) when handling methods
in GADMediatedUnifiedNativeAd. Adapters in such case should notify the Google Mobile Ads SDK by
calling the relevant methods from this class.
- `


  ### [+mediatedNativeAdDidRecordImpression:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidRecordImpression:)


  ` Called by the adapter when it has registered an impression on the tracked view. Adapter should
  only call this method if -\[GADMAdNetworkAdapter handlesUserImpressions\] returns YES.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdDidRecordImpression:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

- `


  ### [+mediatedNativeAdDidRecordClick:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidRecordClick:)


  ` Called by the adapter when it has registered a user click on the tracked view. Adapter should
  only call this method if -\[GADMAdNetworkAdapter handlesUserClicks\] returns YES.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdDidRecordClick:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

- `


  ### [+mediatedNativeAdWillPresentScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdWillPresentScreen:)


  ` Must be called by the adapter just before mediatedNativeAd has opened an in-app modal screen.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdWillPresentScreen:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

- `


  ### [+mediatedNativeAdWillDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdWillDismissScreen:)


  ` Must be called by the adapter just before the in-app modal screen opened by mediatedNativeAd is
  dismissed.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdWillDismissScreen:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

- `


  ### [+mediatedNativeAdDidDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidDismissScreen:)


  ` Must be called by the adapter after the in-app modal screen opened by mediatedNativeAd is
  dismissed.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdDidDismissScreen:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

- `


  ### [+mediatedNativeAdWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdWillLeaveApplication:)


  ` Must be called by the adapter just before mediatedNativeAd leaves the application.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdWillLeaveApplication:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

[## Mediated Native Video Ad Notifications](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/Mediated%20Native%20Video%20Ad%20Notifications)

- `


  ### [+mediatedNativeAdDidPlayVideo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidPlayVideo:)


  ` Called by the adapter when native video playback has begun or resumed.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdDidPlayVideo:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

- `


  ### [+mediatedNativeAdDidPauseVideo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidPauseVideo:)


  ` Called by the adapter when native video playback has paused.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdDidPauseVideo:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;

- `


  ### [+mediatedNativeAdDidEndVideoPlayback:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediatedUnifiedNativeAdNotificationSource#/c:objc(cs)GADMediatedUnifiedNativeAdNotificationSource(cm)mediatedNativeAdDidEndVideoPlayback:)


  ` Called by the adapter when native video playback has ended.

  #### Declaration

  Objective-C

      + (void)mediatedNativeAdDidEndVideoPlayback:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedNativeAd;