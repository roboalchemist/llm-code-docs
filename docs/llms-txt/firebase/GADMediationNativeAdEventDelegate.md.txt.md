# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADMediationNativeAdEventDelegate

    @protocol GADMediationNativeAdEventDelegate <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate.html>

Reports native related information to the Google Mobile Ads SDK from the adapter.
- `


  ### [-didPlayVideo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate#/c:objc(pl)GADMediationNativeAdEventDelegate(im)didPlayVideo)


  ` Notifies Google Mobile Ads SDK that the GADMediationAd started video playback.

  #### Declaration

  Objective-C

      - (void)didPlayVideo;

- `


  ### [-didPauseVideo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate#/c:objc(pl)GADMediationNativeAdEventDelegate(im)didPauseVideo)


  ` Notifies Google Mobile Ads SDK that the GADMediationAd paused video playback.

  #### Declaration

  Objective-C

      - (void)didPauseVideo;

- `


  ### [-didEndVideo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate#/c:objc(pl)GADMediationNativeAdEventDelegate(im)didEndVideo)


  ` Notifies Google Mobile Ads SDK that the GADMediationAd's video playback finished.

  #### Declaration

  Objective-C

      - (void)didEndVideo;

- `


  ### [-didMuteVideo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate#/c:objc(pl)GADMediationNativeAdEventDelegate(im)didMuteVideo)


  ` Notifies Google Mobile Ads SDK that the GADMediationAd muted video playback.

  #### Declaration

  Objective-C

      - (void)didMuteVideo;

- `


  ### [-didUnmuteVideo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate#/c:objc(pl)GADMediationNativeAdEventDelegate(im)didUnmuteVideo)


  ` Notifies Google Mobile Ads SDK that the GADMediationAd unmuted video playback.

  #### Declaration

  Objective-C

      - (void)didUnmuteVideo;

- `


  ### [-willBackgroundApplication](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationNativeAdEventDelegate#/c:objc(pl)GADMediationNativeAdEventDelegate(im)willBackgroundApplication)


  ` Notifies Google Mobile Ads SDK that an action on the GADMediationAd will cause the application
  to move into the background.

  #### Declaration

  Objective-C

      - (void)willBackgroundApplication;