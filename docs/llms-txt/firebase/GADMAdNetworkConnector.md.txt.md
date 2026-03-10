# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector.md.txt

# GoogleMobileAds Framework Reference

# GADMAdNetworkConnector

    protocol GADMAdNetworkConnector : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest.html

Ad network adapters interact with the mediation SDK using an object that implements the
GADMAdNetworkConnector protocol. The connector object can be used to obtain necessary
information for ad requests, and to call back to the mediation SDK on ad request returns and
user interactions.
- `


  ### [viewControllerForPresentingModalView()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)viewControllerForPresentingModalView)


  ` When you need to show a landing page or any other modal view, such as when a user clicks or when
  your Ads SDK needs to show an interstitial, use this method to obtain a UIViewController that
  you can use to show your modal view. Call the -presentViewController:animated:completion: method
  of the returned UIViewController.

  #### Declaration

  Swift

      func viewControllerForPresentingModalView() -> UIViewController!

- `


  ### [adVolume()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adVolume)


  ` Returns the preferred ad volume as a fraction of system volume (0.0 to 1.0).

  #### Declaration

  Swift

      func adVolume() -> Float

- `


  ### [adMuted()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adMuted)


  ` Returns whether the ad should be muted.

  #### Declaration

  Swift

      func adMuted() -> Bool

[## Adapter Callbacks](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/Adapter%20Callbacks)

- `


  ### [adapter(_:didFailAd:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didFailAd:)


  ` Tells the connector that the adapter failed to receive an ad.

  #### Declaration

  Swift

      func adapter(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!, didFailAd error: Error!)

- `


  ### [adapter(_:didReceiveAdView:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveAdView:)


  ` Tells the connector that the adapter received a banner ad.

  #### Declaration

  Swift

      func adapter(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!, didReceiveAdView view: UIView!)

- `


  ### [adapterDidReceiveInterstitial(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidReceiveInterstitial:)


  ` Tells the connector that the adapter received an interstitial.

  #### Declaration

  Swift

      func adapterDidReceiveInterstitial(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapter(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveMediatedNativeAd:)


  ` Tells the connector that the adapter has received a mediated native ad. \|mediatedNativeAd\| is
  used by the Google Mobile Ads SDK to construct a native ad object.

  #### Declaration

  Swift

      func adapter(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!, didReceive mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html!)

- `


  ### [adapter(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveMediatedUnifiedNativeAd:)


  ` Tells the connector that the adapter has received a unified mediated native ad.
  mediatedUnifiedNativeAd is used by the Google Mobile Ads SDK to construct a unified native ad
  object.

  #### Declaration

  Swift

      func adapter(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!, didReceive mediatedUnifiedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html!)

[## Ad events](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/Ad%20events)

- `


  ### [adapterDidGetAdClick(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidGetAdClick:)


  ` Tells the connector that the adapter recorded a user click.

  #### Declaration

  Swift

      func adapterDidGetAdClick(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapterWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillLeaveApplication:)


  ` Tells the connector that the adapter will leave the application because of a user action.

  #### Declaration

  Swift

      func adapterWillLeaveApplication(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapterWillPresentFullScreenModal(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillPresentFullScreenModal:)


  ` Tells the connector that the adapter will present a full screen modal.

  #### Declaration

  Swift

      func adapterWillPresentFullScreenModal(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapterWillDismissFullScreenModal(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillDismissFullScreenModal:)


  ` Tells the connector that the adapter will dismiss a full screen modal.

  #### Declaration

  Swift

      func adapterWillDismissFullScreenModal(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapterDidDismissFullScreenModal(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidDismissFullScreenModal:)


  ` Tells the connector that the adapter dismissed a full screen modal.

  #### Declaration

  Swift

      func adapterDidDismissFullScreenModal(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapterWillPresentInterstitial(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillPresentInterstitial:)


  ` Tells the connector that the adapter will present an interstitial.

  #### Declaration

  Swift

      func adapterWillPresentInterstitial(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapterWillDismissInterstitial(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterWillDismissInterstitial:)


  ` Tells the connector that the adapter will dismiss an interstitial.

  #### Declaration

  Swift

      func adapterWillDismissInterstitial(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

- `


  ### [adapterDidDismissInterstitial(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapterDidDismissInterstitial:)


  ` Tells the connector that the adapter did dismiss an interstitial.

  #### Declaration

  Swift

      func adapterDidDismissInterstitial(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!)

[## Deprecated](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/Deprecated)

- `


  ### [adapter(_:didReceiveInterstitial:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didReceiveInterstitial:)


  ` Deprecated. Use -adapterDidReceiveInterstitial:.

  #### Declaration

  Swift

      func adapter(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!, didReceiveInterstitial interstitial: NSObject!)

- `


  ### [adapter(_:clickDidOccurInBanner:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:clickDidOccurInBanner:)


  ` Deprecated. Use -adapterDidGetAdClick:.

  #### Declaration

  Swift

      func adapter(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!, clickDidOccurInBanner view: UIView!)

- `


  ### [adapter(_:didFailInterstitial:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkConnector#/c:objc(pl)GADMAdNetworkConnector(im)adapter:didFailInterstitial:)


  ` Deprecated. Use -adapter:didFailAd:.

  #### Declaration

  Swift

      func adapter(_ adapter: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMAdNetworkAdapter.html!, didFailInterstitial error: Error!)