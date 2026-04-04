# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventNativeAdDelegate

    @protocol GADCustomEventNativeAdDelegate <NSObject>

The delegate of the GADCustomEventNativeAd object must adopt the GADCustomEventNativeAdDelegate
protocol. Methods in this protocol are used for native ad's custom event communication with the
Google Mobile Ads SDK.
- `
  ``
  ``
  `

  ### [-customEventNativeAd:didReceiveMediatedNativeAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate#/c:objc(pl)GADCustomEventNativeAdDelegate(im)customEventNativeAd:didReceiveMediatedNativeAd:)

  `
  `  
  Tells the delegate that the custom event ad request succeeded and loaded a native ad.  

  #### Declaration

  Objective-C  

      - (void)customEventNativeAd:
                  (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd.html>)customEventNativeAd
          didReceiveMediatedNativeAd:
              (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>)mediatedNativeAd;

- `
  ``
  ``
  `

  ### [-customEventNativeAd:didFailToLoadWithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate#/c:objc(pl)GADCustomEventNativeAdDelegate(im)customEventNativeAd:didFailToLoadWithError:)

  `
  `  
  Tells the delegate that the custom event ad request failed.  

  #### Declaration

  Objective-C  

      - (void)customEventNativeAd:
                  (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd.html>)customEventNativeAd
           didFailToLoadWithError:(nonnull NSError *)error;

- `
  ``
  ``
  `

  ### [-customEventNativeAd:didReceiveMediatedUnifiedNativeAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAdDelegate#/c:objc(pl)GADCustomEventNativeAdDelegate(im)customEventNativeAd:didReceiveMediatedUnifiedNativeAd:)

  `
  `  
  Tells the delegate that the custom event ad request succeeded and loaded a unified native ad.  

  #### Declaration

  Objective-C  

      - (void)customEventNativeAd:
                  (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventNativeAd.html>)customEventNativeAd
          didReceiveMediatedUnifiedNativeAd:
              (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedUnifiedNativeAd.html>)mediatedUnifiedNativeAd;