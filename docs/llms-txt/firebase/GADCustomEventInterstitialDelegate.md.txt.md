# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventInterstitialDelegate

    @protocol GADCustomEventInterstitialDelegate <NSObject>

Call back to this delegate in your custom event. You must call
customEventInterstitialDidReceiveAd: when there is an ad to show, or
customEventInterstitial:didFailAd: when there is no ad to show. Otherwise, if enough time passed
(several seconds) after the SDK called the requestInterstitialAdWithParameter: method of your
custom event, the mediation SDK will consider the request timed out, and move on to the next ad
network.
- `


  ### [-customEventInterstitialDidReceiveAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialDidReceiveAd:)


  ` Your Custom Event object must call this when it receives or creates an interstitial ad.

  #### Declaration

  Objective-C

      - (void)customEventInterstitialDidReceiveAd:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent;

- `


  ### [-customEventInterstitial:didFailAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitial:didFailAd:)


  ` Your Custom Event object must call this when it fails to receive or create the ad. Pass along
  any error object sent from the ad network's SDK, or an NSError describing the error. Pass nil if
  not available.

  #### Declaration

  Objective-C

      - (void)customEventInterstitial:
                  (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent
                            didFailAd:(nullable NSError *)error;

- `


  ### [-customEventInterstitialWasClicked:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWasClicked:)


  ` Your Custom Event object should call this when the user touches or clicks the ad to initiate
  an action. When the SDK receives this callback, it reports the click back to the mediation
  server.

  #### Declaration

  Objective-C

      - (void)customEventInterstitialWasClicked:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent;

- `


  ### [-customEventInterstitialWillPresent:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWillPresent:)


  ` Your Custom Event should call this when the interstitial is being displayed.

  #### Declaration

  Objective-C

      - (void)customEventInterstitialWillPresent:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent;

- `


  ### [-customEventInterstitialWillDismiss:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWillDismiss:)


  ` Your Custom Event should call this when the interstitial is about to be dismissed.

  #### Declaration

  Objective-C

      - (void)customEventInterstitialWillDismiss:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent;

- `


  ### [-customEventInterstitialDidDismiss:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialDidDismiss:)


  ` Your Custom Event should call this when the interstitial has been dismissed.

  #### Declaration

  Objective-C

      - (void)customEventInterstitialDidDismiss:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent;

- `


  ### [-customEventInterstitialWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitialWillLeaveApplication:)


  ` Your Custom Event should call this method when a user action will result in app switching.

  #### Declaration

  Objective-C

      - (void)customEventInterstitialWillLeaveApplication:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent;

[## Deprecated](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/Deprecated)

- `


  ### [-customEventInterstitial:didReceiveAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitialDelegate#/c:objc(pl)GADCustomEventInterstitialDelegate(im)customEventInterstitial:didReceiveAd:)


  ` Deprecated. Use customEventInterstitialDidReceiveAd:.

  #### Declaration

  Objective-C

      - (void)customEventInterstitial:
                  (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventInterstitial.html>)customEvent
                         didReceiveAd:(nonnull NSObject *)ad;