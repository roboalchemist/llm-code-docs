# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADNativeExpressAdViewDelegate

    @protocol GADNativeExpressAdViewDelegate <NSObject>

Delegate methods for receiving GADNativeExpressAdView state change messages such as ad request
status and ad click lifecycle.
[## Ad Request Lifecycle Notifications](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/Ad%20Request%20Lifecycle%20Notifications)

- `


  ### [-nativeExpressAdViewDidReceiveAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewDidReceiveAd:)


  ` Tells the delegate that the native express ad view successfully received an ad. The delegate may
  want to add the native express ad view to the view hierarchy if it hasn't been added yet.

  #### Declaration

  Objective-C

      - (void)nativeExpressAdViewDidReceiveAd:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html *)nativeExpressAdView;

- `


  ### [-nativeExpressAdView:didFailToReceiveAdWithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdView:didFailToReceiveAdWithError:)


  ` Tells the delegate that an ad request failed. The failure is normally due to network
  connectivity or ad availablility (i.e., no fill).

  #### Declaration

  Objective-C

      - (void)nativeExpressAdView:
                  (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html *)nativeExpressAdView
          didFailToReceiveAdWithError:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADRequestError *)error;

[## Click-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/Click-Time%20Lifecycle%20Notifications)

- `


  ### [-nativeExpressAdViewWillPresentScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewWillPresentScreen:)


  ` Tells the delegate that a full screen view will be presented in response to the user clicking on
  an ad. The delegate may want to pause animations and time sensitive interactions.

  #### Declaration

  Objective-C

      - (void)nativeExpressAdViewWillPresentScreen:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html *)nativeExpressAdView;

- `


  ### [-nativeExpressAdViewWillDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewWillDismissScreen:)


  ` Tells the delegate that the full screen view will be dismissed.

  #### Declaration

  Objective-C

      - (void)nativeExpressAdViewWillDismissScreen:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html *)nativeExpressAdView;

- `


  ### [-nativeExpressAdViewDidDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewDidDismissScreen:)


  ` Tells the delegate that the full screen view has been dismissed. The delegate should restart
  anything paused while handling adViewWillPresentScreen:.

  #### Declaration

  Objective-C

      - (void)nativeExpressAdViewDidDismissScreen:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html *)nativeExpressAdView;

- `


  ### [-nativeExpressAdViewWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADNativeExpressAdViewDelegate#/c:objc(pl)GADNativeExpressAdViewDelegate(im)nativeExpressAdViewWillLeaveApplication:)


  ` Tells the delegate that the user click will open another app, backgrounding the current
  application. The standard UIApplicationDelegate methods, like applicationDidEnterBackground:,
  are called immediately before this method is called.

  #### Declaration

  Objective-C

      - (void)nativeExpressAdViewWillLeaveApplication:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeExpressAdView.html *)nativeExpressAdView;