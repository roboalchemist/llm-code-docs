# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector.md.txt

# GoogleMobileAds Framework Reference

# GADMAdNetworkConnector

    @protocol GADMAdNetworkConnector <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest.html>

Ad network adapters interact with the mediation SDK using an object that implements the
GADMAdNetworkConnector protocol. The connector object can be used to obtain necessary
information for ad requests, and to call back to the mediation SDK on ad request returns and
user interactions.
- `
  ``
  ``
  `

  ### [-viewControllerForPresentingModalView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)viewControllerForPresentingModalView)

  `
  `  
  When you need to show a landing page or any other modal view, such as when a user clicks or when
  your Ads SDK needs to show an interstitial, use this method to obtain a UIViewController that
  you can use to show your modal view. Call the -presentViewController:animated:completion: method
  of the returned UIViewController.  

  #### Declaration

  Objective-C  

      - (UIViewController *)viewControllerForPresentingModalView;

- `
  ``
  ``
  `

  ### [-adVolume](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adVolume)

  `
  `  
  Returns the preferred ad volume as a fraction of system volume (0.0 to 1.0).  

  #### Declaration

  Objective-C  

      - (float)adVolume;

- `
  ``
  ``
  `

  ### [-adMuted](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adMuted)

  `
  `  
  Returns whether the ad should be muted.  

  #### Declaration

  Objective-C  

      - (BOOL)adMuted;

[## Adapter Callbacks](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/Adapter%20Callbacks)

- `
  ``
  ``
  `

  ### [-adapter:didFailAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didFailAd:)

  `
  `  
  Tells the connector that the adapter failed to receive an ad.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter didFailAd:(NSError *)error;

- `
  ``
  ``
  `

  ### [-adapter:didReceiveAdView:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveAdView:)

  `
  `  
  Tells the connector that the adapter received a banner ad.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter
          didReceiveAdView:(UIView *)view;

- `
  ``
  ``
  `

  ### [-adapterDidReceiveInterstitial:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidReceiveInterstitial:)

  `
  `  
  Tells the connector that the adapter received an interstitial.  

  #### Declaration

  Objective-C  

      - (void)adapterDidReceiveInterstitial:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapter:didReceiveMediatedNativeAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveMediatedNativeAd:)

  `
  `  
  Tells the connector that the adapter has received a mediated native ad. \|mediatedNativeAd\| is
  used by the Google Mobile Ads SDK to construct a native ad object.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter
          didReceiveMediatedNativeAd:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>)mediatedNativeAd;

- `
  ``
  ``
  `

  ### [-adapter:didReceiveMediatedUnifiedNativeAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveMediatedUnifiedNativeAd:)

  `
  `  
  Tells the connector that the adapter has received a unified mediated native ad.
  mediatedUnifiedNativeAd is used by the Google Mobile Ads SDK to construct a unified native ad
  object.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter
          didReceiveMediatedUnifiedNativeAd:
              (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedUnifiedNativeAd;

[## Ad events](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/Ad%20events)

- `
  ``
  ``
  `

  ### [-adapterDidGetAdClick:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidGetAdClick:)

  `
  `  
  Tells the connector that the adapter recorded a user click.  

  #### Declaration

  Objective-C  

      - (void)adapterDidGetAdClick:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillLeaveApplication:)

  `
  `  
  Tells the connector that the adapter will leave the application because of a user action.  

  #### Declaration

  Objective-C  

      - (void)adapterWillLeaveApplication:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterWillPresentFullScreenModal:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillPresentFullScreenModal:)

  `
  `  
  Tells the connector that the adapter will present a full screen modal.  

  #### Declaration

  Objective-C  

      - (void)adapterWillPresentFullScreenModal:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterWillDismissFullScreenModal:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillDismissFullScreenModal:)

  `
  `  
  Tells the connector that the adapter will dismiss a full screen modal.  

  #### Declaration

  Objective-C  

      - (void)adapterWillDismissFullScreenModal:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterDidDismissFullScreenModal:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidDismissFullScreenModal:)

  `
  `  
  Tells the connector that the adapter dismissed a full screen modal.  

  #### Declaration

  Objective-C  

      - (void)adapterDidDismissFullScreenModal:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterWillPresentInterstitial:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillPresentInterstitial:)

  `
  `  
  Tells the connector that the adapter will present an interstitial.  

  #### Declaration

  Objective-C  

      - (void)adapterWillPresentInterstitial:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterWillDismissInterstitial:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillDismissInterstitial:)

  `
  `  
  Tells the connector that the adapter will dismiss an interstitial.  

  #### Declaration

  Objective-C  

      - (void)adapterWillDismissInterstitial:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterDidDismissInterstitial:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidDismissInterstitial:)

  `
  `  
  Tells the connector that the adapter did dismiss an interstitial.  

  #### Declaration

  Objective-C  

      - (void)adapterDidDismissInterstitial:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter;

[## Deprecated](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/Deprecated)

- `
  ``
  ``
  `

  ### [-adapter:didReceiveInterstitial:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveInterstitial:)

  `
  `  
  Deprecated. Use -adapterDidReceiveInterstitial:.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter
          didReceiveInterstitial:(NSObject *)interstitial;

- `
  ``
  ``
  `

  ### [-adapter:clickDidOccurInBanner:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:clickDidOccurInBanner:)

  `
  `  
  Deprecated. Use -adapterDidGetAdClick:.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter
          clickDidOccurInBanner:(UIView *)view;

- `
  ``
  ``
  `

  ### [-adapter:didFailInterstitial:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didFailInterstitial:)

  `
  `  
  Deprecated. Use -adapter:didFailAd:.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html>)adapter
          didFailInterstitial:(NSError *)error;