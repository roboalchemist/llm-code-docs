# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventNativeAdDelegate

    protocol GADCustomEventNativeAdDelegate : NSObjectProtocol

The delegate of the GADCustomEventNativeAd object must adopt the GADCustomEventNativeAdDelegate
protocol. Methods in this protocol are used for native ad's custom event communication with the
Google Mobile Ads SDK.
- `


  ### [customEventNativeAd(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate#/c:objc(pl)GADCustomEventNativeAdDelegate(im)customEventNativeAd:didReceiveMediatedNativeAd:)


  ` Tells the delegate that the custom event ad request succeeded and loaded a native ad.

  #### Declaration

  Swift

      func customEventNativeAd(_ customEventNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd.html, didReceive mediatedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html)

- `


  ### [customEventNativeAd(_:didFailToLoadWithError:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate#/c:objc(pl)GADCustomEventNativeAdDelegate(im)customEventNativeAd:didFailToLoadWithError:)


  ` Tells the delegate that the custom event ad request failed.

  #### Declaration

  Swift

      func customEventNativeAd(_ customEventNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd.html, didFailToLoadWithError error: Error)

- `


  ### [customEventNativeAd(_:didReceive:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate#/c:objc(pl)GADCustomEventNativeAdDelegate(im)customEventNativeAd:didReceiveMediatedUnifiedNativeAd:)


  ` Tells the delegate that the custom event ad request succeeded and loaded a unified native ad.

  #### Declaration

  Swift

      func customEventNativeAd(_ customEventNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd.html, didReceive mediatedUnifiedNativeAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html)