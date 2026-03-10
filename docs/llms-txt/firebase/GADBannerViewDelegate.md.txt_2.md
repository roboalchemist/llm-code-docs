# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADBannerViewDelegate

    @protocol GADBannerViewDelegate <NSObject>

Delegate methods for receiving GADBannerView state change messages such as ad request status
and ad click lifecycle.
[## Ad Request Lifecycle Notifications](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/Ad%20Request%20Lifecycle%20Notifications)

- `


  ### [-adViewDidReceiveAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewDidReceiveAd:)


  ` Tells the delegate that an ad request successfully received an ad. The delegate may want to add
  the banner view to the view hierarchy if it hasn't been added yet.

  #### Declaration

  Objective-C

      - (void)adViewDidReceiveAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)bannerView;

- `


  ### [-adView:didFailToReceiveAdWithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adView:didFailToReceiveAdWithError:)


  ` Tells the delegate that an ad request failed. The failure is normally due to network
  connectivity or ad availablility (i.e., no fill).

  #### Declaration

  Objective-C

      - (void)adView:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)bannerView
          didFailToReceiveAdWithError:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADRequestError *)error;

[## Click-Time Lifecycle Notifications](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/Click-Time%20Lifecycle%20Notifications)

- `


  ### [-adViewWillPresentScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewWillPresentScreen:)


  ` Tells the delegate that a full screen view will be presented in response to the user clicking on
  an ad. The delegate may want to pause animations and time sensitive interactions.

  #### Declaration

  Objective-C

      - (void)adViewWillPresentScreen:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)bannerView;

- `


  ### [-adViewWillDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewWillDismissScreen:)


  ` Tells the delegate that the full screen view will be dismissed.

  #### Declaration

  Objective-C

      - (void)adViewWillDismissScreen:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)bannerView;

- `


  ### [-adViewDidDismissScreen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewDidDismissScreen:)


  ` Tells the delegate that the full screen view has been dismissed. The delegate should restart
  anything paused while handling adViewWillPresentScreen:.

  #### Declaration

  Objective-C

      - (void)adViewDidDismissScreen:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)bannerView;

- `


  ### [-adViewWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADBannerViewDelegate#/c:objc(pl)GADBannerViewDelegate(im)adViewWillLeaveApplication:)


  ` Tells the delegate that the user click will open another app, backgrounding the current
  application. The standard UIApplicationDelegate methods, like applicationDidEnterBackground:,
  are called immediately before this method is called.

  #### Declaration

  Objective-C

      - (void)adViewWillLeaveApplication:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADBannerView.html *)bannerView;